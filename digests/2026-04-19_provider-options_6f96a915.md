---
url: https://vercel.com/docs/ai-gateway/provider-options#reasoning
title: Provider Options
scraped_at: '2026-04-19T03:57:41Z'
word_count: 823
raw_file: raw/2026-04-19_provider-options_6f96a915.txt
tldr: Vercel’s AI Gateway `providerOptions` let you control provider routing, ordering, fallback, caching, BYOK credentials, and reasoning settings for supported models, with provider availability varying by model.
key_quote: By default, Vercel AI Gateway dynamically chooses the default providers to give you the best experience based on a combination of recent uptime and latency.
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
- Vercel
tags:
- ai-gateway
- provider-options
- model-routing
- caching
- reasoning
---

### TL;DR
Vercel’s AI Gateway `providerOptions` let you control provider routing, ordering, fallback, caching, BYOK credentials, and reasoning settings for supported models, with provider availability varying by model.

### Key Quote
“By default, Vercel AI Gateway dynamically chooses the default providers to give you the best experience based on a combination of recent uptime and latency.”

### Summary
- **What this page is about**
  - Documentation for **AI Gateway Provider Options** in Vercel.
  - Explains how to customize **routing behavior** across AI providers rather than model-specific behavior.

- **Default behavior**
  - AI Gateway normally picks providers automatically.
  - Selection is based on **recent uptime** and **latency**.

- **Routing controls in `providerOptions.gateway`**
  - `order`: set the order providers should be tried.
  - `only`: restrict requests to specific providers.
  - `sort`: rank providers by a **performance or cost metric** so the gateway tries them in that order.
  - More details are in the linked doc on **Provider Filtering, Ordering & Sorting**.

- **Automatic caching**
  - `caching: 'auto'` lets AI Gateway choose the appropriate caching strategy automatically.
  - Mentioned as useful for providers like **Anthropic** and **MiniMax** that require explicit cache markers.
  - See linked **Automatic Caching** docs for provider support and examples.

- **Timeouts and failover**
  - You can set **per-provider timeouts** to trigger faster failover if a provider is slow.
  - Separate docs exist for **Provider Timeouts**.
  - For model-level backup behavior, use **Model Fallbacks**.

- **Combining gateway options with provider-specific options**
  - You can mix gateway routing controls with **provider-specific settings** in the same request.
  - Example mentioned:
    - Using an **Anthropic model** such as **Claude 4 Sonnet** through **Vertex AI**
    - Anthropic-specific options still apply, including `thinkingBudget`
  - AI SDK docs are the reference for provider-specific options.

- **BYOK per request**
  - `byok` in `providerOptions.gateway` lets you supply your own provider credentials on a **per-request basis**.
  - Useful when you want to use existing provider accounts without setting credentials in the dashboard.
  - The BYOK docs cover credential structures, multiple credentials, and Chat Completions API usage.

- **Reasoning / “thinking” configuration**
  - For models that support reasoning, `providerOptions` can configure reasoning behavior.
  - The page specifically calls out **OpenAI `gpt-oss-120b`** as an example.
  - Relevant reasoning docs are linked for:
    - **OpenAI**
    - **DeepSeek**
    - **Anthropic**
  - Important note:
    - For **`openai/gpt-5`** and **`openai/gpt-5.4`**, both `reasoningEffort` and `reasoningSummary` must be set to receive reasoning output.

- **Model/provider catalog**
  - The page points users to the **Model List** in the Vercel dashboard or the public models page.
  - It includes a long table of provider slugs, names, and websites.
  - Providers listed include, among others:
    - `anthropic`, `openai`, `google`, `vertex`, `mistral`, `deepseek`, `groq`, `azure`, `bedrock`, `fireworks`, `togetherai`, `xai`, `nebius`, `perplexity`, `cohere`, `sambanova`, `voyage`, `zai`, and others.

- **Caveat**
  - **Provider availability may vary by model**.
  - Some models are only available through certain providers, or their capabilities may differ depending on the provider.

### Assessment
This is a **reference/documentation** page with **medium durability**: the core concepts of routing, fallback, caching, and reasoning are fairly durable, but the exact provider list and model-specific notes can change over time. The content is mostly **fact/reference** with some implementation guidance, and it is **high density** because it packs several related features and links into a compact page. It appears to be **primary source** documentation from Vercel rather than commentary or synthesis. Best used as a **refer-back** resource when configuring AI Gateway requests or checking supported provider options. Scrape quality is **good**: the text, key notes, and provider table are captured, though any code examples or richer formatting referenced in the original page are not included here.
