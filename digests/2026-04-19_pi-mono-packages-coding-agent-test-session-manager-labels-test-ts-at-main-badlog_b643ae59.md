---
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/test/session-manager/labels.test.ts
title: pi-mono/packages/coding-agent/test/session-manager/labels.test.ts at main · badlogic/pi-mono
scraped_at: '2026-04-19T06:46:14Z'
word_count: 668
raw_file: raw/2026-04-19_pi-mono-packages-coding-agent-test-session-manager-labels-test-ts-at-main-badlog_b643ae59.txt
tldr: This is a Vitest test file for `SessionManager` labeling behavior, verifying that labels can be set, cleared, reflected in tree nodes, preserved across branching when on-path, excluded when off-path, omitted from session context, and rejected for missing entries.
key_quote: last label wins
durability: high
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- vitest
libraries: []
companies: []
tags:
- testing
- session-management
- labels
- branching
- vitest
---

### TL;DR
This is a Vitest test file for `SessionManager` labeling behavior, verifying that labels can be set, cleared, reflected in tree nodes, preserved across branching when on-path, excluded when off-path, omitted from session context, and rejected for missing entries.

### Key Quote
"last label wins"

### Summary
- This file tests `SessionManager` from `../../src/core/session-manager.js` using `vitest`.
- It focuses specifically on label-related behavior for session entries, especially messages.
- Covered behaviors:
  - **Set/get labels**:
    - `appendLabelChange(msgId, "checkpoint")` assigns a label.
    - `getLabel(msgId)` returns the latest label.
    - The label change is stored as an entry of type `"label"` with:
      - `id`
      - `targetId`
      - `label`
  - **Clear labels**:
    - Passing `undefined` to `appendLabelChange` removes the label.
  - **Last write wins**:
    - Multiple label changes on the same message result in the most recent label being returned.
    - The tree node’s `labelTimestamp` matches the timestamp of the latest label entry.
  - **Tree integration**:
    - Labels appear on nodes returned by `getTree()`.
    - The test checks both a root message and a child assistant message.
  - **Branching behavior**:
    - `createBranchedSession(msg2Id)` preserves labels for entries on the branched path.
    - Label entries remain present after branching.
    - Labels for entries not on the branched path are removed/not preserved.
  - **Session context behavior**:
    - `buildSessionContext()` includes messages but excludes label entries.
  - **Error handling**:
    - Labeling a non-existent entry throws: `Entry non-existent not found`.
- The tests use both a simple user message and a more detailed assistant message shape including:
  - `api: "anthropic-messages"`
  - `provider: "anthropic"`
  - `model: "test"`
  - `usage` with token counts and cost fields
  - `stopReason: "stop"`

### Assessment
This is a high-durability, reference-oriented test file: the behavior it asserts is fairly stable conceptually, though it is tied to the specific `SessionManager` API in the current codebase. The content type is **tutorial/reference-like test specification** rather than prose, and it is **high density** because nearly every line asserts a concrete invariant. It is **primary source** material because it directly documents intended behavior through executable tests. Best used as **refer-back** material to confirm how labels should behave in `SessionManager`, especially around branching and tree representation. Scrape quality is **good**: the full test file appears present, including all test cases and relevant code blocks.
