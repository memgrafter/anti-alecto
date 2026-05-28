---
url: https://github.com/memgrafter/pi-codex-model-guard-extension/blob/master/extensions/codex-model-guard.ts
title: pi-codex-model-guard-extension/extensions/codex-model-guard.ts at master · memgrafter/pi-codex-model-guard-extension
scraped_at: '2026-04-19T08:39:13Z'
word_count: 3840
raw_file: raw/2026-04-19_pi-codex-model-guard-extension-extensions-codex-model-guard-ts-at-master-memgraf_144e013f.txt
tldr: A TypeScript Pi extension that intercepts `openai-codex` streaming requests, rewrites/normalizes Codex Responses API payloads, and raises a UI warning when a requested `gpt-5.3-codex` response comes back downgraded to another model.
key_quote: “Overrides openai-codex provider streaming via pi.registerProvider(..., streamSimple)”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- openai-codex
- pi
libraries:
- '@mariozechner/pi-ai'
- '@mariozechner/pi-coding-agent'
companies:
- OpenAI
tags:
- typescript
- streaming-apis
- model-guard
- browser-extension
- openai-responses-api
---

### TL;DR
A TypeScript Pi extension that intercepts `openai-codex` streaming requests, rewrites/normalizes Codex Responses API payloads, and raises a UI warning when a requested `gpt-5.3-codex` response comes back downgraded to another model.

### Key Quote
“Overrides openai-codex provider streaming via pi.registerProvider(..., streamSimple)”

### Summary
- **What this file is**
  - A single extension module: `codex-model-guard.ts`
  - It registers a custom provider override for `openai-codex` under the API name `openai-codex-responses`
  - Its main purpose is to detect model downgrades for `gpt-5.3-codex` by inspecting the raw `response.completed` / `response.done` stream payload and comparing the returned `response.model`

- **Core behavior**
  - Wraps Codex streaming with `createGuardedCodexStreamSimple(...)`
  - Sends requests to the Codex endpoint derived from `baseUrl`:
    - default: `https://chatgpt.com/backend-api`
    - resolved path: `/codex/responses`
  - Builds request headers including:
    - `Authorization: Bearer <token>`
    - `chatgpt-account-id`
    - `OpenAI-Beta: responses=experimental`
    - `originator: pi`
    - a custom `User-Agent`
    - optional `session_id`
  - Parses SSE manually (`parseSSE`) and maps Codex event types into OpenAI Responses API event objects

- **Model downgrade guard**
  - Only checks for downgrades when:
    - the guard is enabled, and
    - the selected model matches `gpt-5.3-codex` via `isExpectedModelId`
  - Watches the completed response’s `model` field:
    - if it is missing, records a mismatch with `"<missing response.model>"`
    - if it differs from `gpt-5.3-codex` (or a variant starting with that prefix), records a downgrade
  - Does **not** stop the request; it only warns in the UI and appends a mismatch entry

- **State and UI**
  - Maintains extension state:
    - `enabled: boolean`
  - Persists guard state in session entries of type:
    - `codex-model-guard`
  - Stores downgrade events as entries of type:
    - `codex-model-guard-mismatch`
  - UI status indicator:
    - muted dot when enabled
    - error/red dot when a downgrade has been detected
  - Provides a command:
    - `/codex-guard on|off|status|test|clear`
  - Also registers a boolean flag:
    - `codex-guard`
    - default: `true`

- **Request/response transformation details**
  - `convertResponsesMessages(...)` converts Pi message history into OpenAI Responses input
  - It handles:
    - user text
    - user images
    - assistant text
    - assistant thinking/reasoning
    - assistant tool calls
    - tool results
  - It normalizes tool call IDs for Codex-compatible providers:
    - replaces illegal characters
    - trims overly long IDs
    - ensures item IDs have an `fc_` prefix when needed
  - `transformMessages(...)` also repairs message sequences by inserting synthetic `toolResult` messages with `"No result provided"` when assistant tool calls appear without matching results
  - Thinking content:
    - preserved as thinking when possible
    - converted to plain text if message/model context differs
  - Tool call signatures are stripped when needed for cross-model compatibility

- **Streaming/event handling**
  - `processResponsesStreamLocal(...)` converts raw Responses SSE events into Pi assistant stream events:
    - `thinking_start`, `thinking_delta`, `thinking_end`
    - `text_start`, `text_delta`, `text_end`
    - `toolcall_start`, `toolcall_delta`, `toolcall_end`
    - `done`, `error`
  - Tracks reasoning summaries, output text, refusal text, and streaming function-call arguments
  - On `response.completed`:
    - computes usage/cached token counts
    - calls `calculateCost(model, output.usage)`
    - maps final stop reason from Codex status
    - if tool calls exist and stop reason is still `"stop"`, changes it to `"toolUse"`

- **Retries and error handling**
  - Retries up to `MAX_RETRIES = 3`
  - Retryable statuses:
    - `429`, `500`, `502`, `503`, `504`
  - Also retries on certain error text patterns:
    - rate limit, overloaded, service unavailable, upstream connect, connection refused
  - `parseErrorResponse(...)` tries to turn OpenAI-style error JSON into friendlier messages
    - especially for usage limits / plan limits
  - Aborted requests become `"Request was aborted"`

- **Token/account handling**
  - `extractAccountId(...)` decodes a JWT access token and reads:
    - `https://api.openai.com/auth.chatgpt_account_id`
  - This is required for the `chatgpt-account-id` request header

- **Reasoning/text settings**
  - Supports `reasoningEffort`, `reasoningSummary`, and `textVerbosity`
  - Clamps unsupported effort values:
    - `xhigh` becomes `high`
  - Applies model-specific constraints:
    - `gpt-5.2*` and `gpt-5.3*`: `minimal` becomes `low`
    - `gpt-5.1`: `xhigh` becomes `high`
    - `gpt-5.1-codex-mini`: `high`/`xhigh` become `high`, otherwise `medium`

- **Notable implementation choices**
  - The extension does not block or alter a downgraded response; it only surfaces the mismatch
  - The guard is keyed to `event.message.timestamp` and a `mismatchByTimestamp` map
  - It includes a synthetic `test` command that fabricates a downgrade alert for UI verification

### Assessment
This is a high-density, highly specific **reference/tutorial-mixed** code file with **high durability** in terms of patterns but **medium staleness risk** because it depends on current OpenAI/Codex streaming shapes, model names (`gpt-5.3-codex`), and Pi extension APIs. It appears to be **primary source** code rather than commentary or synthesis. Best used as **refer-back** material if you need to understand how the guard works, how it serializes Responses API messages, or how to hook into Pi’s provider/session/UI events. Scrape quality is **good**: the full TypeScript file content is present, including imports, helper functions, streaming logic, command registration, and event handlers; no obvious sections or code blocks appear missing.
