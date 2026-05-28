---
url: https://github.com/memgrafter/analysis
title: 'memgrafter/analysis: Analysis'
scraped_at: '2026-04-19T07:47:28Z'
word_count: 679
raw_file: raw/2026-04-19_memgrafter-analysis-analysis_5b2b3196.txt
tldr: A large GitHub repository that publishes 121,245 standardized markdown analyses of arXiv machine-learning papers from 2023–2025, with search tools, a SQLite index, curated topic clusters, and notes on generation pipeline and limitations.
key_quote: “Each paper is distilled into a standardised markdown report so you can survey findings, compare mechanisms, and spot trends without reading thousands of PDFs.”
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
- FlatAgents
- GLM-5
- Trinity Large
libraries: []
companies:
- arXiv
tags:
- machine-learning
- research-corpus
- paper-analysis
- search-indexing
- llm-pipeline
---

### TL;DR
A large GitHub repository that publishes 121,245 standardized markdown analyses of arXiv machine-learning papers from 2023–2025, with search tools, a SQLite index, curated topic clusters, and notes on generation pipeline and limitations.

### Key Quote
“Each paper is distilled into a standardised markdown report so you can survey findings, compare mechanisms, and spot trends without reading thousands of PDFs.”

### Summary
- This repository is an **output corpus** of ML paper analyses, not the pipeline code itself.
- It contains **121,245 analyses** across arXiv papers from **2023–2025**:
  - **2023:** 29,961 analyses / 29,961 unique papers
  - **2024:** 39,185 analyses / 38,027 unique papers
  - **2025:** 52,099 analyses / 51,517 unique papers
- Each paper analysis follows a standard markdown structure:
  - `Quick Facts` — arXiv link, authors, headline numbers
  - `Executive Summary` — one-paragraph overview
  - `Method Summary` — experimental setup, models, data
  - `Key Results` — quantitative findings
  - `Mechanism Analysis` — why the approach works
  - `Reproduction Notes` — hyperparameters, compute, data details
  - `Limitations & Confidence`
- Example frontmatter includes:
  - `arxiv_id`
  - `core_contribution`
  - `tags`
- The repo warns that **tags are noisy and unreliable**, because every record includes a long generic tail. It recommends searching:
  - `core_contribution`
  - titles
  - body text
- Ways to use the corpus:
  - **ripgrep** over year folders for topic search, e.g.:
    - `rg -l "mixture of experts|MoE" ml_research_analysis_2025/`
    - `rg -n "speculative decoding" ml_research_analysis_202*/`
  - Use the search script:
    - `python scripts/search_topic.py --topic "mixture of experts" --alias moe`
    - `python scripts/search_topic.py --topic "reinforcement learning" --alias rl --limit 25 --json`
  - Query the SQLite index:
    - `analysis_outputs/research_index.sqlite`
    - indexes the **2025 bucket** with columns: `title`, `arxiv_id`, `core_contribution`, `tags`, `filename`, `file_size`
- It highlights **curated topic clusters** in `spot_analyses/` and the `spot_analysis_paper_groups` table, spanning eight themes:
  - `test_time_compute_scaling`
  - `reasoning_distillation`
  - `multi_agent_debate`
  - `process_reward_models`
  - `agentic_workflow_pipeline_design`
  - `adaptive_compute_allocation`
  - `test_time_adaptation`
  - `continual_online_tta`
- The `website/` directory provides a **static browse/search UI** with build/deploy instructions in `website/README.md`.
- Repository layout includes:
  - year folders: `ml_research_analysis_2023/`, `ml_research_analysis_2024/`, `ml_research_analysis_2025/`
  - `analysis_outputs/` for SQLite index, digests, assessment outputs
  - `scripts/` for indexing and topic search
  - `spot_analyses/` for deep dives
  - `archive/` for superseded v1 analyses
  - `docs/` for internal references
- Generation pipeline:
  - Uses a three-phase **FlatAgents pipeline**:
    1. **Prep** — download arXiv PDF, extract text, match ML terminology corpus
    2. **Expensive** — parallel LLM calls for mechanism analysis, reproduction notes, open questions
    3. **Wrap** — limitations/confidence, tagging, assembly, quality judge + auto-repair
  - The **2025 batch used GLM-5 (pony-alpha)** in the expensive phase
  - **2023–2024 used Trinity Large**
  - The repo explicitly says the pipeline code/configs/databases live in another repo; this repo is **output only**
- Known limitations:
  - About **190 permanent failures** total, including:
    - PDF 404s (~106)
    - context overflow >256k (~60)
    - provider errors (~9)
    - PDF parse errors (~15)
  - **No pending retries**
  - **Duplicate filenames** exist due to reruns:
    - 1,158 in 2024
    - 582 in 2025
  - SQLite and filenames are deduplicated by `(arxiv_id, timestamp)`
- Reindexing instructions are provided:
  - `python scripts/index_frontmatter.py ml_research_analysis_2025`
  - `python scripts/index_frontmatter.py ml_research_analysis_2025 --prune`

### Assessment
This is a **high-durability** reference/repository description: the general idea of a large structured ML paper-analysis corpus will remain useful, though the exact counts, model names, and failure statistics are tied to the current snapshot and may age. The content type is **mixed**, combining reference docs, project overview, usage instructions, and operational notes. Density is **high**, because it packs concrete counts, commands, folder names, schema details, and pipeline specifics into a relatively compact page. It is primarily a **primary source** description of the repository itself rather than commentary. It is best suited for **refer-back** use if you need to search, index, or understand the corpus structure. Scrape quality appears **good** overall: the main README content, tables, commands, and code blocks are present, with no obvious missing major sections.
