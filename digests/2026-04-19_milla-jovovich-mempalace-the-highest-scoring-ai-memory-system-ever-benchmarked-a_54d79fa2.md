---
url: https://github.com/milla-jovovich/mempalace
title: 'milla-jovovich/mempalace: The highest-scoring AI memory system ever benchmarked. And it''s free.'
scraped_at: '2026-04-19T07:20:57Z'
word_count: 785
raw_file: raw/2026-04-19_milla-jovovich-mempalace-the-highest-scoring-ai-memory-system-ever-benchmarked-a_54d79fa2.txt
tldr: MemPalace is a local-first AI memory system that stores conversation history verbatim, uses semantic search plus a structured “palace” index to retrieve context, and claims strong benchmark results without requiring API calls.
key_quote: Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- ChromaDB
- Claude Code
- Gemini CLI
- MCP
- Ollama Cloud
libraries: []
companies:
- MemPalace
- ChromaDB
tags:
- ai-memory
- semantic-search
- knowledge-graph
- mcp-tools
- local-first-ai
---

### TL;DR
MemPalace is a local-first AI memory system that stores conversation history verbatim, uses semantic search plus a structured “palace” index to retrieve context, and claims strong benchmark results without requiring API calls.

### Key Quote
“Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.”

### Summary
- **What it is**
  - MemPalace is presented as a local-first AI memory system for storing and retrieving conversation history.
  - It explicitly does **not** summarize, extract, or paraphrase stored content; it keeps text verbatim.
  - The system organizes information into a structured metaphor:
    - people and projects become **wings**
    - topics become **rooms**
    - original content lives in **drawers**
  - This structure is meant to make search more scoped than a flat corpus.

- **Retrieval / architecture**
  - Retrieval is pluggable via a backend interface defined in `mempalace/backends/base.py`.
  - Default backend is **ChromaDB**.
  - The repo emphasizes that nothing leaves the user’s machine unless they opt in.
  - The architecture and concepts are documented on the official site under “the palace.”

- **Installation and basic use**
  - Install with:
    - `pip install mempalace`
    - `mempalace init ~/projects/myapp`
  - Core workflow examples:
    - Mine project files: `mempalace mine ~/projects/myapp`
    - Mine Claude Code sessions: `mempalace mine ~/.claude/projects/ --mode convos`
    - Search memories: `mempalace search "why did we switch to GraphQL"`
    - Load context for a session: `mempalace wake-up`
  - For Claude Code, Gemini CLI, MCP tools, and local models, the repo points to getting-started docs on the official site.

- **Benchmarks**
  - Claims are backed by reproducible commands in `benchmarks/BENCHMARKS.md`, with result files committed in the repo.
  - Main benchmark highlighted:
    - **LongMemEval — retrieval recall (R@5, 500 questions)**
      - Raw semantic search, no heuristics, no LLM: **96.6%**
      - Hybrid v4, held-out 450 questions: **98.4%**
      - Hybrid v4 + LLM rerank: **≥99%**
  - The README stresses that the raw 96.6% requires no API key, cloud, or LLM.
  - It describes the hybrid pipeline as adding:
    - keyword boosting
    - temporal-proximity boosting
    - preference-pattern extraction
  - The rerank pipeline uses an LLM reader to choose the best candidate from the top 20 retrieved sessions, and is reported as model-agnostic across Claude Haiku, Claude Sonnet, and minimax-m2.7 via Ollama Cloud.
  - Other reported benchmarks:
    - **LoCoMo**: R@10 **60.3%**; hybrid v5 **88.9%**
    - **ConvoMem**: average recall **92.9%**
    - **MemBench (ACL 2025)**: R@5 **80.3%**
  - The repo explicitly avoids side-by-side comparisons with Mem0, Mastra, Hindsight, Supermemory, or Zep, arguing that metrics and splits are not directly comparable.

- **Knowledge graph**
  - Includes a temporal entity-relationship graph with validity windows.
  - Supported actions include:
    - add
    - query
    - invalidate
    - timeline
  - Backed by local SQLite.

- **MCP server**
  - The project includes **29 MCP tools**.
  - These cover:
    - palace reads/writes
    - knowledge-graph operations
    - cross-wing navigation
    - drawer management
    - agent diaries

- **Agents**
  - Each specialist agent gets its own wing and diary.
  - Agents are discoverable at runtime via `mempalace_list_agents`.
  - The repo presents this as avoiding prompt bloat.

- **Auto-save hooks**
  - Two Claude Code hooks are described:
    - periodic saving
    - saving before context compression

- **Requirements**
  - Python **3.9+**
  - A vector-store backend, with ChromaDB as default
  - About **300 MB** disk for the default embedding model
  - No API key needed for the core benchmark path

- **Docs and project status**
  - Links are provided for:
    - getting started
    - CLI reference
    - Python API
    - benchmark methodology
    - release notes
    - corrections/public notices
  - Contributing is open via PRs.
  - License is **MIT**.
  - The repo shows version **3.3.0** in the badge.

- **Important caution**
  - The top of the page includes a **scam alert** warning that only three sources are official:
    - the GitHub repository
    - the PyPI package
    - `mempalaceofficial.com`
  - It warns that other domains, including `mempalace.tech`, are impostors and may distribute malware.

### Assessment
This is a **mixed** content type, combining product documentation, tutorial-style quickstart, benchmark reporting, and a security notice. Durability is **medium**: the core design ideas of local-first verbatim memory and structured retrieval are fairly stable, but the exact benchmarks, version number (3.3.0), supported tools, and official site details are version- and project-state-dependent. Density is **high**, with many concrete commands, metrics, and architectural details packed into a compact README. Originality is **primary source** for the project’s own claims, though naturally promotional in tone. It’s best used as **refer-back** material if you want install commands, benchmark claims, or a quick understanding of the system’s architecture. Scrape quality is **good**: the main README content, links, badges, and the scam warning are present, though embedded images and linked external docs are not included here.
