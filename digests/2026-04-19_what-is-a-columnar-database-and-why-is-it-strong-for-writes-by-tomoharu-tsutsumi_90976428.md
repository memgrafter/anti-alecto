---
url: https://tomoharutsutsumi.medium.com/what-is-a-columnar-database-and-why-is-it-strong-for-writes-012bf9c032a3
title: What is a Columnar Database and Why is it Strong for Writes? | by Tomoharu Tsutsumi | Medium
scraped_at: '2026-04-19T04:00:57Z'
word_count: 1573
raw_file: raw/2026-04-19_what-is-a-columnar-database-and-why-is-it-strong-for-writes-by-tomoharu-tsutsumi_90976428.txt
tldr: Tomoharu Tsutsumi’s Medium post argues that columnar databases can be write-efficient because they batch, compress, parallelize, and append data by column, but it’s a broad introductory explainer with simplistic technical claims and little engine-specific evidence.
key_quote: “Columnar databases handle data writes efficiently by appending values to columns in batches.”
durability: medium
content_type: tutorial
density: medium
originality: commentary
reference_style: skim-once
scrape_quality: partial
people:
- Tomoharu Tsutsumi
- MySQL
- PostgreSQL
- InfluxDB
tools: []
libraries: []
companies:
- Amazon Redshift
- Google BigQuery
tags:
- columnar-databases
- database-architecture
- write-performance
- time-series-data
- data-warehousing
---

### TL;DR
Tomoharu Tsutsumi’s Medium post argues that columnar databases can be write-efficient because they batch, compress, parallelize, and append data by column, but it’s a broad introductory explainer with simplistic technical claims and little engine-specific evidence.

### Key Quote
“Columnar databases handle data writes efficiently by appending values to columns in batches.”

### Summary
- **Article type:** short Medium explainer, published **Dec 22, 2024** by **Tomoharu Tsutsumi**.
- Defines a **columnar database** as one that stores data by **columns rather than rows**, contrasting it with row-oriented systems like **MySQL** and **PostgreSQL**.
- Uses a simple table example (`ID, Name, Age, City`) to show the difference between:
  - **row storage**: records stored together row by row
  - **column storage**: each column stored as a separate sequence of values
- Main claim: columnar databases are “strong for writes” because they:
  - support **efficient batch writes**
  - reduce **I/O overhead**
  - achieve **high compression ratios**
  - allow **parallel writes**
  - use **write-ahead logging (WAL)** and batching
  - work well for **append-only workloads**
- Examples used:
  - log ingestion for batch writes
  - IoT sensor streams for parallel writes
  - stock-price recording for append-only storage
- Lists use cases where the author says columnar databases fit well:
  - **real-time analytics**
  - **time-series data**
  - **data warehousing**
- Names specific systems:
  - **InfluxDB** for time-series
  - **Amazon Redshift**
  - **Google BigQuery**
- Notes limitations:
  - frequent **row-level updates/deletes** can be inefficient
  - **complex joins** may underperform compared with row-oriented databases
- Concludes that columnar databases are best for **high-throughput ingestion**, especially in analytics/time-series/warehouse contexts.

### Assessment
This is a **tutorial/explainer** with **medium durability**: the general columnar-vs-row concept is timeless, but the article is tied to current database framing and contains simplified performance claims that may age poorly. The content is **medium density** and **synthesis-like** rather than primary research; it reads as a high-level summary, not an original benchmarked analysis. Its **reference style** is mostly **skim-once** unless you want a quick refresher on the terminology. The biggest limitation is **technical credibility/usefulness**: the article presents a broad claim that columnar databases are strong for writes, but it gives no engine-specific evidence, workload details, or benchmarks, and the reasoning is somewhat misleading because column stores are more commonly associated with read/analytics optimization and append-heavy ingestion rather than general write superiority. **Scrape quality is partial-but-usable**: the main text is present, but the page includes a lot of Medium UI/recommendation clutter, subscription prompts, and image placeholders, which makes the extraction noisier than the actual article.
