---
url: https://www.tensorzero.com/
title: TensorZero · open-source LLM infrastructure
scraped_at: '2026-04-19T08:20:47Z'
word_count: 366
raw_file: raw/2026-04-19_tensorzero-open-source-llm-infrastructure_dd4f0273.txt
tldr: TensorZero is an open-source LLM infrastructure platform for building, observing, evaluating, and optimizing production AI systems, with an “Autopilot” product for improving agents and a stack that includes a low-latency gateway, observability, evaluation, optimization, and experimentation.
key_quote: Think of it like Claude Code for LLM engineering.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: skim-once
scrape_quality: partial
people:
- Aaron Hill
- Alan Mishler
- Andrew Jesson
- Antoine Toussaint
- Gabriel Bianconi
- Michelle Hui
- Viraj Mehta
tools: []
libraries: []
companies:
- TensorZero
- FirstMark
- Bessemer
- Bedrock
- OpenAI
tags:
- llm-infrastructure
- llm-observability
- llm-evaluation
- ai-optimization
- startup-product
---

### TL;DR
TensorZero is an open-source LLM infrastructure platform for building, observing, evaluating, and optimizing production AI systems, with an “Autopilot” product for improving agents and a stack that includes a low-latency gateway, observability, evaluation, optimization, and experimentation.

### Key Quote
“Think of it like Claude Code for LLM engineering.”

### Summary
- **What TensorZero is**
  - An **open-source LLM infrastructure** product.
  - Claimed to be used by companies “ranging from frontier AI startups to the Fortune 10.”
  - Says it currently powers **~1% of global LLM API spend**.

- **TensorZero Autopilot**
  - Positioned as an AI-assisted system for **LLM engineering**.
  - Goal: **dramatically improve LLM agent performance across diverse tasks**.
  - Capabilities listed:
    - Analyze **millions of inferences** to find error patterns and optimization opportunities.
    - Set up **evaluations**, prevent regressions, and align LLM judges with real-world scenarios.
    - Recommend **models and inference strategies** to improve quality, cost, and latency.
    - Generate and refine **prompts** using human feedback, metrics, and evaluations.
    - Support optimization workflows like **fine-tuning, reinforcement learning, and distillation**.
    - Run **A/B tests** to validate changes, identify winners, and close the feedback loop.

- **TensorZero Stack**
  - A modular stack for LLM applications with five components:
    - **Gateway**: unified API access to every LLM provider, with **<1ms p99 latency**.
    - **Observability**: monitor LLM systems via UI or programmatically.
    - **Evaluation**: benchmark single inferences or end-to-end workflows.
    - **Optimization**: improve prompts, models, and inference strategies.
    - **Experimentation**: built-in A/B testing, fallbacks, and deployment support.
  - Emphasis on **incremental adoption**: use only what you need and combine with other tools.
  - Claims compatibility with the **OpenAI SDK**, **OpenTelemetry**, and every major LLM provider.
  - Mentions a **Quick Start** that can set up a production-ready LLM app with observability and fine-tuning in **5 minutes**.

- **Company / team**
  - Lists the founding team and their backgrounds:
    - **Aaron Hill**: Rust compiler maintainer, OSS contributor, Svix, AWS
    - **Alan Mishler**: VP at J.P. Morgan AI Research, CMU PhD, 1.3k+ citations
    - **Andrew Jesson**: Columbia postdoc, Oxford PhD, 4k+ citations
    - **Antoine Toussaint**: staff SWE, quant, Stanford math professor, Princeton PhD
    - **Gabriel Bianconi (CEO)**: former CPO at Ondo Finance, Stanford BS/MS
    - **Michelle Hui**: ML + product + community, Wing/Alphabet, UN, Cornell BS/MS
    - **Viraj Mehta (CTO)**: CMU PhD in reinforcement learning, Stanford BS/MS
  - Funding and growth:
    - Backed by **FirstMark, Bessemer, Bedrock**, and dozens of angels.
    - References a **$7.3M seed round** and VentureBeat coverage.
    - Says the company is **hiring in NYC**.

### Assessment
This is a **mixed** landing-page style product overview with a strong **marketing/announcement** tone and some concrete technical claims. **Durability is medium**: the architectural ideas around gateway/observability/evaluation/optimization are broadly useful, but funding claims, adoption stats, and hiring status can become stale quickly. **Density is medium**—it packs in a lot of product positioning and team credibility signals, but not deep technical detail. **Originality is primarily a primary source** because it describes TensorZero’s own offering and team. It’s best used as a **skim-once / refer-back** reference to understand the product’s scope and positioning. **Scrape quality is partial**: the content appears to capture the homepage text, but some links are truncated (“Reach out on”), and any visuals, demos, or deeper docs sections are missing.
