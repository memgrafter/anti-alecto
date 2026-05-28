---
url: https://news.ycombinator.com/item?id=46571980
title: 'Show HN: Ferrite – Markdown editor in Rust with native Mermaid diagram rendering | Hacker News'
scraped_at: '2026-04-12T07:27:38Z'
word_count: 109
raw_file: raw/2026-04-12_show-hn-ferrite-markdown-editor-in-rust-with-native-mermaid-diagram-rendering-ha_50ef4992.txt
tldr: Ferrite is a Rust-based Markdown/text/code editor with native Mermaid rendering, split-view editing, syntax highlighting, structured data tree views, Git status integration, and a small fast-launching binary.
key_quote: Built a Markdown editor using Rust + egui. v0.2.1 just dropped with major Mermaid improvements
durability: medium
content_type: announcement
density: medium
originality: primary
reference_style: skim-once
scrape_quality: good
people:
- OlaProeis
tools:
- Ferrite
- egui
- GitHub
libraries: []
companies: []
tags:
- markdown-editor
- rust
- mermaid
- code-editor
- productivity-tools
---

### TL;DR
Ferrite is a Rust-based Markdown/text/code editor with native Mermaid rendering, split-view editing, syntax highlighting, structured data tree views, Git status integration, and a small fast-launching binary.

### Key Quote
“Built a Markdown editor using Rust + egui. v0.2.1 just dropped with major Mermaid improvements”

### Summary
- **What it is:** Ferrite is a desktop editor for Markdown, text, and code, built in **Rust** with **egui**.
- **Main headline feature:** It now supports **native Mermaid diagram rendering** in pure Rust, with no JavaScript.
- **Supported Mermaid diagram types mentioned:**
  - flowcharts
  - sequence diagrams
  - state diagrams
  - ER diagrams
  - git graphs
- **Editing workflow features:**
  - **Split view** with raw Markdown and rendered preview side by side
  - **Sync scrolling** between views
- **Code and data features:**
  - **Syntax highlighting** for **40+ languages**
  - **Large file optimization**
  - **JSON/YAML/TOML tree viewer** with expandable/collapsible structure for structured editing
  - **Code folding indicators**
- **Developer/productivity features:**
  - **Git integration** showing modified, staged, and untracked files in the file tree
  - **Minimap**
  - **Zen mode**
  - **Auto-save**
  - **Session restore**
- **Performance/platform claims:**
  - About **15 MB binary**
  - **Instant startup**
  - Works on **Windows, Linux, and macOS**
- **Release/status notes:**
  - Post announces **v0.2.1** as just released with “major Mermaid improvements”
  - **v0.2.2** is said to be coming soon with **performance improvements for large files**
- **Call to action:** The author is **looking for feedback**
- **Link provided:** GitHub repository at **https://github.com/OlaProeis/Ferrite**

### Assessment
This is a **mixed** announcement/product post with some tool-description content. Durability is **medium** because the core idea of a Rust editor with Mermaid support is stable, but the specifics are tied to **v0.2.1** and an upcoming **v0.2.2**, so feature details may change quickly. Density is **medium**: the post is compact but packed with concrete features, platform claims, and version notes. Originality is **primary source** since it’s the project author’s own Show HN announcement. It’s best used as a **skim-once** or **refer-back** reference to remember what Ferrite offers and whether it’s worth evaluating further. Scrape quality is **good** for the text shown, but it likely omits richer context from the GitHub repo, screenshots, demo details, or deeper implementation notes.
