---
url: https://github.com/ghuntley/how-to-build-a-coding-agent
title: 'ghuntley/how-to-build-a-coding-agent: A workshop that teaches you how to build your own coding agent. Similar to Roo code, Cline, Amp, Cursor, Windsurf or OpenCode.'
scraped_at: '2026-04-12T09:36:53Z'
word_count: 1131
raw_file: raw/2026-04-12_ghuntley-how-to-build-a-coding-agent-a-workshop-that-teaches-you-how-to-build-yo_46ebc323.txt
tldr: A step-by-step Go workshop for building a local Claude-powered coding agent, starting from a basic chat app and progressively adding file reading, directory listing, shell execution, file editing, and code search tools.
key_quote: We call this the **event loop** — it's like the agent's heartbeat.
durability: medium
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- devenv
- ripgrep
libraries: []
companies:
- Anthropic
tags:
- coding-agents
- go
- claude
- tool-use
- workshop
---

### TL;DR
A step-by-step Go workshop for building a local Claude-powered coding agent, starting from a basic chat app and progressively adding file reading, directory listing, shell execution, file editing, and code search tools.

### Key Quote
“We call this the **event loop** — it's like the agent's heartbeat.”

### Summary
- This GitHub repository is a workshop titled **“Build Your Own Coding Agent”** and is presented as similar in spirit to tools like **Roo code, Cline, Amp, Cursor, Windsurf, or OpenCode**.
- The workshop aims to teach how to build an **AI-powered coding assistant** using **Go** and the **Anthropic Claude API**.
- It is structured as **6 progressive versions** of the agent:
  1. `chat.go` — basic chat with Claude
  2. `read.go` — read files
  3. `list_files.go` — list directory contents
  4. `bash_tool.go` — run shell commands
  5. `edit_tool.go` — edit files / create code
  6. `code_search_tool.go` — search code using pattern matching
- The core architecture is an **event loop**:
  - receive user input
  - send it to Claude
  - let Claude either answer directly or request a tool
  - execute the tool
  - return tool results to Claude
  - continue until a final answer is produced
- The repo includes:
  - **prerequisites**: Go **1.24.2+** or **devenv**, plus an **Anthropic API key**
  - setup instructions:
    - `devenv shell`
    - or `go mod tidy`
    - `export ANTHROPIC_API_KEY="your-api-key-here"`
  - run commands for each stage, e.g.:
    - `go run chat.go`
    - `go run read.go`
    - `go run list_files.go`
    - `go run bash_tool.go`
    - `go run edit_tool.go`
    - `go run code_search_tool.go`
- It highlights sample files included in the repo:
  - `fizzbuzz.js`
  - `riddle.txt`
  - `AGENT.md`
- It explains tool design at a high level:
  - each tool has a **name**, **input schema**, and **function**
  - schema generation is based on **Go structs**
- Troubleshooting advice covers:
  - API key issues
  - Go setup/version issues
  - tool execution errors
  - environment problems
- The ending suggests extensions beyond the workshop, such as:
  - custom tools
  - tool chains
  - memory across sessions
  - a web UI
  - support for other AI models

### Assessment
This is a **tutorial/workshop** with strong instructional structure and fairly high information density, though it reads like a guided repo README rather than a deep technical spec. Its durability is **medium**: the core agent patterns are broadly useful, but the concrete setup depends on **Go 1.24.2+**, the **Anthropic Claude API**, and the current state of the repository. It appears to be a **primary source** for the workshop content, not a synthesis or commentary, and it’s best used as a **refer-back** reference while following the repo or as a **deep-study** starting point if you want to reproduce the agent yourself. Scrape quality is **good**: the main sections, commands, architecture explanation, and examples are present, though code implementation details and any deeper repo files are not included here.
