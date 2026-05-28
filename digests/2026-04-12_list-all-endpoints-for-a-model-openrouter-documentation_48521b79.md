---
url: https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints#response.200.data.architecture.input_modalities
title: List all endpoints for a model | OpenRouter | Documentation
scraped_at: '2026-04-12T07:27:06Z'
word_count: 1567
raw_file: raw/2026-04-12_list-all-endpoints-for-a-model-openrouter-documentation_48521b79.txt
tldr: OpenRouter’s `list-endpoints` API returns a `data` wrapper containing model metadata plus a list of available endpoints for a specific model, including architecture, pricing, latency, uptime, and supported parameters.
key_quote: “GET https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints”
durability: medium
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries: []
companies:
- OpenRouter
tags:
- api-reference
- openapi
- endpoint-metadata
- model-hosting
- bearer-authentication
---

### TL;DR
OpenRouter’s `list-endpoints` API returns a `data` wrapper containing model metadata plus a list of available endpoints for a specific model, including architecture, pricing, latency, uptime, and supported parameters.

### Key Quote
“GET https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints”

### Summary
- **What this endpoint does**
  - Fetches the available endpoints for a specific model identified by `{author}` and `{slug}`.
  - The documented route is: `GET https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints`
  - The operationId is `list-endpoints`.

- **Authentication**
  - Requires an `Authorization` header with a bearer token.
  - The docs explicitly say: API key as bearer token in `Authorization` header.

- **Successful response shape**
  - The `200` response returns JSON with a single top-level `data` field.
  - `data` is a `ListEndpointsResponse` object containing:
    - `id`: unique identifier for the model
    - `name`: display name
    - `description`: model description
    - `created`: Unix timestamp for model creation
    - `architecture`: architecture details
    - `endpoints`: array of endpoint objects

- **Architecture object**
  - `architecture.input_modalities`: supported input types
    - enum: `text`, `image`, `file`, `audio`, `video`
  - `architecture.output_modalities`: supported output types
    - enum: `text`, `image`, `embeddings`, `audio`, `video`, `rerank`
  - `architecture.instruct_type`: instruction format type
    - values include `none`, `chatml`, `claude`, `llama3`, `mistral`, `deepseek-r1`, `deepseek-v3.1`, `qwen3`, and others
  - `architecture.modality`: primary modality, can be a string or null
  - `architecture.tokenizer`: present, but the schema is an empty object placeholder in this spec

- **Endpoint objects in `endpoints[]`**
  - Each `PublicEndpoint` includes:
    - `model_id`, `model_name`, `name`, `tag`
    - `provider_name`
    - `context_length`
    - `max_prompt_tokens`
    - `max_completion_tokens`
    - `status`
    - `quantization`
    - `supported_parameters`
    - `supports_implicit_caching`
    - `pricing`
    - `latency_last_30m`
    - `throughput_last_30m`
    - `uptime_last_1d`, `uptime_last_30m`, `uptime_last_5m`

- **Notable endpoint telemetry fields**
  - `latency_last_30m` is percentile latency over the last 30 minutes, measured as time to first token.
    - Includes `p50`, `p75`, `p90`, `p99`
    - Only visible when authenticated; unauthenticated requests get `null`
  - `throughput_last_30m` also includes `p50`, `p75`, `p90`, `p99`
  - Uptime fields are percentages over different windows:
    - last 1 day
    - last 30 minutes
    - last 5 minutes
  - Uptime excludes rate-limited requests in the calculation for the documented fields with descriptions.

- **Pricing structure**
  - `pricing` is a structured object with fields such as:
    - `prompt`
    - `completion`
    - `discount`
    - `request`
    - `image`, `image_output`, `image_token`
    - `audio`, `audio_output`
    - `input_cache_read`, `input_cache_write`
    - `input_audio_cache`
    - `internal_reasoning`
    - `web_search`
  - `prompt` and `completion` are required.

- **Supported parameters**
  - `supported_parameters` is an array of parameter names such as:
    - `temperature`, `top_p`, `top_k`, `min_p`, `top_a`
    - penalties like `frequency_penalty`, `presence_penalty`, `repetition_penalty`
    - generation controls like `max_tokens`, `stop`, `seed`
    - structured/tooling options like `response_format`, `structured_outputs`, `tools`, `tool_choice`, `parallel_tool_calls`
    - reasoning/search controls like `include_reasoning`, `reasoning`, `reasoning_effort`, `web_search_options`, `verbosity`

- **Provider and model enums**
  - `provider_name` is restricted to a long enum of providers, including:
    - `OpenAI`, `Anthropic`, `Google`, `Groq`, `Mistral`, `Cohere`, `xAI`, `DeepSeek`, `Amazon Bedrock`, `Cloudflare`, and many others
  - `status` is an enum of string codes:
    - `0`, `-1`, `-2`, `-3`, `-5`, `-10`

- **Error responses**
  - `404 Not Found`:
    - returns `NotFoundResponse`
    - includes `error` with `code`, `message`, and optional `metadata`
    - may also include `user_id`
  - `500 Internal Server Error`:
    - same overall structure via `InternalServerResponse`

- **Code samples**
  - The page includes SDK-style examples in:
    - Python (`requests`)
    - JavaScript (`fetch`)
    - Go
    - Ruby
    - Java (`Unirest`)
    - PHP (`Guzzle`)
    - C#
    - Swift
  - All examples use the same pattern:
    - `GET https://openrouter.ai/api/v1/models/openai/gpt-4/endpoints`
    - `Authorization: Bearer <token>`

### Assessment
This is a **reference** page with **high density** because it is mostly raw OpenAPI schema rather than explanatory prose. **Durability is medium**: the endpoint pattern and schema concepts are stable, but the exact enum values, pricing fields, and supported parameters are version-sensitive and may change as the API evolves. **Content type is reference/mixed** because it combines specification, response schema, and code examples. **Originality is primary source** since it appears to be direct documentation/OpenAPI output from OpenRouter. It is best used **refer-back** for implementation details and field names rather than deep study of narrative explanation. **Scrape quality is good**, capturing the endpoint definition, schemas, and multi-language examples, though the page is still schema-heavy and may omit any richer prose context beyond the OpenAPI output.
