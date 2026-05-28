---
url: https://github.com/memgrafter/analysis/blob/main/analysis_outputs/research_index.sqlite
title: analysis/analysis_outputs/research_index.sqlite at main · memgrafter/analysis
scraped_at: '2026-04-17T05:23:59Z'
word_count: 679
raw_file: raw/2026-04-17_analysis-analysis-outputs-research-index-sqlite-at-main-memgrafter-analysis_06ac894b.txt
tldr: A structured library of 121,245 machine-learning paper analyses covering arXiv publications from 2023–2025, with a SQLite index and search tools for browsing standardized summaries by topic, paper, or year.
key_quote: Each paper is distilled into a standardised markdown report so you can survey findings, compare mechanisms, and spot trends without reading thousands of PDFs.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people: []
tools:
- ripgrep
- sqlite3
- FlatAgents
- GLM-5
- Trinity Large
libraries: []
companies:
- arXiv
tags:
- machine-learning
- research-corpus
- sqlite-index
- paper-analysis
- search-tools
---

### TL;DR
This repository is an output corpus for **121,245 ML paper analyses from arXiv (2023–2025)**, with a SQLite index and search tools for browsing standardized summaries by topic, paper, or year.

### Key Quote
“Each paper is distilled into a standardised markdown report so you can survey findings, compare mechanisms, and spot trends without reading thousands of PDFs.”

### Summary
- **What this is**
  - A structured library of machine-learning paper analyses, not the original papers themselves.
  - Covers arXiv publications from **2023, 2024, and 2025**.
  - Total scale: **121,245 analyses**.
    - 2023: **29,961**
    - 2024: **39,185** analyses for **38,027 unique papers**
    - 2025: **52,099** analyses for **51,517 unique papers**

- **What each analysis contains**
  - Standardized markdown reports with sections like:
    - **Quick Facts**: arXiv link, authors, headline numbers
    - **Executive Summary**: one-paragraph overview
    - **Method Summary**: setup, models, data
    - **Key Results**: quantitative findings
    - **Mechanism Analysis**: why the method works
    - **Reproduction Notes**: hyperparameters, compute, data details
    - **Limitations & Confidence**
  - Frontmatter includes fields like:
    - `arxiv_id`
    - `core_contribution`
    - `tags`
  - Example focus: a paper on **procedural memory retrieval in language agents**.

- **How to search and browse**
  - Use `ripgrep` to search within year folders:
    - Example: `rg -l "mixture of experts|MoE" ml_research_analysis_2025/`
    - Full-text across years: `rg -n "speculative decoding" ml_research_analysis_202*/`
  - Use a script for structured search:
    - `python scripts/search_topic.py --topic "mixture of experts" --alias moe`
    - `python scripts/search_topic.py --topic "reinforcement learning" --alias rl --limit 25 --json`
  - Query the SQLite index directly:
    - The database is `analysis_outputs/research_index.sqlite`
    - It indexes the **2025 bucket** with columns:
      - `title`
      - `arxiv_id`
      - `core_contribution`
      - `tags`
      - `filename`
      - `file_size`
    - Example queries:
      - Find papers mentioning distillation in `core_contribution`
      - Look up filename by `arxiv_id`

- **Curated topic clusters**
  - The repo includes `spot_analyses/` and a `spot_analysis_paper_groups` table for **8 themed deep-dive clusters**:
    - `test_time_compute_scaling`
    - `reasoning_distillation`
    - `multi_agent_debate`
    - `process_reward_models`
    - `agentic_workflow_pipeline_design`
    - `adaptive_compute_allocation`
    - `test_time_adaptation`
    - `continual_online_tta`
  - These group papers into research themes like inference-time scaling, distillation, agent architectures, and test-time adaptation.

- **Website**
  - A static site in `website/` provides full-text search and browsing.
  - Build/deploy instructions are in `website/README.md`.

- **Repository layout**
  - `ml_research_analysis_2023/`, `ml_research_analysis_2024/`, `ml_research_analysis_2025/`: per-paper markdown analyses
  - `analysis_outputs/`: SQLite index, digests, assessment outputs
  - `scripts/`: indexing and search scripts
  - `spot_analyses/`: curated deep-dives
  - `website/`: static UI
  - `docs/`: internal reference docs
  - `archive/`: older superseded analyses

- **How the analyses are generated**
  - A three-phase **FlatAgents** pipeline creates the reports:
    1. **Prep** — download arXiv PDF, extract text, match ML terminology corpus
    2. **Expensive** — parallel LLM calls for mechanism analysis, reproduction notes, open questions
    3. **Wrap** — limitations, tagging, report assembly, quality judge, auto-repair
  - Models used:
    - **2025** batch: **GLM-5 (pony-alpha)**
    - **2023–2024**: **Trinity Large**
  - This repo is **output only**; pipeline code and configs live elsewhere.

- **Known limitations**
  - About **190 permanent failures** across all years, including:
    - PDF 404s (~106)
    - context overflow >256k (~60)
    - provider errors (~9)
    - PDF parse errors (~15)
  - **Tags are unreliable** because they contain noisy generic tails.
  - **Duplicate filenames** exist from reruns:
    - 1,158 in 2024
    - 582 in 2025
  - The SQLite index and filenames are deduplicated by `(arxiv_id, timestamp)`.

- **Reindexing**
  - If files change, rebuild the index with:
    - `python scripts/index_frontmatter.py ml_research_analysis_2025`
    - `python scripts/index_frontmatter.py ml_research_analysis_2025 --prune`
  - The `--prune` flag removes deleted files from the index too.

### Assessment
This is a **reference** and **tooling-oriented** repository summary with high practical value for locating and comparing ML paper analyses. **Durability is medium** because the corpus content is tied to arXiv papers from 2023–2025 and to specific pipeline/model choices (for example GLM-5 and Trinity Large), but the repository structure and search patterns are likely to remain useful. **Content type is mixed**: it combines reference documentation, tutorial-style usage instructions, and operational notes. **Density is high** because it includes concrete counts, file paths, commands, schema details, and pipeline stages. **Originality is primarily primary source** for the repository’s own structure and process, though the content is an output corpus rather than research authorship itself. **Reference style is deep-study / refer-back**, since users will likely return to it for search, indexing, and corpus navigation details. **Scrape quality is good**: the main README-like content appears intact, including tables, code blocks, and the key limitation notes.
