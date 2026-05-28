---
url: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
title: Announcing the Agent2Agent Protocol (A2A) - Google Developers Blog
scraped_at: '2026-04-19T06:57:12Z'
word_count: 3208
raw_file: raw/2026-04-19_announcing-the-agent2agent-protocol-a2a-google-developers-blog_7685a862.txt
tldr: Google announced Agent2Agent (A2A), an open protocol for letting AI agents from different vendors and frameworks discover each other, exchange messages securely, and coordinate tasks across enterprise systems.
key_quote: “Enabling agents to interoperate with each other, even if they were built by different vendors or in a different framework, will increase autonomy and multiply productivity gains, while lowering long-term costs.”
durability: medium
content_type: announcement
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Alon Talmor
- Brendan Haire
- Arun Subramaniyan
- Jason Lopatecki
- Djon Kleine
- Ketan Kittur
- Nikhil Krishnan
- Rob Skillington
- Babak Hodjat
- Autumn Moulder
- Pascal Vantrepote
- Sachin Rajpal
- Ed Anuff
- Yrieix Garnier
- Steve Kearns
- Anthony Rotio
- Gurashish Brar
- Osama Elkady
- Tapasvi Moturu
- Vladislav Tankov
- Yoav Landman
- Harrison Chase
- Andrew Davidson
- Sudhir Hasbe
- Thomas Lloyd
- Rahul Jain
- Prakhar Mehrotra
- Dallas Dolen
- Walter Sun
- Gary Lerhaupt
- Pat Casey
- Cosmin Ene
- Graham Sheldon
- Eli Tsinovoi
- Shawn Lewis
- Scott Alfieri
- Herschel Parikh
- Gopal Srinivasan
- Marc Cerro
- Vijay Guntur
- Sherif AbdElGawad
- Asif Hasan
- Anupam Singhal
- Nagendra P Bandaru
tools:
- Agentspace
libraries:
- LangChain
companies:
- Google
- Anthropic
- Atlassian
- Box
- Cohere
- Intuit
- LangChain
- MongoDB
- PayPal
- Salesforce
- SAP
- ServiceNow
- UKG
- Workday
- Accenture
- BCG
- Capgemini
- Cognizant
- Deloitte
- HCLTech
- Infosys
- KPMG
- McKinsey
- PwC
- TCS
- Wipro
- Ask-AI
- Articul8
- Arize AI
- BCG
- C3 AI
- Cohere
- Confluent
- Cotality
- DataStax
- Datadog
- Elastic
- GrowthLoop
- Harness
- Incorta
- JetBrains
- JFrog
- Neo4j
- New Relic
- Pendo
- Supertab
- UiPath
- Weights & Biases
- Quantiphi
tags:
- ai-agents
- interoperability
- enterprise-ai
- open-protocol
- multi-agent-systems
---

### TL;DR
Google announced Agent2Agent (A2A), an open protocol for letting AI agents from different vendors and frameworks discover each other, exchange messages securely, and coordinate tasks across enterprise systems.

### Key Quote
“Enabling agents to interoperate with each other, even if they were built by different vendors or in a different framework, will increase autonomy and multiply productivity gains, while lowering long-term costs.”

### Summary
- **What was announced**
  - On **April 9, 2025**, Google launched **Agent2Agent (A2A)**, an **open protocol** for **agent interoperability**.
  - It is aimed at enabling AI agents to **communicate, securely exchange information, and coordinate actions** across enterprise platforms and applications.
  - Google positions A2A as **complementary to Anthropic’s Model Context Protocol (MCP)**: MCP supplies tools/context, while A2A handles **agent-to-agent collaboration**.

- **Why Google says it matters**
  - Enterprises are building autonomous agents for tasks like:
    - ordering laptops
    - helping customer service reps
    - supply chain planning
  - Google argues the next step is a **dynamic multi-agent ecosystem** where agents can collaborate across silos, even if built by different vendors or frameworks.
  - The pitch is that standardization will increase autonomy, improve productivity, and reduce long-term integration costs.

- **Design principles**
  - Google says A2A was designed around five principles:
    - **Embrace agentic capabilities**: support collaboration in natural, unstructured modalities, not just via “tools”
    - **Build on existing standards**: HTTP, SSE, JSON-RPC
    - **Secure by default**: enterprise-grade authn/authz, with parity to OpenAPI auth schemes at launch
    - **Support long-running tasks**: from quick actions to multi-hour or multi-day workflows, with feedback and state updates
    - **Modality agnostic**: supports text plus audio/video streaming

- **How A2A works**
  - A2A defines a **client agent** and a **remote agent**:
    - the **client** formulates tasks and communicates them
    - the **remote** agent performs the work or returns information
  - Key protocol capabilities:
    - **Capability discovery** via an **Agent Card** in JSON
    - **Task management** with a lifecycle and outputs called **artifacts**
    - **Collaboration** through messages carrying context, replies, artifacts, or user instructions
    - **User experience negotiation** via message “parts” that describe content types and UI capabilities such as iframes, video, and web forms

- **Example use case**
  - Google gives a **candidate sourcing** example in a hiring workflow:
    - a hiring manager uses a unified interface like **Agentspace**
    - their agent finds candidates based on job listing, location, and skills
    - specialized agents help source candidates
    - another agent can schedule interviews
    - another can handle background checks
  - The example is meant to show how A2A can coordinate work across systems in a real enterprise workflow.

- **Launch and roadmap**
  - Google says A2A is being released as **open source** with clear paths for contribution.
  - A **production-ready version** is planned **later in 2025**.
  - Readers are directed to the **specification draft**, **code samples**, and **example scenarios** on the A2A website.

- **Partner ecosystem**
  - The post emphasizes support from **50+ technology partners** and major service providers.
  - Named technology partners include **Atlassian, Box, Cohere, Intuit, LangChain, MongoDB, PayPal, Salesforce, SAP, ServiceNow, UKG, Workday**, among others.
  - Named service providers include **Accenture, BCG, Capgemini, Cognizant, Deloitte, HCLTech, Infosys, KPMG, McKinsey, PwC, TCS, Wipro**.
  - The remainder of the post is mostly **partner endorsement quotes** about interoperability, enterprise automation, and standards.

### Assessment
This is a **mixed announcement/reference** piece with a strong product-launch angle. **Durability is medium**: the core interoperability concepts and protocol design are broadly relevant, but the specifics—launch timing, partner list, and production-readiness roadmap—are tied to **April 2025** and will age. **Density is medium-high** because it includes concrete protocol concepts (Agent Card, task lifecycle, artifacts, HTTP/SSE/JSON-RPC, auth parity with OpenAPI) but also a large amount of repetitive promotional partner commentary. **Originality is primary source**, since it is Google’s official announcement, though much of the latter half is endorsement aggregation rather than substantive technical detail. Best used as a **refer-back** reference if you want the protocol’s stated goals, architecture, and launch context; it is less useful for deep study than the actual draft specification. **Scrape quality is partial**: the text seems mostly complete, but a few elements appear malformed or duplicated (for example, image placeholders like “right click to view in new tab” and some repeated/garbled partner quotes), and the actual diagrams/code samples are missing.
