---
url: https://www.youtube.com/watch?v=vi-qMzxxtYs
title: 98% Cloud Cost Saved By Writing Our Own Database - YouTube
scraped_at: '2026-04-12T18:52:16Z'
word_count: 4292
raw_file: raw/2026-04-12_98-cloud-cost-saved-by-writing-our-own-database-youtube_5fdfb8c5.txt
tldr: A location-tracking company claims it cut cloud database costs by 98% by replacing Aurora/PostGIS with a custom in-process binary storage engine optimized for high-write, low-retention geospatial data.
key_quote: “we replaced our $10,000 a month Aurora instance with a $200 a month elastic block storage volume”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- AWS Aurora
- PostGIS
- AWS Glacier
- EBS
- io2
- UDP
- TCP
- Vim
libraries: []
companies:
- Hivekit
- AWS
- Redis
- Geomesa
- TigerBeetle
- Cassandra
- Sila
tags:
- cloud-cost-optimization
- database-architecture
- geospatial-data
- binary-storage
- infrastructure
---

### TL;DR
A location-tracking company claims it cut cloud database costs by 98% by replacing Aurora/PostGIS with a custom in-process binary storage engine optimized for high-write, low-retention geospatial data.

### Key Quote
“we replaced our $10,000 a month Aurora instance with a $200 a month elastic block storage volume”

### Summary
- The video/commentary is reacting to a technical article about **Hivekit** and its custom database/storage approach for tracking **tens of thousands of people and vehicles simultaneously**.
- The core workload:
  - Around **13,000 simultaneous connections**
  - Roughly **one location update per second per connection**
  - About **3.5 billion updates per month**
  - Customers use the data in very different ways:
    - coarse route replay for rental cars
    - precise replay before accidents for delivery companies
    - worker/zone compliance tracking with **sub-meter accuracy**
- Because the company can’t know in advance how granular each customer’s needs are, it stores **every location update** rather than pre-aggregating.
- Their requirements are unusual:
  - **Very high write throughput**: up to **30,000 location updates/sec per node**
  - **Multiple nodes writing simultaneously**
  - **Small disk footprint**
  - **Fast reads**, but reads are much less frequent than writes
  - **Low consistency guarantees**: they can tolerate losing about **1 second** of buffered updates
- They were previously using **AWS Aurora with PostGIS**, costing **$10,000/month** for the database alone.
- They say many alternatives were insufficient because they were either:
  - only extensions on top of existing databases
  - not suited to their exact write-heavy, custom storage pattern
- Their solution:
  - a **purpose-built in-process storage engine** inside the same server executable
  - a **minimal delta-based binary format**
  - a separate **index file** mapping string IDs/types to compact identifiers
  - storing the **full state every 200 writes**, and only **deltas** in between
  - each location update reportedly takes only **34 bytes**
  - allowing about **30 million location updates per gigabyte**
- Claimed results:
  - **98% reduction in cloud cost**
  - replaced Aurora with a **$200/month EBS volume**
  - queries improved significantly; one example says recreating a historical point-in-time view went from **~2 seconds to 13 milliseconds**
- The speaker is broadly impressed but skeptical:
  - questions whether engineering effort outweighed $10k/month savings
  - repeatedly argues that writing your own database is usually risky and hard
  - praises the result as impressive but warns it’s a specialized solution, not a general recommendation
- The commentary emphasizes a recurring warning:
  - custom storage can be the best fit for a narrowly defined workload
  - but it introduces complexity, especially around binary formats and **versioning**
  - the speaker strongly notes that a **version field** should exist in the binary encoding
- The piece ends by noting the product appears to be **Hivekit**, a “location infrastructure for the internet,” and jokingly frames it as something the NSA would use.

### Assessment
This is a **mixed** content piece: mostly a **commentary/reaction** to a technical article, with some embedded summary of the underlying product. Durability is **medium** because the architectural lesson is timeless, but the pricing, cloud services, and product specifics are version- and time-sensitive. Density is **high**: it includes concrete numbers, design constraints, storage format details, and performance claims. Originality is **mixed**—the underlying article seems like a primary source/product write-up, while the speaker provides reactive analysis and skepticism. Reference style is **refer-back** if you want the architectural pattern and cost story, but **skim-once** if you only care about the punchline. Scrape quality is **partial**: the transcript is messy and conversational, with likely missing visuals, diagrams, and any code/examples shown on screen.
