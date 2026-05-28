---
url: https://github.com/cegersdoerfer/pi-ptc
title: 'cegersdoerfer/pi-ptc: Programmatic Tool Calling for the pi-coding-agent'
scraped_at: '2026-04-19T07:03:20Z'
word_count: 1619
raw_file: raw/2026-04-19_cegersdoerfer-pi-ptc-programmatic-tool-calling-for-the-pi-coding-agent_a732ccfc.txt
tldr: This repository provides a pi-coding-agent extension that lets Claude run Python code with async access to tools, so multi-step workflows can happen in one LLM round-trip instead of many.
key_quote: Claude writes Python code that calls tools as async functions, dramatically reducing token usage and latency for multi-tool workflows.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Claude
tools:
- code_execution
- glob
- read
- bash
libraries: []
companies:
- pi-coding-agent
tags:
- llm-tool-calling
- python-automation
- agent-frameworks
- developer-tools
- docker-isolation
---

### TL;DR
This repository provides a pi-coding-agent extension that lets Claude run Python code with async access to tools, so multi-step workflows can happen in one LLM round-trip instead of many.

### Key Quote
“Claude writes Python code that calls tools as async functions, dramatically reducing token usage and latency for multi-tool workflows.”

### Summary
- **What it is**
  - A **Programmatic Tool Calling (PTC)** extension for **pi-coding-agent**.
  - Designed so Claude can write **Python code** that invokes tools as **async functions**.
  - The main goal is to reduce **token usage** and **latency** for workflows that require many tool calls.

- **Core problem it addresses**
  - Normally, multi-tool workflows require repeated LLM round-trips:
    - tool call → result returned → model processes result → next tool call
  - Each intermediate result consumes context tokens and adds latency.

- **Core solution**
  - Claude writes Python that orchestrates tool use locally.
  - The `code_execution` tool runs that Python code.
  - Tool outputs stay inside the Python runtime until the final result is returned to Claude.

- **Main benefits claimed**
  - Reduced token usage from intermediate tool results
  - Lower latency from fewer LLM round-trips
  - Support for loops, conditionals, and aggregation in workflows
  - Optional Docker isolation for better security

- **Requirements**
  - Node.js 18+
  - Python 3.12+ available as `python3`
  - pi-coding-agent installed
  - Docker optional for isolated execution

- **Installation**
  - Clone repo, run:
    ```bash
    npm install
    npm run build
    ```
  - Link it into pi-coding-agent extension directories:
    - Global: `~/.pi/agent/extensions/ptc`
    - Project-specific: `<project>/.pi/extensions/ptc`
  - Restart pi-coding-agent to load the extension

- **Available tools**
  - By default, Python inside PTC can use **pi-coding-agent built-in tools** like:
    - `glob`
    - `read`
    - `bash`
  - Tools from other pi extensions are **not** exposed through this API.
  - To add more tools, place `.js` files in `tools/`.

- **Usage pattern**
  - Once installed, Claude can use `code_execution` to run Python code.
  - Custom tools become async Python functions.
  - Examples show:
    - querying a DB and sending notifications
    - iterating over weather queries
    - combining `read` with a custom deploy tool
    - conditional health checks with restart logic

- **Custom tools**
  - Add `.js` files in `tools/`.
  - Each tool exports an object with:
    - `name`
    - `description`
    - `parameters`
    - `execute(toolCallId, params, signal)`
  - Only `.js` files are loaded; `.ts` and `.example` files are ignored.
  - Restart pi-coding-agent after adding tools.

- **How it works**
  - The extension:
    1. discovers available tools
    2. generates Python wrapper functions
    3. combines wrappers with user code
    4. launches Python in Docker or subprocess mode
  - Python calls tools through a JSON RPC bridge back to Node.js.
  - Final output is returned to the LLM.

- **Architecture/components**
  - `src/index.ts` — extension entry point
  - `src/sandbox-manager.ts` — Docker/subprocess management
  - `src/code-executor.ts` — execution orchestration
  - `src/tool-wrapper.ts` — generates Python wrappers
  - `src/tool-loader.ts` — loads custom tools
  - `src/rpc-protocol.ts` and `src/python-runtime/rpc.py` — Node/Python RPC
  - `src/python-runtime/runtime.py` — Python execution runtime

- **Execution modes**
  - **Subprocess mode** (default)
    - runs `python3` locally
    - minimal isolation
    - simplest setup
  - **Docker mode** (`PTC_USE_DOCKER=true`)
    - network disabled
    - workspace mounted read-only
    - memory and CPU limits
    - container reused for up to 4.5 minutes
  - Important caveat: even with Docker, tool execution still happens on the host via RPC, so it is not a full security boundary.

- **Limits**
  - Timeout: **270 seconds**
  - Max output: **100 KB**
  - Supports cancellation / Ctrl+C

- **Development notes**
  - Build commands:
    - `npm run build`
    - `npm run watch`
    - `npm run clean`
  - The repo includes a TypeScript source tree and a Python runtime subdirectory.

- **Troubleshooting / FAQ highlights**
  - Check extension discovery with `pi --list-extensions`
  - Verify symlink and build output in `dist/`
  - Ensure Python 3.12+ is installed
  - Tool names and parameter types must match exactly
  - Python syntax errors and tracebacks are returned to Claude
  - Standard library only; external Python packages are not supported by default

### Assessment
This is a **technical reference/tutorial** for a current extension architecture, so durability is **medium**: the core idea of reducing LLM round-trips with local orchestration is durable, but the installation steps, file structure, and compatibility details are tied to the current pi-coding-agent and Python/Node setup. The content is a **mixed** piece: it combines how-to installation, implementation docs, and product explanation. Density is **high**, with many concrete commands, file paths, tool contracts, and execution details. It is **primary source** material because it describes the repository’s own design and behavior rather than summarizing others. This is best used as **refer-back** documentation for setup, tool authoring, and architecture questions. Scrape quality appears **good**: the README structure, examples, commands, and caveats are present, though code files and images are not included beyond the text shown.
