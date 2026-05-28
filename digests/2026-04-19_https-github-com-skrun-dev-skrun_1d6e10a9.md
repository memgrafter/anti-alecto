---
url: https://github.com/skrun-dev/skrun
title: https://github.com/skrun-dev/skrun
scraped_at: '2026-04-19T20:07:54Z'
word_count: 1220
raw_file: raw/2026-04-19_https-github-com-skrun-dev-skrun_1d6e10a9.txt
tldr: Skrun is an open-source, self-hostable agent runtime that turns “Agent Skills” into APIs via `POST /run`, supports multiple LLM providers, streaming, state, and a typed SDK, positioning itself as an alternative to proprietary managed agent platforms.
key_quote: Deploy any Agent Skill as an API via `POST /run`.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- pino
- Scalar
- OpenAPI
- Claude Code
- Copilot
- Codex
- MCP
libraries: []
companies:
- Anthropic
- OpenAI
- Google
- Mistral
- Groq
- DeepSeek
- Kimi
- Qwen
- Microsoft
- Koyeb
- Axiom
- Datadog
- ELK
tags:
- agent-runtimes
- api-development
- self-hosting
- llm-platforms
- developer-tools
---

### TL;DR
Skrun is an open-source, self-hostable agent runtime that turns “Agent Skills” into APIs via `POST /run`, supports multiple LLM providers, streaming, state, and a typed SDK, positioning itself as an alternative to proprietary managed agent platforms.

### Key Quote
“Deploy any Agent Skill as an API via `POST /run`.”

### Summary
- **What it is**
  - Skrun is a **multi-model agent runtime** for deploying agent skills as API endpoints.
  - It is presented as an **open-source alternative** to Claude Managed Agents, Microsoft Foundry Agent Service, and Mistral + Koyeb.
  - The project is **MIT licensed** and claims to be **self-hostable** with “zero lock-in.”

- **Core idea**
  - Every agent exposes a `POST /run` interface.
  - It uses the **Agent Skills** format (`SKILL.md`) and says it works with Claude Code, Copilot, and Codex.
  - The runtime separates:
    - **agent behavior**: model, tools, inputs/outputs
    - **runtime environment**: networking, timeout, sandbox, per-run overrides

- **Quick start**
  - Install CLI: `npm install -g @skrun-dev/cli`
  - Import a skill: `skrun init --from-skill ./my-skill`
  - Deploy: `skrun deploy`
  - Call the agent locally with:
    - `POST http://localhost:4000/api/agents/dev/my-skill/run`
    - Authorization header: `Bearer dev-token`
    - JSON body like `{"input": {"query": "analyze this"}}`

- **Features highlighted**
  - **Multi-model support**: Anthropic, OpenAI, Google, Mistral, Groq, DeepSeek, Kimi, Qwen, and any OpenAI-compatible endpoint
  - **Streaming**: SSE events (`run_start` → `tool_call` → `run_complete`) and async webhooks
  - **Typed SDK**: `run()`, `stream()`, `runAsync()` and additional methods
  - **Tool calling**:
    - local scripts from `scripts/`
    - MCP servers via `npx`
  - **Stateful agents**: remembers across runs via key-value state
  - **Interactive docs**: OpenAPI 3.1 schema and Scalar explorer at `GET /docs`
  - **Caller-pays model**: users bring their own LLM keys via `X-LLM-API-Key`
  - **Agent verification**: verified flag controls script execution
  - **Version pinning**: call a specific agent version like `version: "1.2.0"`
  - **Structured logs**: JSON logs with `pino` and `LOG_LEVEL`
  - **Files API**: agents can output files downloadable by run ID

- **SDK details**
  - Install with: `npm install @skrun-dev/sdk`
  - Example client usage:
    - instantiate `SkrunClient` with `baseUrl` and token
    - `client.run(...)` for sync results
    - `client.stream(...)` for event streaming
    - `client.runAsync(...)` for webhook-based async execution
  - The README claims **9 methods**, **zero runtime dependencies**, and **Node.js 18+**

- **Demo agents / examples**
  - `code-review` — turn a skill into a code quality API
  - `pdf-processing` — local script tool calling
  - `seo-audit` — demonstrates stateful behavior across runs
  - `data-analyst` — CSV in, structured insights out
  - `email-drafter` — non-developer business use case
  - `web-scraper` — MCP server example using Playwright MCP
  - The examples default to **Google Gemini Flash**

- **CLI commands**
  - `skrun init [dir]`
  - `skrun init --from-skill <path>`
  - `skrun dev`
  - `skrun test`
  - `skrun build`
  - `skrun deploy`
  - `skrun push` / `pull`
  - `skrun login` / `logout`
  - `skrun logs <agent>`

- **Docs / reference sections**
  - API reference: `docs/api.md`
  - `agent.yaml` spec: `docs/agent-yaml.md`
  - CLI reference: `docs/cli.md`
  - Changelog, contributing guide, OpenAPI schema, and interactive docs are all linked
  - Note: some links are shown as local dev URLs like `http://localhost:4000/docs`, implying the docs are meant to be used in a running local instance

- **Use cases claimed**
  - Turn a skill into a production API in under 2 minutes
  - Build internal AI tools with typed I/O
  - Run untrusted agents more safely with verification
  - Offer agents as a product while users supply keys
  - Self-host on cloud or bare metal
  - Compose agents with MCP servers

### Assessment
This is a **mixed** content type, mostly a **reference/tutorial** README for a developer tool. Durability is **medium**: the architectural ideas around agent runtimes, API deployment, and multi-model support should age fairly well, but specific commands, package names, and provider lists may change quickly with versions. The density is **high**, with many concrete commands, endpoints, feature claims, and examples packed into a marketing-style README. Originality is mostly **primary source** for the project’s own documentation and positioning, though it also includes some competitive framing and ecosystem references. It’s best used as **refer-back** material rather than a one-time skim, especially if you’re evaluating whether Skrun fits a self-hosted agent API workflow. Scrape quality appears **good** for the README content provided, though it may be incomplete relative to the full repository; code examples, docs links, and tables are present, but deeper file contents and implementation details are not included.
