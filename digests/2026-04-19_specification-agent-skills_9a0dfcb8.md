---
url: https://agentskills.io/specification
title: Specification - Agent Skills
scraped_at: '2026-04-19T04:00:31Z'
word_count: 1140
raw_file: raw/2026-04-19_specification-agent-skills_9a0dfcb8.txt
tldr: Agent Skills’ specification defines how to package a skill as a directory with a required `SKILL.md` frontmatter file, optional `scripts/`, `references/`, and `assets/` folders, and rules for naming, metadata, progressive disclosure, and validation.
key_quote: “The complete format specification for Agent Skills.”
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- skills-ref
libraries: []
companies:
- Agent Skills
- Mintlify
- GitHub
tags:
- documentation
- file-structure
- metadata
- validation
- agent-systems
---

### TL;DR
Agent Skills’ specification defines how to package a skill as a directory with a required `SKILL.md` frontmatter file, optional `scripts/`, `references/`, and `assets/` folders, and rules for naming, metadata, progressive disclosure, and validation.

### Key Quote
“The complete format specification for Agent Skills.”

### Summary
- **What this page is:** the official format specification for creating an Agent Skill.
- **Required structure:**
  - A skill is a directory with at minimum:
    - `SKILL.md` — required, contains metadata + instructions
    - optional `scripts/`, `references/`, `assets/`, and any other files
- **`SKILL.md` format:**
  - Must start with **YAML frontmatter**, followed by **Markdown body content**
- **Frontmatter fields:**
  - `name` — required
    - 1–64 characters
    - lowercase letters, numbers, hyphens only
    - cannot start/end with `-`
    - cannot contain consecutive hyphens
    - must match the parent directory name
  - `description` — required
    - 1–1024 characters
    - should explain what the skill does and when to use it
    - should include keywords relevant to agent task matching
  - `license` — optional
    - license name or bundled license file reference
  - `compatibility` — optional
    - environment requirements, such as product, packages, network, Python version
    - most skills don’t need it
  - `metadata` — optional
    - arbitrary string key/value pairs
  - `allowed-tools` — optional and **experimental**
    - space-separated list of pre-approved tools
- **Body content guidance:**
  - No strict format requirements after frontmatter
  - Recommended to include:
    - step-by-step instructions
    - input/output examples
    - common edge cases
  - Keep in mind the agent loads the full file once a skill is activated, so longer content should be split into referenced files
- **Optional directories:**
  - `scripts/`
    - executable code for the agent to run
    - should be self-contained or clearly document dependencies
    - should include helpful errors and handle edge cases
    - common languages: Python, Bash, JavaScript
  - `references/`
    - extra documentation loaded on demand
    - examples: `REFERENCE.md`, `FORMS.md`, domain-specific docs
    - keep files focused to reduce context usage
  - `assets/`
    - static resources like templates, diagrams, images, schemas, lookup tables
- **Progressive disclosure model:**
  - `name` + `description` are loaded at startup for all skills
  - full `SKILL.md` body is loaded only when the skill is activated
  - resources in other folders are loaded only when needed
  - recommendation: keep `SKILL.md` under 500 lines and under ~5000 tokens
- **File references:**
  - use relative paths from the skill root
  - keep references one level deep from `SKILL.md`
  - avoid deep chains of references
- **Validation:**
  - use `skills-ref validate ./my-skill`
  - this checks frontmatter validity and naming conventions
- **Page context:**
  - The site notes an official Agent Skills Discord server and links to a GitHub announcement.
  - The page is documentation on Mintlify and includes the standard “AI may contain mistakes” disclaimer.

### Assessment
This is a **reference** document with **high** durability for the core ideas, though some implementation details like the experimental `allowed-tools` field and the linked Discord/announcement may change over time. The page is **high-density** and mostly **primary-source** specification text, not commentary or synthesis. It’s best used as a **refer-back** resource when creating or validating skills, since the structure, field constraints, and directory conventions are the kinds of details you’ll want to check again later. Scrape quality appears **good**: the main content, tables, examples, and section structure are present, with no obvious missing code blocks or major sections.
