---
url: https://github.com/calesennett/pi-codex-fast#
title: 'calesennett/pi-codex-fast: pi extension that enables priority service tier for OpenAI/OpenAI Codex requests.'
scraped_at: '2026-04-19T06:48:58Z'
word_count: 99
raw_file: raw/2026-04-19_calesennett-pi-codex-fast-pi-extension-that-enables-priority-service-tier-for-op_d15d3ca4.txt
tldr: 'pi-codex-fast is a small extension for the pi coding agent that lets you toggle a “fast” mode, which adds `service_tier: "priority"` to OpenAI/OpenAI Codex requests when enabled.'
key_quote: '“Fast-mode extension for [pi](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent) that injects `service_tier: "priority"` into OpenAI/OpenAI Codex requests.”'
durability: medium
content_type: reference
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- calesennett
tools:
- pi
libraries: []
companies:
- OpenAI
tags:
- coding-agent
- openai
- github-project
- cli-tool
- request-modification
---

### TL;DR
`pi-codex-fast` is a small extension for the `pi` coding agent that lets you toggle a “fast” mode, which adds `service_tier: "priority"` to OpenAI/OpenAI Codex requests when enabled.

### Key Quote
“Fast-mode extension for [pi](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent) that injects `service_tier: "priority"` into OpenAI/OpenAI Codex requests.”

### Summary
- `pi-codex-fast` is a GitHub project by `calesennett` for the `pi` coding agent.
- Its purpose is narrow and specific: it patches request payloads for OpenAI and OpenAI Codex so they include `service_tier: "priority"`.
- The extension exposes two ways to toggle it on/off:
  - Inside `pi`: `/codex-fast`
  - From the CLI: `pi --fast`
- State persistence:
  - Reads enabled/disabled state through `pi`’s `SettingsManager`
  - Global settings file:
    - `$PI_CODING_AGENT_DIR/settings.json`
    - or `~/.pi/agent/settings.json`
  - Project-local override:
    - `<cwd>/.pi/settings.json`
  - Uses the key `pi-codex-fast.enabled`
  - Writes are saved to the global settings file, matching `pi`’s default settings behavior
- Behavior is conditional and limited:
  - Only modifies requests if fast mode is enabled
  - Only applies when the active model provider is `openai` or `openai-codex`
  - All other requests are left unchanged
- The page is short and mostly documentation-style; the included screenshot is referenced but not described in detail.

### Assessment
Durability is medium: the core idea of a toggleable request modifier for a coding agent is fairly stable, but the specifics depend on `pi`, OpenAI provider names, and the `service_tier: "priority"` API field, which may change over time. Content type is reference/tool documentation. Density is medium: it’s concise but contains concrete commands, file paths, and exact behavior rules. Originality is primary source, since it documents the project’s own functionality rather than summarizing others. It’s best used as a refer-back reference for setup/behavior rather than deep study. Scrape quality is good for the text content, but the screenshot image itself isn’t inspectable here, so any UI details in it are effectively missing.
