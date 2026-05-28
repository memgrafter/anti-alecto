---
url: https://www.youtube.com/watch?v=mZzhfPle9QU
title: How I use Claude Code (Meta Staff Engineer Tips) - YouTube
scraped_at: '2026-04-19T07:15:24Z'
word_count: 8444
raw_file: raw/2026-04-19_how-i-use-claude-code-meta-staff-engineer-tips-youtube_81ff504f.txt
tldr: A Meta staff engineer shares 50 practical Claude Code tips, centered on keeping context small and fresh, using plan mode and validation loops, and building reusable workflows with rules, skills, MCPs, sub-agents, hooks, and Chrome/browser automation.
key_quote: context is king. You got to keep it fresh, keep it relevant.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Meta staff engineer
- Anthropic
tools:
- Claude Code
- Xcode
- Puppeteer
- Figma
- iTerm
- Whisper
- Chrome
- Git
libraries: []
companies:
- Meta
- Anthropic
tags:
- ai-coding
- context-engineering
- terminal-workflows
- browser-automation
- developer-productivity
---

### TL;DR
A Meta staff engineer shares 50 practical Claude Code tips, centered on keeping context small and fresh, using plan mode and validation loops, and building reusable workflows with rules, skills, MCPs, sub-agents, hooks, and Chrome/browser automation.

### Key Quote
“context is king. You got to keep it fresh, keep it relevant.”

### Summary
- The video is a hands-on walkthrough of how the speaker uses Claude Code every day for about 6 months, mostly as a terminal-based pair-programming and code-review tool.
- Core thesis: Claude Code works best when you treat it as a context-management system, not just a code generator. The quality of your rules, validation, and workflow design matters more than raw prompting.

- **Getting started / foundations**
  - Run Claude Code from the **root directory** of the project so it can ingest the right project context.
  - Use `/init` to analyze the codebase and generate an initial `claude.md` file.
  - `claude.md` follows a hierarchy: there can be project-local memory and global/user memory (in `~/.claude/...`).
  - Keep `claude.md` relatively small; the speaker suggests roughly **300 lines** as a reasonable target.
  - Put in:
    - high-level architecture
    - requirements
    - domain context
    - file paths
    - design patterns
    - build/validation steps
  - He emphasizes that a strong `claude.md` can take a user far even without advanced features.

- **Validation loops are critical**
  - One of the most important practices is defining a reliable **build/validation loop**.
  - Examples mentioned:
    - build the Xcode project for iOS apps
    - run app/emulator and inspect logs
    - use Puppeteer / `/chrome` for web flows
    - use traces/performance tools like `peretto` MCPs
  - Claude performs much better when it can iterate against a clear validation signal.
  - The speaker frames this as a major part of “agentic coding” and says it dramatically improves first-pass quality.

- **Keyboard shortcuts and session control**
  - **Shift+Tab** toggles between modes, especially useful for switching from edit/accept mode into **plan mode**.
  - He strongly prefers starting new work in **plan mode** before execution.
  - **Escape** interrupts the model; he recommends interrupting early if it’s going off track.
  - **Double Escape** clears input or can rewind/restoring previous context depending on state.
  - Screenshot workflows are useful for UI work: take a screenshot, drag it into Claude, and add explicit instructions.
  - He recommends using a **Figma MCP** or similar for UI validation when relevant.

- **Essential slash commands**
  - `/clear` clears context, useful when starting a new task and not wanting old context to bleed into the next one.
  - `/context` shows a visual view of current context usage and helps identify token-heavy offenders, especially MCPs.
  - `/compact` compresses a long session into a summary; he mostly lets auto-compaction happen.
  - `/models` lets you choose the model; he says he usually defaults to **Opus 4.5** if cost allows.
  - `/resume` restores a prior session if you close or lose the instance.
  - `/mcp` lists installed MCPs; he warns they often inflate context/token usage.
  - `/help` shows available commands and descriptions.

- **Git as safety net**
  - He recommends using **git** heavily as a backup and checkpointing mechanism.
  - Claude can help manage git tasks, summaries, and test plans.
  - He says git is better than relying on rewind features alone.

