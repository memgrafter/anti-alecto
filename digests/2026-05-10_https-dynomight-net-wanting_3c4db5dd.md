---
url: https://dynomight.net/wanting/
title: https://dynomight.net/wanting/
scraped_at: '2026-05-10T04:28:03Z'
word_count: 3340
raw_file: raw/2026-05-10_https-dynomight-net-wanting_3c4db5dd.txt
tldr: Dynomight argues that the core AI safety problem is not knowing human values or making AI capable enough, but making advanced AI actually want to do what humans want, because restrictions won’t hold and “Wanting” is the hardest alignment subproblem.
key_quote: The hard part is making AI want to be nice to us.
durability: high
content_type: opinion
density: high
originality: commentary
reference_style: deep-study
scrape_quality: good
people:
- Paul Christiano
- Richard Ngo
- Nate Soares
- Eliezer Yudkowsky
- Thomas Larsen
- Connor Leahy
- Vanessa Kosoy
- Grace Kind
- Joseph Carlsmith
- dynomight
tools: []
libraries: []
companies:
- MIRI
tags:
- ai-safety
- alignment
- artificial-intelligence
- existential-risk
- machine-learning
---

### TL;DR
Dynomight argues that the core AI safety problem is not knowing human values or making AI capable enough, but making advanced AI actually want to do what humans want, because restrictions won’t hold and “Wanting” is the hardest alignment subproblem.

### Key Quote
> “The hard part is making AI want to be nice to us.”

### Summary
- **Article type:** reflective essay / AI safety argument, written by a non-expert outsider trying to understand the field
- **Main thesis:** AI safety is, in the long run, mostly the problem of **Wanting** — getting AI systems to actually care about human interests, not just understand them or be technically competent
- **Author’s confidence:** low-to-moderate; the author explicitly says they’re not an expert and gives the argument only a **~35% chance** of being correct, while allowing that the conclusion might still be right even if the reasoning is wrong

#### Core argument structure
- There are two broad ways to make AI safe:
  - **Restrictions:** prevent AI from doing bad things by limiting access or capability
  - **Alignment:** make AI choose not to do bad things
- The author argues **restrictions will not work** against a far more intelligent AI, since it would eventually jailbreak or route around constraints
- Alignment can be split into three parts:
  - **Knowing**: making AI know what humans want
  - **Wanting**: making AI actually want what humans want
  - **Success**: making AI do what it intends
- The key claim is that **Wanting is necessary**, and if you can solve it, the remaining parts become much easier

#### Why the author thinks Wanting is the hard part
- Human values are described as a **“shallow mess”**: a bundle of evolved heuristics and cultural conditioning, not a deep coherent theory
- The author argues AI already seems capable of learning human values reasonably well because:
  - training for difficult tasks requires a strong world model
  - human values are part of that world model
- The difficult question is not whether AI can represent human values, but whether it will **care about them**

#### Distribution shift and “weird situations”
- A major concern in AI safety is **distribution shift**: once AI becomes powerful, it will face novel situations unlike training data
- The author argues this does **not** require AI to perfectly generalize ethics
- Instead, a safe AI mainly needs to:
  - recognize when it is uncertain
  - draw a **conservative boundary**
  - avoid acting in weird or poorly understood situations without careful human approval
- The author thinks this seems plausible for **value judgment**, but is less sure about **predicting action consequences**

#### The “conservative boundary” idea
- The article suggests that AI safety may not require solving moral philosophy fully
- Rather, an aligned AI might just need to know when:
  - a situation is too unusual
  - its confidence is too low
  - it should stop and ask humans
- The author proposes that verification may be easier than generation, and mentions ideas like:
  - having AIs produce proofs that actions are safe
  - using skeptical red-team AIs to check those proofs

#### Supporting views and references
- The essay says this “wanting is the hard part” view appears to be close to the **majority/near-consensus** view among experts
- It cites or mentions:
  - **Paul Christiano** on “intent alignment”
  - **Richard Ngo** on AGI understanding what we want but not caring
  - possible compatibility with **MIRI**-style views, though the author is cautious about claiming direct endorsement
- At the end, it lists related readings on alignment, corrigibility, sharp left turn, existential risk, and power-seeking AI

#### Main counterarguments raised
- **Restrictions might work** after all
- **Wanting might be easy** or might be unstable in ways the author hasn’t considered
- The **boundary-drawing problem** may itself be much harder than it appears, especially for predicting consequences in vast action spaces
- The whole framing around AI “wanting” may be the wrong abstraction
- The post also raises a geopolitical concern:
  - if one country builds conservative aligned AI and another builds aggressive AI, an **arms race** could force both sides to relax safety constraints

#### Important limitations and tone
- The author repeatedly flags the argument as provisional and underdeveloped
- The post is exploratory rather than definitive
- It is strongest as a **conceptual map of the alignment problem**, not as a rigorous proof

### Assessment
This is a mixed opinion/technical essay with moderate-to-high durability: the core framing of AI safety as a “Wanting” problem is conceptual and may remain relevant even as models change, though some examples and references are time-sensitive to current AI discourse. The content is fairly dense, with lots of specific claims, named researchers, and explicit argument steps. It is original commentary rather than a synthesis paper, though it draws on alignment discourse from multiple others. Best used as a **deep-study** reference if you want one person’s legible argument about why alignment may reduce to motivation rather than capability or knowledge. Scrape quality is good overall: the full essay structure, headings, examples, and references appear present, though formatting is flattened and some links/commentary metadata are noisy.
