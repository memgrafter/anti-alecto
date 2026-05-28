---
url: https://inference-docs.cerebras.ai/capabilities/predicted-outputs
title: Predicted Outputs - Cerebras Inference
scraped_at: '2026-04-19T03:58:39Z'
word_count: 1324
raw_file: raw/2026-04-19_predicted-outputs-cerebras-inference_75038357.txt
tldr: Cerebras’ Predicted Outputs preview feature lets you speed up chat completions by supplying expected text so the model can reuse matching tokens, with best results for near-known edits like code refactors, document tweaks, and template fills.
key_quote: Reduce latency by specifying parts of the response that are already known.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Cerebras Inference
- Cerebras SDK
libraries: []
companies:
- Cerebras
tags:
- api-documentation
- latency-optimization
- token-reuse
- llm-inference
- preview-feature
---

### TL;DR
Cerebras’ **Predicted Outputs** preview feature lets you speed up chat completions by supplying expected text so the model can reuse matching tokens, with best results for near-known edits like code refactors, document tweaks, and template fills.

### Key Quote
“Reduce latency by specifying parts of the response that are already known.”

### Summary
- **What it is**
  - A **Public Preview** capability in Cerebras Inference called **Predicted Outputs**.
  - Intended to **reduce latency** by letting you provide a draft or expected output via the `prediction` request parameter.
  - The model reuses matching tokens and regenerates only differing parts.

- **Supported models**
  - `gpt-oss-120b`
  - `llama3.1-8b`
  - `zai-glm-4.7`
  - Note: the limitations section says supported models are currently `gpt-oss-120b` and `zai-glm-4.7`, which suggests the docs may be inconsistent or partially updated.

- **When to use it**
  - Best when **most of the output is already known** or can be precomputed.
  - Recommended use cases:
    - **Code refactoring**: tab/inline completion, full-file edits, structural transformations
    - **Document editing**: grammar fixes, tone adjustments
    - **Template filling**: predictable structured text with placeholders
  - It helps only when one or more **continuous token sequences** from the `prediction` field appear in the final response.
  - It provides **no benefit** when the output is highly unpredictable.

- **How to use it**
  - Import the Cerebras SDK and create a client with `CEREBRAS_API_KEY`.
  - Send a normal chat completion request plus a `prediction` object:
    - `prediction={"type": "content", "content": code}`
  - The example shows using the original CSS file as the prediction while asking the model to change text color from green to blue.
  - The doc notes that tokens in the prediction that are **not used** in the final completion are still billed at **completion-token rates**.

- **Metrics to watch**
  - The response usage object includes:
    - `completion_tokens`
    - `prompt_tokens`
    - `total_tokens`
    - `completion_tokens_details.accepted_prediction_tokens`
    - `completion_tokens_details.rejected_prediction_tokens`
  - High accepted / low rejected prediction tokens indicates effective reuse and better speed/cost efficiency.

- **Best practices**
  - Use it when **most of the output is known**.
  - Set `temperature=0` to reduce randomness and increase token acceptance.
  - Keep predictions as accurate as possible to avoid rejection.
  - Monitor accepted vs. rejected prediction tokens.
  - Fall back to a standard completion if rejection rates are high.
  - For reasoning models, reasoning tokens count as completion tokens and can slightly increase `rejected_prediction_tokens`.

- **Limitations**
  - Supported models are limited, and the page explicitly says:
    - `logprobs` is not supported
    - `n > 1` is not supported
    - `tools` / tool calling is not supported with Predicted Outputs
  - Rejected predicted tokens are billed at output-token rates.
  - Dedicated endpoint customers are said to be **not affected by this pricing**.
  - Cerebras says it does **not store prediction data**.

- **FAQ highlights**
  - **API costs increase?** Only when predicted tokens are not accepted.
  - **How to know if it worked?** Check `accepted_prediction_tokens` and `rejected_prediction_tokens`.
  - **If predicted text is wrong?** The model rejects mismatched tokens and regenerates them, reducing speed and increasing cost.
  - **Does Cerebras store prediction data?** No.

### Assessment
This is a **technical reference/docs** page with a practical tutorial component. Durability is **medium** because the general technique of prediction-based token reuse is fairly stable, but the exact supported models, preview status, and API constraints are version-sensitive and likely to change. Density is **medium-high**: it includes a concise explanation, a worked code example, metrics, best practices, limitations, and FAQ. Originality is a **primary source** from Cerebras documentation, so it’s useful for implementation and policy details, though you should verify current support because the page is marked **Public Preview** and the model list appears slightly inconsistent. Best used as a **refer-back** reference when implementing or debugging the feature. Scrape quality is **good** overall: the page content, example, metrics, limitations, and FAQ are present, though the capture also includes a lot of navigation, cookie-banner text, and UI chrome that isn’t part of the substantive documentation.
