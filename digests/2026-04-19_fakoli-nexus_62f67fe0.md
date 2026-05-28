---
url: https://github.com/fakoli/nexus
title: fakoli/nexus
scraped_at: '2026-04-19T08:23:22Z'
word_count: 783
raw_file: raw/2026-04-19_fakoli-nexus_62f67fe0.txt
tldr: fakoli/nexus is a TypeScript “Personal AI Assistant Gateway” that unifies Claude/OpenAI chat access behind a local gateway with CLI, TUI, web UI, channel adapters, and a plugin marketplace.
key_quote: Personal AI Assistant Gateway
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Hono
- SolidJS
- Zod
- Telegram
- Discord
- SQLite
- WebSocket
libraries:
- TypeScript
- Anthropic Claude
- OpenAI GPT
companies: []
tags:
- ai-assistant
- developer-tools
- cli
- web-ui
- plugin-system
---

### TL;DR
`fakoli/nexus` is a TypeScript “Personal AI Assistant Gateway” that unifies Claude/OpenAI chat access behind a local gateway with CLI, TUI, web UI, channel adapters, and a plugin marketplace.

### Key Quote
“Personal AI Assistant Gateway”

### Summary
- **What it is**
  - A GitHub repo for **Nexus**, described as a **Personal AI Assistant Gateway**.
  - Licensed under **MIT**.
  - Written in **TypeScript strict** and claims **533 passing tests**.

- **Core features**
  - **Multi-provider AI**: supports **Anthropic Claude** and **OpenAI GPT** through a shared provider abstraction.
  - **WebSocket gateway**: provides **full-duplex RPC** plus a **server-push event stream**; messages are **Zod-validated** before processing.
  - **Channel integrations**: adapters for **Telegram** and **Discord**.
  - **Plugin marketplace**: supports installing, updating, publishing plugins via an **HTTP registry** using CLI commands.
  - **SolidJS UI**: built-in web interface served at **`/ui/`**, so no separate frontend server is needed.

- **Quick start**
  - Install with `npm install` after cloning, or use the repo directly.
  - Requires setting an API key, e.g.:
    - `export ANTHROPIC_API_KEY=sk-ant-...`
  - Start via:
    - `npx tsx packages/cli/src/index.ts quickstart`
  - `quickstart`:
    - runs a setup wizard,
    - starts the gateway on **port 19200**,
    - opens a live chat session.

- **TUI chat**
  - Start a terminal session with:
    - `nexus chat`
  - Options:
    - `-s, --session <id>` to resume a session
    - `-p, --port <port>` to choose gateway port (default **19200**)
  - Built-in commands:
    - `/new`
    - `/sessions`
    - `/model <name>`
    - `/exit`

- **Architecture**
  - The repo is organized around several packages/components:
    - **Clients**: Browser (SolidJS), CLI, Telegram, Discord
    - **`@nexus/gateway`**: Hono HTTP server + WebSocket RPC server, auth middleware, RPC dispatch table
    - **`@nexus/core`**: SQLite WAL-backed storage for sessions, messages, config, agents, audit, crypto, rate limiting, event bus
    - **`@nexus/agent`**: execution loop, context builder, tool executor; providers include Anthropic/OpenAI; tools include bash and filesystem
    - **`@nexus/plugins`** plus `extensions/*`: plugin loader and marketplace registry client

- **CLI commands**
  - Main commands documented include:
    - `nexus quickstart` / `start`
    - `nexus chat`
    - `nexus gateway run`
    - `nexus gateway stop`
    - `nexus send <message>`
    - `nexus status`
    - `nexus config get [section]`
    - `nexus config set <section> <json>`
    - `nexus plugins list/search/install/update/uninstall/info`
    - registry management commands for plugin sources
  - Many commands support `--json` for machine-readable output.

- **Configuration**
  - Stored locally in **SQLite** at `~/.nexus/nexus.db`.
  - Managed through `nexus config set`.
  - Key config sections:
    - **`gateway`**
      - `port` default **19200**
      - `bind` default **loopback** (`loopback|lan|all`)
      - `verbose` default `false`
    - **`agent`**
      - `defaultProvider` default **anthropic**
      - `defaultModel` default **claude-sonnet-4-6**
      - `workspace` allowed filesystem path
      - `thinkLevel` default **low** (`off|low|medium|high`)
    - **`security`**
      - `gatewayToken`
      - `gatewayPassword`
      - `dmPolicy` default **pairing** (`pairing|open|deny`)
      - `promptGuard` default **enforce** (`enforce|warn|off`)
  - Example config commands show switching to OpenAI and setting a gateway token.

- **Documentation links**
  - Architecture
  - API Reference
  - Configuration
  - Channels (Telegram & Discord)
  - Plugin Authoring
  - Deployment
  - Plugin Marketplace

### Assessment
This is a **mixed** reference/announcement-style README with some tutorial content. **Durability is medium**: the architectural ideas and CLI structure are broadly reusable, but specific defaults like `claude-sonnet-4-6`, port `19200`, the reported test count, and provider support may age as the project evolves. The **density is high** because it packs features, commands, configuration tables, and architecture into one page. It appears to be a **primary source** project README rather than commentary or synthesis. Best used as **refer-back** documentation for quickly checking capabilities, commands, and config keys; it is not a deep technical spec. **Scrape quality is good** overall: the main README content, tables, code blocks, and architecture diagram text are present, though linked docs and images are not expanded here.
