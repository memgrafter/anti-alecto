---
url: https://news.ycombinator.com/item?id=47783940
title: 'Ask HN: Who is using OpenClaw? | Hacker News'
scraped_at: '2026-04-19T22:00:32Z'
word_count: 29907
raw_file: raw/2026-04-19_ask-hn-who-is-using-openclaw-hacker-news_cb347fe3.txt
tldr: 'Hacker News’ “Ask HN: Who is using OpenClaw?” thread splits between people using it for personal assistants, daily briefs, note/memory workflows, and niche automations, and skeptics who say the same jobs are better handled by scripts, Claude Code, or cron—while `lexandstuff` says his Obsidian-backed setup is genuinely handy, not magical, and costs about $20/month now.'
key_quote: I still use it and find it helpful. My OpenClaw instance uses an Obsidian project as its memory.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- lexandstuff
- brtkwr
- dsiegel2275
- mjsweet
- ryanmcgarvey
- piazz
- Misterchocolat
- Claude
- Anthropic
- OpenAI
- Google
- NVIDIA
- Jensen
tools:
- OpenClaw
- NanoClaw
- Hermes Agent
- Claude Code
- Codex
- Obsidian
- Telegram
- WhatsApp
- Discord
- Slack
- Gmail
- Xero
- Anki
- Home Assistant
- Tailscale
- Matrix
- Proxmox
libraries:
- Ollama
- N8N
companies:
- Hacker News
- Anthropic
- OpenAI
- Google
- Nvidia
- Tencent
- Town
- Xero
- GitHub
tags:
- ai-agents
- automation
- personal-productivity
- security
- obsidian
---

### TL;DR
Hacker News’ “Ask HN: Who is using OpenClaw?” thread splits between people using it for personal assistants, daily briefs, note/memory workflows, and niche automations, and skeptics who say the same jobs are better handled by scripts, Claude Code, or cron—while `lexandstuff` says his Obsidian-backed setup is genuinely handy, not magical, and costs about $20/month now.

### Key Quote
“I still use it and find it helpful. My OpenClaw instance uses an Obsidian project as its memory.”

### Summary
- **Top comment (verbatim):** "I still use it and find it helpful."
- **Top commenter:** `lexandstuff`
- **Thread topics:**
  - OpenClaw as a personal assistant with persistent memory stored in Obsidian/Markdown
  - Cost, reliability, and whether it’s better than cron jobs / scripts / Claude Code
  - Privacy/security concerns around giving agents access to email, chat, and files
  - Real-world use cases: family history archiving, daily briefings, todo/reminder management, calorie logging, support triage, and research summaries
  - Whether OpenClaw is a real product category or mostly hype / token-burning

- **Main thread theme:** people are testing whether OpenClaw is useful as an “always-on” agent layer for personal and small-business workflows, especially when paired with messaging apps and a note vault, but many commenters argue that the same tasks are more reliable, cheaper, and safer as deterministic scripts or direct AI coding tools.

- **Strong pro-use cases from the thread:**
  - `lexandstuff`:
    - Uses OpenClaw via **WhatsApp** as a day-to-day LLM.
    - Memory lives in an **Obsidian project** that is just **version-controlled Markdown**, not lock-in.
    - Uses it for:
      - calorie/weight/workout tracking
      - to-do lists and reminders
      - life admin tasks
    - Says it did **not** produce a “10x productivity boost,” but is “handy.”
    - Cost changed from roughly **$100–150/month** on Opus 4.5/6 to about **$20/month** after switching to **Codex + ChatGPT Plus**.

  - `brtkwr`:
    - Uses a bot in a **family Telegram group** to ask relatives for stories and build a **rich family history spanning ~50 family members**.
    - Says the family knows it’s a bot and that it’s taking notes.
    - The bot asks informed follow-up questions because it has the family history in context.

  - `dsiegel2275`:
    - Nightly workflow:
      - OpenClaw pulls changes from a private GitHub repo containing an **Obsidian vault**
      - detects new notes
      - runs a **“create flashcard”** skill
      - inserts cards into a custom spaced-repetition app via API
    - Workflow turns class notes into flashcards by the next day.

  - `mjsweet`:
    - Professional maintenance gardener using NanoClaw/OpenClaw-style setup:
      - schedules jobs in a custom job tool via MCP
      - watches Gmail for work orders
      - analyzes job photos via Telegram
      - generates **14–32 page PDF proposals** in LaTeX
      - drafts Gmail emails
      - creates Xero invoices/contacts
    - Says this saves time on truck-bound admin work and helps with family life.
    - Later says OpenClaw felt like the **biggest security regression ever** and that NanoClaw is just Claude inside an Apple container.
  
  - `ryanmcgarvey`:
    - Uses it to stay in one context and avoid app switching.
    - Examples:
      - emailing contractors/accountants
      - looking up relevant threads/details
      - drafting and reviewing messages
      - generating small productivity apps via GitHub/Vercel
    - Emphasizes reduced friction and faster execution.

  - `piazz`:
    - Uses it daily for:
      - calorie/macros
      - todos and Obsidian wrangling
      - family tech support
      - Anki integration
      - reminders
      - light mental-health support
      - Japanese study
    - Likes Telegram as a UI and prefers it over vanilla chat apps because it can use his personal context.

