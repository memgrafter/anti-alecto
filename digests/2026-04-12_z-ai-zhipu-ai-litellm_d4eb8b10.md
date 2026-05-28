---
url: https://docs.litellm.ai/docs/providers/zai
title: Z.AI (Zhipu AI) | liteLLM
scraped_at: '2026-04-12T07:41:02Z'
word_count: 409
raw_file: raw/2026-04-12_z-ai-zhipu-ai-litellm_d4eb8b10.txt
tldr: LiteLLM’s Z.AI integration lets you call Zhipu AI GLM chat/text models by prefixing model names with `zai/`, using `ZAI_API_KEY`, and supports both direct SDK calls and LiteLLM Proxy setup.
key_quote: We support Z.AI GLM text/chat models, just set zai/ as a prefix when sending completion requests
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- litellm
libraries: []
companies:
- Z.AI
- Zhipu AI
tags:
- llm-providers
- api-integration
- proxy-configuration
- model-pricing
- streaming-completions
---

### TL;DR
LiteLLM’s Z.AI integration lets you call Zhipu AI GLM chat/text models by prefixing model names with `zai/`, using `ZAI_API_KEY`, and supports both direct SDK calls and LiteLLM Proxy setup.

### Key Quote
"We support Z.AI GLM text/chat models, just set zai/ as a prefix when sending completion requests"

### Summary
- **What this page is:** A LiteLLM provider docs page for **Z.AI (Zhipu AI)** integration.
- **Core usage pattern:**
  - Set the API key in the environment as `os.environ['ZAI_API_KEY']`
  - Call models with the prefix `zai/`, e.g. `model="zai/glm-4.7"`
- **Basic SDK example:**
  - Import `completion` from `litellm`
  - Pass a `messages` list with a user prompt
  - Print the response
- **Streaming example:**
  - Same setup as normal completion
  - Add `stream=True`
  - Iterate over returned chunks with `for chunk in response:`
- **Supported models listed:**
  - `glm-4.7` — latest flagship, **200K context**, reasoning
  - `glm-4.6` — **200K context**
  - `glm-4.5` — **128K context**
  - `glm-4.5v` — vision model
  - `glm-4.5-x` — premium tier
  - `glm-4.5-air` — lightweight
  - `glm-4.5-airx` — fast lightweight
  - `glm-4-32b-0414-128k` — 32B parameter model
  - `glm-4.5-flash` — **FREE tier**
- **Pricing table included for each model:**
  - `glm-4.7`: input **$0.60/M tokens**, output **$2.20/M**, cached input **$0.11/M**, context **200K**
  - `glm-4.6`: **$0.60 / $2.20**, 200K
  - `glm-4.5`: **$0.60 / $2.20**, 128K
  - `glm-4.5v`: **$0.60 / $1.80**, 128K
  - `glm-4.5-x`: **$2.20 / $8.90**, 128K
  - `glm-4.5-air`: **$0.20 / $1.10**, 128K
  - `glm-4.5-airx`: **$1.10 / $4.50**, 128K
  - `glm-4-32b-0414-128k`: **$0.10 / $0.10**, 128K
  - `glm-4.5-flash`: **FREE / FREE**, 128K
- **LiteLLM Proxy setup:**
  - Example `config.yaml` maps internal model names like `glm-4.7` to provider models like `zai/glm-4.7`
  - Uses `api_key: os.environ/ZAI_API_KEY`
  - Run with `litellm --config config.yaml`
  - Test via `curl` to `http://0.0.0.0:4000/v1/chat/completions` with an `Authorization: Bearer sk-1234` header
- **Notable detail:** The docs show both direct SDK usage and proxy-based deployment, making it useful for either app integration or hosted gateway setup.

### Assessment
This is a **reference** document with **medium-high durability**: the general integration pattern is stable, but the model list and pricing are tied to current Z.AI offerings and may change. The content type is **mixed**, leaning heavily toward **reference/tutorial**. Density is **high** because it includes setup, code samples, model support, pricing, and proxy configuration in a compact format. It is a **primary source** for LiteLLM usage with Z.AI, not commentary or synthesis. Best used as **refer-back** material when implementing or updating an integration. Scrape quality looks **good** overall: the essential text, tables, and code examples are present, though formatting is flattened and indentation is not fully preserved, which may matter for copy-pasting the YAML and Python snippets.
