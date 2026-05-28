---
url: https://github.com/rtk-ai/rtk
title: 'rtk-ai/rtk: CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies'
scraped_at: '2026-04-19T08:39:28Z'
word_count: 2680
raw_file: raw/2026-04-19_rtk-ai-rtk-cli-proxy-that-reduces-llm-token-consumption-by-60-90-on-common-dev-c_7366ec38.txt
tldr: RTK is a Rust-based CLI proxy for AI coding tools that rewrites and compresses command output to cut LLM token usage by roughly 60–90% on common developer workflows.
key_quote: “High-performance CLI proxy that reduces LLM token consumption by 60-90%”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Patrick Szymkowiak
- Florian Bruniaux
- Adrien Eppling
tools:
- Homebrew
- Claude Code
- Copilot
- Gemini CLI
- Codex
- Cursor
- Windsurf
- Cline
- Kilo Code
- Google Antigravity
libraries: []
companies:
- GitHub
- OpenAI
- Google
- Microsoft
- Discord
tags:
- cli-tooling
- llm-integration
- developer-productivity
- rust
- token-optimization
---

### TL;DR
RTK is a Rust-based CLI proxy for AI coding tools that rewrites and compresses command output to cut LLM token usage by roughly 60–90% on common developer workflows.

### Key Quote
“High-performance CLI proxy that reduces LLM token consumption by 60-90%”

### Summary
- **What it is**
  - `rtk` (“Rust Token Killer”) is a **single Rust binary** with **zero dependencies**.
  - It sits between shell commands and an LLM context, **filtering/compressing command output before the model sees it**.
  - Claims **100+ supported commands** and **<10ms overhead**.

- **Core value proposition**
  - Reduces token usage for routine developer commands by **60–90%**.
  - The README gives an estimated **30-minute Claude Code session** example where total output drops from about **118,000 tokens** to **23,900 tokens** (**~80% savings**).
  - Savings examples include:
    - `ls` / `tree`: 2,000 → 400 tokens
    - `git status`: 3,000 → 600
    - `cargo test`: 25,000 → 2,500
    - `pytest`: 8,000 → 800
    - `git add/commit/push`: 1,600 → 120

- **How it works**
  - RTK applies four main transformations:
    - **Smart filtering**: removes noise like comments, whitespace, boilerplate
    - **Grouping**: combines similar items
    - **Truncation**: keeps relevant context, cuts redundancy
    - **Deduplication**: collapses repeated log lines with counts
  - The README shows the concept as rewriting commands like `git status` to `rtk git status`, so the AI sees a compacted result.

- **Installation**
  - Recommended via **Homebrew**:
    - `brew install rtk`
  - Linux/macOS quick install:
    - `curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh`
  - Cargo install:
    - `cargo install --git https://github.com/rtk-ai/rtk`
  - Prebuilt binaries are available for **macOS, Linux, and Windows** from GitHub releases.
  - The README includes a **version check** example showing `rtk 0.28.2`.

- **Quick start / integration**
  - Initialize hooks for AI tools with commands like:
    - `rtk init -g` for Claude Code / Copilot
    - `rtk init -g --gemini`
    - `rtk init -g --codex`
    - `rtk init -g --agent cursor`
    - `rtk init --agent windsurf`
    - `rtk init --agent cline`
    - `rtk init --agent kilocode`
    - `rtk init --agent antigravity`
  - After setup, shell commands are transparently rewritten, but the README warns that **Claude Code built-in tools** like `Read`, `Grep`, and `Glob` do **not** pass through the Bash hook.

- **Supported command categories**
  - **Files**: `rtk ls`, `rtk read`, `rtk smart`, `rtk find`, `rtk grep`, `rtk diff`
  - **Git**: `rtk git status`, `rtk git log`, `rtk git diff`, `rtk git add/commit/push/pull`
  - **GitHub CLI**: `rtk gh pr list/view`, `rtk gh issue list`, `rtk gh run list`
  - **Test runners**: `rtk jest`, `rtk vitest`, `rtk pytest`, `rtk go test`, `rtk cargo test`, `rtk rspec`, `rtk test <cmd>`
  - **Build/lint**: `rtk lint`, `rtk tsc`, `rtk next build`, `rtk cargo build`, `rtk ruff check`, `rtk golangci-lint run`, etc.
  - **Package managers**, **AWS**, **containers**, and **data/analytics** commands are also supported.

- **Auto-rewrite hook**
  - The “most effective way” to use RTK is the **auto-rewrite hook**.
  - It intercepts Bash tool calls and rewrites them to RTK equivalents.
  - The README claims this enables “100% rtk adoption across all conversations and subagents, zero token overhead.”
  - On **native Windows**, the hook is limited and falls back to **CLAUDE.md injection mode**; **WSL** is recommended for full support.

- **Analytics / telemetry**
  - RTK includes usage analytics like `rtk gain`, `rtk discover`, and `rtk session`.
  - Telemetry is described as:
    - **anonymous**
    - **aggregate**
    - **opt-in**
    - collected **once per day**
  - It tracks things like command counts, tokens saved, adoption, and top passthrough commands.
  - It explicitly says it does **not** collect source code, file paths, command arguments, secrets, environment variables, personal data, or repository contents.

- **Configuration and exit**
  - Config file lives at:
    - `~/.config/rtk/config.toml`
    - macOS: `~/Library/Application Support/rtk/config.toml`
  - Example config options include excluding commands from rewrite and controlling tee behavior.
  - Uninstall options are documented via `rtk init -g --uninstall`, `cargo uninstall rtk`, or `brew uninstall rtk`.

- **Docs and project metadata**
  - The repo links to a separate website guide, install docs, architecture, contributing, and security docs.
  - It is **MIT licensed**.
  - Core team listed:
    - Patrick Szymkowiak — Founder
    - Florian Bruniaux — Core contributor
    - Adrien Eppling — Core contributor

### Assessment
This is a **mixed** content type: primarily a **tool/reference** README with tutorial-style setup instructions and product-marketing claims. Durability is **medium** because the conceptual idea of compressing CLI output for LLMs is fairly stable, but many details are version- and integration-specific (notably the cited `rtk 0.28.2`, supported agents, and platform behavior). Density is **high**: it packs installation, workflows, command lists, telemetry, and platform notes into a single page. Originality is mostly **primary source**, since this is the project’s own README, though it also functions as promotion. It’s best used as a **refer-back** reference for install/setup, supported commands, and integration capabilities rather than deep study. Scrape quality is **good**: the README content appears largely intact, including code blocks, tables, and major sections, though embedded images and linked external docs are not directly captured here.
