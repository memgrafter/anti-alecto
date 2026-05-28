---
url: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
title: What I learned building an opinionated and minimal coding agent
scraped_at: '2026-04-12T07:26:24Z'
word_count: 6678
raw_file: raw/2026-04-12_what-i-learned-building-an-opinionated-and-minimal-coding-agent_cf72e65c.txt
tldr: Mario Zechner describes building a minimal, opinionated coding-agent stack—`pi-ai`, `pi-agent-core`, `pi-tui`, and `pi-coding-agent`—to maximize context control, observability, and simplicity, while rejecting many popular agent features like MCP, background bash, plan mode, and sub-agents.
key_quote: “Context engineering is paramount.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Mario Zechner
- Simon Willison
- Armin
- Peter Steinberger
tools:
- pi-ai
- pi-agent-core
- pi-tui
- pi-coding-agent
- TypeBox
- AJV
- tmux
- Terminal-Bench
- MCP
- Claude
libraries:
- Vercel AI SDK
- Ink
- Blessed
- OpenTUI
- models.dev
companies:
- Anthropic
- OpenAI
- Google
- xAI
- Groq
- Cerebras
- OpenRouter
- Vercel
- Cursor
- Windsurf
- Claude Code
tags:
- coding-agents
- llm-infrastructure
- terminal-ui
- context-engineering
- developer-tools
---

### TL;DR
Mario Zechner describes building a minimal, opinionated coding-agent stack—`pi-ai`, `pi-agent-core`, `pi-tui`, and `pi-coding-agent`—to maximize context control, observability, and simplicity, while rejecting many popular agent features like MCP, background bash, plan mode, and sub-agents.

### Key Quote
“Context engineering is paramount.”

### Summary
- The post is a 2025-11-30 retrospective on building a custom coding agent because existing harnesses felt too bloated, opaque, and unstable for the author’s workflow.
- The project is split into four packages:
  - `pi-ai`: unified multi-provider LLM API
  - `pi-agent-core`: agent loop with tool execution and event streaming
  - `pi-tui`: minimal terminal UI framework
  - `pi-coding-agent`: CLI that ties everything together
- Core philosophy: **if it’s not needed, it won’t be built**.
- Main motivation for rebuilding:
  - existing tools hide or inject context behind the user’s back
  - system prompts and tool behavior change too often
  - self-hosted model support is often poor
  - the author wants full inspection, post-processing, and alternate UIs

#### `pi-ai`: unified LLM abstraction
- Supports many providers, including:
  - Anthropic, OpenAI, Google, xAI, Groq, Cerebras, OpenRouter, and any OpenAI-compatible endpoint
- Covers:
  - streaming
  - tool calling with TypeBox schemas
  - reasoning/thinking support
  - cross-provider context handoff
  - token and cost tracking
- The author argues there are effectively four key API shapes to normalize:
  - OpenAI Completions
  - OpenAI Responses
  - Anthropic Messages
  - Google Generative AI
- Mentions provider quirks:
  - some dislike `store`
  - some use `max_tokens` instead of `max_completion_tokens`
  - some don’t support `developer` role prompts
  - reasoning content appears in different fields
- `pi-ai` includes an extensive test suite across providers, models, images, reasoning, and tools.
- Token/cost tracking is only best-effort because providers report usage inconsistently and often don’t support stable request correlation IDs.
- It works in the browser too; Anthropic and xAI are noted as CORS-friendly.
- Cross-provider context handoff is a design goal:
  - Anthropic thinking traces can be serialized into `<thinking>...</thinking>` text when switching to another provider
  - signed blobs in event streams must be preserved across requests
- Supports type-safe model registry generated from OpenRouter and models.dev data.
- Supports custom/self-hosted models by defining a `Model<'openai-completions'>` object.
- Abort support is treated as essential, including during tool calls.
- Tools can return:
  - content for the LLM
  - separate UI-facing details
  - attachments like images
- Tool arguments are validated with TypeBox + AJV.
- Partial JSON parsing during tool-call streaming enables better UI feedback.
- A limitation: tool result streaming is not yet implemented.

#### `pi-agent-core`
- Provides the orchestration loop:
  - process user input
  - execute tools
  - feed tool results back to the model
  - continue until no more tool calls
- Emits events for reactive UIs.
- The author dislikes arbitrary “max steps” knobs and prefers an agent that just loops until done.
- An `Agent` class adds:
  - state management
  - event subscriptions
  - message queuing
  - attachment handling
  - transport abstraction

