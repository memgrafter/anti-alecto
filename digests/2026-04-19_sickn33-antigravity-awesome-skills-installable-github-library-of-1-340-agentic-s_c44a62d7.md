---
url: https://github.com/sickn33/antigravity-awesome-skills
title: 'sickn33/antigravity-awesome-skills: Installable GitHub library of 1,340+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and more. Includes installer CLI, bundles, workflows, and official/community skill collections.'
scraped_at: '2026-04-19T08:33:10Z'
word_count: 4050
raw_file: raw/2026-04-19_sickn33-antigravity-awesome-skills-installable-github-library-of-1-340-agentic-s_c44a62d7.txt
tldr: A large, installable repository of 1,431+ SKILL.md playbooks plus installer CLI, bundles, workflows, and docs for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and other AI coding assistants.
key_quote: Installable GitHub library of 1,431+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and other AI coding assistants.
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- sickn33
tools:
- Claude Code
- Cursor
- Codex CLI
- Gemini CLI
- Antigravity
- Kiro
- OpenCode
- GitHub Copilot
libraries: []
companies:
- GitHub
- Anthropic
- OpenAI
- Google
- Microsoft
- Supabase
- Vercel
- Hugging Face
- Apify
- Expo
- Neon
- Remotion
- Scopeblind
tags:
- agentic-skills
- ai-coding-assistants
- cli-tools
- prompt-playbooks
- software-documentation
---

### TL;DR
A large, installable repository of 1,431+ `SKILL.md` playbooks plus installer CLI, bundles, workflows, and docs for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and other AI coding assistants.

### Key Quote
"Installable GitHub library of 1,431+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and other AI coding assistants."

### Summary
- **What it is**
  - `sickn33/antigravity-awesome-skills` is a GitHub library of reusable agent skills packaged as `SKILL.md` playbooks.
  - The README says it contains **1,431+ skills**; the prompt title says **1,340+**, but the README itself repeatedly uses **1,431+**.
  - The repo is meant for tools including **Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, Kiro, OpenCode, GitHub Copilot**, and others.

- **Core value proposition**
  - It is **installable**, not just a list of prompts.
  - It provides:
    - an **installer CLI** via `npx antigravity-awesome-skills`
    - **bundles** for role-based starting points
    - **workflows** for ordered execution
    - **plugin-safe distributions** for Claude Code and Codex
    - a generated **catalog** and web UI for browsing skills

- **Version / metadata**
  - The repo header includes sync metadata: `version=10.4.0`, `skills=1431`, `stars=33887`, `updated_at=2026-04-19T07:24:57+00:00`.
  - README states **Current release: V10.4.0.**
  - It claims **34k+ GitHub stargazers**.

- **Installation**
  - Default install:
    ```bash
    npx antigravity-awesome-skills
    ```
  - Default path for Antigravity:
    - `~/.gemini/antigravity/skills`
  - Verify install:
    ```bash
    test -d ~/.gemini/antigravity/skills && echo "Skills installed in ~/.gemini/antigravity/skills"
    ```
  - The README says the npm installer uses a **shallow clone by default** to keep first-run installs lighter than a full history checkout.
  - It also says you can narrow installs with:
    - `--path`
    - `--claude`
    - `--cursor`
    - `--gemini`
    - `--codex`
    - `--antigravity`
    - `--kiro`
    - plus filtering options like `--risk`, `--category`, and `--tags`

- **Tool-specific usage**
  - The README gives per-tool install / first-use examples:
    - **Claude Code**: `npx antigravity-awesome-skills --claude`
    - **Cursor**: `npx antigravity-awesome-skills --cursor`
    - **Gemini CLI**: `npx antigravity-awesome-skills --gemini`
    - **Codex CLI**: `npx antigravity-awesome-skills --codex`
    - **Antigravity**: `npx antigravity-awesome-skills --antigravity`
    - **Kiro CLI/IDE**: CLI flag or `--path ~/.kiro/skills`
    - **OpenCode**: example uses `.agents/skills` with category/risk filters
  - Example first-use phrases include:
    - `@brainstorming`
    - `@test-driven-development`
    - `@debugging-strategies`
    - `@lint-and-validate`
    - `@security-auditor`

- **What the repo contains**
  - `skills/` — skills library
  - `package.json` — installer CLI
  - `CATALOG.md`, `skills_index.json`, `data/` — generated catalog and metadata
  - `apps/web-app` and a **hosted GitHub Pages catalog**
  - docs for:
    - **bundles**
    - **workflows**
    - **plugins**
    - getting started / usage / troubleshooting
    - contributor and maintainer guidance

- **Bundles and workflows**
  - **Bundles** are curated groups of skills for roles like:
    - `Web Wizard`
    - `Security Engineer`
    - `OSS Maintainer`
  - Example bundle combos:
    - SaaS MVP: `Essentials` + `Full-Stack Developer` + `QA & Testing`
    - Production hardening: `Security Developer` + `DevOps & Cloud` + `Observability & Monitoring`
    - OSS shipping: `Essentials` + `OSS Maintainer`
  - **Workflows** are outcome-oriented playbooks, with machine-readable metadata in `data/workflows.json`.
  - Example workflows mentioned:
    - shipping a SaaS MVP
    - security audits
    - AI agent systems
    - QA/browser automation
    - DDD-oriented design work

- **When it is especially useful**
  - If Antigravity hits **context limits** due to too many active skills, the repo points to selective activation guidance.
  - For OpenCode and similar `.agents/skills` hosts, the README recommends a **reduced install up front** rather than copying the full library into a context-sensitive runtime.

- **Contributing / trust signals**
  - Community contributions are handled via `skills/<skill-name>/SKILL.md`.
  - Validation includes `npm run validate`.
  - Community PRs should not commit generated artifacts like `CATALOG.md`, `skills_index.json`, or `data/*.json`.
  - The repo has explicit `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md`.

- **Sources / provenance**
  - The project credits official sources like:
    - Anthropic skills and cookbooks
    - OpenAI skills
    - Google Gemini skills
    - Microsoft skills
    - Supabase, Vercel, Hugging Face, Apify, Expo, Neon, Remotion, Scopeblind, and others
  - It also includes a large community attribution ledger with many third-party skill sources.

### Assessment
This is a **mixed** reference/tutorial repo with strong practical utility and high specificity. **Durability is medium**: the concepts behind agent skills, bundles, workflows, and installable playbooks are likely to stay relevant, but the exact catalog count, tool flags, supported hosts, and version metadata are version-sensitive and can change quickly. **Density is high** because the README compresses installation, compatibility, navigation, and attribution into a single landing page. **Originality is mostly synthesis**: it aggregates official and community skill collections into a curated installable distribution rather than presenting a single original thesis. **Reference style is refer-back** rather than deep-study; the README is meant to orient you, install quickly, and then send you to deeper docs when needed. **Scrape quality is good**: the major README sections, code blocks, metadata, and most source/credit lists are present, though any generated catalog contents, linked docs, and site assets are not fully expanded here.
