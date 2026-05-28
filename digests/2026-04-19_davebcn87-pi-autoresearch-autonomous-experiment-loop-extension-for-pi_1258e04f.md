---
url: https://github.com/davebcn87/pi-autoresearch
title: 'davebcn87/pi-autoresearch: Autonomous experiment loop extension for pi'
scraped_at: '2026-04-19T07:39:06Z'
word_count: 1528
raw_file: raw/2026-04-19_davebcn87-pi-autoresearch-autonomous-experiment-loop-extension-for-pi_1258e04f.txt
tldr: pi-autoresearch is a pi extension and paired skill that turns an AI coding agent into an autonomous optimize/measure/keep-or-revert loop for experiments like test speed, bundle size, build time, or ML training.
key_quote: “Try an idea, measure it, keep what works, discard what doesn't, repeat forever.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- davebcn87
- karpathy
tools:
- pi
- lighthouse
- pnpm
- uv
libraries: []
companies:
- GitHub
tags:
- autonomous-experiments
- ai-coding-agent
- performance-optimization
- developer-tools
- terminal-workflows
---

### TL;DR
`pi-autoresearch` is a `pi` extension and paired skill that turns an AI coding agent into an autonomous optimize/measure/keep-or-revert loop for experiments like test speed, bundle size, build time, or ML training.

### Key Quote
“Try an idea, measure it, keep what works, discard what doesn't, repeat forever.”

### Summary
- **What it is**
  - A GitHub project by `davebcn87` named **`pi-autoresearch`**.
  - It extends **[pi](https://pi.dev/)**, an AI coding agent that runs in the terminal.
  - The goal is to automate iterative experimentation: change code, run a benchmark, decide whether to keep the change, and repeat.

- **Core idea**
  - Inspired by **karpathy/autoresearch**.
  - Meant for **any optimization target**, including:
    - test runtime
    - bundle size
    - LLM training metrics
    - build time
    - Lighthouse performance scores
  - Separates:
    - a **global extension** (tools, widget, dashboard)
    - a **domain-specific skill** (what to optimize, how to benchmark, which files are in scope)

- **Quick start / install**
  - Install with:
    ```bash
    pi install https://github.com/davebcn87/pi-autoresearch
    ```
  - Manual install copies:
    - `extensions/pi-autoresearch` to `~/.pi/agent/extensions/`
    - `skills/autoresearch-create` to `~/.pi/agent/skills/`
  - Then run `/reload` in pi.

- **What’s included**
  - **Extension**
    - tools
    - live widget
    - `/autoresearch` dashboard
  - **Skill**
    - asks or infers the optimization goal
    - writes session files
    - starts the loop

- **Extension tools**
  - `init_experiment`
    - one-time setup for session name, metric, unit, and direction
  - `run_experiment`
    - runs a command
    - measures wall-clock time
    - captures output
  - `log_experiment`
    - stores the result
    - auto-commits
    - updates widget and dashboard

- **`/autoresearch` commands**
  - `/autoresearch <text>`
    - enter autoresearch mode
    - if `autoresearch.md` exists, resume using `<text>` as context
    - otherwise create a new session
  - `/autoresearch off`
    - stop auto-resume and clear runtime state
    - keeps `autoresearch.jsonl`
  - `/autoresearch clear`
    - delete `autoresearch.jsonl`
    - reset all state
    - turn autoresearch mode off
  - `/autoresearch export`
    - open a live browser dashboard that auto-updates

- **Keyboard shortcuts**
  - `Ctrl+X`
    - toggle dashboard expand/collapse
  - `Ctrl+Shift+X`
    - open fullscreen scrollable dashboard overlay
    - supports navigation with `↑/↓`, `j/k`, `PageUp/PageDown`, `u/d`, `g/G`, and closes with `Escape` or `q`

- **UI behavior**
  - A persistent status widget sits above the editor and shows:
    - number of runs
    - number kept
    - total metric change
    - confidence score
  - Confidence is shown after **3+ runs**
    - `≥ 2.0×` = likely real improvement
    - `1.0–2.0×` = marginal
    - `< 1.0×` = likely noise
  - Expanded dashboard shows a table with commit, metric, status, and description.
  - Fullscreen overlay shows live progress and elapsed time.

- **Skills provided**
  - `autoresearch-create`
    - asks about goal, command, metric, and scope
    - creates:
      - `autoresearch.md`
      - `autoresearch.sh`
    - then starts the loop immediately
  - `autoresearch-finalize`
    - takes a noisy autoresearch branch
    - groups kept experiments into logical changes
    - creates independent branches from the merge-base
    - each branch should be reviewable and mergeable independently

- **Session files**
  - `autoresearch.md`
    - objective
    - metrics
    - files in scope
    - tried ideas
  - `autoresearch.sh`
    - benchmark script
    - pre-checks
    - workload execution
    - outputs `METRIC name=number`
  - `autoresearch.checks.sh` *(optional)*
    - correctness/backpressure checks
    - runs after each passing benchmark
    - failures block keeping the change

- **How the loop works**
  - Repeated cycle:
    - edit
    - commit
    - `run_experiment`
    - `log_experiment`
    - keep or revert
    - repeat
  - Results are appended to `autoresearch.jsonl`, one line per run.
  - This design is meant to:
    - survive restarts
    - survive context resets
    - remain human-readable
    - support branch-aware sessions

- **Example domains**
  - Test speed: `pnpm test`
  - Bundle size: `pnpm build && du -sb dist`
  - LLM training: `uv run train.py`
  - Build speed: `pnpm build`
  - Lighthouse: `lighthouse http://localhost:3000 --output=json`

- **Configuration**
  - Optional `autoresearch.config.json` in the pi session directory.
  - Supported fields:
    - `workingDir`
      - overrides directory for file I/O, command execution, and git
    - `maxIterations`
      - caps how many experiments the agent will run
  - Config can help control scope and cost.

- **Confidence scoring**
  - Uses **Median Absolute Deviation (MAD)** to estimate noise.
  - Computes confidence as:
    - `|best_improvement| / MAD`
  - The score is advisory only:
    - it does **not** auto-discard results
    - it helps decide whether to re-run noisy experiments
  - Stored in `autoresearch.jsonl` and shown in the UI.

- **Backpressure checks**
  - Optional `autoresearch.checks.sh` runs tests/types/lint after passing benchmark runs.
  - If checks fail:
    - experiment is logged as `checks_failed`
    - change is reverted
    - no commit is kept
  - Checks have a separate timeout, default **300s**.

- **Prerequisites and cost control**
  - Requires:
    - pi installed
    - an API key for an LLM provider configured in pi
  - Cost controls:
    - provider-side API budgets
    - `maxIterations` in config

- **License**
  - MIT

### Assessment
This is a **tutorial/reference** project page with fairly high information density and lots of implementation detail, especially around commands, file names, UI behavior, and session workflow. Its durability is **medium**: the general autonomous optimization-loop pattern is durable, but the instructions are tied to the current `pi` extension/skill system and could change with pi versions. The content is a mix of **tool documentation** and **product-style announcement**, and it reads like a **primary source** for the project’s own features. It’s best used as a **refer-back** reference if you plan to install or operate the extension, rather than a one-time skim. Scrape quality is **good**: the README content appears largely intact, including tables, commands, configuration, and code blocks, with no obvious missing major sections.
