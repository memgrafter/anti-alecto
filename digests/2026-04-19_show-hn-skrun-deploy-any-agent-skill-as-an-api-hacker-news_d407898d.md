---
url: https://news.ycombinator.com/item?id=47689319
title: 'Show HN: Skrun – Deploy any agent skill as an API | Hacker News'
scraped_at: '2026-04-19T22:04:46Z'
word_count: 691
raw_file: raw/2026-04-19_show-hn-skrun-deploy-any-agent-skill-as-an-api-hacker-news_d407898d.txt
tldr: Hacker News thread on Skrun, a tool for exposing “agent skills” as APIs; u/frizull says it lets you deploy a skill in under 2 minutes, while the thread centers on security risks, model commoditization, and whether the skill registry can become genuinely useful.
key_quote: With this project you can expose your skills as an API endpoint in under 2 minutes.
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: skim-once
scrape_quality: good
people:
- frizull
- jonnycoder
- sergioisidoro
- Tarcroi
- 7777777phil
- rohitghumare
tools:
- Skrun
- Claude Code
- Codex
- SkillKit
libraries: []
companies:
- Hacker News
tags:
- agent-tools
- api-design
- prompt-injection
- model-commoditization
- sandboxing
---

### TL;DR
Hacker News thread on **Skrun**, a tool for exposing “agent skills” as APIs; **u/frizull** says it lets you deploy a skill in under 2 minutes, while the thread centers on security risks, model commoditization, and whether the skill registry can become genuinely useful.

### Key Quote
“**With this project you can expose your skills as an API endpoint in under 2 minutes.**”

### Summary
- **Top comment (verbatim):** "Hey HN.My colleague built this because he wanted to use his skills outside of Claude Code.With this project you can expose your skills as an API endpoint in under 2 minutes.If you could have a look at the repo and give your feedback, it would be much appreciated.Thanks!"
- **Top commenter:** `u/frizull`
- **Thread topics:**
  - Turning agent skills into API endpoints
  - Security concerns around public exposure and prompt injection
  - Multi-model / model-provider switching and “commodity” model layers
  - Whether a skill registry can have network effects or stays a flat directory
  - Comparison with SkillKit and similar products

- **What Skrun is**
  - A Show HN project on GitHub: `skrun-dev/skrun`
  - Described as a way to **deploy agent skills as API endpoints** quickly, “in under 2 minutes”
  - Framed as a way to use skills outside of Claude Code

- **Main reactions**
  - `u/jonnycoder` says it looks clever and could be a cleaner alternative to custom plugins and MCP servers for code reviews.
    - Mentions using different models to review each other’s plans after perceived degradation in Claude over the past 1–2 months.
    - Likes the idea of isolating tool-calling security in an ephemeral sandbox.
  - `u/sergioisidoro` warns this would be a **security nightmare** if published publicly, especially due to **prompt injection** and data exfiltration.
    - In reply, `u/Tarcroi` says it’s currently local only and public deployment would need sandboxes and verification steps, though prompt injection can’t be fully eliminated.
  - `u/7777777phil` argues auto-switching across model providers implies the model layer is a commodity.
    - Raises the open question of whether the registry gains network effects or remains a flat directory.
    - Connects the idea to a broader trend of agent stacks becoming modular and swappable, with value shifting to encoded process knowledge.
    - Links to a related enterprise perspective article.
    - `u/Tarcroi` agrees with the commodity-model view and says multi-model support was planned from the start.
    - Notes interest in adding usage data like **success rates, cost, and trust scores** so the registry can recommend the best-working skills.
  - `u/rohitghumare` says **SkillKit.sh** already does something similar and was ranked #3 on Product Hunt.
    - `u/Tarcroi` responds that it’s different: **SkillKit distributes skills to agents**, while **Skrun runs them as APIs**.

- **Overall tone / discussion pattern**
  - The thread is mostly short, practical feedback rather than deep debate.
  - The strongest concerns are around **security** and **public deployment risk**.
  - The most substantive technical discussion is about **multi-model strategy**, **sandboxing**, and **whether a registry can become a valuable layer**.

### Assessment
This is a **mixed** content type: primarily a **Show HN announcement** with commentary and light technical discussion. Durability is **medium**: the broad ideas around agent skills, API wrappers, sandboxes, and prompt injection are durable, but the specific project and comparisons are tied to current tooling and HN context. Density is **medium**; it’s concise but includes several concrete opinions and implementation hints (local-only deployment, planned sandboxes, RuntimeAdapter, usage metrics). Originality is mostly **commentary** rather than primary research, though the OP’s brief project description is a primary-source product pitch. Reference style is **skim-once** unless you’re tracking agent-infrastructure trends or this specific project. Scrape quality is **good**: it captures the title, metadata, top comments, and a representative discussion sample, though it does not include the linked repo content itself.
