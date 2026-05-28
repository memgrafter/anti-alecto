---
url: https://github.com/VoltAgent/awesome-agent-skills
title: 'VoltAgent/awesome-agent-skills: Claude Code Skills and 1000+ agent skills from official dev teams and the community, compatible with Codex, Antigravity, Gemini CLI, Cursor and others.'
scraped_at: '2026-04-19T08:33:26Z'
word_count: 11992
raw_file: raw/2026-04-19_voltagent-awesome-agent-skills-claude-code-skills-and-1000-agent-skills-from-off_eaa907a9.txt
tldr: A curated GitHub index of 1,184+ “Agent Skills” from major engineering teams and the community, with compatibility paths for Claude Code, Codex, Cursor, Gemini CLI, and other assistants.
key_quote: “Unlike many bulk-generated skill repositories, this collection focuses on real-world Agent Skills created and used by actual engineering teams, not mass AI‑generated stuff.”
durability: high
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Corey Haines
- Paweł Huryn
- Dean Peters
- Garry Tan
- Addy Osmani
tools:
- Claude Code
- Codex
- Antigravity
- Gemini CLI
- Cursor
- GitHub Copilot
- OpenCode
- Windsurf
- Playwright
- n8n
libraries:
- React
- Next.js
- Flutter
- Terraform
- GraphQL
- MongoDB
- Apache Airflow
companies:
- VoltAgent
- Anthropic
- Google
- Vercel
- Stripe
- Cloudflare
- Netlify
- Trail of Bits
- Sentry
- Expo
- Hugging Face
- Figma
- Microsoft
- OpenAI
- Supabase
- Auth0
- Brave
- Firebase
tags:
- agent-skills
- ai-agents
- developer-tools
- github-repository
- reference-directory
---

### TL;DR
A curated GitHub index of 1,184+ “Agent Skills” from major engineering teams and the community, with compatibility paths for Claude Code, Codex, Cursor, Gemini CLI, and other assistants.

### Key Quote
“Unlike many bulk-generated skill repositories, this collection focuses on real-world Agent Skills created and used by actual engineering teams, not mass AI‑generated stuff.”

### Summary
- **What this repo is**
  - A large curated collection of **Agent Skills** hosted by VoltAgent.
  - Emphasizes **official skills** from companies and teams like **Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Expo, Hugging Face, Figma, Microsoft, OpenAI**, and many others.
  - Positions itself against low-quality mass-generated skill dumps: “**Hand-picked, not AI-slop generated**.”

- **Scale and scope**
  - Badge shows **Skills-1184+**.
  - Claims to be “**the most contributed Agent Skills repository**,” maintained with the community.
  - Includes both:
    - **Official skills** from vendor/dev teams
    - **Community skills** across marketing, productivity, development, research, security, and more

- **What kinds of skills are listed**
  - **Document/workflow skills**: DOCX, PPTX, XLSX, PDF creation/editing, Notion knowledge capture, meeting prep, spreadsheets, transcription.
  - **Development skills**: React, Next.js, Flutter, Terraform, GraphQL, MongoDB, Azure SDKs, WordPress, Expo, Cloudflare, Netlify, Playwright, GitHub workflows.
  - **AI/agent infrastructure**: MCP servers, agent orchestration, memory systems, context engineering, evaluation, tool design.
  - **Security skills**: Trail of Bits security analysis, static analysis, Semgrep, threat modeling, secure contracts, secret detection.
  - **Marketing/PM skills**: SEO, copywriting, positioning, roadmap planning, pricing, customer research, GTM strategy.
  - **Domain-specific skills**: finance, observability, Web3/crypto, video, documents, accessibility, iOS, data systems, etc.

- **Notable structure**
  - Organized into large sections by source:
    - **Official Claude Skills**
    - **Skills by VoltAgent**
    - Vendor/team sections such as **Google Gemini, Stripe, Cloudflare, OpenAI, Microsoft, Figma, Auth0, Brave, Firebase, Flutter, DuckDB, GSAP, MongoDB**, etc.
    - **Community Skills**
    - **Context Engineering**
    - **Specialized Domains**
    - **n8n Automation**
  - Many sections are collapsible `<details>` blocks, suggesting the page is meant for browsing and discovery rather than reading linearly.

- **Compatibility / installation paths**
  - Gives path conventions for multiple agent platforms:
    - **Antigravity**: `.agent/skills/`
    - **Claude Code**: `.claude/skills/`
    - **Codex**: `.agents/skills/`
    - **Cursor**: `.cursor/skills/`
    - **Gemini CLI**: `.gemini/skills/`
    - **GitHub Copilot**: `.github/skills/`
    - **OpenCode**: `.opencode/skills/`
    - **Windsurf**: `.windsurf/skills/`
  - Also lists official docs links for each tool.

- **Safety / trust warning**
  - The repo explicitly warns that the skills are **curated, not audited**.
  - It recommends reviewing source code before use because skills may include:
    - prompt injections
    - tool poisoning
    - hidden malware payloads
    - unsafe data handling
  - Suggested scanning tools include:
    - **Snyk Skill Security Scanner**
    - **Agent Trust Hub**

- **Quality standards**
  - Includes criteria for skill authors:
    - use **third-person descriptions**
    - keep metadata concise
    - use **progressive disclosure**
    - avoid **absolute paths**
    - declare **scoped tools** only
  - These standards indicate the repo is also trying to shape ecosystem conventions.

- **Contribution / maintenance**
  - Accepts PRs for new skills and improvements.
  - Explicitly says not to submit very new skills: it prefers **community-adopted, proven skills**.
  - The repo is MIT licensed.
  - It provides an issue path for takedown/bug reports.

### Assessment
This is a **reference** repository with **high durability** in concept but **medium durability** in details, because the specific skill list, counts, and compatibility notes will change as the ecosystem evolves. The content type is **mixed**: mostly a curated reference directory, plus a short announcement/positioning statement and safety guidance. Density is **high** because it packs a very large catalog of specific skill names, organizations, and use cases into one page. Originality is mostly **synthesis/curation** rather than original research; the repo aggregates and organizes skills from many external sources. It’s best used as a **refer-back** resource for finding skills by vendor, domain, or tool. Scrape quality is **good** overall: the major sections, lists, warnings, and path tables are present, though the page is extremely long and some linked skill contents are not included here.
