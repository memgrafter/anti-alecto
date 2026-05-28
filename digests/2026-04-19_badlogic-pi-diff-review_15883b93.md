---
url: https://github.com/badlogic/pi-diff-review
title: badlogic/pi-diff-review
scraped_at: '2026-04-19T08:24:01Z'
word_count: 182
raw_file: raw/2026-04-19_badlogic-pi-diff-review_15883b93.txt
tldr: pi-diff-review is a proof-of-concept pi plugin that adds a native /diff-review window for reviewing Git changes with file search, scope switching, and comment drafting, but the author explicitly calls it “pure slop” and points readers to a pi.dev session for the real idea.
key_quote: Native diff review window for pi, powered by [Glimpse](https://github.com/hazat/glimpse) and Monaco.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: skim-once
scrape_quality: good
people: []
tools:
- pi
- Glimpse
- Monaco
- Tailwind
libraries: []
companies: []
tags:
- git
- code-review
- developer-tools
- plugins
- ui-prototype
---

### TL;DR
`pi-diff-review` is a proof-of-concept `pi` plugin that adds a native `/diff-review` window for reviewing Git changes with file search, scope switching, and comment drafting, but the author explicitly calls it “pure slop” and points readers to a `pi.dev` session for the real idea.

### Key Quote
“Native diff review window for pi, powered by [Glimpse](https://github.com/hazat/glimpse) and Monaco.”

### Summary
- **What it is**
  - A GitHub repo for a `pi` extension called `pi-diff-review`.
  - It is described by the author as “pure slop” and framed as an idea that someone else should improve into something “gud.”
  - It uses **Glimpse** and **Monaco** to build a native diff review experience.

- **Install command**
  - Install via:
    - `pi install git:https://github.com/badlogic/pi-diff-review`

- **What the `/diff-review` command does**
  - Adds a **native review window** to `pi`.
  - Lets you switch between review scopes:
    - `git diff`
    - `last commit`
    - `all files`
  - Includes a **collapsible sidebar** with **fuzzy file search**.
  - Displays **git status markers** for:
    - changed files
    - untracked files
  - **Lazy-loads file contents** as you change files and scopes.
  - Lets you draft comments on:
    - the original side
    - the modified side
    - the whole file
  - Inserts the resulting **feedback prompt** into the `pi` editor after submission.

- **Requirements**
  - Works on:
    - macOS
    - Linux
    - Windows
  - Requires:
    - Node.js 20+
    - `pi` installed
    - internet access for Tailwind and Monaco CDNs

- **Windows-specific notes**
  - Glimpse supports Windows now.
  - Building the native host during install requires:
    - .NET 8 SDK
    - Microsoft Edge WebView2 Runtime

- **Overall character**
  - This is more of a **prototype / demonstration plugin** than polished documentation.
  - The repo is mainly useful if you want to try the feature or inspect how a native diff-review UI for `pi` might work.

### Assessment
**Durability:** medium — the core idea of a native diff-review UI is fairly durable, but the implementation depends on specific tools (`pi`, Glimpse, Monaco CDNs, Node.js 20+, WebView2 on Windows) that may change. **Content type:** mixed, mostly a short tool/plugin reference with installation instructions. **Density:** medium — concise but specific about features and requirements. **Originality:** primary source, since it is the author’s own repo description. **Reference style:** skim-once to quickly identify the plugin, or refer-back if you need install steps and feature list. **Scrape quality:** good — the key README content appears captured, with no obvious missing code blocks or sections beyond this short document.
