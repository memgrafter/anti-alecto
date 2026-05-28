---
url: https://github.com/alirezarezvani/claude-skills
title: 'alirezarezvani/claude-skills: +192 Claude Code skills & agent plugins for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product, compliance, C-level advisory.'
scraped_at: '2026-04-19T07:46:43Z'
word_count: 2131
raw_file: raw/2026-04-19_alirezarezvani-claude-skills-192-claude-code-skills-agent-plugins-for-claude-cod_15784760.txt
tldr: A large MIT-licensed GitHub repository claiming to provide 235 Claude Code skills/agent plugins, 305 stdlib-only Python tools, and conversion/install support for 12 AI coding tools across engineering, marketing, product, compliance, C-level advisory, and more.
key_quote: '**The most comprehensive open-source library of Claude Code skills and agent plugins** — also works with OpenAI Codex, Gemini CLI, Cursor, and 7 more coding agents.'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Alireza Rezvani
tools:
- Claude Code
- OpenAI Codex
- Gemini CLI
- OpenClaw
- Hermes Agent
- Cursor
- Aider
- Windsurf
- Kilo Code
- OpenCode
- Augment
- Antigravity
libraries: []
companies:
- GitHub
- Claude
- OpenAI
tags:
- ai-coding-tools
- agent-skills
- developer-productivity
- plugin-ecosystem
- software-documentation
---

### TL;DR
A large MIT-licensed GitHub repository claiming to provide 235 Claude Code skills/agent plugins, 305 stdlib-only Python tools, and conversion/install support for 12 AI coding tools across engineering, marketing, product, compliance, C-level advisory, and more.

### Key Quote
"**The most comprehensive open-source library of Claude Code skills and agent plugins** — also works with OpenAI Codex, Gemini CLI, Cursor, and 7 more coding agents."

### Summary
- **What this repo is**
  - A GitHub repository called **alirezarezvani/claude-skills** that packages reusable “skills,” “agent plugins,” and “personas” for AI coding tools.
  - It positions itself as a broad library for **Claude Code** and other agents such as **OpenAI Codex, Gemini CLI, Cursor, Aider, Windsurf, Kilo Code, OpenCode, Augment, Antigravity, OpenClaw, and Hermes Agent**.
  - The README claims **235 production-ready skills** and **305 Python CLI tools**.

- **Core concept**
  - A “skill” is described as a modular instruction package containing:
    - `SKILL.md` for workflows and decision frameworks
    - Python tools (stdlib-only, no pip installs)
    - Reference docs, templates, and checklists
  - It distinguishes:
    - **Skills** = how to execute a task
    - **Agents** = what task to do
    - **Personas** = who is thinking
  - The repo emphasizes that these can be combined through an **orchestration** pattern.

- **Installation / usage**
  - **Claude Code**:
    - Add marketplace:
      - `/plugin marketplace add alirezarezvani/claude-skills`
    - Install bundles like:
      - `engineering-skills@claude-code-skills`
      - `marketing-skills@claude-code-skills`
      - `ra-qm-skills@claude-code-skills`
      - `c-level-skills@claude-code-skills`
    - Or install individual skills like `skill-security-auditor`, `playwright-pro`, `self-improving-agent`, `content-creator`.
  - **Gemini CLI**:
    - Clone repo and run `./scripts/gemini-install.sh`
    - Then call something like `activate_skill(name="senior-architect")`
  - **OpenAI Codex**:
    - `npx agent-skills-cli add alirezarezvani/claude-skills --agent codex`
  - **OpenClaw / manual install**:
    - Shell installer scripts or copy skill folders into the tool’s skill directory.

- **Multi-tool conversion**
  - The repo claims a single script can convert **156 skills** into native formats for several tools:
    - **Cursor** (`.mdc`)
    - **Aider** (`CONVENTIONS.md`)
    - **Kilo Code**
    - **Windsurf**
    - **OpenCode**
    - **Augment**
    - **Antigravity**
    - **Hermes Agent**
  - Example commands:
    - `./scripts/convert.sh --tool all`
    - `./scripts/install.sh --tool cursor --target /path/to/project`
  - It says converted outputs include per-tool README files and zero manual conversion work.

