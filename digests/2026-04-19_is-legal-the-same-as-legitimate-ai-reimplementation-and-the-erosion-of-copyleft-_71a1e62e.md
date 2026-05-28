---
url: https://news.ycombinator.com/item?id=47310160
title: 'Is legal the same as legitimate: AI reimplementation and the erosion of copyleft | Hacker News'
scraped_at: '2026-04-19T21:41:32Z'
word_count: 43166
raw_file: raw/2026-04-19_is-legal-the-same-as-legitimate-ai-reimplementation-and-the-erosion-of-copyleft-_71a1e62e.txt
tldr: Hacker News debates whether an AI-assisted rewrite of chardet 7.0 from the API and test suite can legally and morally escape LGPL/copyleft, with top commenter Mark Pilgrim arguing it erodes the commons and others arguing it is just a legitimate clean-room reimplementation and that the new code should probably have been published as a separate project, not an MIT relicensing of the old one.
key_quote: If source code can now be generated from a specification, the specification is where the essential intellectual content of a GPL project resides.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: deep-study
scrape_quality: partial
people:
- Mark Pilgrim
- Dan Blanchard
- Antirez
- Armin Ronacher
tools:
- Claude
- Copilot
- JPlag
- GitHub
libraries:
- chardet
companies:
- Anthropic
- Microsoft
- Google
- Oracle
tags:
- copyleft
- ai-reimplementation
- copyright-law
- open-source-licensing
- clean-room-rewrite
---

### TL;DR
Hacker News debates whether an AI-assisted rewrite of **chardet 7.0** from the **API and test suite** can legally and morally escape **LGPL/copyleft**, with top commenter **Mark Pilgrim** arguing it erodes the commons and others arguing it is just a legitimate clean-room reimplementation and that the new code should probably have been published as a separate project, not an MIT relicensing of the old one.

### Key Quote
> "If source code can now be generated from a specification, the specification is where the essential intellectual content of a GPL project resides."

### Summary
- **Top comment (verbatim):** "If source code can now be generated from a specification, the specification is where the essential intellectual content of a GPL project resides."
- **Top commenter:** `Mark Pilgrim`
- **Thread topics:**
  - Whether **chardet 7.0** was a true clean-room rewrite or a license-washing exercise
  - Whether the **API + test suite** count as part of the protected work/source
  - Whether the maintainer’s long familiarity with the codebase taints the rewrite
  - Whether an AI-generated rewrite can be relicensed as **MIT**
  - Whether the project should have been published as a **new repo** (`chardet-ng`, `chardet-fresh`, etc.) instead of overwriting the existing one

- The thread is centered on a specific case: **Dan Blanchard** reportedly fed **Claude** only the **API and test suite** for **chardet** and asked it to reimplement the library from scratch.
- The new version is described as:
  - **~98.7% unique** by JPlag in one comment
  - substantially faster than the previous version
  - relicensed under **MIT**
- A major disagreement is whether this is:
  - a **legitimate reimplementation** that only preserves behavior, or
  - a **copyleft workaround** that strips away the LGPL social contract while keeping the project’s reputation and interface

- A recurring subthread asks whether the **test suite** is effectively part of the source / specification:
  - some argue tests define the contract and should count as protected input under copyleft logic
  - others argue tests and API are not the implementation, and using them is ordinary reverse engineering / clean-room behavior
- Several commenters say the key distinction is not “AI vs human,” but **whether the output copies expressive code** or only reimplements functional behavior.
- Others argue the important issue is that the maintainer had **years of familiarity with the codebase**, so even if Claude didn’t see the source directly, the rewrite may not be meaningfully clean-room.
- There is also a repeated argument about **how the project was published**:
  - some think it would have been cleaner to create a **new MIT-licensed project**
  - others say replacing the old project is the point if the old code is being superseded
  - one complaint is that this feels like “hijacking” an established LGPL project rather than making a new one

- The thread expands into broader arguments about:
  - whether AI is eroding **copyright**, **copyleft**, or IP more generally
  - whether stronger IP protection would mainly help **large corporations**
  - whether the real issue is **corporate capture** rather than licensing itself
  - whether AI-assisted cloning makes open source less attractive because companies can “launder” licenses or repackage community work without reciprocal obligations

- A lot of the discussion turns on legal edge cases:
  - whether **LLM outputs** are copyrightable at all
  - whether AI-assisted code is automatically public domain in the US
  - whether using a model trained on copyleft code creates derivative-work problems
  - whether fair use would cover model training or reimplementation
- There are repeated references to precedents like:
  - **Google v. Oracle**
  - **Thaler v. Perlmutter**
  - the general rule that **AI cannot be the author**
- But the thread often mixes up:
  - **copyrightability**
  - **infringement**
  - **fair use**
  - **license obligations**
  which leads to long back-and-forths with no consensus.

- A substantial cluster of comments argues that this specific rewrite is **morally wrong even if legally defensible**, because:
  - it uses a project built under LGPL expectations
  - it may strip reciprocity from work meant to remain free
  - it benefits the person who wants a more permissive license without asking the broader community
- Another cluster argues the opposite:
  - clean-room reimplementation is a core freedom
  - the GPL/LGPL ecosystem historically benefited from exactly this kind of interoperability pressure
  - if AI makes reimplementation cheap, that may actually expand freedom rather than reduce it

- The thread also repeatedly returns to the practical point that:
  - if AI can reimplement software from specs/tests cheaply, then **software source code may no longer be the real moat**
  - reputation, distribution, certification, and ecosystem may matter more than the code itself
  - but some commenters note that for things like aerospace or medical software, **certification** remains the true barrier, not code copying

- The overall mood is highly polarized:
  - some see this as a sign that **copyleft is being undermined**
  - others see it as the natural next step in the long history of **clean-room reimplementation**
  - many comments worry that the legal system is too slow to adapt and that whatever precedent emerges will be exploited by the biggest players first

### Assessment
This is a **mixed** content type: a social thread with legal, technical, and ideological arguments. Durability is **medium**: the specific chardet/Claude/GPL dispute is tied to a current controversy and evolving AI law, but the broader tensions around reimplementation, clean-room methods, and copyleft vs permissive licensing are long-lived. Density is **high**: the thread is packed with concrete claims, named cases, license details, and recurring subarguments, though it is also repetitive and sometimes circular. Originality is **commentary / synthesis**, not a primary source; it’s a large, argumentative aggregation of reactions to an article plus legal speculation. Reference style is best as **deep-study** if you want the exact dispute shape, or **refer-back** if you’re tracking how HN frames AI reimplementation and copyleft. Scrape quality is **partial**: the capture is very long but extremely duplicated and noisy, with many repeated arguments and some likely-paraphrased or context-stripped claims; it preserves the main debate well, but you should be cautious about treating every legal assertion as cleanly sourced.
