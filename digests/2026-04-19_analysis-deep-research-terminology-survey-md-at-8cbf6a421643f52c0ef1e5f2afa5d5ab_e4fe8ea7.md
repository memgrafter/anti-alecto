---
url: https://github.com/robbintt/analysis/blob/8cbf6a421643f52c0ef1e5f2afa5d5abf426c2a7/DEEP_RESEARCH_TERMINOLOGY_SURVEY.md
title: analysis/DEEP_RESEARCH_TERMINOLOGY_SURVEY.md at 8cbf6a421643f52c0ef1e5f2afa5d5abf426c2a7 · robbintt/analysis
scraped_at: '2026-04-19T07:05:42Z'
word_count: 4804
raw_file: raw/2026-04-19_analysis-deep-research-terminology-survey-md-at-8cbf6a421643f52c0ef1e5f2afa5d5ab_e4fe8ea7.txt
tldr: A living taxonomy of the terms, systems, and benchmarks used in 2023–2025 literature to describe “deep research” AI workflows, mapping them to definitions, use cases, and representative papers.
key_quote: “*A running survey of key terms the literature uses for "deep research" type workflows, their meanings, use cases, and references.*”
durability: high
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Kahneman
tools:
- Model Context Protocol
libraries: []
companies:
- OpenAI
- Google
- Perplexity
tags:
- deep-research
- ai-agents
- information-retrieval
- literature-survey
- evaluation-benchmarks
---

### TL;DR
A living taxonomy of the terms, systems, and benchmarks used in 2023–2025 literature to describe “deep research” AI workflows, mapping them to definitions, use cases, and representative papers.

### Key Quote
“*A running survey of key terms the literature uses for "deep research" type workflows, their meanings, use cases, and references.*”

### Summary
- This document is a **terminology survey** for the “deep research” area, generated on **2026-03-05** from a corpus of roughly **120,000 structured ML paper analyses (2023–2025)** plus cross-references.
- It argues that **“deep research”** is not a single technique but a family of workflows that combine:
  - LLMs with external tools
  - multi-step planning and decomposition
  - adaptive retrieval across sources
  - long-form synthesis with citations
  - agent orchestration and memory/state management
  - evaluation/benchmarking of the whole workflow
- The survey organizes terms into major conceptual buckets:
  - **Top-level / umbrella terms**: agentic search, autonomous research agent, research agent, integrated research, AI scientist, deep research agent/system, etc.
  - **Planning and decomposition**: query/task decomposition, iterative query planning, subquery trees, hierarchical decomposition.
  - **Retrieval and information acquisition**: agentic RAG, adaptive retrieval, multi-hop reasoning, web navigation, viewpoint-aware retrieval, knowledge-gap self-diagnosis.
  - **Synthesis and report generation**: citation grounding, evidence synthesis, conflict-aware synthesis, structured synthesis, long-form report generation, nugget coverage.
  - **Agent architecture and orchestration**: multi-agent workflows, vertical multi-agent systems, dual-system deep research, recursive workflows, plan-code-observe-reflect loops, simulate-before-act.
  - **Memory and state management**: compressed experience buffers, dynamic knowledge bases, persistent world state, memory lifecycle management.
  - **Evaluation and benchmarking**: DR-Bench, DeepResearch-Bench, DR-Arena, ResearcherBench, ResearchRubrics, ScholarGym, LLM-as-Judge, semantic drift, faithfulness vs. groundedness.
  - **Domain-specific variants**: IterSurvey, multimodal deep research, PICOS for medical synthesis, recurrent outline generation, semi-autonomous mode.
  - **Commercial implementations**: OpenAI Deep Research, Gemini Deep Research, Perplexity.
- A notable framing is the **three-stage evolution** of the field:
  - **Agentic Search**
  - **Integrated Research**
  - **Full-stack AI Scientist**
- The document emphasizes that **deep research systems are evaluated differently from standard QA/RAG**:
  - not just answer quality, but **retrieval trustworthiness, citation accuracy, groundedness, topical focus, and process quality**
  - some benchmarks distinguish **faithfulness** from **groundedness**, noting a “**High Faith, Low Ground**” paradox
- It also includes a **review notes** section identifying likely future terminology:
  - reward-based training methods like **GRPO**, **M-GRPO**, **Dual-Reward Optimization**
  - **hallucination propagation / error compounding**
  - **cognitive biases** in research agents
  - **Model Context Protocol (MCP)**
  - **state drift**
  - **budget-constrained research**
  - **hierarchical citation graphs**
- The author explicitly frames this as a **living document** meant to be appended to over time.

### Assessment
This is a **high-durability** reference document: the specific paper list will age, but the terminology map, taxonomy, and conceptual distinctions should remain useful for a long time. It is a **mixed** content type—part reference, part synthesis, part literature survey—with **high density** because it compresses many terms, definitions, and citations into a structured catalog. The work appears to be **original synthesis** built from a large source corpus rather than a primary research paper, and it is best used as a **refer-back** resource when navigating deep-research terminology or deciding which papers/terms to investigate further. Scrape quality looks **good**: the main sections, definitions, references, and review notes are present, and there’s no obvious sign that major content is missing.
