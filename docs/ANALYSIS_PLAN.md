# Corpus Analysis & Prioritization Plan (anti-alecto)

## 1) Goal

Build a repeatable analysis layer that turns the growing URL corpus into an actionable queue:

- what to read now
- what to keep for reference
- what to trim/deprioritize
- what failed URLs are worth retrying

The system must run incrementally as new links are added, with periodic full recomputation.

---

## 2) Product Outcomes

Each URL should get a recommended action:

- `read_now`
- `read_later`
- `archive_only`
- `trim_candidate`
- `retry_candidate`

And every run should produce:

1. topic clusters
2. ranked priority queue
3. trim queue (safe/dry-run first)
4. retry queue for likely recoverable fails
5. daily + weekly reports

---

## 3) Scope and Phases

### Phase 0 (baseline instrumentation)
- Add analysis tables and run tracking.
- Add CLI scaffolding (`aa analyze ...`).
- Ship a deterministic, rules-based baseline (no heavy ML dependency yet).

### Phase 1 (incremental features + scoring)
- Extract stable per-URL features from summaries, metadata, statuses, and reference graph.
- Compute actionable scores (priority, novelty, trim likelihood, retry likelihood).
- Persist recommendations per URL.

### Phase 2 (topic clustering)
- Add clustering over summary text (initially TF-IDF + MiniBatchKMeans/HDBSCAN-like fallback).
- Label clusters with top keywords + representative URLs.
- Expose cluster drilldown in reports.

### Phase 3 (reporting + automation)
- Daily brief and weekly strategy report artifacts.
- Add scheduled runs (cron/launchd/GitHub Action/local script).
- Add confidence tracking and run diffs.

### Phase 4 (optional semantic upgrade)
- Add embedding-based clustering/reranking (if quality gain justifies dependency/runtime).

---

## 4) Data Model Changes

Update `sql/schema.sql` + migration logic in `src/anti_alecto/db.py`.

## New Tables

### `analysis_runs`
Tracks run metadata/versioning.

- `id INTEGER PK`
- `run_type TEXT` (`refresh`, `cluster`, `prioritize`, `trim`, `report`, `full`)
- `config_hash TEXT`
- `started_at TEXT`
- `finished_at TEXT`
- `success INTEGER`
- `notes TEXT`

### `url_analysis`
One current analysis snapshot per URL (latest run wins).

- `url_id INTEGER PK` (FK urls.id)
- `feature_version TEXT`
- `cluster_id TEXT NULL`
- `cluster_confidence REAL`
- `priority_score REAL`
- `novelty_score REAL`
- `redundancy_score REAL`
- `trim_score REAL`
- `retry_score REAL`
- `recommended_action TEXT`
- `recommended_reason TEXT`
- `analysis_run_id INTEGER`
- `updated_at TEXT`

### `cluster_summaries`
Stores cluster-level descriptors.

- `cluster_id TEXT PK`
- `analysis_run_id INTEGER`
- `label TEXT`
- `top_keywords_json TEXT`
- `url_count INTEGER`
- `representative_url_ids_json TEXT`
- `median_priority REAL`
- `updated_at TEXT`

### `url_analysis_history` (optional but recommended)
Append-only snapshots for drift tracking.

---

## 5) Feature Extraction (Incremental)

Implement in new module: `src/anti_alecto/analyze.py`

## Inputs
- `urls` table (status, domain, triage/scrape reasons, strategy, updated_at)
- `summaries` table (summary markdown/frontmatter)
- `url_references` graph (inbound/outbound count and type)

## Features

### Quality/utility features
- summarized? (`status='summarized'`)
- scrape strategy quality hints (`reddit_json`, `hn_json`, `wikipedia_api`, etc.)
- summary density proxy (word count, key-entity count)
- scrape quality frontmatter if present

### Freshness features
- age since `updated_at`
- recency bucket (0-2d / 3-7d / 8-30d / >30d)

### Novelty/redundancy features
- lexical similarity to existing summaries in same domain/topic
- near-duplicate flag by normalized URL + summary overlap

### Graph features
- inbound refs count
- outbound refs count
- whether discovered via HN/Reddit thread
- simple centrality proxy (in_degree + weighted ref types)

### Failure recovery features
- failed status + failure family (`captcha`, `cloudflare`, `429`, `empty`)
- known recoverability heuristics (e.g. archive snapshots available)

---

## 6) Scoring + Decision Policy

Initial transparent weighted model (configurable in YAML):

```text
priority_score =
  0.30 * novelty
+ 0.25 * actionability
+ 0.20 * source_quality
+ 0.15 * graph_value
+ 0.10 * freshness
- 0.25 * redundancy_penalty
- 0.20 * stale_penalty
```

```text
trim_score =
  0.45 * redundancy
+ 0.20 * age
+ 0.20 * low_signal
+ 0.15 * low_graph_value
```

