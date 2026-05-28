---
url: https://github.com/badrisnarayanan/antigravity-claude-proxy
title: 'badrisnarayanan/antigravity-claude-proxy: Proxy that exposes Antigravity provided claude / gemini models, so we can use them in Claude Code'
scraped_at: '2026-04-12T07:28:31Z'
word_count: 1281
raw_file: raw/2026-04-12_badrisnarayanan-antigravity-claude-proxy-proxy-that-exposes-antigravity-provided_9cda8d0c.txt
tldr: A Node.js proxy that converts Claude Code’s Anthropic API requests into Antigravity-backed Google AI calls, enabling Claude and Gemini models in Claude Code/OpenClaw—but with explicit warnings that it may violate Google’s ToS and has reportedly triggered account bans.
key_quote: Using this proxy may violate Google's Terms of Service. A small number of users have reported their Google accounts being **banned** or **shadow-banned** (restricted access without explicit notification).
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- badrisnarayanan
- NoeFabris
- 1rgs
tools:
- antigravity-claude-proxy
- Claude Code CLI
- OpenClaw
- ClawdBot
- npx
- npm
- systemd
libraries: []
companies:
- Google
- Anthropic
tags:
- proxy-server
- claude-code
- google-generative-ai
- oauth
- model-routing
---

### TL;DR
A Node.js proxy that converts Claude Code’s Anthropic API requests into Antigravity-backed Google AI calls, enabling Claude and Gemini models in Claude Code/OpenClaw—but with explicit warnings that it may violate Google’s ToS and has reportedly triggered account bans.

### Key Quote
“Using this proxy may violate Google's Terms of Service. A small number of users have reported their Google accounts being **banned** or **shadow-banned** (restricted access without explicit notification).”

### Summary
- **What it is**
  - `antigravity-claude-proxy` is a proxy server exposing an **Anthropic-compatible API**.
  - It is backed by **Antigravity’s Cloud Code** and acts as a bridge from Claude Code to Google-hosted model access.
  - Supports use with **Claude Code CLI** and **OpenClaw / ClawdBot**.

- **Core workflow**
  - Accepts requests in **Anthropic Messages API** format.
  - Uses OAuth tokens from added Google accounts or Antigravity’s local database.
  - Converts requests into **Google Generative AI format** with Cloud Code wrapping.
  - Sends them to Antigravity’s Cloud Code API at `daily-cloudcode-pa.sandbox.googleapis.com`.
  - Converts responses back to **Anthropic format**, including **full thinking/streaming support**.

- **Major warning**
  - The README prominently warns that Google has been issuing **ToS violation bans** for accounts tied to the proxy.
  - It recommends using a **burner account**, not a main account.
  - The project is explicitly described as **unofficial** and not endorsed by Google.

- **Requirements**
  - **Node.js 18+**
  - Either:
    - **Antigravity installed** for single-account mode, or
    - **Google account(s)** for multi-account mode

- **Installation options**
  - **npx**:
    - `npx antigravity-claude-proxy@latest start`
  - **Global install**:
    - `npm install -g antigravity-claude-proxy@latest`
    - `antigravity-claude-proxy start`
  - **Clone and run**:
    - `git clone https://github.com/badri-s2001/antigravity-claude-proxy.git`
    - `npm install`
    - `npm start`

- **Running the proxy**
  - Default local endpoint: `http://localhost:8080`
  - Runs as a **background process** and survives terminal closure.
  - CLI commands listed:
    - `acc start`
    - `acc stop`
    - `acc restart`
    - `acc status`
    - `acc ui`
    - `acc start --log`

- **Account linking**
  - Three setup methods:
    - **Web dashboard** at `http://localhost:8080` → **Accounts** tab → **Add Account**
    - **CLI**:
      - `antigravity-claude-proxy accounts add`
      - `antigravity-claude-proxy accounts add --no-browser`
    - **Automatic mode** for users already logged into the Antigravity app
  - Supports **manual authorization** for headless/remote environments.

- **Verification**
  - Health check:
    - `curl http://localhost:8080/health`
  - Account/quota inspection:
    - `curl "http://localhost:8080/account-limits?format=table"`

- **Claude Code configuration**
  - Can be configured via:
    - **Web Console** → **Settings** → **Claude CLI**
    - **Manual settings.json**
    - **Shell environment variables**
  - Example Claude settings point Claude Code to:
    - `ANTHROPIC_BASE_URL=http://localhost:8080`
    - `ANTHROPIC_AUTH_TOKEN=test`
  - The README provides two model presets:
    - **Claude models** like `claude-opus-4-6-thinking`
    - **Gemini models** like `gemini-3.1-pro-high[1m]` and `gemini-3-flash[1m]`
  - Mentions `ENABLE_EXPERIMENTAL_MCP_CLI=true`

- **Proxy Mode vs Paid Mode**
  - **Proxy Mode**
    - Backend: local Antigravity server
    - Cost: free (Google Cloud)
    - Models: Claude + Gemini
  - **Paid Mode**
    - Backend: official Anthropic credits
    - Cost: paid
    - Models: Claude only
  - The web UI can switch between modes and apply settings to Claude Code.

- **Running multiple Claude Code instances**
  - Suggests using separate config directories and an alias/function:
    - macOS/Linux: `claude-antigravity`
    - Windows PowerShell function
  - Lets users keep the official Claude Code and proxy-based version side by side.

- **Systemd note**
  - If run as a service, the proxy may not find Claude settings under the service user.
  - Recommends setting `CLAUDE_CONFIG_PATH=/home/youruser/.claude`
  - Important for WebUI access to Claude CLI configuration.

- **Documentation links included**
  - Available models
  - Multi-account load balancing
  - Web management console
  - Advanced configuration
  - Menu bar app
  - OpenClaw / ClawdBot integration
  - API endpoints
  - Testing
  - Troubleshooting
  - Safety notices
  - Legal
  - Development

- **Project provenance**
  - Credits mention inspiration/code from:
    - `opencode-antigravity-auth`
    - `claude-code-proxy`
  - License: **MIT**

### Assessment
This is a **mixed reference/tutorial** README with a strong operational focus: it explains what the proxy does, how to install and configure it, and how to use it with Claude Code. **Durability is medium** because the setup steps and architecture may remain useful, but the specific model names, endpoints, and account-behavior warnings are likely to change as Google/Anthropic/Antigravity update their systems. **Density is high**: it includes concrete commands, config files, model presets, environment variables, and service notes. **Originality is mostly synthesis** rather than primary research, since it documents a tool and its usage rather than presenting novel findings. This is best treated as a **refer-back** reference if you plan to run the proxy; it is not a skim-once read because the setup details matter. **Scrape quality is good** overall: the main README content, code blocks, and warnings are present, though linked docs, images, and any deeper implementation details are not included here.
