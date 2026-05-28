---
url: https://github.com/peteromallet/desloppify
title: 'peteromallet/desloppify: Agent harness to make your slop code well-engineered and beautiful.'
scraped_at: '2026-04-19T07:54:10Z'
word_count: 1106
raw_file: raw/2026-04-19_peteromallet-desloppify-agent-harness-to-make-your-slop-code-well-engineered-and_c8e35b54.txt
tldr: Desloppify is a Python 3.11+ agent harness that scans a codebase for mechanical and LLM-detected quality issues, prioritizes them into an execution queue, and iteratively drives fixes until the project’s score improves.
key_quote: “Your goal is to get the strict score as high as possible. The scoring resists gaming — the only way to improve it is to actually make the code better.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Peter O'Mallet
tools:
- desloppify
libraries: []
companies:
- GitHub
- PyPI
tags:
- code-quality
- developer-tools
- ai-agents
- static-analysis
- software-maintenance
---

### TL;DR
Desloppify is a Python 3.11+ agent harness that scans a codebase for mechanical and LLM-detected quality issues, prioritizes them into an execution queue, and iteratively drives fixes until the project’s score improves.

### Key Quote
“Your goal is to get the strict score as high as possible. The scoring resists gaming — the only way to improve it is to actually make the code better.”

### Summary
- **What it is**
  - A GitHub project and PyPI package called **desloppify**.
  - Described as an “agent harness to make your codebase 🤌” and “make your slop code well-engineered and beautiful.”
  - Targets AI coding agents and human users who want to improve codebase quality systematically.

- **Core idea**
  - Combines two kinds of evaluation:
    - **Mechanical detection**: dead code, duplication, complexity, test coverage gaps, naming issues, and similar static/code-quality problems.
    - **Subjective LLM review**: naming, abstractions, error handling patterns, module boundaries, and broader design quality.
  - Produces a **scorecard** and a prioritized fix loop so the agent can keep improving the codebase across multiple sessions.

- **Workflow**
  - Main pipeline shown as:
    - `scan → score → review → triage → execute → rescan`
  - Key commands and actions:
    - `pip install --upgrade "desloppify[full]"`
    - `desloppify update-skill claude` (with options for `claude`, `cursor`, `codex`, `copilot`, `droid`, `windsurf`, `gemini`)
    - Add `.desloppify/` to `.gitignore`
    - Exclude irrelevant directories with `desloppify exclude <path>`
    - `desloppify scan --path .`
    - `desloppify next`
    - Use `desloppify backlog` for broader open work
    - Use `plan` / `plan queue` to reorder priorities or cluster issues
  - The intended loop is:
    - run `next`
    - fix the issue
    - resolve it
    - run `next` again
    - repeat
  - The README stresses that **`next` is the execution queue from the living plan**, not the entire backlog.

- **State and scoring**
  - State persists in **`.desloppify/`**, so progress survives across sessions.
  - The scoring is explicitly designed to **resist gaming**:
    - won’tfix items widen the gap between lenient and strict scores
    - re-reviewing can lower scores if new issues are found
  - The author claims a score above **98** should correlate with a codebase a seasoned engineer would call beautiful.

- **Language support**
  - Claims support for **29 languages**.
  - Full plugin depth for:
    - TypeScript
    - Python
    - C#
    - C++
    - Dart
    - GDScript
    - Go
    - Rust
  - Generic linter + tree-sitter support for:
    - Ruby
    - Java
    - Kotlin
    - and 18 more
  - For **C++**, `compile_commands.json` is the primary analysis path.
  - For **Makefile** repos, it falls back to best-effort local include scanning.

- **Monorepo guidance**
  - If a workspace has multiple unrelated projects, they should be scanned separately using `--path`.
  - Example given:
    - `desloppify --lang typescript scan --path ./frontend`
    - `desloppify --lang python scan --path ./backend`
  - Scanning the parent directory of multiple projects is warned against because it mixes state and path context.

- **Author’s argument / positioning**
  - Frames the tool as moving from **“Vibe Coding to Vibe Engineering.”**
  - The thesis is that LLMs can help not just build quickly, but also maintain and improve quality when guided by a framework that evaluates codebases holistically.
  - Emphasizes that the project aims to define a score worth optimizing, not a vanity metric or something easily gamed.

- **Use and licensing**
  - Free for any individual to use for their own work.
  - Free for open source companies to use in any capacity, including commercial.
  - Non-open-source companies should check the LICENSE for commercial pricing details.
  - Invites issues, improvements, PRs, and community participation via Discord.

### Assessment
This is a **mixed** reference/announcement/tool page with a strong promotional and instructional component. Durability is **medium**: the conceptual framing around agent-assisted code quality is fairly durable, but the exact commands, supported languages, package extras, and workflow details are version- and project-specific, so they may change. Content density is **high**, with a lot of operational detail packed into the README, including commands, workflow semantics, and language support. Originality is primarily a **primary source** for the project’s own design and positioning, not a synthesis. It is best used as **refer-back** documentation if you plan to adopt the tool, especially for setup and workflow reminders. Scrape quality is **good**: the main README content, commands, and descriptive sections appear captured, though embedded images are referenced rather than viewable here.
