---
url: https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md
title: open-infra-index/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md at main · deepseek-ai/open-infra-index
scraped_at: '2026-04-19T07:53:34Z'
word_count: 986
raw_file: raw/2026-04-19_open-infra-index-202502opensourceweek-day-6-one-more-thing-deepseekv3r1-inferenc_b5227d59.txt
tldr: DeepSeek describes how its V3/R1 online inference system uses large-scale cross-node expert parallelism, communication/computation overlap, and several load balancers to serve huge MoE traffic efficiently on H800 GPUs, while also publishing 24-hour service statistics and rough cost/revenue estimates.
key_quote: 'the optimization objectives of serving DeepSeek-V3/R1 inference are: **higher throughput and lower latency.**'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries: []
companies:
- DeepSeek
tags:
- inference-systems
- expert-parallelism
- load-balancing
- moe
- gpu-serving
---

### TL;DR
DeepSeek describes how its V3/R1 online inference system uses large-scale cross-node expert parallelism, communication/computation overlap, and several load balancers to serve huge MoE traffic efficiently on H800 GPUs, while also publishing 24-hour service statistics and rough cost/revenue estimates.

### Key Quote
“the optimization objectives of serving DeepSeek-V3/R1 inference are: **higher throughput and lower latency.**”

### Summary
- **Core goal:**  
  DeepSeek says its inference-serving design is optimized for two objectives:
  - **higher throughput**
  - **lower latency**

- **Main architectural choice: cross-node Expert Parallelism (EP):**
  - EP increases batch size, which improves GPU matrix efficiency and throughput.
  - EP spreads experts across GPUs so each GPU handles only a small subset of experts, reducing memory access pressure and latency.
  - But EP also adds complexity:
    - cross-node communication must be hidden behind computation
    - multiple nodes require **Data Parallelism (DP)** and load balancing across DP instances

- **Large-scale EP for DeepSeek-V3/R1:**
  - The model has **256 experts per layer**, with only **8 activated** at a time.
  - This extreme sparsity requires very large batch sizes to keep per-expert work efficient.
  - Because the system uses **prefill-decode disaggregation**, it uses different parallelism settings for the two phases:
    - **Prefill:** `Routed Expert EP32`, `MLA/Shared Expert DP32`
      - Each deployment unit spans **4 nodes**
      - Each GPU handles **9 routed experts** and **1 shared expert**
    - **Decode:** `Routed Expert EP144`, `MLA/Shared Expert DP144`
      - Each deployment unit spans **18 nodes**
      - Each GPU manages **2 routed experts** and **1 shared expert**

- **Communication/computation overlap strategy:**
  - To reduce the communication overhead from large-scale EP, DeepSeek uses a **dual-batch overlap strategy**
    - A batch is split into **two microbatches**
    - During **prefill**, the two microbatches alternate so communication from one overlaps with computation from the other
  - During **decode**, stage times are unbalanced, so they:
    - split the attention layer into **two steps**
    - use a **5-stage pipeline** to overlap communication and computation more smoothly
  - The article points readers to `https://github.com/deepseek-ai/profile-data` for more details.

- **Load balancing problem and solutions:**
  - DeepSeek emphasizes that large-scale EP and DP can create bottlenecks if one GPU is overloaded with computation or communication.
  - They define three balancer types:
    1. **Prefill Load Balancer**
       - Problem: varying request counts and sequence lengths across DP instances
       - Goals:
         - balance **core-attention computation**
         - balance **dispatch send load** by equalizing input token counts per GPU
    2. **Decode Load Balancer**
       - Problem: uneven request counts and sequence lengths affect KV cache usage and dispatch send load
       - Goals:
         - balance **KVCache usage**
         - balance **request counts** per GPU
    3. **Expert-Parallel Load Balancer**
       - Problem: some experts are inherently hotter than others
       - Goal:
         - balance expert computation by minimizing the maximum **dispatch receive load** across GPUs

- **Online inference system characteristics:**
  - The system runs on **H800 GPUs**
  - It uses precision consistent with training:
    - **FP8** for matrix multiplications and dispatch transmissions
    - **BF16** for core MLA computations and combine transmissions
  - The deployment scales up during daytime demand and scales down at night to free resources for research and training

- **24-hour service statistics cited in the article**  
  Time window: **UTC+8 02/27/2025 12:00 PM to 02/28/2025 12:00 PM**
  - **Peak node occupancy:** 278 nodes
  - **Average occupancy:** 226.75 nodes
  - Each node contains **8 H800 GPUs**
  - Assuming **$2/hour per H800 GPU**, DeepSeek estimates:
    - **daily cost: $87,072**
  - Traffic totals:
    - **608B input tokens**
    - **342B input tokens (56.3%)** hit the **on-disk KV cache**
    - **168B output tokens**
  - Performance:
    - average output speed: **20–22 tokens/sec**
    - average KV cache length per output token: **4,989 tokens**
    - per H800 node throughput:
      - about **73.7k input tokens/sec** during prefill
      - about **14.8k output tokens/sec** during decode
  - The statistics include traffic from **web, app, and API**

- **Revenue/cost note:**
  - If all tokens were billed at **DeepSeek-R1 pricing**, the article estimates:
    - **daily revenue: $562,027**
    - **cost profit margin: 545%**
  - R1 pricing cited:
    - **$0.14/M input tokens** (cache hit)
    - **$0.55/M input tokens** (cache miss)
    - **$2.19/M output tokens**
  - But actual revenue is lower because:
    - **V3 pricing is lower than R1**
    - **web and app are free**
    - **nighttime discounts** apply during off-peak hours

### Assessment
This is a **mixed technical/reference** post with fairly high density and strong practical detail. Its durability is **medium**: the architectural ideas around expert parallelism, overlap, and load balancing are broadly useful, but the exact numbers, hardware choice (H800), dates, and pricing/cost estimates are time-sensitive and may age quickly. The content is **primary-source** style, since it appears to describe DeepSeek’s own system and metrics rather than summarizing others. It is best used as a **refer-back** reference for understanding DeepSeek’s serving architecture and operational tradeoffs, not as a deep tutorial. Scrape quality is **good** overall, but the embedded figures are referenced rather than visible, so some diagram-specific details may be missing.
