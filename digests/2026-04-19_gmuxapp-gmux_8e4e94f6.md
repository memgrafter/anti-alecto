---
url: https://github.com/gmuxapp/gmux
title: gmuxapp/gmux
scraped_at: '2026-04-19T07:37:21Z'
word_count: 1234
raw_file: raw/2026-04-19_gmuxapp-gmux_8e4e94f6.txt
tldr: gmux is a browser-first terminal/session manager that runs commands as managed sessions, auto-groups them by project, and shows live status for AI agents, tests, and other long-running processes across machines.
key_quote: Keep tabs on every AI agent, test runner, and long-running process across your machines. Work from your desktop, steer from your phone.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- gmux
- gmuxd
- gmux-web
- xterm.js
- pnpm
- WebSocket
- SSE
- REST
libraries: []
companies:
- gmuxapp
- GitHub
- VS Code
- Tailscale
tags:
- terminal-management
- browser-ui
- developer-tools
- process-monitoring
- ai-agents
---

### TL;DR
`gmux` is a browser-first terminal/session manager that runs commands as managed sessions, auto-groups them by project, and shows live status for AI agents, tests, and other long-running processes across machines.

### Key Quote
"Keep tabs on every AI agent, test runner, and long-running process across your machines. Work from your desktop, steer from your phone."

### Summary
- **What it is**
  - `gmux` is a CLI + daemon + web UI system for launching and monitoring commands as managed sessions.
  - It is designed for AI agents, test runners, build commands, and any long-running process.
  - No Electron or desktop app is required; you use a browser.

- **Basic install / startup**
  - Install via Homebrew:
    - `brew install gmuxapp/tap/gmux`
  - Or download from GitHub Releases.
  - Quick start examples:
    - `gmux pi` — launch a coding agent
    - `gmux pytest --watch` — launch a test watcher
    - `gmux make build` — run any command
    - `gmux` — open the UI
  - The UI is available at `localhost:8790`.
  - `gmuxd` starts automatically on first use.
  - For daemon options: `gmuxd -h`

- **How it works**
  - `gmux` wraps a command in a managed session:
    - allocates a PTY
    - exposes a WebSocket for terminal access
    - runs an adapter to infer what the process is doing
  - `gmuxd` runs once per machine:
    - discovers sessions via Unix sockets
    - caches session state
    - proxies WebSocket connections
    - pushes real-time updates to the browser via SSE
    - is stateless and can be restarted safely
  - `gmux-web` is the browser interface:
    - sidebar with grouped sessions
    - terminal built on xterm.js
    - synchronized output for smoother switching
    - 128KB scrollback that replays on reconnect

- **Session intelligence / adapters**
  - Adapters are compiled into the binary and selected automatically by command name.
  - They can report richer state like:
    - thinking
    - waiting for input
    - tests passing
    - build failing
  - Example:
    - `gmux pi` recognizes `pi` and uses the pi adapter automatically
  - Child processes can self-report status through `PUT /status` on `$GMUX_SOCKET`
  - Unknown commands fall back to a shell adapter

- **Directory intelligence / probes**
  - Sessions are grouped into folders by working directory.
  - Folder headings can be enriched by probes:
    - Git branch / dirty state
    - GitHub PR number and status
    - custom script probes
  - Script probes live in `~/.config/gmux/probes/`
  - They can be written in bash and return JSON, with only a few lines needed

- **UI behavior**
  - Sessions are sorted by what needs attention, not alphabetically.
  - Folder status dots reflect the most urgent session inside each folder.
  - Same URL works on desktop and phone.
  - Mobile UI supports tapping a session and sending steering input.
  - `?project=myapp` filters the UI to one project.
  - Theme: Nord dark, with Inter and JetBrains Mono.

- **Architecture / design claims**
  - Runner-authoritative: `gmux` is the source of truth; `gmuxd` is a rebuildable cache.
  - No external deps like tmux, screen, or abduco.
  - Web-first and zero-config.
  - Core stack is two Go binaries plus a web app.

- **Extensibility**
  - Session layer: Go adapters in `gmux`
  - Directory layer: probes in `gmuxd`
  - Child process layer: HTTP API on `$GMUX_SOCKET`
  - User scripts: script probes in `~/.config/gmux/probes/`

- **Development / repo layout**
  - Development setup:
    - `pnpm install`
    - `./dev`
  - Monorepo paths:
    - `cli/gmux` — Go CLI/session launcher
    - `services/gmuxd` — Go daemon for discovery/cache/proxy/probes
    - `apps/gmux-web` — TypeScript/Preact browser UI
    - `packages/protocol` — shared TypeScript/zod schemas
    - `apps/website` — Astro/Starlight docs site
  - Docs cover:
    - Architecture
    - Session schema
    - Adapter architecture
    - Security
    - Remote access / Tailscale setup

- **License**
  - MIT

### Assessment
This is a **mixed** primary-source project README with fairly **high** density: it packs product pitch, quick-start commands, architecture diagrams, feature lists, extensibility details, and repo layout into one page. Durability is **medium** because the core concepts of browser-based session management are lasting, but install commands, ports, implementation details, and feature claims could change as the project evolves. The content is a **reference** more than a tutorial, though it also functions as a quick-start **tutorial** for first use. Originality is **primary source** since it describes the project in its own README and docs structure. The best use is **refer-back**: useful for confirming what gmux does, how it is architected, and where to look deeper in the docs. Scrape quality is **good**; the README content appears complete, including code blocks, diagrams rendered as text, feature lists, and documentation links, with no obvious missing sections.
