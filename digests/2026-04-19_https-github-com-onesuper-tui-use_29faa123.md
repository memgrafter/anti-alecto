---
url: https://github.com/onesuper/tui-use
title: https://github.com/onesuper/tui-use
scraped_at: '2026-04-19T20:08:05Z'
word_count: 1306
raw_file: raw/2026-04-19_https-github-com-onesuper-tui-use_29faa123.txt
tldr: tui-use is a CLI tool and PTY-based runtime that lets AI agents interact with terminal programs, REPLs, debuggers, and full-screen TUI apps as if a human were typing at the keyboard.
key_quote: Like BrowserUse, but for the terminal.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- tui-use
- tmux
- codex
- claude code
- cursor
- gemini cli
- opencode
libraries: []
companies:
- OpenAI
tags:
- terminal-automation
- ai-agents
- cli-tools
- tui
- debugging
---

### TL;DR
`tui-use` is a CLI tool and PTY-based runtime that lets AI agents interact with terminal programs, REPLs, debuggers, and full-screen TUI apps as if a human were typing at the keyboard.

### Key Quote
“Like BrowserUse, but for the terminal.”

### Summary
- `tui-use` is positioned as a way for agents to do in the terminal what BrowserUse does in the browser: interact with programs that expect interactive human input.
- It addresses a gap in normal shell automation:
  - shell commands and APIs are easy for agents
  - REPLs, debuggers, and TUI programs block waiting for keyboard interaction
- The tool spawns programs in a PTY, reads the screen as plain text, and sends keystrokes through a command-line interface.
- Main use cases called out:
  - **Scientific computing / large in-memory state**: inspect live Python/pdb sessions without dumping huge variables to logs
  - **Debugger sessions**: drive GDB, PDB, and similar debuggers without restarting the process
  - **REPL sessions**: interact with Python, Node, and other interpreters
  - **TUI applications**: navigate tools like `vim`, `lazygit`, `htop`, and `fzf`
- The README explicitly targets AI coding agents such as:
  - Claude Code
  - Cursor
  - Codex
  - Gemini CLI
  - OpenCode
- Motivation vs. `tmux`:
  - `tmux send-keys` does not tell you when the program is done responding
  - agents end up guessing with `sleep` or polling `capture-pane`
  - `tui-use` listens to PTY render events directly
  - `wait` resolves when the screen stabilizes
  - `wait --text ">>>"` waits for a semantic cue instead of just silence
- Key features:
  - **Full VT rendering** via a headless xterm emulator
  - **Smart wait** with debounce-based stability detection and optional text matching
  - **Snapshot model** for explicit read/decide/type loops
  - **Highlights** extraction for inverse-video spans, useful for menus and active selections
- Installation options:
  - `npm install -g tui-use` is the recommended path
  - source install via `git clone`, `npm install`, `npm run build`, `npm link`
- The repo includes agent integrations:
  - a **Codex plugin bundle** under `plugins/tui-use`
  - a **Claude Code marketplace/plugin** flow via `/plugin marketplace add onesuper/tui-use`
- The README explains the architecture:
  - program output flows through PTY
  - into a headless terminal emulator
  - render events reset a debounce timer
  - `wait` resolves after silence or when a pattern appears
  - a daemon manages PTY sessions across CLI calls
- CLI commands documented include:
  - session lifecycle: `start`, `use`, `list`, `info`, `rename`, `kill`
  - interaction: `type`, `paste`, `press`
  - inspection: `snapshot`, `find`, `scrollup`, `scrolldown`
  - synchronization: `wait`
  - daemon control: `daemon status`, `stop`, `restart`
- Limitations:
  - terminal **color/style information is mostly lost**
  - `screen` is plain text only
  - selected items/active elements are exposed through `highlights`
  - `title` and `is_fullscreen` are captured
- Troubleshooting notes:
  - if no prebuilt binary is available, it rebuilds from source
  - build tools may be required on macOS/Linux
  - Windows has prebuilt binaries available
- Development and testing:
  - shows how to clone, build, link, and try the tool with `examples/ask.py`
  - includes an integration test skill for Claude Code: `/tui-use-integration-test`
- License is MIT.

### Assessment
This is a **mixed** content type: primarily a **tool/reference** README with some tutorial-like install and usage sections. Durability is **medium** because the core PTY/terminal-agent concept is fairly stable, but commands, plugin workflows, and supported agents may change as the project evolves. Density is **high**: it packs motivation, architecture, feature claims, command reference, integrations, limitations, troubleshooting, and development notes into a single page. Originality is mostly **primary source**, since it describes the project’s own design and usage rather than summarizing others. It is best used as **refer-back** material, especially for installation, CLI commands, and understanding the core wait/snapshot model. Scrape quality is **good**: the main README content appears intact, including code blocks and section structure, though as a README it may omit deeper implementation details beyond the documentation presented here.
