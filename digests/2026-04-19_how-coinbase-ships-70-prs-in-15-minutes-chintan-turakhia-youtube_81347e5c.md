---
url: https://www.youtube.com/watch?v=tidINuXB7PA
title: How Coinbase ships 70 PRs in 15 minutes | Chintan Turakhia - YouTube
scraped_at: '2026-04-19T08:13:06Z'
word_count: 10722
raw_file: raw/2026-04-19_how-coinbase-ships-70-prs-in-15-minutes-chintan-turakhia-youtube_81347e5c.txt
tldr: Coinbase engineering leader Chintan Turakhia argues that AI adoption at enterprise scale only sticks when leaders are hands-on builders, and he demonstrates it with workflow changes that collapsed PR, bug-fix, and feedback cycles from hours or days into minutes.
key_quote: the worst thing any leader could do is just be like, I decree you must use AI. Come on, no one's going to listen to you.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Claire Bell
- Chintan Turakhia
- Brian
tools:
- Cursor
- GitHub Copilot
- Linear
- Slack
- Datadog
- Sentry
- Amplitude
- Snowflake
- Claude Opus 4.5
- ChatGPT
libraries: []
companies:
- Coinbase
- Work OS
- Atlassian
- OpenAI
- Perplexity
- Cursor
tags:
- ai-adoption
- engineering-leadership
- developer-productivity
- workflow-automation
- enterprise-ai
---

### TL;DR
Coinbase engineering leader Chintan Turakhia argues that AI adoption at enterprise scale only sticks when leaders are hands-on builders, and he demonstrates it with workflow changes that collapsed PR, bug-fix, and feedback cycles from hours or days into minutes.

### Key Quote
“the worst thing any leader could do is just be like, I decree you must use AI. Come on, no one's going to listen to you.”

### Summary
- **Context:** Interview on *How I AI* with Claire Bell and Chintan Turakhia, senior director of engineering at Coinbase, focused on how a team of 1,000+ engineers adopted AI tools successfully.
- **Core thesis:** AI adoption in large engineering orgs is less about mandates and more about:
  - a leader with strong conviction,
  - that leader being hands-on in the tools,
  - and showing practical wins to engineers rather than telling them to use AI.
- **Why earlier attempts failed:**
  - Coinbase had tried tools like GitHub Copilot and early Cursor.
  - Adoption initially looked promising but did not stick because the models/tools were not good enough yet.
  - Engineers quickly dismissed weak tools, and skepticism spread across teams.
- **How adoption stuck:**
  - Chintan used Cursor daily for months, both for coding and admin work.
  - He focused on low-friction, high-toil tasks:
    - unit tests
    - linting
    - bug fixes
    - draft PR creation
    - repetitive paperwork
  - He emphasized “show the engineers, not just tell.”
- **Aha moment / team rollout:**
  - The team created a “Cursor wins” Slack channel to share successful examples.
  - They ran a “Cursor speedrun” where everyone picked trivial tasks and tried to ship quickly.
  - Reported result: about **70 PRs in 15 minutes** with roughly **100 people** on the call.
  - A later companywide speedrun with around **800 engineers** reportedly produced **300–400 PRs in 30 minutes** and even broke GitHub under load.
- **Velocity metrics and process changes:**
  - He reframes AI’s value as an **accelerant**, not a headcount replacement.
  - The key metric he cares about is **time from ticket to user-visible change**.
  - They reduced PR review cycle time from about **150 hours** to around **15 hours**.
  - They aim to compress:
    - feedback → ticket
    - ticket → PR ready
    - review → merge
    - merge → customer update
- **Custom internal automation:**
  - Coinbase built an internal agent/bot called **Cloudbot** because of security/compliance needs and platform constraints.
  - It can:
    - create PRs
    - generate plans
    - explain/debug issues
    - use context from tools like **Linear, Slack, Datadog, Sentry, Amplitude, Snowflake**
  - They also built a “superb builder” role: someone whose job is to create more superb builders.
- **Feedback workflow example:**
  - Live product feedback from audio/video is captured.
  - An LLM summarizes the issue and suggests a fix.
  - The system creates a **Linear ticket**.
  - Cloudbot can then generate the **PR** from that ticket.
  - This removes manual summarization, triage, and handoff overhead.
- **Analytics example with Cursor data:**
  - Chintan uses Cursor to analyze Cursor usage itself.
  - He downloads Cursor admin analytics CSVs and asks Cursor to:
    - identify cohorts of users
    - enrich the data
    - generate HTML dashboards
    - produce Slack-ready summaries
    - suggest playbooks for moving users from light/regular usage to power/super-user behavior
  - He describes cohorts like:
    - inactive
    - light users
    - balanced users
    - tab-heavy users
    - agent-heavy users
    - power users / super users
- **Cultural insight:**
  - Engineering leadership can become more tactical and less meeting-heavy when AI handles more coordination work.
  - He says his calendar is “almost empty” because coordination overhead has dropped.
  - He spends more time coding, debugging, and making technical decisions.
- **Personal AI use cases:**
  - Converts school emails into calendar invites.
  - Photographs wine menus or champagne tasting notes and asks an LLM to infer taste preferences and recommend bottles.
  - These examples are used to show AI’s utility for everyday decision-making and preference modeling.
- **Closing points:**
  - If you want career growth, being one of the most AI-literate builders in your org is a major opportunity.
  - Coinbase is hiring frontend, backend, design, and ML engineers / “super builders.”
  - The episode ends with a call to try the Coinbase consumer social app built from the former Coinbase Wallet product.

### Assessment
This is a **mixed** content piece: part interview, part opinion, part practical tutorial, and part product demo. **Durability is medium** because the core management lessons about AI adoption, hands-on leadership, and reducing coordination overhead are fairly timeless, but many specifics are tied to current tools and model quality (Cursor, Claude Opus 4.5, Linear, Slack, GitHub, MCPs) and to Coinbase’s 2025 product transition. **Density is high**: it includes concrete workflow designs, metrics, tool names, and process examples rather than broad platitudes. **Originality is primarily commentary** with some first-hand operational detail from a primary practitioner; it is not a neutral study but a real-world narrative of how Coinbase is applying AI. This is best used **refer-back** rather than deep-study: useful as a playbook for AI adoption, workflow automation, and engineering leadership patterns. **Scrape quality is good** overall, though it’s a transcript-like capture with some repetition, filler, and speech artifacts; no major sections or code blocks appear missing, but there are no visuals beyond descriptions, so any on-screen demos are only represented in text.
