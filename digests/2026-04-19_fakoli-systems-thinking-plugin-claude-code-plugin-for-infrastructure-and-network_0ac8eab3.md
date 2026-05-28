---
url: https://github.com/fakoli/systems-thinking-plugin
title: 'fakoli/systems-thinking-plugin: Claude Code plugin for infrastructure and network architecture decision workflows'
scraped_at: '2026-04-19T08:21:28Z'
word_count: 2308
raw_file: raw/2026-04-19_fakoli-systems-thinking-plugin-claude-code-plugin-for-infrastructure-and-network_0ac8eab3.txt
tldr: A Claude Code plugin that turns infrastructure and architecture evaluation into a structured, systems-thinking workflow for finding hidden complexity, costs, dependencies, and risks before committing to a design.
key_quote: Understanding what systems *don't* do well is as important as understanding what they do well.
durability: high
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
- claude CLI
libraries: []
companies:
- GitHub
- fakoli-flow
tags:
- systems-thinking
- infrastructure
- architecture-review
- workflow-automation
- risk-analysis
---

### TL;DR
A Claude Code plugin that turns infrastructure and architecture evaluation into a structured, systems-thinking workflow for finding hidden complexity, costs, dependencies, and risks before committing to a design.

### Key Quote
“Understanding what systems *don't* do well is as important as understanding what they do well.”

### Summary
- **What it is:** A GitHub repository for `systems-thinking-plugin`, described as a Claude Code plugin for infrastructure and network architecture decision workflows.
- **Core idea:** It applies systems engineering habits to vendor evaluation, cloud migration, storage design, and architecture review by focusing on what is hidden “below the waterline”:
  - quotas and limits
  - scaling cliffs
  - cost mechanics
  - dependency chains
  - operational burdens
  - caveats buried in documentation
- **Main philosophy:**  
  - **Extract before you synthesize** — gather factual claims first, then interpret them.
  - **Preserve what you find** — every finding should have source anchors.
  - **Reuse what worked** — adapt prior designs and proven patterns to new constraints.
  - **Produce artifacts that travel** — generate stakeholder-ready outputs like decision briefs and risk summaries.

- **Installation:**
  - Clone the repo:
    ```bash
    git clone https://github.com/fakoli/systems-thinking-plugin.git
    cd systems-thinking-plugin
    ./setup.sh
    ```
  - `setup.sh` checks for `uv`, `python3`, `tmux` (optional), and `claude` CLI (optional), then syncs dependencies and runs validation.

- **Workflows provided:**
  - `/complexity-mapper`
    - Scans a design/vendor proposal/architecture doc for hidden complexity.
    - Outputs a **Complexity Heat Map** and **Hidden Risk Summary**.
  - `/context-sharding`
    - Breaks large material into chunks for independent extraction.
    - Produces **Context Packets** with findings and source anchors.
  - `/pattern-remix`
    - Adapts a known-good design to new constraints.
    - Produces a **Pattern Remix Draft**.
  - `/decision-brief`
    - Packages findings into a stakeholder-ready **Decision Brief**.
  - `/architecture-risk-review`
    - Focuses on failure modes, dependencies, SPOFs, blast radius, and survivability.
    - Produces a **Hidden Risk Summary**.

- **Example workflow described for `/complexity-mapper`:**
  1. User invokes the skill with a problem statement.
  2. `doc-indexer` maps document structure and flags high-value / caveat-rich sections.
  3. `web-researcher` finds missing external sources when needed.
  4. `extraction-planner` decides how many extraction agents to spawn.
  5. Parallel extractors gather claims, caveats, costs, and dependencies.
  6. `synthesis-brief-writer` combines outputs into artifacts like a **Complexity Heat Map** with top risks and evidence.

- **Agent architecture:**
  - **Orchestration agents**
    - `web-researcher` — source discovery via web and local files
    - `extraction-planner` — dispatch planning
  - **Extraction agents**
    - `doc-indexer` — document structure mapping
    - `doc-reader` — technical claim extraction
    - `caveat-extractor` — buried limitations and traps
    - `cost-capacity-analyst` — cost and scaling constraints
    - `architecture-dependency-mapper` — control/data-plane dependencies
  - **Synthesis agents**
    - `pattern-remix-planner` — adapt prior work
    - `synthesis-brief-writer` — generate decision artifacts
  - Only `web-researcher` has web access; others use discovered material via Read/Grep/Glob.

- **Reference material layout:**
  - `previous_designs/`
  - `vendor_docs/`
  - `prompts/`
  - `examples/`
  These directories are meant to hold the source documents the agents analyze.

- **Output contracts:**
  - **Hidden Risk Summary**
  - **Complexity Heat Map**
  - **Decision Brief**
  - **Pattern Remix Draft**
  - **Context Packet**
  - Every finding is intended to include source anchors.

- **Testing:**
  - CI runs unit and contract tests:
    ```bash
    uv run pytest tests/unit tests/contracts -v
    ```
  - Manual evals require the Claude CLI and are run locally:
    ```bash
    uv run pytest tests/evals -v -m eval --timeout=300
    uv run pytest tests/evals -v -k complexity_mapper
    python tests/evals/harness.py --dry-run
    ```

- **Integration with `fakoli-flow`:**
  - The plugin can work with another orchestration plugin to run agents in waves:
    - Wave 1: discovery
    - Wave 2: parallel extraction
    - Wave 3: synthesis
  - Agents communicate via status files in `docs/plans/agent-<name>-status.md`.

- **Documentation pointers:**
  - `docs/systems-thinking-foundations.md`
  - `docs/output-contracts.md`
  - `docs/agent-design-principles.md`
  - `docs/repo-conventions.md`
  - `docs/flow-protocol.md`
  - `docs/status-file-template.md`
  - `examples/usage-scenarios.md`
  - `COMPATIBILITY_NOTES.md`

### Assessment
This is a **mixed** content type: part tool/plugin documentation, part design rationale, and part workflow/reference guide. Durability is **medium to high** because the systems-thinking framing and workflow patterns are broadly reusable, but some operational details depend on Claude Code, `uv`, and the repo’s current agent setup. Density is **high**: the README is packed with specific workflow names, agent roles, output artifacts, test commands, and execution flow examples. Originality is mostly **primary source** with a strong product/design pitch, since it describes the repository’s own architecture and intended usage rather than summarizing others. It’s best used as a **refer-back** reference rather than skim-once, especially if you want to understand the plugin’s workflow model, agent roles, or installation/testing steps. Scrape quality is **good**: the main README content appears intact, including code blocks, tables, and section structure, though linked documents and images are not included here.
