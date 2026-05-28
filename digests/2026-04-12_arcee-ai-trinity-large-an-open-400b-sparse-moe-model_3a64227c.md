---
url: https://www.arcee.ai/blog/trinity-large
title: 'Arcee AI | Trinity Large: An Open 400B Sparse MoE Model'
scraped_at: '2026-04-12T07:35:03Z'
word_count: 1580
raw_file: raw/2026-04-12_arcee-ai-trinity-large-an-open-400b-sparse-moe-model_3a64227c.txt
tldr: Arcee AI announces Trinity-Large, an open 400B sparse MoE model family with three checkpoints—Preview, Base, and TrueBase—trained on 17T tokens on 2048 Nvidia B300s, aiming to deliver frontier-level performance for reasoning, coding, and agentic use.
key_quote: Being able to say that about a frontier-level model is something we’re immeasurably proud of.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Arcee AI
- DatologyAI
tools:
- OpenRouter
- Kilo Code
- Cline
- OpenCode
- chat.arcee.ai
- docs.arcee.ai
libraries:
- Muon
- AdamW
companies:
- Arcee AI
- Nvidia
- OpenRouter
- DatologyAI
- Kilo Code
- Cline
- OpenCode
- Llama-4-Maverick
tags:
- open-source-llm
- mixture-of-experts
- model-training
- agentic-ai
- inference-infrastructure
---

### TL;DR
Arcee AI announces Trinity-Large, an open 400B sparse MoE model family with three checkpoints—Preview, Base, and TrueBase—trained on 17T tokens on 2048 Nvidia B300s, aiming to deliver frontier-level performance for reasoning, coding, and agentic use.

### Key Quote
"Being able to say that about a frontier-level model is something we’re immeasurably proud of."

### Summary
- **What was released**
  - **Trinity-Large-Preview**: lightly post-trained, chat-ready, and described as a **non-reasoning “instruct” model**
  - **Trinity-Large-Base**: best pretraining checkpoint after the full **17T-token** run
  - **Trinity-Large-TrueBase**: an earlier **10T-token** checkpoint with **no instruct data** and **no LR annealing**, intended as a “true base” research baseline
- **Model architecture**
  - **400B total parameters**
  - **13B active parameters per token**
  - **Sparse MoE** with **256 experts**, **4 active experts per token**
  - The team increased dense layers from **3 to 6** to improve routing stability at this sparsity level
- **Training scale and infrastructure**
  - Trained on **2048 Nvidia B300 GPUs**
  - The pretraining run used **just over 30 days** of machine time and finished in **33 days**
  - The authors claim it is the **largest publicly stated pretraining run on B300s**
  - They estimate **2–3x faster training/inference** than peers in the same weight class, helped by sparsity and efficient attention
- **Training and optimization details**
  - MoE routing is stabilized by:
    - adjusting router bias for over/underused experts
    - capping updates with **tanh**
    - adding **momentum**
    - using a small **per-sequence balance loss**
  - Uses **z-loss** to prevent LM-head logits from growing uncontrollably
  - Fastest setup used **HSDP with expert parallelism = 8**, yielding **2048 data-parallel ranks**
  - Batch size was increased after **5T tokens**
  - They cite **Muon** as supporting a larger critical batch size than AdamW, and reference the **MiniMax-01** paper for batch scaling in this regime
- **Data**
  - Trained on **17T tokens** curated by **DatologyAI**
  - Data was split into **10T / 4T / 3T** phases
  - Dataset emphasizes:
    - programming
    - STEM
    - reasoning
    - multilingual data
  - Targets **14 non-English languages**
  - Over **8T synthetic tokens** were generated across web, code, math, reasoning, and multilingual domains using rephrasing techniques
- **Performance claims**
  - The authors say **Trinity-Large-Base** matches or exceeds peer open-base models across benchmarks in:
    - math
    - coding
    - scientific reasoning
    - raw knowledge absorption
  - Preview is described as competitive with **Llama-4-Maverick Instruct** on standard academic benchmarks
  - They also say the reasoning model is promising but needs more post-training before it becomes maximally useful
- **Product / deployment notes**
  - **Preview** is available now via **OpenRouter**, free during preview until at least **February 2026**
  - Integrations were prepared for **Kilo Code, Cline, and OpenCode**
  - **Trinity-Large** natively supports **512k context**
  - The preview API currently runs at **128k context** with **8-bit quantization** while hosting infrastructure is tuned
  - They provide access points for:
    - **chat.arcee.ai**
    - **docs.arcee.ai**
    - OpenRouter model page
- **Cost and company framing**
  - Arcee says the whole effort—**compute, salaries, data, storage, ops**—cost **$20 million**
  - They frame the release as proof that a smaller lab can still ship a frontier-class open model
  - They emphasize that Open Models get better only if people use them in real-world settings

### Assessment
This is a **mixed announcement/technical deep dive** with strong product-marketing framing but enough concrete details to be useful as a reference. Durability is **medium** because the architecture and training ideas are broadly informative, but the specific model status, benchmark comparisons, API context limits, and availability windows are tied to the January 2026 release and will age quickly. Density is **high**: it includes architecture specs, training setup, data scale, optimization tricks, deployment notes, and cost figures. Originality is **primary source** since it appears to be Arcee’s own launch post describing their work and claims. As a reference, it’s best used **refer-back** for model specs, release variants, and launch details rather than deep-study, though the training notes may be worth revisiting for MoE routing and large-scale sparse training ideas. Scrape quality is **partial**: the text captures most of the article’s narrative and key claims, but some sections appear incomplete or formatting-truncated, such as the “Weights:” line and likely any embedded benchmark tables, figures, or technical report equations.
