---
url: https://github.com/ghuntley/loom
title: 'ghuntley/loom: if your name is not Geoffrey Huntley then do not use loom'
scraped_at: '2026-04-12T10:39:08Z'
word_count: 561
raw_file: raw/2026-04-12_ghuntley-loom-if-your-name-is-not-geoffrey-huntley-then-do-not-use-loom_682cb3e6.txt
tldr: Loom is Geoffrey Huntley’s proprietary, experimental Rust-based AI coding agent with a server-side LLM proxy, modular workspace architecture, and a strong “do not use unless you are Geoffrey Huntley” warning.
key_quote: “Loom is a research project. If your name is not Geoffrey Huntley then do not use.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Geoffrey Huntley
tools:
- cargo2nix
- Nix
- Kubernetes
- PostHog
- OpenAI
- Anthropic
- Svelte 5
libraries: []
companies:
- OpenAI
- Anthropic
tags:
- ai-coding-agent
- rust
- llm-proxy
- modular-architecture
- proprietary-software
---

### TL;DR
Loom is Geoffrey Huntley’s proprietary, experimental Rust-based AI coding agent with a server-side LLM proxy, modular workspace architecture, and a strong “do not use unless you are Geoffrey Huntley” warning.

### Key Quote
“Loom is a research project. If your name is not Geoffrey Huntley then do not use.”

### Summary
- **What it is**
  - Loom is an **AI-powered coding agent** written in **Rust**.
  - It offers a **REPL interface** for interacting with LLM-driven agents that can run tools for:
    - file system operations
    - code analysis
    - other development tasks
- **Warning / status**
  - The repository is explicitly marked as a **research project**.
  - It is described as:
    - **experimental**
    - **unstable**
    - **under active development**
  - The notice says:
    - APIs may change without notice
    - features may be incomplete or broken
    - no support or warranty is provided
    - only Geoffrey Huntley is intended to use it
- **Design principles**
  - **Modularity**: clear separation between core abstractions, LLM providers, and tools
  - **Extensibility**: new providers and tools can be added via trait implementations
  - **Reliability**: retry mechanisms and structured logging are emphasized
- **Architecture**
  - The project is a **Cargo workspace with 30+ crates**.
  - Major areas include:
    - `loom-core` — core abstractions, state machine, types
    - `loom-server` — HTTP API server with LLM proxy
    - `loom-cli` — command-line interface
    - `loom-thread` — conversation persistence and sync
    - `loom-tools` — agent tool implementations
    - `loom-llm-*` — LLM provider integrations
    - `loom-auth*` — authentication/authorization
    - `loom-tui-*` — terminal UI components
    - `web/loom-web` — Svelte 5 frontend
    - `specs/` — design specifications
    - `infra/` — Nix/Kubernetes infrastructure
- **Highlighted subsystems**
  - **Core Agent**: conversation state machine and tool orchestration
  - **LLM Proxy**: server-side proxy where **API keys never leave the server**
  - **Tool System**: registry/execution layer for agent capabilities
  - **Weaver**: remote execution using Kubernetes pods
  - **Thread System**: conversation persistence with **FTS5 search**
  - **Analytics**: PostHog-style analytics with identity resolution
  - **Auth**: OAuth, magic links, and ABAC authorization
  - **Feature Flags**: runtime toggles, experiments, kill switches
- **LLM interaction model**
  - Clients such as `loom-cli` talk to `loom-server`.
  - The server proxies requests to providers like **Anthropic** and **OpenAI**.
  - Communication uses HTTP and SSE streams.
  - The architecture is explicitly server-side so that **provider API keys are stored only on the server**.
- **Build / development**
  - Preferred build method is **Nix** with `cargo2nix` for reproducible builds and per-crate caching:
    - `nix build .#loom-cli-c2n`
    - `nix build .#loom-server-c2n`
    - `nix build .#<crate-name>-c2n`
  - Development with Cargo is also documented:
    - `cargo build --workspace`
    - `cargo test --workspace`
    - `cargo clippy --workspace -- -D warnings`
    - `cargo fmt --all`
    - `make check`
- **Documentation**
  - Design specs live in `specs/`
  - `specs/README.md` is the index, grouped by categories like:
    - Core Architecture
    - LLM Integration
    - Configuration & Security
    - Analytics & Experimentation
    - Editor Integration
    - Remote Execution (Weaver)
- **License**
  - The project is **proprietary**
  - Copyright is held by **Geoffrey Huntley (2025)**

### Assessment
This is a **mixed** reference/announcement-style repository overview with a very strong caveat that the software is not meant for general use. Durability is **medium**: the architectural patterns (Rust workspace, server-side LLM proxy, tool orchestration, feature flags, auth, remote execution) are broadly reusable, but the repository is tied to active development and specific tooling versions like Nix, cargo2nix, Svelte 5, and Kubernetes. The content is fairly **dense** and specific, and it reads as a **primary source** because it is the project’s own README. It is best used as a **skim-once / refer-back** reference for understanding the system layout and build commands, not as deep-study documentation, since the text itself warns that documentation is incomplete and APIs may change. Scrape quality appears **good**: the main README structure, code blocks, architecture diagram, and key sections are all present, though detailed specs and implementation internals are not included here.
