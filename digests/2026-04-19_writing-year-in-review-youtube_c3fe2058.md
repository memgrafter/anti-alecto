---
url: https://www.youtube.com/watch?v=U45RZNVOGwM
title: Writing "Year in Review" - YouTube
scraped_at: '2026-04-19T08:19:27Z'
word_count: 6209
raw_file: raw/2026-04-19_writing-year-in-review-youtube_c3fe2058.txt
tldr: A livestream-style walkthrough of how the author is assembling a 2025 “year in review” post by combining a BlueSky archive dump, GitHub repository history, dictation, and coding agents, while reflecting on projects like Boxy, Cards for Ukraine, and the Wipe Tunnel hackathon.
key_quote: “nobody knows yet how to do this properly. We are all just throwing [ __ ] at the wall, declaring victory while secretly crying over all the tech debt”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Peter Steinberger
- Armen Ron
tools:
- BlueSky
- GitHub CLI
- Google Drive
- Whisper Flow
- Claude
- ChatGPT
- VS Code
libraries: []
companies: []
tags:
- year-in-review
- coding-agents
- dictation
- personal-projects
- static-site-generation
---

### TL;DR
A livestream-style walkthrough of how the author is assembling a 2025 “year in review” post by combining a BlueSky archive dump, GitHub repository history, dictation, and coding agents, while reflecting on projects like Boxy, Cards for Ukraine, and the Wipe Tunnel hackathon.

### Key Quote
“nobody knows yet how to do this properly. We are all just throwing [ __ ] at the wall, declaring victory while secretly crying over all the tech debt”

### Summary
- The video is a live drafting session for a 2025 year-in-review blog post.
- The author describes a workflow that:
  - downloads all 2025 BlueSky posts and images,
  - filters them into monthly text dumps,
  - uses coding agents to extract structured project summaries,
  - merges those summaries into a markdown file,
  - combines that with GitHub repositories created during the year.
- The BlueSky scrape reportedly surfaced **83 different projects**.
- The author notes they may also use GitHub CLI to enumerate:
  - repositories created in 2025,
  - possibly repositories they contributed to, including **Wipe Tunnel** in another organization.
- The blog system is custom:
  - static files / static site generator,
  - markdown with embedded JavaScript,
  - hot reload for immediate preview.
- Writing workflow:
  - used to write posts by hand until around **June 2025**,
  - then built a dictation app,
  - paired it with a coding agent that can edit files, search the internet, and help turn speech into blog paragraphs,
  - insists the agent only fix grammar/spelling and preserve tone unless explicitly asked to tighten text.
- The author frames the year as a mix of:
  - technical work,
  - activism-related work,
  - general “bullshittery.”
- They mention a gap in February/March contributions due to hospitalization and recovery.
- Major project highlights discussed:
  - **Boxy**: an always-offline audio player for their child; they learned PCB design, soldering SMT parts, ordering boards from China, and built a system with about **72 cartridges**.
  - They mention their own dictation tool **Yakadi** (not open source) and compare it to Whisper Flow.
  - They want to embed a video from the related Boxy post and mention a Doom port to an embedded system.
  - **Cards for Ukraine**: the association crossed **€300,000**; the transcript later mentions **two batches** sent in **May (190 cards)** and **October (308 cards)** to Ukrainian families in Austria.
  - They plan to use a Google Drive sheet to verify batch counts and sizes.
  - **Messing with AI**: the author says they’ve been experimenting with LLMs since **early 2023**, and that 2025 saw a shift toward terminal-based coding agents in “YOLO mode.”
  - They describe a hackathon in **Vienna** at Peter Steinberger’s flat with **Armen Ron**, which produced **Wipe Tunnel**.
- The Wipe Tunnel section is presented as a story of collaborative, improvised “ad hoc wipe engineering”:
  - the three participants split modules,
  - the project was a Frankenstein system,
  - they later considered turning it open source,
  - Peter later made a better successor (the title is transcribed unclearly as “Claude this” / similar, so that name is uncertain).
- The author closes with a broad assessment of agentic coding:
  - no one really knows how to do it properly yet,
  - people are still “throwing [ __ ] at the wall,”
  - tools are useful but still introduce tech debt and unpredictability.

### Assessment
**Durability:** medium. The general workflow ideas around archiving social posts, using dictation, and using coding agents will age well, but the specific project names, counts, and tooling details are tied to 2025 and current personal context. **Content type:** mixed, mostly tutorial/process notes plus personal year-in-review commentary. **Density:** high, because the transcript is packed with concrete project names, counts, dates, tools, and implementation details, even though it is messy and conversational. **Originality:** primary source, since this is the author speaking about their own workflow, projects, and opinions. **Reference style:** refer-back; best used to confirm what projects, numbers, and tools were mentioned, or to revisit the author’s workflow for assembling the post. **Completeness / scrape quality:** partial and noisy. The transcript captures the main arc, but it has many speech-recognition glitches, bracketed omissions, and uncertain names; some titles and phrases are unreliable, especially “Claude this” and a few project labels.
