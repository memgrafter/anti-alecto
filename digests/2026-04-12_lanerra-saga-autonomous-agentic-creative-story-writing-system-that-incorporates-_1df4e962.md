---
url: https://github.com/Lanerra/saga
title: 'Lanerra/saga: Autonomous, agentic, creative story writing system that incorporates stored embeddings and Knowledge Graphs.'
scraped_at: '2026-04-12T04:58:34Z'
word_count: 947
raw_file: raw/2026-04-12_lanerra-saga-autonomous-agentic-creative-story-writing-system-that-incorporates-_1df4e962.txt
tldr: SAGA is an early-stage, local-first Python CLI for long-form AI fiction writing that combines LangGraph orchestration, Neo4j canon tracking, and filesystem artifacts to generate chapter-by-chapter novels with consistency checks, revision loops, and resumable workflows.
key_quote: SAGA currently has known critical issues and is **not production-ready**.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- LangGraph
- Neo4j
- Docker
- docker-compose
- OpenAI-compatible HTTP API
libraries:
- Pydantic
companies:
- OpenAI
- DeepWiki
tags:
- ai-fiction-writing
- knowledge-graphs
- workflow-orchestration
- python-cli
- neo4j
---

### TL;DR
SAGA is an early-stage, local-first Python CLI for long-form AI fiction writing that combines LangGraph orchestration, Neo4j canon tracking, and filesystem artifacts to generate chapter-by-chapter novels with consistency checks, revision loops, and resumable workflows.

### Key Quote
> "SAGA currently has known critical issues and is **not production-ready**."

### Summary
- **What it is**
  - **SAGA (Semantic And Graph-enhanced Authoring)**: a **single-user**, **local-first** CLI system for AI-driven novel generation.
  - Core stack:
    - **LangGraph** for checkpointed/resumable workflow orchestration
    - **Neo4j** as persistent story canon store (characters, places, relationships, events)
    - **Filesystem** for human-readable outputs (YAML/Markdown)

- **Design philosophy**
  - Explicitly avoids web/microservice architecture; intended to run on one machine (`docs/PROJECT_CONSTRAINTS.md`).
  - Canon lives in graph DB; writing artifacts live in files for easy inspection/versioning.

- **Current status**
  - The README explicitly says it is **not production-ready** and has known critical issues.

- **Prerequisites / setup**
  - Python **3.12**
  - Running **Neo4j** (docker-compose provided)
  - Local **OpenAI-compatible generation endpoint**
  - Local **embedding endpoint**
  - Setup commands:
    - `python -m venv .venv && source .venv/bin/activate`
    - `pip install -r requirements.txt`
    - `cp .env.example .env`
    - `docker-compose up -d`

- **CLI usage**
  - Bootstrap from premise:
    - `python main.py bootstrap "A suspenseful thriller set inside a deep-sea facility at the bottom of the ocean"`
  - Generate using bootstrapped config:
    - `python main.py generate`
  - Generate directly from premise (auto-accept choices):
    - `python main.py generate "A suspenseful thriller set inside a deep-sea facility at the bottom of the ocean"`

- **Configuration details**
  - Uses **Pydantic settings** via `.env` (`config/settings.py`).
  - Important env vars:
    - `OPENAI_API_BASE`, `OPENAI_API_KEY`
    - `EMBEDDING_API_BASE`, `EMBEDDING_MODEL`
    - `EXPECTED_EMBEDDING_DIM`, `NEO4J_VECTOR_DIMENSIONS`
  - Critical caveat: defaults assume **1024-dim embeddings**, while sample `.env.example` uses **768**; dimensions must be consistent with model output.

- **Output structure**
  - Under `projects/{story_title}/`:
    - `.saga/checkpoints.db` (LangGraph checkpoints)
    - `.saga/logs/`, `.saga/content/*` (drafts, outlines, summaries, extractions, embeddings)
    - `chapters/` (final markdown)
    - `summaries/`
    - `outline/` (`structure.yaml`, `beats.yaml`)
    - `characters/`, `world/` (YAML canon artifacts)
    - `exports/novel_full.md` (compiled manuscript)

- **Workflow (high-level)**
  - **Phase 1: Initialization**
    - Build characters, global act structure (3/5 acts), chapter beats
    - Commit initial canon to Neo4j
    - Persist YAML/Markdown artifacts
  - **Phase 2: Chapter loop**
    1. Plan chapter scenes
    2. Generate scene prose with KG context retrieval
    3. Extract entities/relationships
    4. Generate chapter embeddings
    5. Normalize relationship types
    6. Commit + deduplicate in Neo4j
    7. Validate (consistency, quality, contradiction checks)
    8. Revise on failure and repeat extraction
    9. Finalize chapter + summary + graph healing
    10. Final QA before next chapter

- **Notable features**
  - Scene-level context-aware generation
  - Content externalization via `ContentRef` to keep checkpoints lightweight
  - Graph healing / deduplication
  - LLM-based quality scoring (coherence, pacing, prose, tone)
  - Contradiction detection on timeline/relationship evolution
  - Bootstrap mode with optional review before generation

- **Troubleshooting / maintenance**
  - Inspect logs: `projects/{story_title}/.saga/logs/`
  - Reset graph (destructive): `python reset_neo4j.py`
  - Verify Neo4j connection env vars if connection fails
  - License: **Apache-2.0**

### Assessment
This is a **mixed reference + tutorial-style README** for an actively evolving tool. **Durability: medium**—the architectural concepts (KG-backed canon, chapter loop, checkpointed orchestration) are likely stable, but setup commands, env keys, and workflow behavior may change quickly, especially since it is explicitly “not production-ready.” **Density: high** for a README; it includes concrete commands, folder schema, pipeline stages, and config caveats (notably the 1024 vs 768 embedding-dimension mismatch risk). **Originality: primary source**, since it is the project’s own documentation describing intended design and operation. **Reference style: refer-back**—useful as an operational quickstart/config map while running the tool. **Scrape quality: good**—the main README content, commands, and structure are present; screenshots are referenced but not necessary for understanding core behavior.
