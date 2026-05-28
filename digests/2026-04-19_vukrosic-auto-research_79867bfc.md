---
url: https://github.com/vukrosic/auto-research
title: vukrosic/auto-research
scraped_at: '2026-04-19T07:52:02Z'
word_count: 553
raw_file: raw/2026-04-19_vukrosic-auto-research_79867bfc.txt
tldr: auto-research is a docs-only control plane for running an open, file-based autonomous AI research lab inside another repo, with humans setting direction and agents executing reproducible research loops.
key_quote: Human mission. Agent execution. Reproducible state.
durability: high
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries: []
companies: []
tags:
- autonomous-ai
- research-workflow
- documentation
- file-based-state
- agent-orchestration
---

### TL;DR
`auto-research` is a docs-only control plane for running an open, file-based autonomous AI research lab inside another repo, with humans setting direction and agents executing reproducible research loops.

### Key Quote
“Human mission. Agent execution. Reproducible state.”

### Summary
- **Project identity**
  - Repository: `vukrosic/auto-research`
  - Public system name: **Open Research Loop**
  - Repo/worktree name: **autoresearch**

- **Core mission**
  - The repo aims to make autonomous AI research more **open, inspectable, and reusable**.
  - It emphasizes a division of labor:
    - **Humans** define direction, constraints, and taste.
    - **Agents** handle lower-level research execution.
  - State should be stored in **files**, not hidden memory, so work can be resumed, audited, and shared.

- **What it is**
  - A **docs-only operating system** for running an autonomous research lab inside another codebase.
  - Functions as:
    - a portable lab handbook
    - a file-based operating model
    - a prompt/template kit
    - a concrete product spec for the first useful workflow

- **What it is not**
  - Not a live experiment archive
  - Not a benchmark suite
  - Not a hosted platform
  - Not a polished end-user product

- **Main design choice**
  - The lab is intentionally **file-based**.
  - Plans, experiment records, project configs, knowledge, and handoff state should live in the target repo so:
    - new agents can recover context
    - humans can inspect what happened
    - contributors can reproduce decisions
    - workflow does not depend on hidden orchestration

- **How to start**
  - **Human operator** should read:
    - `README.md`
    - `PRODUCT_SPEC.md`
    - `INTAKE_PROMPT.md`
    - `PLANNING_PROMPT.md`
    - `SETUP.md`
  - **AI agent** should start with:
    - `AGENTS.md`
    - then read `LAB.md`, `OPERATING_MODEL.md`, `PRODUCT_SPEC.md`, `INTAKE_PROMPT.md`, `PLANNING_PROMPT.md`, `FOLDER_BLUEPRINT.md`, and `TEMPLATES.md`

- **Repository map**
  - `README.md` — entrypoint and framing
  - `PRODUCT_SPEC.md` — first shippable workflow and maturity gates
  - `INTAKE_PROMPT.md` — first-conversation scoping behavior
  - `PLANNING_PROMPT.md` — brief-to-plan-to-action behavior
  - `LAB.md` — authority, rules, and policy
  - `OPERATING_MODEL.md` — execution mechanics and research loop
  - `AGENTS.md` — agent onboarding and startup behavior
  - `SETUP.md` — human install flow
  - `FOLDER_BLUEPRINT.md` — durable target-repo folder structure
  - `TEMPLATES.md` — starter files for goals, plans, configs, experiments, and reports
  - `PROMPTS_AUTONOMOUS.md` — autonomous operation entrypoints
  - `PROMPTS_SUPERVISED.md` — approval-gated operation entrypoints
  - `OPERATOR_TIPS.md` — practical human usage tips

- **How to use it**
  - Copy the markdown docs into the repo you actually want to research on.
  - Start an AI coding agent in that repo.
  - Have it read the docs in the prescribed order.
  - Choose autonomous or supervised mode.
  - Let it create the working folders and durable starter files in the target repo.
  - The repo itself does **not** include runtime folders like:
    - `experiments/`
    - `goals/`
    - `knowledge/`
    - `projects/`
    - `state/`
    - `logs/`
    - `reports/`
  - Those are created in the target repo when the lab is instantiated.

- **Long-term direction**
  - Build open autonomous research infrastructure where:
    1. one human directs many agent-run loops
    2. one control plane works across many repos
    3. contributors can inspect and extend the process
    4. public knowledge compounds instead of staying private
  - The immediate goal is narrower: make the workflow from **user question → autonomous research run** actually work.

### Assessment
This is a **high-durability** reference/repo-framing document: the concepts are fairly timeless, though some specific file names and repo structure could evolve as the project changes. The content type is **mixed**, but primarily **reference/documentation** with some product-spec framing. Density is **medium**: it’s concise but packed with concrete repo structure, workflow steps, and intended audience split. Originality is best described as **primary source** since it states the project’s own goals, architecture, and usage model. It’s best used as a **refer-back** doc rather than a deep study text, because it provides orientation and navigation more than detailed implementation. Scrape quality is **good** for the README-like content shown here; no obvious code blocks or sections appear missing from the provided text.
