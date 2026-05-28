---
url: https://github.com/nicobailon/pi-interview-tool
title: 'nicobailon/pi-interview-tool: Interactive form tool for pi-agent to gather user responses with keyboard navigation, themes, and image attachments'
scraped_at: '2026-04-19T08:38:27Z'
word_count: 2237
raw_file: raw/2026-04-19_nicobailon-pi-interview-tool-interactive-form-tool-for-pi-agent-to-gather-user-r_e4575d9e.txt
tldr: pi-interview-tool is a pi-agent extension that opens a keyboard-friendly interview form for collecting structured user answers, images, and rich content, with auto-save, session recovery, theming, and multi-agent queue handling.
key_quote: Responses saved to localStorage, restored on reload
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- pi-agent
- Glimpse
- WKWebView
- Chart.js
- Mermaid
libraries:
- glimpseui
companies:
- pi-agent
tags:
- interactive-forms
- agent-tools
- keyboard-navigation
- session-management
- theming
---

### TL;DR
`pi-interview-tool` is a `pi-agent` extension that opens a keyboard-friendly interview form for collecting structured user answers, images, and rich content, with auto-save, session recovery, theming, and multi-agent queue handling.

### Key Quote
"Responses saved to localStorage, restored on reload"

### Summary
- **What it is**
  - A custom interview tool for `pi-agent` that presents clarification questions in an interactive form.
  - On macOS it uses **Glimpse** to open a native `WKWebView` window; on other platforms it falls back to a browser tab.
  - Installed via:
    ```bash
    pi install npm:pi-interview
    ```
  - Requires **pi-agent v0.35.0+**.
  - Optional dependency for native macOS rendering: `pi install npm:glimpseui`.

- **Core workflow**
  - The agent calls `interview({ questions, timeout, verbose })`.
  - A local server starts, the form opens, the user answers, and responses are returned to the agent.
  - Submission is done with `⌘+Enter`; `Esc` twice cancels.
  - Auto-save writes progress to `localStorage`, and the timeout resets on user activity.

- **Question types and schema**
  - Supported question types:
    - `single`
    - `multi`
    - `text`
    - `image`
    - `info`
  - Questions can include:
    - `options`
    - `recommended`
    - `conviction` (`strong` or `slight`)
    - `weight` (`critical` or `minor`)
    - `context`
    - `content`
    - `media`
  - `info` panels are non-interactive and skipped in keyboard navigation.
  - `content` supports code snippets, diffs, Markdown previews, file/line metadata, and highlighted lines.
  - `media` supports:
    - images
    - tables
    - Chart.js charts
    - Mermaid diagrams
    - raw HTML

- **Recommendation and weighting behavior**
  - Recommended options are visually marked with a badge.
  - Default behavior pre-selects recommended options.
  - `conviction: "slight"` shows the recommendation but does not pre-select.
  - `weight: "critical"` makes the card visually prominent; `minor` makes it more compact.

- **Interactive features**
  - Full keyboard navigation:
    - `↑` / `↓` between options
    - `←` / `→` between questions
    - `Tab` to cycle
    - `Enter` / `Space` to select
    - `⌘+V` to paste image or file path
    - `⌘+Enter` to submit
    - `⌘+Shift+L` to toggle theme when enabled
  - Supports image upload by:
    - drag and drop
    - file picker
    - paste
    - pasted file paths
  - Supports “Other” text input for single/multi-select questions.
  - Includes “Generate more” and “Review options” buttons for select questions, powered by an LLM.

- **Session management**
  - Uses a configurable timeout with visible countdown badge.
  - Shows an overlay when timeout expires, allowing the user to stay or close.
  - Multi-agent support prevents focus stealing:
    - only the first interview auto-opens
    - additional interviews are queued
    - queued sessions are surfaced via URL and a top-right toast dropdown
  - Session status bar shows project path, git branch, and session ID.
  - Sessions can be saved as HTML snapshots for later review or revival.

- **Recovery and persistence**
  - Abandoned or timed-out interviews are saved to:
    - `~/.pi/interview-recovery/`
  - Recovery files are automatically cleaned up after 7 days.
  - Saved snapshots go to:
    - `~/.pi/interview-snapshots/`
  - Snapshot folders contain:
    - `index.html`
    - `images/`
  - Snapshots can be reopened with pre-populated answers.

- **Configuration**
  - Settings live in `~/.pi/agent/settings.json`.
  - Configurable fields include:
    - `timeout`
    - `port`
    - `snapshotDir`
    - `autoSaveOnSubmit`
    - `generateModel`
    - theme settings (`mode`, `name`, `lightPath`, `darkPath`, `toggleHotkey`)
  - Timeout precedence is:
    - params > settings > default (600s)

- **Theming**
  - Built-in themes:
    - `default` — monospace, IDE-like
    - `tufte` — serif, book-like
  - Theme modes:
    - `dark` (default)
    - `light`
    - `auto`
  - Custom themes are done via CSS variables.
  - Theme choice can persist in `localStorage`.

- **Response format**
  - Returns an array of objects like:
    ```ts
    interface Response {
      id: string;
      value: string | string[];
      attachments?: string[];
    }
    ```
  - Attachments are image paths attached to non-image questions.

- **File structure**
  - The repo is organized around:
    - `index.ts` tool entry point
    - `settings.ts`
    - `server.ts`
    - `schema.ts`
    - `form/` with HTML, CSS, themes, and JavaScript

- **Limits**
  - Max 12 images per submission
  - Max 5MB per image
  - Max 4096×4096 pixels
  - Allowed formats: PNG, JPG, GIF, WebP

### Assessment
This is a **mixed** technical/reference page with some tutorial elements. Durability is **medium**: the general patterns around interactive forms, autosave, and schema-driven prompts are fairly stable, but specifics like `pi-agent` versions, extension APIs, default ports, model names, and feature support will age as the project evolves. Density is **high** because it packs installation steps, API usage, schema definitions, configuration, keyboard shortcuts, session behavior, and file layout into one document. Originality is **primary source** because it describes the tool authored in the repo rather than summarizing elsewhere. Reference style is **refer-back**: this is the kind of doc you’d revisit for schema fields, settings, shortcuts, and recovery/snapshot behavior. Scrape quality looks **good** overall; the page content appears complete, including code blocks, tables, and section structure, though images and the linked demo media are not embedded in the text itself.
