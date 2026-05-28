---
url: https://github.com/coder/mux
title: 'coder/mux: A desktop app for isolated, parallel agentic development'
scraped_at: '2026-04-12T07:41:28Z'
word_count: 473
raw_file: raw/2026-04-12_coder-mux-a-desktop-app-for-isolated-parallel-agentic-development_ecdc88f6.txt
tldr: Mux is a desktop and browser app from Coder for managing multiple AI coding agents in isolated local, worktree, or SSH-backed workspaces, with multi-model support and a UX inspired by Claude Code.
key_quote: Mux is a desktop & browser application for parallel agentic development.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Coder Technologies, Inc.
tools:
- Mux
- Ollama
- OpenRouter
- VS Code
libraries: []
companies:
- Coder
- Coder Technologies, Inc.
tags:
- ai-coding
- agent-orchestration
- workspace-management
- developer-tools
- git-worktrees
---

### TL;DR
Mux is a desktop and browser app from Coder for managing multiple AI coding agents in isolated local, worktree, or SSH-backed workspaces, with multi-model support and a UX inspired by Claude Code.

### Key Quote
"Mux is a desktop & browser application for parallel agentic development."

### Summary
- **What it is**
  - Mux is described as a “Coding Agent Multiplexer” for parallel agentic development.
  - It helps developers plan and execute tasks with multiple AI agents on local or remote compute.

- **Core workflow / workspace types**
  - Supports **isolated workspaces** with a central view of **git divergence**.
  - Three runtime modes are highlighted:
    - **Local**: run directly in the project directory
    - **Worktree**: use git worktrees on the local machine
    - **SSH**: run remotely on a server over SSH
  - The runtime docs are linked at `mux.coder.com/runtime`, with dedicated pages for local, worktree, and SSH.

- **Model support**
  - The app supports multiple model families, including:
    - `sonnet-4-*`
    - `grok-*`
    - `gpt-5-*`
    - `opus-4-*`
  - It also supports:
    - **Ollama** for local LLMs
    - **OpenRouter** for broader cloud model access

- **Integrations and UX**
  - Includes a **VS Code extension** for jumping into Mux workspaces directly from VS Code.
  - Emphasizes UI and keybindings for managing a suite of agents efficiently.
  - Produces **rich markdown outputs**, including **Mermaid diagrams** and **LaTeX**.
  - Uses a **custom agent loop**, but the UX is said to be inspired by Claude Code.
  - Familiar features mentioned:
    - **Plan/Exec mode**
    - **vim inputs**
    - **`/compact`**
  - New features called out:
    - **opportunistic compaction**
    - **mode prompts**

- **Screenshots / product behavior highlighted**
  - Integrated code review for faster iteration
  - Agent status shown in the sidebar
  - Git divergence UI to track changes and conflicts
  - Mermaid diagrams for reviewing complex proposals
  - Costs tab for token/cost tracking
  - Context management dialog for compaction controls
  - Orchestration of parallel agent tasks in plan mode
  - Responsive server mode UI for mobile users

- **Installation**
  - Pre-built binaries are available from the **GitHub Releases** page.
  - The README specifically says binaries are available for **macOS and Linux**.
  - Installation docs are linked at `mux.coder.com/install`.

- **Documentation and development**
  - Full documentation is at `https://mux.coder.com`.
  - Development setup and guidelines are in `AGENTS.md`.

- **License**
  - Licensed under **AGPL-3.0**.
  - Copyright line says **2026 Coder Technologies, Inc.**

### Assessment
This is a **mixed** content type: mostly a **reference/announcement-style project README** with product positioning, feature overview, install pointers, screenshots, and licensing details. Durability is **medium** because the high-level idea of agent orchestration and workspace isolation is fairly stable, but the model names, feature list, and installation details may change quickly as the project evolves. Density is **medium**: it is concise but specific, with plenty of named features, runtime modes, and linked docs. Originality is mostly **primary source**, since it comes directly from the project’s own README and marketing copy rather than third-party commentary. It is best used as **refer-back** material to quickly confirm what Mux is, what modes it supports, and whether it fits a workflow involving parallel coding agents. Scrape quality is **good** overall: the README content, feature list, install notes, screenshots captions, and license are present, though the actual linked docs, images, and AGENTS.md content are not included here.
