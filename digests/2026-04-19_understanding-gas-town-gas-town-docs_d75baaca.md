---
url: https://docs.gastownhall.ai/
title: Understanding Gas Town | Gas Town Docs
scraped_at: '2026-04-19T08:19:54Z'
word_count: 918
raw_file: raw/2026-04-19_understanding-gas-town-gas-town-docs_d75baaca.txt
tldr: Gas Town is an orchestration system for AI-agent engineering work that emphasizes attribution, provenance, and role-based workflows across persistent infrastructure agents, human-managed crews, and transient supervised workers.
key_quote: If you find something on your hook, YOU RUN IT.
durability: medium
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Joe
- Claude
- GPT
tools:
- gt convoy list --all
- gt sling
companies:
- Gas Town
tags:
- ai-agents
- orchestration
- workflow-management
- attribution
- provenance
---

### TL;DR
Gas Town is an orchestration system for AI-agent engineering work that emphasizes attribution, provenance, and role-based workflows across persistent infrastructure agents, human-managed crews, and transient supervised workers.

### Key Quote
"If you find something on your hook, YOU RUN IT."

### Summary
- **What Gas Town is**
  - Gas Town is described as an **orchestration layer** that treats AI agent work as **structured data**.
  - Core goals: **accountability**, **quality tracking**, **efficiency in routing work**, and **scaling coordination** across repos and teams.
  - The system emphasizes that **every action is attributed**, **every agent has a track record**, and **every piece of work has provenance**.

- **Role taxonomy**
  - Gas Town separates agents into **infrastructure roles** and **worker roles**.
  - **Infrastructure roles**:
    - **Mayor**: global coordinator at `mayor/`; singleton, persistent.
    - **Deacon**: background supervisor daemon / watchdog chain; singleton, persistent.
    - **Witness**: per-rig polecat lifecycle manager; one per rig, persistent.
    - **Refinery**: per-rig merge queue processor; one per rig, persistent.
  - **Worker roles**:
    - **Polecat**: ephemeral worker with its own worktree; transient and managed by Witness.
    - **Crew**: persistent worker with its own clone; long-lived and user-managed.
    - **Dog**: Deacon helper for infrastructure tasks; ephemeral and managed by Deacon.

- **Convoys for tracking work**
  - A **convoy** (`🚚`) tracks batched work, even for a single issue.
  - Convoys give:
    - one view of **what’s in flight**
    - **cross-rig tracking**
    - **auto-notification** when work lands
    - a **historical record** of completed work via `gt convoy list --all`
  - The **swarm** is the set of workers currently assigned to the convoy’s issues.
  - When issues close, the convoy “lands.”

- **Crew vs. Polecats**
  - Both are project workers, but they differ in lifecycle and control:
    - **Crew**: persistent, user-controlled, can be assigned by humans or self-assigned, pushes to main directly, cleanup is manual.
    - **Polecat**: transient, Witness-controlled, slung via `gt sling`, works on a branch, Refinery merges, cleanup is automatic.
  - Recommended uses:
    - **Crew** for exploratory work, long-running projects, human judgment, and direct control.
    - **Polecats** for discrete tasks, batch work, parallel work, and supervised execution.

- **Dogs vs. Crew**
  - Dogs are explicitly **not workers**; they are narrow **infrastructure utilities** owned by Deacon.
  - Example dog: **Boot**, which triages Deacon health on daemon tick.
  - If you need to work in another rig, use **worktrees**, not dogs.

- **Cross-rig work patterns**
  - Two main options:
    - **Worktrees** (preferred): use when you need to make a quick fix, want work to appear in your CV, or are working directly in another rig’s codebase.
    - **Dispatch to local workers**: use when the target rig should own the work.
  - A small table maps scenarios to the right approach:
    - quick fix → worktree
    - should appear in your CV → worktree
    - should be done by target rig team → dispatch
    - infrastructure/system task → Deacon

- **Identity and attribution**
  - Work is attributed to the actor who performed it, even across rigs.
  - Example shown: `gastown/crew/joe` working in `~/gt/beads/crew/gastown-joe/`
  - Commits still belong to `gastown/crew/joe`, and the work appears on **joe’s CV**, not the target rig’s workers.
  - Gas Town uses the **current working directory (cwd)** for identity detection, so staying in the right directory matters.

- **The Propulsion Principle**
  - The central behavioral rule is:
    - **"If you find something on your hook, YOU RUN IT."**
  - The hook is treated as the assignment; agents should execute immediately without waiting for confirmation.
  - The metaphor is mechanical/steam-engine-like: agents are “pistons.”

- **Model evaluation and A/B testing**
  - Because work is attributed and historical, Gas Town can support **objective model comparison**.
  - Capturing completion time, quality signals, and revision count enables:
    - model selection for codebases
    - capability mapping across models
    - cost optimization for when smaller models are sufficient

- **Common mistakes highlighted**
  - Using **dogs** for user work instead of crew/polecats.
  - Confusing **crew** with **polecats**.
  - Working in the **wrong directory**, which affects identity detection.
  - Waiting for confirmation when the work is already hooked.
  - Using worktrees when **dispatch** would better assign ownership to the target rig.

### Assessment
This is a **reference/documentation** page with a conceptual overview of Gas Town’s architecture and workflow rules. Its **durability is medium**: the underlying ideas about attribution, role separation, and orchestration are fairly stable, but the naming conventions, commands like `gt convoy list --all`, and role details may evolve with the product. The content is **dense** and highly structured, with specific role definitions, lifecycle distinctions, and workflow rules. It appears to be **primary-source documentation**, not commentary or synthesis. This is best used as a **refer-back** reference rather than a one-time skim, especially if you need to remember the distinctions between crew, polecats, dogs, convoys, and cross-rig work patterns. Scrape quality is **partial**: the text captures most of the conceptual content and tables, but some sections appear truncated or incomplete, including the “Directory Structure” area and possibly linked references like “Why These Features” and “Convoys.”
