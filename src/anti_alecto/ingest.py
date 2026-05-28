"""Ingest browser tab dumps into the store."""

import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

from .config import Config
from .db import Store
from .policy import dedupe_prefix, is_ineligible_url


def normalize_url(url: str, tracking_params: set[str] | None = None) -> str:
    """Canonicalize URL for durable de-duplication."""
    if tracking_params is None:
        tracking_params = set()

    parsed = urlparse(url)
    scheme = parsed.scheme or "https"
    host = (parsed.netloc or "").lower()
    path = parsed.path.rstrip("/") or "/"

    # Strip tracking params first.
    if parsed.query and tracking_params:
        params = parse_qs(parsed.query, keep_blank_values=True)
        filtered = {k: v for k, v in params.items() if k not in tracking_params}
    else:
        filtered = parse_qs(parsed.query, keep_blank_values=True) if parsed.query else {}

    query = urlencode(filtered, doseq=True) if filtered else ""

    # Domain-specific canonicalization.
    if host in {"github.com", "www.github.com"}:
        host = "github.com"
        parts = [p for p in path.split("/") if p]
        if len(parts) >= 2:
            owner, repo = parts[0], parts[1]
            remainder = parts[2:]
            marker_idx = -1
            marker = ""
            for i, p in enumerate(remainder):
                if p in {"blob", "tree", "issues", "pull"}:
                    marker_idx = i
                    marker = p
                    break
            if marker_idx >= 0:
                after = remainder[marker_idx + 1 :]
                if marker in {"issues", "pull"} and after and after[0].isdigit():
                    path = f"/{owner}/{repo}/{marker}/{after[0]}"
                elif marker in {"blob", "tree"} and after:
                    path = f"/{owner}/{repo}/{marker}/{'/'.join(after)}"
                else:
                    path = f"/{owner}/{repo}/{marker}"
        query = ""  # GitHub page queries/fragments are often non-durable UI state.

    if host in {"reddit.com", "www.reddit.com", "old.reddit.com", "np.reddit.com"}:
        host = "reddit.com"
        parts = [p for p in path.split("/") if p]
        # /r/<sub>/comments/<id>/...
        if len(parts) >= 4 and parts[0] == "r" and parts[2] == "comments" and parts[3]:
            path = f"/r/{parts[1]}/comments/{parts[3]}"
            query = ""
        # /comments/<id>/...
        elif len(parts) >= 2 and parts[0] == "comments" and parts[1]:
            path = f"/comments/{parts[1]}"
            query = ""

    if host in {"x.com", "www.x.com", "twitter.com", "www.twitter.com", "mobile.twitter.com"}:
        host = "x.com"
        parts = [p for p in path.split("/") if p]
        if len(parts) >= 3:
            for i, p in enumerate(parts):
                if p == "status" and i >= 1 and i + 1 < len(parts):
                    user = parts[i - 1]
                    sid = parts[i + 1]
                    if sid.isdigit() and user:
                        path = f"/{user}/status/{sid}"
                        query = ""
                        break

    if host in {"youtube.com", "www.youtube.com", "m.youtube.com"} and path == "/watch":
        host = "youtube.com"
        v = (filtered.get("v") or [""])[0].strip()
        query = urlencode({"v": v}) if v else ""

    if host == "youtu.be":
        vid = (path or "/").strip("/").split("/")[0]
        host = "youtube.com"
        path = "/watch"
        query = urlencode({"v": vid}) if vid else ""

    normalized = parsed._replace(
        scheme=scheme,
        netloc=host,
        fragment="",
        query=query,
        path=path,
    ).geturl()

    return normalized


def extract_domain(url: str) -> str:
    """Extract domain from URL."""
    parsed = urlparse(url)
    host = parsed.netloc or ""
    # Strip www.
    if host.startswith("www."):
        host = host[4:]
    return host


