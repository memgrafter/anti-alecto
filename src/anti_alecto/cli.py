"""anti-alecto CLI — tame the tab fury."""

import argparse
import asyncio
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from .config import Config
from .db import Store
from .ingest import extract_domain, fetch_page_title, normalize_url
from .policy import classify_skip_status, dedupe_prefix, is_walled_reason

# Resolve paths relative to project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
DUMPS_DIR = PROJECT_ROOT / "dumps"
DIGESTS_DIR = PROJECT_ROOT / "digests"
DIGESTS_RAW_DIR = DIGESTS_DIR / "raw"
DEFAULT_DB = PROJECT_ROOT / "anti-alecto.db"


def get_store() -> Store:
    return Store(DEFAULT_DB)


def get_config() -> Config:
    return Config(PROJECT_ROOT / "config.yml")


# ── Commands ──


def cmd_ingest(args: argparse.Namespace) -> int:
    """Import chrome tab dumps."""
    config = get_config()

    with get_store() as store:
        if args.file:
            from .ingest import ingest_dump

            path = Path(args.file).expanduser()
            if not path.exists():
                print(f"File not found: {path}", file=sys.stderr)
                return 1
            result = ingest_dump(path, store, config)
            _print_ingest_result(result)
        else:
            from .ingest import ingest_all

            if not DUMPS_DIR.exists():
                print(f"No dumps directory: {DUMPS_DIR}", file=sys.stderr)
                return 1
            results = ingest_all(DUMPS_DIR, store, config)
            if not results:
                print("No new dumps to import.")
            else:
                for r in results:
                    _print_ingest_result(r)
                total_new = sum(r["new"] for r in results)
                print(f"\nTotal: {total_new} new URLs from {len(results)} dumps")

    return 0


def _print_ingest_result(r: dict) -> None:
    if r.get("already_imported"):
        print(f"  {r['filename']}: already imported")
    else:
        print(
            f"  {r['filename']}: {r['tab_count']} tabs → "
            f"{r['new']} new, {r['skipped_pattern']} skipped, "
            f"{r['skipped_dupe']} dupes"
        )


def cmd_add(args: argparse.Namespace) -> int:
    """Add a single URL directly, with optional end-to-end processing."""
    url = (args.url or "").strip()
    title = (args.title or "").strip()
    if not url:
        print("URL is required.", file=sys.stderr)
        return 1

    config = get_config()

    with get_store() as store:
        url_norm = normalize_url(url, config.tracking_params)
        row = store.get_url_by_normalized(url_norm)

        if row:
            print(f"Already in corpus: id={row['id']} status={row['status']} url={row['url']}")
        else:
            # Fetch page title if not provided
            has_title = bool(title)
            if not title:
                fetched_title = fetch_page_title(url)
                if fetched_title:
                    title = fetched_title
                    has_title = True

            should_skip, reason = config.should_skip(url)
            if should_skip:
                status = classify_skip_status(url, reason)
                new_id = store.add_url(
                    url=url,
                    url_normalized=url_norm,
                    title=title,
                    domain=extract_domain(url),
                    dump_id=None,
                    status=status,
                    triage_reason=reason,
                )
                row = store.get_url_by_id(new_id) if new_id else store.get_url_by_normalized(url_norm)
                print(f"Added id={row['id']} as {status}: {reason}")
            else:
                prefix = dedupe_prefix(url_norm)
                blocker = store.find_walled_prefix_match_any(prefix)
                if blocker:
                    src_reason = (
                        blocker.get("scrape_failed_reason")
                        or blocker.get("triage_reason")
                        or blocker.get("status")
                        or "walled content"
                    )
                    print(
                        f"Skipped add: prefix dedupe blocked by id={blocker['id']} "
                        f"({blocker.get('status')}): {src_reason}"
                    )
                    return 0

                # No title → skip triage, go straight to scrape
                add_status = "pending" if has_title else "triaged_keep"
                new_id = store.add_url(
                    url=url,
                    url_normalized=url_norm,
                    title=title,
                    domain=extract_domain(url),
                    dump_id=None,
                    status=add_status,
                )
                if new_id is None:
                    row = store.get_url_by_normalized(url_norm)
                    print(f"Already in corpus: id={row['id']} status={row['status']} url={row['url']}")
                else:
                    row = store.get_url_by_id(new_id)
                    print(f"Added id={new_id} as {add_status}")

        if getattr(args, "no_process", False):
            return 0

        # Process just this row end-to-end.
        current = store.get_url_by_id(row["id"]) or row
        status = current.get("status")

        if status == "pending":
            interest_profile = config.get("triage.interest_profile", "")
            try:
                _triage_batch(store, [current], interest_profile)
            except RuntimeError as exc:
                print(str(exc), file=sys.stderr)
                return 1
            current = store.get_url_by_id(row["id"]) or current
            status = current.get("status")

        if status == "triaged_keep":
            success, skipped, failed = _scrape_batch(store, [current], config)
            print(f"\nDone: {success} scraped, {skipped} skipped, {failed} failed")
            current = store.get_url_by_id(row["id"]) or current
            status = current.get("status")

        print(f"Final status: id={current['id']} status={status} url={current['url']}")

    return 0


