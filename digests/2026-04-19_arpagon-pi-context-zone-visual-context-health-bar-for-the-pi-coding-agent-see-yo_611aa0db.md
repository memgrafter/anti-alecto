---
url: https://github.com/arpagon/pi-context-zone
title: 'arpagon/pi-context-zone: Visual context health bar for the Pi coding agent — see your smart/warm/dumb zone at a glance'
scraped_at: '2026-04-19T07:45:09Z'
word_count: 882
raw_file: raw/2026-04-19_arpagon-pi-context-zone-visual-context-health-bar-for-the-pi-coding-agent-see-yo_611aa0db.txt
tldr: A small Pi extension that adds a context “health bar” to show when your AI coding session is in the smart, warm, or dumb zone, based on research about long-context reasoning degradation.
key_quote: “LLMs don't degrade gracefully as their context fills up — they hit cliffs.”
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Dex Horthy
tools:
- Pi coding agent
- pi-context-zone
libraries: []
companies:
- HumanLayer
- Anthropic
- Chroma Research
tags:
- ai-coding
- context-window
- llm-reliability
- developer-tools
- long-context-reasoning
---

### TL;DR
A small Pi extension that adds a context “health bar” to show when your AI coding session is in the smart, warm, or dumb zone, based on research about long-context reasoning degradation.

### Key Quote
“LLMs don't degrade gracefully as their context fills up — they hit cliffs.”

### Summary
- **What this project is**
  - `pi-context-zone` is a Pi coding agent extension that displays a single-line visual status bar in the footer.
  - It helps you see how much context remains and which “zone” you are in:
    - **🧠 Smart**: 0–40%
    - **⚠️ Warm**: 40–70%
    - **🧟 Dumb**: 70%+
- **Installation**
  - Install via Pi package command:
    - `pi install npm:pi-context-zone`
  - Or load directly with:
    - `pi -e ./index.ts`
- **What it shows**
  - A progress bar with dividers at **40%** and **70%**
  - A **green → yellow → red** color gradient as context fills
  - A zone label: **smart / warm / dumb**
  - A remaining percentage indicator
  - Updates automatically after each turn, after compaction, and at session start
- **Why it exists**
  - The author argues that AI coding agents do not simply “forget” as context grows; instead, their **reasoning quality collapses** past certain thresholds.
  - This is framed as **context rot**: instruction drift, shallow pattern matching, hallucinations, and debug loops that get worse as the conversation length increases.
- **Research framing and claims**
  - The README cites Dex Horthy / HumanLayer and says the “dumb zone” idea comes from analysis of **100,000+ developer sessions**.
  - It treats **~40% context utilization** as a common inflection point where agents start degrading.
  - It presents a March 2026 table of model behavior on **MRCR v2 (8-needle)**, emphasizing that the benchmark measures **reasoning quality**, not just retrieval.
  - Claimed examples:
    - **Claude Opus 4.6**: ~78% at 1M tokens, described as the most resilient
    - **GPT-5.4**: 37% at 1M
    - **Gemini 3.1 Pro**: 26% at 1M
    - **DeepSeek V3**: 95% at 128K
  - The README concludes that even the strongest models still degrade, so **40% is a conservative universal default**.
- **Why context rot happens**
  - **Attention dilution**: fixed attention budget is spread thinner
  - **Lost in the middle**: models remember beginnings and ends better than middle context
  - **Trajectory poison**: prior model mistakes and corrections pollute the conversation history
  - **KV cache compression**: older context gets compressed and loses important “why” information
- **What to do when the bar turns yellow/red**
  - **Compact** with `/compact`
  - Start a **new session** using the suggested **RPI workflow**: Research → Plan → Implement
  - Use **sub-agents** for isolated exploration
- **Configuration defaults**
  - Smart → Warm: **40%**
  - Warm → Dumb: **70%**
  - Bar width: **20 chars**
  - These are described as **model-agnostic defaults**
- **References and provenance**
  - The README is heavily reference-driven, citing:
    - “No Vibes Allowed” talk by Dex Horthy
    - Chroma Research on context rot
    - MRCR v2 benchmark
    - “Lost in the Middle”
    - Anthropic Claude Opus 4.6 technical report
    - 12-Factor Agents
  - The project is an **MIT-licensed** open-source utility

### Assessment
This is a **mixed** content piece: part tool README, part opinionated technical explanation, part research summary. Its **durability is medium** because the core idea of context degradation is likely to stay relevant, but the model comparisons and March 2026 benchmark claims are version- and time-sensitive. The **density is high**: it packs installation instructions, UX behavior, thresholds, a conceptual framework, benchmark tables, and citations into a compact README. It is mostly a **primary-source project description** with strong **commentary/synthesis** around third-party research rather than original experimental reporting. As a reference, it is best for **skim-once to refer-back** use: enough to identify the tool quickly and understand its rationale, but not a deep technical spec. **Scrape quality is good** for the text provided; no obvious code blocks or major sections appear missing, though the repository may contain implementation details not shown here.
