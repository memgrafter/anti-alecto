---
url: https://github.com/memgrafter/skills-flatagents/blob/main/website_scraper/website_analysis/2026/2026-02-01_github-marcosommaorka-reasoning-orchestrator-kit-for-agentic.md
title: skills-flatagents/website_scraper/website_analysis/2026/2026-02-01_github-marcosommaorka-reasoning-orchestrator-kit-for-agentic.md at main · memgrafter/skills-flatagents
scraped_at: '2026-04-16T03:55:33Z'
word_count: 292
raw_file: raw/2026-04-16_skills-flatagents-website-scraper-website-analysis-2026-2026-02-01-github-marcos_f8f54aa2.txt
tldr: This is a concise README for a FlatAgents-based skills repo, explaining three agent skills, how to install and configure them, and how to run them with provider-specific API keys.
key_quote: 'LLM/machine readers: use MACHINES.md as a primary reference, it is more comprehensive and token efficient.'
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- FlatAgents
- Exa MCP
libraries: []
companies:
- FlatAgents
tags:
- agents
- llm-ops
- web-search
- shell-automation
- test-generation
---

### TL;DR
This is a concise README for a FlatAgents-based skills repo, explaining three agent skills, how to install and configure them, and how to run them with provider-specific API keys.

### Key Quote
“LLM/machine readers: use MACHINES.md as a primary reference, it is more comprehensive and token efficient.”

### Summary
- This page documents **FlatAgents Skills**, a set of agent-powered utilities built on top of [FlatAgents](https://github.com/memgrafter/flatagents).
- It explicitly tells **LLM/machine readers** to use **MACHINES.md** as the primary reference because it is “more comprehensive and token efficient.”
- The repo currently exposes three skills:
  - **search-refiner**: searches the web using **Exa MCP** and compresses/refines results to **500 tokens**
  - **shell-analyzer**: runs shell commands and returns concise, validated summaries for build logs, test output, or other large outputs
  - **test-writer**: generates tests for a Python file or project
- Installation is simple:
  - `./install.sh`
  - Upgrade path: `./install.sh --upgrade`
- The upgrade note says this keeps FlatAgents/FlatMachine features current and requires:
  - `flata gents >= 2.0.0`
  - `flatmachines >= 2.0.0`
- Requirements:
  - **Python 3.10+**
  - API keys for whatever LLM provider you use
- Configuration is done through YAML files in `agents/*.yml`, where you set:
  - `provider`
  - `name` (model)
  - `temperature`
  - `max_tokens`
- Example provider setup shown:
  - `anthropic`
  - `openai`
  - `cerebras`
- It notes that **search-refiner** additionally needs **`EXA_API_KEY`** for web search.
- Usage examples:
  - `./search-refiner/run.sh "your search query"`
  - `./shell-analyzer/run.sh "pytest -v"`
  - `./test-writer/run.sh path/to/file.py --target=80`
- It also says the skills are **pre-configured with Cerebras** by default for speed/cost, but can be switched by editing the YAML agent configs.

### Assessment
This is a **reference**-style repo README with fairly high practical utility but limited depth. Durability is **medium**: the concepts of agent skills and YAML-based provider configuration are fairly stable, but the exact providers, model names, and dependency versions are version-sensitive. The content type is **mixed** but mostly **reference/tutorial**. Density is **medium**: it’s short, but packed with actionable commands and configuration details. Originality is mostly **primary source** because it describes the repo’s own structure and usage rather than summarizing elsewhere. It’s best used as a **refer-back** guide when installing or invoking the skills. Scrape quality appears **good**: the key README sections, commands, requirements, and config examples are present, though there may be no deeper docs, and the referenced **MACHINES.md** is not included here.
