---
url: https://github.com/ComposioHQ/awesome-claude-skills
title: 'ComposioHQ/awesome-claude-skills: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows'
scraped_at: '2026-04-19T08:32:18Z'
word_count: 3338
raw_file: raw/2026-04-19_composiohq-awesome-claude-skills-a-curated-list-of-awesome-claude-skills-resourc_6b401487.txt
tldr: A curated GitHub index of Claude Skills, templates, and resources for Claude.ai, Claude Code, and the Claude API, with a major Composio-powered section for automating real actions across many SaaS apps.
key_quote: Claude can send emails, create issues, post to Slack, and take actions across 1000+ apps.
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: partial
people:
- Anthropic
- Lenny
- Composio
tools:
- Claude.ai
- Claude Code
- Claude API
- connect-apps
- Rube MCP
libraries: []
companies:
- ComposioHQ
- Anthropic
- Google
- OpenAI
tags:
- claude-skills
- ai-automation
- workflow-templates
- saas-integrations
- prompt-engineering
---

### TL;DR
A curated GitHub index of Claude Skills, templates, and resources for Claude.ai, Claude Code, and the Claude API, with a major Composio-powered section for automating real actions across many SaaS apps.

### Key Quote
"Claude can send emails, create issues, post to Slack, and take actions across 1000+ apps."

### Summary
- This repository is an **“awesome list”** of Claude Skills: practical workflows and tools for customizing Claude across:
  - Claude.ai
  - Claude Code
  - Claude API
- It frames Claude Skills as **repeatable, standardized workflows** that teach Claude how to perform specific tasks consistently.
- The README includes a **Quickstart** for the `connect-apps` plugin:
  - Install with `claude --plugin-dir ./connect-apps-plugin`
  - Run `/connect-apps:setup`
  - Paste an API key from Composio
  - Restart Claude and test by sending an email or other action
  - It claims the plugin connects Claude to **500+ apps** under the hood.
- The repo’s main body is a categorized catalog of skills, including:
  - **Document Processing**: `docx`, `pdf`, `pptx`, `xlsx`
  - **Development & Code Tools**: artifacts builder, changelog generator, terminal title, D3 visualization, fuzzing, iOS simulator, Playwright, TDD, git worktrees, MCP Builder, skill creator, etc.
  - **Data & Analysis**: CSV summarization, deep research, Postgres, root-cause tracing
  - **Business & Marketing**: brand guidelines, competitive ads extraction, domain brainstorming, internal comms, lead research
  - **Communication & Writing**: article extraction, brainstorming, content research writing, meeting insights, NotebookLM integration, Twitter optimization
  - **Creative & Media**: design, image enhancement, GIF creation, themes, video downloading, transcript fetching
  - **Productivity & Organization**: file organizing, invoice organizing, raffle picker, resume generator, knowledge linking
  - **Collaboration & Project Management**: git pushing, Google Workspace, Outline, test-fixing, review-implementing
  - **Security & Systems**: computer forensics, secure file deletion, metadata extraction, Sigma threat hunting
- A large section, **“App Automation via Composio,”** lists **pre-built workflow skills for 78 SaaS apps via Rube MCP (Composio)**.
  - These are grouped by category:
    - CRM & Sales
    - Project Management
    - Communication
    - Email
    - Code & DevOps
    - Storage & Files
    - Spreadsheets & Databases
    - Calendar & Scheduling
    - Social Media
    - Marketing & Email Marketing
    - Support & Helpdesk
    - E-commerce & Payments
    - Design & Collaboration
    - Analytics & Data
    - HR & People
    - Automation Platforms
    - Zoom & Meetings
  - The section emphasizes that each skill includes:
    - tool sequences
    - parameter guidance
    - known pitfalls
    - quick reference tables
- The README also explains:
  - **How to use skills** in Claude.ai, Claude Code, and via the API
  - **Skill structure**: a folder with `SKILL.md`, plus optional `scripts/`, `templates/`, and `resources/`
  - A **basic YAML frontmatter template** for creating a skill
  - **Best practices** for writing skills: specific tasks, examples, edge cases, prerequisites, and error handling
- It includes:
  - Contribution guidance
  - Official documentation links
  - Community resources
  - Inspiration/use-case links
  - License notes: the repo is **Apache 2.0**, though individual skills may have their own licenses

### Assessment
This is a **mixed reference/announcement** style README that functions mainly as a curated directory rather than an original technical deep dive. **Durability is medium**: the core ideas about Claude Skills and skill structure are fairly stable, but the app inventory, plugin instructions, and platform-specific setup details are likely to change as Claude/Composio evolve. **Content type** is mostly **reference** with some tutorial elements in the quickstart and creating-skills sections. **Density is high** because it packs a lot of categorized links, platform instructions, and template guidance into one README. **Originality** is best described as a **synthesis/curation hub**: it organizes external skills and docs, with some original Composio-authored guidance and marketing framing, but it is not primarily a novel research piece. **Reference style** is clearly **refer-back** for finding skills or setup instructions, though the quickstart can be skimmed once for immediate use. **Scrape quality** is **partial**: the README text is captured well, but many linked subpages, skill folders, and any code/examples inside them are not included, so this is good for overview and discovery but not sufficient for the full contents of each skill.
