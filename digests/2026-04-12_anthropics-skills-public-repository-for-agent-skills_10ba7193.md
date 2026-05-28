---
url: https://github.com/anthropics/skills
title: 'anthropics/skills: Public repository for Agent Skills'
scraped_at: '2026-04-12T09:43:31Z'
word_count: 707
raw_file: raw/2026-04-12_anthropics-skills-public-repository-for-agent-skills_10ba7193.txt
tldr: Anthropic’s `anthropics/skills` repo is a reference and demo collection for Claude Agent Skills, showing how skills are packaged, installed, and used across Claude Code, Claude.ai, and the Claude API.
key_quote: “Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Anthropic
- Claude
- Notion
tools:
- Claude Code
- Claude.ai
- Claude API
- MCP
libraries: []
companies:
- Anthropic
- Notion
tags:
- agent-skills
- claude
- documentation
- developer-tools
- repository-reference
---

### TL;DR
Anthropic’s `anthropics/skills` repo is a reference and demo collection for Claude Agent Skills, showing how skills are packaged, installed, and used across Claude Code, Claude.ai, and the Claude API.

### Key Quote
“Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.”

### Summary
- This is a **public repository for Anthropic’s implementation of skills for Claude**.
- It points readers to the broader **Agent Skills standard** at `agentskills.io`.
- The repo’s purpose is to demonstrate what Claude’s skills system can do:
  - **Creative applications**: art, music, design
  - **Technical tasks**: testing web apps, generating MCP servers
  - **Enterprise workflows**: communications, branding, and similar work
- Each skill is organized as a **self-contained folder** with a `SKILL.md` file containing:
  - instructions
  - metadata
  - behavior Claude should follow when the skill is active
- The repository includes:
  - `./skills` — example skills for Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills
  - `./spec` — the Agent Skills specification
  - `./template` — a skill template
- Anthropic says many skills in the repo are **open source under Apache 2.0**.
- It also includes document creation/editing skills used by Claude’s document capabilities:
  - `skills/docx`
  - `skills/pdf`
  - `skills/pptx`
  - `skills/xlsx`
- These document skills are described as **source-available, not open source**, and are included to show more complex, production-used patterns.
- Important caveat: the skills are explicitly for **demonstration and educational purposes only**.
  - Claude’s actual behavior may differ from what is shown.
  - Users are told to **test skills thoroughly before relying on them for critical tasks**.
- Usage paths are described for three environments:
  - **Claude Code**
    - add the repo as a plugin marketplace with `/plugin marketplace add anthropics/skills`
    - install plugins like `document-skills@anthropic-agent-skills` or `example-skills@anthropic-agent-skills`
  - **Claude.ai**
    - example skills are already available to paid plans
    - custom skills can also be uploaded
  - **Claude API**
    - pre-built skills and custom skills can be used via the Skills API
- The repo also explains how to create a **basic skill**:
  - make a folder
  - add a `SKILL.md`
  - include YAML frontmatter with:
    - `name`
    - `description`
  - then write markdown instructions, examples, and guidelines
- The repo highlights a partner example:
  - **Notion** — “Notion Skills for Claude”

### Assessment
This is a **reference**-style repository with some tutorial and product-documentation elements mixed in. Its durability is **medium**: the core idea of skills and the `SKILL.md` structure is likely to remain useful, but plugin commands, supported surfaces, and repo contents may change as Anthropic’s product evolves. The content is fairly **dense** because it packs definition, architecture, usage instructions, file structure, and installation commands into a relatively short README. It is primarily a **primary source** from Anthropic rather than commentary or synthesis. This is best used as a **refer-back** resource if you want to implement or browse skills, not just a one-time skim. Scrape quality is **good** overall: the main README content, commands, and structure are captured, though repository subfolder details and the linked documentation pages are not included here.
