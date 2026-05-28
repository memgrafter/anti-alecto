---
url: https://developers.cloudflare.com/agents/guides/remote-mcp-server/
title: Build a Remote MCP server · Cloudflare Agents docs
scraped_at: '2026-04-12T09:44:55Z'
word_count: 1608
raw_file: raw/2026-04-12_build-a-remote-mcp-server-cloudflare-agents-docs_50b1a1e3.txt
tldr: Cloudflare’s guide shows how to build and deploy a remote MCP server using Streamable HTTP, starting with a public authless server and then optionally adding OAuth-based authentication and authorization.
key_quote: createMcpHandler() is the fastest way to get a stateless MCP server running.
durability: high
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- npm
- yarn
- pnpm
- MCP Inspector
- mcp-remote
- Wrangler
libraries:
- '@modelcontextprotocol/sdk'
companies:
- Cloudflare
- GitHub
- Google
- Slack
- Stytch
- Auth0
- WorkOS
tags:
- remote-mcp
- cloudflare-agents
- oauth
- authentication
- deployment
---

### TL;DR
Cloudflare’s guide shows how to build and deploy a remote MCP server using Streamable HTTP, starting with a public authless server and then optionally adding OAuth-based authentication and authorization.

### Key Quote
“createMcpHandler() is the fastest way to get a stateless MCP server running.”

### Summary
- The guide explains how to deploy a **remote MCP server on Cloudflare** using **Streamable HTTP transport**, which it describes as the **current MCP specification standard**.
- It presents **two access models**:
  - **Without authentication**: anyone can connect and use the server.
  - **With authentication and authorization**: users must sign in, and tool access can be scoped by permissions.
- It compares three Agents SDK approaches for building MCP servers:
  - **`createMcpHandler()`** — stateless, no Durable Objects, simplest setup, best for tools that do not need per-session state.
  - **`McpAgent`** — stateful, requires Durable Objects, supports per-session state, elicitation, and both **SSE** and **Streamable HTTP** transports.
  - **Raw `WebStandardStreamableHTTPServerTransport`** — no SDK dependency, full control.
- The guide recommends a practical path:
  - first deploy a **public MCP server**,
  - then add **authentication and scoped authorization** later if needed.
- For the **authless example**, it walks through:
  - creating a new project with `npm`, `yarn`, or `pnpm` using the Cloudflare template:
    - `cloudflare/ai/demos/remote-mcp-authless`
  - choosing setup options like **No** for AGENTS.md, **No** for git, and **No** for initial deployment,
  - running the local development server,
  - using the **MCP Inspector** to connect to the local endpoint (example given: `http://localhost:8788/mcp`),
  - deploying to a `*.workers.dev` URL (example: `https://remote-mcp-server-authless.your-account.workers.dev/mcp`),
  - testing the deployed server with the Inspector,
  - optionally using **`mcp-remote`** as a local proxy so clients like **Claude Desktop** can connect even if they don’t support remote transport or client-side auth.
- For **authentication**, it explains two options:
  - **Cloudflare Access** as an identity aggregator that checks things like email, upstream identity providers, IP address, and device certificates.
  - **Any OAuth 2.0 provider** such as **GitHub, Google, Slack, Stytch, Auth0, WorkOS**, etc.
- It gives a **GitHub OAuth example**:
  - create a project from `cloudflare/ai/demos/remote-mcp-github-oauth`,
  - note that `src/index.ts` uses `GitHubHandler` as the `defaultHandler`,
  - create **two GitHub OAuth Apps**:
    - one for **local development**,
    - one for **production**,
  - configure local app URLs like `http://localhost:8788` and `http://localhost:8788/callback`,
  - store `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` in a `.env` file for local use,
  - run the local server and use the **MCP Inspector’s Quick OAuth Flow** to authenticate,
  - for production, set the OAuth app homepage and callback URLs to the deployed `workers.dev` domain and `/callback`,
  - set production secrets with **Wrangler** and configure a **KV namespace** in `wrangler.jsonc`,
  - deploy to `workers.dev` and connect through AI Playground, MCP Inspector, or another MCP client.
- Overall, the document is a **practical deployment guide**: it covers both the **hello-world path** (public server) and the **secure path** (OAuth/Access-based server), with concrete commands and testing steps.

### Assessment
This is a **tutorial/reference** with medium-to-high durability: the concepts of remote MCP servers, authless vs authenticated access, and OAuth integration should remain relevant, but the exact commands, templates, ports, and Cloudflare-specific workflow may change over time. The content is highly actionable and fairly dense, especially in the command and setup sections, and it is primarily a **primary-source docs page** rather than commentary or synthesis. It’s best used as a **refer-back** guide when setting up or troubleshooting a Cloudflare MCP server, not as a one-time skim. Scrape quality is **partial**: the text captures most of the guide’s flow and commands, but formatting is flattened and some section structure, code-block clarity, and UI details appear missing or merged together.
