---
url: https://github.com/a2aproject/A2A
title: 'a2aproject/A2A: Agent2Agent (A2A) is an open protocol enabling communication and interoperability between opaque agentic applications.'
scraped_at: '2026-04-19T06:57:25Z'
word_count: 745
raw_file: raw/2026-04-19_a2aproject-a2a-agent2agent-a2a-is-an-open-protocol-enabling-communication-and-in_a9426c06.txt
tldr: A2A (Agent2Agent) is an open protocol from Google/Linux Foundation for letting independent AI agents discover, negotiate, and collaborate over HTTP using JSON-RPC 2.0 without exposing their internal state or tools.
key_quote: An open protocol enabling communication and interoperability between opaque agentic applications.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Holt Skinner
- Ivan Nardini
- Sandi Besen
- Google
libraries: []
companies:
- Google
- IBM Research
- Linux Foundation
tags:
- ai-agents
- interoperability
- open-protocols
- json-rpc
- multi-agent-systems
---

### TL;DR
A2A (Agent2Agent) is an open protocol from Google/Linux Foundation for letting independent AI agents discover, negotiate, and collaborate over HTTP using JSON-RPC 2.0 without exposing their internal state or tools.

### Key Quote
"An open protocol enabling communication and interoperability between opaque agentic applications."

### Summary
- **What it is**
  - Agent2Agent (A2A) is an open protocol for interoperability between AI agents built on different frameworks and running on separate servers.
  - It is designed so agents communicate **as agents**, not merely as tools or API endpoints.

- **Core goals**
  - Let agents:
    - discover each other’s capabilities
    - negotiate interaction modes such as text, forms, and media
    - collaborate on long-running tasks securely
    - keep internal state, memory, tools, and proprietary logic hidden

- **How it works**
  - Uses **JSON-RPC 2.0 over HTTP(S)** as the communication model.
  - Uses **Agent Cards** for discovery and capability advertisement.
  - Supports multiple interaction patterns:
    - synchronous request/response
    - streaming via **SSE**
    - asynchronous push notifications
  - Supports richer payloads including:
    - text
    - files
    - structured JSON data

- **Positioning**
  - A2A is presented as complementary to **MCP**:
    - A2A helps agents collaborate with each other
    - MCP helps agents use tools/resources

- **Ecosystem and SDKs**
  - The README links to SDKs in multiple languages:
    - Python: `pip install a2a-sdk`
    - Go: `go get github.com/a2aproject/a2a-go`
    - JavaScript: `npm install @a2a-js/sdk`
    - Java: via Maven
    - .NET: `dotnet add package A2A`
  - Sample projects are available in the `a2a-samples` repo.

- **Documentation and learning**
  - Main docs site: `a2a-protocol.org`
  - Specification: `a2a-protocol.org/latest/specification/`
  - Includes a DeepLearning.AI short course co-built with Google Cloud and IBM Research.
  - Course topics:
    - making agents A2A-compliant
    - connecting agents with clients
    - orchestrating sequential and hierarchical workflows
    - building a healthcare multi-agent system
    - understanding how A2A complements MCP

- **Project status / roadmap**
  - The repo frames A2A as an evolving protocol with planned enhancements around:
    - richer authorization in Agent Cards
    - a potential `QuerySkill()` method for capability discovery
    - dynamic UX negotiation during tasks
    - client-initiated methods
    - better streaming reliability and push notifications

- **Governance**
  - Open source project under the **Linux Foundation**
  - Contributed by **Google**
  - Licensed under **Apache 2.0**
  - Encourages community contributions via discussions, issues, and feedback forms

### Assessment
Durability is **medium**: the underlying idea of agent interoperability is likely to remain relevant, but the specific protocol details, SDK commands, and roadmap items are version- and ecosystem-dependent. Content type is **mixed**, combining reference/docs with announcement and tutorial-style onboarding. Density is **medium-high** because it packs in protocol goals, transport details, SDK install commands, ecosystem links, and roadmap bullets in a concise README. Originality is mostly **primary source** since this is the project’s own repository README, though it also functions as promotional/introductory documentation. It is best used as **refer-back** material for checking protocol scope, official links, and current positioning. Scrape quality is **good** overall: the main README sections are present, including links, feature lists, SDK commands, and roadmap notes; however, deeper docs, code examples, and any non-README repository contents are not included here.
