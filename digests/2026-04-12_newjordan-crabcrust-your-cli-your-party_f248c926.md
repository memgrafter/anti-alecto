---
url: https://github.com/newjordan/CrabCrust
title: 'newjordan/CrabCrust: Your CLI - Your Party'
scraped_at: '2026-04-12T06:50:25Z'
word_count: 369
raw_file: raw/2026-04-12_newjordan-crabcrust-your-cli-your-party_f248c926.txt
tldr: CrabCrust is an experimental Rust CLI toolkit that wraps shell commands (especially Git) to add braille-rendered terminal animations during execution, aiming to improve real-time feedback while preserving original command behavior and exit codes.
key_quote: '"CrabCrust treats the terminal as an interface surface, not just a text stream."'
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- git
- cargo
- rust
libraries: []
companies:
- GitHub
tags:
- rust-cli
- terminal-ui
- developer-tooling
- git-workflows
- command-feedback
---

### TL;DR
CrabCrust is an experimental Rust CLI toolkit that wraps shell commands (especially Git) to add braille-rendered terminal animations during execution, aiming to improve real-time feedback while preserving original command behavior and exit codes.

### Key Quote
> "CrabCrust treats the terminal as an interface surface, not just a text stream."

### Summary
- **What it is**
  - **CrabCrust** is a Rust project for adding expressive, terminal-native animation to CLI workflows.
  - Focuses on pairing command execution with visual feedback (motion/progress/success cues) directly in the shell.

- **Core motivation**
  - Typical CLI tools report results after completion.
  - CrabCrust explores a more interaction-designed model: showing intent and state *during* command execution.

- **Main features**
  - **Braille-based rendering** for high-density terminal graphics.
  - **Procedural animations** for states/actions like save, push, pull, download, merge, and celebratory outcomes.
  - **Command wrappers** that connect shell commands to themed visual responses.
  - **Modular Rust architecture** separating rendering and animation layers.
  - **Experimental media conversion pipeline** for GIF/video-driven playback in terminal form.
  - **Demo mode** to run animations without wrapping real commands.

- **How it works (pipeline)**
  1. Wrapper intercepts command (e.g., `git push`, `git commit`).
  2. Executor runs underlying command, preserving stdout/stderr and exit code.
  3. Animation engine selects/runs a procedural animation in parallel.
  4. Braille renderer outputs dense colored terminal graphics.
  5. Control returns to shell with original command result intact.

- **Getting started / commands**
  - Prereqs: Rust toolchain + Cargo.
  - Build/run:
    - `git clone https://github.com/newjordan/CrabCrust.git`
    - `cd CrabCrust`
    - `cargo build --release`
    - `cargo run -- demo all`
  - Git wrapper examples:
    - `cargo run -- git commit -m "Prototype CLI feedback"`
    - `cargo run -- git push`
  - Optional alias:
    - `alias git="crabcrust git"`

- **Assets and docs**
  - Demo video in repo: `examples/crabcrust_in_action.mp4`
  - Additional animation/media experiments under `examples/` and `docs/`.

- **Stated future directions**
  - Expand wrappers beyond Git (build/deploy/agent workflows).
  - Add configurable mapping from command outcomes to animations.
  - Better failure/warning/long-task operator cues.
  - Investigate accessibility and legibility for terminal motion design.

### Assessment
This is primarily a **tool/project README** with a mix of **reference + light tutorial** content. **Durability: medium** — the design ideas (terminal as interface surface, feedback affordances) are fairly lasting, but usage details and capabilities may change quickly as an “intentionally experimental” project evolves. **Density: medium** — concise but specific about architecture and commands. **Originality: primary source** — authored as first-party project description. **Reference style: refer-back** — useful to revisit for setup commands, conceptual model, and feature scope. **Scrape quality: good/partial** — text sections are intact and include commands and structure; video is referenced but its content isn’t transcribed, so visual examples are only indirectly captured.
