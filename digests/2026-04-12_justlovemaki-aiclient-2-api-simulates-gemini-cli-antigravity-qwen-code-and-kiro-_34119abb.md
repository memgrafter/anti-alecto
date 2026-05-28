---
url: https://github.com/justlovemaki/AIClient-2-API
title: 'justlovemaki/AIClient-2-API: Simulates Gemini CLI, Antigravity, Qwen Code, and Kiro client requests, compatible with the OpenAI API. It supports thousands of Gemini model requests per day and offers free use of the built-in Claude model in Kiro. Easily connect to any client via the API, making AI development more efficient!'
scraped_at: '2026-04-12T10:42:15Z'
word_count: 5209
raw_file: raw/2026-04-12_justlovemaki-aiclient-2-api-simulates-gemini-cli-antigravity-qwen-code-and-kiro-_34119abb.txt
tldr: AIClient-2-API is a Node.js/OpenAI-compatible proxy that translates client-only AI auth flows and protocols (Gemini CLI, Antigravity, Codex, Grok, Kiro, Qwen) into a local API with account pooling, failover, Web UI management, and Docker support.
key_quote: A powerful proxy that can unify the requests of various client-only large model APIs (Gemini CLI, Antigravity, Codex, Grok, Kiro ...), simulate requests, and encapsulate them into a local OpenAI-compatible interface.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Ruan Yifeng
tools:
- Cherry-Studio
- NextChat
- Cline
- Docker
- Google Cloud Console
libraries: []
companies:
- Google
- OpenAI
- Anthropic
- Alibaba
- xAI
tags:
- ai-proxy
- openai-compatible
- api-gateway
- docker
- oauth-authentication
---

### TL;DR
AIClient-2-API is a Node.js/OpenAI-compatible proxy that translates client-only AI auth flows and protocols (Gemini CLI, Antigravity, Codex, Grok, Kiro, Qwen) into a local API with account pooling, failover, Web UI management, and Docker support.

### Key Quote
"**A powerful proxy that can unify the requests of various client-only large model APIs (Gemini CLI, Antigravity, Codex, Grok, Kiro ...), simulate requests, and encapsulate them into a local OpenAI-compatible interface.**"

### Summary
- **What it is**
  - A local API proxy service called **AIClient2API / AIClient-2-API**
  - Built on **Node.js ≥20**
  - Exposes an **OpenAI-compatible interface** while internally simulating/bridging multiple client-only protocols
  - Targets tools like **Cherry-Studio, NextChat, and Cline**

- **What it supports**
  - Protocols/models mentioned in the README:
    - **Gemini CLI**
    - **Antigravity**
    - **Codex**
    - **Grok**
    - **Kiro**
    - **Qwen Code**
  - Protocol conversion among **OpenAI, Claude, and Gemini**
  - Multimodal input such as **images and documents**
  - Latest model examples called out:
    - **Grok 3 / Grok 4**
    - **Claude 4.5 Opus**
    - **Gemini 3 Pro**
    - **Qwen3 Coder Plus**
    - **Kimi K2 / MiniMax M2**

- **Core architecture and features**
  - Uses **strategy + adapter patterns**
  - Includes:
    - **account pool management**
    - **intelligent polling**
    - **automatic failover**
    - **health checks**
  - Claims **99.9% service availability**
  - Says new providers can be added in **3 steps**
  - Mentions **90%+ integration/unit test coverage**

- **Web UI**
  - A browser-based management console at **http://localhost:3000**
  - Lets users:
    - configure providers in real time
    - upload OAuth/credential files
    - monitor provider health
    - view logs
    - test APIs
    - switch themes
  - Default login password is **`admin123`**
  - Config changes are intended to take effect immediately

- **Installation / quick start**
  - Recommended Docker run example:
    - maps **3000** for Web UI
    - maps OAuth callback ports:
      - **8085** Gemini
      - **8086** Antigravity
      - **1455** Codex
      - **19876–19880** Kiro
  - Docker Compose is also supported
  - Non-Docker users can run:
    - `npm install`
    - `npm start`
  - Optional TLS sidecar for bypassing fingerprint-based blocks requires **Go 1.20+** and building:
    - `cd tls-sidecar && go build -o tls-sidecar && cd ..`

- **Authorization / credential handling**
  - Credentials are stored under standard local paths, e.g.:
    - Gemini: `~/.gemini/oauth_creds.json`
    - Kiro: `~/.aws/sso/cache/kiro-auth-token.json`
    - Qwen: `~/.qwen/oauth_creds.json`
    - Antigravity: `~/.antigravity/oauth_creds.json`
    - Codex: `~/.codex/oauth_creds.json`
  - Supports generating auth through the Web UI
  - Includes provider-specific notes:
    - **Gemini**: Google Cloud project/OAuth setup
    - **Antigravity**: personal/pro/org account caveats
    - **Qwen**: browser-based OAuth, recommends `temperature: 0`, `top_p: 1`
    - **Kiro**: requires Kiro client login and token file
    - **Codex**: OAuth callback port **1455**
    - **Grok**: cookie/SSO token from browser devtools

- **Advanced configuration**
  - Proxy support:
    - unified proxy
    - provider-specific proxy endpoints
    - supports **HTTP, HTTPS, SOCKS5**
  - Model filtering via `notSupportedModels`
  - Cross-type fallback via `providerFallbackChain`
  - TLS Sidecar for Grok/Cloudflare-style 403 bypass using Go uTLS and Chrome-like TLS fingerprints

- **FAQ coverage**
  - Troubleshooting for:
    - OAuth failures
    - port conflicts
    - Docker startup issues
    - invalid credentials
    - 429 rate limits
    - unavailable models
    - UI access issues
    - streaming interruptions
    - config changes not applying
    - 404s from wrong endpoint paths
    - missing/invalid API keys
    - unhealthy provider pools
    - 403 Forbidden errors

- **Maintenance / metadata**
  - License: **GPLv3**
  - Acknowledges inspiration from **Google Gemini CLI** and code from **Cline 3.18.0**
  - Includes sponsor promotions and referral links
  - The version log contains future-dated entries up through **2026.03.02**, which is a strong freshness/credibility flag to verify carefully

### Assessment
Durability is **medium**: the architectural ideas (proxying, OpenAI-compatible adapters, pool failover) are reusable, but much of the practical guidance is tied to specific provider behaviors, ports, auth flows, and rapidly changing model/version names. Content type is **mixed**, leaning heavily toward **tutorial/reference** with some promotional and announcement-style sections. Density is **high** because it packs installation steps, config keys, endpoints, troubleshooting, and provider-specific instructions into one README. Originality is mostly a **primary source** project README, though it also includes promotional sponsor copy and references to external tools/projects. Reference style is **refer-back** for setup, config, and troubleshooting, with some sections suitable for **skim-once** if you only need the project pitch. Scrape quality is **good** overall: the README structure, commands, configs, FAQ, and notes are present, though embedded images and linked docs are not directly inspectable here, and the future-dated changelog entries should be treated with caution when judging current relevance.
