---
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md#branch-summarization
title: pi-mono/packages/coding-agent/docs/compaction.md at main · badlogic/pi-mono
scraped_at: '2026-04-19T08:38:56Z'
word_count: 1685
raw_file: raw/2026-04-19_pi-mono-packages-coding-agent-docs-compaction-md-at-main-badlogic-pi-mono_ee2d0401.txt
tldr: This doc explains how pi manages long LLM sessions by compacting old conversation context and summarizing branch changes, including the triggers, data structures, serialization format, extension hooks, and settings that control both behaviors.
key_quote: LLMs have limited context windows. When conversations grow too long, pi uses compaction to summarize older content while preserving recent work.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- /compact
- /tree
- serializeConversation
- convertToLlm
- read
- bash
libraries:
- '@mariozechner/pi-coding-agent'
companies:
- pi
- pi-mono
tags:
- llm-context-management
- conversation-compaction
- branch-summarization
- extension-hooks
- typescript-architecture
---

### TL;DR
This doc explains how pi manages long LLM sessions by compacting old conversation context and summarizing branch changes, including the triggers, data structures, serialization format, extension hooks, and settings that control both behaviors.

### Key Quote
"LLMs have limited context windows. When conversations grow too long, pi uses compaction to summarize older content while preserving recent work."

### Summary
- The page covers two summarization mechanisms in pi:
  - **Compaction**: triggered when context gets too large, or manually via `/compact`
  - **Branch summarization**: triggered when navigating with `/tree`
- Both mechanisms:
  - use the same **structured summary format**
  - **track file operations cumulatively**
  - can be customized by extensions
- Source files referenced:
  - `packages/coding-agent/src/core/compaction/compaction.ts`
  - `packages/coding-agent/src/core/compaction/branch-summarization.ts`
  - `packages/coding-agent/src/core/compaction/utils.ts`
  - `packages/coding-agent/src/core/session-manager.ts`
  - `packages/coding-agent/src/core/extensions/types.ts`

#### Compaction
- Auto-compaction triggers when:
  - `contextTokens > contextWindow - reserveTokens`
- Default `reserveTokens` is **16384**
  - configurable in `~/.pi/agent/settings.json` or `<project-dir>/.pi/settings.json`
- Manual trigger:
  - `/compact [instructions]`
- Process:
  1. Walk backward through messages to find a cut point based on `keepRecentTokens`
  2. Collect messages to summarize
  3. Generate a structured summary with the LLM
  4. Append a `CompactionEntry`
  5. Reload session using the summary plus kept messages
- Default `keepRecentTokens` is **20000**
- Repeated compactions start from the previous kept boundary, not the compaction entry itself, so earlier preserved messages remain part of later summaries
- `tokensBefore` is recalculated from the rebuilt session context before writing the new entry

#### Split turns
- A **turn** starts with a user message and includes assistant/tool activity until the next user message
- Normally compaction cuts at turn boundaries
- If a single turn exceeds `keepRecentTokens`, compaction may cut mid-turn at an assistant message
- In this case:
  - `isSplitTurn = true`
  - `messagesToSummarize = []`
  - `turnPrefixMessages` holds the early part of the large turn
  - pi generates two summaries and merges them:
    1. history summary
    2. split-turn prefix summary

#### Valid cut points
- User messages
- Assistant messages
- BashExecution messages
- Custom messages (`custom_message`, `branch_summary`)
- Never cut at **tool results** because they must stay attached to their tool call

#### `CompactionEntry`
- Defined in `session-manager.ts`
- Fields:
  - `type: "compaction"`
  - `id`, `parentId`, `timestamp`
  - `summary`
  - `firstKeptEntryId`
  - `tokensBefore`
  - optional `fromHook`
  - optional `details`
- Default `details` for compaction:
  - `readFiles: string[]`
  - `modifiedFiles: string[]`
- `details` can contain any JSON-serializable data

