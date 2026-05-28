---
url: https://github.com/numman-ali/openskills
title: 'numman-ali/openskills: Universal skills loader for AI coding agents - npm i -g openskills'
scraped_at: '2026-04-12T07:22:11Z'
word_count: 1001
raw_file: raw/2026-04-12_numman-ali-openskills-universal-skills-loader-for-ai-coding-agents-npm-i-g-opens_87fd7b43.txt
tldr: OpenSkills is a Node.js CLI that installs, syncs, and loads Anthropic-style `SKILL.md` skills for multiple AI coding agents by writing the same `<available_skills>` format Claude Code uses into `AGENTS.md`.
key_quote: Think of it as the universal installer for SKILL.md.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Anthropic
tools:
- openskills
- Claude Code
- Cursor
- Windsurf
- Aider
- Codex
- AGENTS.md
- SKILL.md
libraries: []
companies:
- Anthropic
tags:
- ai-agents
- cli-tools
- skill-loading
- developer-workflows
- markdown-config
---

### TL;DR
OpenSkills is a Node.js CLI that installs, syncs, and loads Anthropic-style `SKILL.md` skills for multiple AI coding agents by writing the same `<available_skills>` format Claude Code uses into `AGENTS.md`.

### Key Quote
“Think of it as the universal installer for SKILL.md.”

### Summary
- **What it is**
  - A CLI tool for managing “skills” for AI coding agents.
  - Claims compatibility with Claude Code, Cursor, Windsurf, Aider, Codex, and any agent that can read `AGENTS.md`.
  - Positions itself as a universal loader/installer for Anthropic’s skills system.

- **Core idea**
  - Claude Code uses `SKILL.md` files and exposes them through a `<available_skills>` XML block.
  - OpenSkills mirrors that same format so other agents can use the same skills without needing Claude Code.
  - Skills are loaded on demand to keep the agent’s context cleaner.

- **Quick start**
  - Install a marketplace/package of skills with:
    - `npx openskills install anthropics/skills`
  - Sync the generated skills list into the project:
    - `npx openskills sync`
  - Default install target is project-local:
    - `./.claude/skills`
  - With `--universal`, it uses:
    - `./.agent/skills`
  - With `--global`, it installs to:
    - `~/.claude/skills`

- **Why it claims to be useful**
  - Exact Claude Code compatibility: same prompt format, marketplace, folder structure.
  - Universal across agents that can read `AGENTS.md`.
  - Progressive disclosure: loads only the needed skill.
  - Repo-friendly: skills can be committed and versioned with the project.
  - Private-friendly: supports local paths and private Git repos.

- **How it works**
  - The repo shows a Claude Code-style `<available_skills>` XML block listing skill name, description, and location.
  - OpenSkills writes a similar structure into `AGENTS.md`.
  - Agents invoke loading through:
    - `npx openskills read <skill-name>`
  - The README includes a side-by-side comparison showing the same XML format and similar folder layout.

- **Installation sources supported**
  - Anthropic Marketplace:
    - `npx openskills install anthropics/skills`
  - Any GitHub repo:
    - `npx openskills install your-org/your-skills`
  - Local path:
    - `npx openskills install ./local-skills/my-skill`
  - Private Git repo:
    - `npx openskills install git@github.com:your-org/private-skills.git`

- **Universal mode**
  - Designed for mixed-agent setups using one `AGENTS.md`.
  - `--universal` installs into `.agent/skills/` to avoid conflicts with Claude’s plugin marketplace.
  - Priority order listed as:
    1. `./.agent/skills/`
    2. `~/.agent/skills/`
    3. `./.claude/skills/`
    4. `~/.claude/skills/`

- **Commands**
  - `npx openskills install <source> [options]`
  - `npx openskills sync [-y] [-o <path>]`
  - `npx openskills list`
  - `npx openskills read <name>`
  - `npx openskills update [name...]`
  - `npx openskills manage`
  - `npx openskills remove <name>`
  - Flags:
    - `--global`
    - `--universal`
    - `-y, --yes`
    - `-o, --output <path>`

- **SKILL.md format**
  - Uses frontmatter with `name` and `description`.
  - Skills include instructions and can reference bundled resources like `references/` and `scripts/`.
  - Example skill shows PDF-related instructions and file references.

- **Creating your own skills**
  - Minimal skill layout is just:
    - `my-skill/SKILL.md`
  - Optional structure includes:
    - `references/`
    - `scripts/`
    - `assets/`
  - Supports local symlink-based development workflows.
  - Suggests installing Anthropic skills and reading `skill-creator` for authoring guidance.

- **Updating skills**
  - `npx openskills update` refreshes installed skills from a git source.
  - Can update specific skills by comma-separated names.
  - If a skill was installed before update tracking existed, reinstall once to record its source.

- **FAQ / positioning**
  - Explains that skills are static instructions + resources, while MCP is for dynamic tools.
  - Claims skills require no server and work with every agent.
  - Frames OpenSkills as lightweight and aligned with Anthropic’s skills spec.

- **Requirements and license**
  - Requires Node.js 20.6+ and Git.
  - Licensed under Apache 2.0.
  - Attributes Anthropic’s Agent Skills spec and explicitly says it is not affiliated with Anthropic.

### Assessment
This is a **mixed** but mostly **tutorial/reference** README for a CLI tool. Durability is **medium** because the core concept of skill-loading and the `SKILL.md`/`AGENTS.md` workflow may last, but the exact commands, supported agents, and compatibility claims are tied to current ecosystem conventions and the tool’s present implementation. The content is fairly **dense** and practical, with specific commands, folder paths, and configuration examples. It is **primary source** material from the project maintainers rather than an outside commentary. It is best used as a **refer-back** reference for installation and usage rather than a deep study text. Scrape quality looks **good**: the README structure, code blocks, tables, FAQs, and examples are present, though this capture may omit repository files, screenshots, or behavior not shown in the README.
