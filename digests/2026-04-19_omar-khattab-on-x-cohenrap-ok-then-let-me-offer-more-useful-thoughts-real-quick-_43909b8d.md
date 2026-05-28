---
url: https://x.com/lateinteraction/status/2022747248841625741
title: 'Omar Khattab on X: "@cohenrap OK then let me offer more useful thoughts real quick :D An agent that has an LLM tool is one of the baselines in the paper. It''s better than some other baselines, but not that good actually. It has three major problems that together mean that the root LLM cannot scalably use it https://t.co/PgTHwEx28F" / X'
scraped_at: '2026-04-19T08:09:01Z'
word_count: 244
raw_file: raw/2026-04-19_omar-khattab-on-x-cohenrap-ok-then-let-me-offer-more-useful-thoughts-real-quick-_43909b8d.txt
tldr: Omar Khattab argues that “an LLM as a tool” is only a baseline agent pattern and cannot scale for full-context understanding because it is token-verbalized, requires the root model to serially copy subcalls, and is trained for task delegation rather than true distributed reasoning.
key_quote: It has three major problems that together mean that the root LLM cannot scalably use it to actually understand the context.
durability: medium
content_type: opinion
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Omar Khattab
tools:
- dspy.RLM
- Signatures
companies:
- DSPy
tags:
- agents
- llm-tooling
- distributed-reasoning
- prompt-engineering
- dspy
---

### TL;DR
Omar Khattab argues that “an LLM as a tool” is only a baseline agent pattern and cannot scale for full-context understanding because it is token-verbalized, requires the root model to serially copy subcalls, and is trained for task delegation rather than true distributed reasoning.

### Key Quote
“It has three major problems that together mean that the root LLM cannot scalably use it to actually understand the context.”

### Summary
- This is an X/Twitter reply by Omar Khattab responding to a question about using an LLM as a tool inside an agent.
- He says this setup is included as a baseline in the paper and is better than some other baselines, but still “not that good.”
- He identifies **three major limitations**:

  1. **The tool context is not symbolic**
     - The root model is given a **verbalized prompt as tokens**, not a compact symbolic representation.
     - This means the user prompts have to be externalized into text first.

  2. **Subcalls are serialized through token generation**
     - The root LLM must “copy” subcalls token by token.
     - Because of this, it cannot efficiently launch **Ω(N)** subcalls one at a time.
     - To make this workable, you need actual code with **loops**, **recursive helper functions**, or similar mechanisms that manage subcalls programmatically.

  3. **The policy is wrong for context understanding**
     - When an LLM is used as a tool, it is generally trained to do **task delegation**.
     - That helps for assigning small chunks of work, but not for the deeper goal of **understanding every chunk of the input**.
     - He contrasts:
       - “go think about this 1 small problem”
       - versus “go understand every chunk of the input”

- He adds that using **dspy.RLM** may provide more conceptual clarity, because its fit with **Signatures** makes the special behavior more obvious.

### Assessment
This is a short, high-density technical opinion/commentary from a primary source, with medium durability because it discusses agent/tooling design concepts that are likely to remain relevant, though the specific framing may age with future agent architectures and DSPy versions. It is a mixed content type: mostly opinion and technical argument, not a full tutorial or reference. The note is useful as a refer-back item for understanding Khattab’s critique of “LLM-as-tool” agents, especially if you are evaluating agent designs or DSPy/RLM concepts. Scrape quality is partial: the main text is present, but the linked image and surrounding thread context are not fully captured.
