# anti-alecto — Design

## What it does
Captures browser tabs, triages them by relevance, scrapes the keepers, and stores searchable summaries. Turns 200 screaming tabs into "here are the 6 things worth your time."

## Pipeline

```
dump.json → ingest → triage (FlatMachine) → scrape (user-first attempt flow) → summarize (FlatMachine) → store (SQLite)
```

### 1. Ingest
- Reads chrome extension JSON dumps (`{title, date, tabs: [{title, url, win}]}`)
- Normalizes URLs (strip tracking params, canonicalize)
- Deduplicates against existing store
- Records source dump for provenance

### 2. Triage (FlatMachine)
- Batch operation: sends N url+title pairs to an agent
- Agent categorizes each: `keep` / `skip` / `defer` with one-line reason
- Uses configurable interest profile (what topics matter to this user)
- Updates DB status

### 3. Scrape (user-first attempt flow)
Current implementation is a strategy chain. Target behavior is an attempt ladder tuned for user-visible content:

1. Preflight URL classification (public vs session/login page)
2. Cache hit check
3. Light HTTP fetch + static extraction
4. Escalate to Playwright render if JS shell or partial content
5. CAPTCHA/challenge branch (human-in-the-loop, no infinite retries)
6. Cached/archive fallback (Wayback for public URLs) when live fetch is gated

Additional notes:
- No API-first routing for normal user scraping.
- GitHub handling should include direct repo `README.md` fetch from raw endpoints as a high-value fallback.
- Store per-attempt diagnostics to support typed failures and smarter retries.

### 4. Summarize (FlatMachine)
- Existing pipeline: summarizer → judge → frontmatter extraction
- Already has retry loops and validation
- Produces structured markdown with YAML frontmatter

### 5. Store (SQLite)
- Single `anti-alecto.db` file
- Full history: what was ingested, triaged, scraped, summarized
- Queryable by domain, tags, date, status, content type

## Schema

```sql
-- Track imported dump files
CREATE TABLE dumps (
    id INTEGER PRIMARY KEY,
    filename TEXT UNIQUE NOT NULL,
    imported_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    tab_count INTEGER NOT NULL DEFAULT 0
);

-- Every URL we've ever seen
CREATE TABLE urls (
    id INTEGER PRIMARY KEY,
    url TEXT UNIQUE NOT NULL,
    url_normalized TEXT NOT NULL,
    title TEXT NOT NULL DEFAULT '',
    domain TEXT NOT NULL DEFAULT '',
    dump_id INTEGER REFERENCES dumps(id),
    added_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),

    -- Pipeline status: pending → triaged_keep|triaged_skip|triaged_defer → scraping → scraped|scrape_failed → summarized|summarize_failed
    status TEXT NOT NULL DEFAULT 'pending',
    triage_reason TEXT,
    scrape_strategy TEXT,       -- http_static|playwright|github_readme|cache
    scrape_failed_reason TEXT,
    summarize_failed_reason TEXT,

    updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);

-- Raw scraped content
CREATE TABLE content (
    id INTEGER PRIMARY KEY,
    url_id INTEGER UNIQUE NOT NULL REFERENCES urls(id),
    raw_text TEXT NOT NULL,
    word_count INTEGER NOT NULL DEFAULT 0,
    strategy_used TEXT NOT NULL,
    scraped_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);

-- Summaries with structured metadata
CREATE TABLE summaries (
    id INTEGER PRIMARY KEY,
    url_id INTEGER UNIQUE NOT NULL REFERENCES urls(id),
    summary_md TEXT NOT NULL,
    frontmatter_json TEXT,      -- parsed YAML as JSON for querying
    tldr TEXT,
    tags TEXT,                  -- comma-separated for simple queries
    content_type TEXT,
    durability TEXT,
    reference_style TEXT,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);

CREATE INDEX idx_urls_status ON urls(status);
CREATE INDEX idx_urls_domain ON urls(domain);
CREATE INDEX idx_urls_normalized ON urls(url_normalized);
CREATE INDEX idx_summaries_tags ON summaries(tags);
CREATE INDEX idx_summaries_content_type ON summaries(content_type);
```

