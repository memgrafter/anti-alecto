---
url: https://github.com/router-for-me/CLIProxyAPI
title: 'router-for-me/CLIProxyAPI: Wrap Gemini CLI, Antigravity, ChatGPT Codex, Claude Code, Qwen Code, iFlow as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini 2.5 Pro, GPT 5, Claude, Qwen model through API'
scraped_at: '2026-04-12T10:42:34Z'
word_count: 1731
raw_file: raw/2026-04-12_router-for-me-cliproxyapi-wrap-gemini-cli-antigravity-chatgpt-codex-claude-code-_73b26400.txt
tldr: CLIProxyAPI is a Go-based proxy service that turns CLI account access for Gemini, Claude, OpenAI Codex, Qwen, and iFlow into OpenAI/Gemini/Claude/Codex-compatible API endpoints, with OAuth login, multi-account routing, streaming, tools, images, and Amp CLI support.
key_quote: “A proxy server that provides OpenAI/Gemini/Claude/Codex compatible API interfaces for CLI.”
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Gemini CLI
- OpenAI Codex
- Claude Code
- Qwen Code
- iFlow
- Amp CLI
- Amp IDE
- OpenRouter
- ChatGPT
- Cursor
- Cline
- RooCode
libraries: []
companies:
- Z.ai
- PackyCode
- AICodeMirror
- BmoPlus
- LingtrueAPI
- Poixe AI
- OpenAI
- Google
- Claude
- Qwen
- GitHub
tags:
- ai-proxy
- api-gateway
- cli-tools
- oauth-authentication
- multi-account-routing
---

### TL;DR
CLIProxyAPI is a Go-based proxy service that turns CLI account access for Gemini, Claude, OpenAI Codex, Qwen, and iFlow into OpenAI/Gemini/Claude/Codex-compatible API endpoints, with OAuth login, multi-account routing, streaming, tools, images, and Amp CLI support.

### Key Quote
“A proxy server that provides OpenAI/Gemini/Claude/Codex compatible API interfaces for CLI.”

### Summary
- **What it is**
  - CLIProxyAPI is a proxy server for CLI-based AI products.
  - It exposes **OpenAI/Gemini/Claude/Codex-compatible API interfaces**.
  - It now supports **OpenAI Codex (GPT models)** and **Claude Code via OAuth**.
  - The goal is to let users access CLI subscriptions/accounts through standard API clients and SDKs.

- **Supported ecosystems / models**
  - Gemini CLI
  - OpenAI Codex / GPT models
  - Claude Code
  - Qwen Code
  - iFlow
  - Amp CLI and Amp IDE extensions
  - OpenAI-compatible upstream providers such as **OpenRouter**
  - Supports **OpenAI Responses API** as part of the OpenAI compatibility claim

- **Core features**
  - Streaming and non-streaming responses
  - Function calling / tools support
  - Multimodal input support for **text and images**
  - Multiple accounts with **round-robin load balancing**
  - Simple CLI authentication flows
  - Generative Language API Key support
  - AI Studio Build multi-account load balancing
  - Multi-account load balancing for Gemini CLI, Claude Code, Qwen Code, iFlow, and OpenAI Codex
  - Reusable **Go SDK** for embedding the proxy

- **Amp CLI integration**
  - Includes support for **Amp CLI** and Amp IDE extensions.
  - Provides provider route aliases like:
    - `/api/provider/{provider}/v1...`
  - For backend-specific request shapes, it recommends using:
    - `/api/provider/{provider}/v1/messages`
    - `/api/provider/{provider}/v1beta/models/...`
    - `/api/provider/{provider}/v1/chat/completions`
  - Notes that route choice does **not** guarantee a distinct executor if model names overlap; backend pinning requires unique aliases/prefixes or avoiding overlapping model names.
  - Emphasizes **localhost-only management endpoints** for security.

- **Documentation and support links**
  - Getting started guide: `https://help.router-for.me/`
  - Management API docs: `MANAGEMENT_API.md` via the help site
  - SDK docs:
    - `docs/sdk-usage.md`
    - `docs/sdk-advanced.md`
    - `docs/sdk-access.md`
    - `docs/sdk-watcher.md`
  - Custom provider example: `examples/custom-provider`

- **Project ecosystem**
  - The README lists multiple projects “based on CLIProxyAPI,” including:
    - vibeproxy
    - Subtitle Translator
    - CCS (Claude Code Switch)
    - Quotio
    - CodMate
    - ProxyPilot
    - Claude Proxy VSCode
    - ZeroLimit
    - CPA-XXX Panel
    - CLIProxyAPI Tray
    - 霖君
    - CLIProxyAPI Dashboard
    - All API Hub
    - Shadow AI
    - ProxyPal
    - CLIProxyAPI Quota Inspector
  - It also lists “more choices” / inspired ports like:
    - 9Router
    - OmniRoute
  - The README invites PRs to add more projects to these lists.

- **Repo posture**
  - Contributing is open via standard fork/branch/PR workflow.
  - Licensed under **MIT**.

- **Notable context / caveats**
  - The README is heavily promotional, with several sponsor blocks and discount/referral offers.
  - The practical value is mostly in the feature list and documentation pointers, not in detailed implementation instructions.
  - The content appears to be a project landing page rather than a deep technical reference.

### Assessment
Durability is **medium** because the architectural idea of proxying CLI AI accounts into compatible API surfaces is broadly reusable, but many specifics here are tied to current products, model names, and OAuth/provider support that may change quickly. Content type is **mixed**, combining project documentation, feature reference, integration notes, and significant sponsor/promotional material. Density is **medium**: the feature lists and Amp routing notes are specific, but much of the page is marketing and ecosystem promotion. Originality is mainly **primary source** for the project’s own capabilities and docs, though the “Who is with us?” / “More choices” sections are largely curated ecosystem listings. Reference style is **refer-back** for setup, endpoint shapes, and supported integrations, with some sections suitable for **deep-study** if embedding the SDK or integrating Amp CLI. Scrape quality is **good** for the README content shown, though it likely omits linked docs, code examples, and any images beyond their captions/alt text.
