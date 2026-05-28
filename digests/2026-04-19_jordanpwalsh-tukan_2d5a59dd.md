---
url: https://github.com/jordanpwalsh/tukan
title: jordanpwalsh/tukan
scraped_at: '2026-04-19T07:43:00Z'
word_count: 726
raw_file: raw/2026-04-19_jordanpwalsh-tukan_2d5a59dd.txt
tldr: Tukan is a tmux-based kanban task manager that automatically moves cards between In Progress and Review based on pane activity, with both a TUI and CLI for managing tasks, windows, and optional git worktrees.
key_quote: Tukan watches your tmux panes for output changes every few seconds.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- jordanpwalsh
tools:
- tmux
- Node.js
- Ink
- vitest
- tsx
libraries: []
companies: []
tags:
- task-management
- tmux
- kanban
- cli-tools
- developer-tools
---

### TL;DR
Tukan is a tmux-based kanban task manager that automatically moves cards between In Progress and Review based on pane activity, with both a TUI and CLI for managing tasks, windows, and optional git worktrees.

### Key Quote
"Tukan watches your tmux panes for output changes every few seconds."

### Summary
- **What it is**
  - Tukan is a kanban-style task manager that runs inside **tmux**.
  - It represents work as cards on a board and can launch tmux windows from cards.
  - It auto-tracks what you’re actively working on by monitoring pane activity.

- **Core workflow**
  - Board pipeline: **Todo → In Progress → Review → Done**
  - When a card in **In Progress** goes idle for **30 seconds**, Tukan automatically promotes it to **Review**.
  - If activity resumes in a **Review** card’s window, it is demoted back to **In Progress**.
  - The goal is to avoid manual card shuffling and keep the board aligned with real activity.

- **Installation**
  - Requires **Node.js v18+** and **tmux**.
  - Install globally with:
    - `npm install -g tukan`
  - Run inside a tmux session with:
    - `tukan`
  - Cards are stored in `.tukan.cards` in the project directory.
  - Runtime state is stored in `~/.config/tukan/`.

- **Developer setup**
  - Clone and install:
    - `git clone https://github.com/jordanpwalsh/tukan.git`
    - `cd tukan`
    - `npm install`
  - Run from source:
    - `npx tsx src/index.tsx`
  - Tests:
    - `npx vitest`
    - `npx vitest run`
  - Build:
    - `npm run build`
  - Build compiles TypeScript to `dist/` and patches the version.

- **Usage**
  - Default mode is a **TUI** inside tmux:
    - `tukan`
  - CLI subcommands include:
    - `tukan add "Fix login bug"` — create a Todo card
    - `tukan start <card>` — start a card and create a tmux window
    - `tukan stop <card>` — kill the window and mark the card closed
    - `tukan resolve <card>` — move card to Done
    - `tukan edit <card>` — edit card content
    - `tukan move <card> <session>` — move card to another session
    - `tukan show <card>` — show card details, with `--json` supported
    - `tukan peek <card>` — show current pane content
    - `tukan send <card> <text>` — send keystrokes to the pane
    - `tukan list` — list cards, with `--column`, `--all`, and `--json`
    - `tukan sessions` — list sessions
    - `tukan refresh` — sync activity state
    - `tukan register [path]` — register a project directory
    - `tukan migrate` — migrate centralized storage to project-local storage
  - Most commands accept `-s <session>` to target a specific session.

- **Keyboard controls**
  - Arrow keys navigate columns/cards.
  - `h` / `l` move cards between columns.
  - `s` starts or restarts a card.
  - `Enter` switches to the window or confirms start.
  - `n` creates a new card.
  - `e` edits a card.
  - `r` resolves a card to Done.
  - `q` quits.

- **Pane interaction features**
  - Tukan can inspect or interact with a card’s tmux pane from the CLI.
  - Useful for prompts or agent workflows.
  - Examples:
    - `tukan peek <card>` — print full pane content
    - `tukan peek <card> -n 5` — last 5 non-blank lines
    - `tukan send <card> y` — send `y` and Enter
    - `tukan send <card> --no-enter n` — send text without Enter

- **Card status indicators**
  - Blank: unstarted card, no window
  - `○`: has tmux window, idle
  - `●`: active window
  - `◆`: recent activity
  - `◇`: closed after being started

- **Worktree support**
  - Cards can optionally create a **git worktree** when started.
  - Starting a worktree-enabled card creates a sibling directory and branch.
  - Resolving the card merges the worktree back and cleans up.
  - Example flow:
    - `tukan add "feature-x" --worktree`
    - `tukan start feature-x`
    - `tukan resolve feature-x`

- **Architecture**
  - Uses a **functional core, imperative shell** design.
  - Pure board logic is separated from IO concerns like tmux IPC, rendering, and persistence.
  - The TUI is built with **Ink** (React for CLIs).
  - It uses the **tmux CLI** directly; no tmux plugin is required.

### Assessment
This is a high-density reference/documentation page for a specific developer tool, with high durability at the conceptual level but medium staleness risk because installation, commands, and Node/tmux requirements can change over time. The content type is mixed, but mostly tutorial/reference, since it combines product overview, install instructions, command usage, keybindings, and architecture notes. It appears to be the primary project README rather than commentary or synthesis, so it’s likely trustworthy for the project’s intended behavior. Use it as a refer-back reference when deciding whether to adopt the tool or looking up command syntax. Scrape quality is good overall: the main sections, code blocks, tables, and command examples are present, though any screenshots/images are not meaningfully captured beyond the alt text.
