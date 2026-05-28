---
url: https://github.com/Soleone/pi-tasks
title: 'Soleone/pi-tasks: An extension for pi coding agent to manage tasks, via beads or alternative task backends.'
scraped_at: '2026-04-12T07:33:50Z'
word_count: 287
raw_file: raw/2026-04-12_soleone-pi-tasks-an-extension-for-pi-coding-agent-to-manage-tasks-via-beads-or-a_0d2551f4.txt
tldr: '@soleone/pi-tasks is a pluggable task-management extension for the pi coding agent, with a simple keyboard UI and support for sq, beads, or TODO.md-based task backends.'
key_quote: Task management extension for the [pi coding agent](https://github.com/badlogic/pi-mono), designed for pluggable task backends.
durability: medium
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- pi
- sq
- bd
libraries: []
companies:
- GitHub
tags:
- task-management
- coding-agent
- cli-tools
- productivity
- task-backends
---

### TL;DR
`@soleone/pi-tasks` is a pluggable task-management extension for the pi coding agent, with a simple keyboard UI and support for `sq`, `beads`, or `TODO.md`-based task backends.

### Key Quote
“Task management extension for the [pi coding agent](https://github.com/badlogic/pi-mono), designed for pluggable task backends.”

### Summary
- **What it is**
  - A GitHub repo/package named `@soleone/pi-tasks`.
  - Extends the **pi coding agent** with task management.
  - Built around **pluggable backends** rather than a single storage format.

- **Quick start**
  - Install with:
    - `pi install npm:@soleone/pi-tasks`
  - Open/toggle the Tasks UI with:
    - `ctrl + shift + r`
    - `alt + x`
    - or `/tasks`

- **Keyboard usage**
  - Navigation:
    - `w` / `s` for up/down
    - arrow keys also work
    - `a` to go back
    - `Esc` and left arrow also work
  - Task actions:
    - `space` to change status
    - `0`–`4` to change priority
    - `t` to change task type
    - `f` to search by keyword in title/description
  - List view:
    - `d` to open task details
    - `Enter` to work off a task
    - `Tab` to insert task details into the prompt and close the UI
    - `c` to create a new task
  - Edit view:
    - `Tab` switches focus between inputs
    - `Enter` saves

- **Backend behavior**
  - The extension auto-detects the first applicable backend.
  - If none is found, it falls back to `todo-md`.
  - The repo recommends **`sq`** as the default for most setups because it is:
    - lightweight
    - suitable for brand-new directories
    - able to create local data on demand

- **Supported backends**
  - **`sq`**
    - Uses the `sq` CLI
    - Stores tasks in a `.sift` directory using an `issues.jsonl` file
    - No initialization required
  - **`beads`**
    - Uses the `bd` CLI
    - Stores tasks in a `.beads` directory with multiple files
  - **`todo-md`**
    - Reads or creates a `TODO.md`
    - Uses sections to emulate priority

- **Configuration**
  - `PI_TASKS_TODO_PATH` overrides the TODO file path
  - `PI_TASKS_BACKEND` forces a backend selection
    - supported values: `sq`, `beads`, `todo-md`

### Assessment
This is a **reference/tutorial** style GitHub README with moderate-to-high density because it gives installation, keyboard shortcuts, backend behavior, and env-var configuration in a compact format. Its **durability is medium**: the concepts are stable, but usage details depend on the current `pi` agent and backend CLIs (`sq`, `beads`). It appears to be **primary source** documentation for the extension itself. It’s best used as **refer-back** material when installing or operating the tool, rather than deep study. **Scrape quality is good**: the main README content is present, though the screenshot/image itself isn’t readable from the scrape and there are no deeper sections beyond the overview and usage notes.
