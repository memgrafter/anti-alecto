---
url: https://github.com/jdx/pitchfork
title: 'jdx/pitchfork: Daemons with DX'
scraped_at: '2026-04-19T06:55:06Z'
word_count: 559
raw_file: raw/2026-04-19_jdx-pitchfork-daemons-with-dx_8a2a0ef7.txt
tldr: Pitchfork is a developer-focused daemon manager/CLI for starting, supervising, auto-restarting, and auto-stopping background services, with readiness checks, dependencies, cron jobs, UI tools, and AI assistant integration.
key_quote: Daemons with DX
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: skim-once
scrape_quality: good
people:
- jdx
tools:
- pitchfork
- mise
- cargo
- Docker
- Kubernetes
libraries: []
companies:
- Claude
- Cursor
tags:
- daemon-management
- developer-tools
- cli
- background-jobs
- devops
---

### TL;DR
Pitchfork is a developer-focused daemon manager/CLI for starting, supervising, auto-restarting, and auto-stopping background services, with readiness checks, dependencies, cron jobs, UI tools, and AI assistant integration.

### Key Quote
“**Daemons with DX**”

### Summary
- **What it is**
  - Pitchfork is a CLI for managing daemons with a focus on developer experience.
  - It is presented as a project by `jdx` with docs at `pitchfork.jdx.dev`.

- **Core capabilities**
  - **Start services once** so they aren’t duplicated if already running.
  - **Auto start/stop** daemons when entering or leaving a project directory via shell hooks.
  - **Ready checks** supported:
    - time delay
    - output regex
    - HTTP endpoint
    - TCP port
    - custom command
  - **Dependency management**
    - topological startup ordering
    - parallel execution
  - **File watching**
    - auto-restart daemons when source files change
  - **Cron scheduling**
    - recurring tasks with configurable retrigger modes
  - **Lifecycle hooks**
    - commands on ready, fail, retry, stop, and exit
  - **Resource limits**
    - CPU and memory limits per daemon
  - **Interfaces**
    - interactive TUI dashboard
    - browser-based web UI
  - **MCP server**
    - exposes daemon management to AI assistants like Claude and Cursor
  - **Container mode**
    - can run as PID 1 with zombie reaping and signal forwarding

- **Use cases**
  - Development services like web APIs and databases
  - Directory sync tasks such as `rsync` or `unison`
  - General background process management for projects
  - Container entrypoints for Docker/Kubernetes

- **Installation**
  - Recommended: `mise use -g pitchfork`
  - Alternative: `cargo install pitchfork-cli`
  - Also available via GitHub releases

- **Quickstart examples**
  - One-off background process:
    - `pitchfork run docs -- npm start docs-dev-server`
  - Project config via `pitchfork.toml`:
    - define daemons under `[daemons.<name>]`
    - example daemons: `redis`, `api`, `docs`
  - Start all or some daemons in parallel:
    - `pitchfork start --all`
    - `pitchfork start redis api`

- **Shell integration**
  - Bash: `eval "$(pitchfork activate bash)"`
  - Zsh: `eval "$(pitchfork activate zsh)"`
  - Fish: `pitchfork activate fish | source`
  - Example daemon config for shell-triggered behavior:
    - `auto = ["start", "stop"]`

- **Logging**
  - Logs can be viewed with:
    - `pitchfork logs api`
  - Log storage path shown as:
    - `~/.local/state/pitchfork/logs`

- **Example project configuration**
  - Demonstrates a full dev stack:
    - `postgres` via Docker on port `5432`
    - `redis` on port `6379`
    - `api` depending on `postgres` and `redis`, with `ready_output = "listening on"`
    - `worker` depending on the same services
    - `sync` task using `rsync` on a cron schedule of `0 */5 * * * *` (every 5 minutes)
  - Uses `ready_delay`, `depends`, `auto`, and `cron` settings to coordinate startup and recurring jobs.

- **Documentation pointers**
  - Quick start, full docs, and CLI reference are linked prominently.
  - The README is mostly an overview and onboarding page rather than a deep technical reference.

### Assessment
This is a **mixed** content type, leaning toward a **tool/reference** README with tutorial elements. Durability is **medium**: the general daemon-management concepts are stable, but installation commands, CLI behavior, UI/MCP features, and the linked docs/release paths may change with versions. Density is **medium**: it packs a lot of feature coverage and practical examples into a short README, but does not deeply explain implementation details. Originality is mainly **primary source** since it describes the project itself, not an external synthesis. It is best used as **skim-once** for orientation or **refer-back** for install/usage snippets and feature recall. Scrape quality is **good**: the main README content, examples, and code snippets are present, though linked documentation pages, screenshots, and contributor image assets are not included here.
