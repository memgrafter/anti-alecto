"""FlatMachine hooks for triage and scrape machines."""

import json
import re
from datetime import datetime, timezone
from urllib.parse import urlparse

import yaml

from flatmachines import MachineHooks

from .scrape import scrape_url


APPROX_CHARS_PER_TOKEN = 4
MAX_SCRAPE_TOKENS = 200_000
MAX_SCRAPE_CHARS = MAX_SCRAPE_TOKENS * APPROX_CHARS_PER_TOKEN


class TriageHooks(MachineHooks):
    """Hooks for the triage FlatMachine."""

    def on_action(self, action: str, context: dict) -> dict:
        if action == "parse_triage_result":
            return self._parse_triage_result(context)
        return context

    def _parse_triage_result(self, context: dict) -> dict:
        """Parse agent output into structured triage decisions."""
        raw = context.get("triage_output", "")
        decisions = []

        # Parse JSON output from agent
        try:
            # Try to find JSON array in the output
            json_match = re.search(r"\[.*\]", raw, re.DOTALL)
            if json_match:
                decisions = json.loads(json_match.group())
        except (json.JSONDecodeError, ValueError):
            pass

        # Fallback: parse line-by-line if JSON failed
        if not decisions:
            for line in raw.strip().split("\n"):
                line = line.strip()
                if not line:
                    continue
                # Expect: KEEP|SKIP|DEFER <url> — reason
                match = re.match(
                    r"(KEEP|SKIP|DEFER)\s+(\S+)\s*[-—–]\s*(.*)",
                    line, re.IGNORECASE,
                )
                if match:
                    decisions.append({
                        "action": match.group(1).lower(),
                        "url": match.group(2),
                        "reason": match.group(3).strip(),
                    })

        context["triage_decisions"] = decisions
        context["triage_parsed"] = len(decisions) > 0
        return context


