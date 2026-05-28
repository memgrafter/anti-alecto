---
url: https://github.com/poetiq-ai/poetiq-arc-agi-solver
title: 'poetiq-ai/poetiq-arc-agi-solver: This repository allows reproduction of Poetiq''s record-breaking submission to the ARC-AGI-1 and ARC-AGI-2 benchmarks.'
scraped_at: '2026-04-12T07:39:55Z'
word_count: 296
raw_file: raw/2026-04-12_poetiq-ai-poetiq-arc-agi-solver-this-repository-allows-reproduction-of-poetiq-s-_ed8a6631.txt
tldr: Poetiq’s repository is a reproducibility package for its claimed record-breaking ARC-AGI-1 and ARC-AGI-2 benchmark runs, with setup instructions, model API key requirements, and pointers to the company’s announcement and verification blog posts.
key_quote: This repository allows reproduction of **Poetiq's** record-breaking submission to the ARC-AGI-1 and ARC-AGI-2 benchmarks.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Poetiq Team
tools:
- Python
- Gemini
- OpenAI
libraries: []
companies:
- Poetiq AI
- ARC Prize
tags:
- benchmarking
- reproducibility
- machine-learning
- artificial-intelligence
- reasoning
---

### TL;DR
Poetiq’s repository is a reproducibility package for its claimed record-breaking ARC-AGI-1 and ARC-AGI-2 benchmark runs, with setup instructions, model API key requirements, and pointers to the company’s announcement and verification blog posts.

### Key Quote
"This repository allows reproduction of **Poetiq's** record-breaking submission to the ARC-AGI-1 and ARC-AGI-2 benchmarks."

### Summary
- **What this is**
  - A GitHub repository from **Poetiq AI** for reproducing its ARC-AGI benchmark results.
  - Positioned as **“SOTA Reasoning on ARC-AGI”** and linked to Poetiq’s public blog posts.
  - Claims the method is now **on top of the official leaderboard**.

- **Context and claims**
  - The repo says it reproduces Poetiq’s **record-breaking submission** to both:
    - **ARC-AGI-1**
    - **ARC-AGI-2**
  - It references two posts for analysis and verification:
    - **“Traversing the Frontier of Superintelligence”** — the launch/announcement post
    - **“Poetiq Shatters ARC-AGI-2 State of the Art at Half the Cost”** — follow-up verification post
  - It mentions both **public eval results** and **official private eval results**.
  - The private leaderboard problems are explicitly noted as **kept private** by ARC Prize.

- **What the repo appears to provide**
  - A reproducible setup for running the Poetiq configuration on ARC-AGI tasks.
  - Reference visuals/charts for:
    - ARC-AGI-1 public eval
    - ARC-AGI-2 public eval
    - official leaderboard results
  - A default configuration labeled **“Poetiq 3 config”** described in the blog post.

- **How to use it**
  - **Prerequisites**
    - Python **3.11+**
    - API keys for whichever models you want to test, explicitly mentioning **Gemini** and **OpenAI**
  - **Quick start**
    1. Create and activate a virtual environment:
       ```bash
       python -m venv .venv
       source .venv/bin/activate
       pip install -r requirements.txt
       ```
    2. Create a **`.env`** file in the repo root with model keys:
       ```bash
       GEMINI_API_KEY=...
       OPENAI_API_KEY=...
       ```
    3. Edit constants in **`main.py`** to choose problem set, number of problems, etc.
    4. Run:
       ```bash
       python main.py
       ```
    5. Optionally modify configurations in **`config.py`** or uncomment alternatives.
  - The repo implies the execution flow is script-based rather than packaged as a library or CLI tool.

- **Contact and citation**
  - Requests citation of the blog post rather than a formal paper:
    - **Poetiq Team. (2025). _Traversing the Frontier of Superintelligence_. Poetiq AI.**
  - Provides contact email: **poetiq@poetiq.ai**
  - Links to Poetiq social accounts on **X**, **LinkedIn**, and **Bluesky**.

### Assessment
This is a **mixed** content type: part repository documentation, part product/marketing announcement, and part tutorial for reproducing benchmark runs. **Durability is medium** because the ARC-AGI benchmark framing is fairly stable, but the model dependencies, API keys, and configuration details are likely to change quickly as provider APIs and repo code evolve. The page is **dense** in concrete setup details but light on technical implementation specifics, so **density is medium**. It is a **primary source** for Poetiq’s own claims and reproduction instructions, though the benchmark claims themselves are promotional and should be treated as company-reported results rather than independent validation. It is best used as **refer-back** material if you want to reproduce the run or verify the stated configuration, not as deep-study technical documentation. **Scrape quality is good** for the README-level content shown, but likely partial with respect to the full repo: code, notebooks, configs, and any referenced images/charts are not actually included here, only described or linked.
