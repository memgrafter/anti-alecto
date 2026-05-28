---
url: https://news.ycombinator.com/item?id=46710108
title: 'Ask HN: How are you automating your coding work? | Hacker News'
scraped_at: '2026-04-19T21:33:48Z'
word_count: 4243
raw_file: raw/2026-04-19_ask-hn-how-are-you-automating-your-coding-work-hacker-news_0582d845.txt
tldr: 'Hacker News “Ask HN: How are you automating your coding work?” is a thread about practical AI-coding workflows, and the top comment by u/hmokiguess says the key is to tune supervision to project risk: heavy human oversight for compliance-sensitive work, looser AI autonomy for low-risk tasks.'
key_quote: Each project gets its own share of supervision depending on how critical human intervention is needed.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- manthangupta109
- hmokiguess
- denysvitali
- pbohun
- bravura
- simonw
- onlyrealcuzzo
- jmathai
- growthloops
- epolanski
- al_borland
- mjr00
- cadamsdotcom
- anditherobot
- jbreckmckye
- sqircles
- maCDzP
- geiser
- toddmorrow
- theturtletalks
- deterministic
tools:
- Claude Code
- Cursor
- Happy
- Skyportal.ai
- uv run pytest
- AGENTS.md
- CLAUDE.md
- SKILLS.md
- beads
- canopy
- codex-container
- open router
libraries: []
companies:
- Hacker News
- Skyportal.ai
tags:
- ai-coding
- developer-workflows
- coding-agents
- test-automation
- prompt-engineering
---

### TL;DR
Hacker News “Ask HN: How are you automating your coding work?” is a thread about practical AI-coding workflows, and the top comment by **u/hmokiguess** says the key is to tune supervision to project risk: heavy human oversight for compliance-sensitive work, looser AI autonomy for low-risk tasks.

### Key Quote
“Each project gets its own share of supervision depending on how critical human intervention is needed.”

### Summary
- **Thread topic:** how developers are automating coding work with LLMs, agents, scripts, and surrounding tooling rather than just asking “what AI do you use?”
- **Original prompt:** the author says they’re interested in “creative ways people are automating their coding work” given the rise of “vibe coding.”

- **Top comment (verbatim):** “Each project gets its own share of supervision depending on how critical human intervention is needed.I have some complex large and strict compliance projects that the AI is a pair programmer but I make most of the decisions, and I have smaller projects that, despite great impact on the bottom line, can be entirely done unsupervised due to the low risk factor of "mistakes" and the easiness of correcting them after the fact they are caught by the AI as well.”
- **Top commenter:** `u/hmokiguess`

- **Thread topics:**
  - How much autonomy to give coding agents vs. keeping humans in the loop
  - Claude Code, Cursor, and similar tools for drafting/implementing code
  - Using test suites, TDD, and repo templates to make agents more reliable
  - Automation around coding: issue/PR commands, experiment runners, planning tools, context/skill files
  - Limits of LLMs: token/context window costs, hallucinations, need to stop and fix things manually

- **Main patterns people report using:**
  - **Human-supervised pair programming**
    - `u/hmokiguess`: different supervision levels depending on compliance/risk
    - `u/mjr00`: use Claude for mechanical work, but stop when steering it becomes slower than doing it manually
    - `u/jbreckmckye`: use the model more as a reviewer/consultant than as a coder
  - **Agentic coding with guardrails**
    - `u/simonw`: runs **Claude Code for web**, ensures Python repos can pass `uv run pytest`, then tells Claude to run tests and implement changes
    - Uses this to finish ~80% of an idea from an iPhone before returning to a laptop
    - Notes plans/templates for different project types: Datasette plugins, Python libraries, CLI tools, simple HTML+JS tools, some Go apps
  - **Simple command automation**
    - `u/jmathai`: small custom commands like `/gh-issue [issue number]` and `/gh-pr [pr number]` to handle GitHub tasks
  - **Surrounding-work automation, not just coding**
    - `u/growthloops`: uses Cursor/Claude Code for drafts, but more aggressive automation around ML experiments, environment setup, and metric tracking via **Skyportal.ai**
    - `u/bravura`: mentions “beads” for tagging work as `human-spec` or `qa-needed`, plus planned Claude skills to enforce workflow
  - **Documented prompts / skills / codification**
    - `u/cadamsdotcom`: argues for “codification” — turn promptable know-how into reusable scripts/skills so the model can run checks and follow rules without carrying everything in context
    - `u/geiser`: prepares custom `AGENTS.md` files with a prompt-guidance tool
    - `u/maCDzP`: uses `CLAUDE.md`, then `SKILLS.md`, and has Claude write tests, deployment scripts, and commit messages
  - **LLM as helper for understanding code**
    - `u/epolanski`: uses LLMs to connect dots in repos and inspect dependencies, especially in legacy/outdated documentation
    - `u/sqircles`: uses it as a consultant for a closed enterprise system
  - **Side projects benefit more than core work**
    - `u/onlyrealcuzzo`: AI hasn’t been helpful for real work so far, but is a “10x+ multiplier” for side projects

- **Important disagreements / cautions:**
  - Several commenters say LLMs are best for **side projects, mechanical tasks, or exploration**, but not yet trustworthy enough for critical work.
  - `u/al_borland` says it often ends up being “slightly faster web search” and can waste time if pushed too far.
  - `u/mjr00` and others warn that people waste time arguing with the model when a manual fix would be faster.
  - `u/anditherobot` emphasizes token/context efficiency; others push back that cost is often low and the bigger issue is workflow quality, not raw token price.
  - Concerns about unsafe/malicious generated code appear in a subthread under `u/cadamsdotcom`.

- **Notable concrete tools / references mentioned:**
  - **Claude Code**
  - **Cursor**
  - **Happy**
  - **Skyportal.ai**
  - **uv run pytest**
  - **AGENTS.md / CLAUDE.md / SKILLS.md**
  - **beads**, **canopy**, **codex-container**
  - GitHub issue/PR helper commands

### Assessment
This thread has **medium durability**: the specific tool names and model workflows will age quickly, but the underlying patterns—guardrails, testability, codifying workflows, stopping when manual work is cheaper—are durable. It is a **mixed** content type, mostly opinion and practical workflow sharing rather than a tutorial or reference doc. The density is **high** because many top-level comments pack in concrete tools, commands, and workflow patterns. Originality is mostly **commentary / first-hand experience**, not synthesis or primary research. It’s best used as **skim-once or refer-back** depending on whether you want tactical AI-coding ideas, especially around Claude Code, tests, and agent guardrails. **Scrape quality is partial**: the capture preserves many comments, but several are truncated mid-sentence, some top-level entries show misleading `(0)` scores, and the top comment is run together without clean punctuation, which makes verification and quotation a bit messy.
