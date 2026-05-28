---
url: https://inference-docs.cerebras.ai/resources/glm-47-migration?_hsenc=p2ANqtz-_TZ4gF3Cn8iEOcyZOTbLUa7GAjqtyFvXpLJbgyAzRt9NgZ5D7jm9wXNcoBQ9n0S_YBQghzO7Bgkjx1UqXGkgl5psl4JQ&_hsmi=20905077
title: Migrate to GLM 4.7 - Cerebras Inference
scraped_at: '2026-04-19T03:58:28Z'
word_count: 2054
raw_file: raw/2026-04-19_migrate-to-glm-4-7-cerebras-inference_3d1a6a21.txt
tldr: Cerebras’ migration guide for GLM 4.7 explains the new model ID, limits, reasoning controls, streaming behavior, and prompt best practices for developers updating API calls from earlier GLM versions.
key_quote: “GLM 4.7 is a foundation model from Zhipu AI (Z.ai) built for coding and agentic workflows.”
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: partial
people:
- Jan Feddersen
- Sewer56
- Zhipu AI
- Z.ai
tools:
- Cerebras Python SDK
- OpenAI SDK
libraries:
- openai
companies:
- Cerebras
- Anthropic
- OpenAI
- Gemini
- Artificial Analysis
tags:
- llm-migration
- api-usage
- prompt-engineering
- reasoning-controls
- streaming
---

### TL;DR
Cerebras’ migration guide for **GLM 4.7** explains the new model ID, limits, reasoning controls, streaming behavior, and prompt best practices for developers updating API calls from earlier GLM versions.

### Key Quote
“GLM 4.7 is a foundation model from Zhipu AI (Z.ai) built for coding and agentic workflows.”

### Summary
- **What this page is**
  - A developer migration guide for moving API usage to **`zai-glm-4.7`** on Cerebras Inference.
  - Covers model info, benchmark claims, parameter changes, reasoning controls, streaming, prompt strategy, and Q&A on preserved thinking.

- **Model overview**
  - Based on the GLM-4.x foundation with a **Mixture-of-Experts (MoE) Transformer** architecture.
  - Claims **358.0B total parameters** with about **32B active per forward pass**.
  - Described as open source under an **MIT-style permissive license**.
  - Cerebras states inputs/outputs are processed **in memory and never persisted** when using GLM 4.7 on Cerebras Inference.
  - Key published limits:
    - **Cerebras Model ID:** `zai-glm-4.7`
    - **Context:** `131k` / **131,072 tokens**
    - **Max output:** `40k` via `max_completion_tokens`

- **Benchmark / performance claims**
  - The guide says GLM 4.6 was already strong for code generation and that **GLM 4.7 improves further** on **GPQA** and **AIME**, claiming it outperforms **Claude Sonnet 4.5** on both.
  - It also says GLM 4.7 outperforms Anthropic and OpenAI models on **LiveCodeBench**, trailing only **Gemini 3**.
  - It claims improvements in **chat, creative writing, and role-play**.
  - Important caveat: these benchmark sections depend heavily on **embedded chart images** and external references, which are **not readable in the scraped text here**, so the underlying visual evidence is incomplete in this capture.
  - Later in the page, a table summarizes third-party eval positions as of **Dec 30, 2025**:
    - **AA Agentic Index:** 3rd (tie), 1st among open models, score **63**
    - **AA Intelligence Index:** 6th overall, 1st among open models, score **68**
    - **AA Coding Index:** 7th overall, 1st among open models, score **55**

- **Migration checklist**
  - Set `model="zai-glm-4.7"`.
  - Keep defaults unless you have a reason:
    - `temperature=1`
    - `top_p=0.95`
  - For deterministic behavior, adjust **either** `temperature` **or** `top_p`, **not both**.
  - Reasoning defaults and controls:
    - Reasoning is **enabled by default**
    - Disable with `reasoning_effort="none"`
    - `disable_reasoning` is noted as **deprecated as of March 24, 2026**
    - Preserve reasoning traces with `clear_thinking: false`
  - Limits:
    - `max_completion_tokens` up to **40k**
    - Context window around **131k tokens**
  - The page recommends testing real workloads for:
    - randomness
    - latency
    - tool-call parsing
    - long-context behavior

