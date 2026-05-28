---
url: https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607
title: Welcome to Gas City
scraped_at: '2026-04-25T06:01:38Z'
word_count: 4613
raw_file: raw/2026-04-25_welcome-to-gas-city_9948f547.txt
tldr: Steve Yegge announces Gas City v1.0.0 as a rebuilt, enterprise-oriented SDK for deploying multi-agent “dark factories” with strong observability, auditability, and git-versioned memory, positioning it as the next step after Gas Town and a practical path for de-SaaSing business processes.
key_quote: “Gas City is the supervisor plane that connects, manages, and coordinates these deployed mini-factories.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: deep-study
scrape_quality: good
people:
- Steve Yegge
- Julian Knutsen
- Chris Sells
- Gene Kim
- Brendan Hopper
- Marc Benioff
tools:
- Medium
- Discord
- tmux
- MCP
- Git
libraries:
- Beads
- Dolt
companies:
- Salesforce
- Atlassian
- ChatWoot
- ZenDesk
tags:
- agent-orchestration
- multi-agent-systems
- enterprise-ai
- workflow-automation
- saas-replacement
---

### TL;DR
Steve Yegge announces **Gas City v1.0.0** as a rebuilt, enterprise-oriented SDK for deploying multi-agent “dark factories” with strong observability, auditability, and git-versioned memory, positioning it as the next step after Gas Town and a practical path for de-SaaSing business processes.

### Key Quote
> “Gas City is the supervisor plane that connects, manages, and coordinates these deployed mini-factories.”

### Summary
- **What Gas City is**
  - A ground-up rewrite of Gas Town into an SDK for building custom agent topologies.
  - Designed to deploy teams of collaborating agents in arbitrary shapes, not just the original Gas Town team structure.
  - Ships as a **drop-in replacement** for Gas Town via a default “Gas Town” pack that runs on startup.

- **Who built it / status**
  - Yegge says he **did not write Gas City**; it was created by **Julian Knutsen** and **Chris Sells**.
  - He describes himself as lightly affiliated, but now “all-in” and contributing.
  - Gas City released **v1.0.0** this week; it went to alpha a few weeks earlier and is now “ready for use today.”

- **Stack and architecture**
  - Gas City decomposes the Gas Town stack into composable, declarative building blocks called **packs**.
  - It acts as a **supervisor plane** for deployed mini-factories.
  - It is backed by the **MEOW stack** (“Molecular Expression of Work”), which treats Work as a first-class primitive.
  - MEOW sits on top of **Beads** and uses **Dolt** as the base, git-versioned database layer.
  - Claimed benefits:
    - identity
    - messaging
    - history
    - context
    - state
    - skills
    - roles
    - personas
    - fine-grained model selection / switching
    - forensic auditability via versioned logs

- **Core thesis: “dark factories” and “light factories”**
  - A **dark factory** is autonomous background work by coding agents without humans watching.
  - Gas City keeps the “lights on”: agents are visible, addressable, and inspectable at any time.
  - Yegge reframes it as a **Light Factory**: observability is a deliberate design choice.
  - Unlike more opaque agent products, Gas City emphasizes interaction, supervision, and control.

- **Reliability and multi-agent design**
  - Yegge argues that **single-agent packs are too risky** for real business processes because any agent can hallucinate or “go temporarily insane.”
  - His recommended pattern is **2–3+ agents** in a crew, so they can check each other’s work and catch mistakes.
  - Reliability is presented as a **dial**: more reviews, backstops, and guardrails increase trustworthiness up to a practical ceiling.
  - He explicitly says he would **not** use this for physically dangerous domains like **medical or navigation systems** “in 2026.”

- **Practical example: Wyvern image moderation**
  - He uses his online game **Wyvern** as an example of a non-code business process suited to agent automation.
  - The workflow: player-uploaded images for level-25 perks are submitted, visually reviewed for appropriateness, and approved/rejected.
  - He describes a **two-agent pack**:
    - one agent wakes on a hook and does the work
    - a second agent checks the first agent’s result
  - He treats this as a small but representative business automation workflow.

- **AI adoption ladder**
  - The post extends his earlier **8-stage AI adoption chart** into **11 stages**.
  - Key milestones:
    - **Level 8**: mastering an orchestrator with dozens of concurrent agents
    - **Level 9**: first deployed pack; you now have an autonomous mini-factory
    - **Level 10**: many packs; the human becomes the bottleneck/control plane
    - **Level 11**: you start building higher-level orchestrators to manage subsets of packs
  - The role of the human evolves into **shepherd / architect / curator**, not direct worker.

- **Factory-builder mindset**
  - Packs become little 24x7 systems that need maintenance, upgrades, patching, and monitoring.
  - The long-term vision is not just using agents, but **building factories that build other factories**.
  - Yegge emphasizes using **formulae** in MEOW as reusable templates for recurring work:
    - incident triage
    - image review
    - log rotation
    - nightly ETL
  - Over time, these formulas create a version-controlled inventory of business processes.

- **“Escape from SaaS Mountain” / de-SaaSing**
  - The second half of the post argues that agentic systems will begin to **replace or internalize SaaS**.
  - Yegge claims SaaS is increasingly an **extractive model**:
    - customers often use only ~20% of features
    - they subsidize the remaining 80%
    - they pay recurring rent for systems they could own
  - He says a company may only need to rebuild the specific features it uses, not the whole SaaS product.
  - He argues many companies can convert large SaaS bills into headcount and in-house capability.

- **Why Gas City matters for SaaS replacement**
  - To replace SaaS in production, Yegge says you need the unglamorous infrastructure:
    - declarative deploys
    - audit trails
    - version history
    - identity
    - durable memory
    - supervision
  - He claims Gas City provides these primitives, making it a practical tool for building **AI-native internal replacements** for SaaS workflows.
  - He explicitly contrasts it with OSS SaaS replacements that still require too much manual operation.

- **Community and ecosystem**
  - Yegge repeatedly points to the surrounding ecosystem:
    - **gastownhall.ai** Discord
    - thousands of active members
    - Beads, Gas Town, Wasteland, Dolt
  - He says the community signal suggests this is “The Way,” and that the ecosystem is now mature enough to bet on.

- **Bottom line**
  - Gas City is presented as a **high-control, enterprise-focused, open-source agent orchestration SDK**.
  - It is meant to help users build reliable multi-agent business systems, gradually replace portions of SaaS, and manage the resulting workflows with strong auditability.
  - Yegge’s recommendation is clear: **switch to Gas City**, but keep Gas Town supported for those who still need it.

### Assessment
This is a **mixed** piece: part product announcement, part vision essay, part advocacy for a broader “agentic business automation” worldview. Durability is **medium**: the architectural ideas around orchestration, audit trails, and workflow decomposition may age well, but the specifics are tied to the current Gas Town/Gas City ecosystem and the state of agent tooling in 2025. Density is **high** because it packs in product claims, conceptual framing, adoption-stage taxonomy, and business strategy, though it is also rhetorically expansive and promotional. Originality is mostly **commentary/primary-source vision** rather than neutral documentation; it reflects Yegge’s perspective and uses examples from his own projects. As a reference, it is best used **deep-study** if you care about agent orchestration strategy or the Gaslandia ecosystem, and **refer-back** if you want the “Gas City vs Gas Town” positioning. Scrape quality is **good** for the article text, but the embedded images and the 8-stage / 11-stage charts are not fully visible here, so some visual nuance is missing.
