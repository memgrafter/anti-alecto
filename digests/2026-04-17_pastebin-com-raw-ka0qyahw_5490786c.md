---
url: https://pastebin.com/raw/kA0QyaHw
title: pastebin.com/raw/kA0QyaHw
scraped_at: '2026-04-17T05:26:22Z'
word_count: 733
raw_file: raw/2026-04-17_pastebin-com-raw-ka0qyahw_5490786c.txt
tldr: A strict internal “Plan Mode” prompt for codebase exploration that requires targeted search first, a YAGNI check, and a structured handoff plan instead of implementation.
key_quote: Read-only exploration and planning. Do NOT implement - just plan.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people: []
tools:
- rg
- read
- todo create
libraries: []
companies: []
tags:
- codebase-exploration
- planning-workflow
- yagni
- prompt-design
- developer-tools
---

### TL;DR
A strict internal “Plan Mode” prompt for codebase exploration that requires targeted search first, a YAGNI check, and a structured handoff plan instead of implementation.

### Key Quote
“Read-only exploration and planning. Do NOT implement - just plan.”

### Summary
- Defines a planning workflow for complex tasks where the assistant should **analyze and prepare** rather than code.
- Requires a specific sequence:
  - **Explore first** using targeted `rg` searches before reading full files.
  - **Run a YAGNI check** to see whether the request is already satisfied by existing behavior.
  - **Write context first** as a concise handoff summary.
  - **Output a numbered plan** under a `Plan:` header.
  - **Add implementation notes** with files, risks, and acceptance criteria.
- Emphasizes careful dependency tracing:
  - Search both **project source** and **dependency artifacts**.
  - Verify library defaults from installed package files rather than assuming behavior.
  - Trace the **full call path** to see what is actually thrown, returned, or transformed.
- YAGNI check rules are strict:
  - If evidence shows the request is already handled, **do not create a plan**.
  - Instead, start a short conversation and include an `Evidence` field with **specific citations** from tool output.
  - Must include **Unresolved Questions** when there may still be a gap.
- Required output structure for normal cases:
  - `Context & Assumptions`
  - `Plan:` with numbered steps
  - `Implementation Notes:` including files, risks/unknowns, and acceptance criteria
  - `Unresolved Questions` if anything remains ambiguous
- Step-writing constraints:
  - Each step must be **25 words max**
  - Use **imperative fragments only**
  - Include one reason or expected output per step
- Also specifies:
  - Default output is in chat, unless a filename is requested
  - TODO creation is optional and only when explicitly requested

### Assessment
Durability is **medium**: the planning principles and handoff structure are fairly timeless, but the prompt is tied to a specific assistant workflow and tooling conventions like `rg`, `read`, and `todo create`. Content type is **reference** and partly **tutorial**, since it documents a reusable internal procedure. Density is **high** because it packs many operational rules, formatting constraints, and decision branches into a short document. Originality is **primary source** if this is the actual prompt/configuration used by a system, not commentary. Reference style is **deep-study** for someone who needs to follow the workflow exactly, though it can also be skimmed for the required output template. Scrape quality is **good**: the full text appears captured, with no obvious missing sections, code blocks, or formatting gaps.
