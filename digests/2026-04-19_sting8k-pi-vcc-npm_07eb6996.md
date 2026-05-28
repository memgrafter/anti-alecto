---
url: https://www.npmjs.com/package/@sting8k/pi-vcc
title: '@sting8k/pi-vcc - npm'
scraped_at: '2026-04-19T07:33:45Z'
word_count: 918
raw_file: raw/2026-04-19_sting8k-pi-vcc-npm_07eb6996.txt
tldr: A Pi agent extension that replaces LLM-based conversation compaction with deterministic, regex-driven extraction, preserving searchable raw history via `vcc_recall` while producing a compact transcript plus four semantic sections.
key_quote: No LLM calls — produces a brief transcript via extraction and formatting.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- pi
- vcc_recall
- /pi-vcc-recall
- /pi-vcc
libraries:
- '@sting8k/pi-vcc'
companies:
- npm
tags:
- conversation-compaction
- command-line-tools
- search-and-retrieval
- developer-productivity
- pi-agent
---

### TL;DR
`@sting8k/pi-vcc` is a Pi agent extension that replaces LLM-based conversation compaction with deterministic, regex-driven extraction, preserving searchable raw history via `vcc_recall` while producing a compact transcript plus four semantic sections.

### Key Quote
“No LLM calls — produces a brief transcript via extraction and formatting.”

### Summary
- **What it is**
  - An npm package for Pi: `@sting8k/pi-vcc`
  - Described as an “Algorithmic conversation compactor for Pi”
  - Inspired by VCC (View-oriented Conversation Compiler)

- **Core idea**
  - Instead of asking an LLM to summarize conversation history, it uses algorithmic extraction and formatting
  - Goal: make compaction deterministic, fast, cheap, and searchable

- **Why it exists**
  - The page contrasts Pi’s default compaction with `pi-vcc`:
    - **Method**: LLM-generated summary vs. algorithmic extraction
    - **Determinism**: non-deterministic / can hallucinate vs. same input = same output
    - **Token reduction**: variable vs. 35–99% on real sessions
    - **Latency**: waits for LLM call vs. 30–470 ms
    - **History after compaction**: gone vs. still searchable via `vcc_recall`
    - **Repeated compactions**: can lose information vs. sections merge and accumulate
    - **Cost**: burns tokens vs. zero API calls
    - **Structure**: free-form prose vs. brief transcript + 4 semantic sections

- **Reported performance**
  - Measured on real session JSONLs under `~/.pi/agent/sessions`
  - Example reductions and times:
    - Session A: 2,943 messages, 997,162 chars → 7,959 chars, 99.2% reduction, 64 ms
    - Session B: 1,703 messages, 428,334 → 7,762, 98.2%, 29 ms
    - Session C: 1,657 messages, 424,183 → 9,577, 97.7%, 54 ms
    - Session D: 1,004 messages, 2,258,477 → 4,439, 99.8%, 30 ms
    - Session E: 486 messages, 295,006 → 11,163, 96.2%, 30 ms
    - Smaller sessions showed lower reduction:
      - Session F: 46 messages, 35.7% reduction, 5 ms
      - Session G: 27 messages, 71.0% reduction, 2 ms

- **Features**
  - **No LLM**: purely algorithmic, no extra API cost
  - **Brief transcript**: chronological flow with tool calls collapsed to one-line references like `(#N)`
  - **5 semantic sections**:
    - Session Goal
    - Files & Changes
    - Commits
    - Outstanding Context
    - User Preferences
  - **Bounded merge**: sections are recapped after merging so they don’t grow without limit
  - **Lossless recall**: `vcc_recall` reads raw JSONL so old history remains searchable
  - **Regex search**: supports patterns like `hook|inject` and `fail.*build`
  - **Result ranking**: relevance-ranked search, with rarer terms weighted more heavily
  - **Slash command**: `/pi-vcc-recall` searches history and can auto-feed results to the agent
  - **Fallback cut**: still works when Pi core returns nothing to summarize
  - **Manual compaction**: `/pi-vcc`

- **Installation**
  - Via npm package:
    - `pi install npm:@sting8k/pi-vcc`
  - Via GitHub:
    - `pi install https://github.com/sting8k/pi-vcc`
  - Try without installing:
    - `pi -e https://github.com/sting8k/pi-vcc`

- **Usage**
  - Registers a `session_before_compact` hook
  - When Pi triggers compaction, `pi-vcc` supplies the summary
  - Manual compaction: `/pi-vcc`
  - Search older history: `vcc_recall`
  - Search and feed results to the agent: `/pi-vcc-recall <query> [page:N]`
  - Tip: typing `/recall` autocompletes to `/pi-vcc-recall`

- **Compacted message structure**
  - Shows an example summary format with bracketed sections:
    - `[Session Goal]`
    - `[Files And Changes]`
    - `[Commits]`
    - `[Outstanding Context]`
    - `[User Preferences]`
  - Example content includes:
    - Fix auth bug in login flow
    - Modified `src/auth/session.ts`
    - Created `tests/auth-refresh.test.ts`
    - Commit `a1b2c3d`
    - Outstanding lint failure on line 42
    - User preferences like “Prefer Vietnamese responses” and “Always run tests before committing”

- **How compaction works internally**
  - Normalizes raw Pi messages into uniform blocks
  - Filters system messages and empty blocks
  - Builds sections from goals, file paths, blockers, preferences
  - Produces a brief transcript with tool calls collapsed
  - Merges with previous summaries using sticky/volatile rules:
    - Session Goal and User Preferences are concise and sticky
    - Outstanding Context is fresh-only and replaced
    - Files and Changes, Commits are unique unions
    - Transcript is a rolling ~120-line window

- **Recall / search details**
  - `vcc_recall` bypasses Pi’s normal compaction loss by reading the raw session JSONL directly
  - Supports:
    - Simple ranked search by query terms
    - Regex patterns
    - Pagination (`page: 2`)
    - Browsing recent entries with no query
    - Expanding specific indices for full content
  - Important limitation:
    - It can only recover what was actually saved in JSONL; it cannot recover text Pi already truncated at save time

- **Debugging**
  - Debug logging is off by default
  - Can be enabled in `~/.pi/agent/pi-vcc-config.json` with:
    - `{ "debug": true }`
  - Writes detailed debug info to `/tmp/pi-vcc-debug.json`

- **Related / metadata**
  - Related work: VCC and Pi
  - License: MIT

### Assessment
This is a **tool/reference** page with some implementation detail and usage documentation. Durability is **medium**: the core ideas about deterministic compaction and searchable session history are fairly stable, but the exact Pi hook names, slash commands, performance numbers, and file paths are version- and ecosystem-dependent. Density is **high** because it includes feature lists, real session benchmarks, installation commands, internal pipeline notes, and data structure examples. Originality is mostly **primary source** for the package itself, though it also contains marketing-style comparison claims and a nod to the original VCC project. As a reference, it is best for **refer-back** use when installing, configuring, or recalling search/compaction behavior; it is not just a skim-once announcement. Scrape quality is **good**: the page content, examples, install commands, feature descriptions, pipeline notes, and debug/docs sections are present, though any interactive npm page elements or hidden formatting may not be fully represented.
