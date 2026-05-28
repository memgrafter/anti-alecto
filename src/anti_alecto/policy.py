"""URL/status policy helpers."""

from __future__ import annotations

import re
from urllib.parse import parse_qs, urlparse


_INELIGIBLE_REASON_RE = re.compile(
    r"\b(auth|login|sign\s*in|session|account\s+dashboard|private\s+edit|login-gated|access-gated|gated)\b",
    re.I,
)

_WALLED_REASON_RE = re.compile(
    r"\b(paywall|subscription|billing|login|auth|session|access\s+denied|ineligible)\b",
    re.I,
)

# Growing static list of hosts that are not durable scrape targets.
_ALWAYS_INELIGIBLE_HOSTS = {
    "discord.com",
    "www.discord.com",
    "canary.discord.com",
    "ptb.discord.com",
    "discord.gg",
    "discordapp.com",
    "www.discordapp.com",
    "console.firebase.google.com",
    "app.devin.ai",
}


def is_ineligible_url(url: str) -> bool:
    """True when URL is clearly session/auth-gated and not scrapeable as a durable artifact."""
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    path = parsed.path or ""

    if host in _ALWAYS_INELIGIBLE_HOSTS:
        return True

    # Search result pages are navigational, not durable artifacts.
    if (host == "google.com" or host.endswith(".google.com")) and path.startswith("/search"):
        return True

    if host == "gemini.google.com" and path.startswith("/app/"):
        return True
    if host == "claude.ai" and re.match(r"^/(login|chat|new)(/|$)", path, re.I):
        return True
    if host == "cloud.digitalocean.com" and path.startswith("/account"):
        return True
    if host == "openrouter.ai" and path.startswith("/activity"):
        return True
    if host == "docs.google.com" and re.match(r"^/document/d/[^/]+/edit", path, re.I):
        return True
    if re.search(r"/(login|signin|logout|oauth|auth)(/|$)", path, re.I):
        return True

    return False


def is_ineligible_reason(reason: str | None) -> bool:
    if not reason:
        return False
    return bool(_INELIGIBLE_REASON_RE.search(reason))


def is_walled_reason(reason: str | None) -> bool:
    if not reason:
        return False
    return bool(_WALLED_REASON_RE.search(reason))


def dedupe_prefix(url: str) -> str:
    """Coarse prefix key used to avoid re-scraping obviously duplicated/walled areas."""
    parsed = urlparse(url)
    scheme = parsed.scheme or "https"
    host = (parsed.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]

    parts = [p for p in (parsed.path or "").split("/") if p]

    # Hacker News item pages: dedupe by exact item id, not global /item path.
    if host == "news.ycombinator.com" and (parsed.path or "") == "/item":
        q = parse_qs(parsed.query or "")
        item_id = (q.get("id") or [""])[0]
        if item_id.isdigit():
            return f"{scheme}://news.ycombinator.com/item?id={item_id}"

    # Reddit thread URLs: dedupe by exact post id.
    if host in {"reddit.com", "old.reddit.com", "np.reddit.com"}:
        if len(parts) >= 4 and parts[0] == "r" and parts[2] == "comments" and parts[3]:
            return f"{scheme}://reddit.com/r/{parts[1]}/comments/{parts[3]}"
        if len(parts) >= 2 and parts[0] == "comments" and parts[1]:
            return f"{scheme}://reddit.com/comments/{parts[1]}"

    # GitHub: repo-level prefix is a good coarse key.
    if host == "github.com" and len(parts) >= 2:
        return f"{scheme}://github.com/{parts[0]}/{parts[1]}"

    # X status: dedupe by exact status path, not whole account.
    if host in {"x.com", "twitter.com"} and len(parts) >= 3:
        if parts[1] == "status" and parts[2].isdigit():
            return f"{scheme}://x.com/{parts[0]}/status/{parts[2]}"

    # Generic: host + first path segment.
    if parts:
        return f"{scheme}://{host}/{parts[0]}"
    return f"{scheme}://{host}/"


def classify_skip_status(url: str, reason: str | None = None) -> str:
    """Map skip-like decisions to triaged_skip vs ineligible."""
    if is_ineligible_url(url) or is_ineligible_reason(reason):
        return "ineligible"
    return "triaged_skip"
