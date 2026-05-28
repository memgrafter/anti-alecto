---
url: https://github.com/memgrafter/research-crawler-flatagents/tree/main/discovery_pipeline
title: 'memgrafter/research-crawler-flatagents: Research crawling, scoring, and analysis. Uses flatagents + flatmachines for llm orchestration.'
scraped_at: '2026-04-16T03:57:45Z'
word_count: 386
raw_file: raw/2026-04-16_memgrafter-research-crawler-flatagents-research-crawling-scoring-and-analysis-us_16768897.txt
tldr: discovery_pipeline is a CLI-driven workflow for automatically discovering, scoring, enriching, and summarizing new AI/ML papers from arXiv, with OpenAlex and Cerebras API integration and cron-friendly backfill behavior.
key_quote: Unified pipeline that discovers, scores, enriches, and summarizes new AI/ML papers.
durability: medium
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- arxiv
- openalex
- cerebras
libraries: []
companies:
- OpenAlex
- Cerebras
tags:
- arxiv
- paper-discovery
- llm-workflows
- data-pipelines
- research-automation
---

### TL;DR
`discovery_pipeline` is a CLI-driven workflow for automatically discovering, scoring, enriching, and summarizing new AI/ML papers from arXiv, with OpenAlex and Cerebras API integration and cron-friendly backfill behavior.

### Key Quote
“Unified pipeline that discovers, scores, enriches, and summarizes new AI/ML papers.”

### Summary
- This is the `Discovery Pipeline` section of the `memgrafter/research-crawler-flatagents` repo, describing a unified pipeline for AI/ML paper discovery.
- The pipeline has four phases:
  1. **Crawl** — fetch new papers from the arXiv API
  2. **Score** — compute FMR relevance scores using sentence embeddings
  3. **Enrich** — add author and citation data from OpenAlex
  4. **Report** — generate an LLM-powered summary of the top papers
- **Quick start**
  - Set required environment variables:
    - `OPENALEX_MAILTO='your-email@example.com'`
    - `OPENALEX_API_KEY='your-openalex-key'`
    - `CEREBRAS_API_KEY='your-cerebras-key'`
  - Run:
    - `cd discovery_pipeline`
    - `./run.sh`
- **Install behavior**
  - `run.sh` skips dependency installation if required packages already exist in `.venv`
  - Use `--upgrade` or `-u` to force reinstall/upgrade dependencies
- **Date handling / backfill**
  - Default behavior is automatic backfill based on the last successful crawler run
  - If there are no prior runs, it defaults to the **last 7 days**
  - Recommended for scheduled cron execution
  - Custom ranges are supported via `--since YYYY-MM-DD`
- **Selective execution**
  - Can skip crawl, score, and/or enrich phases
  - Example: `./run.sh --skip-crawl --skip-score --skip-enrich` generates only a report from existing data
  - Example: `./run.sh --skip-enrich` skips OpenAlex enrichment only
- **Other CLI options**
  - `--db-path` defaults to `../arxiv_crawler/data/arxiv.sqlite`
  - `--report-path` defaults to `./reports`
  - `--limit` defaults to `10000`
  - `--dry-run` runs without making changes
- **Outputs**
  - Reports are written to `./reports/discovery_report_YYYY-MM-DD_HHMM.md`
  - Reports include:
    - executive summary of themes and trends
    - top 10 papers with implementation notes
    - arXiv links, publication dates, and categories
- **Scheduling**
  - Suggested weekly cron entry:
    - `0 6 * * 1 cd /path/to/discovery_pipeline && ./run.sh >> /tmp/discovery.log 2>&1`
- **Environment requirements**
  - OpenAlex needs both `OPENALEX_MAILTO` and `OPENALEX_API_KEY`
  - Report generation needs `CEREBRAS_API_KEY`

### Assessment
This is a **reference/tutorial** with **high durability** for the general pipeline design and usage, but **medium durability** overall because it depends on specific tools, APIs, and repository defaults that may change over time. The content is **mixed**: mostly procedural documentation with some reference-style configuration details. It is fairly **dense** and specific, giving concrete commands, environment variables, defaults, and cron usage. The work appears to be **primary source** documentation from the repository itself rather than commentary or synthesis. It is best used as a **refer-back** guide for running the pipeline, checking flags, and confirming operational details. Scrape quality looks **good**: the main README-style content, command examples, options table, and scheduling snippet are present, with no obvious missing code blocks or major sections.