- **Skills by domain**
  - The README groups skills into domains with counts and examples:
    - **Engineering — Core**: architecture, frontend, backend, QA, DevOps, SecOps, AI/ML, data, Playwright, security suite, accessibility
    - **Playwright Pro**: test generation, flaky test fixing, Cypress/Selenium migration, TestRail/BrowserStack templates
    - **Self-Improving Agent**: auto-memory curation, skill extraction, memory health
    - **Engineering — POWERFUL**: deeper production-grade tools like agent design, RAG, database design, CI/CD, MCP builders, observability, performance profiling, monorepo navigation, incident management
    - **Product**: PM, agile PO, UX research, SaaS scaffolding, analytics, experiment design, roadmap communication
    - **Marketing**: content, SEO, CRO, channels, growth, intelligence, sales, orchestration
    - **Project Management**: senior PM, scrum master, Jira/Confluence/Atlassian
    - **Regulatory & QM**: ISO 13485, MDR 2017/745, FDA, ISO 27001, GDPR, CAPA, risk management
    - **C-Level Advisory**: full C-suite roles and board/culture workflows
    - **Business & Growth**: customer success, sales engineer, revenue ops, contracts/proposals
    - **Finance**: financial analyst and SaaS metrics coach

- **Personas**
  - Three built-in personas are highlighted:
    - **Startup CTO**
    - **Growth Marketer**
    - **Solo Founder**
  - Personas are described as curated skill loadouts with distinct communication styles and priorities.
  - Example usage includes copying persona markdown files into a Claude/agent personas directory or converting them for other tools.

- **Orchestration**
  - The repo proposes a lightweight protocol for combining personas and skills:
    - **Solo Sprint**
    - **Domain Deep-Dive**
    - **Multi-Agent Handoff**
    - **Skill Chain**
  - Example workflow: a 6-week product launch split across build, prepare, and ship phases using different personas and skills.

- **Notable features**
  - A **Skill Security Auditor** is presented as a security gate that scans skills before installation for:
    - command injection
    - code execution
    - data exfiltration
    - prompt injection
    - dependency supply-chain risks
    - privilege escalation
  - The repo claims this auditor is in **v2.0.0** and is dependency-free.
  - Several “recently enhanced” skills are called out, such as:
    - `git-worktree-manager`
    - `mcp-server-builder`
    - `changelog-generator`
    - `ci-cd-pipeline-builder`
    - `prompt-engineer-toolkit`

- **Python tools/examples**
  - The README gives example CLI invocations for:
    - SaaS metric calculation
    - brand voice analysis
    - tech debt scoring
    - RICE prioritization
    - skill security auditing
    - landing page scaffolding
  - It stresses the scripts are **stdlib-only** and verified with `--help`.

- **Stated project claims and metadata**
  - License: **MIT**
  - Stars claim: **5,200+ GitHub stars** in the README text
  - It also includes badges for **Skills: 235**, **Agents: 28**, **Personas: 3**, **Commands: 27**
  - The repo says it follows semantic versioning and patch releases won’t change script arguments or paths.

### Assessment
This is a **mixed** reference/marketing document: it functions as documentation for installation and usage, but it is also promotional and heavy on breadth claims. Durability is **medium** because the underlying ideas—agent skills, personas, orchestration, and plugin-style tooling—are fairly timeless, but the exact counts, supported tools, commands, and version claims are likely to change as the repo evolves. Content density is **high** because the README is packed with specific tool names, install commands, skill counts, and examples. Originality is mostly **primary source** for this repository’s own structure and claims, though the framing is partly promotional commentary about its scope. For later use, it is best treated as **refer-back** documentation if you plan to install or browse the skill catalog, and as **skim-once** if you only need to know what the project is. Scrape quality looks **good**: the text includes most major sections, commands, and tables, though any rendered images, badge visuals, and linked sub-repository contents are not captured here.
