---
url: https://nolanlawson.com/2026/01/24/ai-tribalism/
title: AI tribalism | Read the Tea Leaves
scraped_at: '2026-04-12T07:31:58Z'
word_count: 1127
raw_file: raw/2026-04-12_ai-tribalism-read-the-tea-leaves_778c39b3.txt
tldr: Nolan Lawson argues that AI coding debates have become tribal and unhelpful, but his own 2025 experience with Claude Code and related tools convinced him that agentic LLM workflows are already materially changing software development.
key_quote: the breakthrough is already here; it just needs a bit more tinkering
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Nolan Lawson
- Steve Yegge
- Geoffrey Huntley
- Anil Dash
tools:
- Claude Code
- Cursor Bugbot
libraries: []
companies:
- Claude
- Cursor
tags:
- ai-coding
- llms
- software-development
- developer-tools
- tribalism
---

### TL;DR
Nolan Lawson argues that AI coding debates have become tribal and unhelpful, but his own 2025 experience with Claude Code and related tools convinced him that agentic LLM workflows are already materially changing software development.

### Key Quote
“the breakthrough is already here; it just needs a bit more tinkering”

### Summary
- The post is a reflection on how the author’s view of LLMs changed dramatically between 2024 and 2025:
  - A year earlier, he saw LLMs as “amusing toys” unsuitable for real software development.
  - By the time of writing, he estimates that “about 90%” of his code is authored by Claude Code.
- He describes the current AI discourse as increasingly tribal:
  - Online discussions on Hacker News, Mastodon, Bluesky, and Lobsters have turned into polarized camps.
  - The debate has shifted from technical evaluation into politics, and then into tribal identity.
- He explains his initial skepticism:
  - Early enthusiasm often came from people he trusted least on programming matters, including crypto promoters who moved from NFTs/monkey JPEGs to AI.
  - Meanwhile, respected engineers were unimpressed by hallucinations, buggy output, and weak autocomplete.
- He says something changed in 2025:
  - He does not know whether it was model improvements like “Opus 4.5,” reinforcement learning, or especially good product design in Claude Code.
  - The key shift was practical: it became more efficient to write markdown specs, refine them in plan mode, and let the model do the repetitive work.
- He argues that the tools are already useful despite remaining flaws:
  - They still make dumb mistakes and hallucinate.
  - But in his workflow, Cursor Bugbot catches bugs he would not have found himself.
  - Claude then fixes those bugs, creating a loop that makes him question what the programmer’s job even is.
- He takes ideas like Steve Yegge’s “Gas Town,” Geoffrey Huntley’s “Ralph loops,” and Anil Dash’s overview more seriously now:
  - He no longer dismisses them as fantasy.
  - In his view, chaining multiple agents together is already producing useful results in his own projects.
- He suggests the important breakthrough may already be behind us:
  - Models do not necessarily need to get much better.
  - Costs do not even need to fall.
  - Adding more agents and tooling may be enough to create a large, effective multi-agent coding system.
- He addresses common objections:
  - **Security**: agents have found vulnerabilities.
  - **Performance**: agents can write benchmarks and iterate on improvements.
  - **Accessibility**: agents are weak here, but prompting them explicitly and giving them browser access can make them better than the “median web dev.”
- He acknowledges the downsides:
  - Multi-agent workflows may be inefficient and environmentally costly.
  - He is not celebrating the end of the old way of working.
- The main takeaway is humility:
  - He thinks neither the hype, the doom, nor the resistance side truly knows what will happen next.
  - Developers should experiment, tinker, and stay curious.
  - He closes by asking for empathy because software development has already changed dramatically and will likely keep changing.

### Assessment
This is a **mixed** opinion essay and personal industry reflection, with a strong first-person stance and lots of concrete examples from the author’s own workflow. Its **durability is medium**: the core argument about tribalism and professional uncertainty will age well, but the specifics are tied to 2025-era tools like Claude Code, Cursor Bugbot, and model/version progress such as “Opus 4.5,” which may date it. The piece is **dense** and fairly specific, especially in its references to workflows, tools, and objections like security, performance, and accessibility. It is primarily **commentary**, not a neutral fact report or tutorial. For future use, it is best as a **refer-back** piece rather than a one-time skim, especially if you want a snapshot of how experienced developers were thinking about AI coding in early 2026. The **scrape quality is good**: the full text appears captured, with no obvious missing sections or code blocks.
