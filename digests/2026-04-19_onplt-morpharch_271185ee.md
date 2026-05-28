---
url: https://github.com/onplt/morpharch?tab=readme-ov-file
title: onplt/MorphArch
scraped_at: '2026-04-19T07:16:46Z'
word_count: 1943
raw_file: raw/2026-04-19_onplt-morpharch_271185ee.txt
tldr: MorphArch is a Rust CLI/TUI tool that scans Git history and source dependencies to surface repository architecture health, drift, hotspots, and blast radius from the terminal.
key_quote: Inspect repository structure, drift, and hotspots from the terminal.
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
- morpharch
- openai
- ollama
- docker
libraries: []
companies:
- GitHub
- OpenAI
tags:
- rust
- cli-tools
- codebase-analysis
- monorepos
- software-architecture
---

### TL;DR
MorphArch is a Rust CLI/TUI tool that scans Git history and source dependencies to surface repository architecture health, drift, hotspots, and blast radius from the terminal.

### Key Quote
"Inspect repository structure, drift, and hotspots from the terminal."

### Summary
- **What it is**
  - A terminal-based architecture analysis tool for large codebases and monorepos.
  - The README positions it as a repeatable inspection workflow rather than a one-off graph viewer.
  - Supports **Rust, TypeScript, JavaScript, Python, and Go** out of the box.

- **Core capabilities**
  - Scans **Git history** and extracts dependency edges from source code.
  - Computes an architectural **health score from 0 to 100**.
  - Highlights **drift**, **hotspots**, **cycles**, **layering issues**, **hub/god modules**, **coupling**, **cognitive debt**, and **instability debt**.
  - Includes **blast radius analysis** for likely downstream impact of risky modules.
  - Provides an **AI architecture assistant** that answers natural-language questions using repository architecture data.

- **Why it claims to be different**
  - Uses **grouped-by-default** cluster maps instead of raw graphs for large repos.
  - Is **Git-native**: scans history, not just `HEAD`, and replays changes in the TUI.
  - Uses **language-aware parsing** with safe fast paths plus AST fallback, rather than regex-only extraction.
  - Designed for **triage, inspection, drift review, and debugging** inside the terminal.
  - Highly configurable via `morpharch.toml`.

- **Supported repo layouts**
  - Works well with **Nx**, **Turborepo**, **pnpm workspaces**, **Cargo workspaces**, and other monorepo patterns.

- **Installation options**
  - `cargo install morpharch`
  - Linux/macOS install script via `curl ... | sh`
  - Windows PowerShell install script via `irm ... | iex`
  - Also available via:
    - `cargo-binstall`
    - Homebrew
    - npm global install
    - Scoop
    - AUR
    - Docker
    - Build from source with `cargo build --release`

- **Quick start commands**
  - `morpharch watch .` — scan repo and open the TUI
  - `morpharch analyze --path .` — static report for `HEAD`
  - `morpharch list-drift --path .` — historical drift table
  - `morpharch list-graphs --path .` — cached graph frames
  - For first-time exploration of large repos: `morpharch watch . -n 150 -s 200`

- **TUI mental model**
  - Start at **Map**: cluster-level repo view
  - Drill into **Cluster details**
  - Then into **Inspect** for a focused module view
  - Insights panel shows:
    - **Overview**
    - **Hotspots**
    - **Blast**

- **Commands documented**
  - `scan <path>`: scan repo history and store results in a repo-scoped SQLite cache
    - `-n, --max-commits <N>` limits scan depth
    - history traversal is **first-parent only**
    - repeated scans reuse cache when repo/config are unchanged
  - `watch <path>`: scan and launch TUI
    - `-s, --max-snapshots <N>` limits timeline snapshots
  - `analyze [commit]`: detailed report for a commit
  - `list-drift`: recent health drift and graph deltas
  - `list-graphs`: stored graph frames

- **Navigation and interaction**
  - Global keyboard model:
    - `Tab` / `Shift+Tab` focus panels
    - `j/k` or arrows move selection
    - `h/l` or `[ ]` switch subviews/tabs
    - `Enter` drill in
    - `Esc` drill out
  - Other shortcuts:
    - `1-4` jump to major panels
    - `/` filter
    - `c` reset graph viewport
    - `r` reheat raw graph layout
    - `x` toggle blast overlay
    - `a` toggle AI panel
    - `q` quit
  - Mouse support includes clicking clusters, dragging graph/timeline, and scrolling to zoom.

- **Configuration**
  - Uses `morpharch.toml` for analysis and presentation tuning.
  - Config sections shown:
    - `[ignore]`
    - `[scan]`
    - `[scoring.weights]`
    - `[scoring.thresholds]`
    - `[[scoring.boundaries]]`
    - `[scoring.exemptions]`
    - `[clustering]`
    - `[clustering.semantic]`
    - `[clustering.structural]`
    - `[[clustering.families]]`
    - `[[clustering.rules]]`
    - `[[clustering.constraints]]`
    - `[clustering.presentation]`
  - Notable knobs:
    - ignore presets and custom presets
    - package depth
    - minimum importers for external deps
    - test path patterns
    - scoring weights and thresholds
    - explicit boundary rules
    - semantic families and clustering constraints
    - presentation aliases, kinds, and color mode

- **Scan heuristics**
  - Python relative imports are resolved as internal dependencies.
  - Default test-path filtering is intentionally narrow; `examples/`, `bench/`, and `mocks/` are not excluded unless configured.
  - Setting `scan.external_min_importers = 0` keeps all third-party deps visible.

- **AI architecture assistant**
  - Enabled with `a` in the TUI.
  - Uses `OPENAI_API_KEY` by default and `gpt-4o-mini`.
  - Can be configured for other providers such as **Ollama** through `[ai]`.
  - Can answer questions about:
    - health scores and drift
    - module instability and fan-in/fan-out
    - blast scores and god-module flags
    - cluster membership and layer topology
    - cycle groups and boundary violations
    - churn hotspots and bus-factor risks
    - commit-to-commit diffs
  - Slash commands include `/help`, `/model`, `/diff N`, `/clear`, `/history`, `/export`.

- **Health scoring**
  - Score ranges:
    - `90-100` Clean
    - `70-89` Healthy
    - `40-69` Warning
    - `0-39` Critical
  - Built from six debts:
    - cycle
    - layering
    - hub/god module
    - coupling
    - cognitive
    - instability

- **Docs and repo links**
  - Website and docs are hosted at **morpharch.dev**
  - Docs source lives under `website/docs`
  - Landing page source is `website/src/pages/index.tsx`

- **Contributing and license**
  - Standard Rust checks: `cargo fmt`, `cargo test`, `cargo clippy -- -D warnings`
  - Website checks: `npm install`, `npm run typecheck`, `npm run build`
  - Licensed under **Apache-2.0 OR MIT**

### Assessment
This is a **mixed** reference/announcement-style README with fairly high information density and lots of implementation-specific detail, especially around CLI commands, configuration, and TUI behavior. Its durability is **medium**: the architectural concepts are fairly timeless, but installation methods, default models, and command behavior may change with releases. The content appears to be **primary source** documentation for the project rather than a synthesis, and it is best used as a **refer-back** reference rather than a deep-study piece unless you are adopting the tool. Scrape quality looks **good**: the main README sections, commands, config examples, and feature descriptions are present, though images and linked docs are not embedded here.
