---
url: https://github.com/uditgoenka/autoresearch
title: 'uditgoenka/autoresearch: Claude Autoresearch Skill — Autonomous goal-directed iteration for Claude Code. Inspired by Karpathy''s autoresearch. Modify → Verify → Keep/Discard → Repeat forever.'
scraped_at: '2026-04-19T08:28:10Z'
word_count: 3610
raw_file: raw/2026-04-19_uditgoenka-autoresearch-claude-autoresearch-skill-autonomous-goal-directed-itera_ca7b7bc1.txt
tldr: 'autresearch is a Claude Code/OpenCode/Codex skill pack that turns an agent into an endless, metric-driven improvement loop: make one change, verify mechanically, keep or revert, and repeat.'
key_quote: Set the GOAL → The agent runs the LOOP → You wake up to results
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Andrej Karpathy
- Udit Goenka
- Anthropic
- OpenCode
- OpenAI
- '@pronskiy'
tools:
- Claude Code
- OpenCode
- OpenAI Codex
- git
libraries: []
companies:
- GitHub
- Anthropic
- OpenCode
- OpenAI
- JetBrains
tags:
- ai-agents
- workflow-automation
- github-repository
- prompt-engineering
- productivity-tools
---

### TL;DR
`autresearch` is a Claude Code/OpenCode/Codex skill pack that turns an agent into an endless, metric-driven improvement loop: make one change, verify mechanically, keep or revert, and repeat.

### Key Quote
"Set the GOAL → The agent runs the LOOP → You wake up to results"

### Summary
- **What it is**
  - A GitHub repository for **Claude Autoresearch Skill**, inspired by **Andrej Karpathy’s `autoresearch`**.
  - Generalizes the original idea from ML experimentation to **any measurable workflow**: code, content, marketing, sales, HR, DevOps, research, and more.
  - Supports **Claude Code, OpenCode, and OpenAI Codex**.

- **Core idea**
  - The system is built around a closed-loop process:
    1. Review current state, git history, and logs
    2. Choose the next change
    3. Make **one focused change**
    4. Commit before verification
    5. Run **mechanical verification** (tests, benchmarks, scores)
    6. Keep if improved, revert if worse, fix or skip if crashed
    7. Log the result
    8. Repeat indefinitely or for `N` iterations
  - Emphasizes:
    - **One metric**
    - **Constrained scope**
    - **Fast verification**
    - **Automatic rollback**
    - **Git as memory**

- **Setup phase**
  - Before looping, Claude is expected to:
    - Read all in-scope files
    - Define or request a **mechanical metric**
    - Define **scope** (modifiable vs read-only files)
    - Establish a baseline using iteration `#0`
    - Confirm setup before starting the loop

- **Critical rules**
  - Loop forever or for a bounded number of iterations
  - Read before writing
  - Only one change per iteration
  - Use mechanical verification only
  - Auto-revert failed changes
  - Prefer simplicity when results are equal
  - Use `git log` and `git diff` before each iteration
  - When stuck, re-read and try harder / broader strategies

- **Command suite**
  - `/autoresearch` — main autonomous optimization loop
  - `/autoresearch:plan` — wizard for goal, scope, metric, and verify command
  - `/autoresearch:security` — STRIDE + OWASP + red-team security audit
  - `/autoresearch:ship` — shipping workflow for code and non-code outputs
  - `/autoresearch:debug` — iterative bug hunting
  - `/autoresearch:fix` — iterative repair loop until errors are gone
  - `/autoresearch:scenario` — scenario/edge-case generator
  - `/autoresearch:predict` — multi-expert pre-analysis
  - `/autoresearch:learn` — autonomous documentation generation/update/check
  - `/autoresearch:reason` — adversarial refinement for subjective decisions

- **Platform-specific install/use**
  - **Claude Code**
    - Recommended via plugin marketplace:
      - `/plugin marketplace add uditgoenka/autoresearch`
      - `/plugin install autoresearch@autoresearch`
    - Also supports manual copy or `./scripts/install.sh --claude --global`
  - **OpenCode**
    - Uses underscore command names like `/autoresearch_debug`
    - Install via `./scripts/install.sh --opencode --global`
  - **Codex**
    - Uses `$autoresearch` mention syntax
    - Install via `./scripts/install.sh --codex --global`

- **Operational details**
  - Results are logged in **TSV** with iteration, commit, metric, delta, status, and description.
  - Every 10 iterations, the agent prints a progress summary.
  - Includes **crash recovery behavior** for syntax errors, runtime errors, resource exhaustion, hangs, and dependency failures.
  - Supports optional **Guard** commands to prevent regressions while optimizing.

- **Repository structure**
  - Canonical Claude implementation lives in `.claude/skills/autoresearch/`
  - OpenCode and Codex versions are generated/adapted into `.opencode/` and `.agents/`
  - Includes installation scripts, sync scripts, guides, a comparison doc, and release automation

- **Important limitations / signals**
  - This is primarily a **workflow/productivity/agent-prompting repo**, not a research paper or software library in the traditional sense.
  - The content is heavily implementation- and platform-specific, so its details may become stale as Claude Code / OpenCode / Codex evolve.
  - The repository notes versioning such as **`v2.0.0-beta.0.2`**, which suggests active iteration and some instability.

### Assessment
Durability is **medium**: the underlying idea of constraint + metric + loop is fairly timeless, but the install commands, platform behavior, and version-specific details are tied to current Claude Code, OpenCode, and Codex tooling. Content type is **mixed**, with a strong bias toward **tutorial/reference** material and some promotional framing. Density is **high** because the README packs in the operating model, command matrix, install instructions, workflow details, and repository layout. Originality is mostly **synthesis**, since it adapts Karpathy’s autoresearch into a broader multi-platform agent workflow rather than presenting novel research. Reference style is **refer-back**: useful when you need the exact commands, workflows, or setup steps later. Scrape quality is **good**: the README content appears largely complete, including command docs, install snippets, FAQ, and repo structure, though any linked guides, images, or external files are not included here.
