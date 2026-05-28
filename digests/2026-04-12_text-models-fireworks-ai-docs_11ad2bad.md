---
url: https://docs.fireworks.ai/guides/querying-text-models#chat-completions-api
title: Text Models - Fireworks AI Docs
scraped_at: '2026-04-12T07:38:32Z'
word_count: 786
raw_file: raw/2026-04-12_text-models-fireworks-ai-docs_11ad2bad.txt
tldr: Fireworks AI’s text-model docs explain how to query serverless and dedicated deployments, use chat/completions/responses APIs, and tune generation with sampling, usage tracking, and advanced features like tool calling and structured outputs.
key_quote: Fireworks provides an OpenAI-compatible API, making migration from OpenAI straightforward.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- Fireworks SDK
- OpenAI SDK
- curl
libraries: []
companies:
- Fireworks AI
tags:
- large-language-models
- api-reference
- prompt-engineering
- text-generation
- openai-compatibility
---

### TL;DR
Fireworks AI’s text-model docs explain how to query serverless and dedicated deployments, use chat/completions/responses APIs, and tune generation with sampling, usage tracking, and advanced features like tool calling and structured outputs.

### Key Quote
“Fireworks provides an OpenAI-compatible API, making migration from OpenAI straightforward.”

### Summary
- This page is a **reference hub** for querying Fireworks text models, with links to:
  - **Serverless Quickstart** for first API calls
  - **Chat Completions API** examples in Python (Fireworks SDK), Python (OpenAI SDK), JavaScript, and curl
  - **Alternative query methods**: Completions API and Responses API
  - **Dedicated deployments** for consistent performance, guaranteed capacity, or higher throughput

- It outlines **common usage patterns**:
  - **Multi-turn conversations**: include all previous messages in history
  - **System prompts**: set the first message with `role: "system"` and empty `content` to override the default system prompt
  - **Streaming responses**: supported for real-time UX, with details referenced in the Serverless Quickstart
  - **Async requests**: use async clients for concurrent requests and better throughput

- It explains **usage and performance tracking**:
  - Every response includes **token usage**: prompt, completion, total tokens
  - **Performance metrics** like latency and time-to-first-token appear in headers for non-streaming requests
  - For streaming, you can set `perf_metrics_in_response` to include metrics in the response body
  - Usage is included in the **final streaming chunk** when `finish_reason` is set
  - This is noted as a **Fireworks extension**, since the OpenAI SDK does not return streaming usage by default

- It lists **advanced capabilities** for text models:
  - **Tool calling** with type-safe parameters
  - **Structured outputs** for JSON schema enforcement
  - **Responses API** for multi-step reasoning
  - **Predicted outputs** to speed up edits
  - **Prompt caching** to reduce latency and cost
  - **Batch inference** for large asynchronous workloads

- It provides a detailed **sampling and generation configuration** section:
  - Fireworks uses recommended defaults from each model’s HuggingFace `generation_config.json` when parameters are not explicitly set
  - It automatically pulls defaults for:
    - `temperature`
    - `top_k`
    - `top_p`
    - `min_p`
    - `typical_p`
  - Key generation controls include:
    - **Temperature**: randomness/creativity
    - **Max tokens**: defaults to 2048 if unspecified; some models support up to full context windows such as **128K for DeepSeek R1**
    - If the limit is reached, response may end with `"finish_reason": "length"`
    - **Top-p**, **top-k**, **min-p**, **typical-p** sampling options
    - **Repetition penalties**: `frequency_penalty`, `presence_penalty`, `repetition_penalty`
    - **Multiple generations**
    - **Token probabilities (logprobs)** for analysis/debugging
    - **Prompt inspection** via `echo` and `raw_output`
    - **Ignore EOS token** for benchmarking, with a warning that quality may degrade and it is experimental
    - **Logit bias** to encourage/discourage tokens
    - **Mirostat sampling** for dynamic perplexity control

- It clarifies **tokens**:
  - Text is processed in chunks called tokens
  - In English, a token can be as small as one character or as large as one word
  - Tokenization differs by model family
  - Tokens matter because:
    - context length is measured in tokens
    - pricing is based on token usage
    - response time depends on token count
    - token usage appears in the `usage` field of API responses

- It includes an **OpenAI SDK migration** note:
  - Fireworks is OpenAI-compatible
  - Users migrating from OpenAI should consult the OpenAI compatibility guide

- It ends with **next steps** linking to related docs:
  - Vision models
  - Audio models
  - Embeddings
  - On-demand deployments
  - Fine-tuning
  - Error codes
  - API Reference

### Assessment
This is a **reference** document with high practical density: it condenses many API features, parameter controls, and usage patterns into a single guide. Its **durability is medium-high** because the core concepts of chat/completions, sampling, tokens, and usage tracking are stable, but some specifics may change with SDKs, defaults, or model versions. The content is a **mixed** type leaning toward reference/tutorial, and it reads like **primary documentation** rather than commentary or synthesis. It’s best used as a **refer-back** resource when implementing or tuning Fireworks text model calls. **Scrape quality is partial**: the page structure and major sections are captured, but some formatting, code examples, and section details appear compressed or missing, so the full docs page would still be worth opening for implementation work.
