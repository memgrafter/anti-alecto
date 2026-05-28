---
url: https://github.com/neovertex1/nuggets
title: 'NeoVertex1/nuggets: First AI assistant with holographic memory'
scraped_at: '2026-04-19T08:04:59Z'
word_count: 1399
raw_file: raw/2026-04-19_neovertex1-nuggets-first-ai-assistant-with-holographic-memory_ed674759.txt
tldr: Nuggets is a TypeScript-based AI assistant project that pairs holographic memory with Telegram/WhatsApp messaging, plus a newer MCP plugin for coding agents that adds lightweight cross-session memory and recall.
key_quote: “facts are stored as superposed complex-valued vectors using Holographic Reduced Representations (HRR).”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- NeoVertex1
- Pi
- Anthropic
- BotFather
- userinfobot
tools:
- nuggets-memory-plugin
- hermes
- claude
- codex
- npm
- Telegram
- WhatsApp
- Pi coding agent
libraries:
- grammY
- Baileys
companies:
- GitHub
- Anthropic
tags:
- ai-assistant
- holographic-memory
- telegram-bot
- whatsapp-integration
- mcp-plugin
---

### TL;DR
Nuggets is a TypeScript-based AI assistant project that pairs holographic memory with Telegram/WhatsApp messaging, plus a newer MCP plugin for coding agents that adds lightweight cross-session memory and recall.

### Key Quote
“facts are stored as superposed complex-valued vectors using Holographic Reduced Representations (HRR).”

### Summary
- **What it is**
  - An AI assistant named **Nuggets** that “remembers” across sessions.
  - Combines:
    - a **holographic memory engine** for storing and recalling facts locally
    - a **multi-channel messaging gateway** for Telegram and WhatsApp
    - a newer **`nuggets-memory-plugin`** for MCP-based coding agents

- **New plugin/MCP workflow**
  - Package name: **`nuggets-memory-plugin`**
  - Install globally:
    ```bash
    npm install -g nuggets-memory-plugin
    ```
  - Register with agent hosts:
    - **Hermes Agent**
      ```bash
      hermes mcp add nuggets-memory --command nuggets-memory-plugin
      ```
    - **Claude Code**
      ```bash
      claude mcp add nuggets-memory -- nuggets-memory-plugin
      ```
    - **Codex**
      ```bash
      codex mcp add nuggets-memory -- nuggets-memory-plugin
      ```
  - Intended for:
    - short durable facts
    - preferences and corrections
    - tiny project hints
    - tools like `guide`, `nudges`, `recall`, `remember`, `list`, and `status`
  - Notes:
    - global binary is recommended for startup speed over `npx`
    - plugin-first development lives in `nuggets-memory/`
    - the rest of the README documents the older app/gateway workflow

- **Core memory model**
  - Uses **Holographic Reduced Representations (HRR)**:
    - facts are encoded as **superposed complex-valued vectors**
    - recall is algebraic and local, with no external vector DB or embedding API
  - Memory operations:
    - **remember** — bind key/value pairs into the vector
    - **recall** — unbind and decode with cosine similarity, plus token-overlap matching for natural-language queries
    - **forget** — subtract a binding from the superposition
    - **promote** — facts recalled **3+ times** are written to `MEMORY.md`
  - Memory is split into kinds:
    - **user** — preferences
    - **project** — files, commands, repo context
    - **agent** — self-knowledge
  - Storage:
    - simple JSON files under `~/.nuggets/`
    - examples: `user.nugget.json`, `project.nugget.json`
    - vectors are **not serialized**; they are rebuilt deterministically from a seeded PRNG
  - There is a migration script:
    - `npm run migrate:memory`

- **Messaging gateway**
  - Routes messages through **Telegram** and **WhatsApp**
  - Notable implementation details:
    - **per-user Pi subprocess pool**
    - **JSONL RPC** over stdin/stdout
    - **per-user message queue** to avoid race conditions
    - **heartbeat** every 30 minutes during waking hours
    - **cron scheduler** for recurring and one-shot messages
    - **quiet hours** from 10 PM to 8 AM by default, configurable
  - Proactive behavior:
    - the assistant can check in, send reminders, and schedule tasks
    - if there’s nothing useful, it stays silent

- **Pi extensions**
  - `nuggets.ts`
    - exposes a `nuggets` tool to Pi for remember/recall/forget
    - auto-captures file paths and user preferences
    - injects memory into the system prompt
  - `proactive.ts`
    - adds a `schedule` tool for reminders and recurring tasks

- **Setup and prerequisites**
  - Requires:
    - **Node.js 18+**
    - **Pi** coding agent
    - **Anthropic API key**
    - **Telegram bot token**
    - **Telegram chat ID**
  - Important note:
    - Anthropic Max plan does **not** work here because third-party OAuth was blocked in **Jan 2026**
  - Quick start:
    ```bash
    npm install -g @mariozechner/pi-coding-agent
    git clone https://github.com/NeoVertex1/nuggets.git
    cd nuggets
    npm install
    npm run setup
    npm run dev
    ```
  - `npm run setup` is the recommended first-run path because it interactively writes `.env`
  - The wizard validates:
    - API key format
    - bot token format
    - numeric chat ID
    - and can show masked existing values

- **How it works**
  - Message flow:
    - user sends message via Telegram/WhatsApp
    - gateway routes it to a Pi subprocess
    - Pi checks Nuggets memory
    - response is delivered back through the gateway
  - Proactive flow:
    - heartbeat or cron triggers an event
    - Pi checks whether something is worth sending
    - if yes, it messages the user; otherwise it remains quiet
  - Promotion flow:
    - repeated recall causes facts to be moved into `MEMORY.md` for permanent context

- **Repository structure**
  - `src/nuggets/` — memory engine
  - `src/gateway/` — messaging gateway
  - `.pi/extensions/` — Pi lifecycle hooks
  - `setup.ts` — interactive configuration wizard

- **Scripts**
  - `npm run setup` — create `.env`
  - `npm run dev` — start gateway
  - `npm test` — run tests
  - `npm run migrate:memory` — migrate memory layout
  - `npm run typecheck` — type-check
  - `npm run build` — compile to `dist/`

- **Testing and license**
  - Tests cover:
    - HRR math
    - remember/recall/forget lifecycle
    - shelf management
  - License: **MIT**

### Assessment
This is a **mixed** technical README/reference page with both product marketing and implementation detail. Durability is **medium**: the memory concepts and architecture are fairly timeless, but setup instructions, integration commands, and the Anthropic/Max-plan note are version- and policy-sensitive. Density is **high**, since it packs architecture, commands, workflow diagrams, and repository layout into one document. Originality is mainly **primary source** documentation from the project authors, though it includes some promotional framing (“first AI assistant with holographic memory”). It’s best used as a **refer-back** reference rather than deep study unless you plan to implement or run the system. Scrape quality is **good** overall: the README structure, commands, and sections are present, though some duplication appears at the end and any visuals are reduced to text/images links rather than the actual rendered content.
