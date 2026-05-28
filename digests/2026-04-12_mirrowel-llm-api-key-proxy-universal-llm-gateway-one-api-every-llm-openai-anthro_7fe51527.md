---
url: https://github.com/Mirrowel/LLM-API-Key-Proxy
title: 'Mirrowel/LLM-API-Key-Proxy: Universal LLM Gateway: One API, every LLM. OpenAI/Anthropic-compatible endpoints with multi-provider translation and intelligent load-balancing.'
scraped_at: '2026-04-12T06:49:58Z'
word_count: 3554
raw_file: raw/2026-04-12_mirrowel-llm-api-key-proxy-universal-llm-gateway-one-api-every-llm-openai-anthro_7fe51527.txt
tldr: LLM-API-Key-Proxy is a self-hosted FastAPI gateway that exposes OpenAI- and Anthropic-compatible endpoints and routes provider/model requests across many LLM backends with built-in key rotation, failover, OAuth credential handling, and deployment-friendly tooling (TUI, Docker, cloud/VPS guides).
key_quote: One proxy. Any LLM provider. Zero code changes.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Docker
- Docker Compose
- FastAPI
- Claude Code
- Cursor
- Continue
- JanitorAI
- SillyTavern
- OpenAI SDK
- Anthropic SDK
- curl
- systemd
- Render
- Railway
- Vercel
libraries:
- LiteLLM
- httpx
- asyncio
- rotator_library
- openai
- anthropic
companies:
- OpenAI
- Anthropic
- Google
- NVIDIA
- Cohere
- Mistral
- Groq
- OpenRouter
tags:
- llm-gateway
- api-proxy
- key-rotation
- oauth-credentials
- multi-provider-routing
---

### TL;DR
`LLM-API-Key-Proxy` is a self-hosted FastAPI gateway that exposes OpenAI- and Anthropic-compatible endpoints and routes `provider/model` requests across many LLM backends with built-in key rotation, failover, OAuth credential handling, and deployment-friendly tooling (TUI, Docker, cloud/VPS guides).

### Key Quote
"**One proxy. Any LLM provider. Zero code changes.**"

### Summary
- **Project scope**
  - Two parts:
    1. **API Proxy** (`src/proxy_app`) with universal endpoints like:
       - `POST /v1/chat/completions` (OpenAI format)
       - `POST /v1/messages` (Anthropic format)
    2. **Resilience Library** (`rotator_library`) for key management, retry/failover, cooldowns, and load balancing.
- **Main value proposition**
  - Lets existing OpenAI/Anthropic-compatible tools point to one base URL (`http://127.0.0.1:8000/v1`) and one proxy key (`PROXY_API_KEY`).
  - Supports many providers via LiteLLM plus custom integrations (notably **Antigravity**, **Gemini CLI**, **Qwen Code**, **iFlow**).
  - Requires model naming as `provider/model_name` (e.g., `gemini/gemini-2.5-flash`).
- **Compatibility targets**
  - Explicit examples for Claude Code, OpenAI SDK, Anthropic SDK, curl, Cursor/Continue, JanitorAI/SillyTavern.
  - Anthropic-compatible endpoint allows Claude Code clients to use non-Anthropic providers.
- **Install/run options**
  - Prebuilt binaries (Windows/macOS/Linux), source install, Docker image (`ghcr.io/mirrowel/llm-api-key-proxy:latest`), Docker Compose.
  - Important Docker gotcha: **create `key_usage.json` first** or Docker may create a directory and break startup.
- **Credential management**
  - Interactive TUI and CLI tool: `python -m rotator_library.credential_tool`.
  - Supports API keys and OAuth flows; stores in `.env` and `oauth_creds/`.
  - Stateless deployment path: export OAuth creds to env vars + `SKIP_OAUTH_INIT_CHECK=true`.
- **Resilience/HA behavior**
  - Async (`asyncio`, `httpx`), global timeout + retries, key rotation, model-aware cooldowns (10→30→60→120s), lockouts for failing keys, daily resets, streaming error handling.
  - Per-provider controls: concurrency limits, rotation mode (`balanced` vs `sequential`), model whitelist/blacklist, quota groups, weighted/randomized rotation.
- **Operational/debugging features**
  - Optional deep request logging (`--enable-request-logging`) with request/response/chunk/metadata artifacts under `logs/detailed_logs/`.
  - Extra endpoints: `/v1/models`, `/v1/providers`, `/v1/token-count`, `/v1/cost-estimate`, and model metadata options (`?enriched=false`).
- **Provider-specific notes**
  - Rich specialized behavior for Gemini CLI and Antigravity (quota grouping, tier handling, thinking/tooling features), plus Qwen/iFlow dual-auth and schema cleaning.
- **Deployment docs**
  - Includes guidance for Render/Railway/Vercel, Docker, and systemd VPS.
- **Licensing**
  - Dual license:
    - Proxy app: **MIT**
    - Resilience library: **LGPL-3.0**

### Assessment
This is **mixed content** (reference + tutorial + project announcement) with **high density** and strong practical specificity (commands, env vars, endpoint table, deployment caveats). **Durability is medium**: architectural concepts and usage patterns are stable, but provider/model names, OAuth details, and integration behaviors will age with upstream API changes. It appears to be a **primary source** (project README by maintainers), making it authoritative for intended behavior but still needing validation against current releases. It is best used as a **refer-back** document rather than skim-once, especially for env configuration and provider quirks. **Scrape quality is good**: core content, code snippets, tables, and cautions are present; only missing elements are noted TODO screenshots, which do not block comprehension.
