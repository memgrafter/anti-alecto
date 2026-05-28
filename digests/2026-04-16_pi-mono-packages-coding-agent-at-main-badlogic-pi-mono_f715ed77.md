---
url: https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent#philosophy
title: pi-mono/packages/coding-agent at main · badlogic/pi-mono
scraped_at: '2026-04-16T03:53:29Z'
word_count: 3089
raw_file: raw/2026-04-16_pi-mono-packages-coding-agent-at-main-badlogic-pi-mono_f715ed77.txt
tldr: Pi is a minimal, highly extensible terminal coding agent that favors a small core plus packages, skills, prompts, extensions, and themes over built-in workflows like MCP, sub-agents, plan mode, and permission popups.
key_quote: Pi is aggressively extensible so it doesn't have to dictate your workflow.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mario Zechner
tools:
- pi
- Hugging Face CLI
- tmux
libraries:
- '@mariozechner/pi-coding-agent'
- '@mariozechner/pi-ai'
- '@mariozechner/pi-agent'
- '@mariozechner/pi-tui'
companies:
- GitHub
- Anthropic
- OpenAI
- Google
- Hugging Face
- Microsoft
- Amazon
tags:
- coding-agent
- terminal-tools
- llm-workflow
- developer-tooling
- extensibility
---

### TL;DR
Pi is a minimal, highly extensible terminal coding agent that favors a small core plus packages, skills, prompts, extensions, and themes over built-in workflows like MCP, sub-agents, plan mode, and permission popups.

### Key Quote
> “Pi is aggressively extensible so it doesn't have to dictate your workflow.”

### Summary
- **What this project is**
  - `@mariozechner/pi-coding-agent` is a terminal-based coding harness/agent called **Pi**.
  - It is designed to be **minimal by default** and **customizable through extensions** rather than hardcoded workflows.
  - The repository page is for `badlogic/pi-mono`, specifically the `packages/coding-agent` package.

- **Core positioning / philosophy**
  - Pi intentionally leaves out several features common in other coding agents:
    - **No MCP** by default
    - **No sub-agents**
    - **No permission popups**
    - **No plan mode**
    - **No built-in to-dos**
    - **No background bash**
  - The preferred alternative is to build those behaviors yourself via:
    - **TypeScript extensions**
    - **Skills**
    - **Prompt templates**
    - **Themes**
    - **Third-party Pi packages**
  - It explicitly says to adapt Pi to your workflow, not the other way around.

- **Session sharing / OSS data**
  - The page asks users to **share OSS coding-agent sessions** to help improve models, prompts, tools, and evaluations.
  - It links to:
    - a post on X explaining the rationale
    - `badlogic/pi-share-hf` for publishing sessions
    - a Hugging Face dataset of Pi-Mono work sessions
  - It says publishing only requires:
    - a **Hugging Face account**
    - the **Hugging Face CLI**
    - `pi-share-hf`

- **Installation / quick start**
  - Install globally:
    - `npm install -g @mariozechner/pi-coding-agent`
  - Start with an API key:
    - `export ANTHROPIC_API_KEY=sk-ant-...`
    - `pi`
  - Or log in with an existing subscription:
    - `pi`
    - `/login`
  - Default tools provided to the model:
    - `read`
    - `write`
    - `edit`
    - `bash`

- **Supported providers and models**
  - Pi maintains a built-in list of **tool-capable models** and updates it with each release.
  - Supported subscription providers include:
    - Anthropic Claude Pro/Max
    - OpenAI ChatGPT Plus/Pro (Codex)
    - GitHub Copilot
    - Google Gemini CLI
    - Google Antigravity
  - Supported API-key providers include:
    - Anthropic, OpenAI, Azure OpenAI, Google Gemini, Google Vertex, Amazon Bedrock, Mistral, Groq, Cerebras, xAI, OpenRouter, Vercel AI Gateway, ZAI, OpenCode Zen, OpenCode Go, Hugging Face, Kimi For Coding, MiniMax
  - Custom providers can be added via `~/.pi/agent/models.json` if they speak a supported API.
  - For custom APIs or OAuth flows, use extensions.

