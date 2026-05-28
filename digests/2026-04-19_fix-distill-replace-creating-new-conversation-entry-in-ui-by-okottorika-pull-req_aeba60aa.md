---
url: https://github.com/boldsoftware/shelley/pull/174
title: 'Fix distill-replace creating new conversation entry in UI by okottorika · Pull Request #174 · boldsoftware/shelley'
scraped_at: '2026-04-19T07:21:26Z'
word_count: 1269
raw_file: raw/2026-04-19_fix-distill-replace-creating-new-conversation-entry-in-ui-by-okottorika-pull-req_aeba60aa.txt
tldr: This pull request fixes a distill-replace UX bug in Shelley by delaying navigation until the source conversation is archived via SSE, so users no longer briefly see a confusing blank/new conversation entry; it also updates tests to wait for the async slug-swap and archival steps.
key_quote: 'Now the UI: - Tracks active distill-replace operations (source ID -> new ID mapping) - Stays on the source conversation after initiating distill-replace - Waits for the SSE conversation list update showing the source was archived - Only then navigates to the new conversation'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Honjo Masamune
- Qwen-Coder
tools: []
libraries: []
companies:
- Shelley
tags:
- user-interface
- event-driven-updates
- asynchronous-workflows
- testing
- bug-fix
---

### TL;DR
This pull request fixes a distill-replace UX bug in Shelley by delaying navigation until the source conversation is archived via SSE, so users no longer briefly see a confusing blank/new conversation entry; it also updates tests to wait for the async slug-swap and archival steps.

### Key Quote
“Now the UI: - Tracks active distill-replace operations (source ID -> new ID mapping) - Stays on the source conversation after initiating distill-replace - Waits for the SSE conversation list update showing the source was archived - Only then navigates to the new conversation”

### Summary
- **Problem being fixed**
  - The `distill-replace` flow was navigating to the newly created conversation too early.
  - Before the slug swap completed, the UI could show a confusing blank/new conversation in the sidebar.

- **UI behavior changes in `ui/src/App.tsx`**
  - Added `distillReplaceOperations` state to track active operations as a mapping from:
    - `sourceConvID -> newConvID`
  - After `api.distillReplaceConversation(sourceConversationId, model, cwd)`:
    - The app now stores the operation in `distillReplaceOperations`
    - Refreshes the conversation list with `api.getConversations()`
    - **Does not immediately navigate** to the new conversation
  - When an SSE conversation update arrives and the **source conversation is archived**:
    - The code checks whether that source conversation is part of an active distill-replace
    - If so, it removes the tracking entry
    - Then it navigates to the new conversation after state updates complete
  - Added a **15-second fallback timeout**:
    - If SSE never reports the archival update
    - The UI navigates anyway so the user doesn’t get stuck

- **Additional UI details**
  - The SSE handler dependency list now includes:
    - `distillReplaceOperations`
    - `conversationCache`
  - This makes the handler aware of the tracked distill-replace state.

- **Test updates in `server/distill_test.go`**
  - Tests now wait for asynchronous slug swaps before asserting results.
  - `TestDistillReplaceConversation`
    - Polls up to 100 times with `50ms` sleeps until the new conversation’s slug becomes the original slug
  - `TestDistillReplaceConversationNoSlug`
    - Waits until the new conversation gets a generated slug
    - Then waits until the source conversation becomes archived and parented
  - `TestDistillReplaceMultiPass`
    - Adds waits after each distillation pass for the slug swap to complete before checking the final state
  - These changes reflect that slug swap and archival are asynchronous, so immediate assertions were flaky.

- **Net effect**
  - Users should see a smoother transition without intermediate confusing states.
  - Tests are made more reliable by accounting for async backend behavior.

### Assessment
This is a **mixed** content item: mostly a small code-change announcement/patch description plus inline diff context. Durability is **medium** because the underlying pattern—waiting for backend state to settle before navigating—is broadly useful, but the exact implementation is tied to the current Shelley UI and SSE flow. Density is **high**, with concrete state variables, event timing, timeout values (`15000` ms), and test polling logic (`100` iterations at `50ms`). Originality is **primary source** because it includes the actual patch diff and author explanation rather than commentary. It’s best used as a **refer-back** reference if you need to understand this specific bug fix or the async navigation pattern. Scrape quality is **good** overall: the key diff and description are present, though this excerpt does not include the full surrounding file context beyond the changed hunks.