## CLI

```
aa ingest <dump.json>         Import a chrome tab dump
aa ingest --all               Import all new dumps from dumps/
aa triage                     Triage pending URLs (runs FlatMachine)
aa scrape                     Scrape triaged-keep URLs
aa scrape --limit 10          Scrape up to 10
aa run                        Full pipeline: ingest --all → triage → scrape
aa status                     Pipeline stats (pending/triaged/scraped/failed)
aa search <query>             Search summaries
aa digest                     Show today's new summaries
aa failed                     Show failed scrapes with reasons
aa retry                      Re-attempt failed scrapes
```

## Project layout

```
anti-alecto/
├── pyproject.toml            # deps, entry point
├── install.sh                # one-command setup (venv + deps + playwright browsers)
├── config.yml                # skip patterns, interest profile, batch size
├── profiles.yml              # flatagent model profiles
├── machines/
│   ├── triage.yml            # batch URL triage
│   └── scrape.yml            # scrape + summarize single URL
├── agents/
│   ├── triager.yml           # keep/skip/defer categorizer
│   ├── summarizer.yml        # content summarizer
│   ├── judge.yml             # summary quality judge
│   └── frontmatter.yml       # metadata extractor
├── src/anti_alecto/
│   ├── __init__.py
│   ├── cli.py                # entry point
│   ├── db.py                 # SQLite store (init, migrate, query)
│   ├── ingest.py             # chrome dump parser + URL normalization
│   ├── scrape.py             # strategy chain + block detection
│   ├── hooks.py              # FlatMachine hooks (triage + scrape)
│   └── config.py             # load config.yml
├── sql/
│   └── schema.sql
├── dumps/                    # chrome JSON dumps (gitignored)
├── tests/
├── README.md
└── .gitignore
```

## Configuration

```yaml
# config.yml
skip_patterns:
  - "^https?://(www\\.)?youtube\\.com"
  - "^https?://(www\\.)?discord\\.com"
  - "^https?://(www\\.)?x\\.com"
  - "^https?://(www\\.)?twitter\\.com"
  - "^https?://.*\\.google\\.com/(chrome|search)"
  - "^chrome-extension://"
  - "^chrome://"

# Tracking params to strip during normalization
tracking_params:
  - utm_source
  - utm_medium
  - utm_campaign
  - utm_term
  - utm_content
  - fbclid
  - gclid
  - ref

# Triage settings
triage:
  batch_size: 30              # URLs per triage call
  interest_profile: |
    Software engineering, developer tools, AI/ML, programming languages,
    systems programming, open source projects, startups, productivity.
    Less interested in: gaming, crypto, social media drama, celebrity news.

# Scrape settings
scrape:
  timeout_seconds: 30
  max_concurrent: 3
  playwright_wait_ms: 3000    # wait for JS rendering
  min_content_length: 200     # chars, below = likely blocked
  cache_ttl_hours: 24         # use cached successful scrape before refetch

# Jina (legacy placeholder)
jina:
  enabled: false
```

## Block detection signals

Checked after every scrape attempt:

| Signal | Detection |
|--------|-----------|
| HTTP 403/429/503 | Status code |
| Cloudflare | "cf-browser-verification", "Just a moment" in title |
| Captcha | "captcha", "challenge-platform", "verify you are human" |
| Access denied | "access denied", "forbidden" in body/title |
| Paywall | "subscribe to continue", "premium content" |
| Empty | Extracted text < min_content_length |
| Login wall | "sign in to continue", "create an account" |

Failed scrapes are marked with the specific reason so retry logic can be smarter later.

See `SCRAPING_FLOW.md` for the detailed decision flow, budget rules, and GitHub-specific order.

## Principles
- **SQLite is the source of truth** — flat files are exports, not the store
- **Idempotent everything** — re-importing a dump, re-triaging, re-scraping are all safe
- **Fail loudly, recover gracefully** — block detection marks failures with reasons, never saves garbage
- **One install.sh, one venv** — no ambient dependencies, no "works on my machine"
- **Config over code** — skip patterns, interest profile, model selection all in YAML
