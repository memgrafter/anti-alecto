---
url: https://github.com/dotcommander/cclint
title: 'dotcommander/cclint: Linter for Claude Code agents, commands, and skills'
scraped_at: '2026-04-12T09:43:01Z'
word_count: 193
raw_file: raw/2026-04-12_dotcommander-cclint-linter-for-claude-code-agents-commands-and-skills_43f06e05.txt
tldr: cclint is a Go-based linter for Claude Code agents, commands, skills, plugins, and settings that checks schema, structure, cross-file references, and quality scores, with baseline mode for gradual adoption.
key_quote: A linter for Claude Code components. Catches schema errors, enforces structure, and flags cross-file problems before they surface as confusing runtime behavior.
durability: medium
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- cclint
- go
libraries: []
companies:
- dotcommander
tags:
- code-linting
- cli-tools
- go-programming
- configuration-validation
- developer-tools
---

### TL;DR
`cclint` is a Go-based linter for Claude Code agents, commands, skills, plugins, and settings that checks schema, structure, cross-file references, and quality scores, with baseline mode for gradual adoption.

### Key Quote
“A linter for Claude Code components. Catches schema errors, enforces structure, and flags cross-file problems before they surface as confusing runtime behavior.”

### Summary
- **What it is**
  - `cclint` is a linter for Claude Code components.
  - It covers **agents, commands, skills, plugins, and settings**.
  - Its goal is to catch issues before they become runtime problems.

- **Install**
  - Install with Go:
    ```bash
    go install github.com/dotcommander/cclint@latest
    ```

- **Basic usage**
  - Lint everything under the default Claude directory:
    ```bash
    cclint
    ```
  - Lint a specific component type:
    ```bash
    cclint agents
    ```
  - Lint specific files:
    ```bash
    cclint ./path/to/file.md
    ```
  - Lint only staged files for pre-commit workflows:
    ```bash
    cclint --staged
    ```
  - Produce quality scores from 0–100:
    ```bash
    cclint --scores
    ```
  - Auto-format component files:
    ```bash
    cclint fmt --write
    ```

- **What it catches**
  - **Frontmatter schema errors**, including embedded CUE schemas
  - **Size, structure, and naming violations** by component type
  - **Cross-file problems**
    - broken references
    - orphaned skills
    - ghost triggers
  - **Settings validation**
    - hooks
    - permissions
    - MCP servers
    - security-related configuration
  - **Delegation anti-patterns** in commands and agents

- **Baseline mode**
  - Designed for projects that already have lint issues.
  - Workflow:
    ```bash
    cclint --baseline-create
    cclint --baseline
    ```
  - `--baseline-create` snapshots the current state.
  - `--baseline` fails only on newly introduced issues.
  - The baseline file should be committed as `.cclintbaseline.json`.
  - The project can then be tightened gradually over time.

- **Quality scoring**
  - Each component receives a **0–100 score**.
  - Score dimensions include:
    - structural completeness
    - practices
    - composition
    - documentation
  - Scores map to **A–F tier grades**.
  - Intended use: help prioritize what to fix first.

- **Where to look next**
  - The page points to `docs/README.md` for:
    - setup
    - CI integration
    - contributor guides

### Assessment
This is a **reference/tool** page with fairly high practical density: it quickly tells you what `cclint` does, how to install it, and the main commands you’d use day to day. Durability is **medium** because the core linting concepts are stable, but the exact CLI flags, supported component types, and integration details may change with repository versions. The content is a **primary source** from the project README, so it’s useful for evaluating the tool’s stated capabilities, though it’s naturally promotional and not a benchmark or third-party review. It works best as a **refer-back** reference when you need install/usage syntax or want to confirm whether this repo covers Claude Code component linting, and the scrape quality is **good**—the essential README content is present, though deeper documentation, examples, and any code snippets or screenshots from linked docs are not included here.
