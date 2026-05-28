---
url: https://jackhopkins.github.io/factorio-learning-environment/versions/0.3.0.html
title: Factorio Learning Environment - v0.3.0
scraped_at: '2026-04-12T10:37:05Z'
word_count: 3149
raw_file: raw/2026-04-12_factorio-learning-environment-v0-3-0_6567bd5a.txt
tldr: FLE v0.3.0 is a major Factorio-agent benchmark release that adds a headless renderer, Gym-style interface, and CLI-driven evals, while reporting that frontier models still struggle with long-horizon planning, state tracking, and robust automation in lab-play.
key_quote: “FLE no longer depends on the Factorio game client, enabling massively scalable experimentation.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Claude
- GPT
- Gemini
- Grok
- Claude Opus 4.1
- GPT-5
- Gemini 2.5 Pro
- Grok 4
tools:
- uv
- fle
- OpenAI Gym
- Weights & Biases
libraries: []
companies:
- Factorio Learning Environment
tags:
- agent-benchmarking
- factorio
- long-horizon-planning
- reinforcement-learning
- multimodal-agents
---

### TL;DR
FLE v0.3.0 is a major Factorio-agent benchmark release that adds a headless renderer, Gym-style interface, and CLI-driven evals, while reporting that frontier models still struggle with long-horizon planning, state tracking, and robust automation in lab-play.

### Key Quote
“FLE no longer depends on the Factorio game client, enabling massively scalable experimentation.”

### Summary
- **What this release is**
  - Version **0.3.0** of the **Factorio Learning Environment (FLE)**.
  - Positioned as a major step toward evaluating agents on **long-term planning, reasoning, and world modeling**.
  - The page includes a short getting-started flow:
    - `uv add factorio-learning-environment`
    - `fle cluster start`
    - `fle eval --config configs/gym_run_config.json`

- **Main product changes in v0.3.0**
  - **No longer depends on the Factorio game client**, which allows more scalable experimentation.
  - Introduces a **new headless game renderer** that still provides **realistic pixel observations** for multimodal research.
  - Standardizes the environment to the **OpenAI Gym interface** for easier integration into research codebases.
  - Adds a **CLI** for one-line experiment runs.
  - Evaluation code is open-sourced with:
    - **Weights & Biases logging**
    - **sweep resuming**
    - **analysis tools**

- **Example agent behavior shown**
  - The page includes several code-like snippets of an agent building an **iron gear wheel factory**.
  - The snippets illustrate iterative debugging:
    - power setup with **offshore pump**, **boiler**, and **steam engine**
    - mining with **electric mining drills** and **electric furnaces**
    - assembly using an **Assembling Machine 2** to craft **iron gear wheels**
    - repeated mistakes involving **blocking chests**, belt routing, and rethinking logistics
  - These examples are used to demonstrate how agents interact programmatically with the environment and how errors emerge during complex factory construction.

- **Observation / interface design**
  - Agents receive a structured **Observation** object with fields such as:
    - `raw_text`
    - `entities`
    - `inventory`
    - `research`
    - `game_info`
    - `flows`
    - `messages`
    - `task_info`
    - `task_verification`
    - `serialized_functions`
    - `map_image`
  - The page emphasizes that this mix of structured data and human-readable text supports:
    - spatial awareness
    - production tracking
    - debugging
    - multi-step planning
    - optional visual reasoning
  - The agent harness concatenates these fields into a formatted **markdown string**.

- **Lab-play benchmark setup**
  - The release formalizes **lab-play** as the first benchmark.
  - Lab-play is described as:
    - highly constrained
    - fixed resources
    - a single target entity
    - focused on throughput targets
  - Compared with **open-play**, which starts from a procedurally generated map and is much harder.
  - Evaluation details mentioned:
    - **16 per minute** for solid items
    - **250 per minute** for fluids
    - max **64 steps**
    - **early stopping** on completion
    - default **reasoning enabled** for supported models

- **Research results and claims**
  - The page claims **open-source models have caught up** to the state of the art seen in **v0.2.0 (May 2025)** on some tasks like:
    - electronic circuits
    - steel plate
    - sulfur
    - plastic automation
  - It also says the newest frontier models show **substantial improvement** over v0.2.0 and can now solve harder tasks with **dozens of ingredient dependencies**.
  - The authors argue FLE helps differentiate frontier models more sharply than many static benchmarks.
  - They compare performance ordering as roughly:
    - **Claude > GPT > Gemini > Grok**
  - They also say this ranking resembles **GDPVal** more than exam-style benchmarks like:
    - Humanity’s Last Exam
    - AIME 25
    - GPQA
    - MMMU

- **Failure modes and evaluation concerns**
  - A key critique is that many successful agents rely on **semi-manual strategies** instead of robust automation.
  - Common workaround:
    - using **storage chests as buffers**
    - shuttling resources manually
  - To reduce this “local optimum,” FLE enforces a **60-second holdout period** after the agent stops acting, then checks whether throughput targets are still met.
  - The authors argue higher throughput targets would make manual buffering less effective.
  - They note agents often fail to use the Python namespace to define reusable abstractions, with **Gemini 2.5 Pro** singled out as the only one doing this notably.
  - Frequent error categories:
    - **Syntactic errors**
    - **Semantic/API errors**
    - **Pragmatic errors**
    - **Planning and control errors**
  - Reported mean error rates for proprietary frontier models:
    - **Claude Opus 4.1: 22.99%**
    - **GPT-5: 25.05%**
    - **Gemini 2.5 Pro: 27.29%**
    - **Grok 4: 40.89%**
  - Model-specific observations:
    - Claude Opus 4.1: zero syntactic errors, mostly pragmatic errors
    - GPT-5 and Grok 4: more syntactic mistakes than expected
    - all but Claude show noticeable API misunderstandings

- **Broader interpretation**
  - The authors say frontier models are “shockingly bad” at playing Factorio, especially at:
    - modeling dynamic environments
    - maintaining consistent mental models
    - recovering from mistakes
  - They still report steady improvement during **2025**.
  - The page argues Factorio is a strong platform for studying:
    - long-horizon planning
    - spatial reasoning
    - system debugging
    - world modeling
    - constraint satisfaction under uncertainty

- **Future research agenda**
  - Human baseline measurement
  - Better handling of **reward hacking**
  - **METR-style task scaling**
  - Expansion to:
    - **open-play**
    - **megabases**
    - **real-time performance under latency constraints**
    - **multi-agent coordination**
    - **modded/out-of-distribution environments**
    - **native computer-use interfaces**
    - **adversarial dynamics and robustness**
  - The release closes as an open invitation for:
    - researchers
    - engineers
    - modders
    - Discord community members

### Assessment
This is a **mixed** release note / benchmark announcement / research summary with some tutorial-like setup commands and a lot of promotional framing. **Durability is medium**: the core ideas about long-horizon agent evaluation and Factorio as a benchmark are fairly stable, but the specific release version, model rankings, and reported error rates are version- and time-sensitive. **Content density is high** because it packs in setup commands, environment design, benchmark methodology, qualitative failure analysis, and quantitative model comparisons. It is **primary source** material from the FLE project team, though presented with a strong advocacy angle. This is best used as a **refer-back** reference if you care about the release’s features, evaluation setup, and headline findings; it is not just a skim-once announcement because the benchmark details and reported results are substantial. **Scrape quality is partial**: the text captured most of the page content, but the apparent figures/images, charts, and some formatting from the original webpage are missing, and several code blocks are flattened into plain text.
