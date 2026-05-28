---
url: https://github.com/mpfaffenberger/code_puppy/
title: 'mpfaffenberger/code_puppy: Agentic AI for writing code'
scraped_at: '2026-04-12T07:32:48Z'
word_count: 3178
raw_file: raw/2026-04-12_mpfaffenberger-code-puppy-agentic-ai-for-writing-code_ec9a5d37.txt
tldr: Code Puppy is a Python 3.11+ open-source, privacy-focused agentic AI coding tool that competes with IDE assistants like Cursor/Windsurf, supports model browsing via models.dev, custom agents/commands, MCP, DBOS durable execution, and a strong “no telemetry, no prompt logging” privacy stance.
key_quote: “Code Puppy is an AI-powered code generation agent, designed to understand programming tasks, generate high-quality code, and explain its reasoning similar to tools like Windsurf and Cursor.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- mpfaffenberger
tools:
- code-puppy
- uvx
- models.dev
- DBOS
- MCP
- Ollama
libraries:
- Pydantic AI
- dbos-transact-py
companies:
- OpenAI
- Anthropic
- Google
- Cerebras
- Groq
- Mistral
- xAI
- Cohere
- Perplexity
- DeepInfra
- Together AI
- AIHubMix
- Synthetic
- Windsurf
- Cursor
tags:
- ai-coding-assistant
- agentic-ai
- privacy
- python
- developer-tools
---

### TL;DR
Code Puppy is a Python 3.11+ open-source, privacy-focused agentic AI coding tool that competes with IDE assistants like Cursor/Windsurf, supports model browsing via models.dev, custom agents/commands, MCP, DBOS durable execution, and a strong “no telemetry, no prompt logging” privacy stance.

### Key Quote
“Code Puppy is an AI-powered code generation agent, designed to understand programming tasks, generate high-quality code, and explain its reasoning similar to tools like Windsurf and Cursor.”

### Summary
- **What it is**
  - GitHub repo for **`mpfaffenberger/code_puppy`**, described as “Agentic AI for writing code.”
  - Positioned as “the sassy AI code agent that makes IDEs look outdated.”
  - The README frames it as a reaction against **Windsurf and Cursor** removing model access and raising prices.

- **Core capabilities**
  - AI code-generation agent that can:
    - understand programming tasks
    - generate code
    - explain reasoning
  - Uses a tool-based agent system with file and shell access.
  - Supports multiple agents, including a default **`code-puppy`** persona and an **`agent-creator`** for making custom agents.

- **Quick start / installation**
  - Main launch command: `uvx code-puppy -i`
  - Recommended install path is via **UV**:
    - macOS/Linux: install UV with `curl -LsSf https://astral.sh/uv/install.sh | sh`
    - Windows: install UV with PowerShell via `irm https://astral.sh/uv/install.ps1 | iex`
  - Windows notes emphasize global installation for better keyboard shortcut behavior.

- **Model integration**
  - Integrates with **models.dev** for browsing and adding models from **65+ providers**.
  - `/add_model` opens an interactive TUI that lets you:
    - browse providers
    - preview model capabilities, pricing, context length, features
    - add a model with correct endpoints/API key configuration
  - Offers **live API fetching** with **offline fallback** to a bundled database.
  - Mentions providers such as:
    - OpenAI, Anthropic, Google, Cerebras, Groq, Mistral, xAI, Cohere, Perplexity, DeepInfra, Together AI, AIHubMix
  - Warns about:
    - unsupported providers requiring special auth
    - models lacking tool-calling support

- **Durable execution**
  - Supports **DBOS durable execution** through `DBOSAgent`.
  - When enabled, it checkpoints:
    - agent inputs
    - LLM responses
    - MCP calls
    - tool calls
  - Can be toggled with `/set enable_dbos false` and is enabled by default.
  - Configuration is controlled via env vars like:
    - `DBOS_CONDUCTOR_KEY`
    - `DBOS_LOG_LEVEL`
    - `DBOS_SYSTEM_DATABASE_URL`
    - `DBOS_APP_VERSION`

- **Custom commands**
  - Supports custom slash commands via markdown files in:
    - `.claude/commands/`
    - `.github/prompts/`
    - `.agents/commands/`
  - Filename becomes the command name; content becomes the prompt.

- **Requirements**
  - Python **3.11+**
  - API keys for:
    - OpenAI
    - Gemini
    - Cerebras
    - Anthropic
  - An Ollama endpoint is also listed.

- **Agent system**
  - Supports **AGENT.md** files for coding standards and style rules.
  - `/agent` command:
    - shows current agent and available agents
    - switches agents
    - opens the agent creator
  - `/truncate <N>` trims message history while preserving the system message.
  - Agent discovery includes:
    - built-in Python agents in `code_puppy/agents/`
    - user JSON agents in `~/.code_puppy/agents/`

- **Available agents**
  - **Code-Puppy (`code-puppy`)**
    - default general-purpose coding assistant
    - playful/sarcastic/pedantic personality
    - full tool access
    - enforces max 600 lines per file
  - **Agent Creator (`agent-creator`)**
    - helps build custom JSON agent configs
    - validates schema and guides creation

- **Tool access**
  - Listed tools include:
    - `list_files`
    - `read_file`
    - `grep`
    - `create_file`
    - `replace_in_file`
    - `delete_snippet`
    - `delete_file`
    - `agent_run_shell_command`
    - `agent_share_your_reasoning`
  - Notes that `edit_file` still works and expands into file-editing tools.

- **Round-robin model distribution**
  - Supports rotating across multiple models to reduce rate-limit pressure.
  - Example config uses three Cerebras API keys and a `round_robin` model that rotates every 5 requests.

- **Extensibility**
  - The README goes deep on creating new agents:
    - Python agents subclass `BaseAgent`
    - JSON agents define `name`, `description`, `system_prompt`, `tools`, etc.
  - Custom agents can be built for:
    - tutoring
    - code review
    - DevOps
    - web/data/mobile workflows
  - Provides schema examples and file locations for both Python and JSON agents.

- **Docs and implementation references**
  - Implementation files named in the README:
    - `code_puppy/agents/json_agent.py`
    - `code_puppy/agents/agent_manager.py`
    - tests in `tests/test_json_agents.py`
  - Includes troubleshooting for:
    - agent not found
    - validation errors
    - permission issues

- **Privacy / trust**
  - Strong privacy commitment:
    - no telemetry
    - no prompt logging
    - no behavioral profiling
    - no third-party data sharing
  - Clarifies that prompts still go to whichever LLM provider you configure.
  - Claims a fully local setup is possible with VLLM/SGLang/Llama.cpp, keeping data on your network.

- **License / community**
  - Licensed under **MIT**.
  - Mentions a Discord community and a docs site.
  - Uses badges to claim build/tests passing and “100% Open Source.”

### Assessment
This is a **mixed** content piece that is primarily a **reference/docs** README with some **tutorial** and **announcement/marketing** elements. Durability is **medium**: the core concepts around agentic coding, custom agents, and privacy-first design are fairly stable, but many specifics—supported providers, endpoints, DBOS integration, model availability, and commands—are version- and ecosystem-dependent. Density is **high** because the README packs in installation steps, command usage, architecture, examples, environment variables, and configuration snippets. Originality is mostly a **primary source** for the project’s own features and philosophy, though it also references external services like models.dev and DBOS. For later use, this is best treated as **refer-back** material: useful for setup, feature comparison, and confirming capabilities. Scrape quality looks **good**, with a very large amount of README content captured, including commands, examples, and configuration details; however, any images, linked docs, and external pages are not included, so some context may still be missing.
