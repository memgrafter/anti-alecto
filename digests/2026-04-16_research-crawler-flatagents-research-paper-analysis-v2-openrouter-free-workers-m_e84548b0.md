---
url: https://github.com/memgrafter/research-crawler-flatagents/blob/main/research_paper_analysis_v2/OPENROUTER_FREE_WORKERS.md
title: research-crawler-flatagents/research_paper_analysis_v2/OPENROUTER_FREE_WORKERS.md at main · memgrafter/research-crawler-flatagents
scraped_at: '2026-04-16T03:58:41Z'
word_count: 518
raw_file: raw/2026-04-16_research-crawler-flatagents-research-paper-analysis-v2-openrouter-free-workers-m_e84548b0.txt
tldr: This note lays out a three-phase worker and request-budget strategy for OpenRouter free-tier usage, optimized to maximize `pony-alpha` calls while staying within a shared ~1000 requests/day and ~20 RPM cap.
key_quote: Phase 2 is 100% pony-alpha. Every API call during the expensive phase hits pony-alpha.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- run.py
libraries: []
companies:
- OpenRouter
tags:
- request-budgeting
- worker-scheduling
- api-rate-limits
- openrouter
- throughput-optimization
---

### TL;DR
This note lays out a three-phase worker and request-budget strategy for OpenRouter free-tier usage, optimized to maximize `pony-alpha` calls while staying within a shared ~1000 requests/day and ~20 RPM cap.

### Key Quote
“Phase 2 is 100% pony-alpha. Every API call during the expensive phase hits pony-alpha.”

### Summary
- The document is a planning/reference note titled **“OpenRouter Free Tier Budget Planning (v2)”**.
- It assumes **OpenRouter free requests are shared** across two models:
  - `openrouter/openai/gpt-oss-120b:free` for cheap/structured calls
  - `openrouter/openrouter/pony-alpha` for expensive/reasoning calls
- The stated constraints are:
  - **~1000 requests/day**
  - **~20 requests per minute (RPM)** shared cap

#### Three-phase per-paper workflow
- **Phase 1: Prep**
  - Uses the **cheap model**
  - **1 request**
  - Agent: `key_outcome_writer`
- **Phase 2: Expensive**
  - Uses **pony-alpha only**
  - **3 requests**, all parallel
  - Agents:
    - `why_hypothesis_writer`
    - `reproduction_writer`
    - `open_questions_writer`
- **Phase 3: Wrap**
  - Uses the **cheap model**
  - **3–5 requests**
  - Agents:
    - `limits_confidence_writer`
    - `report_assembler`
    - `completeness_judge`
    - `targeted_repair` if needed
    - `re-judge` if repaired
- Total cost per paper is **7–9 requests**
  - **3 expensive**
  - **4–6 cheap**

#### Why the split matters
- The old two-phase design mixed expensive and cheap calls in the analysis phase.
- That caused **40–60% of calls** to be cheap even when pony-alpha was available.
- The new structure improves efficiency by:
  - making **Phase 2 entirely pony-alpha**
  - pushing **prep and wrap** into cheap-model windows or buffer-filling time

#### Capacity planning scenarios
- **Scenario A: Maximize pony-alpha, steady state with full buffer**
  - 100 papers processed
  - 300 pony-alpha calls
  - 300–500 cheap wrap calls
  - plus 100 prep calls
  - Total: **700–900 calls**
- **Scenario B: Cold start**
  - Build buffer first with 100 prep calls
  - Then 75 papers through expensive + wrap
  - Total: **550–700 calls**
- **Scenario C: Pony-alpha burst window**
  - If pony-alpha comes back after downtime, all workers run the expensive phase
  - 5 workers × 3 requests = **15 pony-alpha calls per pass**
  - Each pass takes about **40 seconds**
  - About **22 passes per 15 minutes**
  - Roughly **330 pony-alpha calls** or **110 papers** through the expensive phase

#### Worker sizing under RPM limits
- The note estimates throughput for different phases:
  - **Expensive phase:** 3 parallel calls, ~40s per paper
    - 5 workers → ~7.5 RPM
    - 8 workers → ~12 RPM
  - **Wrap phase:** 3–5 sequential calls, ~90s per paper
    - 5 workers → ~2 RPM
  - **Prep phase:** 1 call, ~15s per paper
    - 10 workers → ~4 RPM
- The expensive phase is framed as the most RPM-efficient because calls run in parallel.

#### Recommended operating modes
The note ends with example commands:
- **Balanced normal operation**
  - `python run.py --workers 5 --daemon`
- **Maximize pony-alpha throughput**
  - `python run.py --workers 8 --daemon`
- **Fill buffer with cheap calls**
  - `python run.py --workers 10 --prep-only --daemon`
- **Conservative mode**
  - `python run.py --workers 3 --daemon`

### Assessment
This is a **reference/mixed planning document** with **medium durability**: the budgeting strategy and phase-splitting logic are broadly useful, but the exact request caps, model names, and throughput numbers are tied to current OpenRouter behavior and will age as platform limits or model availability change. The content is **high density** because it includes concrete request counts, worker estimates, scenarios, and commands, and it is clearly a **primary-source operational note** rather than a synthesis. It is best used as a **refer-back** document for configuring or auditing the crawler’s execution strategy. Scrape quality is **good**: the full Markdown structure, tables, and code block appear captured, with no obvious missing sections.
