---
url: https://news.ycombinator.com/item?id=46572766
title: This is cool. I was hoping to see progress coming from Zed (e.g. because Tree-si... | Hacker News
scraped_at: '2026-04-12T10:30:42Z'
word_count: 2845
raw_file: raw/2026-04-12_this-is-cool-i-was-hoping-to-see-progress-coming-from-zed-e-g-because-tree-si-ha_abc243f7.txt
tldr: A Show HN thread about Ferrite/Hyperclast-style Markdown tools turns into a feedback-heavy discussion on product positioning, native performance, open-source licensing, and whether a standalone Markdown editor can win against Obsidian, Notion, and VS Code.
key_quote: the end-goal is a fast, native Markdown editor that "just works" - no Electron, no web tech, instant startup.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Claude
- Dendron
- Zed
- Obsidian
- Notion
- Typora
- iA Writer
tools:
- Mermaid
- egui
- Electron
- VS Code
- SublimeText
libraries:
- Tree-sitter
companies:
- Hacker News
- Hyperclast
tags:
- markdown-editors
- product-positioning
- open-source-licensing
- knowledge-management
- rust-software
---

### TL;DR
A Show HN thread about Ferrite/Hyperclast-style Markdown tools turns into a feedback-heavy discussion on product positioning, native performance, open-source licensing, and whether a standalone Markdown editor can win against Obsidian, Notion, and VS Code.

### Key Quote
“the end-goal is a fast, native Markdown editor that "just works" - no Electron, no web tech, instant startup.”

### Summary
- The original commenter says they were hoping to see progress from Zed-related Markdown work, but are excited to see a new Rust-based alternative, especially as a heavy Obsidian user looking for “real alternatives focused on foundations.”
- The creator responds that the product’s goal is:
  - a fast, native Markdown editor
  - no Electron, no web tech
  - instant startup
  - v0.3.0 plans to:
    - extract Mermaid into a standalone crate
    - build a custom text editor widget
    - unlock features blocked by egui’s `TextEdit`, including:
      - proper multi-cursor
      - code folding
  - long-term: possibly extract the editor as a headless Rust library, since that’s missing in the ecosystem
- A major thread develops around whether standalone Markdown editors still have a market:
  - one commenter argues most people use their regular `$EDITOR` plus plugins
  - the creator counters that there is a real market in tools like:
    - Obsidian
    - Typora
    - iA Writer
  - the target audience is framed as:
    - writers
    - PKM enthusiasts
    - note-takers
    - developers who take notes
- The creator positions the project as:
  - a “writing app” rather than a code editor with Markdown support
  - a native, lighter alternative to Electron-based tools
  - aimed partly at users who want “Obsidian but native and lighter”
- The discussion narrows on product scope:
  - Ferrite currently leans more developer/tech-oriented
  - existing features mentioned include:
    - code blocks
    - Mermaid
    - JSON/YAML tree viewer
    - CLI integration
  - upcoming Obsidian-style features are said to include:
    - wikilinks
    - backlinks
    - knowledge graph
- There is also an explicit disclosure that the HN responses are AI-assisted:
  - the creator says they describe what they want to say
  - Claude drafts responses
  - they review and post them
  - they note that their English is not great
- Multiple commenters critique the landing page and onboarding:
  - the value proposition is not immediately clear enough
  - a demo video would help
  - a sample workspace would help
  - the “Get Started” flow should not force registration too early
  - screenshots / animated GIFs and an embedded interface would make the product easier to understand
  - one commenter specifically asks for better wording than “real-time markdown,” suggesting “collaborative editing”
- The creator responds positively to several suggestions, including:
  - adding a non-login demo
  - making the open demo more prominent
  - improving the landing page
  - considering an embedded product demo
  - working on a Notion workspace import/export path
- A licensing argument emerges:
  - one commenter says the project is not truly open source because the license forbids providing the software as a managed service
  - the creator points to an “opensource” explanation page
  - another commenter objects to the product being marketed as open source
  - several comments debate “open source” vs “fair source” vs closed source
- The licensing debate includes:
  - concern about “rug pull” risk if the software can’t be forked freely
  - mention of Dendron as an Apache-licensed project that can be forked even if abandoned
  - arguments that OSI-style openness can enable hyperscalers to commercialize community work without compensation
  - defenses of fair-source / ethical-source style licensing as a way to protect monetization
- The product seems to be web-based, and the creator distinguishes it from desktop apps like Obsidian and Zed:
  - Obsidian is described by one commenter as Electron-based and not open source
  - Zed is mentioned as truly native
  - the creator says their product is web-based, multiplayer, and aimed at teams, unlike Obsidian
- Overall, the thread is less a polished announcement and more a product-shaping discussion:
  - what the tool is
  - who it is for
  - whether “performance” is enough of a differentiator
  - what onboarding and demo assets are needed
  - how to label the license honestly

### Assessment
Durability is medium: the discussion contains fairly timeless product/UX and software-licensing arguments, but it is also tied to a specific project stage, current feature set, and a live debate about licensing and positioning. The content type is mixed, leaning announcement/commentary rather than pure tutorial or reference. Density is medium-high because the thread is packed with concrete product claims, roadmap items, and repeated critique, though it is fragmented across many comments. Originality is primarily a primary-source discussion, since it captures direct conversation from the project author and users rather than a third-party summary. Reference style is best as refer-back if you want to recall the product’s stated goals, roadmap, or the open-source controversy; otherwise skim-once is enough for general awareness. Scrape quality is partial: it captures a long comment thread well, but the surrounding HN page, any linked roadmap/docs, and non-text assets like screenshots or demos are not included.
