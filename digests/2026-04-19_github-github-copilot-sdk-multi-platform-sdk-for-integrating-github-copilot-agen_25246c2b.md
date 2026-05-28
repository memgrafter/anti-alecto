---
url: https://github.com/github/copilot-sdk
title: 'GitHub - github/copilot-sdk: Multi-platform SDK for integrating GitHub Copilot Agent into apps and services · GitHub'
scraped_at: '2026-04-19T07:34:09Z'
word_count: 1052
raw_file: raw/2026-04-19_github-github-copilot-sdk-multi-platform-sdk-for-integrating-github-copilot-agen_25246c2b.txt
tldr: GitHub’s Copilot SDK is a public-preview, multi-language SDK that lets apps embed Copilot CLI’s agent runtime via JSON-RPC, with support for GitHub auth or BYOK across Node.js, Python, Go, .NET, and Java.
key_quote: “Embed Copilot's agentic workflows in your application—now available in public preview as a programmable SDK for Python, TypeScript, Go, .NET, and Java.”
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Copilot CLI
- JSON-RPC
libraries:
- '@github/copilot-sdk'
- github-copilot-sdk
- GitHub.Copilot.SDK
- copilot-sdk-java
companies:
- GitHub
- OpenAI
- Azure AI Foundry
- Anthropic
tags:
- developer-tools
- artificial-intelligence
- sdk
- authentication
- api-integration
---

### TL;DR
GitHub’s Copilot SDK is a public-preview, multi-language SDK that lets apps embed Copilot CLI’s agent runtime via JSON-RPC, with support for GitHub auth or BYOK across Node.js, Python, Go, .NET, and Java.

### Key Quote
“Embed Copilot's agentic workflows in your application—now available in public preview as a programmable SDK for Python, TypeScript, Go, .NET, and Java.”

### Summary
- This repository is the main landing page for the **GitHub Copilot CLI SDKs**.
- It presents the SDK as a way to embed **Copilot’s agentic workflows** into applications and services.
- The SDK uses the same runtime behind **Copilot CLI**, exposing:
  - planning
  - tool invocation
  - file edits
  - process lifecycle management
- Supported SDKs and install commands:
  - **Node.js / TypeScript**: `npm install @github/copilot-sdk`
  - **Python**: `pip install github-copilot-sdk`
  - **Go**: `go get github.com/github/copilot-sdk/go`
  - **.NET**: `dotnet add package GitHub.Copilot.SDK`
  - **Java**: Maven coordinate `com.github:copilot-sdk-java` via the separate `github/copilot-sdk-java` repo
- Architecture:
  - Application → SDK client → Copilot CLI in **server mode**
  - Communication happens over **JSON-RPC**
  - The SDK automatically manages the CLI process, but can also connect to an **external CLI server**
- Getting started flow:
  1. Optionally install Copilot CLI
     - bundled automatically for **Node.js, Python, .NET**
     - **Go** may require manual CLI installation or `copilot` on PATH
  2. Install the preferred SDK
  3. Read the language-specific README for examples and API docs
- Authentication options include:
  - GitHub signed-in user via stored OAuth credentials
  - OAuth GitHub App tokens
  - environment variables: `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN`
  - **BYOK** using provider keys from OpenAI, Azure AI Foundry, Anthropic, etc.
- Important BYOK caveat:
  - only **key-based authentication**
  - **Microsoft Entra ID**, managed identities, and third-party identity providers are **not supported**
- Billing:
  - follows the Copilot CLI model
  - each prompt counts toward **premium request quota**
- Default tool behavior:
  - SDK runs as if `--allow-all` were passed
  - first-party tools like file system, Git, and web requests are enabled by default
  - tools can be customized per client configuration
- The SDK supports:
  - custom agents
  - skills
  - tools
  - runtime model discovery
- Status:
  - **Public Preview**
  - functional for development/testing, but not yet recommended as fully production-ready
- Documentation links provided for:
  - getting started
  - setup/deployment/scaling
  - auth
  - features
  - troubleshooting
  - cookbook examples
  - community resources
- The repo also lists **unofficial community-maintained SDKs** for Rust, Clojure, and C++ with a warning that they are not supported by GitHub.

### Assessment
This is a high-level reference/landing page for a currently evolving developer product, so durability is **medium**: the core architecture and concepts may last, but installation commands, supported languages, preview status, billing, and auth details are version- and product-state-dependent. The content type is **mixed**—part reference, part announcement, part tutorial. Density is **medium**: it contains many concrete product facts, but most details are summarized rather than deeply explained. It is primarily a **primary source** because it is the official repository README, not third-party commentary. It’s best used as **refer-back** material for installation, supported languages, auth options, and basic architecture. Scrape quality is **good** overall: the main README content, tables, and FAQ were captured, though deeper linked docs, code examples, and images are not included here.
