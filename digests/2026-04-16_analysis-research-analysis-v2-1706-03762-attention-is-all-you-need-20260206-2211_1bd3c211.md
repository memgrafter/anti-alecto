---
url: https://github.com/memgrafter/analysis/blob/main/research_analysis_v2/1706.03762_attention-is-all-you-need_20260206_221149.md
title: analysis/research_analysis_v2/1706.03762_attention-is-all-you-need_20260206_221149.md at main · memgrafter/analysis
scraped_at: '2026-04-16T03:57:22Z'
word_count: 679
raw_file: raw/2026-04-16_analysis-research-analysis-v2-1706-03762-attention-is-all-you-need-20260206-2211_1bd3c211.txt
tldr: This repository is an output-only corpus of 121,245 standardized machine-learning paper analyses from arXiv 2023–2025, with search tools, a SQLite index, curated topic clusters, and notes on pipeline generation and known limitations.
key_quote: Each paper is distilled into a standardised markdown report so you can survey findings, compare mechanisms, and spot trends without reading thousands of PDFs.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- ripgrep
- sqlite3
- Python
- GLM-5
- pony-alpha
- Trinity Large
libraries: []
companies:
- arXiv
- FlatAgents
- memgrafter
tags:
- machine-learning
- research-corpus
- information-retrieval
- sqlite-index
- data-pipeline
---

### TL;DR
This repository is an output-only corpus of 121,245 standardized machine-learning paper analyses from arXiv 2023–2025, with search tools, a SQLite index, curated topic clusters, and notes on pipeline generation and known limitations.

### Key Quote
"Each paper is distilled into a standardised markdown report so you can survey findings, compare mechanisms, and spot trends without reading thousands of PDFs."

### Summary
- **What this is**
  - A large structured library of ML research analyses, not the original papers themselves.
  - Covers arXiv publications from **2023–2025**.
  - Total size: **121,245 analyses**.
  - Breakdown:
    - **2023:** 29,961 analyses / 29,961 unique papers
    - **2024:** 39,185 analyses / 38,027 unique papers
    - **2025:** 52,099 analyses / 51,517 unique papers

- **What each analysis contains**
  - All files follow a standardized markdown template with:
    - `frontmatter` including `arxiv_id`, `core_contribution`, and `tags`
    - `Quick Facts`
    - `Executive Summary`
    - `Method Summary`
    - `Key Results`
    - `Mechanism Analysis`
    - `Reproduction Notes`
    - `Limitations & Confidence`
  - The example emphasizes that `core_contribution` is more reliable than tags.

- **Search and browsing workflows**
  - Topic search with ripgrep:
    - `rg -l "mixture of experts|MoE" ml_research_analysis_2025/`
    - `rg -n "speculative decoding" ml_research_analysis_202*/`
  - Structured search script:
    - `python scripts/search_topic.py --topic "mixture of experts" --alias moe`
    - `python scripts/search_topic.py --topic "reinforcement learning" --alias rl --limit 25 --json`
  - SQLite lookup:
    - Database: `analysis_outputs/research_index.sqlite`
    - Indexes the **2025 bucket** with columns:
      - `title`, `arxiv_id`, `core_contribution`, `tags`, `filename`, `file_size`
    - Example queries show how to search by `core_contribution` or find the filename for a given arXiv ID.

- **Curated topic clusters**
  - The `spot_analyses/` directory and `spot_analysis_paper_groups` table contain **8 deep-dive themes** across **1,824 papers**:
    - `test_time_compute_scaling`
    - `reasoning_distillation`
    - `multi_agent_debate`
    - `process_reward_models`
    - `agentic_workflow_pipeline_design`
    - `adaptive_compute_allocation`
    - `test_time_adaptation`
    - `continual_online_tta`

- **Repository layout**
  - `ml_research_analysis_2023/`, `ml_research_analysis_2024/`, `ml_research_analysis_2025/` — per-paper markdown analyses
  - `analysis_outputs/` — SQLite index, digests, assessment outputs
  - `scripts/` — indexing and topic search scripts
  - `spot_analyses/` — curated topic deep-dives
  - `website/` — static browse/search UI
  - `docs/` — internal references
  - `archive/` — superseded v1 analyses

- **How the analyses are generated**
  - Produced by a three-phase **FlatAgents pipeline**:
    1. **Prep** — download arXiv PDF, extract text, match ML terminology
    2. **Expensive** — parallel LLM calls for mechanism analysis, reproduction notes, open questions
    3. **Wrap** — limitations/confidence, tagging, report assembly, quality judge + auto-repair
  - Model usage:
    - **2025:** GLM-5 (pony-alpha) for the expensive phase
    - **2023–2024:** Trinity Large throughout
  - This repository contains **output only**; pipeline code lives in a separate repo.

- **Known limitations**
  - About **190 permanent failures** across all years, including:
    - PDF 404s (~106)
    - context overflow >256k (~60)
    - provider errors (~9)
    - PDF parse errors (~15)
  - **Tags are unreliable** because they include noisy generic tails.
  - There are **duplicate filenames** from reruns:
    - 1,158 in 2024
    - 582 in 2025
  - The SQLite index and filenames are deduplicated by `(arxiv_id, timestamp)`.

- **Reindexing**
  - To rebuild the SQLite index after file changes:
    - `python scripts/index_frontmatter.py ml_research_analysis_2025`
    - `python scripts/index_frontmatter.py ml_research_analysis_2025 --prune`

### Assessment
This is a high-durability reference artifact because its main value is as a structured corpus and search index rather than time-sensitive commentary, though specific counts, model choices, and failure modes will age as the corpus grows. The content type is a mix of reference and tutorial, with dense operational detail about how to browse, query, and reindex the archive. It appears to be primary source documentation for the repository itself, not a synthesis of outside work. This is best used as a refer-back resource when searching or navigating the corpus, rather than as a deep-study read. Scrape quality is good overall: the key sections, code blocks, repository layout, and limitations are present, though this is clearly a repository README-style document rather than the full underlying dataset or analyses.
