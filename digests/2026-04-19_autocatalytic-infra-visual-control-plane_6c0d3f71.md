---
url: http://argent:8080/reports/control-plane/control-plane.html
title: Autocatalytic Infra — Visual Control Plane
scraped_at: '2026-04-19T07:42:47Z'
word_count: 722
raw_file: raw/2026-04-19_autocatalytic-infra-visual-control-plane_6c0d3f71.txt
tldr: This is a monitoring dashboard for an “Autocatalytic Infra” control plane showing that planning and review are functioning, but execution is bottlenecked by stalled workflows, aging reviews, and the absence of a real priority/queueing system.
key_quote: Priority is currently an emergent human behavior, not a system property.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools: []
libraries: []
companies: []
tags:
- infrastructure
- monitoring
- workflow-automation
- queueing
- operations
---

### TL;DR
This is a monitoring dashboard for an “Autocatalytic Infra” control plane showing that planning and review are functioning, but execution is bottlenecked by stalled workflows, aging reviews, and the absence of a real priority/queueing system.

### Key Quote
“Priority is currently an emergent human behavior, not a system property.”

### Summary
- **What this is**
  - A visual control-plane report for an infrastructure workflow system called **Autocatalytic Infra**.
  - It summarizes health across plans, executions, changesets, reviews, and docs, with emphasis on where the pipeline is breaking down.

- **System health snapshot**
  - **35 total plans**
  - **11 active plans**, with a note that many are stalled
  - **6 stalled executions** needing triage
  - **344 changesets** with a **96% commit rate**
  - **2 pending reviews** that are **14+ days old**
  - **164 doc registry entries** across **18 kinds**

- **Stalled executions**
  - The dashboard flags **6 executions** as “Non-Terminated, Not Advancing.”
  - These are described as **plan_lifecycle** and **checker-gpt** instances that:
    - have **not terminated**
    - have **no waiting_channel**
    - require **manual investigation or cleanup**

- **Pipeline / lifecycle model**
  - The report includes a **plan lifecycle state machine** showing phases like:
    - `start`
    - `prepare_checker_input`
    - `run_checker_parallel`
    - `invoke_checkers`
    - `publish_checker_review`
    - `wait_checker_decision`
    - `prepare_atomizer_input`
    - `invoke_atomizer`
    - `publish_candidate_review`
    - `wait_candidate_decision`
    - `planned`
    - `rejected`
  - It also shows revision-limit branches for both checker and candidate loops.

- **Execution funnel / where work gets stuck**
  - The key bottleneck is not plan creation but execution:
    - **11 active plans**
    - only **2 have task runs** (plans **134** and **154**)
    - plans **117, 130, and 141** have **approved candidates** and **pending tasks** but **zero task runs**
  - Conclusion: **the pipeline creates plans faster than the swarm can execute them**.

- **Changeset velocity**
  - The changeset system is relatively healthy:
    - **330 committed out of 344**
    - about **96% commit rate**
    - only about **4% abandoned**
  - This is called out as a **working well** area.

- **Review turnaround analysis**
  - Review response times are **bimodal**:
    - either **under 3 minutes** when the operator is actively monitoring
    - or **over 4 hours** when they are away
  - There is **no queueing or batch review mechanism**, so reviews block the whole pipeline until a human responds.
  - Suggested fixes:
    - **async continuation**
    - **priority-based review queuing**

- **Open review requests**
  - Two reviews are explicitly listed as aging:
    - **Action ID 60** — `prompt_pack` for `plan-20260311T1105-prompt-pack-qa-gate`, created **2026-03-12 05:13**, **14 days old**
    - **Action ID 61** — `checker` for `design-20260311T2345-execution-dag-canonical-block`, created **2026-03-12 07:02**, **14 days old**

- **Priority gap analysis**
  - The report argues the system lacks real prioritization:
    - `user_actions.priority` exists, but values are only **1 or 2**, so it behaves like a binary flag rather than a queue
    - early Git history references priority in **3 commits** from **Feb 21–22** about gap analysis, lifecycle criteria, and model selection
    - plan states like **active / inactive / superseded** are only coarse triage
  - What’s missing:
    - **plan-level priority** in the docs table
    - **task-level priority** for swarm execution
    - **execution priority** for resuming waiting work
    - **automated staleness alerts / cleanup**
  - Core claim: **operator attention currently acts as the scheduler**, which works only at low scale.

- **Key insights: working well**
  - **Changeset system**: 96% commit rate is healthy
  - **Dual-checker pattern**: parallel GPT + ZAI review catches more issues
  - **Signal-driven resume**: checkpoint persistence supports long-lived workflows
  - **Task decomposition**: example plan **104** produced **29 tasks**, with **5 executed**, proving end-to-end flow
  - **Swarm execution**: plan **134** completed **5 tasks across 5 workers in 4 minutes**

- **Key insights: needs attention**
  - **Execution gap**: most active plans have no task runs
  - **Stalled executions**: 6 stuck instances from **Mar 11–18**
  - **Review bottleneck**: human response latency blocks the pipeline
  - **Draft rot**: **7 draft plans** are aging **18–30 days** without a path forward
  - **No priority system**: the system doesn’t scale because human attention is the only scheduler

### Assessment
This is a **mixed technical dashboard/report** with high practical value for operators of the system. **Durability is medium**: the architectural observations about bottlenecks, queueing, and priority are broadly useful, but the specific counts, dates, and execution IDs are time-sensitive. **Density is high** because it condenses status metrics, lifecycle behavior, and root-cause analysis into a small space. The content appears to be a **primary-source operational report** rather than commentary or synthesis. It’s best used as a **refer-back** reference when diagnosing workflow bottlenecks or comparing later dashboard snapshots. **Scrape quality is partial**: the main text and metrics are present, but the visual charts themselves, table contents beyond headers, and any underlying images/interactive elements are not fully captured.