```text
retry_score =
  recoverability_pattern_weight + historical_success_prior - hard_block_penalty
```

## Action Mapping
- high priority + low redundancy => `read_now`
- medium priority => `read_later`
- low priority + non-duplicate => `archive_only`
- high trim score => `trim_candidate`
- failed + high retry score => `retry_candidate`

All recommendations include a short reason string for auditability.

---

## 7) Clustering Strategy (repeatable)

## V1 (deterministic baseline)
- Text source: summary body (not raw scrape text)
- Vectorization: TF-IDF (ngram 1-2, capped vocab)
- Clustering: MiniBatchKMeans with `k` selected by corpus size heuristic
- Labeling: top TF-IDF terms + representative docs

## V2 (optional)
- embeddings model (local sentence-transformer)
- HDBSCAN/UMAP or agglomerative clustering
- improved topic naming via LLM cluster summarizer

Store cluster assignment + confidence in `url_analysis` and cluster metadata in `cluster_summaries`.

---

## 8) CLI Surface

Add commands in `src/anti_alecto/cli.py`:

- `./bin/aa analyze refresh [--since-run <id>] [--full]`
- `./bin/aa analyze cluster [--full] [--k <n>]`
- `./bin/aa analyze prioritize`
- `./bin/aa analyze trim --dry-run [--apply]`
- `./bin/aa analyze retry-candidates [--limit N]`
- `./bin/aa analyze report --daily|--weekly`

### Recommended Routine
- after scrape runs: `aa analyze refresh && aa analyze prioritize`
- weekly: `aa analyze cluster --full && aa analyze report --weekly`

---

## 9) Reporting Artifacts

Write artifacts under `.cache/analysis/` and optional committed summaries in `digests/analysis/`:

- `daily-YYYY-MM-DD.md`
- `weekly-YYYY-WW.md`
- `priority_queue.tsv`
- `trim_candidates.tsv`
- `retry_candidates.tsv`
- `clusters.tsv`

## Daily report sections
- new high-priority URLs
- top retry candidates
- biggest new clusters/topics

## Weekly report sections
- topic growth/decay
- over-indexed topics (possible trim)
- under-covered topics (possible ingest targets)
- source/domain quality trends

---

## 10) Trimming Policy (safe by default)

1. Always start with `--dry-run`.
2. Mark `trim_candidate` in analysis table only (no deletion).
3. After cooling period (e.g., 14 days), allow optional archival step.
4. Keep at least one canonical URL per near-duplicate cluster.
5. Keep a reversible trail (history table + reason).

No destructive delete in MVP.

---

## 11) Retry Intelligence

Generate retry queues from `scrape_failed` with recoverability hints:

- archive snapshot likely available
- domain now supported by scraper improvements
- transient error classes (429/network)

Exclude low-yield hard blockers unless policy changes.

---

## 12) Implementation Tasks by File

- `sql/schema.sql`
  - add analysis tables/indexes
- `src/anti_alecto/db.py`
  - migration + CRUD methods for analysis tables
- `src/anti_alecto/analyze.py` (new)
  - feature extraction
  - scoring
  - clustering
  - report generation
- `src/anti_alecto/cli.py`
  - `analyze` subcommands
- `tests/`
  - scoring tests
  - clustering determinism tests (seeded)
  - recommendation mapping tests

---

## 13) Acceptance Criteria

MVP is complete when:

1. `aa analyze refresh` updates `url_analysis` incrementally.
2. `aa analyze cluster --full` assigns >=95% of summarized URLs to clusters.
3. `aa analyze prioritize` outputs deterministic recommendations.
4. `aa analyze trim --dry-run` produces explainable trim list.
5. Weekly report is generated in one command and includes cluster + queue sections.
6. End-to-end runtime stays practical on current corpus (target: <2 min refresh, <5 min weekly full).

---

## 14) Rollout Plan

## Week 1
- Schema + DB migrations
- `analyze refresh` + scoring + recommendations
- daily report

## Week 2
- clustering + weekly report
- trim dry-run and retry-candidate queue
- test hardening + docs

## Week 3 (optional)
- embedding upgrade experiment
- compare quality vs runtime and decide keep/discard

---

## 15) Risks and Mitigations

- **Over-complex scoring early** → start simple + transparent weights in config.
- **Cluster instability** → seed algorithms, store `feature_version`, compare run diffs.
- **False-positive trim** → no deletes in MVP, cooling window + canonical retention.
- **Runtime creep** → incremental first; full recompute only weekly.

---

## 16) First Command Sequence (once implemented)

```bash
./bin/aa analyze refresh
./bin/aa analyze prioritize
./bin/aa analyze report --daily

# weekly
./bin/aa analyze cluster --full
./bin/aa analyze trim --dry-run
./bin/aa analyze retry-candidates --limit 50
./bin/aa analyze report --weekly
```

This yields a repeatable operating loop that keeps the corpus useful as it grows, instead of turning into a passive dump.
