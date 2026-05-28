---
url: https://github.com/Dicklesworthstone/frankentui
title: 'Dicklesworthstone/frankentui: Minimal, high-performance terminal UI kernel with diff-based rendering, inline mode, and RAII terminal cleanup'
scraped_at: '2026-04-19T08:34:54Z'
word_count: 12688
raw_file: raw/2026-04-19_dicklesworthstone-frankentui-minimal-high-performance-terminal-ui-kernel-with-di_e6909173.txt
tldr: FrankenTUI is a large, evolving Rust TUI workspace centered on the ftui kernel, with a demo-first workflow, inline scrollback-preserving UI, diff-based rendering, pane workspaces, and in-tree web/WASM support.
key_quote: FrankenTUI is a kernel‑level TUI foundation with a disciplined runtime, diff‑based renderer, and inline‑mode support that preserves scrollback while keeping UI chrome stable.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Jeffrey Emanuel
tools:
- cargo
- git
- curl
- jq
- rg
- python3
libraries:
- crossterm
- tracing-subscriber
companies:
- OpenAI
- Anthropic
tags:
- terminal-ui
- rust
- rendering
- webassembly
- testing
---

### TL;DR
`frankentui` is a large, evolving Rust TUI workspace centered on the `ftui` kernel, with a demo-first workflow (`cargo run -p ftui-demo-showcase`), inline scrollback-preserving UI, diff-based rendering, pane workspaces, and in-tree web/WASM support.

### Key Quote
"FrankenTUI is a kernel‑level TUI foundation with a disciplined runtime, diff‑based renderer, and inline‑mode support that preserves scrollback while keeping UI chrome stable."

### Summary
- GitHub repo: **`Dicklesworthstone/frankentui`**
- Project name: **FrankenTUI (ftui)**
- Repo position: a **minimal/high-performance terminal UI kernel** presented as a Rust workspace, but the README is also highly promotional and makes many large claims that should be treated as self-described rather than independently verified.
- Primary entry point for trying it:  
  - `cargo run -p ftui-demo-showcase`
  - The README explicitly says the **demo showcase is the primary way to see what the system can do**
- Quick-start / install flow:
  - Download source tarball via `curl` or clone with `git`
  - `cargo build` / `cargo build --release`
  - Requires **Rust nightly** according to the README
- Core architecture described by the repo:
  - `ftui-core`: terminal lifecycle, events, capabilities, input parsing, gestures
  - `ftui-render`: buffer, diffing, ANSI presentation
  - `ftui-runtime`: Elm/Bubbletea-style app loop, commands, subscriptions
  - `ftui-layout`: flex/grid plus pane workspace system
  - `ftui-widgets`: widget implementations
  - `ftui-web` and `ftui-showcase-wasm`: in-tree web/WASM support
- Notable design claims in the README:
  - **Inline mode** to keep UI chrome stable while logs scroll above it
  - **Deterministic rendering** with explicit buffer diffing and a “one-writer rule”
  - **RAII cleanup** via `TerminalSession`
  - **Shadow-run validation** for comparing runtime lanes / migrations
  - **Evidence logs** in JSONL for decisions like diff strategy, resizing, and degradation
- Demo / showcase details:
  - The showcase has **46 interactive screens**
  - Categories include dashboard, layout, text, data, input, visual FX, system, diagnostics, workflow, advanced, and 3D/code views
  - Snapshot tests can be updated with `BLESS=1 cargo test -p ftui-demo-showcase`
- Example usage shown in the README:
  - A minimal Rust app implementing `Model`
  - Uses `App::new(...).screen_mode(ScreenMode::Inline { ui_height: 1 }).run()`
  - Example command handling: press `q` to quit
- Workspace/crate inventory:
  - The README lists **20 crates**
  - It says only some crates are on crates.io so far: **`ftui-core`**, **`ftui-layout`**, **`ftui-i18n`**
  - The rest are intended to be used via workspace/path dependencies for now
- Important clarification on web integration:
  - The README distinguishes between **in-tree `ftui-web` + `ftui-showcase-wasm`**
  - and **adjacent/out-of-tree `FrankenTermWeb` / `frankenterm-*` names**, which are referenced in docs/specs but not fully vendored in this checkout
- Behavioral / tooling focus:
  - Many sections discuss deterministic testing, E2E scripts, coverage gates, telemetry, rollout policies, and “doctor_frankentui” verification tooling
  - Commands listed include `cargo test`, `cargo fmt`, `cargo clippy --all-targets -- -D warnings`, and several `scripts/*.sh` E2E scripts
- Documentation pointers:
  - `docs/getting-started.md`
  - `docs/telemetry.md`
  - `docs/operational-playbook.md`
  - `docs/spec/*`, `docs/testing/*`, `docs/WINDOWS.md`
- Contribution policy:
  - The README states the maintainer does **not accept outside contributions for merge**, though issues and illustrative PRs are welcome
- License:
  - The README says **MIT License (with OpenAI/Anthropic Rider)**, but this is part of the project’s own stated licensing and should be checked against the repo’s actual license file if needed

### Assessment
This is a **mixed** source: part reference docs, part tutorial, part architecture manifesto, part marketing copy. Durability is **medium** because many ideas are timeless (inline TUI patterns, diff rendering, RAII cleanup, pane layouts), but the specifics are tied to the project’s current state, nightly Rust, and a fast-changing codebase. Content type is **mixed**, with a heavy tutorial/reference component wrapped in opinionated self-description. Density is **high**: the README is packed with crate names, commands, feature lists, algorithms, and configuration examples, though it is also repetitive and promotional. Originality is mostly **primary source** for the project’s own design claims, but it also reads like **self-commentary** rather than neutral documentation. Reference style is best as **refer-back** for commands, crate names, and architecture orientation; it is not ideal as a deep-study source unless you are specifically evaluating the project’s design claims. Scrape quality is **good** in the sense that the README text is extensive and largely intact, but the source itself is sprawling, highly repetitive, and full of aspirational claims that are not independently verified in the text; images and repository files beyond the README are not part of this capture.
