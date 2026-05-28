---
url: https://github.com/boldsoftware/shelley/pull/175
title: 'Add unit tests for custom model endpoint with Anthropic thinking blocks by okottorika · Pull Request #175 · boldsoftware/shelley'
scraped_at: '2026-04-19T07:21:36Z'
word_count: 1949
raw_file: raw/2026-04-19_add-unit-tests-for-custom-model-endpoint-with-anthropic-thinking-blocks-by-okott_aba9e381.txt
tldr: This PR fixes a racey distill-replace UI flow so users stay on the source conversation until the slug swap/archive completes, and adds mock-SSE unit tests for Anthropic custom-model test endpoints with thinking blocks.
key_quote: 'Now the UI: - Tracks active distill-replace operations (source ID -> new ID mapping) - Stays on the source conversation after initiating distill-replace - Waits for the SSE conversation list update showing the source was archived - Only then navigates to the new conversation (which now has the original slug)'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- okottorika
- Qwen-Coder
- Shelley Contributor
tools:
- Anthropic
- SSE
- httptest
libraries:
- ant
companies:
- boldsoftware
- Shelley
tags:
- ui-race-condition
- asynchronous-testing
- anthopic-thinking-blocks
- pull-request
- conversation-management
---

### TL;DR
This PR fixes a racey distill-replace UI flow so users stay on the source conversation until the slug swap/archive completes, and adds mock-SSE unit tests for Anthropic custom-model test endpoints with thinking blocks.

### Key Quote
"Now the UI: - Tracks active distill-replace operations (source ID -> new ID mapping) - Stays on the source conversation after initiating distill-replace - Waits for the SSE conversation list update showing the source was archived - Only then navigates to the new conversation (which now has the original slug)"

### Summary
- **PR #175** in `boldsoftware/shelley` contains **2 patches** dated **Mon, 6 Apr 2026**.
- **Patch 1/2: distill-replace UX and async test fixes**
  - Fixes a UI bug where `distill-replace` immediately navigated to the new conversation before the slug swap completed.
  - The old behavior caused a confusing intermediate state: a blank/new conversation appeared in the sidebar before the source conversation was archived and the original slug moved.
  - UI changes in `ui/src/App.tsx`:
    - Adds `distillReplaceOperations: Record<string, string>` to track `sourceConvID -> newConvID`.
    - On `api.distillReplaceConversation(...)`, it now:
      - records the mapping,
      - refreshes the conversation list,
      - **does not navigate immediately**.
    - When an SSE update shows the **source conversation archived**:
      - it checks whether that source ID is tracked as a distill-replace operation,
      - removes the tracking entry,
      - navigates to the new conversation after state updates settle.
    - Also updates the `useCallback` dependency list to include `distillReplaceOperations` and `conversationCache`.
  - Backend test updates in `server/distill_test.go`:
    - Existing tests were asserting too early because slug swap and archival happen asynchronously.
    - Adds polling loops (up to **100 iterations**, sleeping **50ms** each time) to wait for:
      - the new conversation to receive the original slug,
      - the source conversation to become archived and parented,
      - multi-pass distill-replace slug swaps to complete before assertions.
    - Affected tests:
      - `TestDistillReplaceConversation`
      - `TestDistillReplaceConversationNoSlug`
      - `TestDistillReplaceMultiPass`
- **Patch 2/2: custom model Anthropic thinking-block tests**
  - Adds unit tests for **issue #146** in `server/custom_models_test.go`.
  - Motivation: prior tests required a real `ANTHROPIC_API_KEY`, so they were not runnable in CI or by most contributors.
  - Introduces helper `mockAnthropicSSE(thinkingText, responseText string)` that emits an SSE stream with:
    - `message_start`
    - a `thinking` content block
    - a `text` content block
    - `message_delta`
    - `message_stop`
  - New tests:
    - `TestCustomModelTestEndpointWithMockAnthropic`
      - Verifies the custom model test endpoint successfully handles Anthropic responses where a thinking block is followed by real text.
      - Expects HTTP 200 and `success=true`.
      - Confirms the returned message is non-empty and not the empty-response error.
    - `TestCustomModelTestEndpointOnlyThinkingBlocks`
      - Verifies responses that contain **only thinking blocks** and no text are rejected.
      - Expects the error message: `"Test failed: empty response from model"`.
  - Both tests use `httptest.NewServer` as a mock SSE Anthropic endpoint and call `h.server.handleTestModel(...)` directly.

### Assessment
This is a **mixed** content item combining a small **feature fix** and **test additions**. Durability is **medium**: the UI race condition and async polling pattern are broadly useful, but the exact code and tests are tied to the current Shelley implementation and Anthropic SSE format as of **2026-04-06**. Density is **high** because the patch details are specific and code-centric. Originality is **primary source** since this is a pull request diff with direct implementation and tests, not a summary of others’ work. Reference style is **refer-back** for anyone maintaining distill-replace behavior or Anthropic model testing. Scrape quality is **good** overall: the diff and test content are present, though only the patch text is shown rather than the full surrounding repository context.
