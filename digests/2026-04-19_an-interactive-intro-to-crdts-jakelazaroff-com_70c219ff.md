---
url: https://jakelazaroff.com/words/an-interactive-intro-to-crdts/
title: An Interactive Intro to CRDTs | jakelazaroff.com
scraped_at: '2026-04-19T07:11:10Z'
word_count: 3480
raw_file: raw/2026-04-19_an-interactive-intro-to-crdts-jakelazaroff-com_70c219ff.txt
tldr: This article gives an interactive, TypeScript-based introduction to state-based CRDTs by implementing a Last Write Wins Register and then composing it into a Last Write Wins Map, with emphasis on merging rules, tombstones, and collaborative app behavior.
key_quote: “Peers may have different states at different points in time, but are guaranteed to eventually converge on a single agreed-upon state.”
durability: high
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Jake Lazaroff
tools:
- TypeScript
libraries: []
companies:
- Recurse Center
- Google Docs
- Figma
tags:
- crdts
- distributed-systems
- typescript
- collaborative-editing
- data-structures
---

### TL;DR
This article gives an interactive, TypeScript-based introduction to state-based CRDTs by implementing a Last Write Wins Register and then composing it into a Last Write Wins Map, with emphasis on merging rules, tombstones, and collaborative app behavior.

### Key Quote
“Peers may have different states at different points in time, but are guaranteed to eventually converge on a single agreed-upon state.”

### Summary
- The post is the first in a series aimed at readers who have heard of CRDTs but want an accessible, code-oriented explanation without heavy math or academic framing.
- It focuses specifically on **state-based CRDTs** and introduces the core idea: peers can update locally, sync later, and still converge.
- CRDTs are framed as data structures with:
  - a **value** (`T`) the app uses,
  - a **state** (`S`) carrying synchronization metadata,
  - a **merge(state)** function for reconciling remote state.
- The merge function must satisfy:
  - **commutativity**
  - **associativity**
  - **idempotence**
- The article contrasts **state-based** vs **operation-based** CRDTs:
  - state-based transmits full state and merges
  - operation-based transmits actions but requires exactly-once, causally ordered delivery
- First concrete example: **Last Write Wins Register (LWW Register)**:
  - stores a single value with metadata `[peer, timestamp, value]`
  - `set(value)` increments the local logical timestamp and records the local peer ID
  - `merge(...)` keeps whichever state has the higher timestamp; ties are broken by peer ID
  - the article explains this with interactive scenarios involving network loss, latency, and simultaneous writes
- Second example: **Last Write Wins Map (LWW Map)**:
  - a map composed of LWW Registers, one per key
  - `value` is exposed as a plain object of key/value pairs
  - `state` is a map from keys to the full register state
  - `merge` iterates over incoming keys and delegates to each child register’s `merge`
- The article emphasizes **composition** as the key CRDT design pattern:
  - complex CRDTs are built by nesting smaller ones
  - parent CRDTs mostly route state slices to child CRDTs
- The map implementation includes typical map-like methods:
  - `set(key, value)`
  - `get(key)`
  - `delete(key)`
  - `has(key)`
- Important deletion detail:
  - deletion is implemented by setting the register value to `null`, not by removing the key
  - this leaves a **tombstone** so peers can distinguish “deleted” from “never seen”
  - removing keys outright can cause deleted keys to reappear incorrectly during sync
- The article notes a key limitation of CRDTs:
  - they are **monotonically increasing** in the sense that metadata accumulates
  - you can hide deleted data from the app, but the underlying state still retains the tombstone
- It ends by pointing to the next installment, which will use these CRDTs to build a **collaborative pixel art editor**.

### Assessment
This is a high-durability tutorial/reference hybrid: the conceptual CRDT material is broadly durable, but the TypeScript examples and interactive demos are tied to the article’s specific implementation and could age as libraries or best practices evolve. It’s a mixed content type, but primarily tutorial with explanatory reference value. Density is high because it includes concrete algorithms, type signatures, merge rules, and full class code for both `LWWRegister` and `LWWMap`. The piece is original explanatory work rather than a synthesis of external sources, though it includes footnotes and references to broader CRDT research. It’s best used as a refer-back resource if you want to understand or reimplement the patterns, not just a skim-once overview. Scrape quality is good overall: the main prose and code are present, though the interactive demos and visual examples are not captured beyond textual description.
