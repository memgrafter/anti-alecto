---
url: https://ccunpacked.dev/#query-loop
title: Claude Code Unpacked
scraped_at: '2026-04-19T08:20:05Z'
word_count: 214
raw_file: raw/2026-04-19_claude-code-unpacked_c7ca5fc0.txt
tldr: A source-mapped explainer of Claude Code that shows its agent loop, architecture, built-in tools, and slash commands, with emphasis on how the product works internally rather than how to use it as a normal end user.
key_quote: What actually happens when you type a message into Claude Code?
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- claude-code
libraries:
- Ink
companies: []
tags:
- developer-tools
- agent-workflows
- software-architecture
- command-line
- source-code
---

### TL;DR
A source-mapped explainer of Claude Code that shows its agent loop, architecture, built-in tools, and slash commands, with emphasis on how the product works internally rather than how to use it as a normal end user.

### Key Quote
"What actually happens when you type a message into Claude Code?"

### Summary
- **Claude Code Unpacked** is an interactive, source-based walkthrough of Claude Code’s internals.
- It frames the project around four main areas:
  - **The Agent Loop**: “From keypress to rendered response, step by step through the source.”
  - **Architecture Explorer**: a clickable view into the source tree.
  - **Tool System**: built-in tools Claude Code can call, grouped by function.
  - **Command Catalog**: slash commands, grouped by workflow.
- The page claims to map:
  - **50+ tools**
  - **0+ files**
  - **0K+ lines of code**
  - **0+ commands**
  - These counters appear as placeholders or non-final values in the scrape, so they are not reliable as-is.
- The **Agent Loop** section shows a concrete path from user input to processing:
  - User input originates in `src/components/TextInput.tsx`
  - Users can type a message or pipe input through **stdin**
  - In interactive mode, input comes from **Ink's `TextInput` component**
  - In non-interactive mode, it reads from **piped stdin**
- The **Architecture Explorer** organizes the codebase into labeled areas:
  - Tools & Commands
  - Core Processing
  - UI Layer
  - Infrastructure
  - Support & Utilities
  - Personality & UX
- The **Tool System** groups built-in tools by purpose and indicates counts per category:
  - File Operations — **6 tools**
  - Execution — **3 tools**
  - Search & Fetch — **4 tools**
  - Agents & Tasks — **11 tools**
  - Planning — **5 tools**
  - MCP — **4 tools**
  - System — **11 tools**
  - Experimental — **8 tools**
- The **Command Catalog** groups slash commands by workflow area:
  - Setup & Config — **12**
  - Daily Workflow — **24**
  - Code Review & Git — **13**
  - Debugging & Diagnostics — **23**
  - Advanced & Experimental — **23**
- The overall purpose is exploratory and diagnostic: it helps readers trace how Claude Code is structured and what capabilities it exposes, likely useful for developers, power users, or anyone trying to understand the product beyond surface-level docs.

### Assessment
This is a **reference**-style, source-mapped explainer with a **mixed** content type leaning technical/documentary. Its durability is **medium**: the high-level architecture concepts may age well, but the tool and command catalogs are tied to the specific Claude Code version and may change as the product evolves. The density is **medium-high** because it packs a lot of named sections, counts, and code-path hints into a short landing page. Originality is best described as **primary source** if the site is truly mapped from source code, though the scrape itself only captures a top-level overview. It is best used as a **refer-back** resource for locating specific internal features, tools, or commands. Scrape quality is **partial**: the page’s structure and headings are captured, but detailed subsection content, interactive details, source snippets, and any code blocks or expanded panels are missing.
