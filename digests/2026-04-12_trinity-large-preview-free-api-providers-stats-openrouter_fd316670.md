---
url: https://openrouter.ai/arcee-ai/trinity-large-preview:free
title: Trinity Large Preview (free) - API, Providers, Stats | OpenRouter
scraped_at: '2026-04-12T10:38:32Z'
word_count: 129
raw_file: raw/2026-04-12_trinity-large-preview-free-api-providers-stats-openrouter_fd316670.txt
tldr: OpenRouter’s page for Arcee AI Trinity Large Preview (free) says it is a reasoning-enabled model released Jan 27, 2026, with 131,000 context, and $0/M input/output tokens, and points developers to OpenRouter’s request, parameters, reasoning, and framework docs.
key_quote: “Use the reasoning parameter in your request to enable reasoning, and access the reasoning_details array in the response to see the model's internal reasoning before the final answer.”
durability: low
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Arcee AI
tools:
- OpenRouter
libraries: []
companies:
- OpenRouter
- Arcee AI
tags:
- large-language-models
- model-metadata
- reasoning
- api-documentation
- openrouter
---

### TL;DR
OpenRouter’s page for **Arcee AI Trinity Large Preview (free)** says it is a **reasoning-enabled model** released **Jan 27, 2026**, with **131,000 context**, and **$0/M input/output tokens**, and points developers to OpenRouter’s request, parameters, reasoning, and framework docs.

### Key Quote
“Use the reasoning parameter in your request to enable reasoning, and access the reasoning_details array in the response to see the model's internal reasoning before the final answer.”

### Summary
- **Model/page:** `Trinity Large Preview (free)` on OpenRouter, by **arcee-ai**
- **Release date:** **Jan 27, 2026**
- **Context window:** **131,000**
- **Pricing:** **$0/M input tokens** and **$0/M output tokens**
- **Capability highlighted:** OpenRouter says it supports **reasoning-enabled models** that can expose step-by-step thinking via:
  - the **`reasoning`** parameter in the request
  - the **`reasoning_details`** array in the response
- **Conversation handling:** When continuing a conversation, you should **preserve the complete `reasoning_details`** when sending messages back so the model can continue reasoning from where it left off.
- **Docs pointers included:**
  - **Learn more about reasoning tokens**
  - **Request docs** for all possible fields
  - **Parameters** docs for sampling parameter explanations
  - **Frameworks documentation** for third-party SDKs/framework integrations
- **Headers note:** OpenRouter-specific headers are **optional** in the examples; enabling them lets your app appear on **OpenRouter leaderboards**

### Assessment
This is a **reference/announcement** page for a specific model listing on OpenRouter. Its **durability is low to medium** because it includes a release date, pricing, and platform-specific API guidance that may change over time, though the reasoning-model usage pattern may remain relevant. The content is **mixed**, combining model metadata with brief integration guidance. It is **high-density** in the sense that it packs several concrete details into a short snippet, but it is not a deep tutorial. The page appears to be **primary source** content from OpenRouter rather than commentary or synthesis. Best used as a **refer-back** reference if you need the model’s specs or the reasoning API notes. **Scrape quality is partial**, since only a short excerpt is available and the full page sections, examples, and any provider/stat details are not included.
