---
url: https://github.com/libukai/awesome-agent-skills
title: 'libukai/awesome-agent-skills: Agent Skills 终极指南：快速入门、资源推荐、精选技能与实用工具 ｜The Ultimate Guide to Agent Skills: QuickStart, Resources, Features&Toolkit'
scraped_at: '2026-04-19T08:33:45Z'
word_count: 675
raw_file: raw/2026-04-19_libukai-awesome-agent-skills-agent-skills-the-ultimate-guide-to-agent-skills-qui_ade8df8b.txt
tldr: This is a curated Chinese/English/Japanese “awesome list” for Agent Skills that explains what Skills are, how to install them across Claude, Claude Code, OpenClaw, and Chinese ecosystems, and where to find official projects, tutorials, security guidance, and a Claude Code plugin toolkit for creating Skills.
key_quote: Skill 是一种轻量级的 Agent 构建方案，通过封装特定的业务流程与行业知识，强化 AI 执行特定任务的专业能力。
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- 李不凯正在研究
- 一泽 Eze
- deeptoai
- 马克的技术工作坊
- 宝玉
- 余弦
tools:
- Claude
- ChatGPT
- Cursor
- Claude Code
- OpenClaw
- skillsmp
- skills.sh
- npx skills
- ClawHub
- SkillHub
- skill-creator
- agent-skills-toolkit
- slowmist-agent-security
- OpenClaw
libraries:
- n8n
- Three.js
companies:
- Anthropic
- Google
- Vercel
- Tencent
- OpenAI
- Gemini
- Hugging Face
- Replicate
- ElevenLabs
- Black Forest Labs
- Cloudflare
- HashiCorp
- Databricks
- ClickHouse
- Supabase
- Stripe
- LaunchDarkly
- Sentry
- Microsoft
- Expo
- Better Auth
- Posit
- Remotion
- Slidev
- Notion
- Obsidian
- WordPress
- Dify
- Sanity
- WPS
- ListenHub
- Firecrawl
tags:
- agent-skills
- claude-code
- ai-agents
- skill-marketplaces
- prompt-engineering
---

### TL;DR
This is a curated Chinese/English/Japanese “awesome list” for Agent Skills that explains what Skills are, how to install them across Claude, Claude Code, OpenClaw, and Chinese ecosystems, and where to find official projects, tutorials, security guidance, and a Claude Code plugin toolkit for creating Skills.

### Key Quote
> “Skill 是一种轻量级的 Agent 构建方案，通过封装特定的业务流程与行业知识，强化 AI 执行特定任务的专业能力。”

### Summary
- **What this repo is**
  - A “少而精” curated resource hub for Agent Skills, emphasizing high-quality Skill resources, tutorials, practice cases, and tool links.
  - Bilingual/trilingual navigation is provided: **简体中文 | English | 日本語**.
  - The repo is framed as a practical guide for getting started with building and using agents via Skills.

- **Core concept of Skill**
  - Skills are described as a lightweight way to build agents by packaging:
    - business workflows
    - domain knowledge
    - reference materials
    - scripts
    - assets
  - The goal is to avoid repeating background/context in every conversation; once installed, AI can “learn” the skill as needed.
  - The page claims Skills have become a standard approach for boosting vertical-domain AI capability and are widely supported by agent frameworks and AI products.

- **Standard Skill structure**
  - A Skill is a normalized folder containing:
    - `SKILL.md` — required; workflow instructions and metadata
    - `references/` — optional reference docs
    - `scripts/` — optional executable scripts
    - `assets/` — optional templates/resources

- **How to install Skills**
  - Skills can be used in:
    - GUI apps like **Claude** and **ChatGPT**
    - coding IDE/TUI tools like **Cursor** and **Claude Code**
    - Agent Harnesses like **OpenClaw**
  - Installation is described as placing the Skill folder into a specific directory so the AI can load it when needed.

- **Claude App ecosystem**
  - Skills can be installed either from the built-in Skill store or by uploading a ZIP package.
  - If a Skill is missing from the official store, the page points users to third-party stores.

- **Claude Code ecosystem**
  - Recommends **skillsmp** (`skillsmp.com/zh`) as a marketplace that aggregates GitHub Skill projects and sorts them by category, update time, and star count.
  - Mentions **skills.sh** by Vercel as a popularity leaderboard.
  - Recommends the CLI tool **`npx skills`** from `vercel-labs/skills`, with commands:
    - `npx skills find [query]`
    - `npx skills add <owner/repo>`
    - `npx skills list`
    - `npx skills check`
    - `npx skills update`
    - `npx skills remove [skill-name]`

