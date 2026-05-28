---
url: https://www.reddit.com/r/ClaudeAI/comments/1oeutj8/haiku_45_is_insane_in_claude_code/
title: 'Haiku 4.5 is insane in Claude Code! : ClaudeAI'
scraped_at: '2026-04-19T21:39:34Z'
word_count: 2627
raw_file: raw/2026-04-19_haiku-4-5-is-insane-in-claude-code-claudeai_aeee43c4.txt
tldr: 'Reddit thread in r/ClaudeAI debating whether Haiku 4.5 is “insane” in Claude Code: OP says it’s extremely fast and cheap for a real app build, while top commenter `u/n00b_whisperer` says it creates more cleanup work than it saves.'
key_quote: “oh yes it's fast it created a ton of work for sonnet to fix in no time”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: skim-once
scrape_quality: partial
people:
- Electronic-Air5728
- n00b_whisperer
- merx96
- QuantWizard
- Aperturebanana
- ravencilla
- iwdnPRAY
- Dry_Pomegranate4911
- ConversationBrave998
- TheOriginalSuperTaz
- RickySpanishLives
tools:
- Claude Code
- Claude Sonnet
- Haiku 4.5
- Sonnet 4.5
- Opus
- Codex
- SuperClaude
- MCPS
- Firebase
- Next.js
- Invidious
libraries: []
companies:
- Anthropic
- GitHub
tags:
- claude-code
- llm-coding
- model-comparison
- ai-programming
- software-development
---

### TL;DR
Reddit thread in r/ClaudeAI debating whether Haiku 4.5 is “insane” in Claude Code: OP says it’s extremely fast and cheap for a real app build, while top commenter `u/n00b_whisperer` says it creates more cleanup work than it saves.

### Key Quote
“oh yes it's fast it created a ton of work for sonnet to fix in no time”

### Summary
- **Thread context**
  - Subreddit: r/ClaudeAI
  - Title: **“Haiku 4.5 is insane in Claude Code!”**
  - Author: `u/Electronic-Air5728`
  - Score: **352**
  - Comment count reported: **154**
- **Top comment (verbatim):** “oh yes it's fast it created a ton of work for sonnet to fix in no time”
- **Top commenter:** `u/n00b_whisperer`
- **Thread topics:**
  - Haiku 4.5 speed vs correctness in Claude Code
  - Whether cheaper/faster models create hidden rework
  - Sonnet vs Opus vs Haiku for coding workflows
  - Greenfield app builds vs refactors / long-running projects
  - Prompting, compaction, and instruction-following quality

- **OP’s main claim**
  - Haiku 4.5 is extremely productive in Claude Code and feels much faster than Sonnet for app development.
  - OP says they were working on an app for **4 hours**, feeding it “thousands upon thousands of lines of logs,” and the conversation had been compacted **7–8 times**.
  - They report being at only **41%** of their current session usage on the Pro plan, with weekly usage at **12%**, and call the value “insane.”

- **Concrete example OP later gives**
  - The app is a **personal YouTube dashboard**:
    - like a private Netflix-like interface for YouTube channels
    - lets you add favorite channels, organize them into folders, create playlists, and browse videos in one UI
    - uses **Invidious** (self-hosted YouTube alternative) to avoid rate limits and tracking
  - OP says they built the **entire app in 2 sessions**, including:
    - full architecture design: **NAS + Invidious + Next.js + Firebase**
    - complete React UI: sidebar, folders/playlists, video grid, modal player
    - custom hooks: `useFirebaseChannels`, `useFeaturedChannels`, `useChannelSearch`, `useUIState`
    - Firebase Firestore integration
  - When someone suggested YouTube rate limits, OP replied: **“That is why I self-hosted Invidious.”**

- **Main pushback from commenters**
  - The dominant skeptical view is that Haiku may be fast, but it often produces sloppy output that Sonnet has to repair.
  - Several commenters describe the model as suitable only if you carefully review code or if the task is very constrained.
  - `u/merx96` explicitly asks for specifics: “Write down what specific tasks you do. Everyone has different tasks, and your post is not informative.”
  - Another common criticism: a model can look productive while generating extra files, wrong assumptions, or hidden bugs.

- **Representative opposing experiences**
  - Some users say **Sonnet 4.5** or **Opus** still outperform Haiku for reliability, deeper reasoning, or refactors.
  - Others say they prefer Sonnet over Opus because Opus is slower and still makes similar mistakes.
  - A few commenters say Claude Code works well for them generally, and that careful instructions, examples, end-to-end testing, and review are key.
  - One commenter describes Haiku as fast but ineffective on a real project, creating unnecessary `.md` files and not solving the problem.
  - Another says Haiku is useful as a fast tool-call engine, but they still swap back to Sonnet for quality.

- **Discussion pattern**
  - The thread splits into:
    - **“Haiku is fast and valuable”** camp, usually emphasizing greenfield builds, workflow speed, and low usage burn
    - **“Fast but error-prone”** camp, emphasizing rework, hidden bugs, and poor reliability on complex or evolving codebases
  - Several users note that **building from scratch** is where these models shine; adding features later or refactoring existing code is where problems multiply.
  - The conversation also includes side debates about prompt style, tone, sycophancy, compaction memory loss, and how different people appear to get very different results from Claude Code.

### Assessment
This is a **mixed social thread** with high relevance for people evaluating Claude Code model choices, but it is highly tied to the specific moment of **Haiku 4.5 / Sonnet 4.5 / Opus** usage patterns, so durability is **medium** rather than timeless. The content type is **mixed**: part announcement-style praise post, part opinion debate, part practical workflow discussion. Density is **medium-high** because it contains concrete usage figures, model names, stack details, and real workflow examples, though a lot of the thread is repetitive argumentation. Originality is mainly **commentary**: the OP offers firsthand anecdotal experience, while commenters add reactions and contrasting anecdotes rather than new evidence. As a reference, this is best for **skim-once / refer-back** use when comparing Claude models for coding; it is not deep-study material. Scrape quality is **partial**: the main post and many comments are captured, but some comments are deleted/removed, and at least one long reply is visibly truncated mid-sentence, so the thread is incomplete.
