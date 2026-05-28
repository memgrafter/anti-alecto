---
url: https://www.youtube.com/watch?v=CQmI4XKTa0U
title: How AI will change software engineering – with Martin Fowler - YouTube
scraped_at: '2026-04-19T07:15:06Z'
word_count: 22189
raw_file: raw/2026-04-19_how-ai-will-change-software-engineering-with-martin-fowler-youtube_e381c7d5.txt
tldr: Martin Fowler argues that AI is the biggest shift in software engineering of his career because it moves the field from deterministic to non-deterministic systems, making prototyping, legacy-code understanding, and tight feedback loops more valuable while making vibe coding, blind trust, and shallow workflows risky.
key_quote: the biggest part of it is the shift from determinism to non-determinism
durability: high
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Martin Fowler
- Kent Beck
- Rebecca Parsons
- Daryl Smith
- Jim Odell
- James Lewis
- Unmesh Joshi
- Grady Booch
- Bob Martin
- Alistair Cockburn
- Daniel Kahneman
- Robert Caro
- Robert Moses
- Simon Willis
- Bita
tools:
- Thoughtworks Technology Radar
- Statsig
- Linear
- Cursor
- ReSharper
- Visual Studio
- Xcode
- Cloud Code
- MCP
- ClickHouse
- Ruby
- Smalltalk
libraries: []
companies:
- Thoughtworks
- Statsig
- Linear
- JetBrains
- Microsoft
- Apple
- AWS
- Google Cloud
- Uber
- American Express
- Federal Reserve
tags:
- software-engineering
- artificial-intelligence
- refactoring
- agile
- enterprise-software
---

### TL;DR
Martin Fowler argues that AI is the biggest shift in software engineering of his career because it moves the field from deterministic to non-deterministic systems, making prototyping, legacy-code understanding, and tight feedback loops more valuable while making vibe coding, blind trust, and shallow workflows risky.

### Key Quote
"the biggest part of it is the shift from determinism to non-determinism"

### Summary
- Martin Fowler says the AI transition is the biggest change he has seen in software, comparable to the shift from assembly language to early high-level languages like COBOL and Fortran.
- His core thesis: AI introduces **non-determinism** into software engineering, which changes how developers must think about:
  - testing
  - refactoring
  - code review
  - system design
  - trust and verification
- He defines **vibe coding** as useful for:
  - exploratory work
  - throwaway prototypes
  - disposable tools
  - non-developers experimenting with code
  but not for long-lived software, because it removes the learning loop and produces hard-to-modify code.
- He emphasizes that AI tools can speed up software work, but the main value comes from **learning and feedback loops**, not from blindly accepting output.
- He warns that LLMs can “lie” or confidently produce wrong output, so developers must “trust, but verify.”
- He sees especially strong value in AI for:
  - understanding legacy systems
  - analyzing codebases with semantic/graph-based approaches
  - generating prototypes quickly
  - exploring unfamiliar APIs, languages, or environments
  - helping create initial skeleton projects
- He says Thoughtworks’ **Technology Radar** is a bottom-up internal process:
  - engineers submit “blips”
  - the Doppler group reviews them
  - the company publishes the result publicly
  - it reflects what practitioners are seeing across many client projects
- The radar currently includes many AI-related items because AI is highly active across the company’s projects.
- On AI and architecture/specification:
  - he thinks “spec-driven development” is only useful if it stays in **small, tight loops**
  - building a huge upfront specification is still too waterfall-like
  - the useful pattern is: small spec → build → test → deploy → iterate
- He believes LLMs may help developers build more rigorous shared languages or abstractions, similar to:
  - domain-driven design
  - ubiquitous language
  - DSLs
  - language workbenches
- On refactoring:
  - he wrote *Refactoring* after seeing Kent Beck perform extremely small, safe refactoring steps at Chrysler
  - he still sees refactoring as crucial, especially as AI produces more code that may “work” but be poorly structured
  - he expects refactoring to become more important, not less
- He explains why the second edition of *Refactoring* moved from Java to JavaScript:
  - Java examples had aged
  - JavaScript broadened the audience
  - it allowed a less object-oriented framing
- On design patterns:
  - he thinks patterns were valuable as a vocabulary for communication
  - their popularity declined partly because they were overused and partly because cloud platforms and managed services reduced the need to build certain infrastructure patterns from scratch
  - he still sees value in patterns for distributed systems and shared understanding
- On agile:
  - he was one of the 17 signers of the Agile Manifesto in 2001
  - he describes it as an attempt to make incremental, test-driven, customer-facing development more acceptable in organizations that preferred long upfront planning
  - he thinks agile has made real progress but remains far from the original vision
- On enterprise adoption:
  - large organizations are not monolithic
  - some pockets are highly experimental while others are extremely cautious
  - sectors like banking, government, airlines, and the Federal Reserve have very different constraints because of regulation, risk, and legacy systems
- He notes that the industry is currently in a strange macroeconomic period:
  - software layoffs are widespread
  - zero-interest-rate era has ended
  - AI is simultaneously creating excitement and bubble-like behavior
  - he sees AI as real, unlike some past hype cycles, but still highly uncertain in its long-term shape
- For junior engineers, his advice is:
  - use AI tools, but don’t rely on them blindly
  - find good senior mentors
  - ask AI to explain its reasoning and sources
  - learn to judge output quality through experience and review
- He believes the most important traits for excellent software engineers are still:
  - communication
  - collaboration
  - curiosity
  - the ability to understand user needs
  - the ability to work across the business/technical divide
- In the closing rapid-fire section, he recommends:
  - favorite language: **Ruby** currently, but **Smalltalk** as his love
  - book: **Thinking, Fast and Slow** by Daniel Kahneman
  - book: **The Power Broker** by Robert Caro
  - board game: **Concordia**

### Assessment
This is a high-durability, mixed content interview/podcast conversation with a strong opinion-and-practice orientation, plus some reference-value discussion of Thoughtworks Radar, refactoring, agile, and enterprise software culture. The density is high: it contains many specific claims, named people, historical references, and concrete examples of AI use cases and limitations. It is original commentary and firsthand perspective from Martin Fowler, not a synthesis. It is best used as a refer-back reference rather than a one-time skim, especially for readers tracking AI’s impact on software engineering, refactoring, and enterprise development. Scrape quality is partial: the transcript appears substantial, but it includes sponsor inserts and some transcription artifacts, with likely missing visual/contextual elements from the video.
