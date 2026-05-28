---
url: https://lobste.rs/s/sbtjef/spreadsheets_vi_json
title: spreadsheets + vi + json | Lobsters
scraped_at: '2026-04-12T10:33:37Z'
word_count: 623
raw_file: raw/2026-04-12_spreadsheets-vi-json-lobsters_a833c84f.txt
tldr: A developer shares an early proof of concept for a “spreadsheets + vi + JSON” tool that replaces rigid cell grids with JSON-path-addressed data and table support, inviting feedback on whether spreadsheets should evolve into more flexible, API-friendly data structures.
key_quote: “Think of a new form of spreadsheets where the primary data structure is not a rigid grid but a free-form JSON-like structure (but with first class tables support of course).”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: skim-once
scrape_quality: good
people: []
tools:
- vi
- Codeberg
libraries: []
companies:
- Stack Overflow
tags:
- spreadsheets
- json
- prototype
- user-interface
- data-model
---

### TL;DR
A developer shares an early proof of concept for a “spreadsheets + vi + JSON” tool that replaces rigid cell grids with JSON-path-addressed data and table support, inviting feedback on whether spreadsheets should evolve into more flexible, API-friendly data structures.

### Key Quote
“Think of a new form of spreadsheets where the primary data structure is not a rigid grid but a free-form JSON-like structure (but with first class tables support of course).”

### Summary
- The post introduces a **proof of concept** for a spreadsheet-like interface built around a **free-form JSON-like data model** rather than a traditional two-dimensional grid.
- The interface demo uses **vi-style hotkeys**, but the author says the concept is **not dependent on vi bindings**.
- In this model:
  - Data addresses are **JSON paths**.
  - The layout is currently **rigid** because it is only a prototype, but the author imagines a more **canvas-like** layout with more control.
  - Cells can reference other cells via **JSON-based addresses**, including **relative references**.
- The prototype does **not yet support expressions**, though a table example includes a **dynamic column**.
- The author envisions tables as a way to represent **arrays of homogeneous records**, with some columns being **dynamically calculated** or having **default dynamic calculations**.
- Expressions are described as **JavaScript functions**, but the author suggests they could be anything that works with **JSON types**.
- The motivation is that traditional spreadsheets are powerful but limited by their **rigidity**; the author argues they are not ideal for:
  - **Version control**
  - Acting as **authoritative data sources**
  - **Powering APIs**
- The author is explicitly uncertain whether this is the right direction, and says they are mainly trying to **share an early idea** and gather feedback.
- They note the code was **100% manually written** by them, except for a copied **CSS background** from Stack Overflow.
- They invite collaboration and say they may publish the source on **Codeberg** if there is enough interest.
- Comment feedback on the post suggests:
  - Adding an **animated GIF or video** near the top to better show the UI in action.
  - Listing **common use cases** more clearly.
  - Writing a **deeper walkthrough** of one realistic use case.
- The author responds positively, agreeing the project is hard to communicate and that a **realistic demo/use-case** may be the best way to explain it.

### Assessment
This is a **mixed** announcement/commentary post about an early-stage **prototype** rather than a mature tutorial or reference. Its durability is **medium**: the general idea of JSON-based spreadsheet structures is conceptually interesting and not tied to a specific version, but the implementation details and project status are highly provisional. The content is **dense** in architectural ideas but light on concrete technical implementation, so it reads as a **primary-source announcement** with some community discussion. As a reference, it’s best for **skim-once** unless you’re evaluating the project concept or looking for inspiration about alternative spreadsheet models. Scrape quality is **good** for the text shown, though it likely omits the actual demo, images, and any code or linked media that would be important for fully understanding the prototype.
