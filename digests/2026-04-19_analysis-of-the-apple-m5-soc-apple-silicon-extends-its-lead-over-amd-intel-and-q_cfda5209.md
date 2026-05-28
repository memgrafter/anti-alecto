---
url: https://www.reddit.com/r/hardware/comments/1odvzw4/analysis_of_the_apple_m5_soc_apple_silicon/
title: 'Analysis of the Apple M5 SoC: Apple silicon extends its lead over AMD, Intel and Qualcomm : r/hardware'
scraped_at: '2026-04-19T21:59:33Z'
word_count: 3648
raw_file: raw/2026-04-19_analysis-of-the-apple-m5-soc-apple-silicon-extends-its-lead-over-amd-intel-and-q_cfda5209.txt
tldr: A r/hardware thread about Notebookcheck’s Apple M5 SoC analysis argues that the M5 is a big single-core and efficiency win for Apple, but the article’s GPU wording is inconsistent and the biggest debate is whether its iGPU lead is meaningful given competing AMD/Intel/Qualcomm chips can catch up at much higher power.
key_quote: “The new M5 chip features one of the fastest current iGPUs (with the exception of Strix Halo), but it is no faster than the best versions of the Intel Arc Graphics 140V or the AMD Radeon 890M.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- u/-protonsandneutrons-
- u/WarEagleGo
- u/luuuuuku
- u/DerpSenpai
tools:
- Notebookcheck
- Cinebench 2024
- Geekbench Compute
libraries: []
companies:
- Apple
- AMD
- Intel
- Qualcomm
- Notebookcheck
tags:
- apple-silicon
- gpu-performance
- laptop-benchmarks
- power-efficiency
- hardware-discussion
---

### TL;DR
A r/hardware thread about Notebookcheck’s Apple M5 SoC analysis argues that the M5 is a big single-core and efficiency win for Apple, but the article’s GPU wording is inconsistent and the biggest debate is whether its iGPU lead is meaningful given competing AMD/Intel/Qualcomm chips can catch up at much higher power.

### Key Quote
> “The new M5 chip features one of the fastest current iGPUs (with the exception of Strix Halo), but it is no faster than the best versions of the Intel Arc Graphics 140V or the AMD Radeon 890M.”

### Summary
- **Top comment (verbatim):** "LOL, the first paragraph says the M5 iGPU is **well ahead of** while the 3rd paragraph says "new M5 chip features one of the fastest current iGPUs (with the exception of Strix Halo), **but it is no faster** than the best versions of the Intel Arc Graphics 140V or the AMD Radeon 890M." > The new GPU is also well ahead of the current iGPUs from AMD, Intel, and Qualcomm. > The situation is slightly different when playing Cyberpunk 2077. The title has now been released as a native version for macOS, which is why we can now better assess the performance (we use the pure performance without Metal FX upscaling). > The new M5 chip features one of the fastest current iGPUs (with the exception of Strix Halo), but it is no faster than the best versions of the Intel Arc Graphics 140V or the AMD Radeon 890M."
- **Top commenter:** `u/WarEagleGo`

- **Thread topics:**
  - Notebookcheck’s seemingly contradictory claims about M5 GPU performance
  - M5 power draw vs M4 in Cinebench 2024
  - Whether Apple’s performance lead is “real” or mostly power-class dependent
  - How M5 compares with AMD Strix Point/Strix Halo, Intel Arc 140V, and Qualcomm Snapdragon X2
  - Gaming performance vs synthetic/compute performance on Apple Silicon

- The thread is centered on a Notebookcheck review/article titled **“Analysis of the Apple M5 SoC: Apple silicon extends its lead over AMD, Intel and Qualcomm.”**
- The main disagreement is whether the article fairly compares devices:
  - One side says the M5 iGPU is clearly ahead in many benchmarks, especially at roughly **28W sustained**.
  - Others argue that AMD/Intel can match or beat it only at much higher power levels, so the comparison is not like-for-like.
  - A separate criticism is that the article mixes phrasing: it says the M5 GPU is **“well ahead”** in one section but **“no faster than”** competing iGPUs in another.
- The OP / author account (`u/-protonsandneutrons-`) posts benchmark context:
  - Under **Cinebench 2024**:
    - **Single-thread power**: M4 ≈ **5.2W**, M5 ≈ **7.0–7.7W**
    - **Multi-thread power**: M4 ≈ **24W**, M5 ≈ **27.5W**
    - Claimed changes: **+34% to +48%** more power in 1T, **+15%** in nT
  - They argue the M5’s perf/W is mostly stable because performance rose too, but this is **not “free” performance**.
  - They note the node shift was only **TSMC N3E → N3P**, with roughly **3% higher clocks** and higher IPC.
- A recurring theme is that Apple still appears ahead in:
  - **single-thread performance**
  - **single-thread efficiency**
  - **overall perf/W at low-to-moderate power**
- But critics note:
  - the M5 is a smaller chip (**4P + 6E**) and cannot be directly compared to larger AMD/Intel laptop CPUs in multicore
  - GPU performance is highly workload-dependent; only a couple of games are discussed, and **Cyberpunk 2077** may be a poor or atypical Mac benchmark
- Several commenters focus on gaming and GPU caveats:
  - M5’s GPU may look strong in compute/pro apps but less impressive in actual games
  - Mac gaming is still seen as limited by ports, drivers, and Apple’s ecosystem priorities
  - Some argue the M5 GPU is around the level of **Intel Arc 140V / AMD Radeon 890M** in real gaming workloads, while others say that still ignores the power gap
- Qualcomm comparisons are also heavily debated:
  - One camp says Qualcomm’s newer chips are close or even ahead in some CPU metrics, especially multicore
  - Another says Apple will still have stronger GPU performance and that Qualcomm’s comparison is not apples-to-apples because the core counts and power envelopes differ
- There’s also a side argument about what counts as an **iGPU**:
  - Some users dispute whether Intel Arc 140V or AMD Radeon 890M should be called “integrated” in the same sense as Apple’s GPU
  - Others say this distinction is irrelevant to consumers and only matters in technical classification
- Tone of the thread:
  - largely argumentative and nitpicky
  - several comments accuse the article of being AI-written or poorly worded
  - many users still agree on the broad conclusion that Apple remains ahead in efficiency, especially in low-power laptop scenarios

### Assessment
This is a **mixed** content item combining article critique, benchmark interpretation, and community argument. Durability is **medium**: the specific M5 numbers and competitor comparisons will age as newer chips ship, but the broader themes—Apple’s efficiency lead, power-class comparisons, and the difficulty of comparing laptop APUs across wattages—remain useful. Density is **high**, with lots of specific wattage figures, chip names, and benchmark references, though the discussion is somewhat repetitive and opinionated. Originality is mostly **commentary/synthesis** rather than primary research: the thread reacts to a Notebookcheck analysis and expands on its claims. Best reference style is **skim-once / refer-back** for the benchmark figures and the main dispute; not really deep-study material unless you care about the technical comparison methodology. Scrape quality is **good**: the thread metadata, prominent viewpoints, and substantial discussion sample are present, though the full comment tree and any linked article/images are not included.
