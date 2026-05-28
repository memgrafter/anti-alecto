---
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/README.md
title: pi-mono/packages/coding-agent/README.md at main · badlogic/pi-mono
scraped_at: '2026-04-16T03:54:59Z'
word_count: 3089
raw_file: raw/2026-04-16_pi-mono-packages-coding-agent-readme-md-at-main-badlogic-pi-mono_13a8c1b1.txt
tldr: pi-coding-agent is a highly extensible terminal-based coding harness that supports interactive, print/JSON, RPC, and SDK usage, with customization via TypeScript extensions, skills, prompt templates, themes, and shareable “Pi Packages.”
key_quote: Pi is a minimal terminal coding harness.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Mario Zechner
tools:
- pi
- npm
- GitHub Copilot
- Google Gemini CLI
- Google Antigravity
- Anthropic Claude Pro/Max
- OpenAI ChatGPT Plus/Pro
- Vercel AI Gateway
libraries:
- '@mariozechner/pi-coding-agent'
- '@mariozechner/pi-ai'
- '@mariozechner/pi-agent'
- '@mariozechner/pi-tui'
companies:
- Anthropic
- OpenAI
- Azure OpenAI
- Google
- Amazon Bedrock
- Mistral
- Groq
- Cerebras
- xAI
- OpenRouter
- Vercel
- Hugging Face
- GitHub
tags:
- coding-agent
- terminal-tools
- developer-productivity
- extensibility
- cli-reference
---

### TL;DR
`pi-coding-agent` is a highly extensible terminal-based coding harness that supports interactive, print/JSON, RPC, and SDK usage, with customization via TypeScript extensions, skills, prompt templates, themes, and shareable “Pi Packages.”

### Key Quote
“Pi is a minimal terminal coding harness.”

### Summary
- **What it is**
  - `pi` is presented as a minimal terminal coding agent/tool designed to be adapted to the user’s workflow rather than forcing a fixed workflow.
  - It emphasizes extensibility over built-in opinionated features.
  - Core feature set is intentionally small; features like sub-agents, plan mode, permission popups, built-in to-dos, and background bash are explicitly not built in.

- **Installation and quick start**
  - Install globally with:
    - `npm install -g @mariozechner/pi-coding-agent`
  - Authenticate either with:
    - an API key, e.g. `export ANTHROPIC_API_KEY=sk-ant-...`
    - or an existing subscription via `pi` then `/login`
  - Default built-in tools provided to the model:
    - `read`
    - `write`
    - `edit`
    - `bash`

- **Supported providers and models**
  - Built-in provider/model lists are maintained and updated each release.
  - Subscription-based access includes:
    - Anthropic Claude Pro/Max
    - OpenAI ChatGPT Plus/Pro (Codex)
    - GitHub Copilot
    - Google Gemini CLI
    - Google Antigravity
  - API key providers include:
    - Anthropic, OpenAI, Azure OpenAI, Google Gemini, Google Vertex, Amazon Bedrock, Mistral, Groq, Cerebras, xAI, OpenRouter, Vercel AI Gateway, ZAI, OpenCode Zen, OpenCode Go, Hugging Face, Kimi For Coding, MiniMax
  - Custom providers/models can be configured through `~/.pi/agent/models.json` if they match supported APIs; custom APIs/OAuth require extensions.

- **Interactive mode**
  - The UI is described top-to-bottom as:
    - startup header
    - messages
    - editor
    - footer
  - The editor supports:
    - `@` file reference search
    - tab path completion
    - multiline input with Shift+Enter
    - image paste/drag-and-drop
    - bash command shortcuts:
      - `!command` runs and sends output to the LLM
      - `!!command` runs without sending output
  - Commands include:
    - `/login`, `/logout`, `/model`, `/settings`, `/resume`, `/new`, `/tree`, `/fork`, `/compact`, `/copy`, `/export`, `/share`, `/reload`, `/hotkeys`, `/changelog`, `/quit`
  - Keyboard shortcuts and message queuing are documented, including:
    - Ctrl+L for model selection
    - Ctrl+P / Shift+Ctrl+P for scoped model cycling
    - Escape twice to open `/tree`
    - Enter to queue steering messages
    - Alt+Enter to queue follow-up messages

