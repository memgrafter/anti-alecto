---
url: https://github.com/coctostan/pi-superpowers
title: coctostan/pi-superpowers
scraped_at: '2026-04-19T07:25:28Z'
word_count: 620
raw_file: raw/2026-04-19_coctostan-pi-superpowers_0b7efd1b.txt
tldr: pi-superpowers is a pi-compatible package of structured coding-agent workflow skills—brainstorming through finishing—that adds process guides, plan tracking, and optional subagent-based workflows.
key_quote: Brainstorming → Planning → TDD → Debugging → Code Review → Finishing — as composable skills your coding agent loads on demand.
durability: high
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Jesse Vincent
tools:
- pi
- vitest
- plan_tracker
libraries: []
companies:
- GitHub
tags:
- coding-agents
- workflow-automation
- test-driven-development
- developer-tools
- software-documentation
---

### TL;DR
`pi-superpowers` is a pi-compatible package of structured coding-agent workflow skills—brainstorming through finishing—that adds process guides, plan tracking, and optional subagent-based workflows.

### Key Quote
“Brainstorming → Planning → TDD → Debugging → Code Review → Finishing — as composable skills your coding agent loads on demand.”

### Summary
- **What it is**
  - A GitHub repository for `pi-superpowers`, described as “Structured workflow skills for [pi](https://github.com/badlogic/pi-mono), adapted from [Superpowers](https://github.com/obra/superpowers) by Jesse Vincent.”
  - Intended for coding agents that load specific process skills on demand.

- **Installation**
  - Via CLI:
    - `pi install git:github.com/coctostan/pi-superpowers`
  - Or configure it in:
    - project-level `.pi/settings.json`
    - global `~/.pi/agent/settings.json`
  - Example JSON:
    - `"packages": ["git:github.com/coctostan/pi-superpowers"]`

- **Optional subagent support**
  - Some skills marked with 🤖 can dispatch work to subagents.
  - The repo itself **does not include a subagent tool**.
  - Those skills still work manually without automation.
  - Options to enable automated dispatch:
    - pi’s example subagent extension in `examples/extensions/subagent/`
    - Any compatible extension exposing a `subagent` tool
    - Manual parallelism using `pi -p "prompt"` in another terminal or tmux panes

- **Skills included**
  - **brainstorming** — Socratic design refinement, alternatives, incremental validation
  - **writing-plans** — implementation plans with bite-sized TDD tasks
  - **executing-plans** — batch execution with checkpoints for architect review
  - **subagent-driven-development** 🤖 — fresh subagent per task with two-stage review
  - **test-driven-development** — RED-GREEN-REFACTOR cycle and anti-patterns
  - **systematic-debugging** — 4-phase root-cause investigation
  - **verification-before-completion** — “evidence before claims”
  - **requesting-code-review** 🤖 — pre-merge review with severity categories
  - **receiving-code-review** — evaluating review feedback technically
  - **dispatching-parallel-agents** 🤖 — concurrent subagent workflows
  - **using-git-worktrees** — isolated development branches
  - **finishing-a-development-branch** — merge/PR decision workflow
  - **writing-skills** 🤖 — apply TDD to process documentation itself

- **Plan tracker**
  - Introduces a `plan_tracker` tool that replaces file-based task tracking.
  - State is stored in the session and shown in the TUI.
  - Example status display:
    - `Tasks: ✓✓→○○ (2/5)  Task 3: Recovery modes`
  - Supported actions:
    - `init` with task list
    - `update` status by index
    - `status`
    - `clear`

- **Workflow structure**
  - The repo defines a recommended development flow:
    1. Brainstorm
    2. Isolate with git worktrees
    3. Plan into small TDD tasks
    4. Execute via plans or subagents
    5. Verify before claiming completion
    6. Review with code review
    7. Finish by merging or opening a PR
  - Each skill cross-references related skills so the agent can move through the workflow coherently.

- **Development and testing**
  - Uses **vitest**.
  - Tests live in `tests/`:
    - `tests/extension/plan-tracker.test.ts` for plan-tracker core logic
    - `tests/skills/skill-validation.test.ts` for validating all skills and cross-references
  - Test commands:
    - `npm test`
    - `npm run test:watch`
  - Skill validation checks:
    - valid `SKILL.md` frontmatter (`name`, `description`)
    - directory/name conventions
    - valid `/skill:name` cross-references
    - existence of referenced files
    - correct `package.json` wiring for `pi.skills` and `pi.extensions`

- **Attribution and license**
  - Skill content is adapted from Jesse Vincent’s **Superpowers** project.
  - Licensed under **MIT**.

### Assessment
This is a **reference/tool** repo with a **high-durability** core idea, though some installation and extension details are naturally tied to the current `pi` ecosystem. It’s a **mixed** content type: mostly documentation plus a lightweight announcement of capabilities. The page is fairly **dense** with specific skill names, commands, file paths, and test behaviors, making it useful as a quick reference and for deciding whether to install or inspect the package further. Originality is mainly **synthesis/adaptation** rather than primary invention, since it explicitly builds on Jesse Vincent’s Superpowers workflow. Best used as **refer-back** documentation rather than deep study unless you plan to extend or validate the package. Scrape quality appears **good**: the main README structure, install instructions, skill list, workflow, tests, and licensing info are all present; no obvious code blocks or sections seem missing beyond the banner image.
