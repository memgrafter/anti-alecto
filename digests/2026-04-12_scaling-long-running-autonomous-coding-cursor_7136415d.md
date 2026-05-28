---
url: https://cursor.com/blog/scaling-agents
title: Scaling long-running autonomous coding · Cursor
scraped_at: '2026-04-12T09:45:05Z'
word_count: 1066
raw_file: raw/2026-04-12_scaling-long-running-autonomous-coding-cursor_7136415d.txt
tldr: Cursor describes how it scaled autonomous coding by shifting from flat, lock-based agent coordination to a planner-worker system, enabling hundreds of agents to work for weeks on huge codebases like a browser-from-scratch project.
key_quote: The right amount of structure is somewhere in the middle.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries:
- Rust
companies:
- Cursor
- GitHub
tags:
- multi-agent-systems
- autonomous-coding
- software-engineering
- agent-coordination
- cursor
---

### TL;DR
Cursor describes how it scaled autonomous coding by shifting from flat, lock-based agent coordination to a planner-worker system, enabling hundreds of agents to work for weeks on huge codebases like a browser-from-scratch project.

### Key Quote
“The right amount of structure is somewhere in the middle.”

### Summary
- Cursor says it has been running coding agents autonomously for weeks to test how far agentic coding can go on projects that normally take human teams months.
- The post focuses on one central problem: **scaling multiple agents on a single codebase without them duplicating work, drifting, or getting stuck coordinating**.
- **Initial approach: flat self-coordination**
  - All agents had equal status.
  - They used a shared coordination file to see what others were doing, claim tasks, and update status.
  - A locking mechanism was added to prevent two agents from taking the same task.
  - This failed because:
    - locks were held too long or never released,
    - throughput collapsed as agents waited,
    - the system was brittle when agents crashed or misused locks.
- **Second approach: optimistic concurrency control**
  - Agents could read freely, but writes failed if state changed since the last read.
  - This was simpler and more robust than locks.
  - But without hierarchy, agents became **risk-averse**:
    - they avoided hard tasks,
    - made small safe changes,
    - no one took ownership of end-to-end work,
    - work churned without real progress.
- **Third approach: planners and workers**
  - Cursor split agents into distinct roles:
    - **Planners** explore the codebase, create tasks, and can spawn sub-planners recursively.
    - **Workers** only execute assigned tasks and do not worry about the broader picture.
  - At the end of each cycle, a **judge agent** decides whether to continue, then the next iteration starts fresh.
  - This architecture solved most coordination problems and scaled better to large projects.
- **What they tested**
  - **Building a web browser from scratch**
    - Ran close to a week.
    - Produced over **1 million lines of code** across **1,000 files**.
    - Cursor says new agents can still understand and continue the codebase.
    - Hundreds of workers could push to the same branch with minimal conflicts.
  - **Migrating Solid to React in the Cursor codebase**
    - Took over **three weeks**.
    - Resulted in **+266K / -193K edits**.
    - Was passing CI and early checks, though still needed review.
  - **Improving an upcoming product**
    - A long-running agent made video rendering **25x faster** using an efficient Rust implementation.
    - It also added smoother zoom/pan with spring transitions and motion blur.
    - This code was merged and expected to ship soon.
  - Other ongoing examples:
    - **Java LSP**: 7.4K commits, 550K LoC
    - **Windows 7 emulator**: 14.6K commits, 1.2M LoC
    - **Excel**: 12K commits, 1.6M LoC
- **Main lessons learned**
  - Cursor says it has deployed **trillions of tokens** toward this single goal.
  - The system is not perfectly efficient, but more effective than expected.
  - **Model choice matters** for long-running autonomous work:
    - **GPT-5.2** performs better at extended tasks, instruction-following, focus, avoiding drift, and precise completion.
    - **Opus 4.5** tends to stop earlier and take shortcuts.
    - Different models are better for different roles; Cursor now picks the best model per role instead of using one universal model.
  - **Simpler systems often work better**:
    - Cursor removed an integrator role because it created bottlenecks.
    - Workers could already resolve conflicts themselves.
  - **Too little structure** causes duplication, conflict, and drift.
  - **Too much structure** causes fragility.
  - A large part of success came from **prompting and harness design**, not just model selection.
- **What’s next**
  - Multi-agent coordination is still unsolved in an optimal sense.
  - Cursor wants agents to better wake up when tasks finish, avoid running too long, and periodically restart to reduce drift and tunnel vision.
  - Still, the post argues the core question has a more optimistic answer than expected: **hundreds of agents can collaborate on one codebase for weeks and make real progress**.
  - Cursor says these techniques will inform future Cursor agent capabilities and invites hiring interest.

### Assessment
This is a **mixed** announcement/technical reflection with some experimental results and product-direction signaling. Durability is **medium**: the coordination lessons and tradeoffs between locks, optimistic concurrency, and planner-worker structure are broadly useful, but specific model comparisons, numbers, and product experiments may age quickly as Cursor’s stack and model lineup change. The content is **high-density** and mostly **primary source** reporting from Cursor’s own experiments, so it’s useful for understanding their current approach but should be treated as company-authored evidence rather than independent validation. Best used as a **refer-back** reference if you’re tracking multi-agent coding systems, Cursor’s agent roadmap, or practical orchestration patterns; the scrape quality is **good**, with the main narrative and metrics captured, though there are no missing code blocks or images to evaluate here.