#### `pi-tui`: minimal terminal UI
- Built for a terminal-first coding agent experience.
- The author compares two TUI styles:
  - full-screen TUIs that take over the viewport
  - linear scrollback-based TUIs that behave more like normal CLI programs
- `pi-tui` uses the second style because:
  - scrollback and search stay available
  - the interaction is naturally chat-like
  - the constraints encourage minimalism
- It uses a retained-mode component model:
  - `Component.render(width)`
  - optional `handleInput(data)`
  - `Container` arranges components vertically
  - `TUI` compares current output to previous output
- Rendering strategy:
  - first render: print everything
  - width change: full clear and rerender
  - normal update: redraw only changed lines from the first differing line onward
- Uses synchronized terminal output escape sequences:
  - `CSI ?2026h`
  - `CSI ?2026l`
- Works best in terminals like Ghostty and iTerm2; VS Code terminal may flicker somewhat.
- The author accepts some flicker as a tradeoff for simplicity.
- Memory/performance overhead is considered acceptable for modern machines.

#### `pi-coding-agent`: the CLI
- Features listed include:
  - Windows/Linux/macOS support
  - multi-provider and mid-session model switching
  - session continue/resume/branching
  - hierarchical `AGENTS.md` project context
  - slash commands
  - custom markdown slash commands
  - Claude Pro/Max OAuth
  - JSON config
  - live-reloading themes
  - file editor with fuzzy search, completion, drag-and-drop, multiline paste
  - message queuing
  - image support
  - HTML export
  - headless JSON streaming and RPC mode
  - token/cost tracking
- The system prompt is intentionally tiny: under 1000 tokens together with tool definitions.
- Only four core tools are built in:
  - `read`
  - `write`
  - `edit`
  - `bash`
- Additional read-only tools can be enabled, but are disabled by default.

#### Strongly opinionated design choices
- **YOLO by default**
  - full filesystem and command execution access
  - no permission prompts
  - no built-in safety rails
- The author argues guardrails are mostly security theater if the agent can already read, write, and execute code.
- Recommends containerization if users want isolation.
- **No built-in to-dos**
  - use a file like `TODO.md` with checkboxes instead
- **No built-in plan mode**
  - use a file like `PLAN.md`
  - the author values observability and editable artifacts over hidden planning
- **No MCP support**
  - argues MCP tool descriptions are too token-heavy
  - prefers CLI tools with README files and progressive disclosure
  - mentions a personal `agent-tools` repository and mcporter as a wrapper if MCP is unavoidable
- **No background bash**
  - prefers synchronous commands
  - recommends `tmux` for long-running processes, dev servers, and debugging
- **No sub-agents**
  - considers them opaque and hard to debug
  - prefers using a fresh session or spawning the agent via `bash` when needed
  - says sub-agents are sometimes useful for code review, but not for parallel feature work

#### Benchmarks and evaluation
- The author ran Terminal-Bench 2.0 with `pi` and Claude Opus 4.5 against other coding harnesses such as Codex, Cursor, and Windsurf.
- Five trials per task were used so results could be submitted to the leaderboard.
- A CET-only benchmark run was started because benchmark quality allegedly changes later in the day.
- The author cites the presence of a minimal competitor, Terminus 2, as evidence that a simple design can perform well.
- The benchmark section is presented as supporting evidence, but the author explicitly notes benchmarks are not representative of real work.

#### Conclusion
- The author is broadly happy with `pi` and says it performs well in daily use.
- Missing compaction has not been a major problem for them.
- Future features mentioned:
  - compaction
  - tool result streaming
- The project is intentionally narrow and maintainable, and contributors are welcome, though the author says they tend to be strict about scope.
- The broader takeaway: current coding-agent tools often make context engineering harder than it should be, and `pi` is the author’s attempt to put control back in the user’s hands.

### Assessment
This is a mixed technical/opinion post with a high-density, highly specific description of a custom coding-agent stack and its design philosophy. Durability is medium: the architectural ideas around context control, observability, tool minimalism, and terminal UI design are fairly timeless, but many provider/model references, benchmark results, and feature/status claims are tied to late-2025 tooling and will age quickly. The content is a blend of original implementation notes, commentary, and product philosophy rather than a neutral reference. It’s best treated as deep-study material if you’re building agents or evaluating harness design, and skim-once if you just want the author’s stance. Scrape quality appears good: the article text is largely intact, including code snippets and section structure, though the embedded benchmark images/plots are referenced but not visible in the plain text.
