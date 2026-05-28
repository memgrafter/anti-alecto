---
url: https://openrouter.ai/docs/guides/guides/usage-accounting#usage-information
title: Usage Accounting | Track AI Model Usage with OpenRouter | OpenRouter | Documentation
scraped_at: '2026-04-12T07:43:17Z'
word_count: 629
raw_file: raw/2026-04-12_usage-accounting-track-ai-model-usage-with-openrouter-openrouter-documentation_1fcaad21.txt
---

### TL;DR
OpenRouter now includes full usage accounting automatically in every API response, showing token counts, cached tokens, and cost details without extra parameters or calls.

### Key Quote
"Usage is always included automatically in every response."

### Summary
- OpenRouter’s API has **built-in Usage Accounting** so you can track model usage directly from responses.
- Included usage data:
  - **Prompt tokens** and **completion tokens** using the model’s native tokenizer
  - **Reasoning tokens** when applicable
  - **Cached tokens** when available
  - **Cost in credits**
- For **streaming responses**, usage appears in the **last SSE message / final chunk**.
- For **non-streaming responses**, usage is included in the **complete response**.
- No extra parameters are needed anymore.
- Two deprecated options are called out as no-ops:
  - `usage: { include: true }`
  - `stream_options: { include_usage: true }`
- Example response format includes:
  - `usage.completion_tokens`
  - `usage.completion_tokens_details.reasoning_tokens`
  - `usage.cost`
  - `usage.cost_details.upstream_inference_cost`
  - `usage.prompt_tokens`
  - `usage.prompt_tokens_details.cached_tokens`
  - `usage.prompt_tokens_details.cache_write_tokens`
  - `usage.total_tokens`
- Clarifications on fields:
  - `cached_tokens` = tokens read from cache
  - `cache_write_tokens` = tokens written to cache, only for models with explicit caching and cache-write pricing
  - `upstream_inference_cost` applies only to **BYOK (Bring Your Own Key)** requests
- Benefits emphasized:
  - No separate usage API call needed
  - Native-tokenizer accuracy
  - Real-time visibility into cost and cache usage
  - Detailed breakdown across prompt, completion, reasoning, and cache
- Best practices recommended:
  - Monitor token consumption and costs using usage data
  - Use it during development to optimize before production
  - Use cached token info to improve performance
- Alternative method:
  - Retrieve usage asynchronously using the **generation ID**
  - Workflow: make request normally → note `id` → query `/generation`
  - Suggested for post-completion retrieval or historical auditing
- Examples shown:
  - **TypeScript SDK** example using `openRouter.chat.send(...)` and reading `response.usage`
  - **Streaming example** using the OpenAI SDK against `https://openrouter.ai/api/v1`, printing content chunks and then usage from the final chunk

### Assessment
This is a **reference/tutorial** page with **high durability** for the core concept, since it documents an API behavior rather than a time-sensitive event, though specific field names and deprecated parameters could still change with future API versions. The content is mostly **fact** with some **tutorial** guidance and example code, and it is **high-density** because it includes concrete schema fields, deprecations, and usage patterns. It appears to be **primary source** documentation from OpenRouter, so it is the right place to verify current behavior. This is best used as a **refer-back** resource when implementing or checking usage tracking, not just a skim-once article. Scrape quality is **good**: the key sections, response schema, notes, and code examples are present, though formatting is flattened and some code block styling/context may be missing.
