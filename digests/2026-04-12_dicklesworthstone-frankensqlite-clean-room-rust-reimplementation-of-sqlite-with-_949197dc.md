---
url: https://github.com/Dicklesworthstone/frankensqlite
title: 'Dicklesworthstone/frankensqlite: Clean-room Rust reimplementation of SQLite with MVCC page-level versioning'
scraped_at: '2026-04-12T07:42:10Z'
word_count: 20991
raw_file: raw/2026-04-12_dicklesworthstone-frankensqlite-clean-room-rust-reimplementation-of-sqlite-with-_949197dc.txt
tldr: FrankenSQLite is a Rust, SQLite-compatible database engine repo that aims for page-level MVCC, SSI, and RaptorQ-based durability, but the current runnable path is still a hybrid compatibility mode over standard SQLite .db files while many Native/ECS and extension features remain design or partial implementation.
key_quote: Compatibility runtime (Current)
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Dicklesworthstone
tools:
- cargo
- fsqlite-cli
- sqlite3
libraries:
- asupersync
companies:
- SQLite
tags:
- rust
- sqlite
- mvcc
- database-engine
- durability
---

### TL;DR
FrankenSQLite is a Rust, SQLite-compatible database engine repo that aims for page-level MVCC, SSI, and RaptorQ-based durability, but the current runnable path is still a hybrid compatibility mode over standard SQLite `.db` files while many Native/ECS and extension features remain design or partial implementation.

### Key Quote
"Compatibility runtime (Current)"

### Summary
- Repository: `Dicklesworthstone/frankensqlite`
- Project claim: an "independent ground-up Rust reimplementation of SQLite" with concurrent writers and information-theoretic durability.
- Current status is explicitly hybrid:
  - The **current user-facing runtime** is the **compatibility/pager-backed path** over standard SQLite files.
  - **Native mode / ECS / commit-stream design** is described, but the README says it should be treated as **design plus partial implementation unless explicitly called out as live behavior**.
- Core architectural goals:
  - **Page-level MVCC** instead of SQLite’s single-writer model.
  - **SSI by default** for serializable concurrent transactions.
  - **Safe Rust engine core**, with `unsafe` mainly confined to `fsqlite-vfs` and optional `fsqlite-c-api`.
  - **RaptorQ / fountain-code durability** for self-healing WALs, replication, and encoded storage.
  - **SQLite file-format compatibility** remains a major goal for the current runtime.

- Important concrete implementation/status notes:
  - The public entry point is `fsqlite::Connection`.
  - The CLI is `fsqlite-cli`, described as a **small interactive SQL shell**, not yet a full sqlite3-equivalent front-end.
  - `fsqlite-cli` supports `--verify-proof`.
  - The README repeatedly distinguishes between:
    - **Compatibility runtime**: standard SQLite `.db` + WAL/journal files, used today.
    - **Native mode**: ECS / commit capsules / commit markers / content-addressed storage, described as future-facing or partial.
  - The query planner crate exists and is substantial, but the README says `fsqlite_core::Connection` often compiles table-backed work directly through `fsqlite_vdbe::codegen` today.
  - Extensions exist as crates, but runtime wiring is still in progress.

- MVCC / transaction model:
  - Writers can commit in parallel if they touch different pages.
  - Conflicts are page-level first-committer-wins with SSI read tracking.
  - The README says deadlocks are impossible because page locking is eager and non-blocking.
  - Two especially important pragmas for later reference:
    - `PRAGMA fsqlite.serializable = OFF` — downgrades from SSI to plain snapshot isolation.
    - `PRAGMA fsqlite.write_merge = OFF | SAFE | LAB_UNSAFE` — controls merge policy; `SAFE` enables deterministic rebase replay and structured page patch merges.

- Transaction observability section:
  - `PRAGMA fsqlite_txn_stats`
  - `PRAGMA fsqlite_transactions`
  - `PRAGMA fsqlite_txn_advisor`
  - `PRAGMA fsqlite_txn_timeline_json`
  - Tunable thresholds:
    - `PRAGMA fsqlite.txn_advisor_long_txn_ms`
    - `PRAGMA fsqlite.txn_advisor_large_read_ops`
    - `PRAGMA fsqlite.txn_advisor_savepoint_depth`
    - `PRAGMA fsqlite.txn_advisor_rollback_ratio_percent`

- Storage / file-format details:
  - Standard SQLite database header and B-tree page layout are documented.
  - WAL format, rollback journal format, pointer map / auto-vacuum behavior, and lock-byte page handling are all described as compatibility targets.
  - The project claims support for standard SQLite interoperability in compatibility mode.

- CLI and API facts that are useful for finding the repo again:
  - `Connection::open()`
  - `execute()`, `query()`, `prepare()`
  - `fsqlite-cli`
  - `--verify-proof`
  - `cargo build`, `cargo test`, `cargo clippy --all-targets -- -D warnings`
  - Workspace size: **27-member Cargo workspace**

- The README also contains many ambitious design sections:
  - ECS / commit capsules / commit markers
  - page-level encryption with XChaCha20-Poly1305
  - multi-process MVCC via shared memory
  - time-travel queries with `FOR SYSTEM_TIME AS OF`
  - formal proof sketches, e-process monitoring, BOCPD, conformal calibration, Mazurkiewicz traces
  - all of these should be read carefully as **design, partial implementation, or roadmap content**, not uniformly as shipped behavior.

### Assessment
This is a mixed-content repository README with very high density and mixed originality: part project overview, part architecture manifesto, part specification, part roadmap, and part implementation status note. Durability is **medium** because the underlying database concepts are partly timeless, but many claims are tied to a specific codebase state, a specific SQLite compatibility target, and evolving implementation details. Content type is **mixed** rather than pure tutorial/reference/opinion; it reads mostly like a technical reference/specification with promotional framing. Originality is **primary source** for the project’s own design and status, though it also synthesizes a lot of database theory and cites external ideas. For **Recall**, it is excellent: the README is highly structured and memorable. For **Decide**, it is also good because it clearly flags the current hybrid runtime and partial areas, letting a reader judge whether to dig deeper. For **Evaluate**, it is usable but needs skepticism because many of the most ambitious features are aspirational or partial, and the prose is strongly promotional in places. For **Find**, it is very strong: the repo name, `Connection::open()`, `fsqlite-cli`, `--verify-proof`, `PRAGMA fsqlite.serializable = OFF`, `PRAGMA fsqlite.write_merge = SAFE`, and the **27-member Cargo workspace** are all strong confirmatory markers. Scrape quality is **good but not perfect**: the text captured a large amount of README content, including tables and code blocks, but the two referenced images/diagrams are only present as `<img>` tags with alt text, so the visual diagrams themselves were not captured.
