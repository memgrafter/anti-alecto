---
url: https://github.com/Soju06/codex-lb
title: 'Soju06/codex-lb: Codex/ChatGPT account load balancer & proxy with usage tracking, dashboard, and OpenCode-compatible endpoints'
scraped_at: '2026-04-19T06:48:49Z'
word_count: 2357
raw_file: raw/2026-04-19_soju06-codex-lb-codex-chatgpt-account-load-balancer-proxy-with-usage-tracking-da_0af0609a.txt
tldr: codex-lb is a self-hosted proxy/load balancer for multiple ChatGPT/Codex accounts that adds usage tracking, API-key management, a dashboard, and OpenAI-compatible endpoints for clients like Codex CLI, OpenCode, and the Python SDK.
key_quote: Pool multiple accounts, track usage, manage API keys, view everything in a dashboard.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Soju06
- Jonas Kamsker
- Quack
- Jill Kok
- San Mou
- PARK CHANYOUNG
- Choi138
- LYA⚚CAP⚚OCEAN
- Eugene Korekin
- jordan
- DOCaCola
- JoeBlack2k
- Peter A.
- Hannah Markfort
- mws-weekend-projects
- Quang Do
- Anand Aiyer
- defin85
- Jacky Fong
- flokosti96
- Woonggi Min
- Yigit Konur
- Ruben
- Steve Santacroce
- Hugh Do
- Hubert Salwin
- Teemu Koskinen
- Yu Peng Zheng
- embogomolov
- Renat Sharipov
- Liu Rui
- OverHash
- Kazet
tools:
- Codex CLI
- OpenCode
- OpenClaw
- OpenAI Python SDK
- FastAPI
- Docker
- uvx
- bun
- Helm
- Authelia
- TOTP
libraries:
- openai
companies:
- OpenAI
- GitHub
- GHCR
tags:
- load-balancing
- proxy
- usage-tracking
- openai-compatible
- self-hosting
---

### TL;DR
`codex-lb` is a self-hosted proxy/load balancer for multiple ChatGPT/Codex accounts that adds usage tracking, API-key management, a dashboard, and OpenAI-compatible endpoints for clients like Codex CLI, OpenCode, and the Python SDK.

### Key Quote
“Pool multiple accounts, track usage, manage API keys, view everything in a dashboard.”

### Summary
- **What it is**
  - A Python/FastAPI-based service that balances requests across a pool of ChatGPT accounts.
  - Exposes OpenAI-compatible endpoints, including:
    - `http://127.0.0.1:2455/v1`
    - `http://127.0.0.1:2455/backend-api/codex`
  - Targets tools such as **Codex CLI**, **OpenCode**, **OpenClaw**, and the **OpenAI Python SDK**.

- **Core features**
  - **Account pooling**: load-balances across multiple ChatGPT accounts.
  - **Usage tracking**: per-account tokens, cost, and 28-day trends.
  - **API keys**: dashboard-managed keys with rate limits by:
    - tokens
    - cost
    - time window
    - model
  - **Dashboard auth**: password plus optional TOTP.
  - **OpenAI-compatible**: works with standard OpenAI clients.
  - **Auto model sync**: upstream model list is fetched automatically.

- **Quick start**
  - Recommended Docker run:
    ```bash
    docker volume create codex-lb-data
    docker run -d --name codex-lb \
      -p 2455:2455 -p 1455:1455 \
      -v codex-lb-data:/var/lib/codex-lb \
      ghcr.io/soju06/codex-lb:latest
    ```
  - Alternative launch:
    ```bash
    uvx codex-lb
    ```
  - Basic flow: open `localhost:2455` → add account → done.

- **Bootstrap / remote setup**
  - First-time remote dashboard access requires a **bootstrap token** to set the initial password.
  - Default behavior:
    - server generates a one-time token on first startup
    - token is printed in logs via `docker logs codex-lb`
  - Manual token can be set with:
    ```bash
    CODEX_LB_DASHBOARD_BOOTSTRAP_TOKEN=your-secret-token
    ```
  - Localhost access bypasses bootstrap entirely.
  - In multi-replica setups, replicas must share the same encryption key for restart recovery.