def cmd_triage(args: argparse.Namespace) -> int:
    """Triage pending URLs."""
    config = get_config()
    batch_size = config.get("triage.batch_size", 30)
    all_mode = bool(getattr(args, "all", False))

    with get_store() as store:
        interest_profile = config.get("triage.interest_profile", "")

        if not all_mode:
            pending = store.get_urls_by_status("pending", limit=batch_size)
            if not pending:
                print("No pending URLs to triage.")
                return 0
            try:
                _triage_batch(store, pending, interest_profile)
            except RuntimeError as exc:
                print(str(exc), file=sys.stderr)
                return 1
            return 0

        total_processed = 0

        # Repeat until queue is at or below one batch.
        while len(store.get_urls_by_status("pending")) > batch_size:
            pending = store.get_urls_by_status("pending", limit=batch_size)
            if not pending:
                break
            try:
                processed = _triage_batch(store, pending, interest_profile)
            except RuntimeError as exc:
                print(str(exc), file=sys.stderr)
                return 1
            if processed < 1:
                print("Triage aborted: processed 0 URLs in batch.", file=sys.stderr)
                return 1
            total_processed += processed

        # Final single pass when pending <= batch_size.
        pending = store.get_urls_by_status("pending", limit=batch_size)
        if not pending:
            if total_processed == 0:
                print("No pending URLs to triage.")
            return 0

        try:
            processed = _triage_batch(store, pending, interest_profile)
        except RuntimeError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        if processed < 1:
            print("Triage aborted: processed 0 URLs in batch.", file=sys.stderr)
            return 1

    return 0


def _triage_batch(store: Store, pending: list[dict], interest_profile: str) -> int:
    """Run one triage batch and persist decisions. Returns processed count."""
    print(f"Triaging {len(pending)} URLs...")

    urls_batch = [{"url": u["url"], "title": u["title"]} for u in pending]
    result = asyncio.run(_run_triage_machine(urls_batch, interest_profile))

    if "error" in result:
        raise RuntimeError(f"Triage failed: {result['error']}")

    decisions = _coerce_triage_decisions(result.get("decisions", []))
    if not decisions:
        raise RuntimeError("Triage produced no parseable decisions.")

    # Build URL→decision map
    decision_map = {}
    for d in decisions:
        url = d.get("url", "")
        decision_map[url] = d

    # Apply decisions
    keep = skip = defer = unmatched = 0
    for u in pending:
        d = decision_map.get(u["url"])
        if not d:
            unmatched += 1
            continue

        action = d.get("action", "").lower()
        reason = d.get("reason", "")

        if action == "keep":
            store.update_url_status(u["id"], "triaged_keep", triage_reason=reason)
            keep += 1
        elif action == "skip":
            status = classify_skip_status(u["url"], reason)
            store.update_url_status(u["id"], status, triage_reason=reason)
            skip += 1
        elif action == "defer":
            store.update_url_status(u["id"], "triaged_defer", triage_reason=reason)
            defer += 1

    print(f"  keep: {keep}  skip: {skip}  defer: {defer}  unmatched: {unmatched}")
    return keep + skip + defer


async def _run_triage_machine(urls: list[dict], interest_profile: str) -> dict:
    from flatmachines import FlatMachine
    from .hooks import TriageHooks

    machine_file = PROJECT_ROOT / "machines" / "triage.yml"
    hooks = TriageHooks()
    machine = FlatMachine(config_file=str(machine_file), hooks=hooks)
    return await machine.execute(input={"urls": urls, "interest_profile": interest_profile})


def _coerce_triage_decisions(raw: object) -> list[dict]:
    """Normalize machine output into list[{'url','action','reason'}]."""
    import ast
    import re

    parsed = raw

    if isinstance(parsed, str):
        text = parsed.strip()
        if not text:
            return []

        # Strip optional markdown fences
        if text.startswith("```"):
            text = re.sub(r"^```\w*\n?", "", text)
            text = re.sub(r"\n?```$", "", text)
            text = text.strip()

        try:
            parsed = json.loads(text)
        except Exception:
            match = re.search(r"\[.*\]", text, re.DOTALL)
            if match:
                try:
                    parsed = json.loads(match.group(0))
                except Exception:
                    parsed = text
            try:
                if isinstance(parsed, str):
                    parsed = ast.literal_eval(text)
            except Exception:
                parsed = []

    if isinstance(parsed, dict):
        parsed = [parsed]

    if not isinstance(parsed, list):
        return []

    cleaned: list[dict] = []
    for item in parsed:
        if not isinstance(item, dict):
            continue
        url = str(item.get("url", "") or "").strip()
        action = str(item.get("action", "") or "").strip().lower()
        reason = str(item.get("reason", "") or "").strip()
        if not url or action not in {"keep", "skip", "defer"}:
            continue
        cleaned.append({"url": url, "action": action, "reason": reason})

    return cleaned


