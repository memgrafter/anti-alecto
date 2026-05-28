---
url: https://github.com/nicobailon/pi-subagents
title: 'nicobailon/pi-subagents: Pi extension for async subagent delegation with truncation, artifacts, and session sharing'
scraped_at: '2026-04-12T07:34:23Z'
word_count: 6655
raw_file: raw/2026-04-12_nicobailon-pi-subagents-pi-extension-for-async-subagent-delegation-with-truncati_3336d59d.txt
tldr: pi-subagents is a Pi extension for delegating work to specialized subagents, adding slash commands, async/parallel chains, a TUI agent manager, worktree isolation, artifacts, session logs, and optional model fallback/sandboxing.
key_quote: “Pi extension for delegating tasks to subagents with chains, parallel execution, TUI clarification, and async support.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people: []
tools:
- gh
- npx
- pi
- pi-prompt-template-model
- pi-web-access
- pi-mcp-adapter
libraries: []
companies:
- GitHub
- Pi
tags:
- subagents
- task-automation
- tui
- parallel-execution
- git-worktrees
---

### TL;DR
`pi-subagents` is a Pi extension for delegating work to specialized subagents, adding slash commands, async/parallel chains, a TUI agent manager, worktree isolation, artifacts, session logs, and optional model fallback/sandboxing.

### Key Quote
“Pi extension for delegating tasks to subagents with chains, parallel execution, TUI clarification, and async support.”

### Summary
- **What it is**
  - A GitHub-hosted Pi extension named **`pi-subagents`**.
  - It extends Pi with **subagent delegation** and orchestration features: single runs, sequential chains, parallel execution, background/async runs, and TUI-based clarification.
  - Optional companion integrations are mentioned for:
    - **`pi-prompt-template-model`** for reusable slash-command workflows
    - **`pi-web-access`** for the built-in `researcher` agent
    - **`pi-mcp-adapter`** for MCP tool access

- **Installation / removal**
  - Install with:
    - `pi install npm:pi-subagents`
  - Remove with:
    - `npx pi-subagents --remove`

- **Core user-facing commands**
  - `/run <agent> <task>` — run one agent
  - `/chain agent1 "task1" -> agent2 "task2"` — sequential multi-agent pipeline
  - `/parallel agent1 "task1" -> agent2 "task2"` — parallel execution
  - `/subagents-status` — open async status overlay
  - `/agents` — open the Agents Manager TUI
  - Commands support tab-completion, validation, live progress, and can be run in the background with `--bg`
  - `--fork` starts child runs from a branched session instead of a fresh one

- **Agents**
  - Agents are **Markdown files with YAML frontmatter**.
  - Search/discovery order:
    - Builtin: `~/.pi/agent/extensions/subagent/agents/`
    - User: `~/.pi/agent/agents/{name}.md`
    - Project: `.pi/agents/{name}.md`
  - Builtin agents included:
    - `scout`, `planner`, `worker`, `reviewer`, `context-builder`, `researcher`, `delegate`
  - User/project agents override builtin ones by name.
  - Example frontmatter fields include:
    - `name`, `description`, `tools`, `extensions`, `model`, `fallbackModels`, `thinking`, `skill`, `output`, `defaultReads`, `defaultProgress`, `interactive`, `maxSubagentDepth`

- **Agent configuration highlights**
  - `thinking` appends a suffix to the model string at runtime, e.g. `claude-sonnet-4-5:high`
  - `fallbackModels` defines ordered backup models for provider/model availability failures only
  - `extensions` can sandbox which extensions a subagent may access:
    - absent = all extensions
    - empty = none
    - explicit list = allowlist
  - `tools` can include MCP tools via `mcp:server/tool` syntax if `pi-mcp-adapter` is installed
  - `maxSubagentDepth` tightens recursion depth for nested delegation

- **Chains**
  - Chains live in `.chain.md` files:
    - user: `~/.pi/agent/agents/{name}.chain.md`
    - project: `.pi/agents/{name}.chain.md`
  - Chain variables:
    - `{task}` — original task
    - `{previous}` — prior step output
    - `{chain_dir}` — artifacts directory
  - Supports:
    - sequential steps
    - parallel fan-out/fan-in steps
    - per-step overrides for `model`, `output`, `reads`, `skill`, `progress`, `cwd`
  - Parallel steps support:
    - `concurrency`
    - `failFast`
    - `worktree` isolation

- **Clarification / TUI workflows**
  - The extension has a **chain clarification TUI** and an **Agents Manager overlay**.
  - The Agents Manager supports:
    - browsing, searching, viewing, editing, cloning, deleting, creating, and launching agents/chains
    - multi-select workflows
    - parallel builder
    - chain detail visualization
    - run history display
  - Keybinding examples:
    - `Ctrl+Shift+A` or `/agents` opens the manager
    - `Ctrl+R` runs selected agents as a chain
    - `Ctrl+P` opens parallel builder

- **Execution modes**
  - Supports:
    - **Single**
    - **Chain**
    - **Parallel**
  - All modes support foreground and background execution.
  - Default execution context is `"fresh"`.
  - `"fork"` creates real branched sessions from the parent’s current leaf.
  - Single and parallel modes can use the clarification TUI when `clarify: true`.
  - Chains default to clarify mode unless disabled.

- **Worktree isolation**
  - `worktree: true` gives each parallel agent its own git worktree.
  - Intended to prevent file conflicts when agents edit the same repository in parallel.
  - Requires:
    - a git repository
    - clean working tree
  - After completion, diffs are captured and patch files are written to artifacts.

- **Artifacts, logs, and async observability**
  - The extension writes debug artifacts per task:
    - input prompt
    - full output
    - JSONL event stream
    - metadata with timing, usage, exit code, and model attempts
  - Async runs get dedicated status directories under:
    - `<tmpdir>/pi-async-subagent-runs/<id>/`
  - Background status is exposed through:
    - `subagent_status`
    - `/subagents-status`
  - Notifications are session-scoped.

- **Session sharing**
  - `share: true` exports a session to HTML and uploads it as a GitHub Gist via `gh`
  - Returns a shareable URL
  - Disabled by default due to possible sensitive data exposure

- **Management actions**
  - The tool supports runtime CRUD operations on agents/chains:
    - `list`, `get`, `create`, `update`, `delete`
  - Newly created agents are immediately usable in the same session
  - Config mapping is documented for agent and chain creation/update

- **Docs quality and scope**
  - This README is very detailed and highly implementation-oriented.
  - It includes:
    - examples
    - parameter tables
    - file layout
    - behavior precedence rules
    - config precedence
    - TUI keybindings
    - session/async details
  - It appears to be a **primary source** for the extension, not a secondary summary.

### Assessment
Durability is **medium** because the architectural ideas—subagents, chains, parallel execution, worktrees, session logs, and fallback models—are broadly useful, but the exact commands, file paths, tool names, and versioned model examples are tied to the current Pi ecosystem and this extension’s implementation. Content type is **mixed**, leaning heavily toward **reference** and **tutorial** with some product/documentation style announcement language. Density is **high**: it packs a large amount of specific behavior, syntax, file paths, defaults, and edge-case rules into each section. Originality is **primary source** since it reads like the project’s own README/specification. Reference style is **deep-study** if you plan to use the extension, or **refer-back** for commands/config details. Scrape quality is **good**: the text seems complete and includes extensive prose, tables, and code examples, though any images, the linked demo media, and interactive behavior obviously can’t be fully captured from the scrape alone.
