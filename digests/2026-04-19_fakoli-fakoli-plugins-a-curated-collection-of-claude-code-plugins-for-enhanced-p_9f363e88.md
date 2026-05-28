---
url: https://github.com/fakoli/fakoli-plugins
title: 'fakoli/fakoli-plugins: A curated collection of Claude Code plugins for enhanced productivity and development workflows'
scraped_at: '2026-04-19T08:21:13Z'
word_count: 1279
raw_file: raw/2026-04-19_fakoli-fakoli-plugins-a-curated-collection-of-claude-code-plugins-for-enhanced-p_9f363e88.txt
tldr: A GitHub marketplace repo for Claude Code plugins that bundles productivity, media, security, and workflow tools, with documented install commands, plugin architecture, and a CI-validated contribution pipeline.
key_quote: “Extend Claude Code with production-grade plugins.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- fakoli
tools:
- Claude Code
- GitHub Actions
- gws
- WebFetch
- WebSearch
- NotebookLM
- Gemini
libraries: []
companies:
- GitHub
- Anthropic
- Google
- OpenAI
- Deepgram
- ElevenLabs
tags:
- claude-code
- plugins
- productivity-tools
- workflow-automation
- github-repository
---

### TL;DR
A GitHub marketplace repo for Claude Code plugins that bundles productivity, media, security, and workflow tools, with documented install commands, plugin architecture, and a CI-validated contribution pipeline.

### Key Quote
“Extend Claude Code with production-grade plugins.”

### Summary
- **What this repository is**
  - `fakoli/fakoli-plugins` is a curated marketplace for Claude Code plugins.
  - It is positioned as a collection of “battle-tested” plugins covering Google Workspace automation, AI image generation, text-to-speech, diagram authoring, secure web fetching, and marketplace self-management.
  - The repository is MIT licensed and uses GitHub Actions for validation.

- **Quick start / installation**
  - Add the marketplace to Claude Code with:
    - `/plugin marketplace add fakoli/fakoli-plugins`
  - Install individual plugins with commands such as:
    - `/plugin install gws`
    - `/plugin install safe-fetch`
    - `/plugin install nano-banana-pro`

- **What Claude Code plugins include**
  - **Skills**: reusable context files for workflows and tool use
  - **Commands**: slash commands like `/send-email`, `/speak`, `/fetch`
  - **Agents**: isolated sub-agents for multi-step tasks
  - **Hooks**: `PreToolUse` / `PostToolUse` interceptors for guarding or modifying behavior
  - Plugins are stored in directories with a `.claude-plugin/plugin.json` manifest.
  - The marketplace validates plugins against a JSON Schema on every push and pull request.

- **Highlighted ecosystem plugins**
  - **fakoli-crew**
    - A set of 8 polyglot agents: architect, reviewer, researcher, plugin engineer, integration specialist, documenter, infrastructure engineer, QA.
  - **fakoli-flow**
    - Intent-driven orchestration pipeline: brainstorm → plan → execute → verify → finish.
    - Uses wave-based dispatch and mandatory critic gates between code-writing phases.
  - **systems-thinking**
    - Multi-agent architecture analysis: discovery → extraction → synthesis.
    - Intended for decisions affecting the whole system.
  - These three are described as complementary: workers, orchestration, and architecture analysis.

- **Other available plugins**
  - **gws**
    - Full Google Workspace integration via the `gws` CLI.
    - Claims 100 skills, 15 commands, 11 role-based agents, and 44 recipes across Gmail, Calendar, Drive, Docs, Sheets, Slides, Chat, and more.
  - **notebooklm-enhanced**
    - Programmatic control of Google NotebookLM for notebooks, PDF/YouTube ingestion, podcast and slide deck generation, and end-to-end research workflows.
  - **nano-banana-pro**
    - AI image generation/editing/remixing with Google Gemini 3 Pro.
    - Includes a 5-agent “PaperBanana” pipeline: Retriever → Planner → Stylist → Visualizer → Critic.
  - **fakoli-speak**
    - Multi-provider text-to-speech for Claude Code.
    - Supports OpenAI, Deepgram, ElevenLabs, Google Gemini, and macOS Say.
    - Includes `/provider`, `/cost`, and `/autospeak`.
  - **excalidraw-diagram**
    - Generates `.excalidraw` diagrams from natural language or codebase analysis.
    - Supports flowcharts, architecture diagrams, ER diagrams, and dependency graphs.
  - **safe-fetch**
    - A drop-in replacement for Claude’s web fetch/search that sanitizes content through a 6-layer pipeline.
    - Claims to neutralize CSS-hidden text, zero-width Unicode, fake LLM delimiters, base64 payloads, and markdown exfiltration vectors.
  - **marketplace-manager**
    - Manages plugin creation and marketplace maintenance from inside Claude Code.
    - Can scaffold plugins, validate manifests, regenerate registry indices, and install GitHub Actions workflows.

- **Example commands shown**
  - `/triage` for Gmail search/triage
  - `/generate-image ...` for banner generation
  - `/fetch https://...` for safe webpage fetching
  - `/excalidraw ...` for architecture diagrams
  - `/speak` and `/provider deepgram` for TTS
  - `/add-plugin my-new-plugin` for scaffolding plugins

- **How to create a plugin**
  - The repo gives a 5-step process:
    1. Copy the basic template from `templates/basic` into `plugins/your-plugin-name`
    2. Edit `.claude-plugin/plugin.json`
    3. Add skills, commands, agents, or hooks
    4. Validate locally with `./scripts/validate.sh plugins/your-plugin-name`
    5. Open a pull request for CI validation
  - Plugin structure is explicitly documented, including required `plugin.json` and `README.md`.

- **Validation and CI**
  - Every pull request runs three checks:
    - `validate.yml`: schema, required files, JSON validity
    - `pr-check.yml`: preview of registry changes
    - `update-index.yml`: auto-regenerates `registry/index.json` on merge to main
  - The schema is stored at `schemas/plugin.schema.json`.
  - Local validation is encouraged before pushing.

- **Documentation and repo layout**
  - Key docs include:
    - Contributing Guide
    - Create Your Own Marketplace
    - Plugin Guidelines
    - Testing Standards
    - Official Anthropic plugin docs
  - Repo structure includes:
    - `.github/workflows/`
    - `plugins/`
    - `archive/`
    - `registry/`
    - `schemas/`
    - `scripts/`
    - `templates/`
    - `docs/`

- **Archived plugins**
  - Some plugins are archived and preserved in `archive/` for reference, but are no longer actively maintained.

### Assessment
This is a **mixed** reference/tutorial repository with fairly high **density** because it packs installation instructions, plugin descriptions, repo structure, and contribution workflow into one page. Its **durability is medium**: the general plugin architecture and contribution patterns will remain useful, but the specific plugin lineup, counts, and claimed capabilities are tied to the current repository state and Claude Code/plugin ecosystem. It is largely a **primary source** for this marketplace’s own documentation and should be used as a **refer-back** reference rather than deep study. The scrape quality is **good** overall: the main README content, lists, commands, and tables are present, though linked subdocs and actual plugin implementations are not included here.
