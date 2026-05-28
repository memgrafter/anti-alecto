---
url: https://www.youtube.com/watch?v=XP9Zg--DLr8
title: This leaked Anthropic interview is crazy - YouTube
scraped_at: '2026-04-12T18:55:30Z'
word_count: 11422
raw_file: raw/2026-04-12_this-leaked-anthropic-interview-is-crazy-youtube_62909cea.txt
tldr: A Coding Jesus commentary video uses a leaked Anthropic interview to dissect a C++/sampling-profiler coding problem, showing how misunderstanding call stacks, sampling, and stack-diff logic derailed the candidate.
key_quote: the key to understanding this is that you only need to care about the differences between the two
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Coding Jesus
- David
- Anthropic
- ByteDance
tools:
- Google
- secflow
- getcracked.io
libraries: []
companies:
- Anthropic
- ByteDance
tags:
- c-plus-plus
- sampling-profiler
- call-stacks
- interview-prep
- algorithms
---

### TL;DR
A Coding Jesus commentary video uses a leaked Anthropic interview to dissect a C++/sampling-profiler coding problem, showing how misunderstanding call stacks, sampling, and stack-diff logic derailed the candidate.

### Key Quote
“the key to understanding this is that you only need to care about the differences between the two”

### Summary
- **Source / framing**
  - YouTube video titled **“This leaked Anthropic interview is crazy”**
  - Creator repeatedly identifies himself as **Coding Jesus** and says he replicated the problem on **getcracked.io**
  - The video is presented as both:
    - a critique of a leaked Anthropic interview
    - a teaching example for how to solve the coding problem correctly

- **Interview context**
  - Candidate reportedly works at **ByteDance** and claims:
    - **10 years of C++ experience**
    - experience with **Golang, Python, React**
    - work on **large-scale distributed systems and cryptographic infrastructure**
    - **billions of requests per hour**
  - Interviewer is identified as **David** from Anthropic; he is described as patient and professional
  - Candidate is told he may use **Google and secflow**, but **no AI tools**

- **Problem being discussed**
  - Title/topic: **“Converting stack samples to a trace”**
  - Goal: convert periodic **sampling profiler** snapshots into a list of **start/end events** for visualization
  - Input:
    - a vector of samples
    - each sample has:
      - `ts` = timestamp
      - `stack` = function names from **outermost to innermost**
  - Output:
    - list of events with **three fields**:
      - `kind` = start or end
      - `timestamp`
      - `name`
  - The trace must be **properly nested**:
    - nested function starts after enclosing start
    - nested function ends before enclosing end

- **Key example details mentioned in the transcript**
  - Example trace timestamps include:
    - **7.5**
    - **9.2**
    - **10.7**
    - later hypothetical **12**
  - Example interpretation:
    - at **7.5**, `main` is running
    - at **9.2**, `main`, `my function`, and `my function 2` are running
    - at **10.7**, only `main` remains in the shown sample
  - The discussion emphasizes that a timestamp is a **snapshot in time**, not the duration of execution
  - A later hypothetical sample at **12** is used to show how an end event might be emitted when `main` disappears

- **Core technical lesson**
  - The solution idea is to compare **adjacent samples** and find the **first point of difference**
  - Everything that disappears between two samples should get an **end event**
  - Everything newly appearing should get a **start event**
  - Because of call-stack nesting:
    - removals should be processed **backwards** from inner to outer
    - additions should be processed **forwards** from outer to inner
  - The creator explicitly says the key is that you only need to care about the **mismatch** between two vectors
  - He mentions C++’s **`std::mismatch`** as the natural standard algorithm for this

- **Candidate mistakes highlighted in the video**
  - Would not clearly answer whether he knew what a **sampling profiler** or **call stack** was
  - Repeatedly misread or misinterpreted the problem statement
  - Assumed timestamps meant execution durations rather than snapshots
  - Proposed overly complicated data structures:
    - hash tables
    - vectors of active functions
    - sets with counts
  - Wrote code with multiple issues the creator mocks:
    - poor formatting
    - `int`/`size_t` style complaints
    - copies where references would be preferable
    - invalid indexing / loop bugs
    - use of `prev.size()` style mistakes
    - recursion concerns raised, then dismissed as not changing the core mismatch logic

- **Ending / interview meta**
  - The interviewer eventually explains the intended approach more directly
  - The video ends with the creator concluding the candidate hurt himself by pretending to know concepts he didn’t understand
  - The interviewer then asks a few general Anthropic questions about:
    - what the team does
    - speed vs safety
    - regulation and safety tradeoffs
  - Anthropic’s stated position in the clip:
    - **safety above all**
    - speed and quality are in service of safety

### Assessment
This is a **mixed** content piece: mostly **commentary** with a built-in **tutorial/technical walkthrough** of a specific interview problem. Durability is **medium** because the exact interview, candidate, and company context are time-bound, but the underlying ideas—sampling profilers, call stacks, stack-diffing, and nested event reconstruction—are durable. Density is **high**: the transcript contains lots of specific timestamps, code-review notes, and interview dialogue, though much of it is creator commentary rather than clean exposition. Originality is primarily **commentary** with some **synthesis** and a small amount of genuine technical explanation; it is not a primary technical source for the algorithm itself. Reference style is best as **refer-back** if you want the exact interview/problem framing, or **deep-study** only for the core algorithm idea. Scrape quality is **partial**: the transcript includes most of the spoken content, but not the visual code blocks/images in full, and some formatting/context from the YouTube video is necessarily missing.