def cmd_scrape(args: argparse.Namespace) -> int:
    """Scrape triaged-keep URLs."""
    config = get_config()
    limit = args.limit or 1
    all_mode = bool(getattr(args, "all", False))

    with get_store() as store:
        if not all_mode:
            urls = store.get_urls_by_status("triaged_keep", limit=limit)
            if not urls:
                print("No URLs ready to scrape.")
                return 0
            success, skipped, failed = _scrape_batch(store, urls, config)
            print(f"\nDone: {success} scraped, {skipped} skipped, {failed} failed")
            return 0

        total_success = total_skipped = total_failed = 0
        while True:
            urls = store.get_urls_by_status("triaged_keep", limit=limit)
            if not urls:
                if total_success == 0 and total_skipped == 0 and total_failed == 0:
                    print("No URLs ready to scrape.")
                break
            success, skipped, failed = _scrape_batch(store, urls, config)
            total_success += success
            total_skipped += skipped
            total_failed += failed

        print(f"\nDone: {total_success} scraped, {total_skipped} skipped, {total_failed} failed")

    return 0


def _scrape_batch(store: Store, urls: list[dict], config: Config) -> tuple[int, int, int]:
    """Run one scrape batch. Returns (success, skipped, failed)."""
    print(f"Scraping {len(urls)} URLs...")

    success = failed = skipped = 0
    for u in urls:
        print(f"\n  → {u['title'][:60]}")
        print(f"    {u['url']}")

        # Avoid duplicate re-scrapes for the same canonical URL.
        dup = store.find_terminal_duplicate_by_normalized(u["id"], u.get("url_normalized", ""))
        if dup:
            src_reason = (
                dup.get("scrape_failed_reason")
                or dup.get("triage_reason")
                or dup.get("status")
                or "already processed"
            )
            duplicate_status = "ineligible" if (dup.get("status") == "ineligible" or is_walled_reason(src_reason)) else "triaged_skip"
            reason = f"duplicate of id={dup['id']} ({dup.get('status')}): {src_reason}"[:200]
            store.update_url_status(u["id"], duplicate_status, triage_reason=reason)
            print(f"    ↷ skipped duplicate: {reason}")
            skipped += 1
            continue

        # Avoid re-scraping under prefixes already known to be walled/paywalled.
        prefix = dedupe_prefix(u["url"])
        blocker = store.find_walled_prefix_match(u["id"], prefix)
        if blocker:
            src_reason = (
                blocker.get("scrape_failed_reason")
                or blocker.get("triage_reason")
                or blocker.get("status")
                or "walled content"
            )
            reason = f"dedupe blocked prefix ({prefix}) via id={blocker['id']}: {src_reason}"[:200]
            store.update_url_status(u["id"], "ineligible", triage_reason=reason)
            print(f"    ↷ ineligible duplicate: {reason}")
            skipped += 1
            continue

        store.update_url_status(u["id"], "scraping")

        result = asyncio.run(
            _run_scrape_machine(u, config)
        )

        if "error" in result:
            full_reason = str(result["error"])
            if full_reason.startswith("SKIP_"):
                reason = full_reason.split(":", 1)[1].strip() if ":" in full_reason else full_reason
                reason = reason[:200]
                status = "ineligible" if full_reason.startswith("SKIP_INELIGIBLE:") else "triaged_skip"
                store.update_url_status(
                    u["id"], status, triage_reason=reason
                )
                print(f"    ↷ skipped: {reason}")
                skipped += 1
                continue

            reason = full_reason[:200]
            store.update_url_status(
                u["id"], "scrape_failed", scrape_failed_reason=reason
            )
            print(f"    ✗ {reason}")
            failed += 1
            continue

        raw_text = result.get("raw_content", "")
        word_count = int(result.get("word_count", 0) or 0)
        strategy = result.get("scrape_strategy", "unknown")
        diagnostics_json = result.get("scrape_diagnostics_json", "[]")
        details_json = result.get("scrape_details_json", "{}")
        summary_md = result.get("summary", "")
        frontmatter_yaml = result.get("frontmatter_yaml", "")
        fm = _parse_frontmatter(frontmatter_yaml)
        scraped_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        # Use title from scrape machine if generated (e.g. by summarizer)
        effective_title = u.get("title") or result.get("title") or ""
        if not u.get("title") and result.get("title"):
            store.update_url_title(u["id"], result["title"])

        try:
            summary_file = _write_archive_files(
                url=u["url"],
                title=effective_title,
                scraped_at=scraped_at,
                word_count=word_count,
                raw_text=raw_text,
                summary_md=summary_md,
                frontmatter=fm,
            )
        except Exception as exc:
            reason = f"artifact write failed: {exc}"[:200]
            store.update_url_status(
                u["id"], "scrape_failed", scrape_failed_reason=reason
            )
            print(f"    ✗ {reason}")
            failed += 1
            continue

        # Keep DB light: store only pointer to summary artifact, not summary/raw payloads.
        store.save_summary(
            url_id=u["id"],
            summary_md=summary_file,
            frontmatter_json=None,
            tldr=None,
            tags=None,
            content_type=None,
            durability=None,
            reference_style=None,
        )

        store.update_url_status(
            u["id"], "summarized", scrape_strategy=strategy
        )
        print(f"    ✓ {word_count} words ({strategy})")
        print(f"    saved: {summary_file}")

        ref_msg = _queue_outbound_reference(store, config, source_row=u, scrape_details_json=details_json)
        if ref_msg:
            print(f"    ↳ queued reference: {ref_msg}")

        try:
            attempts = json.loads(diagnostics_json)
            if len(attempts) > 1:
                def _fmt_attempt(a: dict) -> str:
                    status = "ok" if a.get("success") else (a.get("reason") or "fail")
                    src = a.get("source_url")
                    if src:
                        return f"{a.get('strategy')}:{status} ({src})"
                    return f"{a.get('strategy')}:{status}"

                pretty = " -> ".join(_fmt_attempt(a) for a in attempts)
                print(f"    diagnostics: {pretty}")
        except Exception:
            pass
        success += 1

    return success, skipped, failed


