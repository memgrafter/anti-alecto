---
url: https://nickdirienzo.com/what-s-left-when-ai-writes-the-code/
title: What's Left When AI Writes the Code
scraped_at: '2026-04-12T10:38:00Z'
word_count: 702
raw_file: raw/2026-04-12_what-s-left-when-ai-writes-the-code_109b9426.txt
tldr: The author argues that as AI coding tools get strong enough to write most code quickly, engineers’ highest-value work shifts to vision, architecture, and taste rather than manual implementation.
key_quote: 'the higher leverage stuff: vision, architecture, and taste.'
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Anthropic
tools:
- Claude Desktop Code
- Claude
- Coder
libraries: []
companies:
- Anthropic
tags:
- ai-coding
- software-engineering
- code-generation
- developer-productivity
- software-architecture
---

### TL;DR
The author argues that as AI coding tools get strong enough to write most code quickly, engineers’ highest-value work shifts to vision, architecture, and taste rather than manual implementation.

### Key Quote
“the higher leverage stuff: vision, architecture, and taste.”

### Summary
- The post argues that the software engineer’s job is being redefined: it is fundamentally about **solving problems with software**, not typing code.
- The author claims recent models like **Anthropic’s Opus 4.5** can generate code as well as a mid-level engineer and can compress work that would take weeks into minutes.
- Based on their own experience, the author says:
  - They’ve written only **5–10% of code** in the last couple of months.
  - In the last week, they **didn’t open an editor at all** and worked through **Claude Desktop Code**.
  - Their team saw an **80% increase in contributions to main** when comparing pre-Claude vs post-Claude data.
- The author identifies three areas that remain especially valuable for engineers:
  - **Vision**: defining what to build and why, including product differentiation and what not to build.
  - **Architecture**: choosing sound technical systems, balancing simplicity vs. overengineering, and ensuring technical decisions fit the business context.
  - **Taste**: making judgment calls about what “feels right,” especially in UX, developer experience, naming, and product flows.
- The author says current models can read docs, ADRs, and conversation history, but still lack the human empathy, product intuition, and contextual judgment that come from experience.
- They expect models to improve further in these higher-level areas, but don’t yet know what engineers should focus on once AI can handle them too.
- Their current workflow is heavily AI-assisted:
  - They give Claude planning/architecture guidance.
  - Claude auto-edits code while they mostly avoid reading it during development.
  - They act as **QA**, especially where automated testing can’t cover behavior.
  - They use **Coder** and **Claude Desktop’s Code feature** with **git worktrees** to run multiple projects in parallel.
  - They are increasingly open to more autonomous “yolo mode” because of how much Claude can already do.
- After development, they focus on:
  - Reviewing the **PR**
  - Recording architectural decisions in **ADRs**
  - Checking **data models** and **API contracts**
  - Doing only a cursory code review, then asking Claude to iterate on feedback
- The conclusion is a direct recommendation to engineers:
  - **Develop vision, architectural instincts, and taste**
  - The code-writing part is becoming easier
  - The judgment part is not, at least yet
- The author closes by saying they are **shipping faster than ever**.

### Assessment
This is a **mixed** opinion/experience-based piece with a strong argument about how AI changes engineering work. Its **durability is medium**: the core ideas about engineering judgment, architecture, and taste are fairly timeless, but the claims are tied to current AI tools, especially **Anthropic’s Opus 4.5** and **Claude Desktop Code**, which makes some details likely to age quickly. The **density is medium-high** because it packs concrete workflow details, tool names, and usage patterns into a short post. It is primarily **commentary** rather than a primary technical source, though it includes a few anecdotal metrics from the author’s own team. Best used as **refer-back** material if you want to revisit the author’s framing of AI-assisted software development and the skills they believe will matter most. The **scrape quality is good**: the full text appears captured, with no obvious missing sections, code blocks, or images.