def _extract_tabs(data: object) -> list[dict[str, str]]:
    """Normalize supported dump formats into a list of {'url','title'} items.

    Supported shapes:
    - Chrome-style: {"tabs": [{"title": ..., "url": ...}, ...]}
    - Brave-style:  [{"title": ..., "url": ...}, ...]
    - Window dumps: {"windows": [{"tabs": [...]}, ...]}
    """
    candidates: list[object] = []

    if isinstance(data, list):
        # Brave flat export format.
        candidates = data
    elif isinstance(data, dict):
        tabs = data.get("tabs")
        if isinstance(tabs, list):
            candidates = tabs
        else:
            windows = data.get("windows")
            if isinstance(windows, list):
                for w in windows:
                    if isinstance(w, dict) and isinstance(w.get("tabs"), list):
                        candidates.extend(w["tabs"])

    tabs_out: list[dict[str, str]] = []
    for item in candidates:
        if not isinstance(item, dict):
            continue
        url = str(item.get("url") or "").strip()
        if not url:
            continue
        title = str(item.get("title") or "").strip()
        tabs_out.append({"url": url, "title": title})

    return tabs_out


def _extract_tabs_from_plaintext(text: str) -> list[dict[str, str]]:
    """Extract one URL per line from plaintext dumps.

    Supports simple lines like:
    - https://example.com
    - - https://example.com
    - * https://example.com
    """
    tabs_out: list[dict[str, str]] = []
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue

        line = re.sub(r"^[-*]\s+", "", line).strip()
        if line.startswith("http://") or line.startswith("https://"):
            tabs_out.append({"url": line, "title": ""})

    return tabs_out


def ingest_dump(dump_path: Path, store: Store, config: Config) -> dict:
    """
    Import a single browser tab dump JSON into the store.

    Returns stats: {filename, tab_count, new, skipped_pattern, skipped_dupe}
    """
    filename = dump_path.name
    tracking_params = config.tracking_params

    raw = dump_path.read_text(encoding="utf-8", errors="replace")

    tabs: list[dict[str, str]] = []
    try:
        data = json.loads(raw)
        tabs = _extract_tabs(data)
    except json.JSONDecodeError:
        tabs = _extract_tabs_from_plaintext(raw)

    if not tabs:
        raise ValueError(f"Unsupported or empty dump format: {dump_path}")
    tab_count = len(tabs)

    # Record dump (idempotent — returns None if already imported)
    dump_id = store.record_dump(filename, tab_count)
    if dump_id is None:
        return {
            "filename": filename,
            "tab_count": tab_count,
            "new": 0,
            "skipped_pattern": 0,
            "skipped_dupe": 0,
            "already_imported": True,
        }

    new = 0
    skipped_pattern = 0
    skipped_dupe = 0

    for tab in tabs:
        url = tab.get("url", "").strip()
        title = tab.get("title", "").strip()

        if not url:
            continue

        # Check skip patterns
        should_skip, reason = config.should_skip(url)
        if should_skip:
            store.add_url(
                url=url,
                url_normalized=normalize_url(url, tracking_params),
                title=title,
                domain=extract_domain(url),
                dump_id=dump_id,
                status="ineligible",
                triage_reason=reason,
            )
            skipped_pattern += 1
            continue

        # Normalize and check for exact global duplicate.
        url_norm = normalize_url(url, tracking_params)
        existing = store.get_url_by_normalized(url_norm)
        if existing:
            skipped_dupe += 1
            continue

        # Ingest-time prefix dedupe for known walled/paywalled areas.
        prefix = dedupe_prefix(url_norm)
        blocked = store.find_walled_prefix_match_any(prefix)
        if blocked:
            skipped_dupe += 1
            continue

        store.add_url(
            url=url,
            url_normalized=url_norm,
            title=title,
            domain=extract_domain(url),
            dump_id=dump_id,
            status="pending",
        )
        new += 1

    return {
        "filename": filename,
        "tab_count": tab_count,
        "new": new,
        "skipped_pattern": skipped_pattern,
        "skipped_dupe": skipped_dupe,
        "already_imported": False,
    }


def ingest_all(dumps_dir: Path, store: Store, config: Config) -> list[dict]:
    """Import all un-imported supported dumps from a directory."""
    imported = set(store.get_imported_dumps())
    results = []

    candidates = {p for p in dumps_dir.glob("*.json")}
    # Brave quick-export one-url-per-line dumps.
    candidates.update({p for p in dumps_dir.glob("brave-*.txt")})

    for dump_path in sorted(candidates):
        if dump_path.name in imported:
            continue
        result = ingest_dump(dump_path, store, config)
        results.append(result)

    return results
