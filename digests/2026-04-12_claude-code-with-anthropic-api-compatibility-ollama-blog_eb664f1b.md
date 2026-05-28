---
url: https://ollama.com/blog/claude
title: Claude Code with Anthropic API compatibility · Ollama Blog
scraped_at: '2026-04-12T07:28:57Z'
word_count: 434
raw_file: raw/2026-04-12_claude-code-with-anthropic-api-compatibility-ollama-blog_eb664f1b.txt
tldr: Ollama v0.14.0+ adds Anthropic Messages API compatibility, letting Claude Code and Anthropic SDK apps run against local Ollama models or Ollama Cloud models via a simple base URL change.
key_quote: Ollama v0.14.0 and later are now compatible with the Anthropic Messages API, making it possible to use tools like Claude Code with open-source models.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Claude Code
libraries:
- anthropic
companies:
- Ollama
- Anthropic
tags:
- api-compatibility
- coding-agents
- local-llms
- function-calling
- developer-tools
---

### TL;DR
Ollama v0.14.0+ adds Anthropic Messages API compatibility, letting Claude Code and Anthropic SDK apps run against local Ollama models or Ollama Cloud models via a simple base URL change.

### Key Quote
“Ollama v0.14.0 and later are now compatible with the Anthropic Messages API, making it possible to use tools like Claude Code with open-source models.”

### Summary
- **What this announcement is about**
  - Ollama released Anthropic Messages API compatibility in **v0.14.0 and later**.
  - This enables **Claude Code**, Anthropic’s terminal-based agentic coding tool, to work with **Ollama models**.
  - It supports both:
    - **Local models** running on your machine
    - **Cloud models** through **ollama.com**

- **Using Claude Code with Ollama**
  - Install Claude Code:
    - **macOS / Linux / WSL**: `curl -fsSL https://claude.ai/install.sh | bash`
    - **Windows PowerShell**: `irm https://claude.ai/install.ps1 | iex`
    - **Windows CMD**: `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`
  - Configure environment variables:
    - `export ANTHROPIC_AUTH_TOKEN=ollama`
    - `export ANTHROPIC_BASE_URL=http://localhost:11434`
  - Run Claude Code with a local Ollama model:
    - `claude --model gpt-oss:20b`
  - Run it with a cloud model:
    - `claude --model glm-4.7:cloud`

- **Model guidance**
  - Ollama recommends using a model with **at least 32K tokens of context length** for coding tasks.
  - Ollama notes that **cloud models always run at full context length**.
  - Recommended coding models listed:
    - **Local:** `gpt-oss:20b`, `qwen3-coder`
    - **Cloud:** `glm-4.7:cloud`, `minimax-m2.1:cloud`

- **Using the Anthropic SDK with Ollama**
  - Existing apps using the Anthropic SDK can connect by changing the **base URL** to Ollama.
  - Example Python setup:
    - `base_url='http://localhost:11434'`
    - `api_key='ollama'` (required but ignored)
  - Example JavaScript setup:
    - `baseURL: 'http://localhost:11434'`
    - `apiKey: 'ollama'`
  - Example code shows a `messages.create(...)` call using model `qwen3-coder`.

- **Tool calling**
  - The post demonstrates Anthropic-style **tool use / function calling** with Ollama.
  - Example defines a `get_weather` tool with a JSON schema requiring a `location` string.
  - The model can return a `tool_use` block, including tool name and input.

- **Supported features**
  - Messages and multi-turn conversations
  - Streaming
  - System prompts
  - Tool calling / function calling
  - Extended thinking
  - Vision (image input)
  - The post points readers to Ollama’s **Anthropic compatibility documentation** for the full list.

- **Where to learn more**
  - For more detailed setup and configuration, the post refers readers to the **Claude Code guide**.
  - For broader compatibility details, it points to **Anthropic compatibility documentation** and **context length documentation**.

### Assessment
This is a **mixed announcement/reference** post with **high durability** for the integration pattern but some version-sensitive details tied to **Ollama v0.14.0+**, specific install commands, and model recommendations that may change over time. The content is **dense** and practical, with concrete commands, environment variables, model names, and code snippets, making it useful as a **refer-back** resource rather than something to skim once. It appears to be a **primary-source** product announcement/documentation post from Ollama, and the scrape quality is **good**: the main text, code examples, and feature list are present, with no obvious missing sections beyond any visual formatting or page chrome.
