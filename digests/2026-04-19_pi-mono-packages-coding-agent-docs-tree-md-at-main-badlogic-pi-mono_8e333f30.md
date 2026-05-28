---
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/tree.md
title: pi-mono/packages/coding-agent/docs/tree.md at main · badlogic/pi-mono
scraped_at: '2026-04-19T07:29:19Z'
word_count: 1078
raw_file: raw/2026-04-19_pi-mono-packages-coding-agent-docs-tree-md-at-main-badlogic-pi-mono_8e333f30.txt
tldr: /tree is a session-history navigation command that lets you jump to any node in a conversation tree, optionally summarize the abandoned branch, and fire hook events around the switch.
key_quote: Sessions are stored as trees where each entry has an `id` and `parentId`.
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- /tree
- /fork
libraries: []
companies:
- pi-mono
- badlogic
tags:
- session-history
- navigation
- hooks
- documentation
- tree-structure
---

### TL;DR
`/tree` is a session-history navigation command that lets you jump to any node in a conversation tree, optionally summarize the abandoned branch, and fire hook events around the switch.

### Key Quote
“Sessions are stored as trees where each entry has an `id` and `parentId`.”

### Summary
- **What `/tree` does**
  - Provides **tree-based navigation** of session history, unlike `/fork`, which creates a new session file.
  - Moves the **leaf pointer** within the same session to a selected node.
  - Can optionally **summarize the branch being left** before switching.

- **Comparison with `/fork`**
  - `/fork`:
    - Shows a flat list of user messages
    - Extracts a path into a **new session file**
    - Never summarizes
    - Emits `session_before_fork` / `session_start` (`reason: "fork"`)
  - `/tree`:
    - Shows the **full tree structure**
    - Changes the leaf in the **same session**
    - Summary is **optional**
    - Emits `session_before_tree` / `session_tree`

- **Tree UI behavior**
  - Displays the conversation as a tree with active path and branch points.
  - Keyboard controls:
    - `↑/↓`: depth-first navigation
    - `←/→`: page up/down
    - `Ctrl+←` / `Alt+←`: fold branch or jump to previous branch segment start
    - `Ctrl+→` / `Alt+→`: unfold branch or jump to next branch segment start
    - `Shift+L`: set/clear label
    - `Shift+T`: toggle label timestamps
    - `Enter`: select node
    - `Escape` / `Ctrl+C`: cancel
    - `Ctrl+U`: toggle user messages only
    - `Ctrl+O`: toggle show all entries, including custom/label entries
  - Display details:
    - Terminal height is half the screen
    - Current leaf marked with `← active`
    - Labels appear inline like `[label-name]`
    - Foldable nodes use `⊟`; folded branches use `⊞`
    - Search/filter changes reset all folds
    - Active subtree is shown first at each branch point; sibling branches are sorted by timestamp (oldest first)

- **Selection behavior**
  - **User message or custom message**
    - Leaf becomes the **parent** of the selected node
    - Message text is placed in the editor for re-submission
    - User edits and submits to create a new branch
  - **Non-user message** (assistant, compaction, etc.)
    - Leaf becomes the **selected node**
    - Editor stays empty
    - User continues from that point
  - **Selecting the root user message**
    - Leaf resets to `null`
    - Message is placed in the editor
    - Effectively restarts the conversation

- **Branch summarization**
  - When switching branches, the user can choose:
    1. **No summary**
    2. **Summarize** with the default prompt
    3. **Summarize with custom prompt**, appended to or replacing the default prompt
  - The system summarizes the path from the **old leaf back to the common ancestor** with the target branch.
  - Summarization stops at:
    - the **common ancestor**, or
    - a **compaction node**, whichever comes first
  - Summaries are stored as `BranchSummaryEntry` with:
    - `type: "branch_summary"`
    - `id`
    - `parentId` = new leaf position
    - `timestamp`
    - `fromId` = old leaf
    - `summary`
    - optional `details`

- **Implementation details**
  - Main API:
    - `AgentSession.navigateTree(targetId, options?)`
    - Options include:
      - `summarize`
      - `customInstructions`
      - `replaceInstructions`
      - `label`
    - Returns `{ editorText?: string; cancelled: boolean }`
  - Navigation flow:
    1. Validate target and no-op
    2. Find common ancestor
    3. Collect entries to summarize if needed
    4. Fire `session_before_tree`
    5. Run default summarizer if needed
    6. Switch leaf via `branch()` or `branchWithSummary()`
    7. Update agent messages from session context
    8. Fire `session_tree`
    9. Notify custom tools
    10. Return editor text if a user message was selected
  - `SessionManager` methods highlighted:
    - `getLeafUuid()`
    - `resetLeaf()`
    - `getTree()`
    - `branch(id)`
    - `branchWithSummary(id, summary)`
  - `InteractiveMode` flow:
    - `/tree` opens `TreeSelectorComponent`
    - prompts for summarization
    - calls `session.navigateTree()`
    - clears and re-renders chat
    - sets editor text if applicable

- **Hook events**
  - `session_before_tree`
    - Carries preparation data: target, old leaf, common ancestor, entries to summarize, summary choice, custom instructions, label
    - Can cancel navigation or override summary/custom instructions/label
  - `session_tree`
    - Reports the new and old leaf IDs
    - Includes the summary entry if one was created
    - Indicates whether the event came from a hook
  - Example custom summarizer hook shows how an extension can intercept `session_before_tree`, generate its own summary, and return it.

- **Error handling**
  - If summarization fails, navigation is canceled and an error is shown.
  - If the user aborts with Escape, navigation is canceled.
  - If a hook returns `cancel: true`, navigation is canceled silently.

### Assessment
This is a **reference/documentation** page with **high durability** in the sense that it describes a concrete command architecture and API, though some implementation specifics may change with future versions of the project. The content is **mixed** but mostly technical/reference, with high density and a lot of specific API names, event payloads, keyboard shortcuts, and behavior rules. It appears to be a **primary source** from the project repository rather than commentary or synthesis. It is best used as a **refer-back** document, especially for implementing or using `/tree`, hook events, or session navigation behavior. Scrape quality looks **good**: the main text, tables, code snippets, and interface details are present, with no obvious missing sections from this markdown page.
