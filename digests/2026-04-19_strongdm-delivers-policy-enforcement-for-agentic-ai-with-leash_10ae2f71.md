---
url: https://www.strongdm.com/blog/policy-enforcement-for-agentic-ai-with-leash
title: StrongDM Delivers Policy Enforcement for Agentic AI with Leash
scraped_at: '2026-04-19T07:12:19Z'
word_count: 1209
raw_file: raw/2026-04-19_strongdm-delivers-policy-enforcement-for-agentic-ai-with-leash_10ae2f71.txt
tldr: StrongDM announces Leash, an open-source kernel-level control project for enforcing Cedar policies on AI agents and MCP traffic so enterprises can monitor, block, and audit autonomous actions in real time.
key_quote: “Leash turns the host into an enforcement node that speaks the same policy language as StrongDM’s authorization layer, unifying human and machine access control under a single model.”
durability: medium
content_type: announcement
density: medium
originality: primary
reference_style: skim-once
scrape_quality: good
people:
- Justin McCarthy
tools:
- Leash
- MCP
libraries:
- Cedar
companies:
- StrongDM
tags:
- agentic-ai
- access-control
- policy-enforcement
- cybersecurity
- model-context-protocol
---

### TL;DR
StrongDM announces Leash, an open-source kernel-level control project for enforcing Cedar policies on AI agents and MCP traffic so enterprises can monitor, block, and audit autonomous actions in real time.

### Key Quote
“Leash turns the host into an enforcement node that speaks the same policy language as StrongDM’s authorization layer, unifying human and machine access control under a single model.”

### Summary
- This is a StrongDM product/announcement post dated **October 29, 2025** by **Justin McCarthy (Co-founder / CTO)** introducing **Leash**, an **open-source** project for **agentic AI security**.
- Core thesis: enterprises increasingly need to govern **non-human identities**—AI agents and autonomous workloads—not just humans, because agents can act unpredictably across systems and networks.
- Leash is positioned as a way to extend StrongDM-style access control to agents by providing:
  - **agent identity** handling
  - **runtime security**
  - **fine-grained control** over non-human access
  - **hot-reloadable policies** for rapid iteration
- It works by operating **inside the kernel network stack** and intercepting agent activity before connections are established.
- Leash uses **Cedar-defined policies** (the same policy language as StrongDM’s Policy Engine) to evaluate actions against context such as:
  - source process
  - identity
  - environment tags
  - destination attributes
- Claimed enforcement capabilities:
  - inspect outbound traffic and identify target service/domain
  - enforce policy before connection establishment
  - apply context-aware rules in Cedar
  - record every action for auditability
- The post frames Leash as a way to eliminate blind spots, prevent “runaway” agents, and replace credential-centric thinking with **behavior-based governance**.
- In the **MCP (Model Context Protocol)** section, StrongDM says Leash:
  - directly parses and handles MCP
  - controls which MCP providers/tools are permitted
  - intercepts MCP calls at the OS level to reduce bypass/misconfiguration risk
  - can block malicious or runaway agents before data exfiltration
  - provides system-level logs for allowed/blocked connections
- The article includes an architecture comparison table showing how Leash fits alongside StrongDM components:
  - **Policy Definition** → context-aware, Cedar-based access logic
  - **Authorization & routing** → dynamic resource authorization
  - **Credential Security** → secretless session management
  - **Endpoint Verification** → device trust & posture enforcement
  - **Kernel-level filtering** → agentic AI & service traffic control
- StrongDM presents a layered model:
  - **Human access** → Gateway enforcement
  - **Service access** → Relay enforcement
  - **Agentic AI access** → Leash enforcement
- It claims:
  - same policy substrate (**Cedar**)
  - same audit pipeline
  - same real-time authorization semantics
  - low latency and HA deployment characteristics
  - **negligible overhead (<1ms per decision)**
  - compatibility with SIEM/observability export
- The closing argument: access control is evolving from “who can access what?” to **“what are autonomous systems doing, and should they be allowed to do it?”** StrongDM calls this **Agentic Control**.

### Assessment
This is a **mixed announcement/marketing-technical post** with strong product positioning and some architectural detail. **Durability: medium**—the high-level idea of governing AI agents is likely to remain relevant, but the specifics are tied to **StrongDM’s 2025 product messaging, Leash, Cedar, and MCP**. **Content type: announcement / mixed**. **Density: medium**; it contains concrete claims, architecture terms, and a comparison table, but much of the prose is promotional. **Originality: primary source** since it’s StrongDM’s own announcement. **Reference style: skim-once to refer-back**—useful for understanding StrongDM’s framing and product claims, but not a deep technical spec. **Scrape quality: good**; the main article text and table appear captured, though any linked visuals, diagrams, or deeper implementation details are not present.
