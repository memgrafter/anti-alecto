---
url: http://argent:8080/reports/throughput-analysis-2026-03-25/throughput-analysis-2026-03-25.html
title: Throughput Analysis & Forecast — Mar 2026
scraped_at: '2026-04-19T07:41:20Z'
word_count: 2451
raw_file: raw/2026-04-19_throughput-analysis-forecast-mar-2026_e4fece9a.txt
tldr: A March 2026 throughput report argues that the biggest drivers of commits per active hour are short, commit-targeted sessions, low error rates, and single-project focus, while 8+ hour sessions and compaction are major throughput killers.
key_quote: Focus × intent = throughput.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries: []
companies: []
tags:
- productivity
- throughput
- workflow-optimization
- session-management
- focus
---

### TL;DR
A March 2026 throughput report argues that the biggest drivers of commits per active hour are short, commit-targeted sessions, low error rates, and single-project focus, while 8+ hour sessions and compaction are major throughput killers.

### Key Quote
“Focus × intent = throughput.”

### Summary
- **What this is**
  - A data-heavy throughput analysis and forecast for **Mar 2026**, based on weekly, daily, session-level, project-level, and hour-of-day performance.
  - The core metric throughout is **commits per active hour**.

- **Weekly trajectory**
  - Weekly throughput fluctuated substantially:
    - **W1 (Feb 21–28):** 70 sessions, 1,141 turns, 96 commits, **0.39 commits/active hr**
    - **W2 (Feb 28–Mar 7):** 97 sessions, 984 turns, 53 commits, **0.07 commits/active hr**
    - **W3 (Mar 7–14):** 88 sessions, 1,090 turns, 76 commits, **0.09 commits/active hr**
    - **W4 (Mar 14–21):** 74 sessions, 896 turns, 175 commits, **0.30 commits/active hr**
    - **W5 (Mar 18–25):** 50 sessions, 705 turns, 192 commits, **0.74 commits/active hr**
  - The report frames **W2–W3 as a throughput collapse** caused by:
    - 3–5× more active hours spread across 3–5× more projects
    - Long-running, exploratory/R&D sessions without commit targets
    - “Massive parallelism with no delivery pressure”
  - Recovery in **W4→W5** is attributed to:
    - Project count dropping from **26 to 10**
    - Shorter sessions
    - More commit-oriented work

- **Session duration is the main lever**
  - Sub-60-minute sessions are the sweet spot:
    - **<30 min:** 202 sessions, **2.60 commits/hr**
    - **30–60 min:** 39 sessions, **2.24 commits/hr**
    - **1–2 hr:** 40 sessions, **1.79 commits/hr**
    - **2–4 hr:** 23 sessions, **0.69 commits/hr**
    - **4–8 hr:** 20 sessions, **1.25 commits/hr**
    - **8 hr+:** 55 sessions, **0.07 commits/hr**
  - The report highlights a **37× throughput gap** between sub-60-minute sessions and 8+ hour sessions.
  - Exception: the **4–8 hour bucket** sometimes performs well because these are described as marathon autonomous **flatagents** sessions.

- **Session tier analysis**
  - Sessions are grouped into tiers:
    - **Elite:** ≥3 c/hr, ≥3 commits — 29 sessions, **9.17 commits/hr**, 1.64 avg hours, **0.17% error**
    - **High:** ≥1 c/hr, ≥2 commits — 23 sessions, **4.62 commits/hr**
    - **Medium:** ≥1 commit — 64 sessions, **1.20 commits/hr**
    - **Zero-commit:** 133 sessions, **0.00 commits/hr**
  - Elite sessions show:
    - Higher tool density (**13.3 tools/turn**)
    - Shorter duration
    - Very low error rate
    - Slightly higher bash usage and lower read usage than slower tiers
  - Main conclusion: elite sessions **execute more and explore less**.

- **Error rate matters**
  - Throughput drops as error rate rises:
    - **0% errors:** 0.27 commits/hr
    - **<1% errors:** 0.15 commits/hr
    - **1–3% errors:** 0.08 commits/hr
    - **3%+ errors:** 0.09 commits/hr
  - The report says zero-error sessions commit at:
    - **1.8×** the rate of low-error sessions
    - **3×** the rate of high-error sessions
  - High-error sessions produce churn rather than shipped output.

- **Focus beats parallelism**
  - Day-level focus bands:
    - **1–2 projects:** 11 days, **0.94 commits/active hr**
    - **3–5 projects:** 12 days, **0.75 commits/active hr**
    - **6+ projects:** 9 days, **0.40 commits/active hr**
  - Conclusion:
    - 1–2 project days produce **2.4×** the commits/active-hour of 6+ project days.
    - More projects increase sessions but reduce efficiency.
    - 3–5 projects may yield more raw commits, but not better hourly efficiency.

- **Compaction is treated as a failure signal**
  - Comparison:
    - **No compaction:** 107 sessions, **4.14 commits/hr**, 12.1 avg hours, 0.23% error
    - **Compacted:** 9 sessions, **0.66 commits/hr**, 18.8 avg hours, 0.52% error
  - Compacted sessions are described as:
    - ~3× longer
    - ~3× more turns
    - ~2× higher error rate
    - ~6× lower commit rate
  - Recommendation: if a session compacts, **end it and restart fresh**.

