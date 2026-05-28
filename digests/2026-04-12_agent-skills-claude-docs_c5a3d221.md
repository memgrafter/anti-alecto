---
url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
title: Agent Skills - Claude Docs
scraped_at: '2026-04-12T07:22:22Z'
word_count: 2293
raw_file: raw/2026-04-12_agent-skills-claude-docs_c5a3d221.txt
tldr: Claude Agent Skills are filesystem-based, modular extensions that give Claude reusable domain expertise and tools, with progressive loading, surface-specific support, and important security/data-retention constraints.
key_quote: Progressive disclosure ensures only relevant content occupies the context window at any given time.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people: []
tools:
- bash
- pdfplumber
libraries: []
companies:
- Anthropic
tags:
- ai-agents
- developer-tools
- filesystem
- security
- documentation
---

### TL;DR
Claude Agent Skills are filesystem-based, modular extensions that give Claude reusable domain expertise and tools, with progressive loading, surface-specific support, and important security/data-retention constraints.

### Key Quote
"Progressive disclosure ensures only relevant content occupies the context window at any given time."

### Summary
- **What Skills are**
  - Modular capabilities that extend Claude’s functionality.
  - Package **instructions, metadata, and optional resources** like scripts and templates.
  - Claude uses them **automatically when relevant**.

- **Why use them**
  - Reusable, filesystem-based expertise for specific domains or workflows.
  - Unlike one-off prompts, Skills:
    - reduce repeated instructions across conversations
    - let Claude specialize
    - can be composed into larger workflows

- **How they work**
  - Skills run in Claude’s **VM/code execution environment** with filesystem access.
  - They use **progressive disclosure**:
    - **Level 1: Metadata** — YAML frontmatter, always loaded at startup
      - Example fields: `name`, `description`
      - Rough cost noted: ~100 tokens per Skill
    - **Level 2: Instructions** — `SKILL.md` body loaded only when triggered
      - Procedural guidance, workflows, best practices
      - Rough cost noted: under 5k tokens
    - **Level 3+: Resources/code** — extra markdown files, scripts, schemas, templates
      - Loaded only when referenced
      - Executable scripts run via bash; only output enters context
      - Effectively unlimited bundled content

- **Skill structure**
  - Every Skill requires a `SKILL.md` file with YAML frontmatter:
    - `name`
      - max 64 characters
      - lowercase letters, numbers, hyphens only
      - cannot include XML tags
      - cannot use reserved words like `"anthropic"` or `"claude"`
    - `description`
      - required, non-empty
      - max 1024 characters
      - cannot include XML tags
      - should explain both what it does and when to use it
  - The page includes an example PDF-processing Skill structure with:
    - `SKILL.md`
    - `FORMS.md`
    - `REFERENCE.md`
    - `scripts/fill_form.py`

- **Where Skills work**
  - **Claude API**
    - Supports both pre-built and custom Skills
    - Uses `skill_id` in the `container` parameter with code execution
    - Requires beta headers:
      - `code-execution-2025-08-25`
      - `skills-2025-10-02`
      - `files-api-2025-04-14`
    - Custom Skills are shared **organization-wide**
  - **Claude Code**
    - Supports only **custom Skills**
    - Skills are filesystem directories with `SKILL.md`
    - Automatically discovered; no API upload needed
  - **Claude.ai**
    - Supports both pre-built and custom Skills
    - Pre-built Skills work automatically
    - Custom Skills are uploaded as zip files in **Settings > Features**
    - Available on **Pro, Max, Team, and Enterprise** with code execution enabled
    - Custom Skills are **per-user**, not org-wide

- **Available Skills listed**
  - Pre-built Skills:
    - **PowerPoint (pptx)**: create/edit/analyze presentations
    - **Excel (xlsx)**: spreadsheets, analysis, reports, charts
    - **Word (docx)**: create/edit/format documents
    - **PDF (pdf)**: generate formatted PDFs and reports
  - Open-source Skills:
    - Anthropic publishes a Claude API Skills repository with up-to-date API references, SDK docs, and best practices for 8 programming languages

- **Security considerations**
  - Strong recommendation: use Skills only from **trusted sources**
  - Risks include:
    - malicious tool invocation
    - unauthorized system access
    - data exfiltration
    - harmful external URL fetching
  - Advice: audit all bundled files, scripts, and external dependencies carefully

- **Data retention**
  - Agent Skills are **not eligible for Zero Data Retention (ZDR)**
  - Skill definitions and execution data follow Anthropic’s standard retention policy

- **Limitations and constraints**
  - **No cross-surface sync**
    - Claude.ai, API, and Claude Code Skills are separate
  - **Sharing differs by surface**
    - Claude.ai: individual user only
    - Claude API: workspace-wide
    - Claude Code: personal or project-based, also via plugins
  - **Runtime environment constraints**
    - Claude.ai: network access may vary by settings
    - Claude API: no network access; no installing packages at runtime
    - Claude Code: full network access, but package installation should be local and not system-wide

- **Overall intent of the page**
  - This is a **product/reference overview** for understanding what Agent Skills are, how they’re loaded and executed, where they’re supported, and what operational/security constraints apply.

### Assessment
This is a **high-durability reference** with mixed content: mostly product documentation, with some tutorial-like setup details and a few implementation specifics. It is **high-density** because it includes architecture, loading behavior, API requirements, sharing models, and security guidance, plus concrete field constraints and beta header names. The material is **primarily source documentation** rather than commentary or synthesis. It’s best used as a **refer-back** or **deep-study** reference, especially if you plan to create or deploy Skills. Scrape quality looks **good overall**: the page content appears substantially captured, including tables, examples, and section structure, though image/diagram content is only described in text rather than visually preserved.
