---
url: https://github.com/memgrafter/flatagents/blob/main/sdk/examples/coding_agent_cli/python/src/tool_use_cli/main.py
title: flatagents/sdk/examples/coding_agent_cli/python/src/tool_use_cli/main.py at main · memgrafter/flatagents
scraped_at: '2026-04-19T07:16:31Z'
word_count: 473
raw_file: raw/2026-04-19_flatagents-sdk-examples-coding-agent-cli-python-src-tool-use-cli-main-py-at-main_0a03c466.txt
tldr: This file is the entry point for a Python “Tool Use CLI” coding agent that can run in interactive REPL mode, single-shot mode, or standalone no-human-review mode, using configurable FlatAgent/FlatMachine tool loops over a working directory.
key_quote: 'Default: interactive REPL. Use -p for single-shot mode.'
durability: medium
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- readline
- python
libraries:
- flatagents
- flatmachines
- LiteLLM
companies:
- memgrafter
tags:
- cli-tools
- coding-agents
- tool-use
- python
- repl
---

### TL;DR
This file is the entry point for a Python “Tool Use CLI” coding agent that can run in interactive REPL mode, single-shot mode, or standalone no-human-review mode, using configurable FlatAgent/FlatMachine tool loops over a working directory.

### Key Quote
"Default: interactive REPL. Use -p for single-shot mode."

### Summary
- This is a CLI script for a coding agent with tools for **read, write, bash, and edit** operations.
- It supports three main modes:
  - **Default REPL**: interactive loop where you type tasks and the agent executes them with human review.
  - **Single-shot mode** via `-p/--print TASK`: runs one task and exits.
  - **Standalone mode** via `--standalone TASK` or `--standalone -p TASK`: runs a `ToolLoopAgent` directly, without the `FlatMachine` and without human review.
- It loads configuration from:
  - `config/machine.yml` for the machine-based workflow
  - `config/agent.yml` for the standalone agent workflow
- The script determines the config path relative to the file location via `_config_path(name)`.
- Logging is kept quiet by default:
  - Reads `LOG_LEVEL` from the environment
  - Defaults to `WARNING`
  - Applies that level to `flatagents`, `flatmachines`, and `LiteLLM`
- It suppresses certain warnings about validation and Flatmachine/Flatagent schema issues.
- It optionally enables `readline` for better terminal input behavior like arrow keys and history.
- `run_machine(task, working_dir)`:
  - Creates `CLIToolHooks`
  - Instantiates `FlatMachine` with the machine config and hooks
  - Calls `machine.execute()` with:
    - `task`
    - `working_dir`
- `run_standalone(task, working_dir)`:
  - Creates a `FlatAgent` from `agent.yml`
  - Creates a `CLIToolProvider` for the working directory
  - Wraps them in `ToolLoopAgent`
  - Applies guardrails:
    - `max_turns=30`
    - `max_tool_calls=100`
    - `max_cost=2.00`
    - `tool_timeout=60.0`
    - `total_timeout=600.0`
  - Prints a completion report including:
    - stop reason
    - tool call count
    - LLM turns
    - API calls
    - total cost
    - any error
    - returned content
- `repl(working_dir)`:
  - Prints the working directory banner
  - Repeatedly prompts with `> `
  - Handles:
    - single `Ctrl-C` by clearing input
    - double `Ctrl-C` by exiting
    - `Ctrl-D` (`EOFError`) by exiting
  - Runs each entered task through `run_machine()`
- `main()` parses CLI arguments:
  - `-p/--print TASK`: single task mode
  - `--working-dir/-w`: directory for file operations, defaulting to current directory
  - `--standalone/-s`: standalone mode, optionally taking a task directly
- Control flow:
  - If `--standalone` is used, it runs `run_standalone()`
  - Else if `-p/--print` is used, it runs `run_machine()`
  - Otherwise it starts the REPL
- The module is meant to be run directly with `python -m tool_use_cli.main`.

### Assessment
This is a **tutorial/reference hybrid**: it documents and implements a CLI workflow rather than presenting an argument or research result. **Durability is medium** because the overall structure of a CLI agent entry point is fairly stable, but it is tied to specific project modules (`FlatMachine`, `FlatAgent`, `ToolLoopAgent`) and current config conventions (`machine.yml`, `agent.yml`). The content is **dense** and fairly specific, with concrete arguments, defaults, and guardrails, and it is **primary source** code rather than commentary or synthesis. It is best used as **refer-back** material when you need to remember how to invoke the CLI, what modes exist, or where execution paths diverge. **Scrape quality is good** for the visible file contents: the main code and docstring are present, though only this single file is included, so related hook/tool/config implementations are not shown.
