---
url: https://www.reddit.com/r/LocalLLaMA/comments/1q37jz3/glm_47_performances/
title: 'GLM 4.7 performances : LocalLLaMA'
scraped_at: '2026-04-16T06:31:48Z'
word_count: 401
raw_file: raw/2026-04-16_glm-4-7-performances-localllama_7982ad06.txt
tldr: A LocalLLaMA thread where the OP says GLM 4.5/4.6/4.7 performs badly for CLI coding tasks, and commenters debate whether the issue is Z.ai routing, plan tier, or misconfiguration, with OpenRouter and the “Coding plan” suggested as fixes.
key_quote: Use open router not the zai one, they sneakily route some requests to 4.5 air and 4.6 for cache or response which lowers the output quality
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- AppealRare3699
- Zealousideal-Ice-847
- leonbollerup
- Automatic-Outcome389
- websitegest
- No_Afternoon_4260
- AlwaysInconsistant
tools:
- OpenRouter
- Claude
- Codex
libraries: []
companies:
- Z.ai
- Reddit
tags:
- local-llm
- cli-coding
- model-routing
- benchmarking
- rate-limits
---

### TL;DR
A LocalLLaMA thread where the OP says GLM 4.5/4.6/4.7 performs badly for CLI coding tasks, and commenters debate whether the issue is Z.ai routing, plan tier, or misconfiguration, with OpenRouter and the “Coding plan” suggested as fixes.

### Key Quote
“Use open router not the zai one, they sneakily route some requests to 4.5 air and 4.6 for cache or response which lowers the output quality”

### Summary
- **Original complaint:**  
  - OP says they’ve been using **GLM 4.5, 4.6, and 4.7** and “it’s not really good” for their **CLI** tasks.
  - They compare it unfavorably to **Claude** and **Codex**, which “been working really fine.”
  - They ask whether others have the same problem with **z.ai models** or have tips for using them well.

- **Main discussion points:**
  - **Routing theory / quality inconsistency:**  
    - One commenter claims users should use **OpenRouter** instead of Z.ai directly because Z.ai allegedly routes some requests to **4.5 Air** and **4.6** for cache/response, which supposedly lowers output quality.
    - Another commenter says Z.ai has been “sketchy” with routing lately and describes this as **“model roulette”** behind the scenes.
  - **Plan tier / availability:**  
    - OP asks whether this advice applies if they use the **Coding plan**.
    - The reply says yes, and suggests checking the **billing usage panel**.
    - OP responds that they only see **GLM 4.7** requests in billing, not 4.5 Air or 4.6.
  - **Alternative explanation: misconfiguration:**  
    - One commenter says it “Seems you misconfigured something.”
  - **Plan/pricing anecdote:**  
    - Another commenter says they had **429 errors** on **Lite/Pro GLM plans**, upgraded, and found **GLM 4.7 on the Coding plan** had much better availability over 2 weeks.
    - They say it still does **not beat Opus on complex debugging**, but is **faster for implementation cycles** because they aren’t waiting on rate limits.
    - They also mention a **30% discount** on GLM plans with an additional 10%, and link to a **z.ai subscribe** URL.

- **Overall thread takeaway:**  
  - The thread is less a settled performance comparison and more a debate over whether poor results come from:
    - **model quality itself**
    - **Z.ai routing behavior**
    - **plan limitations / rate limits**
    - **user configuration**
  - There is no consensus verdict, but **OpenRouter**, **Coding plan**, and **billing/routing checks** are the main troubleshooting ideas.

### Assessment
This is a **mixed**-type Reddit discussion with moderate durability: the specific claims about **GLM 4.7**, **Z.ai routing**, **OpenRouter**, and **429 errors** are tied to a particular service state and can become stale quickly, but the broader lesson about model-routing inconsistencies and plan-tier effects is still useful. The density is **medium**: short but information-rich, with concrete model versions, service names, and error codes. Originality is mainly **commentary** rather than primary research; it’s a user-reported experience plus speculation and advice, not verified benchmarking. Best used as a **refer-back** thread for troubleshooting and comparison, not as deep-study material. **Scrape quality is partial**: the capture reports **11 comments**, but only a subset is shown, and the referenced image links are not directly accessible here, so the thread may be incomplete.