- **Time-of-day throughput peaks**
  - Best productivity windows:
    - **12 PM PT:** 6.27 commits/hr
    - **8 PM PT:** 3.67 commits/hr
    - **2 PM PT:** 2.79 commits/hr
    - **5 PM PT:** 2.29 commits/hr
    - **8 AM PT:** 1.58 commits/hr
  - Noon and 8 PM are identified as the strongest throughput windows.
  - Late-night activity can produce high raw output, but at lower per-hour efficiency because sessions run long.

- **Project rankings**
  - Highest commits/hr among named projects:
    - **pi-claude-cache-warming:** 3.77 c/hr
    - **rerere:** 3.64 c/hr
    - **flatmachines_manager:** 3.49 c/hr
    - **prototyping:** 2.63 c/hr
  - Low-efficiency large projects include:
    - **flatagents:** 0.45 c/hr
    - **autocatalytic-infra:** 0.22 c/hr
    - **skills-flatagents:** 0.17 c/hr
    - **speed-kills:** 0.01 c/hr
  - Some projects generate huge volume but low hourly efficiency.

- **Peak days**
  - Strongest days and patterns:
    - **Mar 17:** 9 sessions, 1 project, 38 commits, **6.91 c/hr** — single-project focus day
    - **Mar 22:** 10 sessions, 4 projects, 60 commits, **4.11 c/hr** — high-focus, zero-error
    - **Mar 20:** 26 sessions, 6 projects, 41 commits — high-session sprint day
    - **Mar 18:** 9 sessions, 4 projects, 28 commits — solid all-round
    - **Feb 22:** 12 sessions, 2 projects, 40 commits — focused + reliable

- **Elite session hall of fame**
  - Extremely fast sessions appear mostly in **autocatalytic-infra**, with some in **flatagents**, **skills-flatagents**, and **prototyping**.
  - Top example:
    - **9f50bb15** on autocatalytic-infra: 5 turns, 5 commits, 0.13 hours, **37.8 commits/hr**
  - These are used as proof that very high throughput is possible in short, highly focused bursts.

- **Tool mix**
  - Fast, medium, and slow sessions have surprisingly similar tool compositions.
  - Main differences are not tool mix but:
    - **session duration**
    - **turn count**
  - Conclusion: session shaping matters more than tool optimization.

- **Forecast**
  - **Status quo forecast:** **0.85 commits/active hr by W9**
    - Assumes no behavior changes
    - Predicts modest improvement from familiarity
  - **Optimized forecast:** **1.50 commits/active hr by W9**
    - Assumes session shaping and focus discipline
    - Roughly **2× current throughput**
  - **Maximum forecast:** **2.50 commits/active hr by W9**
    - Assumes sustained elite-mode behavior:
      - sub-2-hour sessions
      - single-project focus
      - zero-error targeting

- **Ranked recommendations**
  1. **Kill 8+ hour sessions** — highest impact, estimated **+60% throughput**
     - Hard-stop at 2 hours
     - Commit or snapshot state, then restart
     - Compaction should trigger immediate termination
  2. **Single-project focus days** — estimated **+25% throughput**
     - Aim for 3–4 single-project days per week
     - Keep at least 2 days/week with ≤2 active projects
  3. **Target <60-minute sessions** — estimated **+20% throughput**
     - Start each session with a clear commit target
     - Avoid “while I’m here” expansion
  4. **Move autonomous work to burst mode**
     - Break long agentic sessions into 90-minute sprints with phase checkpoints
  5. **Protect zero-error mode**
     - Current error rate is reported as **0.06%**
     - Keep reliability high rather than trading it for speed
  6. **Exploit peak hours**
     - Put high-priority commit work at **12 PM** and **8 PM**
     - Use late night for autonomous or batch work

- **Model / equation**
  - The report formalizes throughput as:
    - **Commits/Hr = Base Rate × 1/Duration Factor × 1/Error Factor × Focus Multiplier**
  - Stated factors:
    - Base rate ≈ **2.4 c/hr**
    - Duration factor:
      - 1.0 for <1hr
      - 1.3 for 1–2hr
      - 3.5 for 2–4hr
      - 34× for 8hr+
    - Error factor:
      - 1.0 for 0%
      - 1.8 for <1%
      - 3.4 for 1–3%
    - Focus multiplier:
      - 1.25 for 1–2 projects
      - 1.0 for 3–5
      - 0.53 for 6+
  - Ideal operating point is given as **3.0 commits/hr**.

### Assessment
This is a **mixed** analytical report with a strong **tutorial/advice** component built on operational data. Durability is **medium**: the underlying lessons about short sessions, focus, and error reduction are fairly timeless, but the specific numbers, project names, and forecast are tied to a narrow time window in **Mar 2026** and likely to drift as workflows change. Density is **high** because it contains many tables, ratios, thresholds, and rank-ordered findings. Originality appears to be **primary source** or at least a direct internal synthesis of observed activity data, not a commentary on outside work. It’s best used as **refer-back** material: useful for comparing future throughput patterns, validating workflow changes, or remembering the specific recommendations and benchmark values. Scrape quality looks **good** overall: the major sections, tables, forecast, and recommendations are present, though the raw HTML-to-text conversion may have flattened the diagram/flowchart formatting.
