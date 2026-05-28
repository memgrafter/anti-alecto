-- anti-alecto schema v1
PRAGMA journal_mode=WAL;
PRAGMA busy_timeout=5000;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS dumps (
    id INTEGER PRIMARY KEY,
    filename TEXT UNIQUE NOT NULL,
    imported_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    tab_count INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY,
    url TEXT UNIQUE NOT NULL,
    url_normalized TEXT NOT NULL,
    title TEXT NOT NULL DEFAULT '',
    domain TEXT NOT NULL DEFAULT '',
    dump_id INTEGER REFERENCES dumps(id),
    added_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    status TEXT NOT NULL DEFAULT 'pending',
    triage_reason TEXT,
    scrape_strategy TEXT,
    scrape_failed_reason TEXT,
    summarize_failed_reason TEXT,
    updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);

-- NOTE: raw scrape artifacts are stored on disk under digests/raw/ and not in SQLite.

CREATE TABLE IF NOT EXISTS summaries (
    id INTEGER PRIMARY KEY,
    url_id INTEGER UNIQUE NOT NULL REFERENCES urls(id),
    summary_md TEXT NOT NULL,
    frontmatter_json TEXT,
    tldr TEXT,
    tags TEXT,
    content_type TEXT,
    durability TEXT,
    reference_style TEXT,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);

-- Directed URL reference graph (e.g. HN item -> linked article, Reddit thread -> linked URL).
CREATE TABLE IF NOT EXISTS url_references (
    id INTEGER PRIMARY KEY,
    source_url_id INTEGER NOT NULL REFERENCES urls(id),
    target_url_id INTEGER NOT NULL REFERENCES urls(id),
    ref_type TEXT NOT NULL DEFAULT 'outbound',
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    UNIQUE(source_url_id, target_url_id, ref_type)
);

CREATE INDEX IF NOT EXISTS idx_urls_status ON urls(status);
CREATE INDEX IF NOT EXISTS idx_urls_domain ON urls(domain);
CREATE UNIQUE INDEX IF NOT EXISTS idx_urls_normalized_unique ON urls(url_normalized);
CREATE INDEX IF NOT EXISTS idx_urls_normalized ON urls(url_normalized);
CREATE INDEX IF NOT EXISTS idx_summaries_tags ON summaries(tags);
CREATE INDEX IF NOT EXISTS idx_summaries_content_type ON summaries(content_type);
CREATE INDEX IF NOT EXISTS idx_url_refs_source ON url_references(source_url_id);
CREATE INDEX IF NOT EXISTS idx_url_refs_target ON url_references(target_url_id);
