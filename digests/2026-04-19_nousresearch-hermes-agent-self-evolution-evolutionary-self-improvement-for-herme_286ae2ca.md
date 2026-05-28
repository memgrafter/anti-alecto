---
url: https://github.com/NousResearch/hermes-agent-self-evolution
title: 'NousResearch/hermes-agent-self-evolution: ⚒ Evolutionary self-improvement for Hermes Agent — optimize skills, prompts, and code using DSPy + GEPA'
scraped_at: '2026-04-19T07:35:10Z'
word_count: 415
raw_file: raw/2026-04-19_nousresearch-hermes-agent-self-evolution-evolutionary-self-improvement-for-herme_286ae2ca.txt
tldr: Hermes Agent Self-Evolution is a MIT-licensed framework from Nous Research that uses DSPy + GEPA to automatically improve Hermes Agent’s skills, prompts, tool descriptions, and eventually code via API-based evolutionary search, with tests and human review as guardrails.
key_quote: “GEPA reads execution traces to understand *why* things fail (not just that they failed), then proposes targeted improvements.”
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Nous Research
tools:
- DSPy
- GEPA
- Darwinian Evolver
- pytest
companies:
- Nous Research
tags:
- prompt-optimization
- evolutionary-search
- agent-frameworks
- software-development
- machine-learning
---

### TL;DR
Hermes Agent Self-Evolution is a MIT-licensed framework from Nous Research that uses DSPy + GEPA to automatically improve Hermes Agent’s skills, prompts, tool descriptions, and eventually code via API-based evolutionary search, with tests and human review as guardrails.

### Key Quote
“GEPA reads execution traces to understand *why* things fail (not just that they failed), then proposes targeted improvements.”

### Summary
- **What it is**
  - A repository for **“Hermes Agent Self-Evolution”**, described as **evolutionary self-improvement for Hermes Agent**.
  - It aims to optimize:
    - skill files
    - tool descriptions
    - system prompt sections
    - tool implementation code
  - The stated approach is to produce **measurably better versions** through **reflective evolutionary search**.

- **Core method**
  - Uses **DSPy + GEPA (Genetic-Pareto Prompt Evolution)**.
  - The workflow is:
    - read the current skill/prompt/tool
    - generate an eval dataset
    - run the GEPA optimizer
    - use execution traces to propose candidate variants
    - evaluate candidates
    - apply constraint gates
    - select the best variant
    - open a **PR against hermes-agent**
  - The text emphasizes that GEPA uses **execution traces** to diagnose *why* failures occur, not just that they occurred.

- **Operational claims**
  - **No GPU training required**
  - Runs entirely via **API calls**
  - Mutates text, evaluates outputs, and selects the best variants
  - Estimated cost: **~$2–10 per optimization run**
  - Claimed to be **ICLR 2026 Oral**
  - Licensed under **MIT**

- **Quick start / usage**
  - Install:
    - `git clone https://github.com/NousResearch/hermes-agent-self-evolution.git`
    - `cd hermes-agent-self-evolution`
    - `pip install -e ".[dev]"`
  - Point the tool at a Hermes Agent checkout:
    - `export HERMES_AGENT_REPO=~/.hermes/hermes-agent`
  - Run a skill evolution job:
    - `python -m evolution.skills.evolve_skill --skill github-code-review --iterations 10 --eval-source synthetic`
  - Or use real session history:
    - `--eval-source sessiondb`
  - The examples show **github-code-review** as the sample skill.

- **Roadmap / phases**
  - A table outlines five phases:
    1. **Phase 1** — Skill files (`SKILL.md`): **implemented**
    2. **Phase 2** — Tool descriptions: planned
    3. **Phase 3** — System prompt sections: planned
    4. **Phase 4** — Tool implementation code: planned
    5. **Phase 5** — Continuous improvement loop: planned

- **Engines**
  - **DSPy + GEPA**
    - For reflective prompt evolution
    - Reads traces and proposes targeted mutations
    - Listed as **MIT**
  - **Darwinian Evolver**
    - For code evolution with Git-based organisms
    - Listed as **AGPL v3**
    - Noted as **external CLI only**

- **Guardrails**
  - Every evolved variant must pass:
    1. **Full test suite**: `pytest tests/ -q` must pass 100%
    2. **Size limits**: skills ≤ 15KB, tool descriptions ≤ 500 chars
    3. **Caching compatibility**: no mid-conversation changes
    4. **Semantic preservation**: no drift from original purpose
    5. **PR review**: human review required; no direct commit

- **Where to look next**
  - The page explicitly points to **PLAN.md** for:
    - architecture
    - evaluation data strategy
    - constraints
    - benchmarks integration
    - phased timeline

### Assessment
This is a **mixed** technical/reference page with some tutorial-like quick-start commands and some product/roadmap framing. Durability is **medium**: the general idea of evolutionary prompt/skill optimization is fairly durable, but specific versions, phase status, pricing, and the “ICLR 2026 Oral” claim may age or require verification. Density is **medium-high** because it packs architecture, workflow, guardrails, roadmap, and install commands into a short README. Originality is primarily **primary source** since it appears to be the project’s own README rather than commentary. It’s best used as **refer-back** material: enough to identify the project, understand its approach, and decide whether to inspect PLAN.md or the code. Scrape quality is **good** for the provided README text, though the actual linked PLAN.md content, code, and any diagrams beyond the ASCII flow are not included here.
