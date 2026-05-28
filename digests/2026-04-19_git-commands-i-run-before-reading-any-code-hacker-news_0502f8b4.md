---
url: https://news.ycombinator.com/item?id=47687273
title: Git commands I run before reading any code | Hacker News
scraped_at: '2026-04-19T22:04:34Z'
word_count: 3661
raw_file: raw/2026-04-19_git-commands-i-run-before-reading-any-code-hacker-news_0502f8b4.txt
tldr: Hacker News thread about a blog post on Git commands to run before reading unfamiliar code, where the top comment says the heuristics are helpful and that they also argue for good Git discipline.
key_quote: These are some helpful heuristics, thanks.This list is also one of many arguments for maintaining good Git discipline.
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- grepsedawk
- gherkinnn
- pzmarzly
- ramon156
- seba_dos1
- palata
- Jenk
- martinvonz
tools:
- git
- jj
- jujutsu
libraries: []
companies:
- Hacker News
tags:
- git
- codebase-analysis
- version-control
- jujutsu
---

### TL;DR
Hacker News thread about a blog post on **Git commands to run before reading unfamiliar code**, where the top comment by **u/gherkinnn** says the heuristics are helpful and that they also argue for **good Git discipline**.

### Key Quote
"These are some helpful heuristics, thanks.This list is also one of many arguments for maintaining good Git discipline."

### Summary
- **Context**
  - HN discussion of the linked post: **“Git commands I run before reading any code”** by **grepsedawk**
  - Thread stats: **2333 points**, **180 comments**, but only **4 top-level comments captured** in this scrape

- **Top comment (verbatim):** "These are some helpful heuristics, thanks.This list is also one of many arguments for maintaining good Git discipline."
- **Top commenter:** `u/gherkinnn`
- **Thread topics:**
  - Pre-reading Git inspection heuristics for understanding a codebase
  - Whether the same workflow can be expressed in **Jujutsu (`jj`)**
  - How much value tools like **jj** add versus standard Git
  - Tradeoffs around Git discipline, rebasing, signing, aliases, and commit history quality

- **What the thread is mainly about**
  - The linked article appears to be a practical “before you read the code, inspect the repo history” guide.
  - The thread treats these commands as a way to answer questions like:
    - what files change most
    - who changed the code most
    - where bug-fix activity clusters
    - whether a project is accelerating or stagnating
    - whether the team is firefighting
  - The most visible replies are less about the article itself and more about how these ideas map to **jj** and whether **jj** is worth adopting.

- **Concrete discussion points from prominent replies**
  - **u/pzmarzly** posts **Jujutsu equivalents** using `jj log` with revsets and templates for:
    - “What Changes the Most”
    - “Who Built This”
    - “Where Do Bugs Cluster”
    - “Is This Project Accelerating or Dying”
    - “How Often Is the Team Firefighting”
  - **u/ramon156** questions the “most changed file” heuristic, noting the top file is often the one people are afraid to touch.
  - **u/seba_dos1** argues squash-merge workflows lose information and are unnecessary because Git already stores author and committer separately.
  - The longer discussion drifts into a broader **Git vs jj** debate:
    - jj is praised for ergonomic rebases and stacked diffs
    - critics say Git already works well, is ubiquitous, and jj can feel like extra complexity
    - signing, conflict handling, compatibility, and submodules come up as practical friction points

- **Useful anchor details for finding the source later**
  - HN item ID: **47687273**
  - Title: **Git commands I run before reading any code**
  - Author: **grepsedawk**
  - Linked article URL: **https://piechowski.io/post/git-commands-before-reading-code/**
  - Prominent command family discussed: `git log`-style repo archaeology and `jj log` equivalents

### Assessment
This is a **mixed** content type: mostly a **social thread** reacting to a practical Git article, with some technical commentary and tool comparison. **Durability** is medium to high: the specific Git heuristics and the Git-vs-jj arguments will stay relevant, but the exact thread context and any tool-specific syntax can age as versions and community opinions change. **Density** is medium: the thread contains a lot of concrete command ideas and implementation debate, but the scrape only captures a small slice of the full conversation. **Originality** is mostly **commentary/synthesis** rather than primary research, though the linked blog post itself appears to be the original source of the Git workflow. For **reference style**, this is best as **refer-back** material if you want the command patterns or the Git/jj comparison, and **skim-once** if you only want the gist. **Scrape quality** is **partial**: the capture includes the thread metadata and a useful sample of comments, but only **4 top-level comments** out of **180**, and some replies are visibly truncated mid-command and mid-paragraph, so important context and exact wording from the full discussion are missing.
