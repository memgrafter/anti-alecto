---
url: https://www.youtube.com/watch?v=kvZ6pUKtN64
title: Claude Code, You, and Todos - YouTube
scraped_at: '2026-04-19T08:19:43Z'
word_count: 4756
raw_file: raw/2026-04-19_claude-code-you-and-todos-youtube_ecf020b1.txt
tldr: 'The speaker prototyped a Claude Code slash-command workflow that turns a `docs/todo.md` file into an interactive task manager: list open todos, refine a selected todo into “what” and “how,” update the file, implement the task, run checks, review diffs in VS Code, then commit and push.'
key_quote: “the to-do item itself and as a human try to judge if this is enough information to claw to do what it's supposed to do.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- Claude Code
- VS Code
- VSCloud
libraries: []
companies: []
tags:
- claude-code
- task-management
- prompt-engineering
- workflow-automation
- software-development
---

### TL;DR
The speaker prototyped a Claude Code slash-command workflow that turns a `docs/todo.md` file into an interactive task manager: list open todos, refine a selected todo into “what” and “how,” update the file, implement the task, run checks, review diffs in VS Code, then commit and push.

### Key Quote
“the to-do item itself and as a human try to judge if this is enough information to claw to do what it's supposed to do.”

### Summary
- The video is a **voice-transcribed, live demo** of building a custom Claude Code **slash command** for managing and executing todos from a markdown file in `docs/todo.md`.
- The intended workflow:
  - **Step 0:** Check whether `docs/todo.md` exists; create it from a template if not.
  - **Step 1:** Read only the **open todos** from the file, present them as a **numbered list with short summaries**, and wait for the user to pick one.
  - **Step 2:** Show the selected todo **verbatim** and ask whether to refine it.
    - Refine the **“what”**: clarify the desired functional/behavioral outcome by asking questions until the description is complete.
    - Refine the **“how”**: use task agents to inspect the codebase and produce a concise implementation plan with the relevant files and changes.
    - Confirm both parts with the user before updating the file.
  - **Step 2C:** Replace the old todo with the refined version, preserving checkbox format.
  - **Step 3:** Implement the todo:
    - Use the refined todo as **guidance**, not a strict guardrail.
    - Follow codebase style/patterns.
    - Run checks after changes (`npm run check` for TypeScript; `npm run build:daemon` for Swift was mentioned as the Swift-side task).
    - Review diffs in a custom **VSCloud** VS Code extension before committing.
    - Commit, push, and record the commit hash and GitHub URL in the completed todo entry.
    - Move the todo from the open section to the completed section at the top of the file.
- The speaker iteratively tightens the command prompt based on Claude’s behavior:
  - Clarifies that step 1 must explicitly **present todos and ask for selection**.
  - Clarifies that step 2 needs a **confirmation step** for both the refined “what” and “how.”
  - Clarifies that the “how” section should be **guidance**, not a hard constraint.
  - Adds an explicit instruction to **replace** the old todo in the file after confirmation.
  - Adds a **manual review step** using VSCloud to inspect diffs before committing.
  - Adds support for **opening multiple diffs in one call** to avoid wasting turns.
- A second todo is then used to test the workflow on a real task:
  - Add a new **`exited`** session state.
  - Stop deleting dead sessions immediately; instead mark them exited in memory.
  - Rename “clear all” to **clear exited**, and make it remove only exited sessions.
  - Sort sessions by status and then by timestamp.
  - Add a visual distinction so exited sessions appear faded/red.
- The implementation demo shows the custom workflow working end-to-end:
  - The agent reads the selected todo, asks clarifying questions, produces a refined description and implementation plan, updates the todo file, and then proceeds to code changes.
  - The speaker manually inspects the diffs through the VSCloud extension.
  - After building and running the app, the UI shows sessions in different states: working, waiting for input, and exited.
- A notable side observation: the speaker says the workflow may eventually **replace a separate `development.md`** file because the refined todo can serve as a more compact implementation guide.
- The transcript is **messy and highly conversational** because it comes from voice transcription; it includes interruptions, self-corrections, and ad hoc experimentation rather than a polished tutorial.

### Assessment
This is a **mixed tutorial/demo and workflow design session** with high practical detail but low polish. **Durability: medium** — the general pattern of using Claude Code to refine todos and drive implementation is fairly reusable, but many specifics are tied to this particular setup, custom slash commands, the `docs/todo.md` format, and the speaker’s current toolchain/version behavior. **Content type: tutorial / mixed**. **Density: high** in the parts where the prompt is refined and the implementation workflow is described, though the transcript is also padded by live editing and narration. **Originality: primary source** because it is the speaker’s own live experimentation, not a summary of others’ work. **Reference style: refer-back** if you’re building a similar Claude Code workflow or want the exact prompt-shaping ideas; otherwise skim-once is enough. **Scrape quality: partial** — the transcript is clearly incomplete/garbled in places, and visual elements, code, exact file contents, and the final prompt text are not fully captured.
