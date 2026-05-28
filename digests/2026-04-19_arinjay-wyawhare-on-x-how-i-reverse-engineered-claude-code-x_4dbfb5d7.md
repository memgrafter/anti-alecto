---
url: https://x.com/jaywyawhare/status/2033488305191616875?s=46
title: 'Arinjay Wyawhare on X: "How I Reverse Engineered Claude Code " / X'
scraped_at: '2026-04-19T06:57:43Z'
word_count: 1134
raw_file: raw/2026-04-19_arinjay-wyawhare-on-x-how-i-reverse-engineered-claude-code-x_4dbfb5d7.txt
tldr: A security-minded reverse-engineering writeup shows how Claude Code is packaged as a Bun single-executable app, how its minified JavaScript bundle and runtime prompts can be extracted and studied, and how feature flags/telemetry suggest Anthropic ships disabled features before publicly enabling them.
key_quote: The binary is packaging. The prompt is the product.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Arinjay Wyawhare
- Anthropic
tools:
- Bun
- Claude Code
- GrowthBook
- Statsig
- OpenTelemetry
- Datadog
- mitmproxy
libraries: []
companies:
- Anthropic
tags:
- reverse-engineering
- cli-tools
- feature-flags
- telemetry
- prompt-engineering
---

### TL;DR
A security-minded reverse-engineering writeup shows how Claude Code is packaged as a Bun single-executable app, how its minified JavaScript bundle and runtime prompts can be extracted and studied, and how feature flags/telemetry suggest Anthropic ships disabled features before publicly enabling them.

### Key Quote
“The binary is packaging. The prompt is the product.”

### Summary
- The author reverse engineered **Claude Code**, Anthropic’s CLI tool, because it is a **closed 213 MB binary** and they wanted to understand what it was actually doing.
- The analysis started with standard binary triage:
  - `file /opt/claude-code/bin/claude`
  - `readelf`
  - `strings`
- A key discovery was that the executable is a **Bun single executable application (SEA)**:
  - the binary contains the bundled **JavaScriptCore runtime**
  - the actual app logic is a **~9.88 MB minified JavaScript bundle** extracted from the ELF
- The author used **string searches** as an entry point into the minified code:
  - searching for **“You are Claude”** revealed the system prompt
  - searching for **`tengu_`** exposed a feature-flag namespace with hundreds of references
- The system prompt is described as **assembled dynamically from 15+ modular sections**, including:
  - identity
  - tone/style rules
  - task management
  - tool usage policy
  - security policy
  - code-reference formatting
  - dynamic sections like memory, environment, and MCP servers
- One notable finding is a **hidden minimal mode**:
  - setting `CLAUDE_CODE_SIMPLE=true` collapses the prompt to a single sentence
- The author found an internal feature-flag and telemetry system called **“Tengu”**:
  - about **37 feature flags**
  - about **560 telemetry events**
  - flags evaluated via **GrowthBook** with **Statsig fallback**
  - telemetry sent through **OpenTelemetry** to **Datadog** and Anthropic’s own analytics endpoint
- The code contained **gated features that were present but disabled**, including:
  - extended thinking modes
  - alternative model routing
  - experimental UI
  - cost optimization experiments
- To confirm the hypothesis, the author compared versions:
  - extracted and diffed **v2.1.33** against **v2.1.76**
  - found that features previously behind flags were **enabled or expanded** in the newer release
- The writeup argues that Anthropic **ships features in the binary weeks before public activation**, which the author treats as evidence that the flags are meaningful release gates rather than dead code.
- The author also notes operational/security findings:
  - the bash sandbox is **real**, with actual allow/deny and network restrictions
  - the binary has **no encryption, integrity checking, or anti-tamper**
  - it is **minified, not obfuscated**
- The broader conclusion:
  - **Claude Code is primarily a prompt delivery system**
  - the executable mostly provides plumbing for tools, context management, and API calls
  - the real product is the **carefully engineered prompt**
- The author briefly outlines related reverse-engineering approaches and their tradeoffs:
  - **mitmproxy** interception: good for runtime behavior, misses prompt architecture
  - **source maps** in early releases: cleaner but removed later
  - **runtime-behavior reconstruction**: thorough but speculative
  - **SDK monkey-patching**: logs API calls but is indirect

### Assessment
This is a **mixed** but mostly **technical / opinionated reverse-engineering report**, with high durability for the general methods and medium durability for the product-specific details, since version numbers like **v2.1.33** and **v2.1.76** will age quickly as Claude Code changes. The content is **dense** with concrete commands, offsets, flag counts, and architectural claims, and it reads as **primary-source commentary** based on the author’s own analysis rather than a synthesis of others’ work. It is best treated as **refer-back** material if you care about Bun single-executable apps, prompt architecture, or CLI reverse engineering. Scrape quality is **good** overall: the thread’s main narrative and most technical details are present, though the original formatting and any embedded visuals or code-context outside the quoted commands are naturally missing.