- **How to write better `claude.md` rules**
  - Important rules:
    - Put the most important instructions first; he believes Claude reads top to bottom with priority order.
    - Include “always do / never do” style constraints.
    - Add clear examples for project-specific patterns.
  - If Claude repeatedly makes a mistake, fix it manually once, then update the rules so it doesn’t recur.
  - He suggests using Claude itself to update rules rather than editing them manually.
  - He also mentions using keyword triggers in rules to invoke specific behaviors, like “use my Xcode MCP to build the app.”

- **Skills, commands, and composability**
  - He describes **skills** as reusable workflows saved as markdown/system-prompt-like instructions.
  - Example workflow: fetch Hacker News items, summarize them, and save the summary locally.
  - He notes that Anthropic has recently blurred the line between **skills** and **slash commands**, and both are now more interchangeable.
  - You can ask Claude to extend a skill over time, e.g. fetching from multiple sources.
  - He treats these as composable primitives that can be combined into broader automation.

- **MCPs**
  - MCPs are powerful but risky from a context/token perspective.
  - He avoids installing many MCPs and prefers only the ones needed for a specific project.
  - He suggests asking Claude to find and even install an MCP when needed, though he warns search results may be outdated.
  - Example use cases:
    - Xcode MCP for iOS build flows
    - Figma MCP for design validation
    - web/debug tooling

- **Sub-agents**
  - Sub-agents are useful mainly for **parallel work** and **context protection**.
  - But he cautions that sub-agents only return outputs, not the full reasoning or context used to reach them.
  - He prefers keeping context-heavy tasks in the main session when the model needs to understand the code it just wrote.
  - He does not love the common pattern of splitting work into many role-based agents like “CEO agent” or “design agent.”
  - His principle: **bring the work to the context, not the context to the work**.

- **Parallel workflows / working style**
  - He has changed his workflow to favor **multiple Claude instances** in parallel.
  - Uses terminal tools like **iTerm** and switches between tabs/windows/instances quickly.
  - Mentions naming tabs like “local” and “remote SSH.”
  - Uses voice input (Whisper) at home.
  - He sees this as a way to juggle multiple projects and increase throughput.
  - Notifications can be customized, including audible cues or TTS-style summaries.

- **Git worktrees**
  - Worktrees are recommended for true parallel code execution within the same project when multiple branches need active development.

- **Chrome / browser automation**
  - `/chrome` opens browser control and lets Claude navigate websites interactively.
  - Demonstrated with YouTube search: Claude can type into the browser and navigate results.
  - He recommends it for cases where there’s no API access but browser access is available.
  - It’s also useful for debugging, validation, scraping, and form-filling.

- **Hooks and automation**
  - Hooks are “before/after” automation steps, similar in spirit to git hooks.
  - Useful for:
    - formatting
    - linting
    - blocking destructive operations
    - preventing dangerous mutations like accidental database removal
  - He recommends asking Claude to set them up.

- **Overall philosophy**
  - Claude Code is framed as a tool for **context engineering** and **agent orchestration**, not just prompt answering.
  - The speaker repeatedly stresses:
    - keep context fresh
    - don’t bloat sessions
    - use plan mode
    - build validation loops
    - prefer reusable workflows and automation
    - rely on git as backup
  - He ends by encouraging viewers to explore the plugin ecosystem and combine skills, MCPs, sub-agents, and scripts into larger workflows.

### Assessment
This is a **mixed tutorial/reference** video with high practical density: it’s packed with specific commands, workflows, and opinionated best practices about Claude Code usage. Durability is **medium** because many recommendations are tied to current Claude Code features, model names (like Opus 4.5), and evolving command/skill/MCP behavior, though the underlying advice about context management and validation is more durable. The content is primarily **commentary/tutorial**, not a neutral docs source; it reflects one engineer’s workflow and preferences, especially his strong bias toward minimal MCP usage, plan mode, and parallel terminal-based work. It’s best used as a **refer-back** resource if you’re building your own Claude Code workflow. Scrape quality is **partial**: the transcript is messy and likely auto-generated, with repeated phrases, transcription errors, and some unclear command names, but it still captures the major structure and most of the substantive tips.
