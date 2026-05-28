---
url: https://www.notebookcheck.net/Analysis-of-the-Apple-M5-SoC-Apple-silicon-extends-its-lead-over-AMD-Intel-and-Qualcomm.1144213.0.html
title: https://www.notebookcheck.net/Analysis-of-the-Apple-M5-SoC-Apple-silicon-extends-its-lead-over-AMD-Intel-and-Qualcomm.1144213.0.html
scraped_at: '2026-04-19T21:20:52Z'
word_count: 1490
raw_file: raw/2026-04-19_https-www-notebookcheck-net-analysis-of-the-apple-m5-soc-apple-silicon-extends-i_259f063f.txt
tldr: Notebookcheck’s analysis of Apple’s M5 SoC says the new chip further extends Apple silicon’s lead over AMD, Intel, and Qualcomm by delivering much higher single-core, multi-core, and GPU performance than the M4, though at the cost of somewhat higher power draw.
key_quote: “Apple is once again able to increase performance with the new M5 SoC.”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries: []
companies:
- Apple
- TSMC
- AMD
- Intel
- Qualcomm
tags:
- apple-silicon
- cpu-benchmarks
- gpu-performance
- power-efficiency
- semiconductor-analysis
---

### TL;DR
Notebookcheck’s analysis of Apple’s M5 SoC says the new chip further extends Apple silicon’s lead over AMD, Intel, and Qualcomm by delivering much higher single-core, multi-core, and GPU performance than the M4, though at the cost of somewhat higher power draw.

### Key Quote
“Apple is once again able to increase performance with the new M5 SoC.”

### Summary
- The article compares the **Apple M5 SoC** against the previous **M4/M3 generations** and current chips from **AMD, Intel, and Qualcomm**.
- Apple is using the **third generation of TSMC 3 nm**, with the M5 mainly benefiting from **higher clocks** rather than a major architectural overhaul.
- Two M5 variants are described:
  - **10-core**: 4 performance cores + 6 efficiency cores
  - **9-core**: 3 performance cores + 6 efficiency cores
- The tested system is the **base MacBook Pro 14** with the **10-core M5**.
- Reported power behavior in the MacBook Pro 14:
  - CPU briefly peaks at **30.5 W**, then settles around **27.5 W**
  - GPU draw reaches **18–19 W**
- Notebookcheck’s methodology emphasizes comparing **performance plus power consumption** to estimate efficiency, with measurements taken on an **external display** to reduce display-related variance.

#### Single-core performance
- The M5 is **10–12% faster than the M4** in **Cinebench 2024 single-core**.
- It is said to be **26–38% faster** than the fastest non-Apple processor in their database, the **Intel Core Ultra 9 285K** desktop chip.
- The passively cooled **iPad Pro 11 M5** also leads in **Geekbench 6.5 single-core**.
- Tradeoff: single-core power use rises to about **7–7.7 W**, versus roughly **5.2 W** for the M4.
- Efficiency is noted as **about 4% worse** than the 10-core M4, though Apple’s overall lead remains large.

#### Multi-core performance
- Multi-core performance is **nearly 20% better than M4** on average.
- The M5 can challenge strong mobile x86 chips such as:
  - **Intel Core Ultra 7 255H**
  - **AMD Ryzen AI 9 HX 370**
- Those Intel/AMD chips often need **70 W+** to reach their best results, while the M5’s performance comes at a much lower level of power.
- The M5 also beats the older **Apple M3 Pro**.
- In efficiency, the M5 takes the lead in **Cinebench 2024 multi-core efficiency charts**, followed by the **10-core M4** and then **Qualcomm Snapdragon X Elite 78-100**.

#### GPU performance
- The M5 GPU appears to use about the **same power as the M4 GPU** (**18–19 W**) but is **25–30% faster** in synthetic tests.
- It is clearly ahead of current integrated GPUs from **AMD, Intel, and Qualcomm** in benchmarks.
- In **Cyberpunk 2077** on macOS, the M5 is among the fastest current iGPUs, but it is **roughly on par** with the best versions of:
  - **Intel Arc Graphics 140V**
  - **AMD Radeon 890M**
- In **Baldur’s Gate 3**, the M5 apparently performs better than those same Intel/AMD iGPUs, showing that results vary by game.
- For **Cyberpunk 2077 efficiency**, the M5 is only slightly ahead of the best Arc Graphics 140V, so Apple does **not** have a huge margin in GPU efficiency.

#### Conclusion / takeaway
- Apple continues to optimize its **3 nm chips**, and the M5 further extends Apple’s lead.
- The article calls the M5 the **fastest single-core processor currently available**, even surpassing Intel’s top desktop chip in that metric.
- The main downside is **higher power consumption**, which can slightly reduce battery life and increase short-load power spikes.
- In **multi-core and graphics**, the M5 improves both **performance and efficiency** noticeably.
- Notebookcheck is especially interested in the upcoming **M5 Pro** and **M5 Max**, and also in whether **Intel Panther Lake** and next-gen **Snapdragon X Elite** parts can respond.

### Assessment
This is a **mixed technical analysis/review** with high durability in the short-to-medium term: the core architectural conclusions about Apple’s M5 performance lead will stay useful, but the specific rankings against AMD, Intel, and Qualcomm may age as new chips arrive. The content is **high density**, packed with concrete benchmark comparisons, wattage numbers, and model names, and it is clearly **original analysis** based on Notebookcheck’s own testing rather than a simple summary of others’ claims. It’s best used as a **refer-back** reference if you want benchmark context for the M5’s launch. Scrape quality appears **good** overall, though the captured text references charts and benchmark figures that are not included here, so some visual data is missing.
