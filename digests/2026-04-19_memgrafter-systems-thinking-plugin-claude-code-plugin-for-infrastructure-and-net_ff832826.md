---
url: https://github.com/memgrafter/systems-thinking-plugin
title: 'memgrafter/systems-thinking-plugin: Claude Code plugin for infrastructure and network architecture decision workflows'
scraped_at: '2026-04-19T08:21:55Z'
word_count: 2134
raw_file: raw/2026-04-19_memgrafter-systems-thinking-plugin-claude-code-plugin-for-infrastructure-and-net_ff832826.txt
tldr: A Claude Code plugin that turns systems-thinking practices into reusable workflows for infrastructure/architecture decisions, emphasizing hidden risks, source-anchored extraction, and decision-ready artifacts.
key_quote: “Understanding what systems *don't* do well is as important as understanding what they do well.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Claude Code
- uv
- tmux
- claude
- pytest
libraries: []
companies:
- GitHub
tags:
- systems-thinking
- infrastructure-architecture
- decision-workflows
- risk-analysis
- claude-code
---

### TL;DR
A Claude Code plugin that turns systems-thinking practices into reusable workflows for infrastructure/architecture decisions, emphasizing hidden risks, source-anchored extraction, and decision-ready artifacts.

### Key Quote
“Understanding what systems *don't* do well is as important as understanding what they do well.”

### Summary
- **What it is**
  - A GitHub repo for `systems-thinking-plugin`, described as a **Claude Code plugin for infrastructure and network architecture decision workflows**.
  - The core idea is the **“iceberg problem”**: vendors and docs show the visible tip, while the real operational complexity sits below the waterline.

- **Why it exists**
  - Designed for systems engineers evaluating:
    - network designs
    - cloud migrations
    - storage architectures
    - vendor proposals/services
    - OS provisioning at scale
  - The repo argues that good decisions require:
    - separating facts from interpretation
    - preserving source anchors and caveats
    - reusing prior designs/patterns
    - producing artifacts suitable for reviews and handoffs

- **Key workflow philosophy**
  - **Extract before you synthesize**: gather claims, limitations, costs, dependencies first; interpret later.
  - **Preserve what you find**: every finding should trace to a file/section/page.
  - **Reuse what worked**: prior designs and patterns are inputs, not just starting points.
  - **Produce artifacts that travel**: outputs are meant for design reviews and stakeholder decisions.

- **Install**
  - Clone and run setup:
    ```bash
    git clone https://github.com/fakoli/systems-thinking-plugin.git
    cd systems-thinking-plugin
    ./setup.sh
    ```
  - Setup checks for:
    - `uv`
    - `python3`
    - optional `tmux`
    - optional `claude` CLI
  - Then it syncs dependencies and runs validation.

- **Main workflows**
  - `/complexity-mapper`
    - Scans a design/vendor/architecture doc for hidden complexity, cost traps, scaling cliffs, dependency chains, and operational burden.
    - Produces a **Complexity Heat Map** and **Hidden Risk Summary**.
  - `/context-sharding`
    - Splits large material into chunks and extracts from each independently.
    - Produces **Context Packets**.
  - `/pattern-remix`
    - Adapts a known-good design to new constraints.
    - Produces a **Pattern Remix Draft** with divergence risks.
  - `/decision-brief`
    - Turns findings into a stakeholder-ready **Decision Brief** with evidence, options, risks, and next steps.
  - `/architecture-risk-review`
    - Focuses on failure modes, hidden dependencies, SPOFs, blast radius, and survivability.
    - Produces a **Hidden Risk Summary**.

- **How the workflow runs**
  - Example shown for `/complexity-mapper`:
    1. invoke the skill
    2. document indexing (`doc-indexer`)
    3. optional source discovery via web research (`web-researcher`)
    4. dispatch planning (`extraction-planner`)
    5. parallel extraction by specialized agents
    6. synthesis into structured outputs
  - The example output highlights:
    - SLA exclusions
    - storage pricing tiers
    - missing rollback procedure
    - pricing calculator limitations
    - hidden risks like IOPS throttling and undocumented backup restore time

- **Agents**
  - **Orchestration**
    - `web-researcher` — discovers source material
    - `extraction-planner` — estimates volume and plans dispatch
  - **Extraction**
    - `doc-indexer`
    - `doc-reader`
    - `caveat-extractor`
    - `cost-capacity-analyst`
    - `architecture-dependency-mapper`
  - **Synthesis**
    - `pattern-remix-planner`
    - `synthesis-brief-writer`
  - Only `web-researcher` has web access; the rest operate on pre-discovered material.
  - The plugin uses a pipeline like:
    - `web-researcher → doc-indexer → extraction-planner → parallel extractors → synthesis-brief-writer`

- **Reference material layout**
  - Recommended folders under `reference/`:
    - `previous_designs/`
    - `vendor_docs/`
    - `prompts/`
    - `examples/`

- **Output contracts**
  - Defined in `docs/output-contracts.md`
  - Output types include:
    - Hidden Risk Summary
    - Complexity Heat Map
    - Decision Brief
    - Pattern Remix Draft
    - Context Packet
  - Every finding includes **source anchors**.

- **Testing**
  - CI tests:
    ```bash
    uv run pytest tests/unit tests/contracts -v
    ```
  - Manual evals require Claude CLI and run locally:
    ```bash
    uv run pytest tests/evals -v -m eval --timeout=300
    uv run pytest tests/evals -v -k complexity_mapper
    python tests/evals/harness.py --dry-run
    ```

- **Further reading**
  - `docs/systems-thinking-foundations.md`
  - `docs/output-contracts.md`
  - `docs/agent-design-principles.md`
  - `docs/repo-conventions.md`
  - `examples/usage-scenarios.md`
  - `COMPATIBILITY_NOTES.md`

### Assessment
This is a **mixed** repository README/documentation page with fairly high information density and moderate-to-high durability, since the systems-thinking framing is timeless but the implementation details, workflow names, and tooling dependencies are version- and platform-specific. It is a **primary source** for how the plugin is intended to work, with strong reference value if you want to understand the repo’s architecture, workflows, and output contracts rather than just install it. The style is best suited for **refer-back** use: it’s detailed enough to justify re-reading when setting up or using the plugin, especially because it names specific agents, commands, outputs, and test invocations. Scrape quality is **good**: the README content is captured well, including command blocks, tables, and workflow explanations, though linked docs, images, and the actual referenced files are not included here.