def _queue_outbound_reference(store: Store, config: Config, *, source_row: dict, scrape_details_json: str) -> str:
    """Create/queue referenced target URL rows discovered while scraping source_row."""
    from urllib.parse import urlparse

    try:
        details = json.loads(scrape_details_json or "{}")
    except Exception:
        return ""

    if not isinstance(details, dict):
        return ""

    target_url = str(details.get("outbound_url") or "").strip()
    if not target_url:
        return ""

    parsed = urlparse(target_url)
    if parsed.scheme not in {"http", "https"}:
        return ""

    target_norm = normalize_url(target_url, config.tracking_params)
    source_norm = source_row.get("url_normalized") or normalize_url(source_row.get("url", ""), config.tracking_params)
    if target_norm and source_norm and target_norm == source_norm:
        return ""

    ref_type = str(details.get("reference_type") or "outbound").strip() or "outbound"

    target_row = store.get_url_by_normalized(target_norm)
    if target_row is None:
        target_id = store.add_url(
            url=target_url,
            url_normalized=target_norm,
            title=target_url,
            domain=extract_domain(target_url),
            status="triaged_keep",
            triage_reason=f"queued from {ref_type} reference of id={source_row['id']}",
        )
        if target_id is None:
            target_row = store.get_url_by_normalized(target_norm)
        else:
            target_row = store.get_url_by_id(target_id)
    else:
        if target_row.get("status") in {"pending", "triaged_defer", "triaged_skip", "scrape_failed"}:
            store.update_url_status(
                target_row["id"],
                "triaged_keep",
                triage_reason=f"retry from {ref_type} reference of id={source_row['id']}",
            )
            target_row = store.get_url_by_id(target_row["id"])

    if not target_row:
        return ""

    store.add_url_reference(source_row["id"], target_row["id"], ref_type=ref_type)
    return f"id={target_row['id']} {target_row['url']} ({ref_type})"


async def _run_scrape_machine(url_row: dict, config: Config) -> dict:
    from flatmachines import FlatMachine
    from .hooks import ScrapeHooks

    machine_file = PROJECT_ROOT / "machines" / "scrape.yml"
    hooks = ScrapeHooks()
    machine = FlatMachine(config_file=str(machine_file), hooks=hooks)
    return await machine.execute(input={
        "url": url_row["url"],
        "title": url_row["title"],
        "timeout_seconds": config.get("scrape.timeout_seconds", 30),
        "playwright_wait_ms": config.get("scrape.playwright_wait_ms", 3000),
        "min_content_length": config.get("scrape.min_content_length", 200),
        "cache_ttl_hours": config.get("scrape.cache_ttl_hours", 24),
    })


def _parse_frontmatter(yaml_str: str) -> dict:
    """Parse frontmatter YAML, stripping code fences if present."""
    import re
    import yaml

    clean = yaml_str.strip()
    if clean.startswith("```"):
        clean = re.sub(r"^```\w*\n?", "", clean)
        clean = re.sub(r"\n?```$", "", clean)
    try:
        return yaml.safe_load(clean) or {}
    except yaml.YAMLError:
        return {}


