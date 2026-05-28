---
url: https://news.ycombinator.com/item?id=44483530
title: Backlog.md – Markdown‑native Task Manager and Kanban visualizer for any Git repo | Hacker News
scraped_at: '2026-04-19T21:46:55Z'
word_count: 1619
raw_file: raw/2026-04-19_backlog-md-markdown-native-task-manager-and-kanban-visualizer-for-any-git-repo-h_771412bf.txt
tldr: Hacker News thread about Backlog.md, a markdown-native task manager/Kanban visualizer for Git repos, where top commenter argues the real win is process and task structuring—not bigger models—and that Backlog.md works best when paired with clear repo instructions and agent workflows.
key_quote: Backlog.md is still a bit rough on the edges but is definitely a proof that markdown files and AI Agents work really well together.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Claude
- Codex
- aider
- Gemini
- MetaGPT
tools:
- Backlog.md
- Claude Code
- MCP
- Jira
- Taskmaster-ai
libraries: []
companies: []
tags:
- ai-agents
- task-management
- markdown
- git
- developer-tools
---

### TL;DR
Hacker News thread about **Backlog.md**, a markdown-native task manager/Kanban visualizer for Git repos, where **top commenter argues the real win is process and task structuring—not bigger models—and that Backlog.md works best when paired with clear repo instructions and agent workflows**.

### Key Quote
"Backlog.md is still a bit rough on the edges but is definitely a proof that markdown files and AI Agents work really well together."

### Summary
- **Top comment (verbatim):** "Backlog.md is still a bit rough on the edges but is definitely a proof that markdown files and AI Agents work really well together."
- **Top commenter:** `u/<not provided>`
- **Thread topics:**
  - Using **Backlog.md** to break PRDs/features into small markdown task files for Claude/Codex/aider
  - Whether AI agents can reliably manage tasks, dependencies, and sub-tasks as projects grow
  - How to integrate with **Claude Code**, **aider**, and possibly **MCP** workflows
  - Repo/layout questions: multiple branches, multiple repos (BE/FE), Jira integration, and non-git usage
  - Practical limitations: context windows, file size, rough edges, and git command noise

- The original post claims the author tried dropping **Claude Code** into an existing codebase and found it slower than starting from scratch; the fix was **process**, not model strength.
- They describe an iteration ladder:
  - **50% task success**: add `README.md` and `CLAUDE.md` so the model understands the project
  - **75%**: use **one markdown file per task**; **Codex plans, Claude codes**
  - **95%+**: build **Backlog.md**, a CLI that automatically turns a high-level spec into those task files
- The suggested workflow is a **three-step loop**:
  1. **Generate tasks** with Codex / Claude Opus and self-review
  2. **Generate a plan** in “plan” mode and tweak if needed
  3. **Implement** with the coding agent using the backlog-generated task files
- The tool stores data as human-readable Markdown under a `backlog/` folder, with files like:
  - `task-<task-id> - <task-title>.md`
- The thread repeatedly returns to one core idea: **LLMs do better when the work is decomposed into small, explicit, markdown-structured tasks**.
- Several commenters say they’ve had similar results with other tools:
  - **Taskmaster-ai** worked until projects grew larger
  - **aider** can be paired with `--watch-files` and special markers like `// #AI` and `// !AI`
  - Some people built their own tiny dependency-tracking task systems in Markdown or with SQLite/MCP
- A practical detail from the author: when initializing Backlog.md in a folder, it asks whether to create agent instructions like **`CLAUDE.md`**, and the author says **you should say yes** so Claude understands how to use Backlog.
- Example usage given in the thread:
  - “Claude please have a look at the @prd.md file and use ultrathink to create relevant tasks…”
  - The tool can also be used without AI agents; it just produces output that is easy for LLMs to ingest.
- Common questions and concerns in the thread:
  - **Dependencies/subtasks:** several users ask for stronger dependency handling
  - **Multi-branch / multi-repo support:** questions about BE/FE split repos and branch-wide task state
  - **Jira integration:** one user asks if it can sync with Jira tickets
  - **Avoiding git commits:** someone wants to use it locally without committing backlog files and hits git-related errors
- The author answers that the system uses **git** to fetch files from other branches, so task state stays current across main and feature branches, though performance with many branches may need improvement.
- Some commenters note rough edges:
  - missing or broken references in `AGENTS.md` / `GEMINI.md`
  - AI agents confusing the folder vs. file structure
  - context-budget issues if tasks become too large
- Overall, the thread is broadly positive: readers see **Backlog.md** as a promising proof that **Markdown + AI agents + explicit task decomposition** can improve coding workflows, though the project is still early and not yet polished.

### Assessment
This is a **mixed** social-thread / product announcement discussion with high practical density: lots of concrete workflow details, example commands, and implementation concerns, but no formal benchmark data or rigorous evaluation. Durability is **medium** because the ideas around task decomposition and agent workflows are useful beyond the current tools, but the specifics are tied to fast-moving products like Claude Code, Codex, aider, and MCP. The content is mostly **commentary and synthesis** around the tool, not a primary technical spec, though the author’s comments include useful firsthand notes. It’s best as a **skim-once / refer-back** reference if you care about agentic coding workflows, backlog design, or markdown-based project management. Scrape quality is **partial**: the thread text is captured, but commenter handles, exact ordering, and any screenshots/code blocks are missing.
