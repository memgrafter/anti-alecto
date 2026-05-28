---
url: https://github.com/RandomsUsernames/sgrep
title: RandomsUsernames/sgrep
scraped_at: '2026-04-12T09:43:15Z'
word_count: 885
raw_file: raw/2026-04-12_randomsusernames-sgrep_d231b032.txt
tldr: sgrep is a Rust-based semantic code search tool that lets you query a codebase in natural language, generate AI answers, and integrate with Claude/Cursor via MCP.
key_quote: Semantic grep for the AI era
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Claude
- Cursor
- Gemini CLI
- OpenCode
- Continue
tools:
- sgrep
- Claude Code
- Cursor
- Continue
- Gemini CLI
- OpenCode
- Codex CLI
libraries:
- BGE
- CodeRankEmbed
companies:
- RandomsUsernames
- OpenAI
tags:
- semantic-search
- code-search
- mcp
- rust
- ai-tools
---

### TL;DR
`sgrep` is a Rust-based semantic code search tool that lets you query a codebase in natural language, generate AI answers, and integrate with Claude/Cursor via MCP.

### Key Quote
“Semantic grep for the AI era”

### Summary
- `sgrep` is presented as “Natural language code search powered by Rust,” aimed at finding code by meaning rather than literal text.
- Core workflow:
  - `sgrep index .` to index a codebase
  - `sgrep search "..."` to run semantic search
  - `sgrep ask "..."` for AI-synthesized answers
  - `sgrep map` to inspect codebase structure
- Claimed advantages over traditional `grep`:
  - Finds code by meaning, not exact keywords
  - Understands synonyms and context
  - Works with AI tools like Claude and Cursor
- Installation options:
  - Homebrew on macOS: `brew tap RandomsUsernames/sgrep` then `brew install sgrep`
  - Cargo: `cargo install searchgrep`
  - From source via `git clone` and `cargo install --path .`
- Features highlighted:
  - Semantic search with default, `--code`, and `--hybrid` modes
  - AI answers using OpenAI/GPT via `OPENAI_API_KEY`
  - Codebase mapping for functions/classes/relationships
  - MCP server support for Claude Code, Cursor, Continue, etc.
  - “Skills” setup for Claude, Gemini CLI, and OpenCode
- Search options listed:
  - `-m, --max-results <n>` default 10
  - `-c, --content` to show snippets
  - `-a, --answer` to generate an AI answer
  - `--code` and `--hybrid` for model/mode selection
- How it works:
  - Files are chunked and embedded locally using BGE or CodeRankEmbed
  - Embeddings are cached in `~/.sgrep/`
  - Queries are embedded and ranked by cosine similarity
  - Top results can be sent to GPT for synthesis
- Performance claims:
  - Optimized for Apple Silicon using Accelerate
  - No API calls needed for search itself
  - Indexing around 100 files/minute
  - Search around 2s for single model, 3.5s for hybrid
- Configuration and environment:
  - `sgrep config --api-key sk-...` to set OpenAI key
  - `OPENAI_API_KEY` and `OPENAI_BASE_URL` supported
  - Respects `.gitignore` and `.sgrepignore`
- Troubleshooting section notes MCP stdio issues with some clients and recommends a Node.js wrapper script (`scripts/mcp-wrapper.js`) for Codex CLI and Gemini CLI.

### Assessment
This is a mixed content GitHub README / product documentation with high practical density and relatively high durability in its conceptual ideas, though specific commands, model names, performance numbers, and client compatibility notes may age as the project evolves. It is primarily a reference and tutorial document rather than an opinion piece, and it appears to be the project’s own promotional/technical source rather than a synthesis. Use it as a refer-back card when deciding whether to install or integrate `sgrep`, especially for its setup commands, MCP configuration, and troubleshooting notes. Scrape quality is good overall: the main README sections, commands, tables, and troubleshooting content are present, but any linked assets, screenshots, or repository files outside the README are not included.
