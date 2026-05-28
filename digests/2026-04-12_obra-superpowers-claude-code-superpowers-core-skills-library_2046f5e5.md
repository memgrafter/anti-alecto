---
url: https://github.com/obra/superpowers
title: 'obra/superpowers: Claude Code superpowers: core skills library'
scraped_at: '2026-04-12T09:39:52Z'
word_count: 915
raw_file: raw/2026-04-12_obra-superpowers-claude-code-superpowers-core-skills-library_2046f5e5.txt
tldr: Superpowers is a plugin-based workflow system for coding agents that enforces structured brainstorming, planning, TDD, code review, and subagent-driven execution across tools like Claude Code, Cursor, Codex, OpenCode, Copilot CLI, and Gemini CLI.
key_quote: Mandatory workflows, not suggestions.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Jesse Vincent
tools:
- Claude Code
- Cursor
- Codex
- OpenCode
- GitHub Copilot CLI
- Gemini CLI
libraries: []
companies:
- Prime Radiant
tags:
- coding-agents
- test-driven-development
- workflow-automation
- developer-tools
- plugin-system
---

### TL;DR
Superpowers is a plugin-based workflow system for coding agents that enforces structured brainstorming, planning, TDD, code review, and subagent-driven execution across tools like Claude Code, Cursor, Codex, OpenCode, Copilot CLI, and Gemini CLI.

### Key Quote
"Mandatory workflows, not suggestions."

### Summary
- **What it is**
  - An open-source repository called **obra/superpowers**.
  - Described as a “complete software development workflow for your coding agents,” built from composable **skills** plus initial instructions.
  - Goal: make coding agents behave more like disciplined engineers and less like free-form code generators.

- **Core workflow**
  - When a user starts a task, the agent should **ask clarifying questions first** instead of immediately writing code.
  - It then helps turn the conversation into a **spec**, showing it in digestible chunks for approval.
  - After approval, it creates an implementation plan suitable for a junior engineer, emphasizing:
    - **red/green TDD**
    - **YAGNI**
    - **DRY**
  - Once authorized, it proceeds with **subagent-driven development**, where agents handle tasks, review each other’s work, and continue iterating.
  - The repo claims Claude can work autonomously for **a couple hours at a time** without drifting from the plan.

- **Installation and platform support**
  - Notes that installation differs by platform:
    - **Claude Code** and **Cursor** have built-in plugin marketplaces.
    - **Codex** and **OpenCode** require manual setup.
  - Installation paths include:
    - Claude Code official marketplace:
      - `plugin install superpowers@claude-plugins-official`
    - Claude Code via marketplace add:
      - `plugin marketplace add obra/superpowers-marketplace`
      - then `plugin install superpowers@superpowers-marketplace`
    - Cursor:
      - `/add-plugin superpowers`
    - Codex:
      - fetch instructions from `.codex/INSTALL.md`
    - OpenCode:
      - fetch instructions from `.opencode/INSTALL.md`
    - GitHub Copilot CLI:
      - `copilot plugin marketplace add obra/superpowers-marketplace`
      - `copilot plugin install superpowers@superpowers-marketplace`
    - Gemini CLI:
      - `gemini extensions install https://github.com/obra/superpowers`
      - update with `gemini extensions update superpowers`
  - Verification advice: start a new session and ask for something that should trigger a skill, such as planning a feature or debugging an issue.

- **Basic workflow / skills**
  - The repo highlights a canonical sequence of skills:
    1. **brainstorming** — refine ideas and write a design doc
    2. **using-git-worktrees** — create isolated workspace after design approval
    3. **writing-plans** — break work into 2–5 minute tasks with file paths and verification steps
    4. **subagent-driven-development** or **executing-plans** — dispatch subagents or execute in batches with checkpoints
    5. **test-driven-development** — enforce RED-GREEN-REFACTOR and delete pre-test code
    6. **requesting-code-review** — review between tasks; critical issues block progress
    7. **finishing-a-development-branch** — verify tests and decide merge/PR/keep/discard
  - It explicitly says the agent checks for relevant skills **before any task** and that these are **mandatory workflows**.

- **Skills library**
  - **Testing**
    - `test-driven-development`
  - **Debugging**
    - `systematic-debugging`
    - `verification-before-completion`
  - **Collaboration**
    - `brainstorming`
    - `writing-plans`
    - `executing-plans`
    - `dispatching-parallel-agents`
    - `requesting-code-review`
    - `receiving-code-review`
    - `using-git-worktrees`
    - `finishing-a-development-branch`
    - `subagent-driven-development`
  - **Meta**
    - `writing-skills`
    - `using-superpowers`

- **Philosophy**
  - The project’s operating principles are:
    - **Test-Driven Development** — tests first, always
    - **Systematic over ad-hoc** — process over guessing
    - **Complexity reduction** — simplicity first
    - **Evidence over claims** — verify before declaring success
  - It links to a blog post: **“Superpowers for Claude Code”**.

- **Contributing and maintenance**
  - Skills live directly in the repository.
  - To contribute:
    1. fork
    2. create a branch
    3. follow `writing-skills`
    4. submit a PR
  - Updates are automatic when the plugin is updated:
    - `plugin update superpowers`

- **Project metadata**
  - **License**: MIT
  - **Community/support**:
    - Discord
    - GitHub Issues
    - Release announcements signup
  - Built by **Jesse Vincent** and contributors at **Prime Radiant**.

### Assessment
This is a **reference/tutorial/mixed** repository meant to be used as a workflow system for coding agents, not a narrative article. Its **durability is medium**: the underlying practices (TDD, planning, review, worktrees) are fairly timeless, but the installation commands, supported platforms, marketplace names, and references to specific tools/versions will age as Claude Code, Cursor, Codex, OpenCode, and Gemini CLI evolve. The **density is high** because it includes concrete workflow stages, skill names, commands, and operational rules, though parts are promotional. The content is mostly **primary source** documentation from the project itself. It’s best used as a **refer-back** resource when installing, configuring, or following the Superpowers workflow. **Scrape quality is good**: the main README content appears present, including installation commands, workflow descriptions, philosophy, contribution notes, and community links; no obvious code blocks or major sections seem missing from the provided text.