- **Interactive mode**
  - The interface has:
    - a startup header
    - messages area
    - editor
    - footer with working directory, session name, token/cache usage, cost, context usage, and current model
  - Key editor features:
    - `@` file fuzzy search
    - tab path completion
    - multi-line input with Shift+Enter
    - image paste/drag-and-drop
    - shell commands via `!command` and `!!command`
  - Commands include:
    - `/login`, `/logout`
    - `/model`
    - `/settings`
    - `/resume`
    - `/new`
    - `/tree`
    - `/fork`
    - `/compact`
    - `/share`
    - `/reload`
    - `/hotkeys`
    - `/quit`
  - Message queue behavior lets users send steering or follow-up messages while the agent is working.

- **Sessions**
  - Sessions are stored as **JSONL files with a tree structure**.
  - Each entry has an `id` and `parentId`, which enables branching without creating separate files.
  - Session management commands:
    - `pi -c` continue latest session
    - `pi -r` browse sessions
    - `pi --no-session` run ephemerally
    - `pi --session <path>` use a specific session
    - `pi --fork <path>` fork a session
  - `/tree` allows navigation through the session history and branches.
  - `/compact` summarizes older messages when the context window gets large.
  - Compaction is described as **lossy**, but full history remains in the JSONL file.

- **Settings and config**
  - Global settings live in:
    - `~/.pi/agent/settings.json`
  - Project settings live in:
    - `.pi/settings.json`
  - Anonymous install/update telemetry tied to changelog detection can be disabled with:
    - `enableInstallTelemetry: false`
    - or `PI_TELEMETRY=0`

- **Context files and prompts**
  - Pi automatically loads `AGENTS.md` or `CLAUDE.md` from:
    - global config
    - parent directories
    - current directory
  - These files are meant for:
    - project instructions
    - conventions
    - common commands
  - It also supports replacing or appending the system prompt via `.pi/SYSTEM.md`, `~/.pi/agent/SYSTEM.md`, and `APPEND_SYSTEM.md`.

- **Customization**
  - **Prompt templates**
    - Markdown prompts expandable with `/name`
  - **Skills**
    - On-demand capability bundles following the Agent Skills standard
    - Invoked via `/skill:name`
  - **Extensions**
    - TypeScript modules that can add tools, commands, event handlers, UI, checkpoints, sandboxing, MCP support, and more
    - The page explicitly mentions extensions can even implement sub-agents, plan mode, permission systems, or games
  - **Themes**
    - Built-in `dark` and `light`
    - Hot-reload supported
  - **Pi packages**
    - Bundle and share extensions, skills, prompts, and themes via npm or git
    - Security warning: packages run with full system access and should be reviewed before installation

- **Programmatic use**
  - **SDK**
    - Example shows creating an agent session using:
      - `AuthStorage`
      - `ModelRegistry`
      - `SessionManager`
      - `createAgentSession`
  - **RPC mode**
    - `pi --mode rpc`
    - Uses strict LF-delimited JSONL framing over stdin/stdout
    - Documentation warns not to use generic line readers that can split on Unicode separators

- **CLI reference**
  - The document includes a full command-line reference for:
    - package management
    - modes
    - model selection
    - session handling
    - tool selection
    - loading extensions/skills/prompts/themes
    - system prompt overrides
    - environment variables
  - Notable options include:
    - `--print`
    - `--mode json`
    - `--mode rpc`
    - `--tools`
    - `--no-tools`
    - `--extension`
    - `--skill`
    - `--prompt-template`
    - `--theme`
    - `--system-prompt`
    - `--append-system-prompt`

- **Trust / maintenance signals**
  - The page references a specific blog post dated **2025-11-30** for the rationale behind Pi’s philosophy.
  - It also points to multiple docs files, examples, and platform-specific setup guides, suggesting an actively maintained and fairly comprehensive project page.

### Assessment
This is a **mixed** reference/tutorial document with a strong opinionated philosophy section and extensive usage docs. Durability is **medium**: the architectural ideas about extensibility and minimal core are fairly timeless, but many specifics—supported providers, command flags, session behavior, telemetry defaults, and package ecosystem—are version- and project-dependent. Content density is **high**, with lots of concrete commands, file paths, configuration keys, and feature lists. Originality is **primary source** because it is the project’s own documentation and philosophy statement. Best used as **refer-back** material: it’s worth revisiting when installing Pi, configuring providers, writing extensions, or checking its stance on features like MCP or sub-agents. Scrape quality is **good**: the content appears substantially complete for the README section, though embedded images and linked docs/videos are not fully captured in the scrape.
