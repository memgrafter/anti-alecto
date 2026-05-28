---
url: https://x.com/KatanaLarp/status/2029928471632224486
title: 'Hōrōshi バガボンド on X: "Your LLM Doesn''t Write Correct Code. It Writes Plausible Code." / X'
scraped_at: '2026-04-19T07:14:17Z'
word_count: 4155
raw_file: raw/2026-04-19_h-r-shi-on-x-your-llm-doesn-t-write-correct-code-it-writes-plausible-code-x_f4377b59.txt
tldr: This X thread argues that LLM-generated code can look correct while hiding catastrophic performance bugs, using a Rust SQLite reimplementation as a case study that is tens of thousands of times slower than SQLite on basic lookups.
key_quote: LLMs optimize for plausibility over correctness.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: deep-study
scrape_quality: partial
people:
- Richard Hipp
- Tony Hoare
- Steven Skiena
- Andrej Karpathy
- Simon Willison
tools:
- SQLite
- Rust
- fsync
- fdatasync
libraries: []
companies:
- Anthropic
- OpenAI
- Google
- GitClear
- METR
tags:
- llm-code-generation
- software-performance
- database-engineering
- correctness
- ai-sycophancy
---

### TL;DR
This X thread argues that LLM-generated code can look correct while hiding catastrophic performance bugs, using a Rust SQLite reimplementation as a case study that is tens of thousands of times slower than SQLite on basic lookups.

### Key Quote
"LLMs optimize for plausibility over correctness."

### Summary
- The post compares **system SQLite** with a **ground-up Rust reimplementation** generated with heavy LLM assistance.
- Benchmark setup:
  - Same benchmark program compiled against both libraries.
  - Same compiler flags, WAL mode, schema, and queries.
  - Test case: **primary-key lookup on 100 rows**.
- Reported timing:
  - **SQLite:** 0.09 ms
  - **Rust rewrite:** 1,815.43 ms
  - Claimed slowdown: **20,171x** on `SELECT BY ID`
- Main diagnosis:
  - The Rust project compiles, passes tests, reads/writes SQLite files, and has a plausible README.
  - But its query planner fails to treat `id INTEGER PRIMARY KEY` as a rowid alias for fast lookup.
  - As a result, `WHERE id = N` becomes a **full table scan** instead of a B-tree seek.
  - Only `WHERE rowid = ?` hits the fast path.
- Specific bug described:
  - `is_rowid_ref()` only recognizes `"rowid"`, `"_rowid_"`, and `"oid"`.
  - It ignores named integer primary key columns even when `is_ipk: true`.
  - The code therefore routes many queries through `codegen_select_full_scan()`.
- Second major bug:
  - Every bare `INSERT` outside a transaction triggers a full autocommit cycle and an `fsync`.
  - On 100 inserts, this means **100 syncs**.
  - SQLite uses `fdatasync` on Linux when available and has lower per-statement overhead.
- Additional performance anti-patterns called out:
  - AST cloned and recompiled on every call instead of reusing a prepared statement.
  - Page cache returns copied `Vec<u8>` instead of zero-copy references.
  - Schema is reloaded after every autocommit cycle.
  - Eager formatting and unnecessary allocations on each statement.
- Broader argument:
  - Many of these choices are individually defensible as “safe” Rust design choices, but together they destroy performance.
  - The author argues that **safety defaults are not enough for hot paths** like databases.
- Second case study:
  - A separate project by the same author is a disk-cleanup daemon with **82,000 lines of Rust** and **192 dependencies**.
  - The post contrasts this with a trivial one-line `find` + `rm` cron job.
  - The point: LLMs can generate sophisticated-looking systems for problems that already have simple solutions.
- Core thesis:
  - LLMs tend to produce **plausible-looking outputs** that satisfy the prompt but miss the actual requirements.
  - The failure mode is not syntax errors; it is **semantic correctness and performance invariants**.
  - The user must define acceptance criteria before generation, or they may get code that compiles but is operationally wrong.
- Supporting references and claims:
  - Mentions external research on sycophancy, LLM evaluation bias, and coding-performance gaps.
  - Cites studies suggesting AI-assisted developers can be slower in some settings and that subjective impressions of speed gains may be misleading.
  - Uses SQLite’s known design properties—prepared statement reuse, zero-copy page cache, schema cookies, and `INTEGER PRIMARY KEY` rowid behavior—as examples of the hard-won details the rewrite misses.
- Tone and stance:
  - The author frames this as a practitioner’s critique, not an anti-LLM rant.
  - The argument is explicitly **pro-LLM when used with strong verification**, but strongly against trusting generated code without understanding or benchmarking it.

### Assessment
Durability is **medium**: the general lesson about plausibility versus correctness is durable, but the specifics are tied to the particular Rust SQLite reimplementation, benchmarks, and 2024–2026 research citations. Content type is **mixed**—part technical analysis, part opinion essay, part research roundup. Density is **high**: it is packed with benchmark numbers, code-path explanations, bug descriptions, and literature references. Originality is best classified as **commentary informed by primary source analysis**: the author appears to have inspected the project code and benchmarked it, then layered in external research and broader argumentation. Reference style is **refer-back** if you care about the exact benchmark/bug analysis, or **deep-study** if you want the supporting research and methodological details. Scrape quality is **partial**: the text is extensive and includes many claims and quoted fragments, but several links, images, and inline references are missing or collapsed, so some evidence and formatting from the original thread/article likely did not carry over cleanly.
