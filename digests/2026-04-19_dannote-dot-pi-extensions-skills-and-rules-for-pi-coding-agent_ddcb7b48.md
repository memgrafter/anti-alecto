---
url: https://github.com/dannote/dot-pi/
title: 'dannote/dot-pi: Extensions, skills, and rules for Pi coding agent'
scraped_at: '2026-04-19T08:14:52Z'
word_count: 609
raw_file: raw/2026-04-19_dannote-dot-pi-extensions-skills-and-rules-for-pi-coding-agent_ddcb7b48.txt
tldr: dot-pi is a GitHub repository that packages extensions, skills, and reusable rules for the Pi coding agent, with install instructions, dependency notes, and a catalog of available capabilities.
key_quote: Extensions, skills, and rules for [Pi](https://github.com/badlogic/pi-mono) coding agent.
durability: medium
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- ast-grep
- gh
- glab
- grep.app
- pi
libraries: []
companies:
- ElevenLabs
- Exa AI
- GitHub
tags:
- coding-agent
- extensions
- developer-tools
- configuration
- automation
---

### TL;DR
`dot-pi` is a GitHub repository that packages extensions, skills, and reusable rules for the Pi coding agent, with install instructions, dependency notes, and a catalog of available capabilities.

### Key Quote
"Extensions, skills, and rules for [Pi](https://github.com/badlogic/pi-mono) coding agent."

### Summary
- This is a reference/configuration repository for **Pi**, a coding agent.
- It advertises several **demos** via asciinema recordings, covering:
  - Code Search
  - LSP
  - Question
  - Web Fetch
  - Web Search
  - Voice Input
- **Installation**:
  - `pi install git:github.com/dannote/dot-pi`
  - Optional packages:
    - `pi install npm:pi-subagents` for subagent delegation
    - `pi install npm:pi-context` for context window management
  - `pi config` is used to enable/disable extensions and skills.
- **External dependencies / API keys** required by some extensions:
  - `ast-grep` for `ast-grep.ts` (`brew install ast-grep`)
  - `EXA_API_KEY` for `websearch/`
  - `ELEVENLABS_API_KEY` for `voice-input/`
- **Extensions included**:
  - `ast-grep.ts` — AST-based code search and rewrite
  - `background.ts` — run long-running processes in background
  - `bash-completion/` — intelligent shell completions
  - `codesearch.ts` — search public GitHub code via grep.app
  - `context7/` — search library documentation via Context7
  - `confirm-destructive.ts` — confirm destructive actions
  - `critic/` — shadow reviewer for agent output
  - `env-json/` — load env vars from `~/.pi/agent/env.jsonc`
  - `lsp/` — language server features like definition, references, hover, rename
  - `notify.ts` — desktop notifications on completion
  - `permission-gate.ts` — block dangerous bash commands
  - `question.ts` — ask user questions with selectable options
  - `rules.ts` — load rule files from `~/.pi/agent/rules/`
  - `voice-input/` — voice recording/STT via ElevenLabs, triggered with `Ctrl+R`
  - `webfetch/` — fetch URL content and convert it to markdown/text/html
  - `websearch/` — web search via Exa AI
  - `worktrees/` — manage git worktrees for parallel work
- **Experimental extensions** are listed separately and are not installed by default:
  - `decision-guidance.ts`
  - `plan-mode/`
  - `provider/`
  - `sandbox/` (marked WIP)
  - `subagent/` (noted as superseded by `pi-subagents`)
- Example config for enabling experimental extensions:
  - source: `git:github.com/dannote/dot-pi`
  - extensions: `["+extensions/plan-mode"]`
- **Skills included**:
  - `agent-browser` — browser automation
  - `ai-news` — curated AI news digest
  - `applescript` — macOS automation
  - `bird` — X/Twitter CLI
  - `chat-to-skill` — convert a chat session into a reusable skill
  - `github-issues` — manage GitHub Issues via `gh`
  - `keyboard-layout-decoder` — decode text typed with the wrong keyboard layout
  - `skill-discovery` — discover agent skills on GitHub
- **Rules** are not packaged; they must be symlinked into `~/.pi/agent/rules/`.
  - Example: symlink `rules/typescript.md` into that directory
  - Rules listed include:
    - `bun.md` — prefer Bun over Node.js/npm
    - `comments.md` — avoid redundant comments
    - `commit-messages.md` — follow repo commit style
    - `delete-files.md` — use `rm -f`
    - `git-hosting.md` — prefer `gh`/`glab` over fetching URLs
    - `pull-requests.md` — follow PR workflow and templates
    - `ripgrep.md` — prefer `rg`
    - `skills-cli.md` — run skill commands from skill directory
    - `typescript.md` — TypeScript conventions
- License is **MIT**.

### Assessment
This is a **reference**-type repository with fairly high practical density: it documents a Pi agent extension ecosystem, install commands, environment variables, and a feature inventory in a compact format. Durability is **medium** because the general ideas (agent extensions, skills, rules) are lasting, but specifics like package names, APIs, and experimental components may change with Pi’s evolution. Originality is mostly **primary source** as a maintainer-authored catalog rather than commentary or synthesis. It’s best used as **refer-back** material when setting up or browsing Pi capabilities, not as deep theory. Scrape quality is **good**: the main README content, tables, and code blocks appear captured, though linked demo media itself isn’t embedded and any deeper repository files are not included here.
