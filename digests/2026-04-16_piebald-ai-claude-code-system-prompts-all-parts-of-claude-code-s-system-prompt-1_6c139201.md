---
url: https://github.com/Piebald-AI/claude-code-system-prompts/tree/main
title: 'Piebald-AI/claude-code-system-prompts: All parts of Claude Code''s system prompt, 18 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation). Updated for each Claude Code version.'
scraped_at: '2026-04-16T03:53:11Z'
word_count: 6798
raw_file: raw/2026-04-16_piebald-ai-claude-code-system-prompts-all-parts-of-claude-code-s-system-prompt-1_6c139201.txt
tldr: Piebald-AI/claude-code-system-prompts is a GitHub index of extracted Claude Code internals—system prompt fragments, system reminders, builtin tool descriptions, skills, and a large Data/reference section—kept current with Claude Code releases.
key_quote: “This repository contains an up-to-date list of all Claude Code's various system prompts and their associated token counts” as of Claude Code v2.1.110 (April 15th, 2026).
durability: high
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Piebald-AI
- Anthropic
tools:
- AskUserQuestion
- Bash
- Edit
- Grep
- ReadFile
- TodoWrite
- WebFetch
- Write
- REPL
- TaskCreate
- PushNotification
- Skill
- Computer
- EnterPlanMode
- ExitPlanMode
- CronCreate
- Config
- LSP
- NotebookEdit
- PowerShell
- SendMessageTool
- WebSearch
companies:
- Piebald
- Anthropic
tags:
- claude-code
- system-prompts
- prompt-engineering
- reference-index
- ai-tools
---

### TL;DR
`Piebald-AI/claude-code-system-prompts` is a GitHub index of extracted Claude Code internals—system prompt fragments, system reminders, builtin tool descriptions, skills, and a large Data/reference section—kept current with Claude Code releases.

### Key Quote
“**This repository contains an up-to-date list of all Claude Code's various system prompts and their associated token counts** as of Claude Code v2.1.110 (April 15th, 2026).”

### Summary
- This is the **main README/index page** for the repository `Piebald-AI/claude-code-system-prompts`.
- The repo claims to track **Claude Code v2.1.110** and says it is updated **within minutes of each Claude Code release**.
- It includes a **CHANGELOG.md** covering **153 versions since v2.0.14**.
- The page is primarily a **directory of links**, not the prompt contents themselves.

- The repo explains that Claude Code uses **many system prompt strings**, not one:
  - environment/config-dependent prompt pieces
  - builtin tool descriptions
  - sub-agent prompts
  - utility prompts for features like compaction, `CLAUDE.md` generation, session titles, etc.
- It says there are **110+ strings** in a large minified JS file.
- It recommends **tweakcc** if you want to modify Claude Code’s prompts locally:
  - customize prompt pieces as markdown files
  - patch npm/native Claude Code installs
  - manage diffs/conflicts when Anthropic changes the same prompt

- The README organizes the extracted content into several major sections:
  - **Agent Prompts**
    - sub-agents like **Explore** and **Plan mode (enhanced)**
    - creation assistants like **Agent creation architect**, **CLAUDE.md creation**, and **Status line setup**
    - slash-command prompts like **/batch**, **/rename**, **/review-pr**, **/schedule**, and **/security-review**
    - utility prompts like **Bash command prefix detection**, **conversation summarization**, **memory consolidation/pruning**, **verification specialist**, **WebFetch summarizer**, and more
  - **Data**
    - language SDK/API reference files for **C#**, **Go**, **Java**, **PHP**, **Python**, **Ruby**, **TypeScript**, and **cURL**
    - other reference data such as the **Claude model catalog**, **HTTP error codes**, **Files API references**, **Managed Agents docs**, **prompt caching guidance**, **streaming references**, and **tool use concepts/reference**
  - **System Prompt**
    - parts of the main system prompt such as:
      - **Communication style**
      - **Learning mode**
      - **Doing tasks** rules like “no unnecessary additions,” “read before modifying,” “security,” “minimize file creation,” etc.
      - planning/remote planning reminders
      - memory instructions
      - tool usage rules
      - team coordination, hooks, compaction, and other behavior controls
  - **System Reminders**
    - short runtime reminders like:
      - file opened/modified/truncated
      - plan mode reminders
      - hook notifications
      - token usage / budget
      - team coordination/shutdown
      - memory and diagnostics reminders
  - **Builtin Tool Descriptions**
    - descriptions for Claude Code tools such as:
      - `AskUserQuestion`
      - `Bash`
      - `Edit`
      - `Grep`
      - `ReadFile`
      - `TodoWrite`
      - `WebFetch`
      - `Write`
      - `REPL`
      - `TaskCreate`
      - `PushNotification`
      - `Skill`
      - `Computer`
      - `EnterPlanMode` / `ExitPlanMode`
    - plus many **Bash sub-instructions** about sandboxing, file search, read/write preferences, git safety, sleep usage, working directory behavior, etc.
  - **Skills**
    - built-in skill prompts for:
      - `/dream nightly schedule`
      - `/init CLAUDE.md and skill setup`
      - `/loop`
      - `/stuck`
      - **Agent Design Patterns**
      - **Building LLM-powered applications with Claude**
      - **Computer Use MCP**
      - **Verify** workflows
      - config/update and onboarding workflows

- The page also notes that some prompts contain **interpolated context** like tool names or sub-agent lists, so token counts can vary slightly in actual sessions.

### Assessment
This has **high durability** as a reference index because it documents a fast-changing product across versions, though the specifics will stale as Claude Code releases evolve. The content type is **mixed**, but mostly **reference** with some explanatory commentary. Density is **high** because the README packs a large structured catalog of prompt files, token counts, versioning claims, and workflow notes into a single page. Originality is mostly **primary source / extraction-based** rather than synthesis: the repo presents extracted Claude Code prompt text and metadata directly from compiled source, while the README itself adds framing and maintenance notes. For **recall**, this is very useful as a map of Claude Code internals; for **decide**, it’s worth revisiting if you need a directory of prompt fragments rather than the fragments themselves; for **evaluate**, it is trustworthy as an extraction/index of a moving target, but its exact details are version-bound and should be checked against the current Claude Code release; for **find**, it is an excellent identifier if you’re looking for the repository that catalogs Claude Code system prompts, tool descriptions, Data references, reminders, and skills. **Scrape quality is good** for the README/index page itself, but it does not include the linked prompt files’ contents, so the actual referenced documents are missing.
