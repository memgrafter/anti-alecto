---
url: https://github.com/badlogic/pi-mono/pull/903/files
title: 'Add support for intercepting bash by mitsuhiko · Pull Request #903 · badlogic/pi-mono'
scraped_at: '2026-04-16T03:51:44Z'
word_count: 4913
raw_file: raw/2026-04-16_add-support-for-intercepting-bash-by-mitsuhiko-pull-request-903-badlogic-pi-mono_0671578c.txt
tldr: This PR adds a `before_bash_exec` extension hook to intercept, rewrite, block, or retarget bash commands, then refines the API across three patches by removing the initial `errorMessage` return path in favor of `content` + `isError`, plus shell option reuse and a `executedCommand` record for rewritten commands.
key_quote: 'Return a `BashExecOverrides` object to override fields, or return `{ block: true, reason?: string }` to reject the command.'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Armin Ronacher
tools:
- uv
libraries:
- '@mariozechner/pi-coding-agent'
- '@mariozechner/pi-agent-core'
- '@mariozechner/pi-ai'
companies:
- badlogic
tags:
- bash-execution
- extension-hooks
- api-design
- shell-automation
- developer-tools
---

### TL;DR
This PR adds a `before_bash_exec` extension hook to intercept, rewrite, block, or retarget bash commands, then refines the API across three patches by removing the initial `errorMessage` return path in favor of `content` + `isError`, plus shell option reuse and a `executedCommand` record for rewritten commands.

### Key Quote
"Return a `BashExecOverrides` object to override fields, or return `{ block: true, reason?: string }` to reject the command."

### Summary
- **Patch 1/3: new bash interception API**
  - Introduces a new extension event: `before_bash_exec`.
  - This event fires before bash execution for both tool-driven bash and user `!` / `!!` bash.
  - Extensions can:
    - rewrite `command`
    - override `cwd`, `env`, `shell`, `args`, `timeout`
    - block execution with `{ block: true, reason?: string }`
  - Adds `BashExecEvent`, `BeforeBashExecEvent`, `BashExecOverrides`, and `BeforeBashExecEventResult` types.
  - Wires the event into both:
    - `AgentSession.executeBash(...)`
    - `wrapToolWithExtensions(...)` for the `bash` tool
  - Extends bash execution plumbing to pass shell settings, environment, cwd, and timeout through to `executeBash` / `executeBashWithOperations`.
  - Adds docs and an example extension at `packages/coding-agent/examples/extensions/uv.ts` that:
    - blocks `pip` usage
    - rewrites `python` commands to `uv run python ...`
    - appends a hint when Python import errors appear
  - Patch 1 also briefly adds `tool_result` support for returning `errorMessage` to override tool failures or force failures.

- **Patch 2/3: API cleanup and reuse**
  - Removes the `errorMessage` field from `ToolResultEventResult`.
  - Replaces that approach with:
    - `content: [...]`
    - `isError: true`
  - Updates docs and README examples accordingly.
  - Refines the `uv.ts` example to return `isError: true` instead of `errorMessage`.
  - Adds `executedCommand?: string` to `BashExecutionMessage`, so session history can record the rewritten command separately from the original request.
  - `recordBashResult(...)` now accepts `executedCommand`.
  - Introduces `resolveShellExecutionOptions()` in `utils/shell.ts` to centralize shell/env resolution.
  - Reuses that helper in both `bash-executor.ts` and `tools/bash.ts`.

- **Patch 3/3: test fix**
  - Updates the failing test to mock `resolveShellExecutionOptions()` rather than `getShellConfig()`.
  - Confirms the shell-resolution refactor changed the test seam.

### Assessment
Durability is **medium**: the design pattern for intercepting and rewriting shell execution is broadly useful, but the exact API, file paths, and implementation details are tied to this project’s current extension system and will age with future refactors. Content type is **mixed** because it’s primarily a technical patch / API change with documentation updates and a small test adjustment. Density is **high**: the diff is packed with concrete types, hooks, and execution-path changes across multiple files. Originality is **primary source**: this is the patch itself, not a commentary or synthesis. Reference style is **refer-back** if you are implementing or auditing extension hooks, especially around `before_bash_exec`, `resolveShellExecutionOptions()`, and `executedCommand`; otherwise it’s a skim-once change log. Scrape quality is **good**: the provided content includes all three patch fragments and enough surrounding context to reconstruct the evolution, though the final API supersedes the initial `errorMessage` documentation and that versioning should be read carefully when using this as a reference.