- **Sessions**
  - Sessions are stored as JSONL files with a tree structure using `id` and `parentId`.
  - Sessions auto-save under `~/.pi/agent/sessions/` by working directory.
  - CLI options include:
    - `-c` continue
    - `-r` resume
    - `--no-session`
    - `--session <path>`
    - `--fork <path>`
  - Branching:
    - `/tree` lets you navigate prior points and continue from a selected branch.
    - `/fork` creates a new session from the current branch.
  - Compaction:
    - automatic and manual compaction is supported
    - it summarizes older messages while preserving the full history in JSONL
    - compaction is lossy, but the underlying session file preserves full history

- **Settings and context files**
  - Settings can be global or project-specific:
    - `~/.pi/agent/settings.json`
    - `.pi/settings.json`
  - Telemetry for install/update changelog detection can be disabled with:
    - `enableInstallTelemetry: false`
    - or `PI_TELEMETRY=0`
  - Context files:
    - `AGENTS.md` or `CLAUDE.md` are loaded from global, parent directories, and current directory
    - system prompt can be replaced or appended with `.pi/SYSTEM.md`, `~/.pi/agent/SYSTEM.md`, or `APPEND_SYSTEM.md`

- **Customization**
  - **Prompt templates**
    - Markdown files expanded with `/name`
    - used for reusable prompts like code review
  - **Skills**
    - on-demand capability packages following the Agent Skills standard
    - invoked as `/skill:name`
  - **Extensions**
    - TypeScript modules that can add tools, commands, keybindings, event handlers, and UI components
    - can implement advanced behaviors such as custom compaction, permission gates, sandboxing, MCP integration, and even games
  - **Themes**
    - built-in `dark` and `light`
    - hot-reload supported
  - **Pi Packages**
    - bundle and share extensions, skills, prompts, and themes via npm or git
    - installation commands are provided (`pi install`, `pi remove`, `pi update`, `pi list`, `pi config`)
    - important warning: packages run with full system access

- **Programmatic usage**
  - **SDK**
    - Example shows using `AuthStorage`, `createAgentSession`, `ModelRegistry`, and `SessionManager`
    - Supports embedding pi in other apps
  - **RPC mode**
    - `pi --mode rpc`
    - communicates via strict LF-delimited JSONL over stdin/stdout
    - warns not to use generic line readers that split on Unicode separators

- **CLI reference**
  - Main syntax:
    - `pi [options] [@files...] [messages...]`
  - Modes:
    - interactive (default)
    - print (`-p`, `--print`)
    - JSON (`--mode json`)
    - RPC (`--mode rpc`)
    - export
  - Tool selection, resources, model options, session options, and environment variables are all documented in a long reference section.
  - Example commands show:
    - summarizing via piped stdin
    - selecting providers/models
    - read-only review mode
    - high-thinking mode

- **Philosophy**
  - The README strongly argues for a minimal core plus user-extensible behavior.
  - It explicitly rejects several features as built-in defaults:
    - MCP
    - sub-agents
    - permission popups
    - plan mode
    - built-in to-dos
    - background bash
  - The stated idea is that users should implement these via extensions, skills, packages, tmux, or their own workflow.

- **OSS session sharing**
  - The project asks open-source users to share coding agent sessions to help improve models, prompts, tools, and evaluations.
  - It points to:
    - `badlogic/pi-share-hf`
    - a Hugging Face dataset of published `pi-mono` sessions
    - related posts/videos on X

- **Other notes**
  - The page includes badges for Discord, npm version, and GitHub Actions build status.
  - License is MIT.
  - “See Also” lists related packages:
    - `@mariozechner/pi-ai`
    - `@mariozechner/pi-agent`
    - `@mariozechner/pi-tui`

### Assessment
This is a high-density, highly actionable **reference/tutorial/mixed** README for a live software project, with strong practical detail on installation, configuration, customization, CLI usage, and architecture. Durability is **medium** because the concepts around extensible terminal agents are fairly durable, but many specifics depend on current package names, providers, commands, and supported models. Originality is mostly **primary source** because it documents the project’s own design and usage, though it also includes some promotional/community material and links to external posts. It is best used as a **refer-back** or **deep-study** resource rather than a skim-once note, since it contains many commands, flags, paths, and configuration details worth revisiting. Scrape quality is **good** overall: the README content appears complete and well-captured, though embedded images are referenced rather than rendered, and any linked docs/examples are not included in the scrape.
