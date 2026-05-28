---
url: https://github.com/code-yeongyu/oh-my-openagent
title: 'code-yeongyu/oh-my-openagent: omo; the best agent harness - previously oh-my-opencode'
scraped_at: '2026-04-19T08:08:32Z'
word_count: 2509
raw_file: raw/2026-04-19_code-yeongyu-oh-my-openagent-omo-the-best-agent-harness-previously-oh-my-opencod_a7ae5c3d.txt
tldr: oh-my-openagent is the renamed OpenCode plugin “OmO” that promises one-command agent setup, multi-model orchestration, and a hash-anchored edit system called Hashline.
key_quote: Install OmO. Type `ultrawork`. Done.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- code-yeongyu
- Arthur Guiot
- Can Bölük
- d0t3ch
- James Hargis
- Jacob Ferrari
- Henning Kilset
- mysticaltech
- Darren Builds AI
- junhoyeo
tools:
- OpenCode
- Claude Code
- Cursor
- AmpCode
- PostHog
- tmux
- LSP
- AST-Grep
- Exa
- Context7
- Grep.app
- Bun
libraries: []
companies:
- Anthropic
- PostHog
- Google
- Microsoft
- Indentity
- Sisyphus Labs
- Discord
tags:
- ai-agents
- developer-tools
- multi-model-orchestration
- code-editing
- open-source
---

### TL;DR
`oh-my-openagent` is the renamed OpenCode plugin “OmO” (`oh-my-opencode` legacy) that promises one-command agent setup via `ultrawork`/`ulw`, multi-model orchestration with Sisyphus/Hephaestus/Prometheus, and a hash-anchored edit system called Hashline.

### Key Quote
"Install OmO. Type `ultrawork`. Done."

### Summary
- This GitHub repo is the README for **code-yeongyu/oh-my-openagent**, a plugin/harness for **OpenCode** that was previously called **`oh-my-opencode`**.
- The README emphasizes a migration/compatibility transition:
  - The published package and binary name remain **`oh-my-opencode`**.
  - In `opencode.json`, the preferred plugin entry is now **`oh-my-openagent`**.
  - Legacy `oh-my-opencode` entries still load, but with a warning.
  - Both legacy and renamed config basenames are recognized during the transition.
- The central pitch is very simple:
  - Install the plugin.
  - Run **`ultrawork`** (alias **`ulw`**).
  - Let the harness orchestrate agents and tooling automatically.
- The project describes a multi-agent setup with named roles:
  - **Sisyphus**: main orchestrator
  - **Hephaestus**: autonomous deep worker
  - **Prometheus**: planner/interviewer
  - Other referenced agents include **Oracle**, **Librarian**, **Explore**, and **Multimodal Looker**
- It claims the harness supports **multi-model orchestration**, mapping task categories to models rather than forcing users to choose manually.
  - Examples mentioned: **Claude / Kimi / GLM** for orchestration, **GPT** for reasoning, **Minimax** for speed, **Gemini** for creativity.
  - The README also says **`ultrabrain`** routes to **GPT-5.4 xhigh** by default.
- A major technical feature is **Hashline** / “Hash-Anchored Edit Tool”:
  - Lines are tagged with content hashes like `11#VK|`.
  - Edits must reference those tags.
  - If the file changed, mismatched hashes reject the edit before corruption.
  - The README claims this avoids stale-line errors and cites a benchmark improvement for Grok Code Fast 1 from **6.7% → 68.3%** success rate “just from changing the edit tool.”
- Other highlighted capabilities:
  - **IntentGate** for intent analysis before acting
  - **LSP + AST-Grep** for rename, diagnostics, and AST-aware rewrites
  - **Background agents** for parallel work
  - **Built-in MCPs**: Exa web search, Context7 docs, Grep.app GitHub search
  - **Ralph Loop / `/ulw-loop`** for self-referential completion loops
  - **Todo Enforcer** and **Comment Checker**
  - **Tmux integration**
  - **Claude Code compatibility** for hooks, commands, skills, MCPs, and plugins
  - **`/init-deep`** to generate hierarchical `AGENTS.md` files
- Installation is framed for both humans and agents:
  - Humans are told to paste a prompt into their LLM agent.
  - Agents are told to fetch and follow the installation guide directly via `curl`.
- The README also documents:
  - **Uninstallation** steps
  - **Features**
  - **Configuration**
  - **Model setup**
  - **Privacy/telemetry** defaults
- Telemetry note:
  - Anonymous telemetry is enabled by default.
  - It uses **PostHog** with a hashed installation identifier.
  - It can be disabled with `OMO_SEND_ANONYMOUS_TELEMETRY=0` or `OMO_DISABLE_POSTHOG=1`.
- The README is strongly promotional and opinionated:
  - It argues that users should not have to juggle agent tooling manually.
  - It positions OmO as a distilled “best of” harness after extensive experimentation and token spend.
  - It claims broad adoption and includes testimonials, but those are marketing-style quotes rather than independently verified evidence.

### Assessment
**Durability:** medium. The conceptual ideas around agent orchestration, edit safety, and harness design may last, but the README is tied to specific product names, model routing defaults, config keys, and a live migration from `oh-my-opencode` to `oh-my-openagent`, so parts of it will age quickly. **Content type:** mixed, with a strong tutorial/reference component plus promotional commentary and announcement-style migration notes. **Density:** high; the README is packed with product claims, feature lists, model names, config details, and commands. **Originality:** primary source, since this is the project’s own README and installation/reference material, though it also includes external quotes and borrowed framing. **Reference style:** refer-back for installation, config, feature lookup, and migration details; skim-once for the hype/testimonial sections. **Scrape quality:** partial-good; the main README text came through, but the linked docs, screenshots/images, and referenced subpages were not actually fetched here, so deeper installation/config details and visual assets are missing.
