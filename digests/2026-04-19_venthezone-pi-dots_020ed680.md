---
url: https://github.com/VenTheZone/pi-dots
title: VenTheZone/pi-dots
scraped_at: '2026-04-19T07:44:58Z'
word_count: 686
raw_file: raw/2026-04-19_venthezone-pi-dots_020ed680.txt
tldr: pi-dots is a GitHub repo that packages 60+ AI-coding skills, specialist agents, workflows, and model-provider integrations for pi-coding-agent, with a quick-copy install path and a catalog of what each package/skill is for.
key_quote: pi-dots is a comprehensive collection of 60+ skills, agents, and workflows that transform pi into a complete AI development platform.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- pi-coding-agent
- Exa
- Firecrawl
- Playwright
- tmux
- Bun
- Next.js
- Anthropic Claude
- OpenRouter
- Kilo Gateway
- NVIDIA NIM
- Cline
libraries: []
companies:
- GitHub
- OpenRouter
- NVIDIA
- Anthropic
- Cline
tags:
- ai-development
- coding-agents
- developer-workflows
- model-providers
- project-templates
---

### TL;DR
`pi-dots` is a GitHub repo that packages 60+ AI-coding skills, specialist agents, workflows, and model-provider integrations for `pi-coding-agent`, with a quick-copy install path and a catalog of what each package/skill is for.

### Key Quote
“pi-dots is a comprehensive collection of 60+ skills, agents, and workflows that transform pi into a complete AI development platform.”

### Summary
- **What it is**
  - A repository named **`VenTheZone/pi-dots`** that acts as a skill/agent bundle for **pi-coding-agent**.
  - Positioned as a way to turn “pi” into a fuller **AI development platform** covering:
    - project setup
    - research
    - implementation
    - testing
    - debugging
    - deployment
    - content creation

- **Quick start / installation**
  - The repo recommends a “copy what you want” workflow.
  - For LLM agents, it provides a single install instruction pointing to:
    - `https://raw.githubusercontent.com/VenTheZone/pi-dots/refs/heads/main/INSTALL.md`
  - Manual install commands shown:
    - `mkdir -p ~/.pi/agent/skills`
    - `cp -r pi-dotfiles/skills/* ~/.pi/agent/skills/`
    - `cp pi-dotfiles/.pi/settings.json ~/.pi/agent/`
    - `cp pi-dotfiles/.pi/mcp.json ~/.pi/agent/`
  - To install just one skill:
    - `cp -r pi-dotfiles/skills/tdd-workflow ~/.pi/agent/skills/`

- **Packages listed**
  - `pi-dotfiles` — core skills, settings, MCP config
  - `pi-dotfiles-niche-skills` — 60 total skills covering areas like Docker, Python, Go, AI research, content creation, project management, design systems, and web utilities
  - `pi-dotfiles-specialist-skills` — 16 specialist roles
  - `pi-agents` — extended subagents, including `external-scout`
  - `pi-dynamic-model-providers` — additional model providers, including:
    - OpenRouter
    - Kilo Gateway
    - **NVIDIA NIM**
    - Cline free models

- **Core skills highlighted (12)**
  - `brainstorming` — feature planning
  - `coding-standards` — TypeScript/JS/React best practices
  - `context7-base-code-review` — look up docs
  - `context7-driven-development` — use docs while coding
  - `humanizer` — polish documentation
  - `iterative-retrieval` — progressive context
  - `planning-with-files` — file-based task planning
  - `security-review` — auth, secrets, API security
  - `strategic-compact` — manual context compaction
  - `tdd-workflow` — test-driven development
  - `verification-loop` — verify your work
  - `visual-explainer` — HTML diagrams

- **Niche skills (60 total)**
  - The repo says `pi-dotfiles-niche-skills` was expanded from **33 to 60 skills**.
  - Categories and examples:
    - **Infrastructure & Research**
      - `agent-introspection-debugging` — self-healing for failing agents
      - `mcp-server-patterns` — custom MCP servers
      - `deep-research` — multi-source cited research using firecrawl + exa
      - `market-research` — business/competitive intelligence
      - `exa-search` — Exa MCP web/code search
      - `documentation-lookup` — Context7 live docs lookup
    - **Content Creation**
      - `brand-voice` — reusable voice profiles from real examples
      - `content-engine` — platform-native content for X, LinkedIn, newsletters
      - `article-writing` — long-form essays/guides with voice
      - `crosspost` — multi-platform distribution without duplicates
    - **Developer Tools**
      - `dmux-workflows` — parallel agent orchestration via tmux
      - `claude-api` — Anthropic Claude API patterns
      - `bun-runtime` — Bun runtime/package manager/bundler
      - `nextjs-turbopack` — Next.js 16+ development
      - `x-api` — X/Twitter API integration
      - `agent-sort` — optimize skill/agent load based on repo
      - `investor-outreach` — investor communication
      - `api-design` — REST/GraphQL API design patterns
    - **Project Management & Workflow**
      - `quick-setup` — auto-detect stack, generate `.pi/` config
      - `git-workflow` — branching, commits, PRs, conflict resolution
      - `debug-helper` — error analysis, logs, profiling
      - `grill-me` — stress-test plans with aggressive questioning
      - `improve-codebase-architecture` — explore codebases for refactor opportunities
      - `request-refactor-plan` — tiny-commit refactor plans / GitHub RFC
      - `write-a-skill` — meta-skill for creating new skills
      - `decision-commits` — commits that preserve decisions, not just changes
    - **Web Utilities**
      - `web-fetch` — fetch pages and extract readable text
      - `web-search` — lightweight DuckDuckGo search
    - **Testing & E2E**
      - `e2e-testing` — Playwright and Page Object Model patterns
      - `eval-harness` — eval-driven development framework

- **Special features**
  - **External Scout & Plan**
    - Command: `/external-scout-and-plan <feature>`
    - Promises a workflow to:
      1. search the web for open-source implementations
      2. clone top repos into `/tmp/`
      3. analyze patterns and architecture
      4. generate a detailed plan based on real examples
    - Requires:
      - `exa-search` skill
      - `exa-mcp-server` configured
  - **Dynamic Model Providers**
    - Supports model access beyond built-ins:
      - OpenRouter — 350+ models
      - Kilo Gateway — 350+ models
      - NVIDIA NIM — Llama, Nemotron, Nemo; requires `NVIDIA_API_KEY`
      - Cline — 500+ models plus 3 free models:
        - MiniMax M2.5
        - KAT Coder Pro
        - GLM-5
    - Command shown: `/provider-models list`

- **Commands and verification**
  - Notes that `pi-dotfiles/prompts/commands.md` contains all `/` commands, **26 total**.
  - Verification command:
    - `pi --eval "/mcp tools"`

### Assessment
This is a **reference / installation-oriented repo README** with some promotional framing. Durability is **medium**: the conceptual structure of skills, agents, and workflows is reusable, but parts are tied to specific tools and versions, including references to **Next.js 16+**, named model providers, and the current count of skills/commands. Content type is **mixed**—part docs, part announcement/catalog, part product pitch. Density is **high**, since it packs a lot of package names, commands, and feature descriptions into a small space. It appears to be **primary source** project documentation from the repo author. Best used as **refer-back** material when deciding which package or skill to install, or when checking supported commands and integrations. Scrape quality is **good** overall: the README content appears captured clearly, with code blocks, tables, and section structure intact; no obvious missing code samples or images are indicated in the provided text.
