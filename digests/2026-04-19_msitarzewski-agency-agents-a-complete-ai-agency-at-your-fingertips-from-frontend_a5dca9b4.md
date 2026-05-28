---
url: https://github.com/msitarzewski/agency-agents?tab=readme-ov-file
title: 'msitarzewski/agency-agents: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.'
scraped_at: '2026-04-19T08:40:33Z'
word_count: 6474
raw_file: raw/2026-04-19_msitarzewski-agency-agents-a-complete-ai-agency-at-your-fingertips-from-frontend_a5dca9b4.txt
tldr: A large MIT-licensed repository of 147 specialized AI agent prompts/workflows, organized by domain and designed to be installed into tools like Claude Code, Copilot, Cursor, Aider, and Gemini CLI.
key_quote: Each agent is a specialized expert with personality, processes, and proven deliverables.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- claude code
- github copilot
- antigravity
- gemini cli
- opencode
- cursor
- aider
- windsurf
- openclaw
- qwen code
- kimi code
libraries: []
companies:
- GitHub
- Google
- Anthropic
- Microsoft
- OpenClaw
tags:
- ai-agents
- prompt-engineering
- developer-tools
- workflow-automation
- multi-tool-integration
---

### TL;DR
A large MIT-licensed repository of 147 specialized AI agent prompts/workflows, organized by domain and designed to be installed into tools like Claude Code, Copilot, Cursor, Aider, and Gemini CLI.

### Key Quote
“Each agent is a specialized expert with personality, processes, and proven deliverables.”

### Summary
- **What it is**
  - “The Agency” is a curated collection of AI agent definitions, originally born from a Reddit thread and iterated on over months.
  - It emphasizes **specialization over generic prompting**: each agent has a domain, personality, workflow, and concrete deliverables.
  - The repo claims **147 specialized agents across 12 divisions** and **10,000+ lines** of content.

- **How it’s meant to be used**
  - Primary target is **Claude Code**, where agents are copied into `~/.claude/agents/`.
  - Also supports **GitHub Copilot, Antigravity, Gemini CLI, OpenCode, Cursor, Aider, Windsurf, OpenClaw, Qwen Code, and Kimi Code**.
  - Provides scripts:
    - `./scripts/convert.sh` to generate tool-specific formats
    - `./scripts/install.sh` to install agents
  - Supports interactive installation, tool auto-detection, and a `--parallel` mode for faster conversion/install runs.
  - Example commands include:
    - `./scripts/install.sh --tool claude-code`
    - `./scripts/install.sh --tool cursor`
    - `./scripts/install.sh --no-interactive --tool all`

- **Agent organization**
  - Agents are grouped into many divisions, including:
    - **Engineering**: frontend, backend, mobile, AI, DevOps, security, embedded firmware, incident response, architecture, database, SRE, etc.
    - **Design**: UI/UX, brand, visual storytelling, whimsy, image prompts, inclusive visuals
    - **Paid Media**: PPC, tracking, creative strategy, display, social ads
    - **Sales**: outbound, discovery, deal strategy, sales engineering, proposals, pipeline analysis
    - **Marketing**: growth, content, social platform specialists, SEO, China-market specialists, AI citation strategy, video optimization
    - **Product**: sprint prioritization, trend research, feedback synthesis, behavioral nudges, product management
    - **Project Management**: studio producer, project shepherd, operations, experiment tracking, Jira workflow
    - **Testing**: evidence collection, reality checking, performance, API, accessibility, workflow optimization
    - **Support**: support, analytics, finance, infrastructure, legal compliance, executive summaries
    - **Spatial Computing**: XR, macOS/Metal, visionOS, WebXR, terminal integration
    - **Specialized**: orchestrator, LSP/indexing, identity/trust, compliance, document generation, MCP builder, workflow architecture, etc.
    - **Finance, Game Development, Academic** divisions with similarly specialized roles

- **Design philosophy**
  - The repo argues these are not one-off prompts or generic “act as X” instructions.
  - Each agent is intended to include:
    - identity/personality
    - core mission
    - critical rules
    - technical deliverables and examples
    - workflow process
    - success metrics
  - The stated goal is to produce **more reliable, role-specific outputs** with measurable outcomes.

- **Examples and scenarios**
  - The README gives concrete multi-agent usage scenarios:
    - **Startup MVP**: frontend + backend + growth + prototyping + quality checking
    - **Marketing campaign launch**: content + platform-specific social agents + analytics
    - **Enterprise feature development**: project management + architecture + design + testing
    - **Paid media account takeover**: audit, tracking, PPC structure, search term cleanup, creative refresh
    - **Full agency product discovery**: multiple agents collaborating in parallel
  - It points to an example called **“Nexus Spatial Discovery Exercise”** in `examples/`, where 8 agents were used together to produce a unified product plan.

- **Contributing and extensibility**
  - Contributors are encouraged to:
    - add new agents using a template structure
    - improve examples, code samples, workflows, and success metrics
    - share success stories in GitHub Discussions
  - The repo is meant to be **forkable and adaptable**, not a closed product.

- **Community, translations, and ecosystem**
  - Mentions community-maintained translations/localizations, especially Chinese adaptations.
  - Links to related resources like **awesome-openclaw-agents**.
  - Community engagement is active through GitHub Discussions, Issues, Reddit, and Twitter/X.

- **Claims and caveats**
  - The README is heavily promotional, but it also includes concrete install paths, tool-specific usage, and repository structure.
  - It claims the agents are “battle-tested” and used in production environments, though that is self-reported and not independently verified in the README.
  - The exact agent count is slightly inconsistent across sections: it says **144 specialized agents** in the stats section and **147 agents** in acknowledgments, which suggests the repo was changing as the README was captured.

### Assessment
This is a high-level repository README with **medium-to-high durability**: the concepts of specialized AI agents, prompt workflows, and multi-tool integration are fairly durable, but the exact tool list, agent count, and install paths are version-sensitive and may change over time. The content type is **mixed**, leaning toward **reference/documentation** with some promotional/announcement flavor. It is **high density** because it packs a large amount of repository structure, supported tools, commands, and use cases into one page. It is primarily **original source material** from the project maintainers rather than a synthesis. Best used as a **refer-back** reference to decide whether the repo contains an agent or integration you need; you would skim this once, then revisit the specific agent files or integration docs. Scrape quality is **good** overall: the main README content, tables, commands, and sections appear captured, though the repository may contain additional code, examples, or agent file details not included here.
