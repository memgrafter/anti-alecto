---
url: https://github.com/vercel-labs/agent-browser
title: 'vercel-labs/agent-browser: Browser automation CLI for AI agents'
scraped_at: '2026-04-12T07:29:17Z'
word_count: 6976
raw_file: raw/2026-04-12_vercel-labs-agent-browser-browser-automation-cli-for-ai-agents_1ceb56a3.txt
tldr: agent-browser is a fast native Rust CLI for browser automation aimed at AI agents, with ref-based snapshots, rich CLI commands, session/auth persistence, debugging tools, and support for local, CDP, cloud, and iOS browser backends.
key_quote: Browser automation CLI for AI agents. Fast native Rust CLI.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- agent-browser
- chrome
- chromium
- playwright
- puppeteer
- appium
- xcode
- browserless
- browserbase
- browser-use
- kernel
- aws-bedrock-agentcore
- vercel-ai-gateway
libraries:
- '@vercel/sandbox'
- '@sparticuz/chromium'
- '@vercel/ai'
companies:
- Vercel
- Browserless
- Browserbase
- Browser Use
- Kernel
- AWS
- Chrome
tags:
- browser-automation
- cli-tools
- ai-agents
- web-testing
- rust
---

### TL;DR
`agent-browser` is a fast native Rust CLI for browser automation aimed at AI agents, with ref-based snapshots, rich CLI commands, session/auth persistence, debugging tools, and support for local, CDP, cloud, and iOS browser backends.

### Key Quote
"Browser automation CLI for AI agents. Fast native Rust CLI."

### Summary
- **What it is**
  - A browser automation command-line tool for AI agents, implemented as a **native Rust CLI**.
  - Designed to control browsers through a background **client-daemon architecture** for fast repeated commands.

- **Installation options**
  - `npm install -g agent-browser` then `agent-browser install`
  - `npm install agent-browser` for project-local usage
  - `brew install agent-browser` on macOS
  - `cargo install agent-browser`
  - Build from source with `pnpm install`, `pnpm build`, and `pnpm build:native`
  - On Linux, install dependencies with `agent-browser install --with-deps`
  - Upgrade with `agent-browser upgrade`

- **Core requirements**
  - **Chrome** is required; `agent-browser install` downloads Chrome from **Chrome for Testing**.
  - Existing Chrome, Brave, Playwright, and Puppeteer installs are detected automatically.
  - **Rust** is only needed when building from source.

- **Basic workflow**
  - Open a page: `agent-browser open example.com`
  - Capture an accessibility snapshot with refs: `agent-browser snapshot`
  - Interact using refs: `click @e2`, `fill @e3 "test@example.com"`, `get text @e1`
  - Take screenshots and close sessions as needed

- **Command surface**
  - Navigation: `open`, `back`, `forward`, `reload`
  - Interaction: `click`, `dblclick`, `type`, `fill`, `press`, `hover`, `select`, `check`, `uncheck`, `drag`, `upload`
  - Keyboard/mouse control, scrolling, tab/window management, frames, dialogs
  - Information retrieval: text, HTML, values, attributes, title, URL, styles, bounding boxes
  - Wait commands for selectors, text, URLs, load states, or JS conditions
  - Batch execution for multi-step workflows
  - Clipboard, network routing/HAR capture, tracing, profiling, console/errors, highlights, DevTools
  - Diffing for snapshots, screenshots, and URLs
  - AI chat mode: `agent-browser chat`

- **Selector model**
  - Refs from `snapshot` are the recommended AI-friendly locator system.
  - Also supports CSS selectors, text/XPath, and semantic locators (`find role`, `find label`, etc.).

- **Authentication and persistence**
  - Supports multiple auth persistence strategies:
    - Chrome profile reuse via `--profile`
    - Persistent custom profiles
    - Session persistence via `--session-name`
    - Importing auth from a running browser via `--auto-connect`
    - Loading state files via `--state`
    - An encrypted auth vault via `auth save` / `auth login`
  - State files can be encrypted with `AGENT_BROWSER_ENCRYPTION_KEY` using AES-256-GCM.
  - Session state defaults to auto-expiring after a configurable number of days.

- **Security features**
  - Content boundary markers for safer LLM handling of page output
  - Domain allowlists
  - Action policies and action confirmation prompts
  - Output truncation to avoid context flooding
  - Notes that state files contain tokens in plaintext unless encryption is enabled

- **Snapshots and annotated screenshots**
  - `snapshot` can be filtered for interactive elements, URLs, compactness, depth, and scope.
  - `screenshot --annotate` overlays numbered labels on interactive elements, where labels map to refs like `@e1`.
  - Annotated screenshots are supported on CDP-backed browser paths, not Safari/WebDriver.

- **Configuration**
  - Defaults can be set in `~/.agent-browser/config.json` or `./agent-browser.json`
  - Environment variables override config files; CLI flags override everything
  - Config keys use camelCase equivalents of CLI flags

- **Timeout behavior**
  - Default operation timeout is **25 seconds**
  - Can be changed with `AGENT_BROWSER_DEFAULT_TIMEOUT`
  - Warns that setting it above 30 seconds may cause IPC timeout issues

- **Connectivity modes**
  - **CDP mode** for connecting to existing Chrome/Chromium/Electron/WebView2 instances
  - **Auto-connect** to discover Chrome automatically
  - **Streaming** via WebSocket for live viewport preview and human-in-the-loop interaction
  - Supports custom browser executables and file:// local file access

- **Cloud and platform integrations**
  - iOS Simulator / Safari via Appium and XCUITest on macOS
  - Browserless, Browserbase, Browser Use, Kernel, and AWS Bedrock AgentCore cloud providers
  - Serverless examples for Vercel Sandbox and AWS Lambda
  - Supported platforms listed as macOS, Linux, and Windows native Rust binaries

- **Observability and AI assistant features**
  - Includes a local **dashboard** with live viewport, activity feed, console output, and AI chat
  - AI chat is powered by **Vercel AI Gateway**
  - The CLI `chat` command translates natural language into agent-browser actions

- **Target audience / usage style**
  - Optimized for AI agents and coding assistants
  - Recommends a “snapshot → ref → action” workflow
  - Suggests adding the tool as a skill for assistants like Claude Code, Cursor, Copilot, Gemini CLI, and others

- **License**
  - Apache-2.0

### Assessment
This is a high-density **reference** document with a **high-durability** mix of stable concepts and version-sensitive implementation details. The content is mostly **primary source** documentation/README material, not commentary, and it’s best used as a **refer-back** resource rather than a one-time skim. It is very information-rich, with extensive command lists, environment variables, and integration details, though some parts are likely to change over time as the CLI evolves. The scrape quality appears **good**: it captured the major sections, command examples, configuration details, security notes, integrations, and architecture text, with no obvious missing code blocks or major sections.
