---
url: https://github.com/boldsoftware/shelley/pull/176/changes
title: 'Add unit tests for custom model endpoint with Anthropic thinking blocks by okottorika · Pull Request #176 · boldsoftware/shelley'
scraped_at: '2026-04-19T07:21:16Z'
word_count: 764
raw_file: raw/2026-04-19_add-unit-tests-for-custom-model-endpoint-with-anthropic-thinking-blocks-by-okott_9fb02dd1.txt
tldr: This PR adds two unit tests for Shelley’s custom model test endpoint to verify Anthropic SSE responses that include thinking blocks are handled correctly, without needing a real `ANTHROPIC_API_KEY`.
key_quote: Add two unit tests using a mock SSE server
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Honjo Masamune
- Qwen-Coder
tools:
- GitHub
- httptest
libraries:
- net/http
companies:
- boldsoftware
tags:
- unit-testing
- anthropic
- server-sent-events
- mock-server
- go-testing
---

### TL;DR
This PR adds two unit tests for Shelley’s custom model test endpoint to verify Anthropic SSE responses that include thinking blocks are handled correctly, without needing a real `ANTHROPIC_API_KEY`.

### Key Quote
"Add two unit tests using a mock SSE server"

### Summary
- This is a GitHub pull request diff for `boldsoftware/shelley` updating `server/custom_models_test.go`.
- The change addresses **issue #146** and explicitly replaces fragile integration-style coverage with **unit tests** that can run in CI.
- A new helper, `mockAnthropicSSE(thinkingText, responseText string)`, constructs a fake Anthropic **server-sent events (SSE)** stream containing:
  - `message_start`
  - a `thinking` content block
  - a `text` content block
  - `message_delta`
  - `message_stop`
- Two tests are added:
  - **`TestCustomModelTestEndpointWithMockAnthropic`**
    - Starts an `httptest` mock server returning the SSE stream.
    - Sends a POST request to `/api/custom-models/test` with:
      - `provider_type: "anthropic"`
      - fake API key `sk-test-fake`
      - mock endpoint ending in `/v1/messages`
      - `model_name: "claude-test"`
    - Asserts:
      - HTTP 200
      - JSON response has `success: true`
      - `message` is non-empty and not the empty-response error
  - **`TestCustomModelTestEndpointOnlyThinkingBlocks`**
    - Uses a mock SSE stream that contains **only thinking blocks** and no text.
    - Asserts:
      - HTTP 200
      - `success` is false
      - `message` equals `"Test failed: empty response from model"`
- The tests verify two important behaviors:
  - Anthropic responses with thinking followed by text should be accepted.
  - Responses that contain only thinking blocks should be rejected as empty.
- Metadata in the patch:
  - Commit: `aa2d26090a10f267f4889e51665cae08df7da0f9`
  - Date: `Mon, 6 Apr 2026 22:59:01 +0530`
  - Co-author: `Qwen-Coder <qwen-coder@alibabacloud.com>`

### Assessment
This is a **high-durability** technical/test PR focused on a specific Anthropic SSE edge case, so the core pattern may remain useful even as implementation details change. It’s a **mixed** content type, mainly a **tutorial/reference** for how the endpoint is tested rather than a narrative article. The density is **high** because it includes concrete test names, request payload fields, endpoint paths, and exact assertions. It is a **primary source** patch rather than commentary, so it is trustworthy for what changed, though its relevance is tied to the project’s current Anthropic integration and issue #146. For later use, this is best as **refer-back** material. Scrape quality is **good**: the diff, helper function, and both test cases are present, with no obvious missing code blocks or sections.
