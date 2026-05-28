---
url: https://arxiv.org/html/2602.23193v1
title: 'ESAA: Event Sourcing for Autonomous Agents in LLM-Based Software Engineering'
scraped_at: '2026-04-19T08:27:09Z'
word_count: 4100
raw_file: raw/2026-04-19_esaa-event-sourcing-for-autonomous-agents-in-llm-based-software-engineering_d18b565c.txt
tldr: ESAA proposes an event-sourced orchestration architecture for LLM software agents that keeps agents on a strict JSON contract, logs every action immutably, and verifies state by replaying the event stream and hashing the projected repository state.
key_quote: the source of truth is not the current snapshot of the repository, but an immutable log of intentions, decisions, and effects, from which the current state is deterministically projected
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- M. Fowler
- Q. H. Dang
- S. Yao
- J. Zhao
- D. Yu
- N. Du
- I. Shafran
- K. Narasimhan
- Y. Cao
- S. Hong
- Q. Wu
- J. Yang
- A. Rundgren
- B. Jordan
- S. Erdtman
- N. F. Liu
- K. Lin
- J. Hewitt
- A. Paranjape
- M. Bevilacqua
- P. Liang
- C. E. Jimenez
- O. Press
- Claude Sonnet 4.6
- Codex GPT-5
- Claude Opus 4.6
- GPT-5.3-Codex
- Gemini 3 Pro
tools:
- esaa
- JSON Schema
- SGLang
- XGrammar
- AutoGen
- MetaGPT
- LangGraph
- CrewAI
- SWE-bench
- PARCER
- activity.jsonl
- roadmap.json
libraries: []
companies:
- OpenAI
- GitLab
- LangChain
- mlc-ai
- sgl-project
- Antigravity
- Claude Code
- VSCode
tags:
- event-sourcing
- multi-agent-systems
- llm-software-engineering
- auditability
- structured-generation
---

### TL;DR
ESAA proposes an event-sourced orchestration architecture for LLM software agents that keeps agents on a strict JSON contract, logs every action immutably, and verifies state by replaying the event stream and hashing the projected repository state.

### Key Quote
“the source of truth is not the current snapshot of the repository, but an immutable log of intentions, decisions, and effects, from which the current state is deterministically projected”

### Summary
- **What ESAA is**
  - ESAA stands for **Event Sourcing for Autonomous Agents**.
  - It reframes LLM-based software engineering agents as **intention emitters** rather than direct editors of project state.
  - The architecture separates:
    - **LLM cognition**: proposes structured intentions / patches
    - **Deterministic orchestrator**: validates, persists, applies effects, and projects state

- **Core design**
  - Agents can only output **validated JSON** such as `agent.result` or `issue.report`.
  - The orchestrator:
    - validates outputs against **JSON Schema**
    - enforces **boundary contracts** (`AGENT_CONTRACT.yaml`, `ORCHESTRATOR_CONTRACT.yaml`)
    - appends events to an immutable log (`activity.jsonl`)
    - applies authorized file writes
    - rebuilds a read model (`roadmap.json`)
    - runs replay verification with **SHA-256 hashing**
  - The architecture uses **Event Sourcing** and **CQRS** principles:
    - event log = source of truth
    - read model = derived projection

- **Canonical artifacts**
  - `.roadmap/activity.jsonl`: append-only event store
  - `.roadmap/roadmap.json`: derived materialized view
  - `AGENT_CONTRACT.yaml` / `ORCHESTRATOR_CONTRACT.yaml`: action limits and prohibitions
  - `PARCER_PROFILE.*.yaml`: metaprompt profiles that force strict output envelopes
  - Verification command/pattern: `esaa verify` with replay + hash comparison

- **Immutability and traceability**
  - “Trace-first” means events are recorded before irreversible effects.
  - The architecture enforces an **“immutability of done”** rule: completed tasks do not regress.
  - Corrections happen via new events like `issue.report` rather than rewriting history.

- **Determinism / replay**
  - ESAA canonicalizes projected state and hashes it with **SHA-256**.
  - Replay should reconstruct the exact same projection.
  - Divergence between stored and computed projections is detectable via hash mismatch.

- **Multi-agent concurrency**
  - Multiple agents can work concurrently, but the event log serializes their results into a total order.
  - The orchestrator tracks task claims and completions with correlation identifiers.
  - It can detect conflicts such as overlapping file modifications before applying effects.

- **Case study 1: Landing page**
  - **9 sequential tasks**
  - **49 events**
  - Single-agent composition, with tools/models including **GPT-5.3-Codex**, **Claude Code opus 4.6**, and **Antigravity / Gemini 3 Pro**
  - Produced:
    - specs in `.roadmap/specs/`
    - HTML/CSS/JS in `src/`
    - QA reports in `.roadmap/qa/`
  - Ended with:
    - `run.status=success`
    - `verify_status=ok`

- **Case study 2: Clinical dashboard (`clinic-asr`)**
  - Much larger and more complex:
    - **50 tasks**
    - **15 phases**
    - **7 components**
    - **86 events**
    - about **15 hours** of execution
  - Four heterogeneous LLM agents were used:
    - **Claude Sonnet 4.6** — spec/database/config tasks
    - **Codex GPT-5** — UI architecture, audits, implementation, testing
    - **Antigravity (Gemini 3 Pro)** — persistence, repository layer, service integration
    - **Claude Opus 4.6** — security/privacy docs, observability, deployment guides
  - Event distribution:
    - 30 claims
    - 30 completions
    - 17 promotions
    - 8 phase completions
    - 1 version initialization
  - The paper highlights evidence of concurrency: six claims were recorded within one minute.
  - Status at analysis time:
    - **31/50 tasks done**
    - **2 ready**
    - **17 backlog**
    - **8/15 phases complete**
  - Verification still reported `ok` for the completed portion.

- **Main claims / contributions**
  - Constraining LLM output to schema-valid JSON reduces parsing and protocol failures.
  - Event sourcing gives **auditability**, **forensic traceability**, and **time-travel debugging**.
  - The architecture reduces **blast radius** by denying direct write permissions to agents.
  - Purified read models help mitigate **long-context degradation** and “lost in the middle.”
  - The append-only log enables trustworthy multi-agent coordination without agents needing to know each other’s state.

- **Evaluation / limitations**
  - The evidence is based on only **two case studies**.
  - Results are promising but not enough to prove strong generalization to enterprise-scale repositories, CI-heavy workflows, or monorepos.
  - The paper is explicit that it demonstrates **technical feasibility**, not benchmark dominance.
  - Some claims are architectural and observational rather than controlled experimental proof.

- **Future work**
  - Official CLI: `esaa init/run/verify`
  - Remote repository integration
  - Conflict detection and resolution for concurrent writes
  - Time-travel debugging with visual diffs
  - More evaluation on **SWE-bench** and harder real-world projects
  - Formal verification of orchestrator invariants

### Assessment
Durability is **medium-high**: the architectural ideas around event sourcing, CQRS, replay, and auditability are durable, but the specific implementations, model names, event counts, and dated references to 2026 and current LLM products may age quickly. Content type is **mixed**, leaning technical/research with implementation details and case-study validation. Density is **high**: it is packed with specific artifacts, event types, metrics, and workflow mechanics. Originality is **primary source** research/proposal, though it builds on known patterns like Event Sourcing, CQRS, ReAct, and structured generation. Reference style is **deep-study** if you want the architecture details, or **refer-back** if you’re considering adopting the design. Scrape quality is **good** overall: the text includes abstract, sections, tables, references, and appendices, though it looks like the appendix examples and figure content are only partially represented in plain text and any visual diagrams are missing.
