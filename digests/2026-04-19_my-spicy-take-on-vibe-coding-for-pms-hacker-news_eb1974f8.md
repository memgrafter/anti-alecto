---
url: https://news.ycombinator.com/item?id=47240736
title: My spicy take on vibe coding for PMs | Hacker News
scraped_at: '2026-04-19T21:44:56Z'
word_count: 8608
raw_file: raw/2026-04-19_my-spicy-take-on-vibe-coding-for-pms-hacker-news_eb1974f8.txt
tldr: 'Hacker News thread about whether PMs should “vibe code” and land production diffs: the strongest pro-view says it helps PMs prototype and understand products, while the dominant anti-view says production code without engineering understanding creates hidden cleanup work, weak accountability, and quality risk.'
key_quote: “PM vibe coding a prototype for demonstration purposes? Might be a better use of a designer or engineers time, but okay I could see it being valuable. PM vibe coding something to ship to production? Your title is now engineer and you are responsible for your change...”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Robert C. Martin
tools:
- Claude
- Sourcegraph MCP
- Asana
- Agentic Coding by Microsoft
libraries: []
companies:
- Meta
- Google
tags:
- product-management
- vibe-coding
- ai-coding
- engineering-accountability
- tech-culture
---

### TL;DR
Hacker News thread about whether PMs should “vibe code” and land production diffs: the strongest pro-view says it helps PMs prototype and understand products, while the dominant anti-view says production code without engineering understanding creates hidden cleanup work, weak accountability, and quality risk.

### Key Quote
“PM vibe coding a prototype for demonstration purposes? Might be a better use of a designer or engineers time, but okay I could see it being valuable. PM vibe coding something to ship to production? Your title is now engineer and you are responsible for your change...”

### Summary
- **Top comment (verbatim):** “PM vibe coding a prototype for demonstration purposes? Might be a better use of a designer or engineers time, but okay I could see it being valuable. PM vibe coding something to ship to production? Your title is now engineer and you are responsible for your change, otherwise this is a direct path to destroying the quality of your product and the integrity of its data.”
- **Top commenter:** not explicitly identifiable from the provided text
- **Thread topics:**
  - Whether PMs should use AI coding tools for prototypes vs production changes
  - Accountability when a non-engineer ships code they can’t debug
  - Differences between “vibe coding” internal tools, demos, and public/production systems
  - Whether AI is collapsing the distinction between PM and engineer
  - Scrum, Agile, and who should own product direction in larger orgs

- The original post argues that encouraging PMs to code is often a bad incentive:
  - engineering teams are left to review/debug low-quality code they didn’t write
  - metrics like lines of code, commits, and tickets closed get gamed
  - leadership says it understands Goodhart’s Law but still rewards the wrong behaviors
  - business leadership pressure has, in the author’s view, reduced engineering quality and increased short-termism

- A major subthread compares US and European work norms:
  - several commenters argue unpaid on-call and late-hour culture are especially bad
  - others note US compensation can be much higher, but comes with more stress, weaker retirement safety nets, and more job insecurity
  - one commenter cites Google comp examples from Paris vs Seattle and the impact of taxes and cost of living
  - another points out Social Security/401(k) only partly mitigate retirement risk in the US

- The thread repeatedly draws a line between:
  - **low-risk/internal work**: PMs using AI to build prototypes, dashboards, internal tools, or demo apps
  - **high-risk/production work**: code that touches dangerous APIs, external users, or core systems, which should still require real engineering review

- One company comment describes a guardrail approach:
  - “Vibed stuff” can proceed with basic CI and agent instructions
  - anything crossing risk thresholds must be reviewed by an actual developer
  - costs are billed to the creator’s business unit
  - this reportedly works for internal tools, but nothing public has been shipped that way yet

- Another strong theme is that AI is changing the boundary between PM and engineering, but not eliminating accountability:
  - pro-AI commenters say PMs can now build quick proofs of concept, improve PRDs, and communicate ideas better
  - some say this will unlock long-tail improvements and internal alignment
  - several argue the best PMs already need technical intuition, and AI makes that more accessible
  - others say “shipping to production” without the ability to read/debug code is still irresponsible

- The thread also becomes a broad debate about roles and org design:
  - some think dedicated PM roles may shrink or disappear as engineers, designers, and PMs converge around AI-assisted building
  - others say PMs remain essential because engineers are already overloaded and need someone to handle prioritization, stakeholders, and communication
  - some note that many “Scrum” organizations are really just project management in disguise
  - a few commenters argue scrum is useful for small teams only when it improves coordination, and harmful when treated as religion

- Several commenters give personal anecdotes:
  - PMs shipping internal PRs and using Sourcegraph MCP / Claude-like tools to write better bugs
  - engineers being paged for bugs caused by careless diffs labeled with “YOLO!”
  - a PM at Meta saying an internal post about PMs landing prod diffs got a surprisingly positive response
  - someone at a consultancy describing a low-process environment as more pleasant than formal Scrum-heavy orgs

- The main disagreement in the thread is not whether AI can help PMs; it’s **where the line should be drawn**:
  - **Pro:** PMs should prototype, generate internal tools, improve communication, and sometimes even ship small frontend-heavy changes
  - **Anti:** if they can’t read code or own the maintenance burden, production changes are a recipe for hidden costs and degraded quality
  - **Middle ground:** AI can help everyone move faster, but high-risk systems still need people with engineering depth

### Assessment
This is a high-density, mixed-content Hacker News discussion with good long-term value as a snapshot of early “vibe coding” debates inside tech organizations. **Durability: medium** — the specific AI tool references and Meta-centric examples will age quickly, but the underlying themes about incentives, accountability, and role boundaries are durable. **Content type: mixed** — social thread with opinion, workplace anecdotes, and a few practical governance ideas. **Density: high** — many distinct viewpoints, concrete examples, and recurring themes packed into the thread. **Originality: commentary/synthesis** — mostly reactions and experience-based opinions rather than primary evidence. **Reference style: skim-once to refer-back** — useful for recalling the shape of the debate and the best arguments on each side, not for definitive technical guidance. **Scrape quality: partial/good** — the thread text is extensive and captures many replies, but it is flattened, repetitive, and lacks clean author labels for most comments; the top-comment author is not clearly preserved, and the structure of the discussion is harder to parse than the original HN page.
