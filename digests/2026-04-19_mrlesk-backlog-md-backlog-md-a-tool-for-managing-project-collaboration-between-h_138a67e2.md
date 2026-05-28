---
url: https://github.com/MrLesk/Backlog.md
title: 'MrLesk/Backlog.md: Backlog.md - A tool for managing project collaboration between humans and AI Agents in a git ecosystem'
scraped_at: '2026-04-19T07:13:20Z'
word_count: 1542
raw_file: raw/2026-04-19_mrlesk-backlog-md-backlog-md-a-tool-for-managing-project-collaboration-between-h_138a67e2.txt
tldr: Backlog.md is a Markdown-native task manager and Kanban tool that turns any Git repo into a local, AI-friendly project board with CLI, web UI, and MCP integrations.
key_quote: Backlog.md turns any folder with a Git repo into a self‑contained project board powered by plain Markdown files and a zero‑config CLI.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- MrLesk
tools:
- Backlog.md
- backlog
- Claude Code
- Gemini CLI
- Codex
- Kiro
- Cursor
- bun
- npm
- brew
- nix
libraries: []
companies:
- Git
- MIT
tags:
- markdown
- task-management
- kanban
- ai-development
- git-workflows
---

### TL;DR
Backlog.md is a Markdown-native task manager and Kanban tool that turns any Git repo into a local, AI-friendly project board with CLI, web UI, and MCP integrations.

### Key Quote
“Backlog.md turns any folder with a Git repo into a self-contained project board powered by plain Markdown files and a zero-config CLI.”

### Summary
- **What it is**
  - Backlog.md is an open-source, MIT-licensed project collaboration tool for managing tasks inside a Git repository.
  - It stores tasks as plain Markdown files in a project-local `backlog/`, `.backlog/`, or custom configured folder.
  - It is designed for both human workflows and “spec-driven AI development.”

- **Core features**
  - Markdown-native task management: each issue is a `.md` file.
  - AI-ready integrations: works with Claude Code, Gemini CLI, Codex, Kiro, Cursor, and other MCP/CLI-compatible assistants.
  - Terminal Kanban board: `backlog board`.
  - Web UI: `backlog browser` for visual task management.
  - Search: `backlog search` across tasks, docs, and decisions.
  - Task viewing/filtering/archiving commands.
  - Definition of Done defaults that can be automatically attached to new tasks.
  - Board export to shareable Markdown reports.
  - Offline/private operation entirely inside the repo.
  - Cross-platform support for macOS, Linux, and Windows.

- **Install / quick start**
  - Global install examples:
    - `bun i -g backlog.md`
    - `npm i -g backlog.md`
    - `brew install backlog-md`
    - `nix run github:MrLesk/Backlog.md`
  - Initialize in a Git repo with:
    - `backlog init "My Awesome Project"`
  - The init wizard can set up:
    - MCP connector for AI tools
    - CLI instruction files like `CLAUDE.md` and `AGENTS.md`
    - Or skip AI setup entirely

- **AI agent workflow**
  - Recommended workflow is to split work into small tasks with clear descriptions and acceptance criteria.
  - Use one task per agent session and one PR per task.
  - Before coding, ask the agent to research the codebase and write an implementation plan.
  - Review at three checkpoints:
    1. task decomposition
    2. implementation plan
    3. code/test results
  - The README emphasizes avoiding overly large tasks to prevent context-window issues.

- **Manual workflow without AI**
  - Backlog.md can also be used as a standalone task manager from the terminal or browser.
  - Example commands:
    - `backlog task create "Render markdown as kanban"`
    - `backlog task edit BACK-1 -d "Detailed context" --ac "Clear acceptance criteria"`
    - `backlog task list -s "To Do"`
    - `backlog search "kanban"`
    - `backlog board`
    - `backlog browser`
  - It recommends using Backlog.md commands rather than editing task files directly, so metadata stays consistent.

- **Web interface**
  - `backlog browser` launches a responsive web app with:
    - drag-and-drop Kanban
    - task creation/editing forms
    - acceptance criteria editor
    - real-time updates
    - archiving dialogs
    - CLI sync with Markdown files
  - Default port is mentioned later in config as `6420` unless changed.

- **MCP integration**
  - Backlog.md can connect to AI assistants through the Model Context Protocol.
  - Client setup examples are provided for:
    - Claude Code
    - Codex
    - Gemini CLI
    - Kiro
  - Manual configuration uses an MCP server command:
    - `backlog mcp start`
  - If the IDE cannot set the working directory, `BACKLOG_CWD` can be set explicitly.
  - Agents can read workflow instructions from the resource `backlog://docs/task-workflow`.
  - The shared server name is `backlog`.

- **CLI reference**
  - The repo points users to `CLI-INSTRUCTIONS.md` for the full command reference.
  - Common commands include `task create`, `task list`, `task edit`, `search`, `board`, and `browser`.

- **Configuration**
  - Config precedence is:
    1. CLI flags
    2. project config file
    3. built-ins
  - Supported config file locations include:
    - `backlog.config.yml`
    - `backlog/config.yml`
    - `.backlog/config.yml`
  - `backlog config` launches an interactive wizard for settings like:
    - branch checking / remote operations
    - auto commit
    - git hooks bypass
    - zero-padded IDs
    - default editor
    - Definition of Done defaults
    - default web port and browser auto-open
  - Safe defaults when skipping advanced setup include:
    - `checkActiveBranches=true`
    - `remoteOperations=true`
    - `activeBranchDays=30`
    - `autoCommit=false`
    - `bypassGitHooks=false`
    - `defaultPort=6420`
    - `autoOpenBrowser=true`

- **Overall impression**
  - This is a polished project README/docs page rather than a deep technical spec.
  - Its main purpose is onboarding: explain what Backlog.md does, how to install it, how to use it with AI tools, and where to find deeper docs.

### Assessment
Durability is **medium**: the underlying ideas—Markdown-based task management, Git-local boards, and AI-assisted workflows—are fairly stable, but specific commands, supported AI clients, config defaults, and integration details may change as the project evolves. The content type is **mixed**, leaning toward **reference** and **tutorial** rather than opinion. Density is **medium**: it covers many concrete commands and setup options, but in README-style prose rather than exhaustive documentation. Originality is **primary source**, since this is the project’s own documentation. Reference style is **refer-back**: useful for installation, setup, and quick command lookup, with `CLI-INSTRUCTIONS.md` and `ADVANCED-CONFIG.md` as likely follow-ups. Scrape quality is **good** overall; the main README content appears captured, though embedded images/GIFs are referenced but not viewable here, and linked subdocuments are not included.
