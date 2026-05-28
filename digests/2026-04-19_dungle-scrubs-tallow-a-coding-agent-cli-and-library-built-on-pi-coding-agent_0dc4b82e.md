---
url: https://github.com/dungle-scrubs/tallow
title: 'dungle-scrubs/tallow: A coding agent CLI and library built on pi-coding-agent'
scraped_at: '2026-04-19T07:41:39Z'
word_count: 1180
raw_file: raw/2026-04-19_dungle-scrubs-tallow-a-coding-agent-cli-and-library-built-on-pi-coding-agent_0dc4b82e.txt
---

### TL;DR
Tallow is a modular terminal-based coding agent CLI and SDK, built on pi-coding-agent, that lets you install only the tools, themes, and agent templates you need while supporting Claude Code compatibility, multi-model routing, multi-agent workflows, and local session/config management.

### Key Quote
“**Tallow is a terminal coding agent that starts minimal and scales up.**”

### Summary
- **What it is**
  - Tallow is a **coding agent for the terminal**.
  - It is described as a **CLI and library** built on **pi-coding-agent** (“pi”).
  - It is marketed as **modular**: you can install only the extensions, themes, and agent templates you want, or enable everything.

- **Project positioning**
  - Designed to **drop into existing Claude Code projects** via **`.claude/` bridging** so switching does not break existing setups.
  - Ships with:
    - **53 extensions**
    - **34 themes**
    - **9 bundled agent templates**

- **Quick start**
  - Install globally with Bun:
    ```bash
    bun add -g @dungle-scrubs/tallow
    tallow install
    tallow
    ```
  - Requires:
    - **Node.js ≥ 22**
    - **An API key** for at least one LLM provider (Anthropic, OpenAI, Google, etc.)
  - Source install path:
    ```bash
    git clone https://github.com/dungle-scrubs/tallow.git
    cd tallow
    bun install
    bun run build
    node dist/install.js
    ```
  - The installer writes config and starter templates to `~/.tallow/`.

- **Main features / highlights**
  - **Multi-model routing**
    - Routes tasks by intent/cost.
    - Example presets:
      - `auto-cheap` for boilerplate
      - `auto-balanced` for everyday work
      - `auto-premium` for accuracy-sensitive tasks
  - **Multi-agent teams**
    - Can spawn specialized agents that share a **task board**.
    - Supports **dependencies, messaging, archive/resume**, and parallel coordination.
  - **Context fork**
    - Branches into isolated subprocesses with their own tools/model, then merges results back.
  - **Workspace rewind**
    - Snapshots tracked and unignored file changes on every conversation turn.
    - Lets you roll back to earlier turns.
  - **Background tasks**
    - Long-running work can run without blocking the session.
  - **LSP support**
    - Jump to definitions, find references, inspect types, search symbols without an editor.
  - **Claude Code compatibility**
    - Scans both `.tallow/` and `.claude/`; `.tallow/` takes precedence.
  - **User-owned config**
    - Agents, commands, and extensions live in `~/.tallow/`, editable by the user.

- **Usage examples**
  - Interactive session: `tallow`
  - Single prompt: `tallow -p "Fix the failing tests"`
  - Pipe context from git diff or files into a prompt
  - Continue last session: `tallow --continue`
  - Choose model/thinking level:
    - `tallow -m anthropic/claude-sonnet-4-20250514 --thinking high`
  - List sessions: `tallow --list`
  - Restrict tools:
    - `tallow --tools readonly`
    - `tallow --tools none`

- **Extension catalog and least-privilege usage**
  - Can inspect extension metadata:
    - `tallow extensions`
    - `tallow extensions --json`
    - `tallow extensions tasks`
  - Supports explicit allowlists for safer sessions:
    - `tallow --extensions-only --extension tasks --extension lsp`
  - Repeat `--extension <selector>` to include only needed capabilities.

- **Configuration layout**
  - Stored in `~/.tallow/`:
    - `settings.json` — theme, icons, keybindings
    - `.env` — startup env vars, supports `op://` refs
    - `auth.json` — provider auth references
    - `models.json` — model configuration
    - `agents/` — editable agent profiles
    - `commands/` — editable slash commands
    - `extensions/` — user extensions, can override bundled ones
    - `sessions/` — persisted conversations
  - Project overrides live in repo-local `.tallow/`.

- **Extending Tallow**
  - **Themes**
    - Set via `/theme` or JSON config.
  - **Icons**
    - Individual TUI glyphs can be overridden in `settings.json`.
  - **Writing extensions**
    - Extensions are **TypeScript** files that receive the `ExtensionAPI`.
    - Example shows registering a `greet` command and sending a UI notification.
    - User extensions go in `~/.tallow/extensions/...`.
  - **SDK**
    - Can be embedded in scripts via `createTallowSession`.
    - Example shows subscribing to session events and prompting the model.
  - **OpenTelemetry**
    - SDK supports tracing via `telemetry.tracerProvider`.
    - CLI subprocesses propagate `TRACEPARENT` and `TRACESTATE` when telemetry is enabled.

- **tmux notes**
  - Tallow works in tmux, but mouse behavior can be affected by `set -g mouse on`.
  - The README includes recommended tmux bindings for:
    - scrolling out of copy-mode naturally
    - double-click word selection
    - triple-click line selection
  - Also gives practical mouse tips for selection, link clicking, and clipboard copying.

- **Known limitations**
  - Requires **Node.js 22+** due to modern ESM features.
  - **Session persistence is local only**; no cloud sync.
  - `web_fetch` is plain HTTP by default, with optional support for `dendrite-scraper` when available for bot-guarded or JS-heavy pages.

- **Contributing and license**
  - Development/contribution guidelines are in `CONTRIBUTING.md`.
  - The project is a **personal side project**, so issue/PR response times may be slow.
  - Licensed under **MIT**.

### Assessment
This is a **mixed reference/tutorial** README with fairly high density: it covers installation, CLI usage, configuration, extension authoring, SDK embedding, tmux ergonomics, and known limitations in one place. **Durability is medium** because the core ideas are relatively stable, but details like version requirements, model IDs, and feature counts can change quickly. It appears to be **primary source** project documentation rather than commentary or synthesis. It is best used as **refer-back** material when deciding whether to adopt Tallow, especially if you want a fast overview of capabilities and setup. **Scrape quality is good**: the README text, code snippets, tables, and major sections are present, though linked docs and external pages are not included here.