def _slugify(text: str) -> str:
    import re

    slug = (text or "untitled").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug[:80] or "untitled"


def _write_archive_files(
    *,
    url: str,
    title: str,
    scraped_at: str,
    word_count: int,
    raw_text: str,
    summary_md: str,
    frontmatter: dict,
) -> str:
    """Write raw + summary artifacts and return summary file path relative to project root."""
    import hashlib
    import yaml

    DIGESTS_DIR.mkdir(parents=True, exist_ok=True)
    DIGESTS_RAW_DIR.mkdir(parents=True, exist_ok=True)

    date_prefix = (scraped_at or "")[:10] or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    title_slug = _slugify(title)
    url_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    stem = f"{date_prefix}_{title_slug}_{url_hash}"

    raw_rel = Path("digests") / "raw" / f"{stem}.txt"
    summary_rel = Path("digests") / f"{stem}.md"
    raw_abs = PROJECT_ROOT / raw_rel
    summary_abs = PROJECT_ROOT / summary_rel

    raw_abs.write_text(raw_text or "", encoding="utf-8")

    payload = {
        "url": url,
        "title": title,
        "scraped_at": scraped_at,
        "word_count": int(word_count or 0),
        "raw_file": f"raw/{raw_abs.name}",
    }

    for k in [
        "tldr",
        "key_quote",
        "durability",
        "content_type",
        "density",
        "originality",
        "reference_style",
        "scrape_quality",
        "people",
        "tools",
        "libraries",
        "companies",
        "tags",
    ]:
        if k in frontmatter:
            payload[k] = frontmatter[k]

    yaml_text = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=1000).strip()
    summary_abs.write_text(f"---\n{yaml_text}\n---\n\n{(summary_md or '').strip()}\n", encoding="utf-8")

    return str(summary_rel)


