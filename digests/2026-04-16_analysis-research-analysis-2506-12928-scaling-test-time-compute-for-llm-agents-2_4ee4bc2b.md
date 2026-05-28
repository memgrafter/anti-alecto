---
url: https://github.com/memgrafter/analysis/blob/main/research_analysis/2506.12928_scaling-test-time-compute-for-llm-agents_20260126_191018.md?plain=1
title: analysis/research_analysis/2506.12928_scaling-test-time-compute-for-llm-agents_20260126_191018.md at main · memgrafter/analysis
scraped_at: '2026-04-16T03:56:56Z'
word_count: 679
raw_file: raw/2026-04-16_analysis-research-analysis-2506-12928-scaling-test-time-compute-for-llm-agents-2_4ee4bc2b.txt
tldr: A structured library of 121,245 machine-learning paper analyses covering arXiv publications from 2023–2025, with instructions for searching, browsing, indexing, and understanding the pipeline that generated them.
key_quote: Auto-generated `tags` are noisy (every record shares a long generic tail). Prefer searching `core_contribution`, titles, and body text.
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- ripgrep
- SQLite
- scripts/search_topic.py
- scripts/index_frontmatter.py
- FlatAgents
- GLM-5
- pony-alpha
- Trinity Large
libraries: []
companies:
- memgrafter
tags:
- machine-learning
- research-corpus
- paper-analysis
- search-indexing
- llm-pipeline
---

### TL;DR
This repository page describes a large corpus of 121,245 standardized ML paper analyses from 2023–2025, with instructions for searching, browsing, indexing, and understanding the pipeline that generated them.

### Key Quote
"Auto-generated `tags` are noisy (every record shares a long generic tail). Prefer searching `core_contribution`, titles, and body text."

### Summary
- The repository is a **structured library of machine-learning paper analyses** covering arXiv publications from **2023, 2024, and 2025**.
- It contains **121,245 analyses total**, broken down as:
  - **2023:** 29,961 analyses / 29,961 unique papers
  - **2024:** 39,185 analyses / 38,027 unique papers
  - **2025:** 52,099 analyses / 51,517 unique papers
- Each analysis follows a **standard markdown template** with:
  - YAML frontmatter including `arxiv_id`, `core_contribution`, and `tags`
  - Sections such as:
    - Quick Facts
    - Executive Summary
    - Method Summary
    - Key Results
    - Mechanism Analysis
    - Reproduction Notes
    - Limitations & Confidence
- The page warns that **tags are noisy and unreliable**, because every record shares a long generic tail; it recommends searching via:
  - `core_contribution`
  - titles
  - body text
- It provides multiple ways to use the corpus:
  - **ripgrep** for topic browsing across year folders
  - `scripts/search_topic.py` for structured topic search with aliases and JSON output
  - **SQLite queries** against `analysis_outputs/research_index.sqlite`
- The SQLite index currently covers the **2025 bucket** and includes columns:
  - `title`
  - `arxiv_id`
  - `core_contribution`
  - `tags`
  - `filename`
  - `file_size`
- The repository also includes **curated topic clusters** in `spot_analyses/` and the `spot_analysis_paper_groups` table, covering eight themes:
  - test time compute scaling
  - reasoning distillation
  - multi-agent debate
  - process reward models
  - agentic workflow pipeline design
  - adaptive compute allocation
  - test time adaptation
  - continual / online TTA
- There is also a **static website** in `website/` with full-text search and build/deploy instructions in `website/README.md`.
- The repository layout includes:
  - year-specific analysis directories for 2023/2024/2025
  - analysis outputs and SQLite index
  - scripts
  - spot analyses
  - website
  - docs
  - archive for superseded analyses
- The analyses are produced by a **three-phase FlatAgents pipeline**:
  1. **Prep** — download arXiv PDF, extract text, match ML terminology
  2. **Expensive** — parallel LLM calls for mechanism analysis, reproduction notes, open questions
  3. **Wrap** — limitations/confidence, tagging, assembly, quality judge and auto-repair
- The 2025 batch used **GLM-5 (pony-alpha)** for the expensive phase; **2023–2024 used Trinity Large**.
- The page notes several limitations:
  - About **190 permanent failures** across all years
  - Causes include PDF 404s, context overflow over 256k tokens, provider errors, and PDF parse errors
  - **No pending retries**
  - **Duplicate filenames** exist due to reruns, but the SQLite index deduplicates by `(arxiv_id, timestamp)`
- Reindexing instructions are provided for updating the SQLite index after file changes:
  - `python scripts/index_frontmatter.py ml_research_analysis_2025`
  - `python scripts/index_frontmatter.py ml_research_analysis_2025 --prune`

### Assessment
This is a **reference** page with high durability for understanding the structure, search methods, and limitations of the corpus, though some operational details like model choices, counts, and tooling may become stale as the repository evolves. The content is **mixed**: mostly reference/documentation, with some announcement-like corpus statistics and pipeline notes. Density is **high**, since it packs a large amount of specific information, commands, file paths, and dataset metadata into a small space. It is primarily a **primary source** for the repository’s own structure and usage, not a synthesis of outside material. It is best used as **refer-back** material for navigating the corpus or confirming how the analyses are organized. Scrape quality appears **good**: the main sections, tables, code blocks, and warnings are present, though this is a plain markdown extract rather than the full rendered repository context.
