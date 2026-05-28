---
url: https://docs.litellm.ai/docs/providers/fireworks_ai
title: Fireworks AI | liteLLM
scraped_at: '2026-04-12T07:38:16Z'
word_count: 1196
raw_file: raw/2026-04-12_fireworks-ai-litellm_767847eb.txt
tldr: LiteLLM’s Fireworks AI provider docs show how to call Fireworks models by prefixing model names with `fireworks_ai/`, including serverless, your own account, direct-route deployments, proxy setup, document inlining for non-vision models, `reasoning_effort`, audio transcription, and rerank.
key_quote: “We support ALL Fireworks AI models, just set fireworks_ai/ as a prefix when sending completion requests”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- liteLLM
libraries: []
companies:
- Fireworks AI
- LiteLLM
tags:
- llm-providers
- api-integration
- model-serving
- proxy-configuration
- firework-ai
---

### TL;DR
LiteLLM’s Fireworks AI provider docs show how to call Fireworks models by prefixing model names with `fireworks_ai/`, including serverless, your own account, direct-route deployments, proxy setup, document inlining for non-vision models, `reasoning_effort`, audio transcription, and rerank.

### Key Quote
“We support ALL Fireworks AI models, just set fireworks_ai/ as a prefix when sending completion requests”

### Summary
- This is a **provider integration guide** for using **Fireworks AI with LiteLLM**.
- Core rule: prefix Fireworks model names with `fireworks_ai/` for completion and embedding requests.
- The page lists supported OpenAI-style endpoints:
  - `/chat/completions`
  - `/embeddings`
  - `/completions`
  - `/audio/transcriptions`
  - `/rerank`
- It describes three integration modes:
  - **Fireworks serverless models**
  - **Models in your own Fireworks account**
  - **Direct-route deployments** with a specific `api_base`
- API key location:
  - `os.environ['FIREWORKS_AI_API_KEY']`

#### Sample SDK usage
- Example serverless chat call:
  - `model="fireworks_ai/accounts/fireworks/models/llama-v3-70b-instruct"`
- Streaming is supported with `stream=True`.
- For your own account, the model string changes to:
  - `fireworks_ai/accounts/fireworks/models/YOUR_MODEL_ID`
- Direct-route example:
  - `model="fireworks_ai/accounts/fireworks/models/qwen2p5-coder-7b#accounts/gitlab/deployments/2fb7764c"`
  - `api_base="https://gitlab-2fb7764c.direct.fireworks.ai/v1"`
- Note: for the **text completion** interface, the doc says to use:
  - `text-completion-openai/accounts/fireworks/models/qwen2p5-coder-7b#accounts/gitlab/deployments/2fb7764c`

#### LiteLLM Proxy usage
- Example `config.yaml` shows mapping a friendly proxy name to a Fireworks model.
- Start the proxy with:
  - `litellm --config config.yaml`
- Test via:
  - `curl`
  - OpenAI Python client
  - LangChain
- The doc includes proxy examples for both chat and LangChain calling the configured model name.

#### Document inlining
- LiteLLM supports document inlining for Fireworks AI.
- Important detail: it auto-adds `#transform=inline` to `image_url` URLs **when the model is not a vision model** but still needs to parse documents/images.
- The doc includes a sample using a PDF URL and a question about BA and MBA GPAs.
- There is a disable option:
  - `litellm.disable_add_transform_inline_image_block = True`
  - `disable_add_transform_inline_image_block: true`

#### Reasoning effort
- `reasoning_effort` is supported on select Fireworks models.
- Example shown with:
  - `model="fireworks_ai/accounts/fireworks/models/qwen3-8b"`
  - `reasoning_effort="low"`

#### Supported models
- The page emphasizes that **all Fireworks AI models are supported**.
- Example chat models listed include:
  - `llama-v3p2-1b-instruct`
  - `llama-v3p2-3b-instruct`
  - `llama-v3p2-11b-vision-instruct`
  - `llama-v3p2-90b-vision-instruct`
  - `mixtral-8x7b-instruct`
  - `firefunction-v1`
  - `llama-v2-70b-chat`
- Example embedding models listed include:
  - `fireworks_ai/nomic-ai/nomic-embed-text-v1.5`
  - `fireworks_ai/nomic-ai/nomic-embed-text-v1`
  - `fireworks_ai/WhereIsAI/UAE-Large-V1`
  - `fireworks_ai/thenlper/gte-large`
  - `fireworks_ai/thenlper/gte-base`

#### Audio transcription
- Quick start uses:
  - `from litellm import transcription`
  - `model="fireworks_ai/whisper-v3"`
- Proxy configuration sets:
  - `model_info: mode: audio_transcription`
- The endpoint shown is:
  - `/v1/audio/transcriptions`

#### Rerank
- Quick start uses:
  - `from litellm import rerank`
  - `model="fireworks_ai/fireworks/qwen3-reranker-8b"`
- Example includes:
  - `query`
  - `documents`
  - `top_n=3`
  - `return_documents=True`
- Proxy mode sets:
  - `model_info: mode: rerank`
- The endpoint shown is:
  - `/rerank`

### Assessment
This is a **reference/tutorial** page with **high density** and mostly practical integration details. Its durability is **medium** because it is tied to LiteLLM and Fireworks model names, endpoints, and config patterns that can change, though the general integration approach is stable. The content is a **mixed** primary-source doc: mostly instructional/reference material from LiteLLM, not commentary. It is best used as a **refer-back** resource for wiring Fireworks into LiteLLM, especially if you need exact model strings, endpoint paths, proxy configuration, or special behaviors like document inlining and rerank. Scrape quality is **good** overall, with many code examples and sections captured, though formatting is flattened and some code indentation/layout from the original doc is lost.
