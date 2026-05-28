---
url: https://www.youtube.com/watch?v=YcT7gjzj2TU
title: The No-Rework Workflow for AI Coding Assistants - YouTube
scraped_at: '2026-04-19T06:46:57Z'
word_count: 11214
raw_file: raw/2026-04-19_the-no-rework-workflow-for-ai-coding-assistants-youtube_3bc025b1.txt
tldr: 'A live demo of the “No Vibes Allowed” workflow shows how the hosts use AI-assisted research, design docs, learning tests, and vertical planning to reduce rework before coding a feature for Riptide/Human Layer: changing message sending so Enter queues a message by default while preserving interrupt behavior.'
key_quote: The more assumptions that you can bake in ahead of time and the more correct your design is, the more likely it is that your implementation will be correct.
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Bipal
- Dexter
- Kyle
- Josh
- Joshy
- Alvaro
- David
- Russ
- Jensen
- Vib
tools:
- Claude Code
- Cloud Code
- Claude Agent SDK
- Storybook
- Code Rabbit
- Riverside
- Linear
libraries:
- BAML
companies:
- AI That Works
- Human Layer
- Google
- Amazon
tags:
- ai-coding
- software-design
- workflow
- testing
- architecture
---

### TL;DR
A live demo of the “No Vibes Allowed” workflow shows how the hosts use AI-assisted research, design docs, learning tests, and vertical planning to reduce rework before coding a feature for Riptide/Human Layer: changing message sending so Enter queues a message by default while preserving interrupt behavior.

### Key Quote
> “The more assumptions that you can bake in ahead of time and the more correct your design is, the more likely it is that your implementation will be correct.”

### Summary
- This is an episode of **AI That Works** with **Bipal** (co-host, works on **BAML**) and **Dexter** (co-host, works on **Human Layer / context engineering**).
- The segment is part of their recurring **“No Vibes Allowed”** format: a live, structured build session where they use AI tools to design and implement a real feature.
- The feature being built is for **Riptide** (their working title for the Human Layer IDE/workflow product):  
  - Today, pressing **Enter** while a session is running **interrupts** the agent.  
  - They want the default behavior to become **queueing a message** instead, while still allowing explicit interrupts.
- They show a simple example using **Claude Code / Cloud Code**:
  - Run `bash sleep 10`
  - Then send “when you’re done sleep again”
  - Desired behavior: the second message is queued and executed after the first completes.
- They emphasize using **learning tests / proofs** to understand opaque or closed-source behavior:
  - They had a test that didn’t verify queueing properly.
  - They added a test against the **Claude Agent SDK** in bypass permissions mode to observe actual JSON/output and confirm behavior.
  - The goal is to update the design doc with facts from the observed test output.
- Their core workflow philosophy:
  - **Do research first** so assumptions are correct before coding.
  - Use AI to generate **research docs**, **design discussions**, and **structured outlines** before implementation.
  - Prefer **vertical planning** over “horizontal planning”:
    - Horizontal planning = database, then service, then frontend, etc., with no testable slice until late.
    - Vertical planning = build a thin end-to-end slice early so you can validate each layer sooner.
- They describe several decision-making principles:
  - The more correct the design up front, the less backtracking later.
  - It’s better to catch mistakes in a small design doc than in a huge PR.
  - Keep the **frontend dumb** and consolidate logic in the backend.
  - Prefer simple, unified APIs over multiple specialized endpoints where possible.
- Specific design decisions discussed for the queueing feature:
  - They lean toward a **unified message-sending flow** rather than separate complicated paths.
  - They discuss whether queued messages should be stored in:
    - the existing conversation events table,
    - a separate queue/messages table,
    - or another structure.
  - They lean toward a cleaner **separate table / explicit lifecycle** approach for clarity and maintainability, though the discussion includes tradeoffs.
  - They want the UI to have:
    - a default **queue** action on Enter,
    - and a persistent **interrupt** action.
- They discuss how AI models behave in codebases:
  - Models are good at **pattern recognition** and tend to reproduce the dominant patterns in the repo.
  - Bad or inconsistent patterns in the codebase get reinforced if not corrected.
  - The team should **prune tool/skill sprawl** and maintain a smaller set of highly adopted workflows.
- They also talk about their broader development process:
  - Docs and plan files are **throwaway artifacts**; the code is the source of truth after shipping.
  - They sometimes send design docs to teammates like **Kyle** for review on high-stakes architecture decisions.
  - They use AI to surface missing/inconsistent parts of a plan before coding.
- The episode ends with:
  - A commitment to continue the implementation in a later session.
  - A teaser for the next episode: **PII redaction**, including both eval design and code design.

### Assessment
This is a **mixed** content piece: part live demo, part opinionated engineering talk, part workflow tutorial. Durability is **medium**: the high-level principles about design-first development, vertical planning, and learning tests are fairly timeless, but the details are tied to the current **Claude Code / Cloud SDK / Riptide** workflow and will age with those tools. Density is **medium-high** because it includes many concrete architectural decisions, workflow patterns, and example commands, though it is conversational and repetitive in places. Originality is best described as **commentary / primary-source demo**: it’s the hosts discussing and applying their own process live, not a synthesis of external sources. It’s best used as a **refer-back** reference if you’re interested in AI-assisted software workflow design, especially queueing/interrupt semantics and how they use design docs plus learning tests to reduce rework. Scrape quality is **partial**: the transcript captures a lot of the spoken content, but it’s still an auto-captured YouTube transcript with repetition, interruptions, and likely missing visual context from the live demo and on-screen artifacts.
