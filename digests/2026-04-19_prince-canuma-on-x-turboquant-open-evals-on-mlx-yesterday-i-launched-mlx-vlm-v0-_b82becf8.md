---
url: https://x.com/Prince_Canuma/status/2040877782922649865?s=20
title: 'Prince Canuma on X: "TurboQuant: Open Evals on MLX 🔥 Yesterday I launched mlx-vlm v0.4.4 with major TurboQuant performance improvements. Today, the open benchmark results on MM-NIAH (val, 520 samples) using Gemma 4 26B IT by @GoogleDeepMind on M3 Ultra: → 0 quality loss — 78% accuracy for both https://t.co/cHZUKkDsBd" / X'
scraped_at: '2026-04-19T07:29:36Z'
word_count: 92
raw_file: raw/2026-04-19_prince-canuma-on-x-turboquant-open-evals-on-mlx-yesterday-i-launched-mlx-vlm-v0-_b82becf8.txt
tldr: Prince Canuma announces TurboQuant benchmark results for mlx-vlm v0.4.4, claiming no quality loss on MM-NIAH with Gemma 4 26B IT on M3 Ultra, while cutting KV cache use by 30–53% and speeding decoding by 1.16× at ~60K context.
key_quote: → 0 quality loss — 78% accuracy for both BL and TBQ
durability: medium
content_type: announcement
density: high
originality: primary
reference_style: skim-once
scrape_quality: partial
people:
- Prince Canuma
- Google DeepMind
tools:
- mlx-vlm
- TurboQuant
libraries: []
companies:
- Google DeepMind
tags:
- machine-learning
- benchmarking
- quantization
- mlx
- vlm
---

### TL;DR
Prince Canuma announces TurboQuant benchmark results for `mlx-vlm v0.4.4`, claiming no quality loss on MM-NIAH with Gemma 4 26B IT on M3 Ultra, while cutting KV cache use by 30–53% and speeding decoding by 1.16× at ~60K context.

### Key Quote
“→ 0 quality loss — 78% accuracy for both BL and TBQ”

### Summary
- This is a short X post announcing **“TurboQuant: Open Evals on MLX”**.
- The author says they **launched `mlx-vlm v0.4.4` the previous day**, with “major TurboQuant performance improvements.”
- Reported benchmark setup:
  - **Benchmark:** MM-NIAH
  - **Split:** validation
  - **Sample size:** **520 samples**
  - **Model:** **Gemma 4 26B IT** by **Google DeepMind**
  - **Hardware:** **M3 Ultra**
- Claimed results:
  - **0 quality loss**
  - **78% accuracy** for both **BL** and **TBQ**
  - **97% answer agreement** across all context lengths
  - **30–53% KV cache savings** where TBQ is active
  - **1.16× decode speedup** at about **60K context**
- The post includes a **“Benchmark code”** link, implying reproducibility or supporting materials, but the actual code is not included in the scrape.
- The post is framed as a performance/benchmark update for MLX-based VLM inference, specifically highlighting TurboQuant’s efficiency gains without apparent accuracy degradation.

### Assessment
This is a **mixed** content item that is mostly a **technical announcement** with benchmark claims. Its **durability is medium**: the high-level idea of quantization improving inference efficiency is lasting, but the concrete numbers, `mlx-vlm v0.4.4`, MM-NIAH results, and Gemma 4 26B IT on M3 Ultra are version- and hardware-specific and may age quickly. The **density is medium-high** because it compresses several benchmark metrics into a brief post. It appears to be a **primary source** from the project author, which makes it useful for tracking the author’s own claims, though not independently verified here. Best used as **skim-once / refer-back** material if you’re tracking MLX, TurboQuant, or VLM inference performance. **Scrape quality is partial**: the post text is captured, but the linked benchmark code and image contents are not included.
