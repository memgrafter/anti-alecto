---
url: https://news.ycombinator.com/item?id=46572766
title: This is cool. I was hoping to see progress coming from Zed (e.g. because Tree-si... | Hacker News
scraped_at: '2026-04-19T21:29:59Z'
word_count: 2223
raw_file: raw/2026-04-19_this-is-cool-i-was-hoping-to-see-progress-coming-from-zed-e-g-because-tree-si-ha_abc243f7.txt
tldr: HN discussion about a native Markdown editor / Obsidian alternative (Hyperclast/Ferrite) where the top commenter `u/echelon` simply asks “What is Obsidian written in? Electron?”, and the thread quickly turns into debate over Electron, open-source licensing, product positioning, and whether a standalone Markdown editor has a real market.
key_quote: Thanks! The end-goal is a fast, native Markdown editor that "just works" - no Electron, no web tech, instant startup.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: skim-once
scrape_quality: partial
people:
- random3
- u/echelon
- u/kirubakaran
- u/OlaProis
- u/atlintots
- u/dvt
- u/djvdq
- u/tomtom1337
- u/lenova
- u/maxbond
- u/LocalPCGuy
- u/dboon
- u/thegagne
- u/hashhar
- u/yencabulator
- u/allarm
- u/koiueo
- u/RealityVoid
tools:
- Electron
- Obsidian
- Zed
- Notion
- Typora
- iA Writer
- Dendron
- VS Code
- Emacs
libraries:
- tree-sitter-markdown
- Mermaid
- egui
companies:
- Hyperclast
- Ferrite
- OSI
- Amazon
- Google
- Facebook
- Zed
- Obsidian
- Notion
- Dendron
- Typora
- iA Writer
tags:
- markdown-editors
- electron
- open-source-licensing
- product-positioning
- note-taking
---

### TL;DR
HN discussion about a native Markdown editor / Obsidian alternative (Hyperclast/Ferrite) where the top commenter `u/echelon` simply asks “What is Obsidian written in? Electron?”, and the thread quickly turns into debate over Electron, open-source licensing, product positioning, and whether a standalone Markdown editor has a real market.

### Key Quote
> “Thanks! The end-goal is a fast, native Markdown editor that "just works" - no Electron, no web tech, instant startup.”

### Summary
- **Thread type:** Hacker News social thread around a product/dev announcement and feedback request.
- **Original poster / context:**
  - The submission expresses excitement about progress from a native markdown-editing project.
  - The poster says they are a heavy Obsidian user and want “real alternatives focused on foundations.”
  - They ask for the project’s long-term end goal and wish the author luck.

- **Top comment (verbatim):** `"What is Obsidian written in? Electron?"`
- **Top commenter:** `u/echelon`
- **Thread topics:**
  - Whether Obsidian is Electron-based and what that implies
  - Native vs Electron/web-based Markdown editors
  - Open-source licensing and “source-available” concerns
  - Product messaging, demos, and onboarding for a new note-taking / collaboration tool
  - Whether there is a market for a standalone Markdown editor versus using a general-purpose editor

- **Main product discussed:** Hyperclast / Ferrite-style Markdown editor
  - The author says the goal is a **fast, native Markdown editor** with:
    - no Electron
    - no web tech
    - instant startup
  - Planned near-term work:
    - **v0.3.0** will extract **Mermaid** into a standalone crate
    - build a **custom text editor widget**
    - unlock features that `egui`’s `TextEdit` blocks, such as:
      - proper multi-cursor
      - code folding
  - Long-term idea:
    - potentially extract the editor as a **headless Rust library**
    - they note this is missing in the ecosystem

- **What the thread spent time on:**
  - **Electron / native app debate**
    - Obsidian is confirmed in-thread to be Electron-based and not open source.
    - Some commenters treat that as acceptable; others prefer native apps like Zed.
    - One commenter notes Obsidian is “web-based, it just pretends not to be, but it's just Electron.”
  - **Open-source licensing dispute**
    - One commenter points out the project is not truly open source because the license forbids providing it as a managed service.
    - That triggers a mini-argument about “open source purity,” OSI, GPL, and “fair source” / ethical-source style licensing.
    - Some commenters argue closed source is fine; others want forkability and protection against rug pulls.
  - **Early product feedback for Hyperclast**
    - Several replies say the landing page doesn’t clearly explain what the product is.
    - Repeated suggestions:
      - add a **demo without login**
      - include **screenshots / GIFs / demo video**
      - make the value proposition clearer
      - show a **sample workspace**
      - clarify whether it is browser-based or app-based
    - The author responds positively and says they added a non-login demo and will improve the messaging.
  - **Market skepticism**
    - One commenter questions whether standalone Markdown editors still matter because many people use their own editor plus plugins.
    - The author replies that there is a real market:
      - Obsidian has **1M+ users**
      - Typora is popular
      - iA Writer has a loyal following
    - They frame the target audience as writers, PKM users, note-takers, and developers who want a focused writing tool rather than an IDE.

- **Key points of disagreement / consensus:**
  - **Consensus:** the product messaging needed improvement; a demo and clearer explanation help a lot.
  - **Disagreement:** whether “open source” is being used accurately for a license that restricts hosted use.
  - **Disagreement:** whether native Markdown editors can compete with existing editors and plugin ecosystems.
  - **Consensus-ish:** many users do care about performance and instant startup in note-taking tools.

### Assessment
Durability is **medium**: the core discussion about native vs Electron apps, product positioning, and source-available licensing is broadly reusable, but several details are tied to the specific project state and HN feedback at the time. Content type is **mixed**—part product announcement, part opinion, part technical roadmap, and part community critique. Density is **medium-high** because the thread contains concrete roadmap items, license language, and repeated feedback patterns, though it is also noisy with side debates. Originality is mostly **commentary** around a project rather than a primary technical source, with the author’s replies adding some original roadmap context. Reference style is best as **skim-once** for the thread dynamics or **refer-back** if tracking the product’s positioning/licensing discussion. Scrape quality is **partial**: the thread capture includes many comments and useful details, but it appears truncated in places, and any images/code/linked page context from the original HN page is not fully present.
