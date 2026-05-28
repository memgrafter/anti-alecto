---
url: https://www.youtube.com/watch?v=_acTMUmdY9M
title: I Read Honey's Source Code - YouTube
scraped_at: '2026-04-12T18:54:56Z'
word_count: 3049
raw_file: raw/2026-04-12_i-read-honey-s-source-code-youtube_0a474cd0.txt
tldr: The video claims Honey’s Chrome extension uses a long-evolving “standown” system to selectively disable cashback based on affiliate/provider/store/user rules, and it also highlights an unusual JavaScript-in-JavaScript execution path involving Acorn and a “Vim” engine.
key_quote: “this is some obuscation. This is some weird stuff.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Megal
tools:
- Honey
- Acorn
libraries: []
companies:
- Honey
tags:
- browser-extension
- reverse-engineering
- affiliate-marketing
- chrome-extension
- javascript
---

### TL;DR
The video claims Honey’s Chrome extension uses a long-evolving “standown” system to selectively disable cashback based on affiliate/provider/store/user rules, and it also highlights an unusual JavaScript-in-JavaScript execution path involving Acorn and a “Vim” engine.

### Key Quote
“this is some obuscation. This is some weird stuff.”

### Summary
- The speaker is reviewing allegations around Honey, a coupon/cashback Chrome extension, by inspecting its source code over time.
- Main topic: Honey’s **“standown”** behavior — when it should disable itself to avoid overriding an existing affiliate click.
- Demonstration described:
  - Visiting Newegg with no affiliate link: Honey offers cashback.
  - Visiting Newegg through the speaker’s affiliate link: Honey stands down and disables itself.
  - In a second test, two browsers are logged into different Honey accounts:
    - The account with **zero cash back points** stands down.
    - The account with **cashback points** does **not** stand down.
- The speaker says they examined multiple Honey versions from roughly **version 11 (about 2019)** through **version 16 / 1901 (about 2024/present)**.
- According to the speaker, early versions used a more hard-coded rule system:
  - Explicit checks like whether an email contains `"test"` to always stand down.
  - Provider-specific logic such as checking whether the active provider is **LS / LinkShare**.
  - A loop that evaluates rules and stands down if any rule fails.
- The speaker claims the code changed very little from versions **11 through 14** (up to about 2022), but that around **version 16** there was a major refactor.
- In the newer design, the standown decision is described as being driven by configuration from an endpoint:
  - A **base object** is built.
  - Provider-specific values are merged in.
  - Store-specific values are merged in.
  - The resulting rules determine whether Honey stands down.
- The speaker interprets this as a more dynamic, maintainable system that can vary by:
  - **user**
  - **provider**
  - **store**
- The video’s conclusion on this part is careful but skeptical:
  - The speaker says they **cannot prove fraud** from the code alone.
  - They do say the system appears deliberately designed to be robust and to preserve the standown behavior in a more sophisticated way.
- A second major finding concerns a strange **JavaScript-in-JavaScript** mechanism:
  - The speaker notices references to **Acorn** (a JavaScript parser).
  - They mention a “**Vim instance manager**” and an internal **Vim engine**.
  - They describe Honey as having an apparatus that can parse JavaScript, evaluate it, and feed it into this engine.
  - They mention code references such as **`cart ops retrieval.js`** and **`product ops retrieval.js`**.
- The speaker says they were **not able to prove the code was actually executing** in their breakpoints, but they still found the setup highly unusual and obfuscatory.
- They also connect this to **Manifest V3** concerns, implying the design may be trying to avoid direct `eval` while still executing complex commands.
- The video frames this as especially odd because:
  - It seems intentionally designed to hide behavior.
  - The speaker speculates it may be related to interactions with other extensions, especially **ad blockers**.
- The tone is exploratory and opinionated, with the speaker repeatedly emphasizing this is the strangest reverse-engineering-style codebase they’ve seen.
- The video ends with a shout-out to **Megal**, praise for the related investigative videos, and a sponsor-style outro.

### Assessment
Durability is **medium** because the specific Honey versions, extension behavior, and Manifest V3 context are tied to a particular controversy and codebase state, though the general patterns about rule-driven ad/affiliate logic are more lasting. Content type is **mixed**: part commentary, part reverse-engineering / technical analysis, and part announcement-like reaction to an ongoing scandal. Density is **high** because it packs in version numbers, rule behavior, implementation details, and speculative interpretation, though the transcript is also somewhat rambling. Originality is mostly **commentary** informed by hands-on inspection of source code and tests rather than a pure primary source dump. Reference style is best as **refer-back** if you care about the Honey controversy or extension internals; it’s not a deep-study tutorial, but it may be worth revisiting for the specific claims about standown logic and the JavaScript engine. Scrape quality is **partial**: the transcript captures the spoken content well, but likely misses on-screen code, diagrams, and any technical evidence shown visually; it also includes sponsor/outro material that is not central to the technical claims.
