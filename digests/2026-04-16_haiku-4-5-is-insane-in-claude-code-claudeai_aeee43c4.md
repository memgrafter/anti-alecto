---
url: https://www.reddit.com/r/ClaudeAI/comments/1oeutj8/haiku_45_is_insane_in_claude_code/
title: 'Haiku 4.5 is insane in Claude Code! : ClaudeAI'
scraped_at: '2026-04-16T06:32:55Z'
word_count: 2627
raw_file: raw/2026-04-16_haiku-4-5-is-insane-in-claude-code-claudeai_aeee43c4.txt
tldr: A r/ClaudeAI thread claims Haiku 4.5 in Claude Code is “insane” for rapidly building a self-hosted YouTube dashboard with Invidious, Next.js, and Firebase, using only 41% of a Pro session and 12% of weekly usage — but commenters push back hard, saying Haiku is fast yet error-prone and often creates cleanup work for Sonnet.
key_quote: It’s so good! I’ve never built apps so fast, and it does super well.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- u/Electronic-Air5728
- u/n00b_whisperer
- u/merx96
- u/QuantWizard
- u/Aperturebanana
tools:
- Claude Code
- Invidious
- Next.js
- Firebase
- Sonnet
- Opus
libraries: []
companies:
- Anthropic
tags:
- claude-code
- llm-coding
- web-development
- reddit-discussion
- ai-models
---

### TL;DR
A r/ClaudeAI thread claims Haiku 4.5 in Claude Code is “insane” for rapidly building a self-hosted YouTube dashboard with Invidious, Next.js, and Firebase, using only 41% of a Pro session and 12% of weekly usage — but commenters push back hard, saying Haiku is fast yet error-prone and often creates cleanup work for Sonnet.

### Key Quote
“It's so good! I've never built apps so fast, and it does super well.”

### Summary
- **Post context**
  - Reddit thread in **r/ClaudeAI**
  - Title: **“Haiku 4.5 is insane in Claude Code!”**
  - Author: **u/Electronic-Air5728**
  - Score: **343**
  - Reported comment count: **154**

- **Original claim**
  - The author says **Haiku 4.5** is dramatically speeding up app development in **Claude Code**.
  - They report working on an app for **4 hours**, feeding it **“thousands upon thousands of lines of logs,”** and having the conversation compacted **7–8 times** with thinking on.
  - Despite that, they were only at **41% session usage** on the Pro plan, with reset time shown as **1pm (Europe/Copenhagen)**.
  - They also say they repeated similar work the previous day and were only at **12% weekly usage**.
  - Core takeaway from the post: **the value proposition feels “insane” because it is both fast and cheap on usage**.

- **What the app is**
  - The author later clarifies they are building a **personal YouTube dashboard**:
    - like a **private Netflix interface for YouTube channels**
    - lets users add favorite channels
    - organize channels into **folders**
    - create **playlists**
    - browse videos in one unified interface
  - The app uses **Invidious** as a self-hosted YouTube alternative to avoid **rate limits** and **YouTube tracking**.

- **What the author says Haiku built**
  - In a follow-up, they claim Haiku helped them build the **entire app in 2 sessions**.
  - Session 1 allegedly covered:
    - full architecture design: **NAS + Invidious + Next.js + Firebase**
    - complete React UI: sidebar with folders/playlists, video grid, modal player
    - custom hooks such as:
      - `useFirebaseChannels`
      - `useFeaturedChannels`
      - `useChannelSearch`
      - `useUIState`
    - Firebase Firestore integration
  - The capture of this follow-up is **truncated**, so the implementation details after the Firestore mention are not fully visible.

- **Main reactions in comments**
  - **Supportive / impressed**
    - Several commenters say Haiku is genuinely fast and can be useful, especially for tool calls or simpler tasks.
    - Some say they switch between **Haiku, Sonnet, and Opus** depending on the task.
    - A few commenters report that Claude Code works well for them in general, especially with strong prompting, examples, and end-to-end checks.

  - **Critical / skeptical**
    - The top reply says Haiku was fast but **“created a ton of work for sonnet to fix”**.
    - Other commenters accuse the post of being promotional or uninformative.
    - Repeated criticism: **fast model output can hide mistakes**, hallucinations, or bad implementation choices.
    - One user describes Haiku as making unnecessary files and failing to solve the real problem.
    - Several commenters argue that **code review and testing are mandatory regardless of model**.

  - **Broader debate**
    - The thread turns into a recurring Claude Code debate:
      - **Sonnet vs Haiku vs Opus**
      - speed vs quality
      - whether compacted conversations degrade performance
      - whether better prompting, examples, and agent orchestration solve the problems
    - Some commenters insist **Sonnet 4.5** is the practical sweet spot.
    - Others say **Opus** is better for deep reasoning but too slow or expensive.

- **Notable point of disagreement**
  - The central divide is whether **Haiku 4.5’s speed and low usage** outweigh its reported tendency to make subtle mistakes.
  - The author sees it as a breakthrough for velocity and cost.
  - Skeptics see it as a model that can move fast while quietly producing cleanup work or bugs.

### Assessment
This is a **mixed** Reddit thread with a **medium** durability: the specific model/version references, usage percentages, and Claude Code behavior are current and likely to age with product changes, but the broader discussion about fast models producing more downstream cleanup is more durable. The content is **high-density** in the parts where the author describes the app stack and usage numbers, but the overall thread is also noisy and argumentative. It is mostly a **commentary / social thread** rather than a primary benchmark, with the original post functioning as anecdotal evidence and the replies offering counterexamples and broader opinions. It’s best used as a **refer-back** source if you want to recall the community’s reaction to **Haiku 4.5 in Claude Code**, especially in the context of a **personal YouTube dashboard built with Invidious, Next.js, and Firebase**. **Scrape quality: partial** — the thread capture includes the main post, selected comments, and a useful follow-up about the app, but at least one technical description is clearly **truncated**, and the full comment thread is not complete.
