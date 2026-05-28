---
url: https://github.com/disler/pi-vs-claude-code
title: 'disler/pi-vs-claude-code: Comparison between open source PI agent and closed source Claude Code agent'
scraped_at: '2026-04-19T08:12:50Z'
word_count: 1898
raw_file: raw/2026-04-19_disler-pi-vs-claude-code-comparison-between-open-source-pi-agent-and-closed-sour_43f68179.txt
tldr: A demo repository showing how to customize the open-source Pi Coding Agent with UI, orchestration, safety, and cross-agent extensions as a hedge against Claude Code’s dominance in agentic coding.
key_quote: Why?_ To showcase what it looks like to hedge against the leader in the agentic coding market, Claude Code.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mario Zechner
- IndyDevDan
tools:
- Bun
- just
- pi
- firecrawl
- curl
libraries: []
companies:
- OpenAI
- Anthropic
- Google
- OpenRouter
- Claude Code
tags:
- agentic-coding
- multi-agent-systems
- developer-tools
- cli-extension
- ai-safety
---

### TL;DR
A demo repository showing how to customize the open-source Pi Coding Agent with UI, orchestration, safety, and cross-agent extensions as a hedge against Claude Code’s dominance in agentic coding.

### Key Quote
“Why?_ To showcase what it looks like to hedge against the leader in the agentic coding market, Claude Code.”

### Summary
- **What this repo is**
  - `pi-vs-cc` is a collection of customized **Pi Coding Agent** instances designed to demonstrate what Pi can do versus **Claude Code**.
  - The repo’s focus is on **custom UI**, **agent orchestration**, **safety auditing**, and **cross-agent integrations**.
  - It includes a **video demo** link (`https://youtu.be/f8cfH5XX-XU`) and a large illustrative image.

- **Prerequisites**
  - Requires **Bun ≥ 1.3.2**
  - Requires **just** task runner (`brew install just`)
  - Requires **pi** CLI from the Pi Coding Agent project

- **API key setup**
  - Pi does **not** auto-load `.env` files; keys must be in the shell environment before launching.
  - Suggested workflow:
    - `cp .env.sample .env`
    - Fill in API keys manually
    - Source with `source .env && pi`
  - Supported providers in `.env.sample`:
    - **OpenAI** (`OPENAI_API_KEY`)
    - **Anthropic** (`ANTHROPIC_API_KEY`)
    - **Google** (`GEMINI_API_KEY`)
    - **OpenRouter** (`OPENROUTER_API_KEY`)
    - Plus other providers via Pi provider docs

- **Installation**
  - Run `bun install`

- **Extensions included**
  - The repo is mainly a showcase of Pi extensions, including:
    - **pure-focus**: removes footer and status line for distraction-free mode
    - **minimal**: compact footer with model name and context meter
    - **cross-agent**: imports commands/skills/agents from `.claude`, `.gemini`, `.codex`
    - **purpose-gate**: requires session intent before use
    - **tool-counter** / **tool-counter-widget**: tool call and cost tracking UI
    - **subagent-widget**: spawns background subagents with live progress
    - **tilldone**: task discipline and persistent task list
    - **agent-team**: dispatcher model for specialist agents
    - **system-select**: switch personas/system prompts across agent ecosystems
    - **damage-control**: command/path safety auditing
    - **agent-chain**: sequential multi-agent pipeline orchestration
    - **pi-pi**: meta-agent for building Pi agents with parallel research experts
    - **session-replay**: scrollable session timeline UI
    - **theme-cycler**: theme switching via shortcut or `/theme`

- **How to use extensions**
  - Single extension:
    - `pi -e extensions/<name>.ts`
  - Multiple extensions:
    - `pi -e extensions/minimal.ts -e extensions/cross-agent.ts`
  - `just` recipes wrap common setups:
    - `just pi`
    - `just ext-minimal`
    - `just ext-cross-agent`
    - `just ext-agent-team`
    - `just all`
  - `just open ...` can launch combinations in a new terminal window

- **Project structure**
  - `extensions/` contains TypeScript extension source files
  - `specs/` contains extension feature specs
  - `.pi/` contains:
    - session files
    - agents
    - skills
    - themes
    - damage-control rules
    - workspace settings
  - Root docs include:
    - `CLAUDE.md`
    - `THEME.md`
    - `TOOLS.md`

- **Multi-agent workflows**
  - **Subagent Widget (`/sub`)**
    - Spawns headless Pi subagents for background tasks
    - Shows streaming progress in a live widget
  - **Agent Teams (`/team`)**
    - Primary agent acts as a dispatcher and delegates to specialist agents
    - Configured via `.pi/agents/teams.yaml`
    - Includes `pi-pi` as a meta-team using specialized expert agents
    - Notes that its experts use **firecrawl** first, then safely fall back to **curl**
  - **Agent Chains (`/chain`)**
    - Sequential pipeline where one agent’s output becomes the next agent’s input
    - Defined in `.pi/agents/agent-chain.yaml`
    - Example flow: planner → builder → reviewer

- **Safety auditing**
  - `damage-control` intercepts `tool_call` events and checks commands against rules in `.pi/damage-control-rules.yaml`
  - Blocks or warns on:
    - destructive bash patterns like `rm -rf`, `git reset --hard`, `aws s3 rm --recursive`, `DROP DATABASE`
    - sensitive files like `.env`, `~/.ssh/`, `*.pem`
    - risky system paths and critical project files

- **Documentation and references**
  - The repo includes comparison and reference docs for extension authors:
    - `COMPARISON.md`
    - `PI_VS_OPEN_CODE.md`
    - `RESERVED_KEYS.md`
    - `THEME.md`
    - `TOOLS.md`
  - It also lists Pi documentation links for SDK, RPC, JSON event stream, providers, models, extensions, skills, settings, and compaction.

- **Hooks/events comparison**
  - Includes a side-by-side table comparing **Claude Code hooks** vs **Pi Agent hooks/events**
  - Highlights:
    - Shared categories: session, input, tool, compact
    - Pi-specific event richness: branching, agent/turn, message, model/context
    - Claude-specific items: permission, subagents, config, worktree, system
  - This section is especially useful for extension authors comparing lifecycle capabilities.

- **Tone / positioning**
  - The repo is openly promotional and strategic: it frames Pi as a way to “prepare for the future of software engineering.”
  - It also links to “Tactical Agentic Coding” and the IndyDevDan YouTube channel, indicating this is partly a demo, partly advocacy content.

### Assessment
This is a **mixed** technical/demo repository with strong tutorial and reference elements, aimed at showcasing Pi’s extension system and agent orchestration capabilities. Durability is **medium**: the architectural ideas around multi-agent workflows, UI customization, and safety hooks are fairly durable, but the concrete tooling, provider setup, and extension APIs are version-dependent and may age as Pi evolves. The content is **dense** and highly specific, with commands, file paths, event names, and extension names throughout. It appears to be **primary source** material from the project maintainers, though it is also clearly **promotional commentary** in places. For future use, it is best treated as **refer-back** material if you work with Pi extensions or want to compare Pi vs Claude Code; otherwise, **skim-once** may be enough. Scrape quality is **good**: the main README content, tables, commands, and structure are present, though any images, linked docs, and repo code files are not included here.
