---
url: https://github.com/badlogic/pi-mono/issues/104
title: 'ccusage compatibility for session logs · Issue #104 · badlogic/pi-mono'
scraped_at: '2026-04-16T03:52:16Z'
word_count: 309
raw_file: raw/2026-04-16_ccusage-compatibility-for-session-logs-issue-104-badlogic-pi-mono_9d585c42.txt
tldr: A closed GitHub issue asks for `ccusage` compatibility with Pi session logs, and the maintainer explains Pi uses its own log location/format while pointing to the session docs and `Usage` schema for adding support.
key_quote: I'm afraid this won't happen, as that would tie pi to whatever the Claude Code team does.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- arunsathiya
- badlogic
- ryoppippi
- mike1858
tools:
- ccusage
- Splitrail
libraries: []
companies:
- badlogic/pi-mono
- Piebald-AI
tags:
- github-issue
- usage-analysis
- session-logs
- claude-code
- developer-tools
---

### TL;DR
A closed GitHub issue asks for `ccusage` compatibility with Pi session logs, and the maintainer explains Pi uses its own log location/format while pointing to the session docs and `Usage` schema for adding support.

### Key Quote
"I'm afraid this won't happen, as that would tie pi to whatever the Claude Code team does."

### Summary
- **Issue:** `ccusage compatibility for session logs` on `badlogic/pi-mono` (#104), opened by `arunsathiya` and marked **closed**.
- **Problem raised:** `ccusage` analyzes Claude Code usage from local JSONL files, but it does not work with `pi-coding-agent` because Pi stores session logs in `~/.pi/` rather than `~/.claude/projects/`, and the format may differ.
- **Suggested fix in the issue:** either:
  - adopt a compatible log format/location, or
  - document Pi’s current format so `ccusage` can support it.
- **Related follow-up:** the reporter linked a corresponding `ccusage` issue requesting Pi support: `ryoppippi/ccusage#739`.
- **Maintainer response (`badlogic`):**
  - said Pi is unlikely to adopt Claude Code’s format because that would tie Pi to Claude Code’s design choices.
  - suggested it should be relatively simple for `ccusage` to add Pi support.
  - noted Pi session logs include full token counts and cost information.
- **Where the format is documented:** `packages/coding-agent/docs/session.md`.
- **How to parse logs:** iterate JSONL lines of type `message`, then inspect `message.usage`.
- **Example log shape shown:**
  - `{"type":"message","timestamp":"2024-12-03T14:00:02.000Z","message":{"role":"assistant", ... "usage": { ... } } }`
- **Usage schema shown in the thread:** an `Usage` interface with fields:
  - `input`
  - `output`
  - `cacheRead`
  - `cacheWrite`
  - `cost` object with:
    - `input`
    - `output`
    - `cacheRead`
    - `cacheWrite`
    - `total`
- **Important limitation:** the extracted content is visibly truncated right after the `cacheWrite` bullet, so the schema/details are incomplete in this scrape.
- **Later comment:** `mike1858` said they added Pi support to **Splitrail** (`Piebald-AI/splitrail`), a usage analyzer for agentic coding tools, and shared a screenshot.
- **Final reply from `arunsathiya`:** thanked them and said they would try Splitrail.

### Assessment
This is a **mixed** issue thread: part feature request, part maintainer clarification, and part ecosystem update. Its **durability** is medium—conceptually useful for understanding Pi’s log format and compatibility boundaries, but some specifics are tied to the current Pi and `ccusage` ecosystem. The **density** is medium-high because it includes concrete paths, links, log structure, and an interface definition, though the extracted text is **truncated** and the schema list is incomplete after `cacheWrite`, which reduces reliability for exact field lookup. The content is mostly **primary source** commentary from the maintainer plus issue participants, so it is useful for reference but not a full specification. Best used as a **refer-back** note when checking how Pi session logs are structured or why `ccusage` compatibility was discussed; for exact details, the linked session docs should be consulted because the scrape does not capture the full schema.
