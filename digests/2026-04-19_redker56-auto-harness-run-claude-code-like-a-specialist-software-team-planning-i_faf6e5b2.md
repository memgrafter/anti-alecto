---
url: https://github.com/redker56/auto-harness
title: 'redker56/auto-harness: Run Claude Code like a specialist software team: planning, implementation, QA, fix/retest loops, and durable .harness state for long-running project delivery.'
scraped_at: '2026-04-19T07:56:45Z'
word_count: 1436
raw_file: raw/2026-04-19_redker56-auto-harness-run-claude-code-like-a-specialist-software-team-planning-i_faf6e5b2.txt
tldr: Auto-Harness is a Claude Code plugin that turns a single product brief into a durable, multi-stage software delivery workflow with separate planning, build, QA, fix/retest, and final-review agents backed by `.harness/` state files.
key_quote: Run Claude Code like a small, specialized software team instead of a single endless chat.
durability: medium
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Claude Code
- Playwright MCP
- Node.js
libraries:
- '@playwright/mcp'
companies:
- Anthropic
tags:
- claude-code
- software-workflow
- plugin
- project-management
- qa-testing
---

### TL;DR
Auto-Harness is a Claude Code plugin that turns a single product brief into a durable, multi-stage software delivery workflow with separate planning, build, QA, fix/retest, and final-review agents backed by `.harness/` state files.

### Key Quote
"Run Claude Code like a small, specialized software team instead of a single endless chat."

### Summary
- **What it is**
  - A Claude Code plugin called **Auto-Harness**.
  - It is based on Anthropic’s article **“Harness design for long-running application development.”**
  - Its purpose is to manage long-running project work through a structured workflow rather than relying on one continuous chat thread.

- **Core idea**
  - The system uses a durable **`Planner -> Generator -> Evaluator`** workflow.
  - It stores persistent project state in **`.harness/`** so work can survive restarts, compaction, and handoff.
  - The plugin aims to make Claude Code behave like a small software team with specialized roles.

- **Problems it claims to solve**
  - Long tasks fail when planning, implementation, and QA happen in one thread.
  - Multi-day work needs durable state, not just conversation history.
  - Fix loops lose direction if they don’t preserve the original contract and QA findings.
  - Serious delivery work benefits from a visible trail of specs, contracts, QA reports, fix logs, and checkpoints.

- **Best use cases**
  - Multi-sprint feature delivery in Claude Code.
  - Work that benefits from strict separation between **Planner**, **Generator**, and **Evaluator** roles.
  - Projects where QA and retesting should be part of the normal process.
  - Situations where inspectable and resumable `.harness/` artifacts matter.

- **Not recommended for**
  - Small one-off edits.
  - Fast exploratory spikes where workflow overhead would be unnecessary.

- **Workflow**
  - The README shows a typical flow:
    - User brief
    - Orchestrator
    - `planner-clarify-agent`
    - `planner-spec-draft-agent`
    - `generator-draft-contract-agent`
    - `evaluator-review-contract-agent`
    - `generator-build-sprint-agent`
    - `evaluator-write-qa-agent` → `qa-report-reviewer-agent`
    - If QA fails: `generator-apply-fixes-agent` → `evaluator-write-retest-agent` → `retest-report-reviewer-agent`
    - `evaluator-write-final-agent` → `final-report-reviewer-agent`
  - The user stays in chat, while durable logs live in `.harness/*.md`.

- **Quick start / installation**
  - Prerequisites:
    - Claude Code installed and authenticated
    - Node.js on `PATH`
    - A target project directory where `.harness/` can be created
    - Playwright MCP support if browser QA is desired
  - Install steps:
    1. Open Claude Code in the target project.
    2. Add the repository as a marketplace:
       - `/plugin marketplace add redker56/auto-harness`
    3. Install the plugin:
       - `/plugin install auto-harness@auto-harness-marketplace`
    4. Restart Claude Code.
    5. Run:
       - `/auto-harness:harness <your product brief or clarification reply>`

- **Commands**
  - `/auto-harness:harness <brief-or-reply>`: main end-to-end command; also handles clarifications, spec approval, and resume.
  - `/auto-harness:plan <brief-or-clarification-answers>`: planning mode; can create intake, ask questions, draft spec, and design direction.
  - `/auto-harness:build [XX]`: advances generator-side work; auto-selects the current legal generator action.
  - `/auto-harness:qa [XX]`: advances evaluator-side work; auto-selects the current legal evaluator action.