#### Branch summarization
- Triggered when using `/tree` to navigate to another branch
- Purpose: preserve context from the abandoned branch in the new branch
- Process:
  1. Find the deepest common ancestor between old and new positions
  2. Collect entries from the old leaf back to that ancestor
  3. Apply token budget, newest first
  4. Generate summary
  5. Append a `BranchSummaryEntry`
- Example shown:
  - old path `A ─ B ─ C ─ D`
  - target path `A ─ E ─ F`
  - summary covers `B, C, D`

#### Cumulative file tracking
- Both compaction and branch summarization accumulate file history from:
  - tool calls inside summarized messages
  - previous `details` from earlier compactions or branch summaries
- This preserves the full history of files read and modified across multiple summarizations

#### `BranchSummaryEntry`
- Defined in `session-manager.ts`
- Fields:
  - `type: "branch_summary"`
  - `id`, `parentId`, `timestamp`
  - `summary`
  - `fromId`
  - optional `fromHook`
  - optional `details`
- Default `details`:
  - `readFiles: string[]`
  - `modifiedFiles: string[]`

#### Summary format used by both mechanisms
- The structured summary has these sections:
  - `## Goal`
  - `## Constraints & Preferences`
  - `## Progress`
    - Done
    - In Progress
    - Blocked
  - `## Key Decisions`
  - `## Next Steps`
  - `## Critical Context`
  - `<read-files>` and `<modified-files>` blocks
- This format is designed to preserve actionable task state, decisions, and file references

#### Message serialization
- Before summarization, messages are converted to text with `serializeConversation()`
- Serialized forms include:
  - `[User]: ...`
  - `[Assistant thinking]: ...`
  - `[Assistant]: ...`
  - `[Assistant tool calls]: ...`
  - `[Tool result]: ...`
- Tool results are truncated to **2000 characters** to keep prompts manageable

#### Extension hooks
- Extensions can intercept or replace both summarization flows

##### `session_before_compact`
- Fired before auto-compaction or `/compact`
- Can cancel compaction or provide a custom summary
- Exposes:
  - `preparation.messagesToSummarize`
  - `turnPrefixMessages`
  - `previousSummary`
  - `fileOps`
  - `tokensBefore`
  - `firstKeptEntryId`
  - `settings`
  - `branchEntries`
  - `signal`
- Example shows returning a custom `compaction` object with summary, `firstKeptEntryId`, `tokensBefore`, and optional `details`
- The doc also shows how to convert messages to text using:
  - `convertToLlm()`
  - `serializeConversation()`

##### `session_before_tree`
- Fired before `/tree` navigation
- Always fires, even if the user does not want summary
- Can cancel navigation or provide a custom summary
- Exposes:
  - `targetId`
  - `oldLeafId`
  - `commonAncestorId`
  - `entriesToSummarize`
  - `userWantsSummary`
  - `signal`

#### Settings
- Configured in:
  - `~/.pi/agent/settings.json`
  - `<project-dir>/.pi/settings.json`
- Example:
  ```json
  {
    "compaction": {
      "enabled": true,
      "reserveTokens": 16384,
      "keepRecentTokens": 20000
    }
  }
  ```
- Settings table:
  - `enabled` — default `true`
  - `reserveTokens` — default `16384`
  - `keepRecentTokens` — default `20000`
- Auto-compaction can be disabled while still allowing manual `/compact`

### Assessment
This is a high-durability, mixed reference/tutorial document: the core concepts around context-window compaction and branch summarization are fairly stable, but the details are tied to a specific codebase and current implementation. It is dense and technical, with concrete TypeScript interfaces, triggers, settings, and control flow, and it reads as a primary-source implementation guide rather than commentary. It is best used as a **refer-back** reference when working on pi’s agent/session logic or extension hooks. Scrape quality looks **good**: the main sections, code snippets, tables, and diagrams are all present, though any linked source files themselves are not included here.
