---
url: https://github.com/steveyegge/gastown
title: 'steveyegge/gastown: Gas Town - multi-agent workspace manager'
scraped_at: '2026-04-12T07:35:53Z'
word_count: 3356
raw_file: raw/2026-04-12_steveyegge-gastown-gas-town-multi-agent-workspace-manager_ffbc2505.txt
tldr: Gas Town is a Git-backed multi-agent workspace manager for AI coding agents that centers on a “Mayor” coordinator, persistent hooks/worktrees, Beads issue tracking, and queue-based execution/merge workflows like Convoys, Refinery, and Wasteland federation.
key_quote: Gas Town is a workspace manager that lets you coordinate multiple AI coding agents working on different tasks.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Claude Code
- GitHub Copilot
- Codex
- Gemini
tools:
- git
- tmux
- sqlite3
- Docker Compose
- Claude Code CLI
- Codex CLI
- GitHub Copilot CLI
- beads
- bd
- Dolt
libraries: []
companies:
- GitHub
- OpenAI
- Google
- DoltHub
tags:
- multi-agent-systems
- ai-coding
- workspace-management
- git-worktrees
- agent-orchestration
---

### TL;DR
Gas Town is a Git-backed multi-agent workspace manager for AI coding agents that centers on a “Mayor” coordinator, persistent hooks/worktrees, Beads issue tracking, and queue-based execution/merge workflows like Convoys, Refinery, and Wasteland federation.

### Key Quote
"Gas Town is a workspace manager that lets you coordinate multiple AI coding agents working on different tasks."

### Summary
- **What it is**
  - A multi-agent orchestration system for **Claude Code, GitHub Copilot, Codex, Gemini, and others**.
  - Designed to keep work persistent across agent restarts using **git-backed hooks/worktrees** and **Beads** state tracking.

- **Core model**
  - **Mayor**: the primary AI coordinator; the README says to start here and tell it what you want to accomplish.
  - **Town**: the workspace directory, e.g. `~/gt/`.
  - **Rigs**: project containers wrapping git repos.
  - **Crew Members**: your personal workspace within a rig.
  - **Polecats**: worker agents with persistent identity but ephemeral sessions.
  - **Hooks**: persistent storage using git worktrees; survives crashes/restarts.
  - **Convoys**: work-tracking units that bundle beads and assign them to agents.
  - **Beads / issues**: structured git-backed work items; bead IDs look like `gt-abc12` or `hq-x7k2m`.
  - **Molecules**: workflow templates defined in TOML, with “root-only wisps” and “poured wisps” execution modes.
  - **Witness / Deacon / Dogs**: layered monitoring and maintenance system for agent health.
  - **Refinery**: merge queue processor that batches completed work and merges via a Bors-style bisecting queue.
  - **Escalation**: severity-routed blocker handling (`CRITICAL/P0`, `HIGH/P1`, `MEDIUM/P2`).
  - **Scheduler**: capacity governor to avoid API rate-limit exhaustion.
  - **Seance**: session discovery/continuation from `.events.jsonl` logs.
  - **Wasteland**: federated network for sharing wanted work across Gas Towns via DoltHub.

- **Installation prerequisites**
  - **Go 1.25+**
  - **Git 2.25+**
  - **Dolt 1.82.4+**
  - **beads (bd) 0.55.4+**
  - **sqlite3**
  - **tmux 3.0+**
  - **Claude Code CLI** (default runtime)
  - Optional runtimes: **Codex CLI**, **GitHub Copilot CLI**

- **Install examples**
  - `brew install gastown`
  - `npm install -g @gastown/gt`
  - `go install github.com/steveyegge/gastown/cmd/gt@latest`
  - Manual build on Windows or fallback:
    - `git clone https://github.com/steveyegge/gastown.git && cd gastown`
    - `go build -o gt.exe ./cmd/gt`

- **Quick-start flow**
  - `gt install ~/gt --git`
  - `cd ~/gt`
  - `gt config agent list`
  - `gt mayor attach`
  - Then tell the Mayor what to build.

- **Basic multi-agent workflow**
  - Start the Mayor: `gt mayor attach`
  - Create a convoy: `gt convoy create "Feature X" gt-abc12 gt-def34 --notify --human`
  - Sling work to an agent: `gt sling gt-abc12 myproject`
  - Track progress: `gt convoy list`
  - Monitor agents: `gt agents`

