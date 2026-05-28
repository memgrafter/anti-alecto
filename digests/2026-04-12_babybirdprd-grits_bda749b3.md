---
url: https://github.com/babybirdprd/grits
title: babybirdprd/grits
scraped_at: '2026-04-12T10:28:57Z'
word_count: 482
raw_file: raw/2026-04-12_babybirdprd-grits_bda749b3.txt
tldr: Grits is a Git-native, local-first issue tracker for humans and AI agents that adds a structured planner/coder workflow, rich context “pulse” data, and append-only execution logs on top of a SQLite + JSONL issue store.
key_quote: “Grits transforms from a passive tracker into an **Active State Store (World Model)** for agents.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- cargo
- git
- grits-cli
- gr
libraries: []
companies:
- GitHub
tags:
- issue-tracking
- local-first
- git-backed
- ai-agents
- cli-tools
---

### TL;DR
Grits is a Git-native, local-first issue tracker for humans and AI agents that adds a structured planner/coder workflow, rich context “pulse” data, and append-only execution logs on top of a SQLite + JSONL issue store.

### Key Quote
“Grits transforms from a passive tracker into an **Active State Store (World Model)** for agents.”

### Summary
- **What it is**
  - A local-first issue tracker built for **AI Agents and humans**.
  - Described as **Git-native**, with issue data versioned in the repo.
  - Current status shown as **v3.0.0 — "Active State Store"**.

- **Core idea: planner/coder separation**
  - Grits explicitly separates work into:
    - **User Intent** (`description`) — the human’s high-level goal
    - **Planner Agent** — researches code and writes the **Implementation Plan** (`design`)
    - **Coder Agent** — executes from the plan and records progress in `notes`
  - The stated purpose is to reduce LLM hallucinations and context drift.

- **Important agent commands**
  - `gr pulse` — emits a full **Rich Context JSON** containing intent, plan, rules, and history.
  - `gr update --append` — appends to `notes` as an execution log / lab notebook.
  - `gr workon` — warns if coding starts without a `design`.

- **Quick start**
  - Prerequisites: **Rust (latest stable)** and **Git**.
  - Install CLI:
    - `cargo install grits-cli`
    - or download a binary from GitHub Releases
  - Initialize in a repo:
    - `cd your-project`
    - `gr onboard`

- **Issue lifecycle / workflow examples**
  - Check current project status with:
    - `gr pulse`
  - Create an issue with intent, design, and immediate work start:
    - `gr create "Fix login bug" --description "intent" --design "plan" --start-work`
  - Link or migrate issues into a hierarchy:
    - `gr dep add gr-child123 gr-parentabc --migrate`
    - Example result: child renamed to `gr-parentabc.n`
  - Assemble context from files when topology is unknown:
    - `gr context assemble --symbols "README.md,src/main.rs"`

- **CLI reference mapping**
  - `description` → **Intent**
  - `design` → **Strategy**
  - `acceptance_criteria` → **Proof**
  - `notes` → **Memory**
  - Commands highlighted:
    - `gr show <id>` — full context + execution log
    - `gr update --append` — append-only notebook behavior
    - `gr pulse` — hydration JSON
    - `gr context assemble` — fallback blind assembly

- **Architecture**
  - Uses a **Twin Engine**:
    - **SQLite** at `.grits/grits.db` for fast local queries
    - **JSONL** at `.grits/issues.jsonl` as the Git-versioned source of truth
  - Includes **Graph-Lite**:
    - lightweight AST parsing for dependency graphs
    - supports **Blind Assembly** when file topology isn’t available

- **Docs and related files**
  - Mentions planner/coder skill files:
    - `.agent/skills/grits-plan/SKILL.md`
    - `.agent/skills/grits-code/SKILL.md`
  - Mentions workflows in:
    - `.agent/workflows/`
  - Says it follows the **Agent Skills** open specification.

- **License**
  - MIT

### Assessment
This is a **mixed** technical/reference-style project README with tutorial elements. Durability is **medium**: the general idea of local-first, Git-backed issue tracking and agent-oriented workflows should age well, but the specific CLI commands, version tags (**v3.0.0**, **v3.2.0**), and implementation details are version-sensitive. Density is **high**, with many named commands, file paths, and conceptual mappings packed into a short document. Originality is **primary source** since it appears to be the project’s own README and product framing rather than commentary. It is best used as a **refer-back** reference if you are evaluating the tool or trying to recall its workflow model. Scrape quality is **good**: the main README content is present, including commands, architecture notes, and links, though repository-linked subfiles themselves were not expanded here.
