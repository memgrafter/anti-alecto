---
url: http://argent:8080/reports/som-phase2-tradeoffs/som-phase2-tradeoffs.html
title: 'Society of Mind: Phase 2 vs Architecture Change Tradeoffs'
scraped_at: '2026-04-19T07:42:20Z'
word_count: 1625
raw_file: raw/2026-04-19_society-of-mind-phase-2-vs-architecture-change-tradeoffs_15c23a9b.txt
tldr: This document argues that Phase 2 should not build new memory infrastructure yet; instead, FlatMachines should first name its existing agent types and wire current tool/hook/rule agents into K-line and uniframe logic.
key_quote: Phase 2 as-designed is mostly premature formalization.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- tool_loop
- coding_machine_cli
libraries: []
companies: []
tags:
- architecture
- memory-systems
- agent-taxonomy
- llm-orchestration
- software-design
---

### TL;DR
This document argues that Phase 2 should not build new memory infrastructure yet; instead, FlatMachines should first name its existing agent types and wire current tool/hook/rule agents into K-line and uniframe logic.

### Key Quote
“Phase 2 as-designed is mostly premature formalization.”

### Summary
- The central claim is that the team made a framing mistake: the problem is **not** that agents are too coarse-grained and need to be broken into smaller LLM calls.
- The author argues that **atomic agents already exist** in Phase 1, including:
  - hook actions like censors
  - rule-based evaluators like B-brain loop/stall/cost detectors
  - individual tool calls in `tool_loop`
  - heuristic observers like checkpoint polling and state-history tracking
- What is missing is **taxonomy and wiring**, not new infrastructure:
  - existing non-LLM agents are not connected to Minsky-style observation, capture, and signaling
  - tool-call sequences are already checkpointed
  - `on_tool_calls` / `on_tool_result` already fire on each invocation
  - K-line capture can be built by reading existing checkpoint data, not by inventing a new capture system

- The document lays out **three possible paths**:
  - **Path A: Phase 2 as-designed**
    - Build `KLineStore`, guard learning, and a uniframe generator on context-dict snapshots
    - Verdict: low risk, low reward; likely premature because K-lines remain “thin”
  - **Path B: Recognize what exists**
    - Formalize the agent taxonomy
    - Wire existing non-LLM agents into K-line capture and uniframe slots
    - Verdict: low risk, high reward; the recommended path
  - **Path C: New core primitives**
    - Agent pools, typed signal classes, dynamic specialist selection
    - Verdict: high effort, potentially high reward, but only justified by product need

- It evaluates specific Phase 2 items:
  - **KLineStore protocol**: considered weak because it formalizes snapshots without solving the granularity mismatch
  - **Guard learning formalization**: also weak until K-lines are meaningful
  - **Uniframe generator**: singled out as the best Phase 2 candidate because machine YAMLs are already frame-like and diffing them is legitimately useful

- The content also distinguishes between **what already exists** and **what is actually new**:
  - Existing:
    - tool-call checkpointing
    - tool observation hooks
    - hook actions as agents
  - New:
    - typed signal classes
    - agent pool / dynamic selection
    - parallel agencies

- The recommendation is highly specific:
  - **Do now**:
    - formalize the agent taxonomy
    - create K-lines from tool sequences using existing checkpoints
    - build a typed-slot uniframe generator
  - **Next sprint**:
    - add `signal_class` to the `Signal` dataclass
  - **Later / product-driven**:
    - agent pools and parallel agencies

- The document concludes that the real next step is to treat existing hooks, tools, and rule evaluators as first-class agents, which then makes K-lines, guard learning, and uniframes meaningful.

### Assessment
Durability is **medium**: the architectural argument is likely useful for a while, but it is clearly tied to the FlatMachines / Society of Mind implementation state and specific Phase 2 planning. Content type is **mixed**: part opinion/architecture critique, part implementation roadmap, part reference decision matrix. Density is **high** because it contains concrete taxonomy proposals, named hooks, checkpoint fields like `tool_loop_state`, and a prioritized action list. Originality is **primary source** in the sense that it reflects the author’s own design judgment and project-specific conclusions rather than a summary of external material. Reference style is **refer-back**: this is the kind of document you’d revisit when deciding implementation order or architecture direction. Scrape quality is **partial**: the main text and tables are present, but formatting is messy and some diagram content is flattened inline, so a few structural details may be harder to parse than in the original page.
