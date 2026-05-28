---
url: https://github.com/NousResearch/hermes-agent
title: 'NousResearch/hermes-agent: The agent that grows with you'
scraped_at: '2026-04-19T07:43:15Z'
word_count: 1214
raw_file: raw/2026-04-19_nousresearch-hermes-agent-the-agent-that-grows-with-you_930dd134.txt
tldr: Hermes Agent is Nous Research’s MIT-licensed, self-improving AI agent framework with a terminal UI, multi-platform messaging gateway, persistent memory/skills, scheduling, and support for many LLM providers and deployment targets.
key_quote: The self-improving AI agent built by [Nous Research](https://nousresearch.com).
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Nous Research
- Honcho
tools:
- hermes
- hermes model
- hermes tools
- hermes config set
- hermes gateway
- hermes setup
- hermes claw migrate
- hermes update
- hermes doctor
- OpenRouter
- NVIDIA NIM
- Hugging Face
- OpenAI
- Termux
libraries:
- uv
companies:
- Nous Research
- Telegram
- Discord
- Slack
- WhatsApp
- Signal
- OpenRouter
- NVIDIA
- Hugging Face
- OpenAI
- Daytona
- Modal
- MiniMax
- Xiaomi
- Kimi
- Moonshot
- z.ai
- Nous Portal
tags:
- ai-agents
- command-line-tools
- messaging-gateway
- persistent-memory
- model-providers
---

### TL;DR
Hermes Agent is Nous Research’s MIT-licensed, self-improving AI agent framework with a terminal UI, multi-platform messaging gateway, persistent memory/skills, scheduling, and support for many LLM providers and deployment targets.

### Key Quote
"The self-improving AI agent built by [Nous Research](https://nousresearch.com)."

### Summary
- **What it is**
  - Hermes Agent is an AI agent project from Nous Research described as “the agent that grows with you.”
  - It emphasizes a **built-in learning loop**: it can create skills from experience, improve them while in use, persist knowledge, search past conversations, and build a user model across sessions.
  - Licensed under **MIT**.

- **Core capabilities**
  - **Terminal interface (TUI)** with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output.
  - **Messaging gateway** for using the agent through:
    - Telegram
    - Discord
    - Slack
    - WhatsApp
    - Signal
    - Email
    - CLI
  - **Persistent memory and skill system**
    - Agent-curated memory with periodic nudges.
    - Autonomous skill creation after complex tasks.
    - Skills self-improve during use.
    - FTS5 session search plus LLM summarization for cross-session recall.
    - Compatibility with the **agentskills.io** open standard.
    - Mentions **Honcho** for user modeling.
  - **Automation**
    - Built-in cron scheduler for unattended tasks like daily reports, nightly backups, and weekly audits.
  - **Parallel work**
    - Can spawn isolated subagents.
    - Can write Python scripts that call tools via RPC to reduce context overhead.
  - **Deployment flexibility**
    - Supported backends: local, Docker, SSH, Daytona, Singularity, and Modal.
    - Claims it can run on a $5 VPS, GPU cluster, or serverless infrastructure with near-zero idle cost.
  - **Model/provider flexibility**
    - Works with many providers: Nous Portal, OpenRouter, NVIDIA NIM, Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face, OpenAI, or a custom endpoint.
    - Model switching is done with `hermes model` without code changes.

- **Install and first use**
  - Quick install command:
    ```bash
    curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
    ```
  - Supported on **Linux, macOS, WSL2, and Android via Termux**.
  - **Windows is not supported natively**; WSL2 is required.
  - After installation:
    ```bash
    source ~/.bashrc
    hermes
    ```

- **Important CLI commands**
  - `hermes` — start the interactive CLI
  - `hermes model` — choose provider/model
  - `hermes tools` — configure enabled tools
  - `hermes config set` — set config values
  - `hermes gateway` — start messaging integrations
  - `hermes setup` — full setup wizard
  - `hermes claw migrate` — migrate from OpenClaw
  - `hermes update` — update the installation
  - `hermes doctor` — diagnose issues

- **CLI vs messaging usage**
  - The README includes a quick reference table showing shared commands across CLI and messaging platforms.
  - Shared actions include:
    - `/new` or `/reset`
    - `/model [provider:model]`
    - `/personality [name]`
    - `/retry`, `/undo`
    - `/compress`, `/usage`, `/insights`
    - `/skills` or `/<skill-name>`
    - interrupting work via `Ctrl+C`, `/stop`, or sending a new message

- **Documentation structure**
  - Docs are hosted at `hermes-agent.nousresearch.com/docs`.
  - Key sections include:
    - Quickstart
    - CLI Usage
    - Configuration
    - Messaging Gateway
    - Security
    - Tools & Toolsets
    - Skills System
    - Memory
    - MCP Integration
    - Cron Scheduling
    - Context Files
    - Architecture
    - Contributing
    - CLI Reference
    - Environment Variables

- **Migration from OpenClaw**
  - Hermes can import settings, memories, skills, API keys, and other workspace data from OpenClaw.
  - `hermes setup` can detect `~/.openclaw` and offer migration automatically.
  - Migration commands include:
    - `hermes claw migrate`
    - `hermes claw migrate --dry-run`
    - `hermes claw migrate --preset user-data`
    - `hermes claw migrate --overwrite`
  - Imported items include:
    - `SOUL.md`
    - `MEMORY.md` and `USER.md`
    - user-created skills
    - command allowlists
    - messaging settings
    - allowlisted API keys
    - TTS assets
    - `AGENTS.md` workspace instructions

- **Contributing**
  - The project encourages contributions and provides a quick-start path:
    - clone repo
    - run `./setup-hermes.sh`
    - launch `./hermes`
  - Manual contributor setup uses:
    - `uv`
    - Python 3.11
    - editable install with `uv pip install -e ".[all,dev]"`
    - tests with `python -m pytest tests/ -q`
  - Optional RL/training work requires the `tinker-atropos` submodule.

- **Community and ecosystem**
  - Community links include Discord, Skills Hub, Issues, Discussions, and a community WeChat bridge (`HermesClaw`).
  - The README positions the project as both a product and a research platform, mentioning trajectory generation, Atropos RL environments, and trajectory compression for future tool-calling model training.

### Assessment
This is a high-durability but partially promotional reference/announcement-style README for a mixed content type project: it combines product positioning, installation tutorial, usage reference, and some research-oriented claims. The information density is high, especially around features, commands, and migration paths, but many claims are marketing-forward rather than independently validated in the text. Originality is primarily a primary-source project overview from Nous Research, with a broad but non-exhaustive scrape that appears to capture the main README sections well; however, code blocks and section references beyond the README may be incomplete or missing finer details from linked documentation. Use it as a refer-back source for what Hermes Agent claims to do, how to install it, and where to find the deeper docs.
