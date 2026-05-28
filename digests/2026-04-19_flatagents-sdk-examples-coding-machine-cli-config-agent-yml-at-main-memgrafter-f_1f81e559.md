---
url: https://github.com/memgrafter/flatagents/blob/main/sdk/examples/coding_machine_cli/config/agent.yml
title: flatagents/sdk/examples/coding_machine_cli/config/agent.yml at main · memgrafter/flatagents
scraped_at: '2026-04-19T07:52:20Z'
word_count: 382
raw_file: raw/2026-04-19_flatagents-sdk-examples-coding-machine-cli-config-agent-yml-at-main-memgrafter-f_1f81e559.txt
tldr: 'A YAML config for a `flatagent` coding assistant named `cli-agent`, defining its system prompt, user input template, and four tools: `read`, `bash`, `write`, and `edit`.'
key_quote: You are an expert coding assistant. You have access to tools for reading files, writing files, executing bash commands, and making surgical edits.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- read
- bash
- write
- edit
libraries: []
companies: []
tags:
- configuration
- cli
- coding-assistant
- tool-use
- yaml
---

### TL;DR
A YAML config for a `flatagent` coding assistant named `cli-agent`, defining its system prompt, user input template, and four tools: `read`, `bash`, `write`, and `edit`.

### Key Quote
"You are an expert coding assistant. You have access to tools for reading files, writing files, executing bash commands, and making surgical edits."

### Summary
- This is a configuration file at `sdk/examples/coding_machine_cli/config/agent.yml` for the `flatagents` project.
- It declares:
  - `spec: flatagent`
  - `spec_version: "2.4.4"`
- Under `data`:
  - Agent name: `cli-agent`
  - Model: `default`
- The `system` prompt instructs the agent to behave as an expert coding assistant with access to:
  - file reading
  - file writing
  - bash command execution
  - precise edits
- It gives operational guidelines:
  - use `bash` for file operations like `ls`, `grep`, `find`
  - use `read` before editing files
  - use `edit` for surgical changes where old text must match exactly, including whitespace
  - use `write` only for new files or complete rewrites
  - keep responses concise
- The `user` prompt is templated as `{{ input.task }}`, meaning the agent receives a task string from upstream input.
- The `tools` section defines four function tools with explicit schemas and usage notes:
  - `read`
    - reads file contents
    - output truncates at 2000 lines or 50 KB
    - supports `offset` and `limit` for paging large files
  - `bash`
    - executes bash in the current working directory
    - returns stdout and stderr
    - output truncates at 2000 lines or 50 KB
    - optional timeout, default 30 seconds
  - `write`
    - creates or overwrites files
    - automatically creates parent directories
  - `edit`
    - replaces exact text in a file
    - requires an exact `oldText` match, including whitespace
- `metadata` describes it as:
  - `"CLI coding agent with read, write, bash, and edit tools"`
  - tags: `tool-use`, `cli`, `coding`

### Assessment
This is a high-durability reference/config file rather than a narrative document: its content is mostly structural and likely to remain useful as long as the `flatagents` spec and example layout stay similar, though the exact `spec_version: "2.4.4"` and tool descriptions could become stale if the project evolves. It is a mixed technical/reference artifact with high density because it packs prompt text, tool schemas, and agent behavior constraints into one file. The content is original configuration/primary source material, useful as a refer-back reference if you need to understand how this CLI agent is supposed to operate. Scrape quality looks good: the YAML content appears complete, including metadata and tool definitions, with no obvious missing sections.
