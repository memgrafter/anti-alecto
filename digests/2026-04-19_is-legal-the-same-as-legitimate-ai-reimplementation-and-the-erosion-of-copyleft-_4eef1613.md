---
url: https://writings.hongminhee.org/2026/03/legal-vs-legitimate/
title: 'Is legal the same as legitimate: AI reimplementation and the erosion of copyleft — Hong Minhee on Things'
scraped_at: '2026-04-19T06:52:14Z'
word_count: 2187
raw_file: raw/2026-04-19_is-legal-the-same-as-legitimate-ai-reimplementation-and-the-erosion-of-copyleft-_4eef1613.txt
tldr: Hong Minhee argues that AI-assisted reimplementation of copyleft software may be legal, but it is not socially legitimate because it can strip away the reciprocal freedom that copyleft was meant to preserve.
key_quote: Law sets a floor; clearing it does not mean the conduct is right.
durability: high
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Hong Minhee
- Dan Blanchard
- Mark Pilgrim
- Armin Ronacher
- Salvatore Sanfilippo
- Zoë Kooyman
- Bruce Perens
tools:
- Claude
- GitHub
- JPlag
- Vercel
- Cloudflare
libraries:
- chardet
- Flask
- Redis
- Next.js
- GNU Bash
- GNU Readline
companies:
- Anthropic
- FSF
- Vercel
- Cloudflare
tags:
- copyleft
- open-source-licensing
- ai-reimplementation
- software-freedom
- copyright-law
---

### TL;DR
Hong Minhee argues that AI-assisted reimplementation of copyleft software may be legal, but it is not socially legitimate because it can strip away the reciprocal freedom that copyleft was meant to preserve.

### Key Quote
“Law sets a floor; clearing it does not mean the conduct is right.”

### Summary
- The essay responds to the controversy around **chardet 7.0**, where maintainer **Dan Blanchard** released a substantially rewritten version of the Python encoding library:
  - Claimed he **did not inspect the original source code directly**
  - Used only the **API and test suite** with **Claude** to reimplement it
  - Said the result was a **new independent work**
  - Relicensed it from **LGPL to MIT**
  - Original author **Mark Pilgrim** objected, arguing the LGPL’s share-alike obligations should still apply
- The author critiques two public defenses of Blanchard’s move:
  - **Armin Ronacher**: argues the GPL/LGPL restricts sharing and that permissive licensing is more “share-friendly”
  - **Salvatore Sanfilippo (antirez)**: argues AI reimplementation is legally permissible, drawing on copyright law and GNU history
- Main thesis:
  - **Legal permissibility is not the same as legitimacy**
  - The essay is less about whether AI reimplementation violates copyright law and more about whether it violates the **social compact** of copyleft
- Argument against antirez:
  - GNU/Linux-era reimplementation moved software **from proprietary to free**, expanding the commons
  - The chardet case moves in the opposite direction: from **copyleft protection to permissive licensing**
  - The essay says antirez’s historical analogy fails because it ignores this **directional difference**
- Argument against Ronacher:
  - The GPL does **not** prohibit private modification or private use
  - It only requires reciprocity **when code is distributed**
  - The author says copyleft does not suppress sharing; it makes sharing **recursive and self-reinforcing**
  - By contrast, MIT licensing lets others take from the commons without giving back
- The essay uses a Vercel/Cloudflare example to show the double standard:
  - Ronacher highlights that **Vercel reimplemented GNU Bash with AI**
  - But when **Cloudflare reimplemented Next.js** (MIT-licensed), Vercel reacted negatively
  - This is used to argue that “sharing” often means “others may copy me, but I resent being copied”
- Core moral claim:
  - Copyleft is a **community agreement** as much as a legal instrument
  - The real issue is whether those who benefit from the commons have an obligation to **return contributions to it**
  - The author cites **Zoë Kooyman (FSF)**: refusing to grant others the rights you received is “highly antisocial”
- The essay also emphasizes **positional asymmetry**:
  - Figures like **antirez** and **Ronacher** are successful project creators with influence
  - AI reimplementation helps people like them rework others’ projects, but threatens maintainers whose copyleft protections can now be bypassed
  - The author argues that their legal framing aligns with their own interests
- Final conclusion:
  - As AI makes reimplementation easier, **copyleft may become more necessary, not less**
  - The author suggests the community may need stronger licensing tools, possibly extending to:
    - **training copyleft (TGPL)**
    - a future **specification copyleft** for APIs, tests, and other layers below source code
  - The final judgment is social, not legal: **those who take from the commons owe something back**

### Assessment
This is a **high-durability opinion essay** with a strong normative argument about copyleft, legitimacy, and AI-assisted reimplementation. It is **mixed** in content type because it combines legal reasoning, software licensing history, and commentary on current open-source disputes. The piece is **medium-to-high density**, with specific examples, named people, and concrete licensing terms (LGPL, MIT, GPLv2, GPLv3, AGPL). It is **original commentary** rather than a neutral synthesis, and it is best used as **refer-back** reading if you want to revisit the argument about copyleft ethics in the AI era. Scrape quality appears **good**: the article text is present and coherent, with no obvious missing sections, though any embedded links or formatting beyond plain text are not visible here.
