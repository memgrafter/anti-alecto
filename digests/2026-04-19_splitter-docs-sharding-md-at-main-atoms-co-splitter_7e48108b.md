---
url: https://github.com/atoms-co/splitter/blob/main/docs/sharding.md
title: splitter/docs/sharding.md at main · atoms-co/splitter
scraped_at: '2026-04-19T08:40:43Z'
word_count: 716
raw_file: raw/2026-04-19_splitter-docs-sharding-md-at-main-atoms-co-splitter_7e48108b.txt
tldr: Splitter is a coordination system for sharded, stateful distributed services that uses leased shard ownership and routing to support dynamic scaling and multi-region resilience.
key_quote: Shards should be load-balanced across whatever instances are connected, and shard re-assignments might be mildly disruptive at worst but fundamentally benign.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Raft
libraries: []
companies:
- Splitter
- Zookeeper
- etcd
tags:
- distributed-systems
- sharding
- multi-region
- coordination
- stateful-services
---

### TL;DR
Splitter is a coordination system for sharded, stateful distributed services that uses leased shard ownership and routing to support dynamic scaling and multi-region resilience.

### Key Quote
“Shards should be load-balanced across whatever instances are connected, and shard re-assignments might be mildly disruptive at worst but fundamentally benign.”

### Summary
- The document contrasts two distributed service models:
  - **Stateless, request-driven services**: simple at first, but every request can drive more database traffic as complexity grows.
  - **Sharded, stateful services**: instances hold responsibility for a partition of the domain, enabling low-latency reads, authoritative in-memory caching, and stronger correctness at scale.
- The **sharded model** requires three core capabilities:
  - A **partitionable work domain** (for example: users, orders, stores)
  - **Ownership management** for assigning shards to instances
  - **Request routing** to the correct shard owner
- Traditional implementations of sharding ownership/routing may rely on custom coordination systems or distributed stores like **etcd** or **Zookeeper**.

- **Splitter’s model** is designed for **highly resilient multi-region services**, with two main goals:
  - **Dynamic** operation:
    - instances are ephemeral
    - no local disk dependency
    - autoscaling and regional failures should not require special logic
    - shard reassignment should be safe and only mildly disruptive
  - **Multi-region** deployment:
    - shard placement should work with region-local database placement
    - the service should not need to manage shard locality decisions itself
- Splitter handles the core sharding problems in two ways:
  1. **Ownership**
     - Domain and shard management is configured centrally in Splitter.
     - Splitter uses **Raft** for distributed storage and coordination.
     - Service instances connect to Splitter and receive **leased shard assignments**.
     - If an instance crashes or disconnects long enough, its lease expires and shards are reassigned.
  2. **Routing**
     - Instances receive current shard routing data: which instance owns which shards.
     - This supports internal forwarding and fanout.
     - The routing layer is intentionally exposed as a **library**, so services keep control over the data path.
     - It supports both **batch** and **streaming** workloads and does not require 1:1 routing.

- The system is organized around **domains**:
  - A domain may contain one or more **UUID spaces**
  - Each **shard** is a **half-open UUID range**
  - UUID ranges are used because they naturally distribute keys, reduce hotspots, and can be split or merged dynamically
  - This supports **no-downtime re-sharding**, which the document treats as important because service scale is hard to predict in advance

- Example use cases listed:
  - **Keyed Event Queue**: a multi-region message broker for strictly ordered message queues
  - **Robotic Conveyance Routing**: a multi-regional service for managing robots for order dispatch and pickup
  - Services with **in-memory caches of rich objects**

### Assessment
This is a technical/reference-style design document with a clear architectural thesis: Splitter is meant to provide the coordination layer for sharded, stateful services that need dynamic scaling and multi-region resilience. Durability is **medium-high** because the concepts are broadly useful, though the specifics of Splitter’s implementation and tradeoffs are tied to the project’s current design. Content type is **mixed**: part conceptual explanation, part product/architecture documentation. Density is **medium-high** because it packs in concrete terms like Raft, leases, UUID ranges, and example workloads without much filler. Originality is **primary source** since it describes the Splitter model in the project’s own words. Reference style is **refer-back**: useful for understanding the architecture and revisiting when evaluating whether Splitter fits a stateful distributed system. Scrape quality is **good**; the main prose and examples are present, and there’s no sign that important code blocks or images were missed.
