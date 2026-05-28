---
url: https://github.com/aiming-lab/AutoHarness
title: 'aiming-lab/AutoHarness: AutoHarness: Automated Harness Engineering for AI Agents'
scraped_at: '2026-04-19T07:56:27Z'
word_count: 1078
raw_file: raw/2026-04-19_aiming-lab-autoharness-autoharness-automated-harness-engineering-for-ai-agents_bb1f2543.txt
tldr: AutoHarness is a Python MIT-licensed framework that wraps LLM clients and agent loops with a governance “harness” for tool safety, context management, auditing, cost tracking, and multi-agent control, presented as a 2-line integration path with three pipeline modes.
key_quote: “Agent = Model + Harness. The model reasons. The harness does everything else.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Claude Code
- Codex
- Anthropic
tools:
- OpenAI
- Claude Code
- Codex
libraries:
- autoharness
companies:
- OpenAI
- Anthropic
tags:
- ai-agents
- governance
- tool-safety
- observability
- prompt-injection
---

### TL;DR
AutoHarness is a Python MIT-licensed framework that wraps LLM clients and agent loops with a governance “harness” for tool safety, context management, auditing, cost tracking, and multi-agent control, presented as a 2-line integration path with three pipeline modes.

### Key Quote
“Agent = Model + Harness. The model reasons. The harness does everything else.”

### Summary
- **What it is**
  - A GitHub project for **AutoHarness: Automated Harness Engineering for AI Agents**.
  - Positioned as a lightweight **governance framework** for agents, where the model handles reasoning and the harness handles operational safety/control.

- **Core claim**
  - The repo argues that the real leap from a “demo-ready” agent to a reliable system comes from **harness engineering**:
    - context management
    - tool governance
    - cost control
    - observability
    - session persistence
  - It frames the “aha moment” for agents as becoming reliable, not just capable.

- **Quick install / basic usage**
  - Install with:
    ```bash
    git clone https://github.com/aiming-lab/AutoHarness.git
    cd AutoHarness && pip install -e .
    ```
  - Wrap an OpenAI client in two lines:
    ```python
    from openai import OpenAI
    from autoharness import AutoHarness

    client = AutoHarness.wrap(OpenAI())
    ```
  - Alternative full loop usage:
    ```python
    from autoharness import AgentLoop

    loop = AgentLoop(model="gpt-5.4", constitution="constitution.yaml")
    result = loop.run("Fix the failing tests in auth.py")
    ```

- **News / release status**
  - Announces **v0.1.0 released on 04/01/2026**.
  - Claims:
    - three-tier pipeline modes
    - 6-step governance pipeline
    - risk pattern matching
    - YAML constitution
    - trace-based diagnostics
    - multi-agent profiles
    - session persistence with cost tracking
    - **958 tests passing**

- **Pipeline modes**
  - **Core**: 6-step pipeline, secret scanner + path guard + output sanitizer, single agent.
  - **Standard**: 8-step pipeline, adds risk classifier + pre-hooks, basic profiles.
  - **Enhanced ⚠️**: 14-step pipeline, adds turn governor + alias resolution + failure hooks, supports fork/swarm/background multi-agent setups.
  - The README states **Enhanced is the default mode**.

- **Core architecture**
  - Tool calls pass through:
    1. Parse & Validate
    2. Risk Classify
    3. Permission Check
    4. Execute
    5. Output Sanitize
    6. Audit Log
  - It emphasizes detection of:
    - dangerous operations
    - secret exposure
    - path traversal
    - prompt injection and other risky behaviors

- **What it claims to improve**
  - Prevents destructive commands like `rm -rf /`
  - Controls token growth with token budget management and truncation
  - Tracks per-call cost with model-aware pricing
  - Uses layered validation for input, execution, and output
  - Produces JSONL audit logs with provenance
  - Supports multi-agent role-based profiles

- **CLI**
  - Notable commands include:
    - `autoharness init`
    - `autoharness mode` / `autoharness mode enhanced`
    - `autoharness validate constitution.yaml`
    - `autoharness check --stdin --format json`
    - `autoharness audit summary`
    - `autoharness install --target claude-code`
    - `autoharness export --format cursor`

- **Comparison claims**
  - The comparison table positions AutoHarness as having capabilities that LangGraph, Guardrails AI, and the OpenAI SDK lack or only partially cover.
  - It emphasizes:
    - tool governance pipeline
    - context management
    - trace-based diagnostics
    - cost attribution
    - no vendor lock-in
    - 2-line setup

- **Acknowledgments / influences**
  - Credits:
    - **Claude Code** for some ideas in Enhanced mode
    - **Codex** for context engineering practices

- **Citation and licensing**
  - Provides a BibTeX citation under the year **2026**.
  - License is **MIT**.

- **Disclaimer**
  - Notes that some Enhanced-mode architectural decisions were informed by public discussion/analysis of Claude Code after its inadvertent publication via Anthropic’s npm registry on **2026-03-31**.
  - Explicitly says AutoHarness does **not** contain, redistribute, or directly translate Anthropic proprietary code.

### Assessment
This is a **mixed** content type: part announcement, part reference/docs, part promotional product overview. Durability is **medium** because the concepts of governance, auditing, and harnessing are broadly durable, but the specifics are tied to a particular repository state, version **v0.1.0**, and dated release claims from **2026**. Density is **medium-high**: it packs many product claims, mode definitions, CLI commands, and architecture details into a compact README. Originality is mainly **primary source** from the project authors, though it also contains clear positioning/comparison and acknowledgment of external influences. It works best as a **refer-back** reference if you want to evaluate the framework, check install/CLI commands, or confirm feature claims. Scrape quality is **good**: the main README sections, code snippets, comparison table, citation, and disclaimer are all present, though embedded images are not semantically captured and any linked subdocs are not included.
