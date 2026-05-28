---
url: https://medium.com/@mcraddock/unlocking-efficiency-a-practical-guide-to-claude-prompt-caching-3185805c0eef
title: 'Unlocking Efficiency: A Practical Guide to Claude Prompt Caching | by Mark Craddock | Medium'
scraped_at: '2026-04-19T03:59:08Z'
word_count: 1129
raw_file: raw/2026-04-19_unlocking-efficiency-a-practical-guide-to-claude-prompt-caching-by-mark-craddock_d64e1b12.txt
tldr: A practical Medium guide from Aug. 23, 2024 explaining how to use Anthropic’s Claude prompt caching to cut input-token costs and latency by caching reusable prompt prefixes for 5 minutes.
key_quote: Cache writes cost 25% more than base input tokens
durability: medium
content_type: tutorial
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Mark Craddock
tools:
- Anthropic console
- Claude
libraries:
- anthropic
companies:
- Anthropic
tags:
- prompt-caching
- anthropic
- llm-optimization
- api-pricing
- developer-tools
---

### TL;DR
A practical Medium guide from Aug. 23, 2024 explaining how to use Anthropic’s Claude prompt caching to cut input-token costs and latency by caching reusable prompt prefixes for 5 minutes.

### Key Quote
“Cache writes cost 25% more than base input tokens”

### Summary
- **What prompt caching is**
  - An Anthropic Claude optimization that reuses large, stable portions of prompts across multiple API calls.
  - Best for repeated context: system instructions, background info, examples, long documents, tool-use loops, and agentic workflows.

- **Claimed benefits**
  - Up to **90% reduction** in input token costs.
  - Up to **85% reduction** in latency for long prompts.
  - Lets developers include more context/examples without the usual performance penalty.

- **When it’s useful**
  - Long conversations with fixed instructions.
  - Coding assistants with summarized codebase context.
  - Large-doc processing, including images.
  - Detailed instruction sets with many examples.
  - Agentic search/tool use over multiple rounds.
  - Interactive long-form content like books, papers, or transcripts.

- **How to implement it**
  - Put static, reusable content at the **beginning** of the prompt.
  - Mark reusable sections with `cache_control`.
  - Minimum cacheable length:
    - **1024 tokens** for Claude 3.5 Sonnet and Claude 3 Opus
    - **2048 tokens** for Claude 3 Haiku
  - Example shown uses `client.beta.prompt_caching.messages.create(...)` with the model `claude-3-5-sonnet-20240620`.
  - The article says to enable it with the beta header:
    - `anthropic-beta: prompt-caching-2024-07-31`

- **Pricing and monitoring**
  - **Cache writes**: 25% more than base input tokens.
  - **Cache reads**: 90% less than base input tokens.
  - Response fields to inspect:
    - `cache_creation_input_tokens`
    - `cache_read_input_tokens`

- **Cost spreadsheet**
  - The author provides a linked spreadsheet for estimating savings across scenarios.
  - It models token usage, cache writes/reads, and up to **8 hours of continuous usage**.
  - Link is to a GitHub-hosted Excel file, marked **updated 28/08/2024**.

- **Console tracking**
  - In Anthropic console Usage, group by **token type** to view:
    - Beige: output tokens
    - Light orange: prompt caching read tokens
    - Orange: prompt caching write tokens
    - Red: input tokens

- **Best practices**
  - Cache stable content only.
  - Keep cached content at the start of prompts.
  - Use cache breakpoints strategically.
  - Watch hit rates and adjust.
  - Remember the cache TTL is about **5 minutes**, refreshed on use.

- **FAQ highlights**
  - Up to **4 cache breakpoints**.
  - Available only for **Claude 3.5 Sonnet, Claude 3 Haiku, and Claude 3 Opus**.
  - Works with tool use and vision, but changing images or `tool_choice.type` can break the cache.
  - No manual cache clearing; entries expire after inactivity.
  - Cache keys are based on a cryptographic hash of the prompt prefix and are **organization-specific**.
  - `anthropic-beta` can include multiple betas in a comma-separated list.

### Assessment
This is a **tutorial/mixed practical guide** with a strong reference component, published **2024-08-23**, so its durability is **medium**: the core idea of caching reusable prompt prefixes is likely durable, but the model names, headers, minimum token thresholds, pricing multipliers, and beta flags are version-specific and may age quickly. The content is fairly **dense** with concrete implementation details, token thresholds, pricing rules, and API fields, and it reads as **commentary/synthesis** rather than primary documentation. It’s best used as a **refer-back** piece for implementation and cost-checking rather than deep study. Scrape quality is **partial**: the text captures the main article content, but the referenced image/console screenshot and the embedded spreadsheet are not present in full, and the code block is shown in a plain-text form rather than as a fully formatted snippet.
