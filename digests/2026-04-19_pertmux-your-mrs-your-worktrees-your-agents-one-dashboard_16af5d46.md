---
url: https://pertmux.dev/
title: pertmux - Your MRs. Your worktrees. Your agents. One dashboard.
scraped_at: '2026-04-19T07:44:09Z'
word_count: 459
raw_file: raw/2026-04-19_pertmux-your-mrs-your-worktrees-your-agents-one-dashboard_16af5d46.txt
tldr: pertmux is a Rust terminal dashboard that unifies GitHub/GitLab merge requests, local worktrees, tmux sessions, and AI coding agents into one workflow-centric TUI.
key_quote: Your MRs. Your worktrees. Your agents. One dashboard.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- pertmux
- tmux
- neovim
- opencode
- claude
libraries: []
companies:
- GitHub
- GitLab
tags:
- developer-tools
- terminal-ui
- git-workflows
- ai-agents
- worktrees
---

### TL;DR
pertmux is a Rust terminal dashboard that unifies GitHub/GitLab merge requests, local worktrees, tmux sessions, and AI coding agents into one workflow-centric TUI.

### Key Quote
“Your MRs. Your worktrees. Your agents. One dashboard.”

### Summary
- **What it is**
  - A **Rust TUI** for managing development workflow context in one place.
  - Connects **GitHub/GitLab merge requests** to:
    - local branches
    - worktrees
    - tmux panes/sessions
    - AI coding agents
  - Installable with:
    - `cargo install pertmux`

- **Main features**
  - **Multi-Forge**
    - Supports **GitHub + GitLab** behind one interface.
    - Shows pipeline dots, comments, and unread indicators.
  - **Worktree Management**
    - Create, remove, and merge worktrees without leaving the dashboard.
    - Powered by **worktrunk**.
  - **Agent Monitoring**
    - Tracks **Claude** and **opencode** instances across tmux panes.
    - Displays status, tokens, and todos.
  - **Notifications**
    - A daemon polls for MR updates.
    - Updated status is shown when you refocus.
  - **Multi-Project**
    - Includes a fuzzy finder for quick project switching.
    - Overview panel shows MR counts.
  - **Daemon Architecture**
    - A background daemon keeps data fresh.
    - The TUI connects instantly via a **Unix socket**.

- **Why the author built it**
  - Built to fit the author’s own workflow around **neovim, tmux, and opencode**.
  - Motivation came from juggling:
    - multiple worktrees
    - multiple MR dashboards
    - multiple tmux sessions
    - idle AI agents
    - missed chances to rebase or fix issues while focused on other work
  - The author sees the age of AI agents as a reason to better manage “meta-maintenance” work in one dashboard.
  - Emphasizes that this is **personal workflow software**, not a generic one-size-fits-all tool.

- **Customizability / audience**
  - The author explicitly says the tool was built for personal use first.
  - Generic flexibility was an afterthought.
  - Readers are encouraged to:
    - **fork and modify** it for their own workflows
    - use it as inspiration for building their own tools
  - Mentions an **`agents.md`** file for onboarding and customization.

- **Quick start**
  - Install:
    - `cargo install pertmux`
  - Configure:
    - `~/.config/pertmux.toml`
    - Example project block:
      - `name = "My App"`
      - `source = "github"`
      - `local_path = "~/repos/my-app"`
  - Run:
    - `pertmux serve` to start the background daemon
    - `pertmux connect` to open the TUI

### Assessment
This is a **mixed** announcement/tool page with a strong personal-editorial component: it introduces a specific utility, explains the motivation behind it, and gives a short setup example. Durability is **medium** because the workflow pattern (MRs + worktrees + tmux + agents) is broadly relevant, but the exact integrations with **Claude**, **opencode**, **GitHub/GitLab**, and the daemon/TUI architecture may evolve with versions. Density is **medium**: it’s concise but includes concrete commands, config keys, and feature lists. Originality is primarily **primary source** since it’s the author’s own project page and rationale. It’s best as a **refer-back** reference if you’re evaluating whether the tool fits an agent-heavy terminal workflow. Scrape quality appears **good**: the page content, feature descriptions, motivation, and install/run instructions are all present, with no obvious missing code blocks or sections beyond the brief config snippet.
