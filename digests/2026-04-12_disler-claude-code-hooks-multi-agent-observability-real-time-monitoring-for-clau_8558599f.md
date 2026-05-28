---
url: https://github.com/disler/claude-code-hooks-multi-agent-observability
title: 'disler/claude-code-hooks-multi-agent-observability: Real-time monitoring for Claude Code agents through simple hook event tracking.'
scraped_at: '2026-04-12T07:21:36Z'
word_count: 2794
raw_file: raw/2026-04-12_disler-claude-code-hooks-multi-agent-observability-real-time-monitoring-for-clau_8558599f.txt
tldr: A Claude Code observability repo that logs hook events from multiple agents into a Bun/SQLite backend and visualizes them live in a Vue dashboard.
key_quote: Real-time monitoring and visualization for Claude Code agents through comprehensive hook event tracking.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Anthropic
- OpenAI
- ElevenLabs
- Firecrawl
- Casey
- Disler
tools:
- Claude Code
- Astral uv
- Bun
- npm
- yarn
- just
- Vite
- Tailwind CSS
- WebSocket
- SQLite
- Vue
libraries: []
companies:
- Anthropic
- OpenAI
- ElevenLabs
- Firecrawl
tags:
- observability
- multi-agent-systems
- claude-code
- web-dashboard
- hooks
---

### TL;DR
A Claude Code observability repo that logs hook events from multiple agents into a Bun/SQLite backend and visualizes them live in a Vue dashboard.

### Key Quote
"Real-time monitoring and visualization for Claude Code agents through comprehensive hook event tracking."

### Summary
- This repository is a **multi-agent observability system** for Claude Code.
- It captures Claude Code **hook events** in real time, stores them, and displays them in a live dashboard.
- The data flow is:
  - **Claude Agents → Hook Scripts → HTTP POST → Bun Server → SQLite → WebSocket → Vue Client**
- Setup prerequisites listed:
  - **Claude Code**
  - **Astral uv**
  - **Bun**, **npm**, or **yarn**
  - **just** optional
  - **ANTHROPIC_API_KEY** required
  - Optional keys for **OpenAI**, **ElevenLabs**, and **Firecrawl**
- Integration requires copying the `.claude` directory into a project and editing `.claude/settings.json` to set `source-app`.
- The repo shows hook wiring for events such as:
  - `PreToolUse`
  - `PostToolUse`
  - `UserPromptSubmit`
  - plus other Claude Code hook events referenced in the README
- A quick start is included:
  - run `just start` or `./scripts/start-system.sh`
  - open `http://localhost:5173`
  - use Claude Code and generate activity to watch events stream in
- Task recipes via `just` include:
  - `start`, `stop`, `restart`, `server`, `client`, `install`, `health`, `test-event`, `db-reset`, `hooks`, `open`
- Project structure highlights:
  - `apps/server/`: Bun TypeScript server, SQLite DB, HTTP and WebSocket endpoints
  - `apps/client/`: Vue 3 TypeScript client with event timeline, filters, transcript modal, and live pulse chart
  - `.claude/hooks/`: Python hook scripts, validators, and `send_event.py`
  - `.claude/agents/team/`: team agent definitions
  - `.claude/commands/`: slash commands
- Server features described:
  - `POST /events`
  - `GET /events/recent`
  - `GET /events/filter-options`
  - `WS /stream`
  - SQLite with WAL mode
  - schema migrations
  - event validation
  - WebSocket broadcasting
- Client features described:
  - real-time WebSocket updates
  - multi-criteria filtering
  - live pulse chart
  - chat transcript viewer
  - dark/light theme support
  - auto-scroll controls
- The README emphasizes **multi-agent orchestration** and says this system helps trace tool calls, task handoffs, and lifecycle events across parallel agents.
- Security notes include:
  - blocking dangerous `rm -rf` commands in certain cases
  - preventing access to sensitive files like `.env` and private keys
  - guards against infinite hook loops
  - validators for plan files
- The tech stack is:
  - **Server**: Bun, TypeScript, SQLite
  - **Client**: Vue 3, TypeScript, Vite, Tailwind CSS
  - **Hooks**: Python 3.11+, Astral uv, TTS/LLM integrations
  - **Communication**: HTTP REST, WebSocket

### Assessment
This has **high durability** as a concept and medium durability as a repo-specific implementation: the observability and hook-based architecture are broadly useful, but the exact setup, dependencies, and Claude Code agent-teams details can age with tool versions. The content type is **mixed** because it is both reference documentation and a tutorial for setup and integration. Density is **high**: the README is packed with filenames, commands, ports, hook names, and architecture details. Originality is best described as **primary source** for this specific implementation, though it also references Anthropic docs and a YouTube deep dive. For later use, it is **refer-back** material if you want to install, configure, or understand the repo structure; it is also **skim-once** if you only need the high-level idea. Scrape quality is **good**: the README text, lists, code blocks, and section structure are present, and the included images are referenced even if not viewable in the scrape. On the four decision-oriented goals: **Recall** is strong because the summary captures that this is a live Claude Code observability dashboard for multi-agent workflows; **Decide** is strong because the summary makes clear this is worth opening if you need hook-based monitoring or Claude Code integration; **Evaluate** is moderate to strong because it notes the repo is implementation-specific and tied to current Claude Code tooling and hook APIs; **Find** is strong because it names the repo’s purpose, architecture, major endpoints, and distinctive terms like `send_event.py`, `PreToolUse`, `WebSocket`, and `Vue Client`.
