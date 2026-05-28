---
url: https://github.com/YYH211/Claude-meta-skill
title: 'YYH211/Claude-meta-skill: A curated collection of reusable skills for Claude Code. Enhance Claude''s capabilities with ready-to-use skill modules including comprehensive guides, templates, and best practices for creating your own skills.'
scraped_at: '2026-04-12T09:44:07Z'
word_count: 2819
raw_file: raw/2026-04-12_yyh211-claude-meta-skill-a-curated-collection-of-reusable-skills-for-claude-code_4556cf4b.txt
tldr: A GitHub repository that packages 10 reusable Claude Code skills—ranging from prompt optimization and DRY refactoring to MCP server building and FastGPT workflow generation—along with install instructions, trigger keywords, and usage guidance.
key_quote: “Each skill is a self-contained module that teaches Claude how to perform specific tasks or follow particular workflows in your projects.”
durability: high
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- YYH211
- OthmanAdi
- ginobefun
tools:
- Claude Code
- FastGPT
- FastMCP
- MCP SDK
- git
libraries: []
companies:
- Anthropic
- FastGPT
tags:
- claude-code
- agent-skills
- prompt-engineering
- workflow-automation
- mcp
---

### TL;DR
A GitHub repository that packages 10 reusable Claude Code skills—ranging from prompt optimization and DRY refactoring to MCP server building and FastGPT workflow generation—along with install instructions, trigger keywords, and usage guidance.

### Key Quote
“Each skill is a self-contained module that teaches Claude how to perform specific tasks or follow particular workflows in your projects.”

### Summary
- **What this repo is**
  - A curated collection of reusable skills for **Claude Code**.
  - Intended to be copied into a project’s `.claude/skills/` directory to extend Claude’s behavior.
  - MIT licensed and positioned as a practical skill library rather than a single tutorial.

- **Available skills (10 total)**
  - **create-skill-file**
    - Meta-skill for writing high-quality `SKILL.md` files.
    - Includes writing guidelines, templates, examples, checklist, and troubleshooting.
    - Trigger keywords: “create skill”, “write skill”, “SKILL.md”, etc.
    - Install: `cp -r create-skill-file .claude/skills/`
    - Has Chinese and English versions.
  - **prompt-optimize**
    - Prompt engineering skill that helps craft better Claude prompts through collaborative dialogue.
    - Mentions CoT, ToT, Self-Consistency, ReAct, safety considerations, and architecture upgrades.
    - Trigger keywords: “optimize prompt”, “improve prompt”, etc.
  - **deep-reading-analyst**
    - Deep reading / analysis skill using 10+ frameworks like SCQA, 5W2H, critical thinking, mental models, and first principles.
    - Points to a separate intro doc and an external GitHub repo as source.
  - **dry-refactoring**
    - Guides refactoring according to DRY with a 4-step workflow:
      1. Identify repetition
      2. Abstract logic
      3. Replace implementation
      4. Verify and test
    - Covers copy-paste code, magic numbers, structural/logical repetition, and testing strategies.
  - **frontend-design**
    - Helps create production-grade frontend interfaces with distinctive aesthetics.
    - Emphasizes avoiding generic AI-style designs, using intentional typography, themes, layout composition, animations, and accessibility.
  - **mcp-builder**
    - Guide for building high-quality **MCP (Model Context Protocol)** servers.
    - Covers research/planning, tool design, implementation, testing, and publishing.
    - Supports **FastMCP/Python** and **MCP SDK/TypeScript**.
  - **daily-ai-news**
    - Aggregates and summarizes recent AI news from multiple sources.
    - Uses web search and reader tools, filters to recent 24–48h content, deduplicates, and categorizes into:
      - Major Announcements
      - Research & Papers
      - Industry & Business
      - Tools & Applications
      - Policy & Ethics
    - Bilingual Chinese/English support, with direct links and templates.
  - **fastgpt-workflow-generator**
    - Generates production-ready **FastGPT workflow JSON** from natural language requirements.
    - Includes AI semantic matching, JSON generation, validation, incremental modification, and built-in templates.
    - Documents reference formats like `["nodeId", "key"]` and `{{$nodeId.key$}}`.
  - **planning-with-files**
    - Manus-style workflow using persistent markdown files as “working memory on disk.”
    - Uses a **3-file pattern**:
      - `task_plan.md` for phases/progress
      - `notes.md` for research/findings
      - `deliverable.md` for final output
    - Focuses on multi-session work, progress tracking, and avoiding context-window overload.
  - **local-diff-review**
    - Pre-PR self-review skill that runs `git diff` locally and reviews changes with the same strict standards as formal PR review.
    - Uses issue grading: Critical / Suggested / Optional.
    - Outputs change overview, issue list, and conclusion.

- **Installation pattern**
  - Create `.claude/skills/` if needed.
  - Copy a skill directory into it using `cp -r`.
  - Restart Claude Code and test with trigger phrases.
  - The repo provides examples of how to verify skill installation by checking `SKILL.md` frontmatter and asking Claude what skills it can access.

- **How the repo is organized**
  - Intro section explains what Claude Skills are and how they extend Claude Code.
  - A table lists each skill with description, source, and install command.
  - Each skill has a detailed subsection with:
    - version/language notes
    - included features
    - trigger keywords
    - installation command
    - sometimes quick-start examples
  - Additional sections cover:
    - usage examples
    - troubleshooting
    - coming soon roadmap
    - resources and official docs
    - contributing
    - license

- **Notable limitations / context**
  - This is primarily a **repository index and installation guide**, not deep technical documentation for every skill.
  - Some skills point to external sources or separate docs.
  - The content is partly promotional (“happy coding”, “production-grade”, “expert skill”) and should be read as project documentation rather than an impartial benchmark.

### Assessment
This is a **mixed** reference/tutorial repository with **medium-to-high durability**: the underlying Claude Skills concepts and workflow patterns are fairly durable, but details like supported tools, trigger phrases, or best practices may evolve as Claude Code changes. The content is fairly **dense** because it packs installation commands, feature lists, and skill-specific summaries into a single README-style document. Its originality is mainly **synthesis**—it assembles multiple reusable skills into one curated repo, with some sections linking to external sources. As a reference, it’s best used **refer-back** rather than deep study: useful for choosing a skill, checking install steps, or quickly recalling what each module does. Scrape quality appears **good** overall, with most of the README captured, including tables, code blocks, and section structure, though some linked sub-docs and repository files are only referenced, not included.
