# anti-alecto

Tame the tab fury. Capture browser tabs, triage by relevance, scrape the keepers, store searchable summaries.

*Alecto — one of the Furies, she who never rests, relentlessly pursuing and consuming attention.*

## Install

```bash
./install.sh           # create venv, install deps, download Chromium
./install.sh --local   # use local flatagents SDK from ~/code/flatagents
```

## Usage

```bash
# Drop chrome tab dumps into dumps/
cp ~/Downloads/chrome-exit*.json dumps/

# Full pipeline: ingest → triage → scrape
./bin/aa run

# Or step by step
./bin/aa ingest                    # import all new dumps
./bin/aa ingest dumps/tabs.json    # import specific file
./bin/aa add "https://example.com/article"   # add one URL + triage + scrape
./bin/aa add "https://example.com/article" --no-process   # add only
./bin/aa triage                    # AI categorizes: keep/skip/defer
./bin/aa scrape                    # scrape + summarize keepers
./bin/aa scrape --limit 5          # limit batch size

# Query
./bin/aa status                    # pipeline stats
./bin/aa digest                    # recent summaries
./bin/aa search "playwright"       # search by keyword
./bin/aa failed                    # see what broke
./bin/aa retry                     # reset failures for re-scrape
```

## Quickstart: manual rescue / paste mode

Use this for captcha/cloudflare/login walls where automated scraping fails.

**Default and simplest setup: `paste` mode.**

```bash
# Interactive blocked-failure queue (paste content per URL)
./bin/aa rescue --open --limit 10

# For each URL:
# 1) open it in your browser
# 2) copy the rendered text
# 3) paste into terminal, then end with: ::end

# One-off manual paste for a specific URL id
./bin/aa paste --id 123

# One-off manual paste for a new URL
./bin/aa paste --url "https://example.com/article"

# Pipe content directly
pbpaste | ./bin/aa paste --url "https://example.com/article" --stdin

# Optional image OCR (uses local tesseract if installed)
./bin/aa paste --url "https://example.com/screenshot" --image ~/Desktop/capture.png
```

Playwriter is an **optional alternative capture mode label** when you sourced content via Playwriter MCP:

```bash
./bin/aa rescue --open --capture-mode playwriter
./bin/aa paste --id 123 --capture-mode playwriter
```

## How it works

```
dump.json → ingest → triage (LLM) → scrape (cache → HTTP/static → Playwright → fallbacks) → summarize (LLM) → SQLite
```

1. **Ingest** — parse chrome extension JSON, normalize URLs, dedup, skip known-bad patterns
2. **Triage** — LLM batch-categorizes URLs as keep/skip/defer based on your interest profile
3. **Scrape** — user-first attempt ladder (preflight classify → cache → light HTTP/static extract → Playwright render → cached/archive fallback)
4. **Block detection** — Cloudflare, captcha, paywall, login wall, empty page → marked as failed with reason
5. **Strategy diagnostics** — every scrape stores per-strategy attempt diagnostics, including source URL used (e.g. `http:empty -> playwright:captcha -> github_readme:ok`)
6. **Summarize** — LLM generates structured summary → judge validates quality → extract frontmatter metadata
7. **Store** — SQLite with full pipeline history, searchable by tags/domain/content type

See `SCRAPING_FLOW.md` for the detailed scrape attempt flow (including GitHub-specific README fallback).

## Configuration

Edit `config.yml`:
- `skip_patterns` — URLs to auto-skip (regex)
- `triage.interest_profile` — what topics matter to you
- `scrape.timeout_seconds` — per-URL timeout
- `scrape.cache_ttl_hours` — fresh cache window before refetch
- `profiles.yml` — LLM model/provider selection

## Chrome tab dumps

Expected JSON format (from tab export extensions):
```json
{
  "title": "session-name",
  "date": "4/6/2026",
  "tabs": [
    {"title": "Page Title", "url": "https://...", "win": "12345"}
  ]
}
```

## Project layout

```
anti-alecto/
├── bin/aa                    # CLI entry point
├── config.yml                # user configuration
├── profiles.yml              # LLM model profiles
├── machines/                 # FlatMachine workflows
│   ├── triage.yml            # batch URL triage
│   └── scrape.yml            # scrape + summarize
├── agents/                   # FlatAgent prompts
│   ├── triager.yml
│   ├── summarizer.yml
│   ├── judge.yml
│   └── frontmatter.yml
├── src/anti_alecto/          # Python package
│   ├── cli.py                # CLI commands
│   ├── db.py                 # SQLite store
│   ├── ingest.py             # chrome dump parser
│   ├── scrape.py             # strategy chain + block detection
│   ├── hooks.py              # FlatMachine hooks
│   └── config.py             # config loader
├── sql/schema.sql            # DB schema
├── dumps/                    # chrome JSON dumps (gitignored)
└── install.sh                # one-command setup
```

## Incremental Progress as of 2026-04-18

Current pipeline snapshot:
- Total URLs tracked: **370**
- Summarized: **293**
- Scrape failed: **9**
- Ineligible: **23**
- Skipped: **26**
- Triaged skip: **18**
- Triaged defer: **1**

Key improvements delivered incrementally:
- Domain-aware scraping for **GitHub**, **YouTube transcripts**, **Reddit threads**, and **X status threads**.
- Canonical URL normalization + DB uniqueness to prevent duplicate re-scrapes.
- `ineligible` status for truly gated/session-only pages (instead of treating everything as scrape failures).
- Manual operator workflows:
  - `./bin/aa rescue` for blocked queues
  - `./bin/aa paste` for direct text/image capture
- Jina-based recovery pass added substantial additional summaries from previously blocked pages.
