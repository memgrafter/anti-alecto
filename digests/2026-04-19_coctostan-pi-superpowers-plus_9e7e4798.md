---
url: https://github.com/coctostan/pi-superpowers-plus
title: coctostan/pi-superpowers-plus
scraped_at: '2026-04-19T07:25:38Z'
word_count: 2681
raw_file: raw/2026-04-19_coctostan-pi-superpowers-plus_9e7e4798.txt
tldr: 'pi-superpowers-plus is a pi package that upgrades the original workflow-skill system with runtime enforcement: TDD/debug/verification warnings, workflow-phase tracking, a subagent tool, and a plan tracker.'
key_quote: Your coding agent doesn't just know the rules - it follows them.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Jesse Vincent
tools:
- pi
- git
- gh
- subagent
- plan_tracker
- workflow_reference
libraries: []
companies:
- pi
- Superpowers
tags:
- code-assistant
- workflow-automation
- test-driven-development
- git-workflow
- developer-tools
---

### TL;DR
`pi-superpowers-plus` is a `pi` package that upgrades the original workflow-skill system with runtime enforcement: TDD/debug/verification warnings, workflow-phase tracking, a subagent tool, and a plan tracker.

### Key Quote
“Your coding agent doesn't just know the rules - it follows them.”

### Summary
- `pi-superpowers-plus` is a GitHub project/package for the `pi` coding agent (`https://github.com/badlogic/pi-mono`) that combines:
  - **12 workflow skills** for structured development
  - **3 extensions** that enforce process rules during runtime
- The package is meant to make the agent behave more consistently:
  - skills teach **what** to do
  - extensions enforce it **while working**
- Core runtime behaviors after install:
  - warns when source code is written without a failing test
  - gates `git commit`, `git push`, and `gh pr create` until tests pass
  - restricts writes to `docs/plans/` during Brainstorm/Plan phases
  - shows the current git branch or detached HEAD on first tool output in a repo
  - warns on first write/edit to confirm correct branch/worktree
- Installation is simple and automatic:
  - `pi install npm:pi-superpowers-plus`
  - or `pi install git:github.com/coctostan/pi-superpowers-plus`
  - or add `"npm:pi-superpowers-plus"` to `.pi/settings.json` or `~/.pi/agent/config.json`
- The README frames it as a **drop-in upgrade** from `pi-superpowers`:
  - same skill names and workflow
  - adds active enforcement, more explicit TDD guidance, workflow tracking, and plan tooling
- Workflow structure:
  - **Brainstorm → Plan → Execute → Verify → Review → Finish**
  - each phase maps to a specific skill like `/skill:brainstorming`, `/skill:writing-plans`, `/skill:executing-plans`, etc.
- Supporting skills are used as needed:
  - `test-driven-development`
  - `systematic-debugging`
  - `using-git-worktrees`
  - `dispatching-parallel-agents`
  - `receiving-code-review`
- The main extension is **Workflow Monitor**, which:
  - watches tool calls/results
  - tracks TDD state: **RED → GREEN → REFACTOR**
  - escalates debug warnings after **2 consecutive failing test runs**
  - warns on shipping commands without passing tests
  - tracks workflow phase and prompts at boundaries
  - exposes a `workflow_reference` tool for on-demand guidance topics like TDD rationalizations and debugging techniques
- **Plan Tracker** provides:
  - a `plan_tracker` tool for task lists
  - TUI progress display
- **Subagent** support adds a `subagent` tool and bundled agents:
  - `implementer`
  - `worker`
  - `code-reviewer`
  - `spec-reviewer`
  - results include structured fields like `filesChanged`, `testsRan`, and `status`
- The README also includes:
  - a comparison table against original Superpowers / `pi-superpowers`
  - architecture tree showing skills, extensions, agents, and tests
  - development/testing commands
  - attribution to Jesse Vincent’s Superpowers and the MIT license

### Assessment
This is a **reference / project README** with some announcement-style positioning and a lot of implementation detail. Durability is **medium-high**: the general workflow concepts are durable, but package names, install commands, feature lists, and counts like “12 skills,” “3 extensions,” and “373 tests” are version-specific and may change. Content density is **high** because it packs installation, workflow design, runtime behavior, architecture, and comparison tables into one README. Originality is mostly **primary source** for this package’s own design and behavior, though it is also clearly a **port + extension** of prior work from Superpowers and `pi-superpowers`. Reference style is **refer-back**: useful for checking install/configuration, workflow phases, extension behavior, and migration details later. Scrape quality is **good**: the main README content appears intact, including tables, code blocks, and architecture notes, though linked files like `docs/oversight-model.md`, `ROADMAP.md`, and the actual source code are not included here.