def _extract_tldr(summary_ref: str, fallback_summary_md: str | None = None) -> str | None:
    """Resolve TL;DR from a summary artifact path or legacy inline markdown."""
    import re

    text = ""
    if summary_ref:
        p = Path(summary_ref)
        if not p.is_absolute():
            p = PROJECT_ROOT / p
        if p.exists() and p.is_file():
            try:
                text = p.read_text(encoding="utf-8")
            except OSError:
                text = ""

    if not text:
        text = fallback_summary_md or ""

    if not text:
        return None

    # Parse frontmatter tldr first.
    if text.startswith("---\n"):
        try:
            end = text.find("\n---\n", 4)
            if end != -1:
                import yaml

                fm = yaml.safe_load(text[4:end]) or {}
                if isinstance(fm, dict) and fm.get("tldr"):
                    return str(fm.get("tldr"))
                text = text[end + 5 :]
        except Exception:
            pass

    m = re.search(r"^###\s*TL;DR\s*\n+(.+?)(?=\n###|\Z)", text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip()

    return None


def cmd_status(args: argparse.Namespace) -> int:
    """Show pipeline stats."""
    with get_store() as store:
        counts = store.status_counts()
        total = store.total_urls()
        summaries = store.total_summaries()

        print(f"anti-alecto pipeline")
        print(f"{'─' * 30}")
        for status, n in sorted(counts.items()):
            print(f"  {status:<25} {n:>4}")
        print(f"{'─' * 30}")
        print(f"  {'total':<25} {total:>4}")
        print(f"  {'summaries':<25} {summaries:>4}")

    return 0


def cmd_run(args: argparse.Namespace) -> int:
    """Full pipeline: ingest → triage → scrape."""
    print("── ingest ──")
    ret = cmd_ingest(argparse.Namespace(file=None))
    if ret != 0:
        return ret

    print("\n── triage ──")
    ret = cmd_triage(argparse.Namespace())
    if ret != 0:
        return ret

    print("\n── scrape ──")
    ret = cmd_scrape(argparse.Namespace(limit=args.limit if hasattr(args, "limit") else 10))
    return ret


def cmd_search(args: argparse.Namespace) -> int:
    """Search summaries."""
    with get_store() as store:
        results = store.search_summaries(args.query, limit=args.limit or 20)
        if not results:
            print("No results.")
            return 0

        for r in results:
            print(f"\n  {r['title']}")
            print(f"  {r['url']}")
            tldr = r.get("tldr") or _extract_tldr(r.get("summary_md", ""), r.get("summary_md", ""))
            if tldr:
                print(f"  → {tldr}")
            if r.get("tags"):
                print(f"  [{r['tags']}]")

    return 0


def cmd_digest(args: argparse.Namespace) -> int:
    """Show recent summaries and persist digest to digests/."""
    with get_store() as store:
        results = store.recent_summaries(limit=args.limit or 10)
        if not results:
            print("No summaries yet.")
            return 0

        lines: list[str] = []
        for r in results:
            lines.append(f"\n  {r['title']}")
            lines.append(f"  {r['domain']}  {r['created_at'][:10]}")
            tldr = r.get("tldr") or _extract_tldr(r.get("summary_md", ""), r.get("summary_md", ""))
            if tldr:
                lines.append(f"  → {tldr}")

        output = "\n".join(lines)
        print(output)

        DIGESTS_DIR.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")
        out_path = DIGESTS_DIR / f"digest_{stamp}.txt"
        try:
            out_path.write_text(output + "\n", encoding="utf-8")
            print(f"\nSaved digest: {out_path}")
        except OSError as exc:
            print(f"Failed to write digest file: {exc}", file=sys.stderr)
            return 1

    return 0


def cmd_failed(args: argparse.Namespace) -> int:
    """Show failed scrapes."""
    with get_store() as store:
        results = store.failed_scrapes()
        if not results:
            print("No failures.")
            return 0

        for r in results:
            print(f"  {r['title'][:60]}")
            print(f"  {r['url']}")
            print(f"  reason: {r.get('scrape_failed_reason', '?')}")
            print()

    return 0


def cmd_retry(args: argparse.Namespace) -> int:
    """Reset failed scrapes back to triaged_keep for retry."""
    with get_store() as store:
        failed = store.get_urls_by_status("scrape_failed")
        if not failed:
            print("No failed scrapes to retry.")
            return 0

        for u in failed:
            store.update_url_status(u["id"], "triaged_keep")

        print(f"Reset {len(failed)} URLs for retry.")

    return 0


def _is_blocked_like_failure(reason: str | None) -> bool:
    r = (reason or "").lower()
    return (
        "captcha" in r
        or "cloudflare" in r
        or "login wall" in r
        or "access denied" in r
        or "http 403" in r
        or "paywall" in r
    )


def _collect_multiline_input(end_marker: str = "::end") -> str:
    print(f"Paste content below. End input with a line containing only '{end_marker}'.")
    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == end_marker:
            break
        lines.append(line)
    return "\n".join(lines).strip()


def _extract_text_from_image(image_path: Path) -> tuple[str, str]:
    """Best-effort OCR using local tesseract if available."""
    tesseract = shutil.which("tesseract")
    if not tesseract:
        return "", "manual_image_no_ocr"

    try:
        proc = subprocess.run(
            [tesseract, str(image_path), "stdout"],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (subprocess.SubprocessError, OSError):
        return "", "manual_image_no_ocr"

    text = (proc.stdout or "").strip()
    if not text:
        return "", "manual_image_no_ocr"
    return text, "manual_image_ocr"


def _resolve_or_create_manual_row(
    store: Store,
    config: Config,
    *,
    url: str,
    title: str,
) -> dict:
    norm = normalize_url(url, config.tracking_params)
    row = store.get_url_by_normalized(norm)
    if row:
        return row

    new_id = store.add_url(
        url=url,
        url_normalized=norm,
        title=title or url,
        domain=extract_domain(url),
        status="triaged_keep",
        triage_reason="manual capture",
    )
    if new_id:
        row = store.get_url_by_id(new_id)
    else:
        row = store.get_url_by_normalized(norm)

    if not row:
        raise RuntimeError("Failed to create or resolve URL row for manual capture")
    return row


async def _run_manual_summarize_machine(url: str, title: str, raw_content: str, strategy: str) -> dict:
    from flatmachines import FlatMachine
    from .hooks import ScrapeHooks

    machine_file = PROJECT_ROOT / "machines" / "manual_summarize.yml"
    hooks = ScrapeHooks()
    machine = FlatMachine(config_file=str(machine_file), hooks=hooks)
    return await machine.execute(
        input={
            "url": url,
            "title": title,
            "raw_content": raw_content,
            "word_count": len(raw_content.split()),
            "scrape_strategy": strategy,
            "scrape_diagnostics_json": "[]",
        }
    )


def _manual_capture_and_store(
    store: Store,
    *,
    row: dict,
    raw_text: str,
    strategy: str,
    title_override: str | None = None,
) -> str:
    content = (raw_text or "").strip()
    if len(content) < 20:
        raise RuntimeError("Manual content too short; paste more text.")

    title = (title_override or row.get("title") or row.get("url") or "").strip()
    result = asyncio.run(
        _run_manual_summarize_machine(row["url"], title, content, strategy)
    )

    if "error" in result:
        raise RuntimeError(str(result["error"]))

    summary_md = result.get("summary", "")
    frontmatter_yaml = result.get("frontmatter_yaml", "")
    fm = _parse_frontmatter(frontmatter_yaml)
    scraped_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    summary_file = _write_archive_files(
        url=row["url"],
        title=title,
        scraped_at=scraped_at,
        word_count=len(content.split()),
        raw_text=content,
        summary_md=summary_md,
        frontmatter=fm,
    )

    store.save_summary(
        url_id=row["id"],
        summary_md=summary_file,
        frontmatter_json=None,
        tldr=None,
        tags=None,
        content_type=None,
        durability=None,
        reference_style=None,
    )
    store.update_url_status(
        row["id"],
        "summarized",
        scrape_strategy=strategy,
        scrape_failed_reason="",
    )
    return summary_file


def cmd_paste(args: argparse.Namespace) -> int:
    """Manually capture content for a URL (paste-first, optional playwriter-tagged mode)."""
    config = get_config()

    with get_store() as store:
        if args.id:
            row = store.get_url_by_id(args.id)
            if not row:
                print(f"URL id not found: {args.id}", file=sys.stderr)
                return 1
            if args.url and args.url != row.get("url"):
                print("--url ignored when --id is provided", file=sys.stderr)
            url = row["url"]
            title = args.title or row.get("title") or url
        else:
            if not args.url:
                print("Provide --url (or use --id).", file=sys.stderr)
                return 1
            url = args.url
            title = args.title or args.url
            row = _resolve_or_create_manual_row(store, config, url=url, title=title)

        chunks: list[str] = []
        strategy = "manual_playwriter" if args.capture_mode == "playwriter" else "manual_paste"

        if args.file:
            p = Path(args.file).expanduser()
            if not p.exists():
                print(f"File not found: {p}", file=sys.stderr)
                return 1
            chunks.append(p.read_text(encoding="utf-8", errors="replace"))

        if args.image:
            ip = Path(args.image).expanduser()
            if not ip.exists():
                print(f"Image not found: {ip}", file=sys.stderr)
                return 1
            ocr_text, ocr_strategy = _extract_text_from_image(ip)
            strategy = ocr_strategy
            if ocr_text:
                chunks.append(f"[Image OCR from {ip.name}]\n\n{ocr_text}")
            else:
                chunks.append(f"[Image provided: {ip}. OCR unavailable; paste notes below.]")

        needs_stdin = args.stdin or (not args.file and not args.image)
        if needs_stdin:
            if sys.stdin.isatty():
                pasted = _collect_multiline_input(end_marker=args.end_marker)
            else:
                pasted = sys.stdin.read().strip()
            if pasted:
                chunks.append(pasted)

        raw_text = "\n\n".join(c for c in chunks if c and c.strip()).strip()
        if not raw_text:
            print("No manual content provided.", file=sys.stderr)
            return 1

        try:
            summary_file = _manual_capture_and_store(
                store,
                row=row,
                raw_text=raw_text,
                strategy=strategy,
                title_override=title,
            )
        except RuntimeError as exc:
            print(f"Manual summarize failed: {exc}", file=sys.stderr)
            return 1

        print(f"✓ manual capture summarized ({strategy})")
        print(f"  {url}")
        print(f"  saved: {summary_file}")

    return 0


def cmd_rescue(args: argparse.Namespace) -> int:
    """Interactive manual rescue queue for blocked failures."""
    config = get_config()

    with get_store() as store:
        rows: list[dict]
        if args.id:
            row = store.get_url_by_id(args.id)
            if not row:
                print(f"URL id not found: {args.id}", file=sys.stderr)
                return 1
            rows = [row]
        else:
            rows = store.get_urls_by_status("scrape_failed")

        if not args.all:
            rows = [r for r in rows if _is_blocked_like_failure(r.get("scrape_failed_reason"))]

        if args.limit is not None:
            rows = rows[: max(0, args.limit)]

        if not rows:
            print("No rescue candidates.")
            return 0

        capture_strategy = "manual_playwriter" if args.capture_mode == "playwriter" else "manual_paste"
        print(f"Manual rescue queue: {len(rows)} URLs (capture mode: {args.capture_mode})")
        for i, row in enumerate(rows, start=1):
            print(f"\n[{i}/{len(rows)}] {row.get('title','')[:80]}")
            print(f"  id: {row['id']}")
            print(f"  url: {row['url']}")
            print(f"  failed: {row.get('scrape_failed_reason','')}" )

            if args.open:
                try:
                    subprocess.run(["open", row["url"]], check=False)
                except OSError:
                    pass

            while True:
                try:
                    action = input("Action [p=paste, s=skip, i=ineligible, d=defer, q=quit] (default p): ").strip().lower() or "p"
                except EOFError:
                    return 0

                if action == "q":
                    return 0

                if action == "s":
                    store.update_url_status(
                        row["id"],
                        "triaged_skip",
                        triage_reason="manual rescue: skipped",
                        scrape_failed_reason="",
                    )
                    print("  ↷ moved to triaged_skip")
                    break

                if action == "i":
                    store.update_url_status(
                        row["id"],
                        "ineligible",
                        triage_reason="manual rescue: ineligible",
                        scrape_failed_reason="",
                    )
                    print("  ↷ moved to ineligible")
                    break

                if action == "d":
                    store.update_url_status(
                        row["id"],
                        "triaged_defer",
                        triage_reason="manual rescue: defer for later",
                        scrape_failed_reason="",
                    )
                    print("  ↷ moved to triaged_defer")
                    break

                if action == "p":
                    pasted = _collect_multiline_input(end_marker=args.end_marker)
                    if not pasted.strip():
                        print("  no content pasted")
                        continue
                    try:
                        summary_file = _manual_capture_and_store(
                            store,
                            row=row,
                            raw_text=pasted,
                            strategy=capture_strategy,
                        )
                    except RuntimeError as exc:
                        print(f"  ✗ manual summarize failed: {exc}")
                        continue

                    print(f"  ✓ summarized via {capture_strategy}")
                    print(f"    saved: {summary_file}")
                    break

                print("  unknown action")

    return 0


# ── Main ──


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="aa",
        description="anti-alecto — tame the tab fury",
    )
    sub = parser.add_subparsers(dest="command")

    # ingest
    p = sub.add_parser("ingest", help="Import chrome tab dumps")
    p.add_argument("file", nargs="?", help="Specific dump file (default: all new in dumps/)")

    # add
    p = sub.add_parser("add", help="Add one URL and process it end-to-end")
    p.add_argument("url", help="URL to add")
    p.add_argument("--title", default="", help="Optional title hint")
    p.add_argument("--no-process", action="store_true", help="Only add URL; do not triage/scrape")

    # triage
    p = sub.add_parser("triage", help="Triage pending URLs")
    p.add_argument("--all", action="store_true", help="Repeat triage until pending <= batch size, then run one final pass")

    # scrape
    p = sub.add_parser("scrape", help="Scrape triaged URLs")
    p.add_argument("--limit", "-l", type=int, default=1, help="Max URLs to scrape per batch")
    p.add_argument("--all", action="store_true", help="Repeat scrape batches until no triaged_keep URLs remain")

    # run
    p = sub.add_parser("run", help="Full pipeline: ingest → triage → scrape")
    p.add_argument("--limit", "-l", type=int, default=1, help="Max URLs to scrape")

    # status
    sub.add_parser("status", help="Pipeline stats")

    # search
    p = sub.add_parser("search", help="Search summaries")
    p.add_argument("query", help="Search query")
    p.add_argument("--limit", "-l", type=int, default=20)

    # digest
    p = sub.add_parser("digest", help="Recent summaries")
    p.add_argument("--limit", "-l", type=int, default=10)

    # failed
    sub.add_parser("failed", help="Show failed scrapes")

    # retry
    sub.add_parser("retry", help="Reset failed scrapes for retry")

    # paste
    p = sub.add_parser("paste", help="Manually capture content for a URL and summarize it (paste-first)")
    p.add_argument("--id", type=int, help="Existing URL id to attach manual content to")
    p.add_argument("--url", help="URL to capture manually (required if --id not provided)")
    p.add_argument("--title", help="Override title")
    p.add_argument("--file", help="Text file to ingest as manual content")
    p.add_argument("--image", help="Image file for optional OCR")
    p.add_argument("--stdin", action="store_true", help="Also read pasted content from stdin")
    p.add_argument("--capture-mode", choices=["paste", "playwriter"], default="paste", help="Label the manual capture source (paste is simplest; playwriter is optional)")
    p.add_argument("--end-marker", default="::end", help="Marker line used to end interactive paste input")

    # rescue
    p = sub.add_parser("rescue", help="Interactive manual rescue queue for blocked failures (paste-first)")
    p.add_argument("--id", type=int, help="Rescue a specific failed URL id")
    p.add_argument("--limit", "-l", type=int, default=10, help="Max URLs to process interactively")
    p.add_argument("--all", action="store_true", help="Include non-blocked scrape failures too")
    p.add_argument("--open", action="store_true", help="Open each URL in default browser before prompting")
    p.add_argument("--capture-mode", choices=["paste", "playwriter"], default="paste", help="Label capture source for pasted content")
    p.add_argument("--end-marker", default="::end", help="Marker line used to end pasted content")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    commands = {
        "ingest": cmd_ingest,
        "add": cmd_add,
        "triage": cmd_triage,
        "scrape": cmd_scrape,
        "run": cmd_run,
        "status": cmd_status,
        "search": cmd_search,
        "digest": cmd_digest,
        "failed": cmd_failed,
        "retry": cmd_retry,
        "paste": cmd_paste,
        "rescue": cmd_rescue,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
