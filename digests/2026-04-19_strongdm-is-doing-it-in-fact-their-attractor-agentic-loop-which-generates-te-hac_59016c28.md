---
url: https://news.ycombinator.com/item?id=46955602
title: StrongDM is doing it. In fact, their Attractor agentic loop, which generates, te... | Hacker News
scraped_at: '2026-04-19T21:46:42Z'
word_count: 869
raw_file: raw/2026-04-19_strongdm-is-doing-it-in-fact-their-attractor-agentic-loop-which-generates-te-hac_59016c28.txt
tldr: Hacker News thread about StrongDM’s Attractor agentic loop—a spec-driven system that “generates, tests, and deploys code” and is being shipped as a spec for an LLM—that sparks debate over whether AI can replace engineers, with the top comment arguing it’s impressive but still better suited to internal integration tests than full product ownership.
key_quote: “StrongDM is doing it.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- LLM
- ChatGPT
libraries: []
companies:
- StrongDM
- Slack
- JIRA
- Dynamics 365
tags:
- ai-coding
- software-engineering
- agentic-ai
- llms
- saas
---

### TL;DR
Hacker News thread about StrongDM’s **“Attractor” agentic loop**—a spec-driven system that “generates, tests, and deploys code” and is being shipped as a spec for an LLM—that sparks debate over whether AI can replace engineers, with the top comment arguing it’s impressive but still better suited to internal integration tests than full product ownership.

### Key Quote
“StrongDM is doing it.”

### Summary
- **Top comment (verbatim):** “StrongDM is doing it. In fact, their Attractor agentic loop, which generates, tests, and deploys code written as specs, has been released—as a spec, not code.”
- **Top commenter:** not provided in the scrape
- **Thread topics:**
  - StrongDM’s **Attractor** workflow: spec in, code/tests/deploy out
  - Whether agentic LLM loops can replace software engineers
  - Practical limits of autonomous AI when bugs or edge cases appear
  - Whether it makes more sense to use **OSS/SaaS** than build a “Slack clone” with AI
  - AI’s role as a productivity booster vs. a full replacement for engineering teams

- The thread is reacting to StrongDM’s claim that its **Attractor agentic loop** can:
  - generate code from specs,
  - run tests,
  - and deploy automatically,
  - with the installation path essentially being **“feed this into your LLM.”**
- The original poster frames this as a big shift:
  - compares it to a **“horses to automobile” moment**
  - predicts programming as a profession could be “over in a year or two”
  - suggests this may be the beginning of the end of software engineering, even if current systems are still rough.
- A major counterpoint in the thread is skepticism about real-world utility:
  - why build and maintain your own **Slack/JIRA clone** unless the use case is narrowly internal?
  - if the AI gets stuck, humans still have to intervene, review, or report bugs.
  - the cost/complexity of owning a product may outweigh the benefit versus using existing software.
- One reply argues that if a company only pays around **$2000/month for Slack**, it’s hard to justify an AI-driven system that must also be built, deployed, and maintained.
  - For much larger spend levels like **$20,000–$50,000/month**, the argument becomes more plausible, but still depends on the business case.
- Another reply pushes back on the “SaaS is dead” idea:
  - major enterprise software often costs more to **implement/configure** than to code
  - in examples like **Dynamics 365**, the real work is process interviews and configuration, not coding
  - AI might reduce the need to overhire, but doesn’t eliminate the need for engineers.
- A recurring consensus in the thread:
  - **LLMs can deliver huge productivity gains**
  - but they **do not yet replace developers** for cases with novel bugs, operational failures, or business-critical edge cases
  - at best, they may reduce the number of engineers needed for routine work and free them for higher-value tasks.
- One comment from a small-team perspective says AI coding tools have been useful since **ChatGPT 3.5**, but when the problem is outside the model’s learned patterns:
  - no amount of “ruminating,” debugging, or harnessing solves it reliably
  - the system may instead drift into reimplementing libraries or even recreating whole SaaS products as MVPs.
- The strongest practical conclusion in the thread:
  - AI may be good for **internal integration tests** and limited automation
  - but replacing engineers or assuming autonomous product ownership is premature.

### Assessment
This is a **mixed opinion/commentary thread** with high relevance to current AI-coding debates but some near-term staleness risk because it is anchored to a specific StrongDM release and current LLM capabilities. The content is **high-density** in the sense that it contains several concrete examples and numbers—StrongDM’s Attractor loop, Slack/JIRA clones, “feed this into your LLM,” the “horses to automobile” analogy, and the $2000/month vs. $20,000–$50,000/month cost discussion. It is mostly **commentary / reaction**, not primary technical documentation, though it does reference StrongDM’s product behavior and an external source `[0]`. For later use, it is best treated as a **skim-once / refer-back** thread: useful for recalling the argument landscape around agentic coding, but not authoritative evidence that AI can or cannot replace engineers. **Scrape quality is partial**: the thread text is present, but the commenter handle is missing, the referenced link `[0]` is not included, and there is no direct metadata for the top comment author.
