---
url: https://news.ycombinator.com/item?id=47237460
title: An Interactive Intro to CRDTs (2023) | Hacker News
scraped_at: '2026-04-19T21:45:19Z'
word_count: 2912
raw_file: raw/2026-04-19_an-interactive-intro-to-crdts-2023-hacker-news_2601109f.txt
tldr: Hacker News discussion of “An Interactive Intro to CRDTs (2023)” that turns into a deep debate about whether CRDTs need unbounded tombstones/history, with commenters arguing over practical designs like eg-walker, Yjs, Automerge, Diamond Types, and whether central-server or hybrid approaches are often simpler.
key_quote: “In general, you don't really get to compact tombstones meaningfully without consensus”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: deep-study
scrape_quality: partial
people:
- Martin Kleppman
- Kevin Jahns
- Joseph Gentle
- Alex Good
- Mike Toomim
tools:
- Yjs
- Automerge
- Loro
- Diamond Types
- eg-walker
- Antimatter
- DocNode
- Fireproof
- Keyhive
- OT
libraries: []
companies:
- Figma
- Google Docs
- Ink & Switch
- Grafana
tags:
- crdt
- collaborative-editing
- tombstones
- local-first
- distributed-systems
---

### TL;DR
Hacker News discussion of *“An Interactive Intro to CRDTs (2023)”* that turns into a deep debate about whether CRDTs need unbounded tombstones/history, with commenters arguing over practical designs like eg-walker, Yjs, Automerge, Diamond Types, and whether central-server or hybrid approaches are often simpler.

### Key Quote
> “In general, you don't really get to compact tombstones meaningfully without consensus”

### Summary
- **Top comment (verbatim):** “In general, you don't really get to compact tombstones meaningfully without consensus so you really are pushing at least remnants of the entire log around to each client indefinitely.”
- **Top commenter:** not clearly labeled in the provided scrape
- **Thread topics:**
  - Whether CRDTs necessarily accumulate tombstones / unbounded history
  - Practical differences between list CRDT families: WOOT, RGA, YATA, Yjs, Automerge, Peritext, Loro, Cola
  - How eg-walker, Diamond Types, and Antimatter try to reduce storage/history costs
  - Whether CRDTs are the right tool versus a central server, OT, or hybrid systems
  - Real-world tradeoffs for collaborative apps like Figma, Google Docs, and agent conversation stores

- The discussion starts from the article on CRDTs, then quickly pivots into practical concerns about **local-first collaboration**, **order theory**, and the difficulty of modeling complex structures like calendar recurrences with exceptions.
- A major theme is the **tombstone/history problem**:
  - one side argues CRDTs often require preserving historical metadata indefinitely;
  - another side says this is overblown in practice, likening it to Git’s ever-growing history;
  - others point out that some applications really do suffer, especially when documents are cold-loaded frequently or when ephemeral data like cursor positions is stored inside the CRDT.
- Several CRDT implementation lineages are named:
  - **WOOT → RGA → YATA/Yjs → Peritext/Automerge → Loro**
  - **Cola** is mentioned as another recent Rust project
  - The “big libs” (**Yjs, Automerge, Loro**) are said to offer full document models
- Commenters contrast **state-based CRDTs** with **operation-based CRDTs** and mention **delta-CRDTs** as a way to send diffs instead of full state.
- **eg-walker / Diamond Types** are presented as a more flexible design:
  - use **relative positions** instead of stable GUIDs for insert locations
  - allow shallow-clone-like behavior
  - support merging by loading only the metadata needed back to the fork point
  - can often work by downloading the current snapshot plus whatever history is needed later
- **Antimatter** is mentioned as a distributed consensus protocol that can determine when it is safe to purge old metadata, even under network partitions.
- Some commenters argue that in many real collaborative apps, a **central server is the simpler and better fit**:
  - permissions and locking are cited as pain points for CRDTs
  - others counter that CRDTs are still useful between servers or in multi-master setups
  - a hybrid approach is suggested in places, such as **CRDTs between servers** and **OT or simpler comms between client and server**
- The thread also broadens into **schema evolution / distributed schemas**:
  - **Cambria** and **Thema** are cited as projects addressing distributed schema problems
- Another recurring point is that some CRDTs shine most clearly in specific data types:
  - counters
  - append-only structures
  - multi-value registers/maps
  - “non-destructive convergence” cases where operation order should not matter
- Later comments mention:
  - **Figma’s** old docs and tombstone GC issues
  - **Google Docs** and early sync bugs
  - **capability systems** such as **Keyhive**
  - a **hybrid CRDT/OT** strategy for AI agent conversation stores where ordering matters and latency is non-negotiable

### Assessment
This is a **mixed technical discussion** with high practical value if you’re studying collaborative data structures, local-first architecture, or CRDT implementation tradeoffs. **Durability is medium-high**: the core ideas about tombstones, causality, snapshots, and consensus are durable, but the named libraries and implementation details will age. **Content type** is mostly **opinion/commentary** layered on top of a technical article, with some tutorial-like pointers to projects and design patterns. **Density is high** because the thread is packed with concrete libraries, algorithms, and architecture claims, though it is conversational rather than structured. **Originality** is **commentary/synthesis**, not a primary source: it aggregates practitioner experience and opinions around the article’s topic. **Reference style** is **deep-study** if you’re evaluating CRDT architectures, or **refer-back** if you’re comparing specific libraries like Yjs, Automerge, Loro, Diamond Types, or eg-walker. **Scrape quality is partial**: the thread content appears reconstructed from multiple replies, but commenter ordering and handles are incomplete in places, so exact conversational context may be missing.
