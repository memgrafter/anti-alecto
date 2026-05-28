# Scrape Attempt Flow (User-First)

This document defines the **user-facing** scraping strategy for anti-alecto.

> Goal: capture what a normal user can read in a browser, with minimal breakage on bot-protected sites.

## Constraints

- No API-first routing for normal scrape attempts.
- Prefer cheap/fast attempts before expensive browser rendering.
- Treat CAPTCHA/challenge pages as a separate flow, not a generic retry error.

## Per-URL Attempt Ladder

Use this order for each URL:

1. **Preflight classification**
   - Classify URL as `public` vs `session_app`/`login_page` classes.
   - Short-circuit obvious session-gated pages as ineligible (no live scrape attempts).

2. **Cache check + de-dup guard**
   - If we have a fresh successful scrape artifact, return it.
   - Skip re-scraping exact canonical duplicates (`url_normalized`) that already reached a terminal state.
   - If a normalized prefix is already known as walled/paywalled, mark new matching URLs as ineligible to avoid repeated churn.

3. **Reddit thread JSON fetch (thread URLs only)**
   - For Reddit thread URLs (`/r/<sub>/comments/<id>`), fetch public JSON first.
   - Extract OP plus representative comments/replies so summaries can capture key viewpoints and disagreements.

4. **X thread proxy fetch (status URLs only)**
   - For `x.com/<user>/status/<id>` (or Twitter equivalents), try `xcancel.com` proxy first.
   - If xcancel is gated, fallback to mirrored markdown capture.
   - Preserve thread/conversation text so summaries can capture opinion clusters and disagreement.

5. **YouTube transcript fetch (video URLs only)**
   - For `youtube.com/watch`, `youtube.com/shorts`, and `youtu.be/*`, attempt transcript extraction first.
   - If transcript is unavailable, mark as skip (`no transcript available`) instead of scrape failure.

6. **Light HTTP fetch**
   - `curl`/HTTP client with browser-like headers.
   - Follow redirects, capture status/final URL/body hash.

7. **Static extraction**
   - Extract main content from returned HTML.
   - If content quality is sufficient, mark success and stop.

8. **Protection / JS-shell detection**
   - Detect CAPTCHA/challenge/login wall/paywall/empty shell pages.
   - Decide whether to escalate to browser render or exit as gated.

9. **Browser render (agentic route)**
   - Use Playwright with realistic browser context.
   - Wait for content selectors/network idle.
   - Extract rendered text.

10. **CAPTCHA branch (human-in-the-loop)**
   - If CAPTCHA appears, mark `gated_captcha`.
   - Optional manual solve in active session, then retry extraction once.
   - Do not loop endlessly.

11. **Cached/archive fallback**
   - Try known prior snapshots (project cache, Wayback/archive mirrors).
   - Archive lookup should be limited to public `http(s)` URLs (avoid localhost/intranet/private hosts).
   - Return with provenance (`live`, `cached`, `archived`).

12. **Manual rescue fallback (operator-in-the-loop)**
   - If automation repeatedly fails on high-value pages, use `aa rescue` / `aa paste`.
   - Default to `paste` capture mode (simplest setup): open URL, copy content, paste into CLI.
   - Playwriter is an optional alternative capture mode label (`--capture-mode playwriter`) when content was sourced via Playwriter MCP.
   - Optional image OCR path (`aa paste --image`) for screenshot-only captures.

## GitHub-specific Flow

GitHub pages are often anti-bot sensitive. Route by path shape:

1. `/owner/repo/blob/<ref>/<path>` → fetch `raw.githubusercontent.com` file directly.
2. `/owner/repo/tree/<ref>[/subdir]` → try README candidates in that directory via raw URLs.
3. `/owner/repo/issues/<n>` → fetch issue content via GitHub API.
4. `/owner/repo/pull/<n>` (including `/files`) → fetch `.patch`, then API fallback.
5. `/owner/repo/issues` and `/owner` profile pages → skip as index/profile (not a single artifact).
6. Fallbacks: static page extraction, then repo README fetch.

## Retry + Budget Rules

- Max attempts per URL: **4–6**
- Max wall-clock budget per URL: **60–120s**
- Max browser render attempts: **1** (unless manual solve path is active)
- Back off quickly on repeated `rate_limited`/`gated_captcha`

## Required Typed Outcomes

Return one of:

- `success_live`
- `success_rendered`
- `success_cached`
- `success_archived`
- `gated_captcha`
- `needs_login`
- `rate_limited`
- `not_found`
- `transient_error`

## Diagnostics to Store

For every attempt, store:

- strategy name
- source URL used for that attempt (e.g. raw README URL, Wayback snapshot URL)
- success/failure
- failure reason (typed)
- status code (if any)
- block/challenge markers detected
- extracted length / quality signal
- timestamps + elapsed time

This enables smarter retries and domain-specific tuning over time.
