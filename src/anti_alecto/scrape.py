"""User-first scrape attempt flow with block detection + diagnostics."""

from __future__ import annotations

import hashlib
import html
import ipaddress
import json
import re
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, unquote, urlencode, urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen


_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_CACHE_DIR = _PROJECT_ROOT / ".cache" / "scrape"
_PLAYWRIGHT_PROFILE_DIR = _CACHE_DIR / "playwright-profile"

_BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

_HTTP_HEADERS = {
    "User-Agent": _BROWSER_UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,text/plain;q=0.8,*/*;q=0.5",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}


@dataclass
class ScrapeResult:
    """Result of a scrape attempt or chain."""

    success: bool
    text: str
    word_count: int
    strategy: str
    blocked: bool = False
    block_reason: str = ""
    error: str = ""
    diagnostics: list[dict] = field(default_factory=list)
    status_code: int | None = None
    elapsed_ms: int = 0
    outcome: str = ""
    source_url: str = ""
    details: dict = field(default_factory=dict)


BLOCK_SIGNALS = [
    (re.compile(r"cf-browser-verification|cf-challenge|__cf_chl", re.I), "cloudflare challenge"),
    (re.compile(r"<title>\s*Just a moment", re.I), "cloudflare waiting page"),
    (re.compile(r"Attention Required.*Cloudflare", re.I | re.S), "cloudflare attention"),
    (re.compile(r"captcha|recaptcha|hcaptcha", re.I), "captcha"),
    (re.compile(r"verify you are (a )?human|are you human", re.I), "human verification"),
    (re.compile(r"<title>\s*(403|Access Denied|Forbidden)", re.I), "access denied"),
    (re.compile(r"subscribe to (continue|read|access)", re.I), "paywall"),
    (re.compile(r"(premium|paid) (content|article|member)", re.I), "paywall"),
    (re.compile(r"sign in to continue|log in to (continue|access)", re.I), "login wall"),
]

_JS_SHELL_SIGNALS = [
    re.compile(r"__NEXT_DATA__|id=\"__next\"", re.I),
    re.compile(r"id=\"root\"", re.I),
    re.compile(r"<script[^>]+src=", re.I),
]

_GITHUB_RESERVED_ROOTS = {
    "features",
    "topics",
    "collections",
    "trending",
    "marketplace",
    "sponsors",
    "orgs",
    "organizations",
    "settings",
    "about",
    "explore",
    "search",
    "login",
    "signup",
}

_SENSITIVE_ARCHIVE_PATH = re.compile(
    r"/(account|billing|settings|admin|dashboard|login|signin|logout|oauth|auth|session)(/|$)",
    re.I,
)


def classify_url(url: str) -> tuple[str, str]:
    """Classify a URL for scrape routing decisions."""
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    path = parsed.path or ""

    # Session/app pages that generally require user auth context and should not be archived.
    if host in {
        "discord.com",
        "www.discord.com",
        "canary.discord.com",
        "ptb.discord.com",
        "discord.gg",
        "discordapp.com",
        "www.discordapp.com",
    }:
        return "session_app", "discord page"

    if host == "console.firebase.google.com":
        return "session_app", "firebase console page"

    if (host == "google.com" or host.endswith(".google.com")) and path.startswith("/search"):
        return "session_app", "google search page"

    if host == "gemini.google.com" and path.startswith("/app/"):
        return "session_app", "session app page"
    if host == "claude.ai" and re.match(r"^/(login|chat|new)(/|$)", path, re.I):
        return "session_app", "session app page"
    if host == "app.devin.ai":
        return "session_app", "session app page"
    if host == "cloud.digitalocean.com" and path.startswith("/account"):
        return "session_app", "account dashboard page"
    if host == "openrouter.ai" and path.startswith("/activity"):
        return "session_app", "account activity page"
    if host == "docs.google.com" and re.match(r"^/document/d/[^/]+/edit", path, re.I):
        return "session_app", "private edit page"

    if re.search(r"/(login|signin|logout|oauth|auth)(/|$)", path, re.I):
        return "login_page", "login page"

    return "public", ""


def detect_block(html: str, extracted_text: str, min_content_length: int = 200) -> tuple[bool, str]:
    """Return (blocked, reason) if response looks blocked/unusable."""
    for pattern, reason in BLOCK_SIGNALS:
        if pattern.search(html or ""):
            return True, reason

    if not extracted_text or not extracted_text.strip():
        return True, "empty extraction"

    if len(extracted_text.strip()) < min_content_length:
        return True, f"content too short ({len(extracted_text.strip())} chars)"

    return False, ""


def _result_outcome(result: ScrapeResult) -> str:
    if result.success:
        if result.strategy.startswith("cache"):
            return "success_cached"
        if result.strategy.startswith("archive"):
            return "success_archived"
        if "playwright" in result.strategy:
            return "success_rendered"
        return "success_live"

    reason = (result.block_reason or result.error or "").lower()
    if "captcha" in reason or "human verification" in reason:
        return "gated_captcha"
    if (
        "login" in reason
        or "session" in reason
        or "account" in reason
        or "private edit" in reason
        or "auth required" in reason
    ):
        return "needs_login"
    if "429" in reason or "rate limit" in reason:
        return "rate_limited"
    if "404" in reason or "not found" in reason:
        return "not_found"
    return "transient_error"


def _diag_entry(result: ScrapeResult) -> dict:
    reason = result.block_reason or result.error or ""
    out = {
        "strategy": result.strategy,
        "success": result.success,
        "blocked": result.blocked,
        "reason": reason,
        "word_count": result.word_count,
        "status_code": result.status_code,
        "elapsed_ms": result.elapsed_ms,
        "outcome": result.outcome or _result_outcome(result),
    }
    if result.source_url:
        out["source_url"] = result.source_url
    if result.details:
        out["details"] = result.details
    return out


def _looks_like_js_shell(html: str, extracted_text: str, min_content_length: int) -> bool:
    text_len = len((extracted_text or "").strip())
    if text_len >= min_content_length:
        return False
    matches = sum(1 for p in _JS_SHELL_SIGNALS if p.search(html or ""))
    script_count = len(re.findall(r"<script", html or "", flags=re.I))
    return matches >= 1 and script_count >= 5


def _is_archive_safe_url(url: str) -> bool:
    """Only allow archive lookups for public web URLs."""
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return False

    host = (parsed.hostname or "").strip().lower()
    if not host:
        return False

    category, _ = classify_url(url)
    if category in {"session_app", "login_page"}:
        return False

    if host in {"localhost", "127.0.0.1", "::1"}:
        return False

    if host.endswith(".local") or host.endswith(".internal") or host.endswith(".lan"):
        return False

    if _SENSITIVE_ARCHIVE_PATH.search(parsed.path or ""):
        return False

    if re.search(r"(^|&)(token|session|sid|auth|oauth|api[_-]?key|nonce|state)=", parsed.query or "", re.I):
        return False

    try:
        ip = ipaddress.ip_address(host)
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
            return False
    except ValueError:
        # Not an IP literal. Require a plausible public DNS name.
        if "." not in host:
            return False

    return True


def _cache_key(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()


def _cache_file(url: str) -> Path:
    return _CACHE_DIR / f"{_cache_key(url)}.json"


def _load_cache(url: str, ttl_hours: int, allow_stale: bool = False) -> ScrapeResult | None:
    path = _cache_file(url)
    if not path.exists():
        return None

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None

    text = (payload.get("text") or "").strip()
    if not text:
        return None

    now = int(time.time())
    saved_at = int(payload.get("saved_at", 0) or 0)
    ttl_seconds = max(1, int(ttl_hours)) * 3600
    is_stale = saved_at <= 0 or (now - saved_at > ttl_seconds)

    if is_stale and not allow_stale:
        return None

    strategy = "cache_stale" if is_stale else "cache"
    r = ScrapeResult(
        True,
        text,
        int(payload.get("word_count") or len(text.split())),
        strategy,
        source_url=str(payload.get("source_url") or payload.get("url") or url),
    )
    r.outcome = _result_outcome(r)
    return r


def _save_cache(url: str, result: ScrapeResult) -> None:
    if not result.success or not result.text.strip():
        return

    if result.strategy.startswith("cache"):
        return

    try:
        _CACHE_DIR.mkdir(parents=True, exist_ok=True)
        payload = {
            "url": url,
            "source_url": result.source_url or url,
            "saved_at": int(time.time()),
            "text": result.text,
            "word_count": result.word_count,
            "strategy": result.strategy,
            "status_code": result.status_code,
        }
        _cache_file(url).write_text(json.dumps(payload), encoding="utf-8")
    except Exception:
        # Cache should never break scraping.
        pass


def _decode_body(raw: bytes, content_type: str) -> str:
    charset_match = re.search(r"charset=([\w\-]+)", content_type or "", re.I)
    charset = charset_match.group(1) if charset_match else "utf-8"
    try:
        return raw.decode(charset, errors="replace")
    except Exception:
        return raw.decode("utf-8", errors="replace")


def _hn_item_parts(url: str) -> str | None:
    """Return HN item id for /item?id=<n> URLs, else None."""
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    if host != "news.ycombinator.com" or (parsed.path or "") != "/item":
        return None
    item_id = (parse_qs(parsed.query or "").get("id") or [""])[0]
    return item_id if item_id.isdigit() else None


def _hn_extract_outbound_url(requested_url: str, html_text: str) -> str:
    """Extract the primary linked article URL from a Hacker News item page."""
    if not _hn_item_parts(requested_url):
        return ""

    html_text = html_text or ""

    # Prefer titleline/storylink anchors when present.
    patterns = [
        r'<span\s+class="titleline"[^>]*>\s*<a\s+href="([^"]+)"',
        r'<a\s+href="([^"]+)"\s+class="storylink"',
    ]
    href = ""
    for pat in patterns:
        m = re.search(pat, html_text, re.I)
        if m:
            href = m.group(1).strip()
            break

    if not href:
        return ""

    target = html.unescape(urljoin(requested_url, href)).strip()
    if not target:
        return ""

    parsed = urlparse(target)
    host = (parsed.hostname or "").lower()
    if parsed.scheme not in {"http", "https"}:
        return ""
    # Ask HN / Show HN / Jobs often point back to HN itself (not an external target).
    if host == "news.ycombinator.com":
        return ""

    return target


def _hn_clean_text(text: str) -> str:
    t = html.unescape(text or "")
    t = re.sub(r"<br\s*/?>", "\n", t, flags=re.I)
    t = re.sub(r"</p>\s*<p[^>]*>", "\n\n", t, flags=re.I)
    t = re.sub(r"<p[^>]*>", "", t, flags=re.I)
    t = re.sub(r"</p>", "", t, flags=re.I)
    t = re.sub(r"<a[^>]+href=\"([^\"]+)\"[^>]*>(.*?)</a>", r"\2 (\1)", t, flags=re.I | re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def _hn_flatten_comments(children: list, max_comments: int = 140) -> tuple[list[dict], list[dict]]:
    top_level: list[dict] = []
    all_comments: list[dict] = []

    def walk(nodes: list, depth: int) -> None:
        for node in nodes or []:
            if len(all_comments) >= max_comments:
                return
            if not isinstance(node, dict):
                continue
            if node.get("type") != "comment":
                continue

            body = _hn_clean_text(node.get("text") or "")
            entry = {
                "author": node.get("author") or "[deleted]",
                "score": int(node.get("points") or 0),
                "body": body,
                "depth": depth,
                "id": node.get("id") or 0,
            }
            if depth == 0:
                top_level.append(entry)
            if body:
                all_comments.append(entry)

            walk(node.get("children") or [], depth + 1)

    walk(children or [], 0)
    return top_level, all_comments


def _hn_json_to_text(payload: dict, requested_url: str) -> tuple[str, dict]:
    item_id = int(payload.get("id") or 0)
    title = _hn_clean_text(payload.get("title") or "")
    author = payload.get("author") or ""
    points = int(payload.get("points") or 0)
    submission_text = _hn_clean_text(payload.get("text") or "")

    outbound_url = str(payload.get("url") or "").strip()
    if outbound_url:
        out_host = (urlparse(outbound_url).hostname or "").lower()
        if out_host == "news.ycombinator.com":
            outbound_url = ""

    top_level, all_comments = _hn_flatten_comments(payload.get("children") or [], max_comments=180)
    top_sorted = sorted(top_level, key=lambda c: c.get("score", 0), reverse=True)
    top_comment = top_sorted[0] if top_sorted else None

    lines = [
        "Hacker News thread capture",
        "",
        f"Thread URL: {requested_url}",
        f"Item ID: {item_id}" if item_id else "",
        f"Title: {title}" if title else "",
        f"Author: {author}" if author else "",
        f"Points: {points}",
        f"Linked URL: {outbound_url}" if outbound_url else "",
        f"Top-level comments captured: {len(top_level)}",
        f"Total comments captured: {len(all_comments)}",
        "",
    ]

    if submission_text:
        lines.extend(["## Original submission text", submission_text[:12000], ""])

    if top_comment:
        lines.extend(
            [
                "## Top comment (highest-score top-level, verbatim)",
                f"u/{top_comment['author']} ({top_comment['score']}): {top_comment['body'][:2200]}",
                "",
            ]
        )

    if top_sorted:
        lines.append("## Prominent viewpoints (top-level comments)")
        for i, c in enumerate(top_sorted[:8], start=1):
            lines.append(f"{i}. ({c['score']}) u/{c['author']}: {c['body'][:900]}")
        lines.append("")

    if all_comments:
        lines.append("## Thread discussion sample")
        for c in all_comments[:70]:
            indent = "  " * min(int(c.get("depth") or 0), 3)
            lines.append(f"{indent}- ({c['score']}) u/{c['author']}: {c['body'][:700]}")
        lines.append("")

    text = "\n".join(x for x in lines if x is not None).strip()
    details = {
        "requested_url": requested_url,
        "hn_item_id": item_id,
        "captured_top_level_comments": len(top_level),
        "captured_comment_count": len(all_comments),
    }
    if top_comment:
        details["top_comment_author"] = top_comment["author"]
        details["top_comment_score"] = int(top_comment["score"])
        details["top_comment_excerpt"] = top_comment["body"][:500]
    if outbound_url:
        details["outbound_url"] = outbound_url
        details["reference_type"] = "hn_outbound"

    return text, details


def _hn_fetch_json_endpoint(
    endpoint: str,
    requested_url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 120,
) -> ScrapeResult:
    started = time.perf_counter()
    req = Request(
        endpoint,
        headers={
            **_HTTP_HEADERS,
            "Accept": "application/json,text/plain;q=0.9,*/*;q=0.5",
            "User-Agent": "anti-alecto/0.1 hn-json",
        },
    )

    try:
        with urlopen(req, timeout=timeout_seconds) as resp:
            status = getattr(resp, "status", None) or resp.getcode()
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read(5_000_000)
    except HTTPError as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "hn_json",
            blocked=True,
            block_reason=f"HTTP {e.code}",
            status_code=e.code,
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r
    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "hn_json",
            error=f"hn json fetch failed: {e}",
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r

    try:
        payload = json.loads(_decode_body(raw, content_type))
    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "hn_json",
            error=f"hn json parse failed: {e}",
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r

    text, details = _hn_json_to_text(payload if isinstance(payload, dict) else {}, requested_url)
    elapsed_ms = int((time.perf_counter() - started) * 1000)
    if not text or len(text.strip()) < min_content_length:
        r = ScrapeResult(
            False,
            text or "",
            0,
            "hn_json",
            blocked=True,
            block_reason="empty extraction",
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details=details,
        )
        r.outcome = _result_outcome(r)
        return r

    r = ScrapeResult(
        True,
        text,
        len(text.split()),
        "hn_json",
        status_code=status,
        elapsed_ms=elapsed_ms,
        source_url=endpoint,
        details=details,
    )
    r.outcome = _result_outcome(r)
    return r


def scrape_hn_thread(
    url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 120,
) -> ScrapeResult:
    """Scrape Hacker News item threads via Algolia items API."""
    item_id = _hn_item_parts(url)
    if not item_id:
        r = ScrapeResult(
            False,
            "",
            0,
            "hn_json",
            blocked=True,
            block_reason="SKIP_HN_UNSUPPORTED: hn url is not an item thread",
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r

    endpoint = f"https://hn.algolia.com/api/v1/items/{item_id}"
    r = _hn_fetch_json_endpoint(
        endpoint,
        requested_url=url,
        timeout_seconds=timeout_seconds,
        min_content_length=min(min_content_length, 80),
    )
    if r.success:
        r.details = {**(r.details or {}), "hn_api_endpoint": endpoint, "requested_url": url}
        r.outcome = _result_outcome(r)
        r.diagnostics = [_diag_entry(r)]
        return r

    r.details = {**(r.details or {}), "hn_api_endpoint": endpoint, "requested_url": url}
    r.outcome = _result_outcome(r)
    r.diagnostics = [_diag_entry(r)]
    return r


def scrape_http_static(
    url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 200,
    strategy: str = "http_static",
) -> ScrapeResult:
    """Light HTTP fetch + static extraction."""
    started = time.perf_counter()

    req = Request(url, headers=_HTTP_HEADERS)

    try:
        with urlopen(req, timeout=timeout_seconds) as resp:
            status = getattr(resp, "status", None) or resp.getcode()
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read(5_000_000)
    except HTTPError as e:
        html = ""
        try:
            html = e.read().decode("utf-8", errors="replace")
        except Exception:
            pass
        reason = f"HTTP {e.code}"
        blocked, detected = detect_block(html, "", min_content_length=min_content_length)
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            strategy,
            blocked=True,
            block_reason=detected or reason,
            status_code=e.code,
            elapsed_ms=elapsed_ms,
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r
    except URLError as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            strategy,
            error=f"network error: {e}",
            elapsed_ms=elapsed_ms,
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r
    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(False, "", 0, strategy, error=str(e), elapsed_ms=elapsed_ms, source_url=url)
        r.outcome = _result_outcome(r)
        return r

    html = _decode_body(raw, content_type)

    is_plain_text = "text/plain" in (content_type or "").lower() or url.lower().endswith(".md")
    if is_plain_text:
        text = html
    else:
        try:
            import trafilatura

            text = (
                trafilatura.extract(
                    html,
                    include_comments=False,
                    include_tables=True,
                    no_fallback=False,
                    favor_recall=True,
                    output_format="txt",
                )
                or ""
            )
        except ImportError:
            # Fallback extractor when trafilatura isn't available.
            text = re.sub(r"<script[\\s\\S]*?</script>", " ", html, flags=re.I)
            text = re.sub(r"<style[\\s\\S]*?</style>", " ", text, flags=re.I)
            text = re.sub(r"<[^>]+>", " ", text)
            text = re.sub(r"\\s+", " ", text).strip()

    details: dict = {}
    hn_target = _hn_extract_outbound_url(url, html)
    if hn_target:
        details["outbound_url"] = hn_target
        details["reference_type"] = "hn_outbound"
        details["hn_item_id"] = _hn_item_parts(url) or ""

    blocked, reason = detect_block(html, text, min_content_length=min_content_length)
    if blocked and reason.startswith("content too short") and _looks_like_js_shell(
        html, text, min_content_length
    ):
        reason = "js shell"

    elapsed_ms = int((time.perf_counter() - started) * 1000)

    if blocked:
        r = ScrapeResult(
            False,
            text or "",
            0,
            strategy,
            blocked=True,
            block_reason=reason,
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=url,
            details=details,
        )
        r.outcome = _result_outcome(r)
        return r

    r = ScrapeResult(
        True,
        text,
        len(text.split()),
        strategy,
        status_code=status,
        elapsed_ms=elapsed_ms,
        source_url=url,
        details=details,
    )
    r.outcome = _result_outcome(r)
    return r


def scrape_playwright(
    url: str,
    timeout_ms: int = 30000,
    wait_ms: int = 3000,
    min_content_length: int = 200,
) -> ScrapeResult:
    """Browser render pass using Playwright Chromium (sync API)."""
    started = time.perf_counter()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return ScrapeResult(
            False,
            "",
            0,
            "playwright",
            error="playwright not installed",
            source_url=url,
        )

    context = None
    try:
        _PLAYWRIGHT_PROFILE_DIR.mkdir(parents=True, exist_ok=True)

        with sync_playwright() as p:
            context = p.chromium.launch_persistent_context(
                user_data_dir=str(_PLAYWRIGHT_PROFILE_DIR),
                headless=True,
                user_agent=_BROWSER_UA,
                viewport={"width": 1280, "height": 720},
                args=["--disable-blink-features=AutomationControlled"],
            )
            page = context.new_page()

            response = page.goto(url, timeout=timeout_ms, wait_until="domcontentloaded")
            status = response.status if response else None
            page.wait_for_timeout(wait_ms)

            html = page.content()
            text = page.evaluate(
                """() => {
                    const remove = document.querySelectorAll(
                        'script, style, nav, header, footer, .nav, .header, .footer, ' +
                        '.sidebar, .menu, .ad, .advertisement, .cookie-banner, .popup'
                    );
                    remove.forEach(el => el.remove());

                    const article = document.querySelector('article') || document.querySelector('main');
                    if (article) return article.innerText || '';
                    return document.body ? (document.body.innerText || '') : '';
                }"""
            )

            blocked, reason = detect_block(html, text, min_content_length=min_content_length)
            elapsed_ms = int((time.perf_counter() - started) * 1000)

            if status in (403, 429, 503, 401):
                r = ScrapeResult(
                    False,
                    text or "",
                    0,
                    "playwright",
                    blocked=True,
                    block_reason=f"HTTP {status}",
                    status_code=status,
                    elapsed_ms=elapsed_ms,
                    source_url=url,
                )
                r.outcome = _result_outcome(r)
                return r

            if blocked:
                r = ScrapeResult(
                    False,
                    text or "",
                    0,
                    "playwright",
                    blocked=True,
                    block_reason=reason,
                    status_code=status,
                    elapsed_ms=elapsed_ms,
                    source_url=url,
                )
                r.outcome = _result_outcome(r)
                return r

            r = ScrapeResult(
                True,
                text,
                len(text.split()),
                "playwright",
                status_code=status,
                elapsed_ms=elapsed_ms,
                source_url=url,
            )
            r.outcome = _result_outcome(r)
            return r

    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "playwright",
            error=str(e),
            elapsed_ms=elapsed_ms,
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r
    finally:
        if context is not None:
            try:
                context.close()
            except Exception:
                pass


def _youtube_video_id(url: str) -> str | None:
    """Extract YouTube video id from watch/shorts/youtu.be URLs."""
    parsed = urlparse(url)
    host = (parsed.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]

    if host == "youtu.be":
        vid = (parsed.path or "").strip("/").split("/")[0]
        return vid or None

    if host in {"youtube.com", "m.youtube.com"}:
        path = parsed.path or ""
        if path == "/watch":
            q = parse_qs(parsed.query or "")
            vid = (q.get("v") or [""])[0].strip()
            return vid or None
        if path.startswith("/shorts/") or path.startswith("/live/"):
            parts = [p for p in path.split("/") if p]
            if len(parts) >= 2:
                return parts[1]

    return None


def _clean_vtt_text(vtt_text: str) -> str:
    """Convert VTT subtitles to plain text."""
    lines: list[str] = []
    last = ""

    for raw in (vtt_text or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.upper().startswith("WEBVTT"):
            continue
        if line.upper().startswith(("NOTE", "STYLE", "REGION")):
            continue
        if line.startswith(("Kind:", "Language:")):
            continue
        if "-->" in line:
            continue
        if re.fullmatch(r"\d+", line):
            continue

        line = re.sub(r"<[^>]+>", " ", line)
        line = html.unescape(line)
        line = re.sub(r"\s+", " ", line).strip()
        if not line:
            continue
        if line == last:
            continue

        lines.append(line)
        last = line

    return "\n".join(lines).strip()


def scrape_youtube_transcript(url: str, timeout_seconds: int = 30) -> ScrapeResult:
    """Fetch a YouTube transcript via yt-dlp and return plain text."""
    started = time.perf_counter()
    video_id = _youtube_video_id(url)
    if not video_id:
        r = ScrapeResult(
            False,
            "",
            0,
            "youtube_transcript",
            blocked=True,
            block_reason="not a youtube video url",
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r

    yt_dlp = shutil.which("yt-dlp")
    if not yt_dlp:
        r = ScrapeResult(
            False,
            "",
            0,
            "youtube_transcript",
            error="yt-dlp not installed",
            source_url=url,
            details={"video_id": video_id},
        )
        r.outcome = _result_outcome(r)
        return r

    with tempfile.TemporaryDirectory(prefix="anti-alecto-yt-") as tmpdir:
        out_tmpl = str(Path(tmpdir) / "%(id)s.%(ext)s")
        cmd = [
            yt_dlp,
            "--skip-download",
            "--no-playlist",
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs",
            "en,en-orig",
            "--sub-format",
            "vtt",
            "-o",
            out_tmpl,
            url,
        ]

        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=max(20, timeout_seconds * 2),
            )
        except subprocess.TimeoutExpired:
            elapsed_ms = int((time.perf_counter() - started) * 1000)
            r = ScrapeResult(
                False,
                "",
                0,
                "youtube_transcript",
                error="yt-dlp timeout",
                elapsed_ms=elapsed_ms,
                source_url=url,
                details={"video_id": video_id},
            )
            r.outcome = _result_outcome(r)
            return r

        subtitle_files = sorted(Path(tmpdir).glob(f"{video_id}*.vtt"))
        if not subtitle_files:
            elapsed_ms = int((time.perf_counter() - started) * 1000)
            r = ScrapeResult(
                False,
                "",
                0,
                "youtube_transcript",
                blocked=True,
                block_reason="SKIP_NO_TRANSCRIPT: no transcript available",
                elapsed_ms=elapsed_ms,
                source_url=url,
                details={
                    "video_id": video_id,
                    "yt_dlp_exit_code": proc.returncode,
                    "yt_dlp_stderr": (proc.stderr or "")[-400:],
                },
            )
            r.outcome = _result_outcome(r)
            return r

        def _pref_key(p: Path) -> tuple[int, str]:
            name = p.name.lower()
            if ".en-orig." in name:
                return (0, name)
            if ".en." in name:
                return (1, name)
            return (5, name)

        chosen = sorted(subtitle_files, key=_pref_key)[0]
        try:
            vtt_text = chosen.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            elapsed_ms = int((time.perf_counter() - started) * 1000)
            r = ScrapeResult(
                False,
                "",
                0,
                "youtube_transcript",
                error=f"subtitle read failed: {e}",
                elapsed_ms=elapsed_ms,
                source_url=url,
                details={"video_id": video_id, "subtitle_file": chosen.name},
            )
            r.outcome = _result_outcome(r)
            return r

        text = _clean_vtt_text(vtt_text)
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        if len(text) < 80:
            r = ScrapeResult(
                False,
                "",
                0,
                "youtube_transcript",
                blocked=True,
                block_reason="SKIP_NO_TRANSCRIPT: no transcript available",
                elapsed_ms=elapsed_ms,
                source_url=url,
                details={"video_id": video_id, "subtitle_file": chosen.name},
            )
            r.outcome = _result_outcome(r)
            return r

        r = ScrapeResult(
            True,
            text,
            len(text.split()),
            "youtube_transcript",
            elapsed_ms=elapsed_ms,
            source_url=url,
            details={
                "video_id": video_id,
                "subtitle_file": chosen.name,
                "yt_dlp_exit_code": proc.returncode,
            },
        )
        r.outcome = _result_outcome(r)
        return r


def _wikipedia_article_parts(url: str) -> tuple[str, str] | None:
    """Extract (host, article_title) for Wikipedia article URLs."""
    parsed = urlparse(url)
    host = (parsed.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]

    if not host.endswith(".wikipedia.org"):
        return None

    path = parsed.path or ""
    if not path.startswith("/wiki/"):
        return None

    raw_title = path[len("/wiki/") :].strip()
    if not raw_title:
        return None

    title = unquote(raw_title).replace("_", " ").strip()
    if not title:
        return None

    # Skip non-article namespaces (Special:, User:, Talk:, etc.).
    if ":" in title:
        namespace = title.split(":", 1)[0].strip().lower()
        if namespace in {
            "special",
            "talk",
            "user",
            "wikipedia",
            "file",
            "template",
            "help",
            "category",
            "portal",
            "draft",
            "module",
            "mediawiki",
            "book",
            "timedtext",
        }:
            return None

    return host, title


def scrape_wikipedia_article(
    url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 120,
) -> ScrapeResult:
    """Fetch Wikipedia article plaintext via MediaWiki API."""
    parts = _wikipedia_article_parts(url)
    if not parts:
        r = ScrapeResult(
            False,
            "",
            0,
            "wikipedia_api",
            blocked=True,
            block_reason="SKIP_WIKIPEDIA_UNSUPPORTED: wikipedia url is not an article page",
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r

    host, requested_title = parts
    started = time.perf_counter()
    api_url = (
        f"https://{host}/w/api.php?"
        + urlencode(
            {
                "action": "query",
                "prop": "extracts",
                "explaintext": "1",
                "redirects": "1",
                "format": "json",
                "titles": requested_title,
            }
        )
    )

    req = Request(
        api_url,
        headers={
            **_HTTP_HEADERS,
            "User-Agent": "anti-alecto/0.1 wikipedia-api",
            "Accept": "application/json,text/plain;q=0.9,*/*;q=0.5",
        },
    )

    try:
        with urlopen(req, timeout=timeout_seconds) as resp:
            status = getattr(resp, "status", None) or resp.getcode()
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read(5_000_000)
    except HTTPError as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "wikipedia_api",
            blocked=True,
            block_reason=f"HTTP {e.code}",
            status_code=e.code,
            elapsed_ms=elapsed_ms,
            source_url=api_url,
            details={"requested_url": url, "wikipedia_host": host},
        )
        r.outcome = _result_outcome(r)
        return r
    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "wikipedia_api",
            error=f"wikipedia api fetch failed: {e}",
            elapsed_ms=elapsed_ms,
            source_url=api_url,
            details={"requested_url": url, "wikipedia_host": host},
        )
        r.outcome = _result_outcome(r)
        return r

    try:
        payload = json.loads(_decode_body(raw, content_type))
    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "wikipedia_api",
            error=f"wikipedia api parse failed: {e}",
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=api_url,
            details={"requested_url": url, "wikipedia_host": host},
        )
        r.outcome = _result_outcome(r)
        return r

    pages = ((payload.get("query") or {}).get("pages") or {}) if isinstance(payload, dict) else {}
    page = next(iter(pages.values()), {}) if isinstance(pages, dict) else {}
    page_title = str(page.get("title") or requested_title).strip()
    extract = (page.get("extract") or "").strip()
    page_id = int(page.get("pageid") or 0)

    details = {
        "requested_url": url,
        "wikipedia_host": host,
        "article_title": page_title,
        "requested_title": requested_title,
        "wikipedia_api_url": api_url,
    }
    if page_id:
        details["page_id"] = page_id

    elapsed_ms = int((time.perf_counter() - started) * 1000)
    if not extract:
        r = ScrapeResult(
            False,
            "",
            0,
            "wikipedia_api",
            blocked=True,
            block_reason="empty extraction",
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=api_url,
            details=details,
        )
        r.outcome = _result_outcome(r)
        return r

    text = "\n".join(
        [
            "Wikipedia article capture",
            "",
            f"Article URL: {url}",
            f"Title: {page_title}" if page_title else "",
            "",
            "## Article extract (plaintext)",
            extract,
        ]
    ).strip()

    if len(text.strip()) < min_content_length:
        r = ScrapeResult(
            False,
            text,
            0,
            "wikipedia_api",
            blocked=True,
            block_reason=f"content too short ({len(text.strip())} chars)",
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=api_url,
            details=details,
        )
        r.outcome = _result_outcome(r)
        return r

    r = ScrapeResult(
        True,
        text,
        len(text.split()),
        "wikipedia_api",
        status_code=status,
        elapsed_ms=elapsed_ms,
        source_url=api_url,
        details=details,
    )
    r.outcome = _result_outcome(r)
    return r


def _reddit_thread_parts(url: str) -> tuple[str, str] | None:
    """Extract (subreddit, post_id) from Reddit thread URLs."""
    parsed = urlparse(url)
    host = (parsed.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]

    if host not in {"reddit.com", "old.reddit.com", "np.reddit.com"}:
        return None

    parts = [p for p in (parsed.path or "").split("/") if p]
    # /r/<sub>/comments/<id>/...
    if len(parts) >= 4 and parts[0] == "r" and parts[2] == "comments" and re.fullmatch(r"[a-z0-9]+", parts[3], re.I):
        return parts[1], parts[3]
    # /comments/<id>/...
    if len(parts) >= 2 and parts[0] == "comments" and re.fullmatch(r"[a-z0-9]+", parts[1], re.I):
        return "", parts[1]

    return None


def _reddit_clean_text(text: str) -> str:
    t = html.unescape(text or "")
    t = re.sub(r"\s+", " ", t).strip()
    return t


def _reddit_flatten_comments(children: list, max_comments: int = 120) -> list[dict]:
    out: list[dict] = []

    def walk(nodes: list, depth: int) -> None:
        for node in nodes or []:
            if len(out) >= max_comments:
                return
            if not isinstance(node, dict):
                continue
            if node.get("kind") != "t1":
                continue
            data = node.get("data") or {}
            body = _reddit_clean_text(data.get("body") or "")
            if body:
                out.append(
                    {
                        "author": data.get("author") or "[deleted]",
                        "score": int(data.get("score") or 0),
                        "body": body,
                        "depth": depth,
                        "id": data.get("id") or "",
                    }
                )
            replies = data.get("replies")
            if isinstance(replies, dict):
                walk(((replies.get("data") or {}).get("children") or []), depth + 1)

    walk(children, 0)
    return out


def _reddit_json_to_text(payload: list, requested_url: str) -> tuple[str, dict]:
    post_children = (((payload[0] or {}).get("data") or {}).get("children") or []) if payload else []
    if not post_children:
        return "", {"requested_url": requested_url}

    post_data = (post_children[0] or {}).get("data") or {}
    comments_children = (((payload[1] or {}).get("data") or {}).get("children") or []) if len(payload) > 1 else []
    comments = _reddit_flatten_comments(comments_children, max_comments=140)

    title = _reddit_clean_text(post_data.get("title") or "")
    subreddit = post_data.get("subreddit") or ""
    author = post_data.get("author") or ""
    score = int(post_data.get("score") or 0)
    total_comments = int(post_data.get("num_comments") or 0)
    permalink = post_data.get("permalink") or ""
    canonical = f"https://reddit.com{permalink}" if permalink.startswith("/") else requested_url
    selftext = _reddit_clean_text(post_data.get("selftext") or "")

    outbound_url = str(post_data.get("url_overridden_by_dest") or post_data.get("url") or "").strip()
    if outbound_url:
        out_host = (urlparse(outbound_url).hostname or "").lower()
        if out_host in {"reddit.com", "www.reddit.com", "old.reddit.com", "np.reddit.com", "redd.it"}:
            outbound_url = ""

    lines = [
        "Reddit thread capture",
        "",
        f"Thread URL: {canonical}",
        f"Subreddit: r/{subreddit}" if subreddit else "",
        f"Title: {title}" if title else "",
        f"Author: u/{author}" if author else "",
        f"Score: {score}",
        f"Comment count (reported): {total_comments}",
        f"Linked URL: {outbound_url}" if outbound_url else "",
        "",
    ]

    if selftext:
        lines.extend(["## Original post", selftext[:12000], ""])

    top_level = [c for c in comments if c.get("depth", 0) == 0]
    top_sorted = sorted(top_level, key=lambda x: x.get("score", 0), reverse=True)
    top_comment = top_sorted[0] if top_sorted else None

    if top_comment:
        lines.extend(
            [
                "## Top comment (highest-score top-level, verbatim)",
                f"u/{top_comment['author']} ({top_comment['score']}): {top_comment['body'][:2200]}",
                "",
            ]
        )

    if top_sorted:
        lines.append("## Prominent viewpoints (top-level comments)")
        for i, c in enumerate(top_sorted[:8], start=1):
            snippet = c["body"][:900]
            lines.append(f"{i}. ({c['score']}) u/{c['author']}: {snippet}")
        lines.append("")

    if comments:
        lines.append("## Thread discussion sample")
        for c in comments[:60]:
            indent = "  " * min(int(c.get("depth") or 0), 3)
            snippet = c["body"][:700]
            lines.append(f"{indent}- ({c['score']}) u/{c['author']}: {snippet}")
        lines.append("")

    text = "\n".join(x for x in lines if x is not None).strip()
    details = {
        "requested_url": requested_url,
        "canonical_thread_url": canonical,
        "subreddit": subreddit,
        "post_id": post_data.get("id") or "",
        "reported_comment_count": total_comments,
        "captured_comment_count": len(comments),
    }
    if top_comment:
        details["top_comment_author"] = top_comment["author"]
        details["top_comment_score"] = int(top_comment["score"])
        details["top_comment_excerpt"] = top_comment["body"][:500]
    if outbound_url:
        details["outbound_url"] = outbound_url
        details["reference_type"] = "reddit_outbound"
    return text, details


def _reddit_fetch_json_endpoint(
    endpoint: str,
    requested_url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 120,
) -> ScrapeResult:
    started = time.perf_counter()
    req = Request(
        endpoint,
        headers={
            **_HTTP_HEADERS,
            "User-Agent": "anti-alecto/0.1 reddit-json",
            "Accept": "application/json,text/plain;q=0.9,*/*;q=0.5",
        },
    )

    try:
        with urlopen(req, timeout=timeout_seconds) as resp:
            status = getattr(resp, "status", None) or resp.getcode()
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read(5_000_000)
    except HTTPError as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "reddit_json",
            blocked=True,
            block_reason=f"HTTP {e.code}",
            status_code=e.code,
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r
    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "reddit_json",
            error=f"reddit json fetch failed: {e}",
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r

    try:
        payload = json.loads(_decode_body(raw, content_type))
    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "reddit_json",
            error=f"reddit json parse failed: {e}",
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r

    text, details = _reddit_json_to_text(payload if isinstance(payload, list) else [], requested_url)
    elapsed_ms = int((time.perf_counter() - started) * 1000)
    if not text or len(text.strip()) < min_content_length:
        r = ScrapeResult(
            False,
            text or "",
            0,
            "reddit_json",
            blocked=True,
            block_reason="empty extraction",
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details=details,
        )
        r.outcome = _result_outcome(r)
        return r

    r = ScrapeResult(
        True,
        text,
        len(text.split()),
        "reddit_json",
        status_code=status,
        elapsed_ms=elapsed_ms,
        source_url=endpoint,
        details=details,
    )
    r.outcome = _result_outcome(r)
    return r


def _reddit_rss_to_text(xml_text: str, requested_url: str) -> tuple[str, dict]:
    import xml.etree.ElementTree as ET

    if not xml_text.strip():
        return "", {"requested_url": requested_url}

    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return "", {"requested_url": requested_url}

    ns = {
        "a": "http://www.w3.org/2005/Atom",
        "dc": "http://purl.org/dc/elements/1.1/",
    }

    title = (root.findtext("a:title", default="", namespaces=ns) or "").strip()
    entries = root.findall("a:entry", ns)

    lines = [
        "Reddit thread capture (RSS fallback)",
        "",
        f"Thread URL: {requested_url}",
        f"Feed title: {title}" if title else "",
        "",
        "## Entries",
    ]

    count = 0
    for e in entries[:80]:
        etitle = (e.findtext("a:title", default="", namespaces=ns) or "").strip()
        author = (e.findtext("a:author/a:name", default="", namespaces=ns) or "").strip()
        content = (e.findtext("a:content", default="", namespaces=ns) or "").strip()
        if not content and not etitle:
            continue
        content = _reddit_clean_text(content)[:1200]
        lines.append(f"- {etitle}" if etitle else "- (untitled)")
        if author:
            lines.append(f"  author: {author}")
        if content:
            lines.append(f"  {content}")
        count += 1

    text = "\n".join(x for x in lines if x is not None).strip()
    return text, {"requested_url": requested_url, "rss_entries": count}


def _reddit_fetch_rss_endpoint(
    endpoint: str,
    requested_url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 120,
) -> ScrapeResult:
    started = time.perf_counter()
    req = Request(
        endpoint,
        headers={
            **_HTTP_HEADERS,
            "User-Agent": "anti-alecto/0.1 reddit-rss",
            "Accept": "application/atom+xml,application/rss+xml,application/xml,text/xml;q=0.9,*/*;q=0.5",
        },
    )

    try:
        with urlopen(req, timeout=timeout_seconds) as resp:
            status = getattr(resp, "status", None) or resp.getcode()
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read(5_000_000)
    except HTTPError as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "reddit_rss",
            blocked=True,
            block_reason=f"HTTP {e.code}",
            status_code=e.code,
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r
    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "reddit_rss",
            error=f"reddit rss fetch failed: {e}",
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r

    text, details = _reddit_rss_to_text(_decode_body(raw, content_type), requested_url)
    elapsed_ms = int((time.perf_counter() - started) * 1000)
    if not text or len(text.strip()) < min_content_length:
        r = ScrapeResult(
            False,
            text or "",
            0,
            "reddit_rss",
            blocked=True,
            block_reason="empty extraction",
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=endpoint,
            details=details,
        )
        r.outcome = _result_outcome(r)
        return r

    r = ScrapeResult(
        True,
        text,
        len(text.split()),
        "reddit_rss",
        status_code=status,
        elapsed_ms=elapsed_ms,
        source_url=endpoint,
        details=details,
    )
    r.outcome = _result_outcome(r)
    return r


def scrape_reddit_thread(
    url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 120,
) -> ScrapeResult:
    """Scrape Reddit thread via public JSON endpoints, then RSS fallback."""
    parts = _reddit_thread_parts(url)
    if not parts:
        r = ScrapeResult(
            False,
            "",
            0,
            "reddit_json",
            blocked=True,
            block_reason="SKIP_REDDIT_UNSUPPORTED: reddit url is not a thread",
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r

    subreddit, post_id = parts
    json_candidates = [
        f"https://www.reddit.com/comments/{post_id}/.json?raw_json=1&sort=top&limit=500",
    ]
    if subreddit:
        json_candidates.insert(
            0,
            f"https://www.reddit.com/r/{subreddit}/comments/{post_id}/.json?raw_json=1&sort=top&limit=500",
        )

    attempts: list[ScrapeResult] = []
    for endpoint in json_candidates:
        r = _reddit_fetch_json_endpoint(
            endpoint,
            requested_url=url,
            timeout_seconds=timeout_seconds,
            min_content_length=min(min_content_length, 80),
        )
        attempts.append(r)
        if r.success:
            r.details = {**(r.details or {}), "requested_url": url, "json_endpoint": endpoint}
            r.outcome = _result_outcome(r)
            r.diagnostics = [_diag_entry(a) for a in attempts]
            return r

    rss_candidates = [f"https://www.reddit.com/comments/{post_id}/.rss"]
    if subreddit:
        rss_candidates.insert(0, f"https://www.reddit.com/r/{subreddit}/comments/{post_id}/.rss")

    for endpoint in rss_candidates:
        r = _reddit_fetch_rss_endpoint(
            endpoint,
            requested_url=url,
            timeout_seconds=timeout_seconds,
            min_content_length=min(min_content_length, 80),
        )
        attempts.append(r)
        if r.success:
            r.details = {**(r.details or {}), "requested_url": url, "rss_endpoint": endpoint}
            r.outcome = _result_outcome(r)
            r.diagnostics = [_diag_entry(a) for a in attempts]
            return r

    final = _pick_final_failure(attempts) or ScrapeResult(
        False,
        "",
        0,
        "reddit_json",
        error="reddit thread scrape failed",
        source_url=url,
    )
    final.diagnostics = [_diag_entry(a) for a in attempts]
    final.outcome = _result_outcome(final)
    return final


def _x_status_parts(url: str) -> tuple[str, str] | None:
    """Extract (username, status_id) from x.com/twitter status URL."""
    parsed = urlparse(url)
    host = (parsed.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]

    if host not in {"x.com", "twitter.com", "mobile.twitter.com"}:
        return None

    parts = [p for p in (parsed.path or "").split("/") if p]
    if len(parts) < 3:
        return None

    for i, p in enumerate(parts):
        if p == "status" and i >= 1 and i + 1 < len(parts):
            user = parts[i - 1]
            sid = parts[i + 1]
            if sid.isdigit() and user:
                return user, sid

    return None


def _xcancel_status_url(url: str) -> str | None:
    parts = _x_status_parts(url)
    if not parts:
        return None
    user, sid = parts
    return f"https://xcancel.com/{user}/status/{sid}"


def _clean_x_markdown(text: str) -> str:
    """Trim X proxy markdown to post/conversation signals and remove timeline noise."""
    if not text:
        return ""

    t = text
    if "Markdown Content:" in t:
        t = t.split("Markdown Content:", 1)[1]

    # Keep content up to common non-thread sections.
    cut_markers = [
        "## New to X?",
        "## Trending now",
        "## What’s happening",
        "## What's happening",
        "Create account",
        "Terms of Service",
        "© 20",
    ]
    cut = len(t)
    for m in cut_markers:
        idx = t.find(m)
        if idx != -1:
            cut = min(cut, idx)
    t = t[:cut]

    # Strip image/link clutter while preserving text.
    t = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^\)]*\)", r"\1", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    t = t.strip()

    if t and not t.lower().startswith("x thread capture"):
        t = f"X thread capture\n\n{t}"
    return t


