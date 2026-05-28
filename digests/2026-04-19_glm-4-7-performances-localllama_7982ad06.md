---
url: https://www.reddit.com/r/LocalLLaMA/comments/1q37jz3/glm_47_performances/
title: 'GLM 4.7 performances : LocalLLaMA'
scraped_at: '2026-04-19T21:35:43Z'
word_count: 401
raw_file: raw/2026-04-19_glm-4-7-performances-localllama_7982ad06.txt
tldr: Reddit thread on r/LocalLLaMA where u/AppealRare3699 says GLM 4.5/4.6/4.7 perform poorly in CLI tasks, and the top reply from u/Zealousideal-Ice-847 argues that z.ai may be routing requests to other models unless you use OpenRouter, while another commenter suggests the issue may just be misconfiguration.
key_quote: Use open router not the zai one, they sneakily route some requests to 4.5 air and 4.6 for cache or response which lowers the output quality
durability: low
content_type: mixed
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- u/AppealRare3699
- u/Zealousideal-Ice-847
- u/Automatic-Outcome389
- u/No_Afternoon_4260
- u/websitegest
- u/leonbollerup
- u/AlwaysInconsistant
tools:
- OpenRouter
- z.ai
- Claude
- Codex
libraries: []
companies:
- z.ai
- OpenRouter
tags:
- local-llm
- model-routing
- coding-assistants
- reddit-discussion
- cli-workflows
---

### TL;DR
Reddit thread on r/LocalLLaMA where u/AppealRare3699 says GLM 4.5/4.6/4.7 perform poorly in CLI tasks, and the top reply from u/Zealousideal-Ice-847 argues that z.ai may be routing requests to other models unless you use OpenRouter, while another commenter suggests the issue may just be misconfiguration.

### Key Quote
“Use open router not the zai one, they sneakily route some requests to 4.5 air and 4.6 for cache or response which lowers the output quality”

### Summary
- **Thread topic:** whether GLM 4.7 is actually underperforming for coding/CLI work, and whether the problem is model quality, provider routing, or user setup.
- **Top comment (verbatim):** “Use open router not the zai one, they sneakily route some requests to 4.5 air and 4.6 for cache or response which lowers the output quality”
- **Top commenter:** `u/Zealousideal-Ice-847`
- **Thread topics:**
  - alleged provider-side routing from GLM 4.7 to other models on z.ai
  - whether OpenRouter gives more consistent output than z.ai directly
  - GLM Coding plan vs other plans and billing/usage behavior
  - whether inconsistent results are due to routing or user misconfiguration
  - practical coding/CLI performance versus Claude and Codex

- **Original post:** u/AppealRare3699 says they’ve used GLM 4.5, 4.6, and 4.7 and “it’s not really good” for their CLI tasks, while Claude and Codex work fine.
- They ask if others have the same problem with z.ai models or have tips for using them well.

- **Main pro-routing claim (u/Zealousideal-Ice-847):**
  - recommends using **OpenRouter** instead of **z.ai**
  - claims z.ai “sneakily route[s] some requests to 4.5 air and 4.6”
  - says that lowers output quality
  - later says the **Coding plan** should still show this in the billing/usage panel

- **Evidence/discussion around that claim:**
  - u/Automatic-Outcome389 agrees z.ai has been “sketchy” with routing lately and describes outputs as inconsistent / “model roulette”
  - u/AppealRare3699 says they only see **GLM 4.7 requests** in billing, not 4.5 air or 4.6
  - a screenshot/image link is posted in the thread, but the capture only includes the link text, not the image itself
  - u/No_Afternoon_4260 suggests: “Seems you misconfigured something”

- **Alternative viewpoint / usage note:**
  - u/websitegest says **429 rate-limit errors** on Lite/Pro GLM plans hurt productivity
  - they report **GLM 4.7 on the Coding plan** has much better availability over 2 weeks
  - they say it does **not beat Opus on complex debugging**, but is **faster for implementation cycles** because they aren’t waiting on rate limits
  - they also mention a **30% discount** offer and include a z.ai subscription link, which reads like promotional/affiliate-style content

- **Small thread dynamic:**
  - The thread does **not** reach a firm consensus.
  - One camp says quality issues may come from z.ai’s routing behavior.
  - Another says the problem may be setup/configuration.
  - A practical concern also appears: plan availability and 429s may matter more than raw model quality for some users.

### Assessment
This is a **mixed** Reddit discussion with **low-to-medium durability**: the specific claims about z.ai routing, billing panels, and plan behavior could become stale quickly if the platform changes, but the broader question of model consistency versus provider routing is a recurring issue. It is **commentary** rather than primary evidence, with one promotional reply mixed in, so trustworthiness is limited and the routing claim is unverified in this capture. The thread is **medium density** for a small discussion: it contains a few concrete claims, plan names, and user experiences, but not deep technical analysis. For **recall**, it works well because it preserves the main dispute and the exact top claim; for **decide**, it’s useful only if you want anecdotal reports about GLM 4.7 on z.ai/OpenRouter; for **find**, the key identifiers are r/LocalLLaMA, “GLM 4.7 performances,” u/AppealRare3699, and the OpenRouter/routing-to-4.5-air/4.6 allegation. **Scrape quality is partial**: the post text and comment structure are captured, but linked screenshot images are not viewable here, so any visual evidence in those image links cannot be verified from this scrape.
