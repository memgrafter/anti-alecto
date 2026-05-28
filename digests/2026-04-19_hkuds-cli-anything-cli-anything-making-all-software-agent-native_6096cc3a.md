---
url: https://github.com/HKUDS/CLI-Anything
title: 'HKUDS/CLI-Anything: CLI-Anything: Making ALL Software Agent-Native'
scraped_at: '2026-04-19T06:47:43Z'
word_count: 6940
raw_file: raw/2026-04-19_hkuds-cli-anything-cli-anything-making-all-software-agent-native_6096cc3a.txt
tldr: CLI-Anything is a GitHub repo that turns software codebases into agent-ready CLIs via a Claude Code plugin marketplace, a 7-phase generation pipeline, and a CLI-Hub registry for browsing/installing community-built harnesses.
key_quote: Today's Software Serves Humans👨‍💻. Tomorrow's Users will be Agents🤖.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- pip
- cli-hub
- Claude Code
- Pi Coding Agent
- OpenCode
- Goose
- Qodercli
- OpenClaw
- Codex
- GitHub Copilot CLI
- Cursor
- Windsurf
- npx skills
libraries:
- click
- pytest
- bpy
companies:
- HKUDS
- GitHub
tags:
- ai-agents
- command-line-tools
- software-automation
- developer-tools
- agentic-workflows
---

### TL;DR
CLI-Anything is a GitHub repo that turns software codebases into agent-ready CLIs via a Claude Code plugin marketplace, a 7-phase generation pipeline, and a CLI-Hub registry for browsing/installing community-built harnesses.

### Key Quote
"Today's Software Serves Humans👨‍💻. Tomorrow's Users will be Agents🤖."

### Summary
- **What it is**
  - A project called **CLI-Anything: Making ALL Software Agent-Native**.
  - Core idea: transform software into **command-line harnesses** that AI agents can use directly, without GUI automation.
  - Positioned as a bridge between **AI agents and the world’s software**.

- **Main distribution / discovery flow**
  - **CLI-Hub** is the community registry and package manager:
    - Install with `pip install cli-anything-hub`
    - Browse/install via `cli-hub install <name>`
    - Hub supports browsing, searching, updating, uninstalling, and registry-driven discovery.
  - The repo also exposes a **meta-skill** for autonomous agent discovery of tools in the catalog.

- **Core methodology**
  - The repo treats **`cli-anything-plugin/HARNESS.md`** as the **single source of truth** / standard operating procedure.
  - The build pipeline is a **7-phase process**:
    1. Analyze source code
    2. Design command architecture and state model
    3. Implement Click CLI with REPL, JSON output, undo/redo
    4. Plan tests
    5. Write tests
    6. Document results
    7. Publish / package for PATH installation
  - Generated CLIs ship with **`skills/cli-anything-<software>/SKILL.md`** for agent skill discovery, plus a compatibility copy under the installed package path.

- **Supported agent platforms**
  - Claude Code
  - Pi Coding Agent
  - OpenCode
  - Goose
  - Qodercli
  - OpenClaw
  - Codex
  - GitHub Copilot CLI
  - Mentions future support for Cursor, Windsurf, and others

- **Usage pattern**
  - You point `/cli-anything` at a local codebase or GitHub repo, and it generates a harness.
  - Example install/use flow for Claude Code:
    - `/plugin marketplace add HKUDS/CLI-Anything`
    - `/plugin install cli-anything`
    - `/cli-anything ./gimp`
  - The generated CLI can be installed with `pip install -e .`, then used with:
    - `cli-anything-<software> --help`
    - `cli-anything-<software> --json <command>`
    - bare invocation for REPL mode

- **What the generated CLIs do**
  - Wrap real applications and APIs into structured commands.
  - Examples listed in the repo include:
    - GIMP, Blender, Inkscape, Audacity, LibreOffice
    - Browser automation, Zotero, OBS Studio, Kdenlive, Shotcut
    - Zoom, MuseScore, Draw.io, ETH2 QuickStart, Mermaid, AnyGen
    - ComfyUI, NotebookLM, Dify Workflow, AdGuard Home, Ollama
    - Godot, Sketch, RenderDoc, VideoCaptioner, Openscreen, CloudCompare, Exa, CloudAnalyzer, QGIS, n8n, Safari, Uni-Mol Tools
  - The repo emphasizes:
    - real backends
    - JSON + human-readable output
    - REPL + subcommand interfaces
    - production-style testing

- **Notable claims / features**
  - Claims to make software **agent-native** without losing capability.
  - Says no screenshots, no clicking, no RPA fragility.
  - Uses real application backends like:
    - Blender via `bpy`
    - LibreOffice headless
    - Draw.io XML / CLI
    - MLT / melt for video editors
    - REST APIs for some services
  - Includes a **CLI-Hub meta-skill** so agents can find and install the right CLI autonomously.

- **Project structure / findability**
  - Important paths called out in the repo:
    - `cli-anything-plugin/HARNESS.md`
    - `cli-anything-plugin/commands/`
    - `cli-anything-plugin/QUICKSTART.md`
    - `cli-anything-plugin/PUBLISHING.md`
    - `skills/cli-anything-<software>/SKILL.md`
    - per-software `agent-harness/` directories
  - The repo is both a methodology reference and a collection of concrete harness implementations.

- **Testing / validation**
  - The repo presents extensive testing across many harnesses: unit, E2E, backend-real, and subprocess tests.
  - It claims production-grade verification of outputs like PDFs, PNGs, XML, and rendered media.

- **Limitations**
  - Requires strong frontier models for reliable generation.
  - Works best when source code is available.
  - A single `/cli-anything` run may need iterative `/refine` passes for full coverage.

### Assessment
Durability is **medium**: the core idea of agent-friendly CLIs and software harness generation is fairly durable, but the repo is tightly tied to current agent platforms, packaging flows, and rapidly changing registry/news content. Content type is **mixed**: part tutorial, part reference, part announcement, with a strong promotional layer. Density is **high** because the README packs installation steps, platform-specific instructions, architecture notes, demo claims, and a large software catalog into one page. Originality is **primary source**, since this is the project’s own repository and documentation rather than commentary on it. Reference style is **refer-back**: useful when you need install commands, path names, supported platforms, or the repo’s methodology and vocabulary. Scrape quality is **partial**: the text captured the main README and many sections, but the source itself contains clear internal inconsistencies in test counts and status claims—badge says **2,130 passing**, the demo table says **2,152**, the test summary says **2,120 passed**, and the footer says **1,839 passing**—so those numbers should be treated cautiously and likely reflect stale or conflicting repo state.