- **Workflows shown in the README**
  - **Mayor workflow**: recommended for complex, multi-issue work.
  - **Minimal mode**: no tmux; manually run runtime sessions and let Gas Town track state.
  - **Beads formula workflow**: execute TOML-defined templates with `bd formula list`, `bd cook release --var version=1.2.0`, or `bd mol pour release --var version=1.2.0`.
  - **Manual convoy workflow**: create a convoy with `--human`, add issues, and assign them explicitly.

- **Runtime configuration**
  - Runtimes are configured per rig in `settings/config.json`.
  - Claude uses hooks in `.claude/settings.json`.
  - Codex fallback behavior includes `gt prime`, optional `gt mail check --inject`, and `gt nudge deacon session-started`.
  - GitHub Copilot has a built-in preset with executable lifecycle hooks in `.github/hooks/gastown.json`.

- **Important commands**
  - Workspace: `gt install`, `gt rig add`, `gt crew add`
  - Agents: `gt agents`, `gt sling`, `gt mayor attach`, `gt prime`, `gt feed`
  - Convoys: `gt convoy create`, `gt convoy list`, `gt convoy show`, `gt convoy add`
  - Config: `gt config agent set`, `gt config default-agent`
  - Health: `gt escalate`, `gt scheduler status`, `gt seance`
  - Beads: `bd formula list`, `bd cook`, `bd mol pour`
  - Wasteland: `gt wl join`, `gt wl browse`, `gt wl claim`, `gt wl done`

- **Monitoring and dashboards**
  - `gt feed` provides a TUI with:
    - **Agent Tree**
    - **Convoy Panel**
    - **Event Stream**
  - Problems view classifies agents as:
    - **GUPP Violation**
    - **Stalled**
    - **Zombie**
    - **Working**
    - **Idle**
  - Web dashboard:
    - `gt dashboard`
    - `gt dashboard --port 3000`
    - `gt dashboard --open`

- **Health/scale mechanisms**
  - A three-tier watchdog chain is described:
    - **Daemon** → **Boot** → **Deacon** → **Witnesses & Refineries**
  - The README emphasizes this as a way to keep large agent fleets healthy and recover stuck sessions.

- **Telemetry**
  - Emits OpenTelemetry-style structured logs and metrics to OTLP-compatible backends.
  - Example env vars:
    - `GT_OTEL_LOGS_URL`
    - `GT_OTEL_METRICS_URL`
  - Tracks session lifecycle, agent state changes, bd calls, mail operations, sling/nudge/done workflows, and more.

- **Docs and references**
  - The README points to design docs for:
    - architecture
    - glossary
    - molecules
    - escalation
    - scheduler
    - Wasteland
    - OTEL data model
    - witness design
    - convoy lifecycle
    - polecat lifecycle
    - plugin system
    - agent provider integration
    - hooks
    - installation

- **Troubleshooting**
  - `gt hooks list` / `gt hooks repair` for connection issues
  - `gt convoy refresh <convoy-id>` for stuck convoys
  - `gt mayor detach` / `gt mayor attach` if the Mayor is unresponsive

### Assessment
This is a **mixed** README/reference document with tutorial elements, oriented around an actively evolving toolchain rather than a timeless concept. **Durability is medium**: the orchestration ideas, git worktree persistence, and multi-agent coordination patterns are fairly durable, but many concrete details are tied to specific tool versions (`Go 1.25+`, `Dolt 1.82.4+`, `beads 0.55.4+`), runtime CLIs, and project-specific terminology that can change. **Content type is mixed** because it combines reference-style terminology, installation instructions, workflows, command examples, monitoring architecture, and product positioning. **Density is high**: the page is packed with named components, commands, version requirements, and system design terms. **Originality is primary source**, since it appears to be the project’s own README describing its architecture and usage. **Reference style is refer-back** rather than deep-study or skim-once; the glossary, commands, and workflow sections are likely the parts you’d return to later. **Scrape quality is good overall**: the README text, command examples, and structure are present, though diagrams are only shown as markdown/mermaid text rather than rendered visuals, and the entry is overview-heavy with links out to many deeper docs.
