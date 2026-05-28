---
url: https://github.com/davebcn87/pi-autoresearch/tree/62feb2f46ef2a1b8e39af381b47acc4d7af42ca8
title: davebcn87/pi-autoresearch at 62feb2f46ef2a1b8e39af381b47acc4d7af42ca8
scraped_at: '2026-04-19T08:28:38Z'
word_count: 1496
raw_file: raw/2026-04-19_davebcn87-pi-autoresearch-at-62feb2f46ef2a1b8e39af381b47acc4d7af42ca8_1705cc27.txt
tldr: 'pi-autoresearch is a pi extension and skill that turns an AI coding agent into an autonomous optimization loop: benchmark changes, keep improvements, revert regressions, and persist the whole experiment history across restarts.'
key_quote: Try an idea, measure it, keep what works, discard what doesn't, repeat forever.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Davebcn87
- Karpathy
tools:
- pi
- autoresearch.jsonl
- autoresearch.md
- autoresearch.sh
- autoresearch.checks.sh
libraries: []
companies:
- GitHub
- pi.dev
tags:
- ai-coding
- automation
- benchmarking
- developer-tools
- optimization
---

### TL;DR
`pi-autoresearch` is a `pi` extension and skill that turns an AI coding agent into an autonomous optimization loop: benchmark changes, keep improvements, revert regressions, and persist the whole experiment history across restarts.

### Key Quote
“Try an idea, measure it, keep what works, discard what doesn't, repeat forever.”

### Summary
- **What it is**
  - A GitHub project titled **“pi-autoresearch”** for **pi**, an AI coding agent that runs in the terminal.
  - Its purpose is to run **autonomous research/optimization loops** on a target metric such as test speed, bundle size, model training loss, build time, or Lighthouse score.
  - It is **inspired by karpathy/autoresearch**.

- **Core workflow**
  - The agent iterates through: **edit → commit → run_experiment → log_experiment → keep or revert → repeat**.
  - The loop is designed to continue indefinitely until interrupted.
  - Experiment history is stored in **`autoresearch.jsonl`**, so sessions can survive restarts and context resets.

- **What’s included**
  - An **extension** with tools, live widget, and a `/autoresearch` dashboard.
  - A **skill** that helps gather the optimization target, writes session files, and starts the loop.

- **Extension tools**
  - `init_experiment`: one-time setup for session name, metric, unit, and direction.
  - `run_experiment`: runs a command, measures wall-clock duration, and captures output.
  - `log_experiment`: records results, auto-commits, and updates the widget/dashboard.

- **`/autoresearch` command behavior**
  - `/autoresearch <text>`: enters autoresearch mode; resumes from `autoresearch.md` if present, otherwise creates a new session.
  - `/autoresearch off`: leaves autoresearch mode while keeping `autoresearch.jsonl`.
  - `/autoresearch clear`: deletes `autoresearch.jsonl`, resets state, and turns mode off.

- **Skills**
  - `autoresearch-create`
    - Asks about the goal, command, metric, and file scope, or infers them.
    - Creates `autoresearch.md` and `autoresearch.sh`, then starts the loop.
  - `autoresearch-finalize`
    - Turns a noisy branch into clean, independent branches by grouping kept experiments into logical changesets from the merge-base.

- **Session files**
  - `autoresearch.md`: living session document with objective, metric, scope, tried ideas, dead ends, and wins.
  - `autoresearch.sh`: benchmark script that runs the workload and emits `METRIC name=number`.
  - `autoresearch.checks.sh` (optional): backpressure checks for tests/types/lint that run after passing benchmarks.

- **UI and controls**
  - A status widget is always visible above the editor.
  - `Ctrl+X` toggles expanded inline dashboard view.
  - `Ctrl+Shift+X` opens a fullscreen scrollable dashboard overlay.
  - The widget shows:
    - number of runs
    - number kept
    - total metric change
    - confidence score

- **Confidence scoring**
  - After 3+ runs, it computes a **confidence score** using **Median Absolute Deviation (MAD)** to estimate noise.
  - Formula: `|best_improvement| / MAD`
  - Interpreted as:
    - `≥ 2.0×`: likely real improvement
    - `1.0–2.0×`: above noise but marginal
    - `< 1.0×`: likely within noise
  - This is advisory only; it does not automatically discard results.

- **Backpressure checks**
  - If `autoresearch.checks.sh` exists, it runs after each successful benchmark.
  - If checks fail, the run is logged as `checks_failed`, no commit is made, and the changes are reverted.
  - Checks use a separate timeout and do not affect the primary metric.

- **Configuration**
  - Optional `autoresearch.config.json` can set:
    - `workingDir`: directory where autoresearch operates
    - `maxIterations`: maximum number of experiments before auto-stopping

- **Install and usage**
  - Quick install: `pi install https://github.com/davebcn87/pi-autoresearch`
  - Manual install copies extension and skill folders into `~/.pi/agent/`.
  - Typical use:
    - `/skill:autoresearch-create`
    - let the loop run
    - `/skill:autoresearch-finalize` to split results into reviewable branches

- **Examples and target domains**
  - Test speed: `pnpm test`
  - Bundle size: `pnpm build && du -sb dist`
  - LLM training: `uv run train.py`
  - Build speed: `pnpm build`
  - Lighthouse: `lighthouse http://localhost:3000 --output=json`

- **Cost controls**
  - Recommends capping usage via provider budget limits and `maxIterations`.

- **License**
  - MIT

### Assessment
This is a **mixed reference/tutorial** project page with fairly high density and practical specificity: it explains the product, installation, commands, file formats, UI behavior, and the autonomous loop in enough detail to re-use later. Durability is **medium** because it is tied to the `pi` tool, its extension/skill architecture, and the current repository state, though the general pattern of autonomous benchmark-driven optimization is longer-lived. The content is mostly **primary-source documentation** with some promotional framing; it appears trustworthy for intended usage but should be checked against the actual repo code for implementation details. Reference style is **refer-back**: useful when setting up or operating the tool again. Scrape quality is **good** overall: the README content is present and structured, though the rendered image/dashboard visuals themselves are not inspectable from the text alone.