- **OpenClaw ecosystem**
  - For official OpenClaw users with internet access, it recommends **ClawHub** (`clawhub.com`) with more technical skills and many overseas product integrations.
  - CLI commands listed:
    - `npx clawhub search [query]`
    - `npx clawhub explore`
    - `npx clawhub install <slug>`
    - `npx clawhub uninstall <slug>`
    - `npx clawhub list`
    - `npx clawhub update --all`
    - `npx clawhub inspect <slug>`
  - For China-network or China-customized OpenClaw users, it recommends Tencent’s **SkillHub** (`skillhub.tencent.com`).
  - SkillHub CLI install command is provided:
    - `curl -fsSL https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash`
  - SkillHub usage commands:
    - `skillhub search [query]`
    - `skillhub install <skill-name>`
    - `skillhub list`
    - `skillhub upgrade`

- **Tutorials and guides**
  - **Official docs** linked:
    - Anthropic: “Claude Skill 完全构建指南”
    - Anthropic: “Claude Agent Skills 实战经验”
    - Google: “Agent Skills 五种设计模式”
  - **Illustrated tutorials**:
    - A PPT intro by the author
    - A WeChat article by 一泽 Eze
    - A deep-dive by deeptoai
  - **Video tutorials**:
    - A YouTube workshop by 马克的技术工作坊
    - A post/video by 宝玉

- **Official projects list**
  - The repo includes a table of official-ish or major Skill repositories grouped by category:
    - **AI models & platforms**: Anthropic, OpenAI, Gemini, Hugging Face, Replicate, ElevenLabs, Black Forest Labs
    - **Cloud/infrastructure**: Cloudflare, HashiCorp, Databricks, ClickHouse, Supabase, Stripe, LaunchDarkly, Sentry
    - **Frameworks/tools**: Vercel, Microsoft, Expo, Better Auth, Posit, Remotion, Slidev, agent-browser, browser-use, Firecrawl, GSAP
    - **Content/collaboration**: Notion, Obsidian, WordPress, Dify, Sanity, Podwise, WPS, ListenHub
  - This section functions as a directory of notable Skill repositories rather than an evaluation.

- **Selected Skills**
  - **Programming/development**
    - `superpowers` — complete programming workflow
    - `frontend-design` — frontend design
    - `ui-ux-pro-max-skill` — more polished/personalized UI/UX
    - `code-review` — code review
    - `code-simplifier` — code simplification
    - `commit-commands` — Git commit skills
  - **Content creation**
    - `baoyu-skills` — writing, PPT creation, etc.
    - `libukai` — Obsidian-oriented writing skills
    - `op7418` — PPT and YouTube analysis
    - `cclank` — news aggregation and summaries
    - `huangserva` — AI portrait prompt generation
    - `dontbesilent2025/dbskill` — content framework based on an X creator’s posts
    - `seekjourney/md2wechat-skill` — from writing to WeChat publishing
  - **Product usage**
    - `wps` — control WPS
    - `notebooklm` — control NotebookLM
    - `n8n` — create workflows
    - `threejs` — assist in Three.js development
  - **Other**
    - `pua` — “drive AI harder” via PUA-style prompting
    - `office-hours` — YC-style startup advice
    - `marketingskills` — marketing capability
    - `scientific-skills` — research workflows for scientists

- **Security guidance**
  - Warns that Skills may contain:
    - external API calls
    - silent scheduled scripts
    - other potentially risky operations
  - Advises installing from official or well-known marketplaces and reading descriptions/reviews carefully.
  - Recommends:
    - `slowmist-agent-security` for auditing Skills
    - `openclaw-security-practice-guide` for system-prompt-level safety constraints in highly autonomous harnesses

- **Creating your own Skills**
  - Encourages customizing or building Skills yourself for better fit and personalization.
  - Links to Anthropic’s official **skill-creator** plugin.
  - Introduces an enhanced **Agent Skills Toolkit** built from Anthropic and Google best practices, but notes it **currently only supports Claude Code**.
  - Workflow to add the market:
    - `/plugin marketplace add libukai/awesome-agent-skills`
  - After installation, users can install the `agent-skills-toolkit` plugin.
  - Shortcut commands:
    - `/agent-skills-toolkit:skill-creator-pro`
    - `/agent-skills-toolkit:create-skill`
    - `/agent-skills-toolkit:improve-skill`
    - `/agent-skills-toolkit:test-skill`

- **Repo metadata**
  - Apache-2.0 license
  - “Issues welcome”
  - Contains a star history chart
  - Includes promotional banners and images for related ecosystems/tools

### Assessment
Durability is **medium**: the underlying concepts of Skill packaging, folder structure, and safety concerns are fairly durable, but many marketplace names, product ecosystems, CLI commands, and repo links are tied to current tooling and could change quickly. Content type is **mixed**, combining reference, tutorial, directory, and promotional/curated resource list. Density is **high** because it packs many concrete repo names, commands, and ecosystem-specific recommendations into a single page. Originality is best described as **synthesis**: it aggregates official docs, third-party tools, and selected projects rather than presenting original research. Reference style is **refer-back** for anyone working with Agent Skills, especially if they need installation options or curated project links; it can also be skim-once for a quick orientation. Scrape quality is **good** overall: the structure, tables, commands, and major sections are present, though embedded images and linked PDFs/videos are referenced rather than fully captured, and some linked content is external to the scrape.