def scrape_x_proxy_thread(
    url: str,
    timeout_seconds: int = 25,
    min_content_length: int = 120,
) -> ScrapeResult:
    """Scrape X status using xcancel first, then fallback to r.jina mirror."""
    status_parts = _x_status_parts(url)
    if not status_parts:
        r = ScrapeResult(
            False,
            "",
            0,
            "x_proxy",
            blocked=True,
            block_reason="SKIP_X_UNSUPPORTED: x url is not a status thread",
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r

    user, sid = status_parts
    attempts: list[ScrapeResult] = []

    xcancel_url = _xcancel_status_url(url)
    if xcancel_url:
        r_xc = scrape_http_static(
            xcancel_url,
            timeout_seconds=timeout_seconds,
            min_content_length=min(min_content_length, 80),
            strategy="x_proxy_xcancel",
        )
        # Xcancel may return anti-bot verify pages with enough text; treat those as blocked.
        verify_text = (r_xc.text or "").lower()
        if r_xc.success and (
            "verifying your request" in verify_text
            or "sorry this pages exist in order to keep the service usable" in verify_text
        ):
            r_xc = ScrapeResult(
                False,
                "",
                0,
                "x_proxy_xcancel",
                blocked=True,
                block_reason="xcancel verification gate",
                status_code=r_xc.status_code,
                source_url=xcancel_url,
                details={"requested_url": url},
            )
            r_xc.outcome = _result_outcome(r_xc)
        attempts.append(r_xc)
        if r_xc.success:
            cleaned = _clean_x_markdown(r_xc.text)
            if len(cleaned.strip()) >= 80:
                r_xc.text = cleaned
                r_xc.word_count = len(cleaned.split())
                r_xc.details = {**(r_xc.details or {}), "requested_url": url, "proxy_url": xcancel_url}
                r_xc.outcome = _result_outcome(r_xc)
                r_xc.diagnostics = [_diag_entry(a) for a in attempts]
                return r_xc

    # Fallback mirror that often returns conversation markdown for public status pages.
    jina_url = f"https://r.jina.ai/http://x.com/{user}/status/{sid}"
    r_jina = scrape_http_static(
        jina_url,
        timeout_seconds=timeout_seconds,
        min_content_length=min(min_content_length, 80),
        strategy="x_proxy_jina",
    )
    attempts.append(r_jina)
    if r_jina.success:
        cleaned = _clean_x_markdown(r_jina.text)
        if len(cleaned.strip()) >= 80:
            r_jina.text = cleaned
            r_jina.word_count = len(cleaned.split())
            r_jina.details = {
                **(r_jina.details or {}),
                "requested_url": url,
                "proxy_url": jina_url,
                "proxy_fallback": "r.jina.ai",
            }
            r_jina.outcome = _result_outcome(r_jina)
            r_jina.diagnostics = [_diag_entry(a) for a in attempts]
            return r_jina

    final = _pick_final_failure(attempts) or ScrapeResult(
        False,
        "",
        0,
        "x_proxy",
        error="x proxy attempts failed",
        source_url=url,
        details={"requested_url": url},
    )
    final.diagnostics = [_diag_entry(a) for a in attempts]
    final.outcome = _result_outcome(final)
    return final


def _is_github_host(url: str) -> bool:
    host = (urlparse(url).netloc or "").lower()
    return host in {"github.com", "www.github.com"}


def _github_owner_repo(url: str) -> tuple[str, str, list[str]] | None:
    parsed = urlparse(url)
    host = (parsed.netloc or "").lower()
    if host not in {"github.com", "www.github.com"}:
        return None

    parts = [p for p in (parsed.path or "").split("/") if p]
    if len(parts) < 2:
        return None

    owner, repo = parts[0], parts[1]
    if owner.lower() in _GITHUB_RESERVED_ROOTS:
        return None
    if repo.lower().endswith(".git"):
        repo = repo[:-4]
    if not owner or not repo:
        return None
    return owner, repo, parts


def _github_marker(parts: list[str]) -> tuple[str | None, int]:
    for idx, p in enumerate(parts[2:], start=2):
        if p in {"blob", "tree", "issues", "pull"}:
            return p, idx
    return None, -1


def scrape_github_blob_raw(
    url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 120,
) -> ScrapeResult:
    parsed = _github_owner_repo(url)
    if not parsed:
        r = ScrapeResult(False, "", 0, "github_blob_raw", error="not a github repo url", source_url=url)
        r.outcome = _result_outcome(r)
        return r

    owner, repo, parts = parsed
    kind, idx = _github_marker(parts)
    if kind != "blob":
        r = ScrapeResult(False, "", 0, "github_blob_raw", error="not a github blob url", source_url=url)
        r.outcome = _result_outcome(r)
        return r

    rest = parts[idx + 1 :]
    if len(rest) < 2:
        r = ScrapeResult(False, "", 0, "github_blob_raw", error="blob url missing ref/path", source_url=url)
        r.outcome = _result_outcome(r)
        return r

    candidates: list[str] = []
    seen: set[str] = set()
    split_end = min(4, len(rest))
    for split in range(1, split_end):
        ref = "/".join(rest[:split]).strip()
        file_path = "/".join(rest[split:]).strip()
        if not ref or not file_path:
            continue
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{file_path}"
        if raw_url in seen:
            continue
        seen.add(raw_url)
        candidates.append(raw_url)

    attempts: list[ScrapeResult] = []
    for raw_url in candidates:
        r = scrape_http_static(
            raw_url,
            timeout_seconds=timeout_seconds,
            min_content_length=min(min_content_length, 40),
            strategy="github_blob_raw",
        )
        attempts.append(r)
        if r.success:
            r.strategy = "github_blob_raw"
            r.details = {
                **(r.details or {}),
                "requested_url": url,
                "raw_candidate_url": raw_url,
            }
            r.outcome = _result_outcome(r)
            return r

    final = _pick_final_failure(attempts) or ScrapeResult(
        False,
        "",
        0,
        "github_blob_raw",
        error="blob raw fetch failed",
        source_url=url,
    )
    final.strategy = "github_blob_raw"
    final.details = {
        **(final.details or {}),
        "requested_url": url,
        "candidate_count": len(candidates),
    }
    final.outcome = _result_outcome(final)
    return final


def scrape_github_tree_readme(
    url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 120,
) -> ScrapeResult:
    parsed = _github_owner_repo(url)
    if not parsed:
        r = ScrapeResult(False, "", 0, "github_tree_readme", error="not a github repo url", source_url=url)
        r.outcome = _result_outcome(r)
        return r

    owner, repo, parts = parsed
    kind, idx = _github_marker(parts)
    if kind != "tree":
        r = ScrapeResult(False, "", 0, "github_tree_readme", error="not a github tree url", source_url=url)
        r.outcome = _result_outcome(r)
        return r

    rest = parts[idx + 1 :]
    if len(rest) < 1:
        r = ScrapeResult(
            False,
            "",
            0,
            "github_tree_readme",
            blocked=True,
            block_reason="SKIP_GITHUB_NO_README: no readable file at tree path",
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r

    candidates: list[str] = []
    seen: set[str] = set()
    split_end = min(4, len(rest)) + 1
    for split in range(1, split_end):
        ref = "/".join(rest[:split]).strip()
        subdir = "/".join(rest[split:]).strip("/")
        if not ref:
            continue
        rel_paths = [
            f"{subdir}/README.md" if subdir else "README.md",
            f"{subdir}/readme.md" if subdir else "readme.md",
            f"{subdir}/README" if subdir else "README",
            f"{subdir}/docs/README.md" if subdir else "docs/README.md",
        ]
        for rel in rel_paths:
            rel = rel.strip("/")
            if not rel:
                continue
            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{rel}"
            if raw_url in seen:
                continue
            seen.add(raw_url)
            candidates.append(raw_url)

    attempts: list[ScrapeResult] = []
    for raw_url in candidates:
        r = scrape_http_static(
            raw_url,
            timeout_seconds=timeout_seconds,
            min_content_length=min(min_content_length, 40),
            strategy="github_tree_readme",
        )
        attempts.append(r)
        if r.success:
            r.strategy = "github_tree_readme"
            r.details = {
                **(r.details or {}),
                "requested_url": url,
                "readme_candidate_url": raw_url,
            }
            r.outcome = _result_outcome(r)
            return r

    r = ScrapeResult(
        False,
        "",
        0,
        "github_tree_readme",
        blocked=True,
        block_reason="SKIP_GITHUB_NO_README: no readable file at tree path",
        source_url=url,
        details={"requested_url": url, "candidate_count": len(candidates)},
    )
    r.outcome = _result_outcome(r)
    return r


def _github_issue_api_by_number(
    owner: str,
    repo: str,
    issue_number: str,
    requested_url: str,
    timeout_seconds: int = 20,
) -> ScrapeResult:
    endpoint = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    req = Request(
        endpoint,
        headers={
            **_HTTP_HEADERS,
            "Accept": "application/vnd.github+json",
        },
    )

    try:
        with urlopen(req, timeout=timeout_seconds) as resp:
            status = getattr(resp, "status", None) or resp.getcode()
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read(2_000_000)
    except HTTPError as e:
        elapsed = 0
        r = ScrapeResult(
            False,
            "",
            0,
            "github_issue_api",
            blocked=True,
            block_reason=f"HTTP {e.code}",
            status_code=e.code,
            elapsed_ms=elapsed,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r
    except Exception as e:
        r = ScrapeResult(
            False,
            "",
            0,
            "github_issue_api",
            error=f"github api error: {e}",
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r

    try:
        payload = json.loads(_decode_body(raw, content_type))
    except Exception as e:
        r = ScrapeResult(
            False,
            "",
            0,
            "github_issue_api",
            error=f"github api parse failed: {e}",
            status_code=status,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r

    title = (payload.get("title") or "").strip()
    body = (payload.get("body") or "").strip()
    state = payload.get("state") or ""
    author = ((payload.get("user") or {}).get("login") or "")
    html_url = payload.get("html_url") or requested_url

    lines = [
        f"# GitHub issue: {owner}/{repo}#{issue_number}",
        f"Title: {title}" if title else "",
        f"State: {state}" if state else "",
        f"Author: {author}" if author else "",
        f"URL: {html_url}",
        "",
    ]
    if body:
        lines.extend(["## Body", body[:20000], ""])

    comments_url = payload.get("comments_url")
    comments_count = int(payload.get("comments") or 0)
    if comments_url and comments_count > 0:
        sep = "&" if "?" in comments_url else "?"
        comments_req = Request(
            f"{comments_url}{sep}per_page=10",
            headers={
                **_HTTP_HEADERS,
                "Accept": "application/vnd.github+json",
            },
        )
        try:
            with urlopen(comments_req, timeout=timeout_seconds) as resp:
                c_raw = resp.read(2_000_000)
                c_type = resp.headers.get("Content-Type", "")
            comments = json.loads(_decode_body(c_raw, c_type))
            if isinstance(comments, list) and comments:
                lines.append("## Top comments")
                for c in comments[:10]:
                    user = ((c.get("user") or {}).get("login") or "")
                    c_body = (c.get("body") or "").strip()
                    if not c_body:
                        continue
                    lines.append(f"- {user}: {c_body[:1200]}")
        except Exception:
            pass

    text = "\n".join(x for x in lines if x is not None).strip()
    if len(text) < 80:
        r = ScrapeResult(
            False,
            "",
            0,
            "github_issue_api",
            blocked=True,
            block_reason="empty extraction",
            status_code=status,
            source_url=endpoint,
            details={"requested_url": requested_url},
        )
        r.outcome = _result_outcome(r)
        return r

    r = ScrapeResult(
        True,
        text,
        len(text.split()),
        "github_issue_api",
        status_code=status,
        source_url=endpoint,
        details={"requested_url": requested_url},
    )
    r.outcome = _result_outcome(r)
    return r


def scrape_github_issue_api(url: str, timeout_seconds: int = 20) -> ScrapeResult:
    parsed = _github_owner_repo(url)
    if not parsed:
        r = ScrapeResult(False, "", 0, "github_issue_api", error="not a github repo url", source_url=url)
        r.outcome = _result_outcome(r)
        return r

    owner, repo, parts = parsed
    kind, idx = _github_marker(parts)
    if kind != "issues":
        r = ScrapeResult(False, "", 0, "github_issue_api", error="not a github issues url", source_url=url)
        r.outcome = _result_outcome(r)
        return r

    rest = parts[idx + 1 :]
    if not rest or not re.fullmatch(r"\d+", rest[0]):
        r = ScrapeResult(
            False,
            "",
            0,
            "github_issue_api",
            blocked=True,
            block_reason="SKIP_GITHUB_LISTING: issue listing page (not a single issue)",
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r

    return _github_issue_api_by_number(owner, repo, rest[0], url, timeout_seconds=timeout_seconds)


def scrape_github_pull(url: str, timeout_seconds: int = 20, min_content_length: int = 120) -> ScrapeResult:
    parsed = _github_owner_repo(url)
    if not parsed:
        r = ScrapeResult(False, "", 0, "github_pr_patch", error="not a github repo url", source_url=url)
        r.outcome = _result_outcome(r)
        return r

    owner, repo, parts = parsed
    kind, idx = _github_marker(parts)
    if kind != "pull":
        r = ScrapeResult(False, "", 0, "github_pr_patch", error="not a github pull url", source_url=url)
        r.outcome = _result_outcome(r)
        return r

    rest = parts[idx + 1 :]
    if not rest or not re.fullmatch(r"\d+", rest[0]):
        r = ScrapeResult(
            False,
            "",
            0,
            "github_pr_patch",
            blocked=True,
            block_reason="SKIP_GITHUB_LISTING: pull request listing page (not a single PR)",
            source_url=url,
        )
        r.outcome = _result_outcome(r)
        return r

    pr_num = rest[0]
    attempts: list[ScrapeResult] = []

    patch_url = f"https://github.com/{owner}/{repo}/pull/{pr_num}.patch"
    r_patch = scrape_http_static(
        patch_url,
        timeout_seconds=timeout_seconds,
        min_content_length=min(min_content_length, 40),
        strategy="github_pr_patch",
    )
    attempts.append(r_patch)
    if r_patch.success:
        r_patch.strategy = "github_pr_patch"
        r_patch.details = {
            **(r_patch.details or {}),
            "requested_url": url,
            "patch_url": patch_url,
        }
        r_patch.outcome = _result_outcome(r_patch)
        return r_patch

    r_api = _github_issue_api_by_number(owner, repo, pr_num, url, timeout_seconds=timeout_seconds)
    r_api.strategy = "github_pr_api"
    attempts.append(r_api)
    if r_api.success:
        r_api.details = {
            **(r_api.details or {}),
            "requested_url": url,
            "pull_number": pr_num,
        }
        r_api.outcome = _result_outcome(r_api)
        return r_api

    final = _pick_final_failure(attempts) or ScrapeResult(
        False,
        "",
        0,
        "github_pr_patch",
        error="pull scrape failed",
        source_url=url,
    )
    final.details = {
        **(final.details or {}),
        "requested_url": url,
        "pull_number": pr_num,
    }
    final.outcome = _result_outcome(final)
    return final


def scrape_github_url(
    url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 120,
) -> ScrapeResult:
    """GitHub-specific flow for blob/tree/issues/pull/profile/listing paths."""
    parsed_url = urlparse(url)
    parts = [p for p in (parsed_url.path or "").split("/") if p]

    if len(parts) == 1:
        if parts[0].lower() in _GITHUB_RESERVED_ROOTS:
            r = ScrapeResult(
                False,
                "",
                0,
                "github_listing",
                blocked=True,
                block_reason="SKIP_GITHUB_LISTING: GitHub listing/index page",
                source_url=url,
            )
        else:
            r = ScrapeResult(
                False,
                "",
                0,
                "github_profile",
                blocked=True,
                block_reason="SKIP_GITHUB_PROFILE: user/org profile page (not a single artifact)",
                source_url=url,
            )
        r.outcome = _result_outcome(r)
        r.diagnostics = [_diag_entry(r)]
        return r

    parsed = _github_owner_repo(url)
    if not parsed:
        r = scrape_http_static(
            url,
            timeout_seconds=timeout_seconds,
            min_content_length=min_content_length,
            strategy="github_page",
        )
        r.diagnostics = [_diag_entry(r)]
        return r

    _owner, _repo, parts = parsed
    attempts: list[ScrapeResult] = []

    kind, _idx = _github_marker(parts)

    if kind == "blob":
        r = scrape_github_blob_raw(url, timeout_seconds=timeout_seconds, min_content_length=min_content_length)
        attempts.append(r)
    elif kind == "tree":
        r = scrape_github_tree_readme(url, timeout_seconds=timeout_seconds, min_content_length=min_content_length)
        attempts.append(r)
    elif kind == "issues":
        r = scrape_github_issue_api(url, timeout_seconds=timeout_seconds)
        attempts.append(r)
    elif kind == "pull":
        r = scrape_github_pull(url, timeout_seconds=timeout_seconds, min_content_length=min_content_length)
        attempts.append(r)
    else:
        r = scrape_github_readme(url, timeout_seconds=timeout_seconds)
        attempts.append(r)

    reason = r.block_reason or r.error or ""
    if r.success or str(reason).startswith("SKIP_"):
        r.diagnostics = [_diag_entry(a) for a in attempts]
        return r

    # Fallback 1: try the canonical page extraction.
    r_page = scrape_http_static(
        url,
        timeout_seconds=timeout_seconds,
        min_content_length=min_content_length,
        strategy="github_page",
    )
    attempts.append(r_page)
    if r_page.success:
        r_page.diagnostics = [_diag_entry(a) for a in attempts]
        return r_page

    # Fallback 2: repo README fallback (best effort for odd paths).
    r_readme = scrape_github_readme(url, timeout_seconds=timeout_seconds)
    attempts.append(r_readme)
    if r_readme.success:
        r_readme.diagnostics = [_diag_entry(a) for a in attempts]
        return r_readme

    final = _pick_final_failure(attempts) or r
    final.diagnostics = [_diag_entry(a) for a in attempts]
    final.outcome = _result_outcome(final)
    return final


def _github_repo_from_url(url: str) -> tuple[str, str] | None:
    parsed = _github_owner_repo(url)
    if not parsed:
        return None
    owner, repo, _parts = parsed
    return owner, repo


def scrape_github_readme(url: str, timeout_seconds: int = 20, min_content_length: int = 120) -> ScrapeResult:
    """GitHub fallback: fetch repo README.md via raw endpoints."""
    repo = _github_repo_from_url(url)
    if not repo:
        return ScrapeResult(
            False,
            "",
            0,
            "github_readme",
            error="not a github repo url",
            source_url=url,
        )

    owner, name = repo
    branches = ["HEAD", "main", "master"]
    files = ["README.md", "readme.md"]

    attempts: list[ScrapeResult] = []
    for branch in branches:
        for fname in files:
            raw_url = f"https://raw.githubusercontent.com/{owner}/{name}/{branch}/{fname}"
            r = scrape_http_static(
                raw_url,
                timeout_seconds=timeout_seconds,
                min_content_length=min(min_content_length, 120),
                strategy="github_readme",
            )
            attempts.append(r)
            if r.success:
                r.strategy = "github_readme"
                r.details = {
                    **(r.details or {}),
                    "requested_url": url,
                    "readme_candidate_url": raw_url,
                }
                r.outcome = _result_outcome(r)
                return r

    # Return the most informative failure.
    prioritized = _pick_final_failure(attempts)
    if prioritized is None:
        prioritized = ScrapeResult(
            False,
            "",
            0,
            "github_readme",
            error="README fetch failed",
            source_url=url,
        )
    prioritized.strategy = "github_readme"
    prioritized.details = {
        **(prioritized.details or {}),
        "requested_url": url,
    }
    prioritized.outcome = _result_outcome(prioritized)
    return prioritized


def scrape_archive_wayback(
    url: str,
    timeout_seconds: int = 20,
    min_content_length: int = 120,
) -> ScrapeResult:
    """Archive fallback via Wayback Machine availability API."""
    started = time.perf_counter()

    api_url = f"https://archive.org/wayback/available?{urlencode({'url': url})}"
    req = Request(api_url, headers=_HTTP_HEADERS)

    try:
        with urlopen(req, timeout=timeout_seconds) as resp:
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read(2_000_000)
            status = getattr(resp, "status", None) or resp.getcode()
    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "archive_wayback",
            error=f"wayback lookup failed: {e}",
            elapsed_ms=elapsed_ms,
            source_url=api_url,
            details={"requested_url": url},
        )
        r.outcome = _result_outcome(r)
        return r

    try:
        payload = json.loads(_decode_body(raw, content_type))
    except Exception as e:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "archive_wayback",
            error=f"wayback parse failed: {e}",
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=api_url,
            details={"requested_url": url},
        )
        r.outcome = _result_outcome(r)
        return r

    closest = (payload.get("archived_snapshots") or {}).get("closest") or {}
    snapshot_url = closest.get("url")
    if not snapshot_url:
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        r = ScrapeResult(
            False,
            "",
            0,
            "archive_wayback",
            error="no archive snapshot",
            status_code=status,
            elapsed_ms=elapsed_ms,
            source_url=api_url,
            details={"requested_url": url},
        )
        r.outcome = _result_outcome(r)
        return r

    # Fetch the snapshot itself with static extraction.
    r = scrape_http_static(
        snapshot_url,
        timeout_seconds=timeout_seconds,
        min_content_length=min(min_content_length, 120),
        strategy="archive",
    )
    if r.success:
        r.strategy = "archive"
        r.details = {
            **(r.details or {}),
            "requested_url": url,
            "snapshot_url": snapshot_url,
            "wayback_api_url": api_url,
        }
        r.outcome = _result_outcome(r)
        return r

    # Preserve that we found archive metadata, even if extraction failed.
    r.strategy = "archive"
    r.details = {
        **(r.details or {}),
        "requested_url": url,
        "snapshot_url": snapshot_url,
        "wayback_api_url": api_url,
    }
    if not r.error and not r.block_reason:
        r.error = "archive snapshot extraction failed"
    r.outcome = _result_outcome(r)
    return r


def _pick_final_failure(attempts: list[ScrapeResult]) -> ScrapeResult | None:
    if not attempts:
        return None

    def score(r: ScrapeResult) -> int:
        outcome = r.outcome or _result_outcome(r)
        if outcome == "gated_captcha":
            return 100
        if outcome == "needs_login":
            return 95
        if outcome == "rate_limited":
            return 90
        if outcome == "not_found":
            return 85
        if r.blocked:
            return 80
        if r.error:
            return 70
        return 10

    return max(attempts, key=score)


def scrape_url(
    url: str,
    timeout_seconds: int = 30,
    playwright_wait_ms: int = 3000,
    min_content_length: int = 200,
    cache_ttl_hours: int = 24,
) -> ScrapeResult:
    """User-first attempt ladder with diagnostics.

    Flow:
    1) fresh cache
    2) GitHub dedicated flow (github.com)
    3) Hacker News item JSON flow (news.ycombinator.com/item?id=...)
    4) Reddit thread JSON flow (reddit thread URLs)
    5) X thread proxy flow (x.com/twitter status URLs)
    6) YouTube transcript (video URLs)
    7) Wikipedia article API flow (/wiki/... article pages)
    8) light HTTP + static extraction
    9) browser render fallback
    10) github README fallback (github only)
    11) archive fallback (Wayback)
    12) stale cache fallback
    """
    attempts: list[ScrapeResult] = []

    category, preflight_reason = classify_url(url)
    if category in {"session_app", "login_page"}:
        preflight = ScrapeResult(
            False,
            "",
            0,
            "preflight",
            blocked=True,
            block_reason=f"SKIP_INELIGIBLE: {preflight_reason}",
            source_url=url,
            details={"category": category},
        )
        preflight.outcome = _result_outcome(preflight)
        preflight.diagnostics = [_diag_entry(preflight)]
        return preflight

    # For thread captures, prefer fresh domain-specific extraction over cache so
    # top-comment/topic fields stay current and structurally complete.
    skip_fresh_cache = bool(_hn_item_parts(url) or _reddit_thread_parts(url))

    if not skip_fresh_cache:
        cached = _load_cache(url, ttl_hours=cache_ttl_hours, allow_stale=False)
        if cached:
            cached.diagnostics = [_diag_entry(cached)]
            return cached

    # GitHub URLs use a dedicated flow for blob/tree/issues/pull/profile/listing paths.
    if _is_github_host(url):
        r_gh = scrape_github_url(
            url,
            timeout_seconds=timeout_seconds,
            min_content_length=min_content_length,
        )
        if r_gh.success:
            _save_cache(url, r_gh)
        return r_gh

    # Hacker News item URLs: prefer JSON extraction (submission + top comments).
    if _hn_item_parts(url):
        r_hn = scrape_hn_thread(
            url,
            timeout_seconds=timeout_seconds,
            min_content_length=min_content_length,
        )
        attempts.append(r_hn)
        if r_hn.success:
            _save_cache(url, r_hn)
            r_hn.diagnostics = [_diag_entry(r) for r in attempts]
            return r_hn

    # Reddit thread URLs: prefer JSON extraction (captures OP + comments/opinions).
    if _reddit_thread_parts(url):
        r_reddit = scrape_reddit_thread(
            url,
            timeout_seconds=timeout_seconds,
            min_content_length=min_content_length,
        )
        attempts.append(r_reddit)
        if r_reddit.success:
            _save_cache(url, r_reddit)
            r_reddit.diagnostics = [_diag_entry(r) for r in attempts]
            return r_reddit
        reason = (r_reddit.block_reason or r_reddit.error or "")
        if reason.startswith("SKIP_REDDIT_"):
            r_reddit.diagnostics = [_diag_entry(r) for r in attempts]
            return r_reddit

    # X/Twitter status URLs: use proxy flow to capture the post + conversation context.
    if _x_status_parts(url):
        r_x = scrape_x_proxy_thread(
            url,
            timeout_seconds=timeout_seconds,
            min_content_length=min_content_length,
        )
        attempts.append(r_x)
        if r_x.success:
            _save_cache(url, r_x)
            r_x.diagnostics = [_diag_entry(r) for r in attempts]
            return r_x
        reason = (r_x.block_reason or r_x.error or "")
        if reason.startswith("SKIP_X_"):
            r_x.diagnostics = [_diag_entry(r) for r in attempts]
            return r_x

    # YouTube video URLs: prefer transcript extraction over HTML body scraping.
    if _youtube_video_id(url):
        r_yt = scrape_youtube_transcript(url, timeout_seconds=timeout_seconds)
        attempts.append(r_yt)
        if r_yt.success:
            _save_cache(url, r_yt)
            r_yt.diagnostics = [_diag_entry(r) for r in attempts]
            return r_yt
        reason = (r_yt.block_reason or r_yt.error or "")
        if reason.startswith("SKIP_NO_TRANSCRIPT:"):
            r_yt.diagnostics = [_diag_entry(r) for r in attempts]
            return r_yt

    # Wikipedia article URLs: fetch plaintext directly from MediaWiki API.
    if _wikipedia_article_parts(url):
        r_wiki = scrape_wikipedia_article(
            url,
            timeout_seconds=max(10, min(timeout_seconds, 25)),
            min_content_length=min(min_content_length, 80),
        )
        attempts.append(r_wiki)
        if r_wiki.success:
            _save_cache(url, r_wiki)
            r_wiki.diagnostics = [_diag_entry(r) for r in attempts]
            return r_wiki
        reason = (r_wiki.block_reason or r_wiki.error or "")
        if reason.startswith("SKIP_WIKIPEDIA_"):
            r_wiki.diagnostics = [_diag_entry(r) for r in attempts]
            return r_wiki

    r_http = scrape_http_static(url, timeout_seconds=timeout_seconds, min_content_length=min_content_length)
    attempts.append(r_http)
    if r_http.success:
        _save_cache(url, r_http)
        r_http.diagnostics = [_diag_entry(r) for r in attempts]
        return r_http

    # Escalate to rendered browser pass for JS pages or blocked/partial static responses.
    r_play = scrape_playwright(
        url,
        timeout_ms=timeout_seconds * 1000,
        wait_ms=playwright_wait_ms,
        min_content_length=min_content_length,
    )
    attempts.append(r_play)
    if r_play.success:
        _save_cache(url, r_play)
        r_play.diagnostics = [_diag_entry(r) for r in attempts]
        return r_play

    # GitHub-specific high-value fallback: direct README from raw endpoint.
    if _github_repo_from_url(url):
        r_gh = scrape_github_readme(url, timeout_seconds=timeout_seconds)
        attempts.append(r_gh)
        if r_gh.success:
            _save_cache(url, r_gh)
            r_gh.diagnostics = [_diag_entry(r) for r in attempts]
            return r_gh

    # Archive fallback (Wayback) before stale cache.
    if _is_archive_safe_url(url):
        r_archive = scrape_archive_wayback(
            url,
            timeout_seconds=max(10, min(timeout_seconds, 25)),
            min_content_length=min_content_length,
        )
        attempts.append(r_archive)
        if r_archive.success:
            _save_cache(url, r_archive)
            r_archive.diagnostics = [_diag_entry(r) for r in attempts]
            return r_archive

    # Final fallback: stale cache, if available.
    stale = _load_cache(url, ttl_hours=cache_ttl_hours, allow_stale=True)
    if stale:
        attempts.append(stale)
        stale.diagnostics = [_diag_entry(r) for r in attempts]
        return stale

    final = _pick_final_failure(attempts) or ScrapeResult(
        False,
        "",
        0,
        "scrape",
        error="all attempts failed",
        source_url=url,
    )
    final.diagnostics = [_diag_entry(r) for r in attempts]
    final.outcome = _result_outcome(final)
    return final