- **Other concrete uses mentioned:**
  - morning briefs / daily digests from email, calendar, HN, Twitter, RSS
  - weather and run-time recommendations
  - stargazing recommendations
  - home server management
  - support ticket triage
  - sales/strategy brainstorming
  - research summaries and literature review
  - LinkedIn outreach automation
  - grocery/menu planning
  - chatbot-style family or group assistants
  - voice-note journaling
  - code repo maintenance and PR generation
  - ERP issue fixing and GitHub PR creation
  - personalized “coach” or “tough coach” agents

- **Major skeptical arguments:**
  - Many users say the same workflows are better as:
    - **cron jobs**
    - **shell scripts**
    - **Claude Code / Codex**
    - deterministic pipelines with LLMs used only where needed
  - Common complaints:
    - brittle integrations
    - token cost
    - security and prompt-injection risk
    - setup complexity
    - “it fixed itself” but still breaks later
    - too much bloat / too many features / confusing dashboard
  - Several commenters say the tool is more useful to **non-programmers** or people who want a low-friction interface than to engineers who can script things themselves.
  - Some argue the hype is manufactured or that it mainly exists to burn tokens / signal status.

- **Security / trust concerns recur heavily:**
  - Giving an always-on agent access to email, calendars, files, chats, or bank-like accounts is described as risky.
  - Some users sandbox it in:
    - Docker
    - VPS
    - isolated VM
    - separate accounts with limited permissions
  - Several comments mention prompt injection, lockouts, or permission-model conflicts.
  - One commenter says they would not trust it near personal data unless deeply sandboxed.

- **Cost and model access are a major theme:**
  - Expensive when using top-tier models like Opus.
  - Some users mention switching to cheaper models:
    - **Minimax**
    - **Qwen**
    - **Gemma**
    - **GLM**
    - local models
  - Others mention OpenAI/Claude subscription changes and API restrictions as reasons to move away.

- **Pattern in the thread’s opinions:**
  - **Enthusiasts:** OpenClaw is a convenient, always-on interface that lowers friction for daily life admin and cross-app workflows.
  - **Pragmatists:** it’s useful, but mainly as a wrapper around deterministic scripts, with LLMs only where judgment is needed.
  - **Skeptics:** it’s fragile hype, too insecure, too expensive, and often no better than tools people already have.
  - **Non-developer angle:** multiple commenters think the value is mostly for people who are not already comfortable writing automation.

- **Notable thread moments:**
  - The family-history bot debate: one person calls it creepy and “mind zombie”-like; others defend archival as important, especially for preserving elders’ memories.
  - A commenter notes that `lexandstuff`’s setup is less “locked in” than it sounds because it’s just Markdown files and folders.
  - Several users mention that Claude Code / scheduled routines or remote-control features are now eating some of OpenClaw’s use cases.
  - A few commenters say they’ve moved to Hermes Agent, NanoClaw, or custom harnesses because OpenClaw became too bloated or brittle.

### Assessment
This is a high-density, highly relevant social thread capturing a broad snapshot of OpenClaw’s real-world adoption, skepticism, and replacement-by-scripts sentiment. Durability is **medium**: the core arguments about agentic workflows, reliability, security, and “why not just use cron/scripts?” are fairly timeless, but specific model names, subscriptions, and product comparisons will age quickly. Content type is **mixed**: mostly opinion/commentary, with some concrete usage reports and mini-case studies. Originality is **primary social discussion / commentary** rather than a synthesized article; the value is in the lived examples and disagreement patterns, not a single authoritative conclusion. Reference style is **refer-back** if you want to remember the shape of the debate, the common use cases, or the security/cost objections. Scrape quality is **good** overall: the thread is largely captured with many replies and concrete examples, though the page includes noisy HN header text, some truncated links, and the sheer size means the capture is unwieldy rather than clean. For **find**, this is the thread where people cite an Obsidian-backed WhatsApp assistant, a family-history Telegram bot spanning ~50 relatives, a nightly flashcard generator from an Obsidian vault, and a cost comparison that drops from roughly **$100–150/month** to about **$20/month** after switching models.
