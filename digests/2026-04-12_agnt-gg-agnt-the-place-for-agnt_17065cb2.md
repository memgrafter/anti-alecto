---
url: https://github.com/agnt-gg/agnt
title: 'agnt-gg/agnt: The place for AGNT'
scraped_at: '2026-04-12T07:32:29Z'
word_count: 3979
raw_file: raw/2026-04-12_agnt-gg-agnt-the-place-for-agnt_17065cb2.txt
tldr: AGNT is a local-first, self-hostable AI agent operating system for desktop or Docker that combines persistent agents, visual workflows, goal execution, SkillForge self-improvement, plugins, dashboards, and 15+ AI providers into one workspace.
key_quote: AGNT is a **local-first AI agent operating system** that bundles everything you need to build, run, and improve autonomous AI agents into a single desktop application (or self-hosted Docker container).
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Nathan Wilbanks
tools:
- Electron
- Vue.js
- Express.js
- Docker
- Playwright
- Socket.IO
- Whisper
libraries:
- SQLite
companies:
- AGNT
tags:
- ai-agents
- self-hosting
- workflow-automation
- electron-app
- plugin-system
---

### TL;DR
AGNT is a local-first, self-hostable AI agent “operating system” for desktop or Docker that combines persistent agents, visual workflows, goal execution, SkillForge self-improvement, plugins, dashboards, and 15+ AI providers into one workspace.

### Key Quote
“AGNT is a **local-first AI agent operating system** that bundles everything you need to build, run, and improve autonomous AI agents into a single desktop application (or self-hosted Docker container).”

### Summary
- **What it is**
  - AGNT is presented as “The Complete AI Agent Operating System.”
  - It runs as a cross-platform **Electron desktop app** or as a **self-hosted Docker container**.
  - It emphasizes **local-first** ownership: data, agents, history, and SQLite storage stay on the user’s machine.

- **Core positioning**
  - It is **not** a thin chat UI or a stateless workflow tool.
  - The repo frames AGNT as a workspace to **build, run, evaluate, and evolve** autonomous agents.
  - It targets:
    - **Single users**
    - **Families**
    - **Small teams (2–10 people)**
  - It explicitly says it is **not designed** for multi-tenant SaaS or large enterprises.

- **Main capabilities**
  - **Persistent agents** with memory, skills, and goals
  - **Visual workflow designer** with node graphs, checkpoints, versioning, and live execution
  - **AGI loop**: execute → evaluate → re-plan until goals are met
  - **SkillForge**: generates and improves reusable skills from execution traces
  - **Plugin marketplace/system** for local and remote extensions
  - **Custom dashboards** with HTML/JS widgets
  - **Sandboxed code editor**
  - **MCP support**
  - **Speech transcription / text-to-speech**
  - **Email triggers, webhooks**
  - **15+ AI providers**, including local CLI integrations like Claude Code, OpenAI Codex, and Gemini CLI

- **Feature set highlights**
  - **Agent system**: multi-provider agents, persistent memory, real-time streaming chat, token/cost accounting
  - **Workflow designer**: drag-and-drop canvas, 60+ native nodes, dependency analysis, triggers for webhook/timer/email/schedule
  - **Goal system**: planning, decomposition, evaluation, approval flow, snapshots
  - **Evolution engine**: insight extraction, memory learning, prompt refinement, bottleneck/error analysis
  - **SkillForge**:
    - Automated skill evolution
    - Skill Evolution Score (SES)
    - Version lineage
    - A/B experiments
    - Eval datasets and train/test/validation splits
  - **Plugin system**:
    - `.agnt` packages
    - 25+ templates
    - Hot reload
    - Marketplace install/publish
  - **Observability and real-time sync**:
    - Execution traces
    - Live broadcast updates
    - Health monitoring across providers

- **Built-in tools and nodes**
  - The repo claims **60+ built-in nodes**
  - Categories include:
    - **Triggers**: Google Sheets, Discord, Slack, Zapier, email, timer, webhook
    - **Actions**: Discord, Slack, Gmail, Notion, Google Drive/Sheets/Slides, Dropbox, GitHub, Firecrawl, Unsplash, YouTube, web search/scrape, TTS, Stripe, AI/browser/MCP/custom API tools
    - **Utilities**: JavaScript, Python, SQLite CRUD, file system, counters, random numbers
    - **Control flow**: delay, loop, parallel execution, nested workflows
    - **Display widgets**: audio, chart, code, HTML, image, markdown, media, PDF previews

- **AI provider support**
  - The list includes **OpenAI, Anthropic, Gemini, Grok, Groq, Cerebras, DeepSeek, OpenRouter, Together AI, Kimi, MiniMax, Z-AI**, plus:
    - **Claude Code**
    - **OpenAI Codex**
    - **Gemini CLI**
    - Generic **OpenAI-compatible endpoints**
  - It says provider connection health is monitored in real time.

- **Architecture**
  - **Electron shell**
  - **Vue.js 3 frontend**
  - **Express backend** on port **3333**
  - Backend components include orchestrator, workflow engine, goal engine/AGI loop, SkillForge, evolution engine, plugin loader, MCP client, email listener, webhook dispatcher, filesystem, speech, and version service
  - Data is stored in **SQLite**

- **Installation / running**
  - Requires:
    - **Node.js v18+**
    - **npm v9+**
    - **Git**
  - Quick install:
    - `git clone https://github.com/agnt-gg/agnt.git`
    - `npm install`
    - `cd frontend && npm install && cd ..`
    - `npm start`
  - Docker is offered in **Full** and **Lite** variants:
    - **Full**: includes browser automation, about **~1.5GB**, port **33333**
    - **Lite**: no browser automation, about **~715MB**, port **3333**
  - Desktop binaries are available for Windows, macOS, and Linux.

- **Build and development**
  - Development mode runs frontend and Electron separately.
  - Production build compiles the frontend and launches the app.
  - Distribution commands exist for Windows, macOS, Linux, and Lite/Full variants.
  - Testing uses **Playwright E2E** suites.

- **Plugin development**
  - Plugins are ZIP-based `.agnt` packages with a manifest and code.
  - The README includes a minimal plugin example with:
    - `manifest.json`
    - `awesome-tool.js`
  - Plugins can be built with:
    - `node build-plugin.js my-awesome-plugin`
  - They can be installed through the UI or by dropping them into the plugins directory.

- **Docs and repo metadata**
  - Repo version shown: **0.5.1**
  - Electron version referenced: **33.0.2**
  - License is **Custom**
  - The README links to docs for API, build, self-hosting, lite mode, tests, and plugin development.
  - It also includes badges, screenshots, project stats, contribution guidance, and acknowledgments.

### Assessment
This is a **mixed** content type, primarily a **reference/announcement** style README for a software project, with tutorial elements for install, Docker, build, and plugin development. Durability is **medium**: the concepts behind the product are fairly stable, but many specifics are version-tied and may go stale quickly, especially the feature counts, provider list, ports, build sizes, and version **0.5.1**. Density is **high** because it packs a lot of product claims, architecture details, and usage instructions into a single page. Originality is mostly **primary source** marketing/documentation from the project authors, not a neutral synthesis. Reference style is **refer-back**: useful for checking installation steps, architecture, feature claims, and plugin format later. Scrape quality is **good** overall: the README content is extensive and includes commands, tables, and examples, though screenshots and images are referenced rather than captured, and some claims are promotional rather than independently verified.
