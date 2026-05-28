---
url: https://www.reddit.com/r/ClaudeCode/comments/1qijtjx/dont_get_zai_glm_coding_plan/
title: 'Don''t get Z.ai GLM Coding Plan : ClaudeCode'
scraped_at: '2026-04-16T06:31:13Z'
word_count: 3474
raw_file: raw/2026-04-16_don-t-get-z-ai-glm-coding-plan-claudecode_34323e77.txt
tldr: A Reddit thread in r/ClaudeCode where the OP warns against Z.ai’s GLM Coding Plan because the annual Max plan feels heavily throttled—especially compared with the much faster pay-as-you-go API—and commenters argue over whether the problem is the plan, concurrency limits, or just how to use multiple models and subagents.
key_quote: z.ai is absolutely throttles coding plans. Indeed it's unlimited in practice because it's so slow there's no chance you'll spend your quota.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- samidhaymaker
- SynapticStreamer
- Lucyan_xgt
- jpcaparas
- HealthyCommunicat
- isakota
- NullzeroJP
- james__jam
tools:
- Claude Code
- OpenCode
- OpenCode Desktop
- Gemini CLI
- Kilo Code
- Cerebras
- agor.live
- autoclaude
libraries: []
companies:
- Z.ai
- OpenAI
- Anthropic
- Cerebras
- Google
- Nvidia
tags:
- coding-assistants
- model-throttling
- subscription-plans
- ai-workflows
- claude-code
---

### TL;DR
A Reddit thread in r/ClaudeCode where the OP warns against Z.ai’s GLM Coding Plan because the annual Max plan feels heavily throttled—especially compared with the much faster pay-as-you-go API—and commenters argue over whether the problem is the plan, concurrency limits, or just how to use multiple models and subagents.

### Key Quote
“z.ai is absolutely throttles coding plans. Indeed it's unlimited in practice because it's so slow there's no chance you'll spend your quota.”

### Summary
- **Original complaint (u/samidhaymaker)**:
  - Bought the **yearly Max Coding Plan** and regrets it.
  - Says **GLM 4.7** is “decent” but far behind **OpenAI** and **Anthropic** models.
  - Main grievance: **the subscription is so throttled that quota is effectively unreachable**.
  - Claims the **pay-as-you-go API is orders of magnitude faster** than the subscription plan.
  - Says the plan is **not even cheap** relative to the performance.

- **Main discussion points in comments**:
  - **Annual vs monthly plans**:
    - Several users argue to **never buy annual plans** in a fast-moving model market.
    - Others say the yearly deal was worth it because it was cheap enough, especially during promotions.
  - **Throughput / concurrency dispute**:
    - One commenter (u/SynapticStreamer) says OP is using the tool wrong and points to **API concurrency limits**:
      - GLM-4.7: 1
      - GLM-4.7-Flash: 1
      - GLM-4.7-FlashX: 3
      - GLM-4.6: 1
      - GLM-4.6V-Flash: 1
      - GLM-4.6V-FlashX: 3
      - GLM-4.6V: 10
    - OP replies that the issue is **throughput**, not just concurrency: he can run sessions, but **still can’t burn tokens fast enough**, and says the plan feels like a bait-and-switch.
  - **Alternative workflows**:
    - Multiple commenters describe using **GLM as one part of a multi-model stack**:
      - Claude / Opus for planning
      - GLM for execution
      - Gemini CLI, OpenCode, Kilo Code, or other orchestrators as fallbacks
    - Some use **subagents** for documentation, bug-hunting, git commits, research, etc.
  - **Price/value arguments**:
    - Supportive comments say the plan is still a **strong value** for the price:
      - Mentioned examples include **$3/month**, **$28 Christmas special**, **$180/year**, and **$260/year**.
    - Skeptics say it’s only good if you’re not expecting it to replace Claude at full speed.
  - **MCP servers and research use**:
    - One commenter says the **Pro plan for MCP servers** is useful and model/harness-agnostic.
    - They mainly use it for **research**, not browser automation, and consider it a supplement rather than a Claude replacement.
  - **Speed and queueing issues**:
    - Several users report:
      - **10–30 second first-response delays**
      - Sometimes **minutes** waiting for responses
      - The system feeling **slow or unusable** at times
    - Some attribute this to **new model rollout load** (GLM 4.7 Flash), while others think it’s just inherent throttling.
  - **Future model optimism**:
    - A few commenters mention **GLM 5** being in training or new releases coming soon.
    - The idea is that future versions may make the current throttling less of an issue, though one reply notes the opposite happened in practice: models got slower, while plan limits tightened.

- **Broader consensus/disagreement**:
  - **Consensus**: GLM can be useful, but it’s not a clean Claude replacement for everyone.
  - **Disagreement**:
    - Some think the subscription is **excellent value** and the problem is user workflow.
    - Others think the plan is **overpromised and underdelivered**, especially compared to the direct API.

### Assessment
**Durability:** medium. The core lesson about annual plans, throttling, and using multiple models is broadly useful, but the specifics are tied to **GLM 4.7/5**, current pricing, and Reddit-era plan behavior that may change quickly. **Content type:** mixed — it’s a social thread with opinion, troubleshooting, and practical usage advice. **Density:** medium-high, because the thread contains concrete plan prices, model names, concurrency counts, and workflow suggestions, though it’s also noisy and argumentative. **Originality:** commentary / community synthesis rather than a primary source; the value is in the range of user experiences, not authoritative documentation. **Reference style:** skim-once to refer-back, mainly if you’re comparing Claude, GLM, or other coding-agent plans and want real-user complaints about speed vs quota. **Scrape quality:** partial but decent; it captures the post and many nested comments, but it’s still a Reddit thread capture, so context, full branching, and any attached image content are incomplete or missing.
