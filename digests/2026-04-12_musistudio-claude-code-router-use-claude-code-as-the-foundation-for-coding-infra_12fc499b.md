---
url: https://github.com/musistudio/claude-code-router
title: 'musistudio/claude-code-router: Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic.'
scraped_at: '2026-04-12T09:40:14Z'
word_count: 2885
raw_file: raw/2026-04-12_musistudio-claude-code-router-use-claude-code-as-the-foundation-for-coding-infra_12fc499b.txt
tldr: Claude Code Router is a self-hosted proxy/launcher for Claude Code that lets you route coding tasks to different LLM providers and models, customize requests with transformers, and manage everything via CLI, UI, presets, and GitHub Actions.
key_quote: A powerful tool to route Claude Code requests to different models and customize any request.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- musistudio
- Anthropic
- Z.ai
- Simon Leischnig
tools:
- Claude Code
- Claude Code Router
- ccr
- GitHub Actions
libraries: []
companies:
- Anthropic
- OpenRouter
- DeepSeek
- Ollama
- Gemini
- Volcengine
- SiliconFlow
- modelscope
- dashscope
- aihubmix
- Z.ai
tags:
- llm-routing
- coding-assistants
- model-providers
- cli-tools
- developer-automation
---

### TL;DR
Claude Code Router is a self-hosted proxy/launcher for Claude Code that lets you route coding tasks to different LLM providers and models, customize requests with transformers, and manage everything via CLI, UI, presets, and GitHub Actions.

### Key Quote
"A powerful tool to route Claude Code requests to different models and customize any request."

### Summary
- **What it is**
  - An open-source project by **musistudio** for using **Claude Code as the foundation for coding infrastructure**.
  - It acts as a **router/proxy** between Claude Code and model providers, so you can choose how requests are handled while still benefiting from Anthropic updates.
  - Includes a Chinese README link and Discord community link.

- **Core features**
  - **Model routing** for different task types:
    - `default`
    - `background`
    - `think`
    - `longContext`
    - `webSearch`
    - `image` (beta)
  - **Multi-provider support**:
    - OpenRouter
    - DeepSeek
    - Ollama
    - Gemini
    - Volcengine
    - SiliconFlow
    - modelscope
    - dashscope
    - aihubmix
  - **Transformers** to adapt request/response formats for different APIs.
  - **Dynamic switching** with `/model provider,model`.
  - **CLI model management** via `ccr model`.
  - **UI mode** via `ccr ui`.
  - **Presets** for exporting/installing configurations.
  - **GitHub Actions support** for non-interactive automation.
  - **Plugin/custom transformer system**.

- **Installation**
  - First install Claude Code:
    - `npm install -g @anthropic-ai/claude-code`
  - Then install Claude Code Router:
    - `npm install -g @musistudio/claude-code-router`
  - Run Claude Code through the router with:
    - `ccr code`
  - Restart after config changes with:
    - `ccr restart`

- **Configuration**
  - Config file lives at:
    - `~/.claude-code-router/config.json`
  - Important config fields:
    - `PROXY_URL`
    - `LOG`
    - `LOG_LEVEL`
    - `APIKEY`
    - `HOST`
    - `NON_INTERACTIVE_MODE`
    - `Providers`
    - `Router`
    - `API_TIMEOUT_MS`
  - Logging is split into:
    - **Server-level logs** in `~/.claude-code-router/logs/`
    - **Application-level logs** in `~/.claude-code-router/claude-code-router.log`
  - Supports **environment variable interpolation** with `$VAR_NAME` and `${VAR_NAME}`.
  - `APIKEY` enables authenticated access; without it, host is forced to `127.0.0.1` for safety.

- **Provider configuration**
  - Each provider needs:
    - `name`
    - `api_base_url`
    - `api_key`
    - `models`
    - optional `transformer`
  - Example routing setup in the README maps:
    - `default` to DeepSeek chat
    - `background` to Ollama
    - `think` to DeepSeek reasoning
    - `longContext` to Gemini Pro preview
    - `webSearch` to Gemini flash
  - The example also demonstrates provider-specific transformer chains and model-specific transformer overrides.

- **Transformers**
  - Built-in transformers listed include:
    - `Anthropic`
    - `deepseek`
    - `gemini`
    - `openrouter`
    - `groq`
    - `maxtoken`
    - `tooluse`
    - `gemini-cli` (experimental)
    - `reasoning`
    - `sampling`
    - `enhancetool`
    - `cleancache`
    - `vertex-gemini`
    - `chutes-glm`
    - `qwen-cli` (experimental)
    - `rovo-cli` (experimental)
  - Transformers can be:
    - applied globally to a provider
    - applied to a specific model
    - passed options like `maxtoken.max_tokens`
  - Custom transformers can be loaded from local paths in `config.json`.

- **Custom routing**
  - You can define `CUSTOM_ROUTER_PATH` to provide a JavaScript router function.
  - The custom router receives `req` and `config`, and returns a `"provider,model"` string or `null`.
  - Subagent routing uses a special prompt tag:
    - `<CCR-SUBAGENT-MODEL>provider,model</CCR-SUBAGENT-MODEL>`

- **Status line**
  - Version **v1.0.40** includes a built-in **statusline tool** shown as beta, configurable in the UI.

- **GitHub Actions / automation**
  - Shows an example workflow for running Claude Code in CI with the router.
  - Uses `NON_INTERACTIVE_MODE: true` to prevent stdin-related hangs.
  - Notes that the router can be used in automated workflows to run tasks off-peak and reduce costs.

- **Presets**
  - Presets can be exported, installed, listed, inspected, and deleted:
    - `ccr preset export`
    - `ccr preset install`
    - `ccr preset list`
    - `ccr preset info`
    - `ccr preset delete`
  - Export sanitizes sensitive data into placeholders like `{{field}}`.
  - Presets support metadata and versioning.

- **Audience / use case**
  - Best suited for users who:
    - want to swap models without changing workflow
    - need local or alternative providers
    - want automation in GitHub Actions
    - need fine-grained routing for background, reasoning, or long-context tasks

- **Notable staleness / limitations**
  - The README is **feature-heavy and configuration-focused**, but also includes sponsor/promotional content.
  - Some examples and model names are version-specific and may age quickly.
  - There are many provider/model references, so readers should verify current compatibility with their Claude Code and provider versions.

### Assessment
Durability is **medium**: the core idea of routing Claude Code through multiple providers and using transformers is fairly durable, but the concrete model names, endpoints, commands, and feature set are tied to current tooling and may change quickly. Content type is **mixed**—mostly tutorial/reference with some announcement, promotional, and community material. Density is **high** because the README packs many commands, config keys, routing modes, transformer names, and examples into a single document. Originality is primarily **primary source**, since this is the project’s own documentation rather than commentary. Reference style is **refer-back**: this is something you’d likely revisit when setting up or troubleshooting the router, not just skim once. Scrape quality looks **good** overall: the README text, commands, examples, and major sections are present, though images and linked blog posts are referenced rather than fully captured.
