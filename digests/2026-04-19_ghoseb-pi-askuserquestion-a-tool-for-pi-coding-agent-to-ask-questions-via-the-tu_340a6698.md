---
url: https://github.com/ghoseb/pi-askuserquestion/
title: 'ghoseb/pi-askuserquestion: A tool for pi Coding Agent to ask questions via the TUI.'
scraped_at: '2026-04-19T08:38:38Z'
word_count: 622
raw_file: raw/2026-04-19_ghoseb-pi-askuserquestion-a-tool-for-pi-coding-agent-to-ask-questions-via-the-tu_340a6698.txt
tldr: pi-askuserquestion is a pi coding agent extension that adds a Claude Code–style interactive TUI for asking structured questions, with support for single-select, multi-select, tabbed multi-question flows, and free-text answers.
key_quote: instead of guessing or rambling, the agent pauses, presents choices, and waits for your answer.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- pi
- pi-tui
- vitest
- pnpm
libraries:
- TypeBox
companies: []
tags:
- developer-tools
- command-line-tools
- tui
- agent-interaction
- user-input
---

### TL;DR
`pi-askuserquestion` is a `pi` coding agent extension that adds a Claude Code–style interactive TUI for asking structured questions, with support for single-select, multi-select, tabbed multi-question flows, and free-text answers.

### Key Quote
“instead of guessing or rambling, the agent pauses, presents choices, and waits for your answer.”

### Summary
- **What it is**
  - A `pi coding agent` extension for interactive user clarification.
  - Designed to let the LLM ask structured questions through a TUI rather than making assumptions.
  - Heavily inspired by Claude Code’s `AskUserQuestion` tool.

- **What it looks like**
  - Supports:
    - **Single question, single select**
    - **Single question, multi select with checkboxes**
    - **Multiple questions in tab view**
    - **Free-text answer**
    - **Submit review** tab that shows all answers before final submission
  - Screenshots are referenced in `docs/images/` for each interaction mode.

- **Installation**
  - Install with:
    - `pi install git:github.com/ghoseb/pi-askuserquestion`

- **How it’s used**
  - Once installed, the tool becomes available automatically to the LLM.
  - Example prompts suggested in the README:
    - “Help me scaffold a new web app. Ask me what you need to know first.”
    - “I want to refactor this module. Ask me about my preferences before making changes.”
  - The LLM calls `ask_user_question`, the user answers in the TUI, and the answers are sent back so the agent can continue.

- **Tool schema**
  - Input shape:
    - `questions`: array of **1–4** questions
    - Each question includes:
      - `question`: full text
      - `header`: short tab label, max 12 chars
      - `options`: array of **2–4** options
      - each option can have:
        - `label`
        - optional `description`
      - `multiSelect`: boolean
  - Output shape:
    - `answers` keyed by question text
    - Single-select returns the selected label
    - Multi-select returns labels joined with `, `
    - Free-text returns typed text

- **Key bindings and interaction model**
  - `↑` / `↓`: move cursor in options
  - `Enter`: confirm single-select
  - `Space`: toggle checkbox in multi-select
  - `Enter` in multi-select: confirm selection
  - `Space` or `Tab` on “Type something...” row: open inline text editor
  - `Enter` in editor: save and close
  - `Esc` in editor: discard and close
  - `←` / `→`: move between tabs
  - `Enter` on Submit tab: submit all answers
  - `Esc` anywhere: cancel the entire question flow

- **Behavior notes**
  - Cursor movement does **not** mean selection; selection is only recorded by `Enter` or `Space` depending on mode.
  - Moving away from a multi-select question with selections auto-confirms it.
  - Multi-select questions can combine checked options and free-text; both are joined into the answer.
  - If run in a non-interactive session, it disables itself for the rest of the session so the LLM won’t keep retrying.
  - Free-text can be cleared by reopening the editor, deleting text, and pressing `Enter`.
  - Users can navigate back to tabs and revise answers; confirmed state updates automatically.

- **Project structure**
  - `src/schema.ts` — TypeBox schemas for tool input/result
  - `src/component.ts` — interactive TUI component using `pi-tui`, independent of `pi` runtime
  - `src/index.ts` — extension entry point registering the tool
  - `tests/component.test.ts` — 108 unit tests using `vitest`

- **Development workflow**
  - Commands:
    - `pnpm install`
    - `pnpm test`
    - `pnpm coverage`
    - `pnpm check` for lint/format, duplicate-check, and dead-code checks
  - Live testing:
    - `pi -e ./src/index.ts`

- **License**
  - MIT

### Assessment
This is a **high-durability** reference/tool entry: the core idea of structured agent-user clarification is stable, though specific `pi` and TUI implementation details are version- and project-dependent. The content type is mainly **reference/tutorial** with some tool documentation, and it is fairly **dense** because it includes schema details, controls, behavior notes, and development commands. It appears to be a **primary source** project README rather than commentary or synthesis. It’s best used as **refer-back** material if you need to install, integrate, or understand the tool’s interaction model. Scrape quality looks **good**: the main README content, command examples, schema, key bindings, structure, and testing info are present, though the screenshots themselves are referenced rather than embedded in the text.