- **Client setup examples**
  - **Codex CLI / IDE extension**
    - Use `base_url = "http://127.0.0.1:2455/backend-api/codex"`
    - `wire_api = "responses"`
    - `requires_openai_auth = true`
    - Optional env auth via `CODEX_LB_API_KEY`
    - Can enable upstream websocket transport with:
      ```bash
      export CODEX_LB_UPSTREAM_STREAM_TRANSPORT=websocket
      ```
  - **OpenCode**
    - The README warns to use the built-in `openai` provider with a `baseURL` override, not a custom provider, because custom providers drop reasoning/thinking content.
    - Uses Responses API path and preserves reasoning state.
  - **OpenClaw**
    - Configures a `codex-lb` provider pointing at `/v1`
    - Uses `api: "openai-responses"`
  - **OpenAI Python SDK**
    - Example:
      ```python
      from openai import OpenAI

      client = OpenAI(
          base_url="http://127.0.0.1:2455/v1",
          api_key="sk-clb-...",
      )
      response = client.chat.completions.create(...)
      ```

- **API key authentication**
  - Disabled by default.
  - When enabled, clients must send:
    ```http
    Authorization: Bearer sk-clb-...
    ```
  - Protected routes include:
    - `/v1/*` except `/v1/usage`
    - `/backend-api/codex/*`
    - `/backend-api/transcribe`
  - API keys can have:
    - expiration
    - model restrictions
    - token/cost rate limits per day/week/month

- **Configuration**
  - Uses environment variables prefixed with `CODEX_LB_` or `.env.local`.
  - SQLite is the default backend.
  - PostgreSQL is optional via `CODEX_LB_DATABASE_URL`.

- **Dashboard auth modes**
  - `standard`: built-in password + optional TOTP
  - `trusted_header`: trusts a reverse-proxy header like `Remote-User` from approved proxy CIDRs
  - `disabled`: no dashboard auth, intended only behind external protections
  - Example trusted-header env vars:
    ```bash
    CODEX_LB_FIREWALL_TRUST_PROXY_HEADERS=true
    CODEX_LB_FIREWALL_TRUSTED_PROXY_CIDRS=172.18.0.0/16
    CODEX_LB_DASHBOARD_AUTH_PROXY_HEADER=Remote-User
    ```

- **Docker and Kubernetes**
  - Docker examples are given for:
    - trusted-header auth with Authelia
    - fully disabled dashboard auth
  - Helm install example:
    ```bash
    helm install codex-lb oci://ghcr.io/soju06/charts/codex-lb \
      --set postgresql.auth.password=changeme \
      --set config.databaseMigrateOnStartup=true \
      --set migration.schemaGate.enabled=false
    ```
  - The Helm chart handles multi-replica `/responses` owner handoff and mentions `cluster.local` as the default cluster domain.

- **Data and persistence**
  - Local/uvx data directory: `~/.codex-lb/`
  - Docker data directory: `/var/lib/codex-lb/`
  - README explicitly says to back up this directory to preserve data.

- **Development**
  - Backend:
    ```bash
    uv run fastapi run app/main.py --reload
    ```
  - Frontend:
    ```bash
    cd frontend && bun run dev
    ```
  - Docker dev workflow:
    ```bash
    docker compose watch
    ```

- **Project maturity / maintainability signals**
  - The repo includes detailed setup guidance, multiple client integrations, Kubernetes support, and contributor credits.
  - It appears actively maintained and aimed at real self-hosted deployment use, not just a demo.

### Assessment
Durability is **medium**: the architectural ideas—self-hosted account pooling, usage tracking, auth modes, and OpenAI-compatible proxying—are broadly reusable, but the exact client configs, endpoints, model names, bootstrap behavior, and environment variables are tied to this project’s current implementation and upstream OpenAI/Codex/OpenCode conventions. Content type is **mixed**: primarily a **reference/tutorial** README with some product-style positioning. Density is **high**, because it packs installation, configuration, client integration, Kubernetes, and operational details into one document. Originality is **primary source** for the project’s own behavior and setup, though some client guidance is necessarily ecosystem-specific. Reference style is **refer-back**: this is the kind of README you’d revisit when installing, configuring, or debugging deployments. Scrape quality is **good**: the README content appears largely complete, including code blocks, tables, and most major sections; screenshots are referenced but not visually available in the text, which is expected.
