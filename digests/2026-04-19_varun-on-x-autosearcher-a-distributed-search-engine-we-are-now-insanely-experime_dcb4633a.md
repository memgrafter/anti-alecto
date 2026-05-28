---
url: https://x.com/varun_mathur/status/2031550020101480507
title: 'Varun on X: "Autosearcher: a distributed search engine We are now insanely experimenting with building a distributed search engine utilizing the same pattern @karpathy introduced with autoresearch: give an agent a metric, a tight propose→run→evaluate→keep/revert loop, and let it iterate. https://t.co/8VeY0GSEvw" / X'
scraped_at: '2026-04-19T07:21:55Z'
word_count: 251
raw_file: raw/2026-04-19_varun-on-x-autosearcher-a-distributed-search-engine-we-are-now-insanely-experime_dcb4633a.txt
tldr: Varun describes “Autosearcher,” an experimental distributed search engine that reuses an agentic propose→run→evaluate→keep/revert loop from Autoresearch, combining P2P gossip, shared leaderboards, and continuous user-feedback training to scale search quality and indexing capacity.
key_quote: give an agent a metric, a tight propose→run→evaluate→keep/revert loop, and let it iterate.
durability: medium
content_type: announcement
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Varun Mathur
- Andrej Karpathy
libraries:
- CRDT
- DPO
- GossipSub
companies:
- Hyperspace
tags:
- distributed-systems
- search-engines
- agentic-ai
- machine-learning
- peer-to-peer-networking
---

### TL;DR
Varun describes “Autosearcher,” an experimental distributed search engine that reuses an agentic propose→run→evaluate→keep/revert loop from Autoresearch, combining P2P gossip, shared leaderboards, and continuous user-feedback training to scale search quality and indexing capacity.

### Key Quote
“give an agent a metric, a tight propose→run→evaluate→keep/revert loop, and let it iterate.”

### Summary
- **What it is:** A proposed distributed search engine called **Autosearcher** built by the **Hyperspace** team.
- **Core idea:** Apply the same pattern used in **autoresearch**:
  - Give each agent a **metric**
  - Let it **propose → run → evaluate → keep/revert**
  - Use repeated iteration to improve performance autonomously
- **Prior claim used as evidence:** The author says their **autoresearch network** showed this approach can work at scale:
  - **67 autonomous agents**
  - **704 ML training experiments**
  - Completed in **20 hours**
  - Reportedly rediscovered **Kaiming initialization**, **RMSNorm**, and **compute-optimal training schedules**
  - This happened through “pure experimentation” plus **gossip-based cross-pollination**
- **How knowledge spreads:**  
  - Agents share discoveries over **GossipSub**
  - A **CRDT-replicated leaderboard** lets new agents bootstrap from the swarm’s shared state
  - The network is described as compounding insight faster than any single agent
- **Search-engine application:**  
  - Each Hyperspace agent runs an **autonomous search researcher**
  - Agents propose **ranking mutations**
  - Evaluate them using **NDCG@10**
  - Use **real query-passage data**
  - Share improvements with peers for cross-pollination
- **Architecture described:** A **seven-stage distributed pipeline** running across a **P2P network**
  - **Browser agents** contribute pages passively
  - **Desktop agents** crawl and index
  - **GPU nodes** perform neural reranking
- **Feedback loop from users:**  
  - Every user click becomes a **DPO training pair**
  - Those training signals improve the ranking model
  - **Gradient gossip** distributes updates to all agents
- **Scale claims:** The post argues the system benefits from a compound flywheel:
  - At **10,000 agents**: **500,000 pages indexed per day**
  - At **1 million agents**: **50 million pages per day**
  - Claims **90%+ cache hit rates** and **sub-50ms latency**
- **Overall pitch:** The network is framed as a self-improving search system that “gets smarter with every query,” contrasting with centralized search.
- **Important limitation:** This is an **announcement / concept pitch**, not a technical paper or benchmark report. It includes ambitious performance and scaling claims but no detailed implementation evidence in the captured text.

### Assessment
This is a **mixed** announcement and technical concept pitch with moderate-to-high durability for the underlying pattern (agentic optimize/evaluate loops, gossip-based coordination, distributed learning), but low durability for the specific project claims because they depend on current experimental status. The content is **dense** with concrete metrics, system components, and scale numbers, but it remains **primary-source commentary** from the project author rather than a neutral evaluation. It’s best treated as **refer-back** material if you want to remember the architecture and claims, and it is only partially trustworthy as evidence because it doesn’t include detailed methodology, benchmarks, or independently verified results. **Scrape quality is partial**: the thread text is captured, but the “Code and other links in followup tweet” are missing, and any linked media or follow-up details are not included.