class ScrapeHooks(MachineHooks):
    """Hooks for the scrape+summarize FlatMachine."""

    def on_action(self, action: str, context: dict) -> dict:
        if action == "scrape_url":
            return self._scrape_url(context)
        elif action == "validate_summary":
            return self._validate_summary(context)
        elif action == "check_judge_result":
            return self._check_judge_result(context)
        elif action == "validate_frontmatter":
            return self._validate_frontmatter(context)
        return context

    def _scrape_url(self, context: dict) -> dict:
        """Scrape URL using sync strategy chain."""
        url = context["url"]
        timeout = int(context.get("timeout_seconds", 30))
        wait_ms = int(context.get("playwright_wait_ms", 3000))
        min_len = int(context.get("min_content_length", 200))
        cache_ttl_hours = int(context.get("cache_ttl_hours", 24))

        import concurrent.futures

        # Run scraper in worker thread so Playwright sync API isn't inside FlatMachine asyncio loop.
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            result = pool.submit(
                scrape_url,
                url,
                timeout,
                wait_ms,
                min_len,
                cache_ttl_hours,
            ).result()

        if not result.success:
            reason = result.block_reason if result.blocked else (result.error or "unknown scrape error")
            if str(reason).startswith("SKIP_"):
                # Signals a non-error skip path (e.g. no YouTube transcript).
                raise RuntimeError(str(reason))

            attempts = result.diagnostics or []
            if attempts:
                chain = " -> ".join(
                    f"{a.get('strategy')}:{'ok' if a.get('success') else (a.get('reason') or 'fail')}"
                    for a in attempts
                )
                raise RuntimeError(f"Scrape failed: {reason} (attempts: {chain})")
            raise RuntimeError(f"Scrape failed: {reason}")

        raw_text = result.text or ""
        char_count = len(raw_text)
        approx_tokens = char_count // APPROX_CHARS_PER_TOKEN
        if char_count > MAX_SCRAPE_CHARS:
            raise RuntimeError(
                "SKIP_TOO_LARGE: "
                f"content too large (~{approx_tokens} tokens, {char_count} chars; "
                f"limit={MAX_SCRAPE_TOKENS} tokens)"
            )

        context["raw_content"] = raw_text
        context["word_count"] = result.word_count
        context["scrape_strategy"] = result.strategy
        context["scrape_diagnostics_json"] = json.dumps(result.diagnostics or [])
        context["scrape_details_json"] = json.dumps(result.details or {})
        context["scraped_at"] = datetime.now(timezone.utc).isoformat()

        if not context.get("title"):
            context["title"] = self._title_from_url(url)

        return context

    def _validate_summary(self, context: dict) -> dict:
        """Validate summary has required sections."""
        summary = context.get("summary", "")
        errors = []

        required = [
            ("TL;DR", "Missing TL;DR section"),
            ("Key Quote", "Missing Key Quote section"),
            ("Summary", "Missing Summary section"),
            ("Assessment", "Missing Assessment section"),
        ]

        for section, msg in required:
            pattern = rf"^##?#?\s*{re.escape(section)}"
            if not re.search(pattern, summary, re.MULTILINE | re.IGNORECASE):
                errors.append(msg)

        # TL;DR content check
        tldr_match = re.search(
            r"^##?#?\s*TL;DR\s*\n+(.+?)(?=\n##|\n###|\Z)",
            summary, re.MULTILINE | re.IGNORECASE | re.DOTALL,
        )
        if tldr_match and len(tldr_match.group(1).strip()) < 20:
            errors.append("TL;DR too short")

        # Thread-focused summaries must preserve top comment + commenter + thread topics.
        raw_content = context.get("raw_content", "") or ""
        is_thread_capture = (
            "Reddit thread capture" in raw_content
            or "Hacker News thread capture" in raw_content
        )
        if is_thread_capture:
            if not re.search(r"Top comment", summary, re.IGNORECASE):
                errors.append("Thread summary missing 'Top comment' line")
            if not re.search(r"Top commenter", summary, re.IGNORECASE):
                errors.append("Thread summary missing 'Top commenter' line")
            if not re.search(r"Thread topics", summary, re.IGNORECASE):
                errors.append("Thread summary missing 'Thread topics' bullets")

        context["summary_valid"] = len(errors) == 0
        context["summary_validation_errors"] = errors
        context["summary_attempt"] = context.get("summary_attempt", 0) + 1
        return context

    def _check_judge_result(self, context: dict) -> dict:
        """Parse judge PASS/REJECT."""
        result = context.get("judge_result", "").strip()
        first_line = result.split("\n")[0].strip().upper()

        if first_line.startswith("PASS"):
            context["judge_passed"] = True
            context["judge_feedback"] = ""
        else:
            context["judge_passed"] = False
            feedback = result
            if feedback.upper().startswith("REJECT"):
                feedback = feedback[6:].lstrip(":").strip()
            context["judge_feedback"] = feedback

        return context

    def _validate_frontmatter(self, context: dict) -> dict:
        """Validate frontmatter YAML structure."""
        raw = context.get("frontmatter_yaml", "").strip()
        errors = []

        # Strip code fences
        if raw.startswith("```"):
            raw = re.sub(r"^```\w*\n?", "", raw)
            raw = re.sub(r"\n?```$", "", raw)

        try:
            fm = yaml.safe_load(raw) or {}
        except yaml.YAMLError as e:
            errors.append(f"YAML parse error: {e}")
            context["frontmatter_valid"] = False
            context["frontmatter_validation_errors"] = errors
            context["frontmatter_attempt"] = context.get("frontmatter_attempt", 0) + 1
            return context

        required = [
            "tldr", "key_quote", "durability", "content_type",
            "density", "originality", "reference_style", "scrape_quality", "tags",
        ]
        for field in required:
            if field not in fm or fm[field] is None:
                errors.append(f"Missing: {field}")

        enums = {
            "durability": ["low", "medium", "high"],
            "density": ["low", "medium", "high"],
            "content_type": ["fact", "opinion", "tutorial", "reference", "announcement", "mixed"],
            "originality": ["primary", "synthesis", "commentary"],
            "reference_style": ["skim-once", "refer-back", "deep-study"],
            "scrape_quality": ["good", "partial", "poor"],
        }
        for field, valid in enums.items():
            if field in fm and fm[field] not in valid:
                errors.append(f"Invalid {field}: '{fm[field]}'")

        if "tags" in fm and (not isinstance(fm["tags"], list) or len(fm["tags"]) == 0):
            errors.append("tags must be a non-empty list")

        context["frontmatter_valid"] = len(errors) == 0
        context["frontmatter_validation_errors"] = errors
        context["frontmatter_attempt"] = context.get("frontmatter_attempt", 0) + 1
        return context

    def _title_from_url(self, url: str) -> str:
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        if path:
            title = path.split("/")[-1]
            title = re.sub(r"\.[^.]+$", "", title)
            title = re.sub(r"[-_]", " ", title)
            return title.title()
        return parsed.netloc