- **Runtime model**
  - The **Orchestrator** is the main thread.
  - It reads state from `.harness/`, chooses the next phase, dispatches subagents, and updates `.harness/status.md` and checkpoints when needed.
  - It may edit normal project files, but role-owned `.harness/` artifacts are meant to be handled by the corresponding subagents.
  - It talks directly to the user when clarification or approval is required.
  - The Orchestrator does **not** draft the spec or make QA decisions.

- **Subagents**
  - The plugin defines many focused agents, including:
    - `planner-clarify-agent`
    - `planner-spec-draft-agent`
    - `generator-draft-contract-agent`
    - `generator-build-sprint-agent`
    - `generator-apply-fixes-agent`
    - `evaluator-review-contract-agent`
    - `evaluator-write-qa-agent`
    - `evaluator-write-retest-agent`
    - `evaluator-write-final-agent`
    - reviewer agents for QA, retest, and final reports
  - Writer agents preload one internal skill and use current `.harness/` state.
  - Reviewer agents audit reports against templates and rubrics.

- **`.harness/` artifact contract**
  - The README defines a structured file layout for persistent project state:
    - `intake.md`
    - `spec.md`
    - `design-direction.md`
    - `status.md`
    - `runtime.md`
    - `checkpoints/latest.md`
    - sprint contract/review files
    - QA, fix log, retest, and final report files
  - Each file has an explicit owner and purpose.
  - `status.md` is the machine-readable source of truth, with example fields like:
    - `phase: CONTRACTING`
    - `current_sprint: 1`
    - `total_sprints: 3`
    - `pending_action: evaluator_review`
    - `last_agent: generator`
    - `approval_required: false`

- **Repository layout**
  - The README lists the main repo structure:
    - `.claude-plugin/`
    - `agents/`
    - `commands/`
    - `hooks/`
    - `scripts/`
    - `skills/`
    - `.mcp.json`
    - `LICENSE`
    - `README.md`
    - `README.zh-CN.md`

- **Hooks and enforcement**
  - The plugin uses hooks for lifecycle management and enforcement:
    - `SessionStart`: resumes from `.harness/status.md` and checkpoint excerpts
    - `PreCompact`: refreshes `.harness/checkpoints/latest.md`
    - `PreToolUse`: protects `.harness/` boundaries using state and legal-action rules
    - `SubagentStart` / `SubagentStop`: track active subagents
  - Completion checks are enforced with:
    - `node "${CLAUDE_PLUGIN_ROOT}/scripts/action-check.mjs"` for planner/generator/contract-review outputs
    - explicit reviewer agents for QA, retest, and final reports
  - The orchestrator only advances state after checks succeed.

- **Playwright MCP**
  - The plugin ships a `.mcp.json` that starts Playwright via:
    - `npx -y @playwright/mcp@latest`
  - Planner and Generator are meant to stay away from browser-driven MCP work.
  - Evaluator gets browser QA access.
  - Evaluator can also use runtime helpers for health checks.

- **Helper scripts**
  - State helpers:
    - `node "${CLAUDE_PLUGIN_ROOT}/scripts/harness-runtime.mjs" get`
    - `node "${CLAUDE_PLUGIN_ROOT}/scripts/harness-runtime.mjs" healthcheck`
  - Action validation helpers for planner/generator/evaluator steps are also documented.

### Assessment
This is a **tutorial/reference** for a plugin system rather than a conceptual essay, and its durability is **medium** because the workflow ideas are fairly stable but the exact commands, file layout, and Claude Code/plugin behavior are tied to current tooling and could change. The content is **dense** and fairly complete for setup and runtime understanding, with lots of specific file names, commands, agent names, and lifecycle rules. It appears to be **primary source** documentation from the project itself, not a synthesis. Best used as a **refer-back** reference when installing, operating, or debugging the plugin rather than a deep-study text. Scrape quality looks **good**: the README structure, command examples, artifact tree, hooks, and scripts are all captured, though any behavior hidden in linked files or code is not included here.
