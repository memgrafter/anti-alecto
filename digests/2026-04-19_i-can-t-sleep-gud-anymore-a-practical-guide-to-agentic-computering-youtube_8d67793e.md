---
url: https://www.youtube.com/watch?v=sq6a3WC5_Ns
title: I can't sleep gud anymore - A Practical Guide to Agentic Computering - YouTube
scraped_at: '2026-04-19T08:18:04Z'
word_count: 13468
raw_file: raw/2026-04-19_i-can-t-sleep-gud-anymore-a-practical-guide-to-agentic-computering-youtube_8d67793e.txt
tldr: A long practical talk arguing that Claude Code is best used as a controlled, prompt-driven workflow engine for ad hoc scripting, documentation generation, and large-codebase porting, not as an autonomous “vibe coding” replacement for human understanding.
key_quote: “Cloud code is a programming language. Your prompt is your program and your files on disk are your state that you can query and update.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Peter
- Armen
- Nat Friedman
tools:
- Claude Code
- claude
- ffmpeg
- Docker
- grep
- ripgrep
- bash
- git
- jq
- LSP CLI
- VS Clot
- clot trace
- Playwright
- Puppeteer
companies:
- Anthropic
- GitHub
- Microsoft
- OpenAI
- Cursor
- Windsurf
tags:
- agentic-coding
- claude-code
- context-management
- workflow-automation
- code-porting
---

### TL;DR
A long practical talk arguing that Claude Code is best used as a controlled, prompt-driven workflow engine for ad hoc scripting, documentation generation, and large-codebase porting, not as an autonomous “vibe coding” replacement for human understanding.

### Key Quote
“Cloud code is a programming language. Your prompt is your program and your files on disk are your state that you can query and update.”

### Summary
- The speaker says Claude Code is useful because it enables fast iteration on ideas, but it often produces bad code, so humans should keep control and refine the output.
- The core thesis is that agentic coding is still not a mature engineering discipline because LLM behavior is nondeterministic; small prompt changes can change outcomes dramatically.
- The talk focuses on practical usage of Claude Code for:
  - new projects,
  - existing codebases,
  - documentation generation,
  - ad hoc scripting,
  - and large-scale code porting.

- Recommended usage patterns:
  - Use `--dangerously-skip-permissions` to avoid constant permission prompts and keep the agent loop flowing.
  - Run Claude in a container/Docker if you want extra safety.
  - Use `CLAUDE.md` files to inject project instructions into the system prompt.
  - Treat Claude-generated docs and code as first drafts, not gospel.

- For greenfield or small project tasks:
  - Claude can create blog posts, metadata JSON, server startup commands, and helper scripts.
  - It is especially good at writing one-off bash or Node scripts, such as batch-converting files with `ffmpeg`.
  - The speaker emphasizes that Claude shines when asked to generate reusable automation, not when asked to hand-hold every manual step.

- On documentation and project structure:
  - A global `CLAUDE.md` can define general rules like “don’t add comments” or “never add yourself as committer.”
  - Project-specific `CLAUDE.md` files should describe the repo structure, common tasks, and special rules.
  - For larger projects, the speaker recommends splitting docs into:
    - `spec.md` for architectural overview,
    - per-module Markdown files for details,
    - and updating them after each module change using git diffs.
  - This documentation is meant to reduce context waste and improve reproducibility across sessions.

- The speaker shows how Claude can be used to:
  - create new blog posts,
  - run the dev server,
  - update metadata,
  - and open the result in the browser.
  - Claude sometimes hallucinates or makes wrong assumptions, so outputs must be checked and corrected.

- A major theme is context management:
  - Claude Code is powerful when you deliberately control what information it sees.
  - The speaker dislikes IDEs and agents that inject extra context automatically.
  - He argues that uncontrolled context poisons the session and makes behavior less reproducible.
  - He also says the UI hides part of the context, so understanding actual tool usage matters.

- He introduces `clot trace` as a custom tracing tool:
  - It hooks fetch calls and logs Claude Code requests/responses.
  - This reveals hidden system prompts, tool definitions, quota checks, and IDE-injected context.
  - He uses it to show that Claude Code often sends summaries or safety checks through internal Haiku calls before using Opus.

- Tool behavior observations from tracing:
  - `read` tool prefixes lines in a way that may interfere with later `edit` operations.
  - `web fetch` and `web search` do not inject raw data directly; they use LLM summarization for safety.
  - Some tools are useful, but many are still too opaque or context-heavy for his taste.

- He discusses session compaction:
  - Compaction can destroy carefully built conversational state.
  - If a session is compacted at the wrong time, nuanced proposals and decisions can be lost.
  - His workaround is to manually write a `task-summary.md` or similar file before compaction, then start a new session and reload that state.
  - He warns that Claude summaries are first drafts and often omit crucial details.

- In the established-codebase section, he describes a serious workflow for porting Spine runtime changes across languages:
  - Spine is a 2D skeleton animation editor/runtime system with many language ports.
  - He built `LSP CLI` to index a codebase into JSON symbol maps using a local language server.
  - He built `VS Clot`, an MCP-based extension that lets Claude open files/diffs in VS Code.
  - He uses a `port.md` workflow file, a generated porting plan, and per-target-runtime conventions docs.
  - Claude then iterates through types, reads only the relevant source files, updates ports, compiles to verify, and marks items done.

- The porting workflow is presented as a software program:
  - Prompts are the “machine code.”
  - Markdown/JSON files are the persistent state.
  - Claude is the execution substrate.
  - Checkpoints and human review are required for correctness.

- Final stance:
  - MCP servers are mostly useless in his experience because they dump too much irrelevant context.
  - The exception is tooling that gives Claude controlled access to browser state or file editing.
  - Tests generated by Claude are also only first drafts and need manual review because they often become too weak or too mocked-out to be meaningful.
  - The speaker’s main advice is to understand your code, keep control of context, and use Claude to accelerate work rather than replace engineering judgment.

### Assessment
This is a mixed opinion/tutorial talk with a strong personal workflow focus. Durability is medium: the underlying ideas about context management, human-in-the-loop automation, and documentation-driven agent workflows are fairly timeless, but many specifics are tied to current Claude Code behavior, tool names, and quirks that may age quickly. Density is high, with lots of concrete examples, commands, custom tools, and workflow details packed into the transcript. It is primary-source commentary rather than synthesis, since it reflects the speaker’s own experience and opinions. Best used as refer-back material if you’re adopting Claude Code workflows or evaluating agentic coding practices. Scrape quality is partial: the transcript is captured in full enough to summarize, but the source is clearly auto-captioned and noisy, with missing punctuation, repeated fragments, and likely no access to slides, code visuals, or on-screen details.
