---
url: https://github.com/boldsoftware/shelley/pull/177/changes
title: 'Retry automatically when LLM returns only thinking blocks by okottorika · Pull Request #177 · boldsoftware/shelley'
scraped_at: '2026-04-19T07:21:07Z'
word_count: 1290
raw_file: raw/2026-04-19_retry-automatically-when-llm-returns-only-thinking-blocks-by-okottorika-pull-req_eecd42d5.txt
tldr: This pull request adds a safeguard in Shelley’s conversation loop to automatically retry Claude responses that contain only thinking/redacted-thinking blocks, so users don’t see blank assistant turns.
key_quote: Claude sometimes returns only thinking blocks with no output. Retry.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Honjo Masamune
- siddhantmanekar71
- okottorika
- Qwen-Coder
tools: []
libraries: []
companies:
- boldsoftware
tags:
- llm-retries
- claude
- go-testing
- conversation-loop
- error-handling
---

### TL;DR
This pull request adds a safeguard in Shelley’s conversation loop to automatically retry Claude responses that contain only thinking/redacted-thinking blocks, so users don’t see blank assistant turns.

### Key Quote
"Claude sometimes returns only thinking blocks with no output. Retry."

### Summary
- **What changed**
  - In `loop/loop.go`, `processLLMRequest` now tracks `emptyResponseRetries` and checks every LLM response with a new helper, `respHasNoVisibleContent(resp)`.
  - If the response contains content but **no visible output** — meaning no `text` and no `tool_use` blocks, only `thinking` or `redacted_thinking` — the loop:
    - logs a warning,
    - retries the LLM request,
    - and does **not** save the empty response to history/database.
  - After **3 retries**, it gives up and returns an error: `"LLM returned only thinking blocks after 3 retries"`.

- **Behavioral intent**
  - Fixes a rare but confusing UI issue where the assistant would appear to send a blank turn.
  - This is specifically described as happening with **Claude models**.
  - The patch is linked to **Fixes #131**.

- **New helper**
  - `respHasNoVisibleContent(resp *llm.Response) bool`
    - Returns `false` for empty content.
    - Returns `true` for responses that contain content but only `thinking` / `redacted_thinking`.
    - Returns `false` if any `text` or `tool_use` block is present.

- **Tests added in `loop/loop_test.go`**
  - `TestRetryOnThinkingOnlyResponse`
    - Uses a mock `thinkingOnlyService` that returns a thinking-only response on the first call, then a normal text response.
    - Verifies:
      - the loop retries automatically,
      - only the successful assistant response is recorded,
      - the service is called twice.
  - `TestRespHasNoVisibleContent`
    - Covers cases like:
      - empty content → `false`
      - only thinking → `true`
      - only redacted thinking → `true`
      - text present → `false`
      - tool use present → `false`
  - `TestThinkingOnlyResponseRetryLimit`
    - Uses an `alwaysThinkingService` that never produces visible output.
    - Verifies:
      - the loop stops after 3 retries,
      - an error is returned,
      - no messages are recorded,
      - total calls are 4 (initial call + 3 retries).

- **Implementation details**
  - The retry logic lives inside the LLM request loop rather than in outer conversation management.
  - The patch emphasizes that the “empty response is not recorded to the database, so the user never sees it.”

### Assessment
This is a **mixed** content type, mostly a **code patch with tests** and a small amount of explanatory commentary. Durability is **medium**: the underlying idea of retrying malformed/empty model outputs is fairly durable, but the specifics are tied to Claude behavior and the Shelley codebase, so it may age with model API changes. Density is **high** because the diff includes concrete control flow, helper logic, and three focused tests. Originality is **primary source** since this is the actual pull request patch rather than a summary of it. Reference style is **refer-back** if you need to understand or modify the retry logic in `loop/loop.go`, especially the empty-response detection and retry limit. Scrape quality is **good**: the patch, helper function, and tests are present, with no obvious missing code blocks or sections in the provided content.
