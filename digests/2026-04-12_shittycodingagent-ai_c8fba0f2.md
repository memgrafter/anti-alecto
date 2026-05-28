---
url: https://shittycodingagent.ai/
title: shittycodingagent.ai
scraped_at: '2026-04-12T10:43:24Z'
word_count: 694
raw_file: raw/2026-04-12_shittycodingagent-ai_c8fba0f2.txt
tldr: Pi is a minimal, highly extensible terminal coding agent that emphasizes workflow customization over built-in features, with support for multiple providers, sessions-as-trees, extensions, skills, packages, and several integration modes.
key_quote: Adapt pi to your workflows, not the other way around.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mario Zechner
tools:
- tmux
- pi
- OpenClaw
libraries: []
companies:
- Anthropic
- OpenAI
- Google
- Azure
- Bedrock
- Mistral
- Groq
- Cerebras
- xAI
- Hugging Face
- MiniMax
- OpenRouter
- Ollama
- GitHub
- Discord
tags:
- coding-agents
- terminal-tools
- extensibility
- context-management
- developer-tools
---

### TL;DR
Pi is a minimal, highly extensible terminal coding agent that emphasizes workflow customization over built-in features, with support for multiple providers, sessions-as-trees, extensions, skills, packages, and several integration modes.

### Key Quote
"Adapt pi to your workflows, not the other way around."

### Summary
- **What it is**
  - Pi is a **minimal terminal coding harness** distributed as `@mariozechner/pi-coding-agent`.
  - Core philosophy: keep the base tool small and let users add features through **TypeScript extensions**, **skills**, **prompt templates**, and **themes**.
  - Extensions and assets can be bundled into **pi packages** and shared via **npm** or **git**.

- **Core product stance**
  - Pi intentionally omits features common in other coding agents:
    - no sub-agents
    - no plan mode
    - no built-in permission popups
    - no built-in to-dos
    - no background bash
    - no mandatory MCP support
  - The idea is that users can implement these behaviors themselves via extensions, external tools, or packages.

- **Modes / integrations**
  - Four operating modes:
    - **interactive**
    - **print/JSON**
    - **RPC**
    - **SDK**
  - `pi -p "query"` for scripted use.
  - `--mode json` for event streams.
  - RPC uses stdin/stdout and is meant for non-Node integrations.
  - SDK support is intended for embedding Pi in other apps.
  - Mentions **OpenClaw** as a real-world integration/example.

- **Model and provider support**
  - Supports many providers, including:
    - Anthropic, OpenAI, Google, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, Hugging Face, Kimi For Coding, MiniMax, OpenRouter, Ollama, and more.
  - Authentication supports **API keys** or **OAuth**.
  - Model switching is built in:
    - `/model`
    - `Ctrl+L`
    - `Ctrl+P` to cycle favorites
  - Custom providers and models can be added through `models.json` or extensions.

- **Session management**
  - Sessions are stored as **trees**, not linear logs.
  - `/tree` lets you navigate to any previous point and continue from there.
  - All branches live in a **single file**.
  - Sessions can be filtered by message type and have bookmark labels.
  - Export options:
    - `/export` to HTML
    - `/share` uploads to a GitHub gist and returns a shareable rendered URL

- **Context management**
  - The tool is designed for “actual context engineering.”
  - Context can be shaped through:
    - **AGENTS.md** files loaded at startup from:
      - `~/.pi/agent/`
      - parent directories
      - current directory
    - **SYSTEM.md** to replace or append the default system prompt per project
    - **Compaction** that auto-summarizes old messages near the context limit, customizable via extensions
    - **Skills** that load on demand for progressive disclosure
    - **Prompt templates** as Markdown files, expanded with `/name`
    - **Dynamic context** through extensions that can inject messages, filter history, implement RAG, or build long-term memory

- **Queuing behavior**
  - Users can submit messages while the agent is working.
  - **Enter** sends a steering message that is delivered after the current tool and interrupts remaining tools.
  - **Alt+Enter** sends a follow-up that waits until the agent finishes.

- **Extensions**
  - Extensions are TypeScript modules with access to:
    - tools
    - commands
    - keyboard shortcuts
    - events
    - the full TUI
  - The page lists examples of features implementable via extensions:
    - sub-agents
    - plan mode
    - permission gates
    - path protection
    - SSH execution
    - sandboxing
    - MCP integration
    - custom editors
    - status bars
    - overlays
  - It explicitly says “Yes, Doom runs,” implying even game-like overlays are possible.
  - It references **50+ examples**.

- **Packages**
  - Pi packages can bundle:
    - extensions
    - skills
    - prompts
    - themes
  - Installation examples:
    - `$ pi install npm:@foo/pi-tools`
    - `$ pi install git:github.com/badlogic/pi-doom`
  - Version pinning:
    - `@1.2.3`
    - `@tag`
  - Package management commands:
    - `pi update`
    - `pi list`
    - `pi config`
  - You can test packages without installing:
    - `pi -e git:github.com/user/repo`
  - Packages can be found on **npm** or **Discord**, and shared using the `pi-package` keyword.

- **Philosophy / rationale**
  - Pi’s identity is “aggressively extensible” and intentionally minimal.
  - The argument is that features other tools hard-code should instead be:
    - built as extensions
    - supplied as skills
    - installed from third-party packages
  - This allows the core tool to stay small while users adapt it to their workflows.
  - The page gives explicit “No” statements for features, followed by suggested alternatives like tmux, TODO.md, containers, or custom extensions.
  - It points readers to a blog post for the full rationale.

- **Community**
  - Support and discussion channels:
    - **GitHub issues** for bugs and feature requests
    - **Discord** for discussion and sharing

### Assessment
This is a **mixed** reference/announcement page with strong marketing and product-philosophy content rather than a deep technical manual. **Durability is medium**: the core ideas about extensibility, context management, and workflow customization are broadly useful, but the details are tied to the current Pi feature set and command syntax. **Density is medium-high** because it contains many concrete commands, modes, and extension points, though it is still fairly promotional. **Originality is primarily primary source**, since it appears to be the product’s own landing page and docs summary. It’s best used as a **refer-back** source to confirm capabilities, commands, and philosophy, not as deep study. **Scrape quality is good** overall: the key sections, commands, and feature descriptions are present, though this appears to be a text-only capture and may omit visual design, demos, or linked documentation depth.
