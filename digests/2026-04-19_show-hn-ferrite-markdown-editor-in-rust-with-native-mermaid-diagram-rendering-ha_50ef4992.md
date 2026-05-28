---
url: https://news.ycombinator.com/item?id=46571980
title: 'Show HN: Ferrite – Markdown editor in Rust with native Mermaid diagram rendering | Hacker News'
scraped_at: '2026-04-19T21:29:40Z'
word_count: 3122
raw_file: raw/2026-04-19_show-hn-ferrite-markdown-editor-in-rust-with-native-mermaid-diagram-rendering-ha_50ef4992.txt
tldr: Show HN for Ferrite, a Rust/egui Markdown editor with native Mermaid rendering, split view, syntax highlighting, structured JSON/YAML/TOML viewing, and Git integration drew interest around whether Mermaid is truly native Rust, how it compares to Typora/Obsidian/Zed, and whether it could become a serious alternative note editor.
key_quote: “100% pure Rust! No JS interpreter. Parses Mermaid syntax directly and renders via egui drawing primitives.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- OlaProis
- pbronez
- Arubis
- huevosabio
- Levitating
- khimaros
- adamnemecek
- dmitrygr
- dhruv3006
- WillAdams
- jasonjmcghee
- bthallplz
- vunderba
- danfoxley
- gregman1
- swiftcoder
- zen928
- koakuma-chan
- GrowingSideways
- echelon
- random3
- atlintots
- dvt
- djvdq
- kirubakaran
- tomtom1337
- lenova
- maxbond
- dboon
- LoganDark
- thegagne
- hashhar
tools:
- Ferrite
- Mermaid
- Typora
- Obsidian
- Zed
- egui
- Electron
- Tree-sitter
- resvg
libraries: []
companies: []
tags:
- markdown-editors
- rust-gui
- mermaid-diagrams
- note-taking
- developer-tools
---

### TL;DR
Show HN for Ferrite, a Rust/egui Markdown editor with native Mermaid rendering, split view, syntax highlighting, structured JSON/YAML/TOML viewing, and Git integration drew interest around whether Mermaid is truly native Rust, how it compares to Typora/Obsidian/Zed, and whether it could become a serious alternative note editor.

### Key Quote
“100% pure Rust! No JS interpreter. Parses Mermaid syntax directly and renders via egui drawing primitives.”

### Summary
- **Project:** Ferrite, a Markdown/Text/Code editor written in Rust with egui.
- **Version/status:** v0.2.1 announced; v0.2.2 “coming soon” with performance improvements for large files.
- **Core features claimed in the submission:**
  - Native Mermaid diagrams
    - flowcharts, sequence, state, ER, git graphs
    - pure Rust, no JS
  - Split view with raw + rendered side-by-side and sync scrolling
  - Syntax highlighting for 40+ languages with large-file optimization
  - JSON/YAML/TOML tree viewer with expandable structure
  - Git integration showing modified/staged/untracked status
  - Minimap, zen mode, auto-save, session restore, code folding indicators
  - ~15 MB binary, instant startup
  - Cross-platform: Windows/Linux/macOS
- **Top comment (verbatim):** “Is mermaid rendering implemented in Rust, or are you running mermaid.js in a JS interpreter somewhere?On other systems I’ve run into challenges rendering markdown documents with many mermaid diagrams in them. It would be nice to have a more robust way to do this.”
- **Top commenter:** `u/pbronez`
- **Thread topics:**
  - Whether Ferrite’s Mermaid support is truly native Rust or uses mermaid.js underneath
  - Comparisons to Typora as a polished Markdown editor with similar UX goals
  - Potential as an Obsidian alternative, especially missing wikilinks/backlinks
  - Requests for additional formats/features like Typst and TeX
  - React/egui/native app tradeoffs and interest in Rust GUI tooling
  - Performance concerns on large files and fan spin-up reports
  - Whether native rendering will match Mermaid.js output for sharing/export
- **Discussion highlights:**
  - The author clarified that Mermaid rendering is “100% pure Rust,” with no JS interpreter, and that it parses Mermaid syntax directly and renders via egui drawing primitives.
  - A commenter noted the project resembles Typora, and the author responded that Ferrite aims for similar polish plus native Mermaid, structured data support, and a pipeline feature for shell integration.
  - Multiple commenters framed it as a possible Obsidian alternative, but noted missing features like `[[wikilinks]]` and backlinks.
  - The author said those Obsidian-style features are natural additions and may be added to the roadmap.
  - On egui, the author said it is great for rapid prototyping, but the current `TextEdit` is not suitable for a full code editor; v0.3.0 will replace it with a custom widget.
  - A performance complaint (“Made the fan in my Windows 11 laptop spin up.”) prompted the author to ask for repro details and point to upcoming large-file optimizations.
  - The author later outlined an upcoming v0.3.0 Mermaid crate API:
    - `parse() -> AST`
    - `layout() -> positioned elements`
    - `render_svg() -> SVG string`
    - `render_png() -> via resvg`
    - CLI examples for PNG/SVG output without a browser
  - There was some debate over native rendering versus Mermaid.js compatibility: native rendering is faster and avoids JS, but may not be pixel-perfect for sharing outside Ferrite.
  - Several replies drifted into broader tooling and licensing debates around Obsidian, Electron, open source, Typora pricing, and alternative editors.

### Assessment
This is a mixed content thread: part product announcement, part technical Q&A, part market positioning feedback. Durability is medium, since the exact feature set, version numbers, and roadmap items are tied to a specific point in Ferrite’s development, but the broader themes—native Markdown editors, Mermaid rendering, Rust GUI apps, and Obsidian/Typora alternatives—are durable. Density is medium-high because the thread includes concrete implementation details, feature claims, and roadmap/API notes, though some of the thread also veers into side debates. Originality is mostly primary-source commentary from the author plus community reaction, not a neutral synthesis. Best use is skim-once to evaluate the product and note the author’s technical clarifications; refer-back if tracking Ferrite’s roadmap, Mermaid implementation, or Rust editor ecosystem. Scrape quality is good overall: the title, submission text, and many comments were captured, including the key top-comment exchange and author replies, though this is still a thread capture rather than the full HN page rendering.
