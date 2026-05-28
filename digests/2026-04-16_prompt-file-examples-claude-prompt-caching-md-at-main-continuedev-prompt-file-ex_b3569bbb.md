---
url: https://github.com/continuedev/prompt-file-examples/blob/main/claude-prompt-caching.md?ref=blog.continue.dev
title: prompt-file-examples/claude-prompt-caching.md at main · continuedev/prompt-file-examples
scraped_at: '2026-04-16T03:58:29Z'
word_count: 1068
raw_file: raw/2026-04-16_prompt-file-examples-claude-prompt-caching-md-at-main-continuedev-prompt-file-ex_b3569bbb.txt
tldr: A GitHub prompt-file example that embeds Anthropic’s prompt caching announcement and docs excerpt, but the captured page is contaminated by a synthetic “Completion” section with fabricated API usage that is not part of the source.
key_quote: “Prompt caching, which enables developers to cache frequently used context between API calls, is now available on the Anthropic API.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Simon Last
tools:
- Anthropic API
libraries: []
companies:
- Anthropic
- Notion
tags:
- prompt-caching
- api-pricing
- ai-assistants
- developer-tools
- anthropic
---

### TL;DR
A GitHub prompt-file example that embeds Anthropic’s prompt caching announcement and docs excerpt, but the captured page is contaminated by a synthetic “Completion” section with fabricated API usage that is not part of the source.

### Key Quote
“Prompt caching, which enables developers to cache frequently used context between API calls, is now available on the Anthropic API.”

### Summary
- **What this page is**
  - A `prompt-file-examples/claude-prompt-caching.md` file in the `continuedev/prompt-file-examples` GitHub repo.
  - It is structured as a prompt file with frontmatter:
    - `name: claude-prompt-caching`
    - `description: Talk to the Claude prompt caching docs`
  - The content under `<system>` is sourced from Anthropic’s prompt caching announcement/docs excerpt.

- **Main Anthropic announcement details**
  - Prompt caching lets developers cache frequently used context between API calls.
  - Claimed benefits:
    - **Up to 90% cost reduction**
    - **Up to 85% latency reduction** for long prompts
  - Public beta availability mentioned for:
    - Claude 3.5 Sonnet
    - Claude 3 Opus
    - Claude 3 Haiku

- **When prompt caching is useful**
  - Conversational agents with long instructions or uploaded documents
  - Coding assistants that keep summarized codebase context
  - Large document processing, including images
  - Detailed instruction sets with many examples
  - Agentic search / multi-step tool use
  - “Talk to” long-form content such as books, papers, docs, and podcast transcripts

- **Reported performance examples**
  - Chat with a book (100,000 token cached prompt): **11.5s → 2.4s** time to first token, **-90% cost**
  - Many-shot prompting (10,000 token prompt): **1.6s → 1.1s**, **-86% cost**
  - Multi-turn conversation (10-turn convo with long system prompt): **~10s → ~2.5s**, **-53% cost**

- **Pricing model described**
  - Cached prompt writes cost **25% more** than the base input token price.
  - Cached reads cost **10% of the base input token price**.
  - Example model pricing listed:
    - **Claude 3.5 Sonnet**: Input $3/MTok, Prompt caching $3.75/MTok, Output $15/MTok
    - **Claude 3 Opus**: Input $15/MTok, Prompt caching $18.75/MTok, Output $75/MTok
    - **Claude 3 Haiku**: Input $0.25/MTok, Prompt caching $0.30/MTok, Output $1.25/MTok

- **Customer spotlight**
  - Notion is highlighted as using prompt caching in Claude-powered Notion AI features.
  - Quote from Simon Last, co-founder at Notion:
    - “We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality.”

- **Important contamination / non-source content**
  - The provided scrape includes a synthetic “Completion” section answering “how do i cache a prompt.”
  - That section contains fabricated-looking API calls like `client.cache.write(...)` and `client.chat(...)` that are **not part of Anthropic’s announcement text**.
  - Treat that walkthrough as **wrapper contamination**, not authoritative source material.

### Assessment
This is a mixed-content reference with **medium durability**: the general concept of prompt caching is durable, but the availability, model list, pricing, and performance figures are version- and product-specific. The content type is best treated as **mixed**—mostly a reference/news announcement excerpt, but polluted by generated tutorial-like text. It is **high density** in the Anthropic excerpt itself because it packs benefits, use cases, benchmarks, pricing, and a customer quote into a short page. The originality is **mixed** as well: the Anthropic material is primary-source announcement content, while the appended “Completion” is synthetic wrapper output. For future use, this is a **refer-back** card if you want the official prompt caching claims, pricing, and use cases; it is not a deep-study piece. Scrape quality is **partial**: the source excerpt is captured, but the page is clearly contaminated by non-authoritative generated text, which lowers trustworthiness and makes the page unsafe to use for implementation details without checking the official Anthropic docs.
