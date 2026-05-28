---
url: https://github.com/memgrafter/analysis/tree/main
title: 'memgrafter/analysis: Analysis'
scraped_at: '2026-04-19T07:02:36Z'
word_count: 679
raw_file: raw/2026-04-19_memgrafter-analysis-analysis_ab489b65.txt
tldr: A large, structured repository of 121,245 markdown analyses of arXiv ML papers from 2023–2025, with search tools, a SQLite index, curated topic clusters, and notes on how the reports are generated and what their limitations are.
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
- sqlite3
- search_topic.py
- index_frontmatter.py
- FlatAgents
libraries: []
companies:
- GitHub
- arXiv
tags:
- machine-learning
- research-corpus
- literature-analysis
- sqlite-index
- topic-search
---

### TL;DR
A large, structured repository of 121,245 markdown analyses of arXiv ML papers from 2023–2025, with search tools, a SQLite index, curated topic clusters, and notes on how the reports are generated and what their limitations are.

### Key Quote
“Each paper is distilled into a standardised markdown report so you can survey findings, compare mechanisms, and spot trends without reading thousands of PDFs.”

### Summary
- This GitHub repository is an **analysis corpus** for machine-learning research, not the original papers themselves.
- It contains **121,245 paper analyses** covering arXiv publications from **2023–2025**:
  - **2023:** 29,961 analyses / 29,961 unique papers
  - **2024:** 39,185 analyses / 38,027 unique papers
  - **2025:** 52,099 analyses / 51,517 unique papers
- Each analysis follows a **standard markdown template** with:
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
- The repo warns that **tags are noisy and unreliable** because every record shares a long generic tail; users are advised to search **`core_contribution`**, titles, and body text instead.

#### How to use the corpus
- **Search by topic** using `ripgrep` across year folders:
  - `rg -l "mixture of experts|MoE" ml_research_analysis_2025/`
  - `rg -n "speculative decoding" ml_research_analysis_202*/`
- **Use the provided search script**:
  - `python scripts/search_topic.py --topic "mixture of experts" --alias moe`
  - `python scripts/search_topic.py --topic "reinforcement learning" --alias rl --limit 25 --json`
- **Query the SQLite index**:
  - `analysis_outputs/research_index.sqlite` indexes the **2025 bucket** with columns:
    - `title`, `arxiv_id`, `core_contribution`, `tags`, `filename`, `file_size`
  - Example queries:
    - find papers mentioning “distillation”
    - look up a paper by arXiv ID such as `1706.03762`
- **Explore curated topic clusters** in `spot_analyses/` and the `spot_analysis_paper_groups` table. The eight named themes are:
  - `test_time_compute_scaling`
  - `reasoning_distillation`
  - `multi_agent_debate`
  - `process_reward_models`
  - `agentic_workflow_pipeline_design`
  - `adaptive_compute_allocation`
  - `test_time_adaptation`
  - `continual_online_tta`
- **Browse via the static website** in `website/`, with build/deploy instructions in `website/README.md`.

#### Repository layout
- `ml_research_analysis_2023/`, `ml_research_analysis_2024/`, `ml_research_analysis_2025/`: per-paper analyses
- `analysis_outputs/`: SQLite index, digests, assessment outputs
- `scripts/`: indexing and search utilities
- `spot_analyses/`: curated deep-dive clusters
- `website/`: static browse/search UI
- `docs/`: internal reference docs
- `archive/`: superseded v1 analyses

#### How analyses are generated
- The reports are produced by a **three-phase FlatAgents pipeline**:
  1. **Prep** — downloads arXiv PDFs, extracts text, and matches against an ML terminology corpus
  2. **Expensive** — parallel LLM calls generate mechanism analysis, reproduction notes, and open questions
  3. **Wrap** — adds limitations/confidence, tagging, assembles the report, and runs a quality judge plus auto-repair
- The 2025 batch used **GLM-5 (pony-alpha)** for the expensive phase.
- The 2023–2024 batches used **Trinity Large** throughout.
- The repository itself is described as **output only**; pipeline code and configs live in a separate repo.

#### Known limitations
- There are about **190 permanent failures** across all years:
  - PDF 404s (~106)
  - context overflow over 256k (~60)
  - provider errors (~9)
  - PDF parse errors (~15)
- **Duplicate filenames** exist because papers were rerun:
  - 1,158 in 2024
  - 582 in 2025
- The SQLite index and filenames are deduplicated by **`(arxiv_id, timestamp)`**.
- The corpus is useful for discovery, but users should be cautious because:
  - tags are noisy
  - some entries failed permanently
  - 2025 is the only year explicitly indexed in the SQLite database described here

### Assessment
This is a **mixed** reference/technical repository description with strong practical utility. Durability is **medium**: the corpus structure and search patterns are fairly stable, but details like model names, counts, and failure rates will age as the repository grows. Density is **high**, since it includes concrete dataset sizes, directory structure, commands, schema columns, and pipeline stages. Originality is mostly **primary source** in the sense that it describes the repository’s own contents and workflow rather than summarizing outside material. It is best used as **refer-back** material for navigating the corpus, searching topics, or understanding provenance and limitations. Scrape quality appears **good**: the key sections, tables, examples, commands, and limitations are present, with no obvious missing code blocks or major sections.
