---
url: https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md
title: OpenSpec/docs/supported-tools.md at main · Fission-AI/OpenSpec
scraped_at: '2026-04-19T06:54:18Z'
word_count: 595
raw_file: raw/2026-04-19_openspec-docs-supported-tools-md-at-main-fission-ai-openspec_7bca9f65.txt
tldr: OpenSpec’s `supported-tools.md` is a setup reference listing which AI coding assistants it can configure, where it installs skills/commands for each, and how `openspec init` varies by tool selection, profile, and workflow.
key_quote: Skill/command counts are profile-dependent and delivery-dependent, not fixed.
durability: medium
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- OpenSpec
- openspec
- Claude Code
- Cursor
- GitHub Copilot
- Codex
- Gemini CLI
- Windsurf
libraries: []
companies:
- Fission-AI
tags:
- ai-coding-assistants
- cli-configuration
- developer-tools
- documentation
- workflow-automation
---

### TL;DR
OpenSpec’s `supported-tools.md` is a setup reference listing which AI coding assistants it can configure, where it installs skills/commands for each, and how `openspec init` varies by tool selection, profile, and workflow.

### Key Quote
“Skill/command counts are profile-dependent and delivery-dependent, not fixed.”

### Summary
- This document explains how OpenSpec integrates with supported AI coding tools when you run `openspec init`.
- OpenSpec can install two kinds of artifacts, depending on delivery mode:
  - **Skills**: `.../skills/openspec-*/SKILL.md`
  - **Commands**: tool-specific `opsx-*` command files
- By default, OpenSpec uses the **`core` profile**, which includes these workflows:
  - `propose`
  - `explore`
  - `apply`
  - `archive`
- Expanded workflows can be enabled with `openspec config profile`, then applied with `openspec update`. These include:
  - `new`
  - `continue`
  - `ff`
  - `verify`
  - `sync`
  - `bulk-archive`
  - `onboard`

- The main body is a **tool directory reference** mapping each supported tool ID to:
  - the path where OpenSpec installs its skills
  - the path where it installs commands/prompts/workflows
- Supported tools listed include, among others:
  - Amazon Q Developer (`amazon-q`)
  - Claude Code (`claude`)
  - Cursor (`cursor`)
  - Codex (`codex`)
  - Continue (`continue`)
  - GitHub Copilot (`github-copilot`)
  - Gemini CLI (`gemini`)
  - Windsurf (`windsurf`)
  - plus many others such as Antigravity, Cline, Kiro, RooCode, Qwen Code, and Trae

- Notable installation exceptions:
  - **ForgeCode (`forgecode`)**: no command adapter; only skill-based `/openspec-*` invocations
  - **Trae (`trae`)**: no command adapter; only skill-based `/openspec-*` invocations
- Tool-specific path formats vary by ecosystem, for example:
  - Claude: `.claude/skills/...` and `.claude/commands/opsx/<id>.md`
  - Cursor: `.cursor/skills/...` and `.cursor/commands/opsx-<id>.md`
  - GitHub Copilot: `.github/skills/...` and `.github/prompts/opsx-<id>.prompt.md`
  - Codex: command prompts go under `$CODEX_HOME/prompts/` (or `~/.codex/prompts/`), not the project directory
- The file also notes that **GitHub Copilot prompt files** are recognized as custom slash commands in IDE extensions (VS Code, JetBrains, Visual Studio), but **Copilot CLI does not consume `.github/prompts/*.prompt.md` directly**.
- For scripted or CI setup, `openspec init` supports:
  - `--tools claude,cursor`
  - `--tools all`
  - `--tools none`
  - optional `--profile core`
- The doc enumerates the valid `--tools` IDs, making it a practical lookup table for automation.
- It closes by clarifying that workflow artifacts are installed dynamically based on the selected profile/workflows, not as a fixed set.
- Related docs are linked for:
  - **CLI Reference**
  - **Commands**
  - **Getting Started**

### Assessment
This is a **reference** document with medium-to-high durability: the general setup model is likely stable, but the exact supported tool list and path conventions are somewhat version-dependent and could change as OpenSpec evolves. The content is highly **structured and dense**, mostly factual, and clearly **primary-source documentation** from the project itself. It’s best used as a **refer-back** resource when configuring OpenSpec or checking which tool integrations are available. Scrape quality is **good**: the full table, notes, and setup examples appear present, with no obvious missing sections beyond any site-generated navigation not included in the excerpt.