- **API examples**
  - Shows usage with the **Cerebras Python SDK** and the **OpenAI SDK**.
  - Cerebras SDK example: `client.chat.completions.create(model="zai-glm-4.7", ...)`
  - OpenAI SDK example uses:
    - `base_url="https://api.cerebras.ai/v1"`
    - `extra_body={"clear_thinking": False}` for GLM-specific parameters
    - `reasoning_effort="none"` as a standard OpenAI parameter
  - Streaming example notes:
    - Use `stream=True`
    - Reasoning traces may appear in **`delta.reasoning`**
    - Tool calling with streaming may require concatenating partial `delta.tool_calls[*].function.arguments`

- **Migration best practices**
  - The guide argues old prompts should not be copied unchanged.
  - Main recommendations:
    - **Front-load instructions**: place constraints and behavioral rules at the start of the system prompt.
    - **Use explicit language**: prefer **MUST / REQUIRED / STRICTLY** over soft phrasing.
    - **Specify a default language**: e.g. “Always respond in English.”
    - **Use roles intentionally**: clear personas improve consistency.
    - **Use critic agents**: separate code review, QA, security, and performance checks.
    - **Break tasks into steps**: dependencies → structure → code → verification.
    - **Minimize reasoning when not needed**: disable it for simple tasks to reduce latency.
    - **Enable deeper reasoning for complex tasks** when needed.
    - **Hybrid routing**: use GLM 4.7 for simpler tasks and frontier models for harder ones.
    - **Tune sampling**:
      - `temperature`: 1.0 general / 0.8 instruction-following
      - `top_p`: 0.95
      - The page warns that **very low temperature with thinking enabled can degrade quality**

- **Q&A highlights**
  - **`reasoning_effort="none"`** disables reasoning.
  - **`clear_thinking`** controls whether reasoning context is preserved across turns:
    - `true` = default, exclude earlier thinking
    - `false` = preserve thinking, recommended for coding/agentic workflows and cache hit rate
  - The page frames **interleaved thinking** as introduced in **GLM-4.5**, supported in **GLM-4.6**, and enhanced in **GLM-4.7**.
  - GLM 4.7 adds:
    - **Preserved Thinking**
    - **Turn-level Thinking**
  - The model is presented as strong on development tasks and often faster than frontier models, though the guide notes the strongest reasoning-heavy code tasks may still favor frontier models.

- **Credits / next steps**
  - Credits community Discord contributors, including **Autoshot (Jan Feddersen)** and **Sewer56**.
  - Links to:
    - model overview
    - API key signup
    - Discord community

### Assessment
This is a **mixed reference/tutorial** page with **medium durability**: the prompting principles and reasoning/streaming concepts will age slowly, but the exact model behavior, benchmark rankings, parameter defaults, and deprecation note for `disable_reasoning` are tied to a specific model version and will become stale as Cerebras and Z.ai iterate. The **content type** is primarily **tutorial + reference** with some benchmark-heavy factual claims. **Density is high** because it combines migration steps, SDK examples, prompt guidance, and eval summaries in one page. **Originality** is mostly **synthesis/commentary**: it is a vendor-authored migration guide that combines Cerebras guidance with third-party benchmark references and Z.ai model claims, rather than an independent analysis. For **reference style**, this is best as a **refer-back** resource when implementing or troubleshooting GLM 4.7 integration, though it also supports a quick skim if you just need the model ID and key parameters. **Scrape quality is partial**: the text content is largely captured, but the benchmark charts are embedded as images and are not readable here, so the performance section should be treated cautiously and the visual evidence is incomplete.
