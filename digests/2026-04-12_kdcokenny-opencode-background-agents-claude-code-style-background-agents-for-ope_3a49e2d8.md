---
url: https://github.com/kdcokenny/opencode-background-agents
title: 'kdcokenny/opencode-background-agents: Claude Code-style background agents for OpenCode – async delegation with context persistence'
scraped_at: '2026-04-12T09:44:42Z'
word_count: 872
raw_file: raw/2026-04-12_kdcokenny-opencode-background-agents-claude-code-style-background-agents-for-ope_3a49e2d8.txt
tldr: A KDCO/OpenCode plugin that adds Claude Code-style background delegation with persisted markdown results, so research can run asynchronously, survive compaction, and be retrieved later with `delegate()`, `delegation_read()`, and `delegation_list()`.
key_quote: “Keep working while research runs in the background. Your work survives context compaction.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- OpenCode
- Claude Code
- KDCO
- OCX
tools:
- opencode-background-agents
- OCX
- delegate
- delegation_read
- delegation_list
libraries:
- unique-names-generator
companies:
- KDCO Registry
- OpenCode
- OCX
tags:
- background-agents
- context-compaction
- open-code
- plugin-development
- async-delegation
---

### TL;DR
A KDCO/OpenCode plugin that adds Claude Code-style background delegation with persisted markdown results, so research can run asynchronously, survive compaction, and be retrieved later with `delegate()`, `delegation_read()`, and `delegation_list()`.

### Key Quote
“Keep working while research runs in the background. Your work survives context compaction.”

### Summary
- **What it is**
  - `opencode-background-agents` is an OpenCode plugin for async background delegation.
  - It is designed to let you launch research or other read-only tasks, keep coding or brainstorming, and retrieve the results later.
  - It aims to mimic Claude Code-style background-agent lifecycle behavior within OpenCode plugin limits.

- **Core problem it solves**
  - AI context windows fill up, triggering compaction.
  - When compaction happens, research done earlier can be forgotten or lost from immediate context.
  - This plugin persists delegation outputs to disk so results remain recoverable after compaction, session restarts, or crashes.

- **How it works**
  - Workflow shown in the README:
    1. **Delegate** a task like “Research OAuth2 PKCE best practices”
    2. **Continue** working normally
    3. Receive a **task-notification** when the background job finishes
    4. **Retrieve** the result with `delegation_read()`
  - Results are saved as markdown files under:
    - `~/.local/share/opencode/delegations/`
  - Each delegation gets an automatically generated title and summary to make searching and retrieval easier.

- **Tools added**
  - `delegate(prompt, agent)` — launch a background task
  - `delegation_read(id)` — retrieve a specific delegation result
  - `delegation_list()` — list all delegations with titles and summaries

- **Lifecycle behavior claims**
  - Stable delegation IDs are reused across state, artifact path, notifications, and retrieval.
  - Explicit lifecycle states are used: `registered` → `running` → terminal.
  - Terminal-state protection prevents late progress events from changing a completed task back into a non-terminal state.
  - Persistence happens before terminal notification delivery.
  - `delegation_read(id)` blocks until completion or timeout and returns deterministic terminal info with persisted fallback.
  - Running and unread completed delegation context is carried forward during compaction, including retrieval hints.

- **Installation**
  - Preferred install via OCX:
    ```bash
    ocx add kdco/background-agents --from https://registry.kdco.dev
    ```
  - Optional broader package:
    ```bash
    ocx add kdco/workspace --from https://registry.kdco.dev
    ```
    - Described as bundling background agents with specialist agents, planning tools, and research protocols.
  - Manual install is also documented by copying source files into:
    - `.opencode/plugin/background-agents.ts`
  - Manual setup requires handling dependencies like `unique-names-generator`.

- **Important limitations**
  - **Read-only sub-agents only**
    - `delegate` works only for sub-agents with permissions:
      - `edit=deny`
      - `write=deny`
      - `bash={"*":"deny"}`
    - Any write-capable sub-agent must use OpenCode’s native `task` tool instead.
  - Reason given:
    - Background delegations run in isolated sessions outside OpenCode’s session tree.
    - Undo/branching cannot safely track or revert changes made there.
  - **Timeout**
    - Delegations time out after **15 minutes**.
  - **Parity boundaries**
    - The plugin claims lifecycle parity, not internal runtime parity.
    - It does not replicate Claude/OpenCode internal AppState/task queue internals, notification priority controls, or write-capable background execution with native undo/branching parity.

- **FAQ highlights**
  - The AI can identify past work because each delegation gets a title and summary, not just an opaque ID.
  - Results persist beyond the session and remain on disk.
  - The plugin is meant to save context, not consume it.
  - It differs from Claude Code’s native Task tool mainly by adding persistence so results survive compaction.
  - OCX installation is recommended for easier setup, dependency handling, and updates.

- **Project context**
  - The plugin is part of the **KDCO Registry** / **OCX ecosystem**.
  - The README points users to the main OCX monorepo for maintenance, issues, and pull requests.
  - It explicitly says not to file issues or PRs in this facade repository.
  - It includes a disclaimer that it is not built by or affiliated with the OpenCode team.
  - License: **MIT**

### Assessment
This is a high-density, mostly reference-style plugin README with a clear tutorial component and strong product framing. Durability is **medium** because the concepts around delegation, persistence, and context compaction are fairly timeless, but the instructions, install commands, and compatibility claims are tied to the current OpenCode/OCX ecosystem and may change. The content type is **mixed**: part documentation, part tutorial, part product announcement. It appears to be **primary source** project documentation rather than commentary or synthesis. It is best used as **refer-back** material if you plan to install or compare the plugin’s behavior and limitations, though the core idea is readable in a quick skim. Scrape quality is **good**: the README sections, commands, limitations, FAQ, and disclaimer are present, with no obvious missing code blocks or major structural gaps.
