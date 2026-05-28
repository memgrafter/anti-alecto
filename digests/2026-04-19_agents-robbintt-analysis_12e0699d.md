---
url: https://github.com/robbintt/analysis/tasks/606191a4-9722-453f-b57e-f76496009fb0
title: Agents · robbintt/analysis
scraped_at: '2026-04-19T07:47:16Z'
word_count: 679
raw_file: raw/2026-04-19_agents-robbintt-analysis_12e0699d.txt
tldr: This repository is a large, output-only corpus of 121,245 standardized machine-learning paper analyses from arXiv (2023–2025), with search tools, a SQLite index, curated topic deep-dives, and notes on how the analyses were generated.
key_quote: Each paper is distilled into a standardised markdown report so you can survey findings, compare mechanisms, and spot trends without reading thousands of PDFs.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- ripgrep
- SQLite
- FlatAgents
- GLM-5
- Trinity Large
libraries: []
companies:
- arXiv
tags:
- machine-learning
- research-corpus
- literature-search
- text-mining
- knowledge-base
---

### TL;DR
This repository is a large, output-only corpus of 121,245 standardized machine-learning paper analyses from arXiv (2023–2025), with search tools, a SQLite index, curated topic deep-dives, and notes on how the analyses were generated.

### Key Quote
“Each paper is distilled into a standardised markdown report so you can survey findings, compare mechanisms, and spot trends without reading thousands of PDFs.”

### Summary
- **What it is**
  - A structured library of **121,245** ML paper analyses covering arXiv publications from **2023–2025**.
  - The corpus is meant to let readers survey findings and compare mechanisms without opening the original PDFs.

- **Corpus size by year**
  - **2023:** 29,961 analyses / 29,961 unique papers
  - **2024:** 39,185 analyses / 38,027 unique papers
  - **2025:** 52,099 analyses / 51,517 unique papers

- **What each analysis contains**
  - Each file uses a consistent markdown template with YAML frontmatter and sections like:
    - `Quick Facts`
    - `Executive Summary`
    - `Method Summary`
    - `Key Results`
    - `Mechanism Analysis`
    - `Reproduction Notes`
    - `Limitations & Confidence`
  - Example frontmatter includes:
    - `arxiv_id`
    - `core_contribution`
    - `tags`
  - The repository warns that **tags are noisy** and the more reliable fields are `core_contribution`, titles, and body text.

- **How to search/use it**
  - **ripgrep** over year folders for topic search, e.g.:
    - `rg -l "mixture of experts|MoE" ml_research_analysis_2025/`
    - `rg -n "speculative decoding" ml_research_analysis_202*/`
  - A script provides structured topic search:
    - `python scripts/search_topic.py --topic "mixture of experts" --alias moe`
    - `python scripts/search_topic.py --topic "reinforcement learning" --alias rl --limit 25 --json`
  - A **SQLite index** exists at `analysis_outputs/research_index.sqlite` for the **2025** bucket, with columns:
    - `title`, `arxiv_id`, `core_contribution`, `tags`, `filename`, `file_size`
  - Example SQL queries are provided for finding papers by keyword or arXiv ID.

- **Curated topic clusters**
  - The `spot_analyses/` directory and `spot_analysis_paper_groups` table contain deep-dive clusters across **8 themes**:
    - `test_time_compute_scaling`
    - `reasoning_distillation`
    - `multi_agent_debate`
    - `process_reward_models`
    - `agentic_workflow_pipeline_design`
    - `adaptive_compute_allocation`
    - `test_time_adaptation`
    - `continual_online_tta`
  - Total deep-dive cluster size is noted as **1,824 papers**.

- **Website**
  - The `website/` directory contains a static site with full-text search.
  - Build/deploy instructions are in `website/README.md`.

- **Repository layout**
  - `ml_research_analysis_2023/`, `2024/`, `2025/`: per-paper analyses
  - `analysis_outputs/`: SQLite index, digests, assessment outputs
  - `scripts/`: indexing and topic search scripts
  - `spot_analyses/`: curated topic deep-dives
  - `website/`: browse/search UI
  - `docs/`: internal reference docs
  - `archive/`: superseded v1 analyses

- **How the analyses are generated**
  - The repository states the analyses come from a **three-phase FlatAgents pipeline**:
    1. **Prep** — download arXiv PDF, extract text, match terminology corpus
    2. **Expensive** — parallel LLM calls for mechanism analysis, reproduction notes, open questions
    3. **Wrap** — limitations/confidence, tagging, assembly, quality judge + auto-repair
  - 2025 used **GLM-5 (pony-alpha)** in the expensive phase.
  - 2023–2024 used **Trinity Large** throughout.
  - The repo emphasizes that the **pipeline code is not here**; this repository is output only.

- **Known limitations**
  - About **190 permanent failures** across all years, including:
    - PDF 404s (~106)
    - context overflow >256k (~60)
    - provider errors (~9)
    - PDF parse errors (~15)
  - There are **duplicate filenames** due to reruns:
    - 1,158 in 2024
    - 582 in 2025
  - The SQLite index and filenames are deduplicated by **`(arxiv_id, timestamp)`**.
  - No pending retries remain.

- **Reindexing**
  - If files are added or removed, the SQLite index can be rebuilt with:
    - `python scripts/index_frontmatter.py ml_research_analysis_2025`
    - `python scripts/index_frontmatter.py ml_research_analysis_2025 --prune`

### Assessment
This is a **reference/mixed** repository with high practical value for ML literature exploration rather than a narrative article. Its durability is **medium-high**: the corpus itself may remain useful for historical analysis, but some implementation details, model names, and pipeline specifics can become stale as the collection grows or tooling changes. The density is **high**, since it compresses a lot of operational detail—scale, structure, search methods, generation pipeline, limitations, and maintenance instructions—into a compact README-style overview. The content is mostly a **primary-source repository description** with some system-generated documentation flavor, not commentary or synthesis. It’s best used **refer-back** rather than skim-once, especially for the search/index commands and corpus structure. Scrape quality appears **good**: the main sections, examples, commands, limitations, and repository layout are all present, with no obvious missing code blocks or critical sections.
