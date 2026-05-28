---
url: https://github.com/hesreallyhim/awesome-claude-code
title: 'hesreallyhim/awesome-claude-code: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic'
scraped_at: '2026-04-19T08:32:35Z'
word_count: 7861
raw_file: raw/2026-04-19_hesreallyhim-awesome-claude-code-a-curated-list-of-awesome-skills-hooks-slash-co_c7f7e9fb.txt
tldr: awesome-claude-code is a curated directory of Claude Code ecosystem resources—skills, hooks, slash commands, orchestrators, status lines, monitors, CLAUDE.md files, and alternative clients—organized as a living reference for enhancing Anthropic Claude Code workflows.
key_quote: A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.
durability: medium
content_type: reference
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Anthropic
- Claude
- Astro-Han
- Ruller_Lulu
- lis186
- Wolf McNally
- Daniel Rosehill
- Ran Aroussi
tools:
- Claude Code
- Bash
- jq
- Docker
- GitHub CLI
- VS Code
- Emacs
- Neovim
libraries:
- Black
- mypy
- Vitest
- Semgrep
- CodeQL
companies:
- Anthropic
- Signal Foundation
- GitHub
- OpenAI
- Dagger
- Laravel
tags:
- claude-code
- ai-workflows
- developer-tools
- agent-orchestration
- reference-list
---

### TL;DR
`awesome-claude-code` is a curated directory of Claude Code ecosystem resources—skills, hooks, slash commands, orchestrators, status lines, monitors, CLAUDE.md files, and alternative clients—organized as a living reference for enhancing Anthropic Claude Code workflows.

### Key Quote
> “A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.”

### Summary
- This GitHub repo is an **“awesome list”** for **Claude Code by Anthropic**, collecting third-party tools and references that extend the core CLI/workflow experience.
- The list is organized into major sections:
  - **Agent Skills** — model-controlled configs and assets for specialized tasks.
  - **Workflows & Knowledge Guides** — broader process systems for planning, project management, and agentic development.
  - **Tooling** — apps and utilities built around Claude Code, including session tools, Docker wrappers, editors, and analysis utilities.
  - **Status Lines** — terminal status bar customizations showing usage, cost, git info, and rate-limit pacing.
  - **Hooks** — pre/post-action automation, safety checks, notifications, prompt-injection scanning, and formatting tweaks.
  - **Slash-Commands** — reusable command prompts for Git, testing, context loading, docs, deployment, and task management.
  - **CLAUDE.md Files** — repository-specific instruction files showing how real projects guide Claude Code.
  - **Alternative Clients** — non-terminal frontends, dashboards, mobile/web/desktop tools.
  - **Official Documentation** — links to Anthropic’s own docs, quickstarts, and GitHub Actions examples.
- The repo is **not a tutorial itself**; it’s mainly a **curated index** of resources with short descriptions and links.
- The **Latest Additions** section highlights newer entries such as:
  - `claude-pace` — Bash + jq statusline for burn-rate / quota pacing
  - `Clawd on Desk` — animated desktop pet reacting to Claude sessions
  - `ccxray` — transparent HTTP proxy/dashboard for Anthropic API traffic
  - `Encyclopedia of Agentic Coding Patterns` — 190+ pattern reference for AI-assisted development
- The list includes a lot of **workflow-heavy and safety-oriented tooling**, such as:
  - session restore/search tools
  - multi-agent orchestrators
  - hooks for command validation and TDD enforcement
  - usage dashboards and proxies
  - sandboxed/containerized execution tools
- There are also **project instruction examples** in the `CLAUDE.md` section showing how teams encode conventions for languages like Kotlin, Rust, TypeScript, Go, Python, and domain-specific projects.
- The contributing section says **submit recommendations via issues, not PRs**; it explicitly says the only person allowed to submit PRs is Claude.
- The repository is licensed under **Creative Commons CC BY-NC-ND 4.0**, so redistribution is allowed with attribution, but modified versions and commercial use are not.

### Assessment
This is a **reference**-type curated index with **high density** but mostly brief one-line annotations per item, so it’s best used as a **refer-back** resource when you want to find Claude Code tools by category. Durability is **medium**: the core taxonomy and many workflow ideas are useful for a while, but individual links, project quality, and Anthropic Claude Code behavior can change quickly, especially since the repo is explicitly a living list with “latest additions.” Originality is **synthesis** rather than primary research, because it aggregates and editorializes third-party resources; the author’s commentary is part of the value. Scrape quality is **good**: the structure, category headings, representative entries, contribution notes, and license text are present, though the full linked resources, images, and any repository-specific interactive details are of course not included here.
