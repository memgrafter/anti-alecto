---
url: https://www.youtube.com/watch?v=EV7WhVT270Q
title: 'State of AI in 2026: LLMs, Coding, Scaling Laws, China, Agents, GPUs, AGI | Lex Fridman Podcast #490 - YouTube'
scraped_at: '2026-04-19T08:13:39Z'
word_count: 52275
raw_file: raw/2026-04-19_state-of-ai-in-2026-llms-coding-scaling-laws-china-agents-gpus-agi-lex-fridman-p_ff816879.txt
tldr: Lex Fridman’s 2026 AI state-of-the-art episode with Sebastian Raschka and Nathan Lambert argues that AI progress is still real but increasingly driven by systems, post-training, tool use, and compute economics rather than radical architecture changes.
key_quote: “the idea space is very fluid but um culturally anthropic is known for betting very hard on code which is cloud code thing is working out for them right now”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Lex Fridman
- Sebastian Raschka
- Nathan Lambert
- Sam Altman
- Dario Amodei
- Mark Zuckerberg
- Jensen Huang
- Demis Hassabis
- Elon Musk
- Yan LeCun
tools:
- Claude Code
- Cursor
- Codex
- VS Code
- Perplexity
- OpenRouter
- Google Scholar
libraries:
- Hugging Face Transformers
- LoRA
- Gemma
- Llama
companies:
- Anthropic
- Google
- OpenAI
- DeepSeek
- Meta
- NVIDIA
- AI2
- Hugging Face
- xAI
- Mistral
- Microsoft
- Amazon
- Apple
- Allen Institute for AI
tags:
- large-language-models
- ai-research
- post-training
- tool-use
- open-weight-models
---

### TL;DR
Lex Fridman’s 2026 AI state-of-the-art episode with Sebastian Raschka and Nathan Lambert argues that AI progress is still real but increasingly driven by systems, post-training, tool use, and compute economics rather than radical architecture changes.

### Key Quote
“the idea space is very fluid but um culturally anthropic is known for betting very hard on code which is cloud code thing is working out for them right now”

### Summary
- **Format / premise**
  - Long-form podcast discussion on the state of AI in early 2026, focusing on LLMs, coding, scaling laws, China, agents, GPUs, AGI, open-weight models, and the business/research ecosystem.
  - Guests:
    - **Sebastian Raschka** — ML researcher, author of *Build a Large Language Model from Scratch* and *Build a Reasoning Model from Scratch*.
    - **Nathan Lambert** — post-training lead at AI2, author of a book on RLHF.

- **Main thesis**
  - The field is still progressing quickly, but the gains are increasingly coming from:
    - **post-training** (especially RLVR / reasoning training),
    - **tool use / agentic workflows**,
    - **systems improvements** (FP8/FP4, distributed training, better inference),
    - **data quality and data curation**,
    - rather than entirely new model architectures.
  - There is no obvious “winner” globally; the AI ecosystem looks more like a fast-moving arms race than a stable monopoly.

- **China vs. US / open-weight competition**
  - DeepSeek’s January 2025 R1 release is treated as a major inflection point that pushed open-weight competition in China.
  - Chinese open-weight model makers mentioned:
    - **DeepSeek**
    - **Kimi / Moonshot**
    - **Z.AI / GLM**
    - **MiniMax**
    - **Qwen**
    - **Ant**
    - **Ling?** (mentioned in passing)
  - Western/open efforts mentioned:
    - **AI2**
    - **Hugging Face / SmolLM**
    - **NVIDIA / Nemotron**
    - **Stanford Marin**
    - **LLM 360 / Institute for Foundation Models**
    - **Apparis** (Swiss consortium)
    - **OpenAI GPT-OSS**
    - **Gemma**
    - **Mistral**
  - Core point:
    - Chinese companies are incentivized to release open-weight models because many Western users won’t pay for Chinese APIs, but will use/download weights.
    - Open-weight models are a strategic influence play, not just a technical one.
    - Open models are often used locally, so the data usually doesn’t go to China.

- **What seems to be winning in practice**
  - **Anthropic** is seen as culturally strong on coding and relatively organized.
  - **Google/Gemini** is seen as increasingly strong, especially in consumer use and long-context.
  - **OpenAI** remains hard to bet against because it repeatedly lands major product/research steps.
  - The guests do **not** see a clear winner-take-all scenario.
  - They repeatedly emphasize that model access is no longer the main differentiator; **budget, hardware, execution culture, and distribution** matter more.

- **Model choice in practice**
  - Their own usage patterns illustrate that different models win on different tasks:
    - **ChatGPT / GPT-5.x** for quick factual queries, strong reasoning, and code/search.
    - **Gemini** for fast knowledge lookup and long-context tasks.
    - **Claude Opus 4.5** for coding and philosophical discussion, especially with extended thinking.
    - **Grok** for real-time info and some debugging / “AI Twitter” search.
  - They stress that people use models until they break, then switch.
  - Product interface matters almost as much as raw model quality.

- **Programming workflows**
  - Tools discussed:
    - **Claude Code**
    - **Cursor**
    - **Codex plugin for VS Code**
  - Differences:
    - **Claude Code** feels more agentic and “warm,” better for macro-level guidance and building from scratch.
    - **Cursor/Codex** are more inspectable and control-oriented.
  - A recurring theme:
    - AI coding is becoming more like working with a “pair programmer” or “project manager.”
    - A major tension is between convenience and losing the joy/skill-building of debugging and coding yourself.

- **Why the architectures still look similar**
  - Despite huge visible progress, they argue that the core transformer lineage hasn’t changed that much since **GPT-2 / “Attention Is All You Need.”**
  - Common architectural components discussed:
    - **Mixture of Experts (MoE)**
    - **Group Query Attention**
    - **Multi-Head Latent Attention**
    - **Sliding Window Attention**
    - **RMSNorm**
    - **Sparse / dense mixtures**
    - **Gated DeltaNet-like / state-space-inspired tweaks**
  - The big gains are mostly from:
    - data,
    - training stages,
    - scaling tricks,
    - systems engineering,
    - and post-training algorithms.

- **Pre-training / mid-training / post-training**
  - **Pre-training**:
    - Classic next-token prediction on large corpora.
    - Data now includes more synthetic and cleaned data, not just raw web text.
    - Still important, but increasingly expensive.
  - **Mid-training**:
    - A transitional phase focused on specialized capabilities like long context or reasoning-oriented data.
    - Helps avoid catastrophic forgetting while reshaping the model for later post-training.
  - **Post-training**:
    - Fine-tuning, supervised fine-tuning, DPO, RLHF, and especially **RLVR**.
    - The major unlock in 2025 was **reinforcement learning with verifiable rewards**.
    - This is where models learn to do tool use, multi-step reasoning, code execution, and search.

- **RLVR / reasoning models**
  - RLVR = reinforcement learning with **verifiable rewards**.
  - The model generates completions, then gets rewarded for correctness on tasks where correctness can be checked:
    - math,
    - coding,
    - structured constraints,
    - some factual tasks.
  - Key observation:
    - RLVR can unlock abilities already latent in the model, especially if pretraining data or reasoning traces are good.
    - It can produce “aha” moments and self-correction behaviors.
  - Important caveat:
    - There is serious **benchmark contamination** concern, especially in math benchmarks and with some Qwen/DeepSeek-style results.
    - Some of the apparent gains may reflect memorized or near-duplicate training data.
  - Still, the guests think RLVR is a real and important scaling path, unlike older RHF/RLHF, which tends to saturate into style/preference tuning.

- **Scaling laws**
  - They distinguish three kinds of scaling:
    - **Pre-training scaling**
    - **RL / post-training scaling**
    - **Inference-time scaling** (letting the model think longer)
  - Their view:
    - Scaling laws still hold broadly.
    - The low-hanging fruit in pretraining is more limited now because it’s expensive and serving huge models is costly.
    - The most visible recent gains came from inference-time reasoning and RLVR.
  - But:
    - pretraining is not “dead.”
    - The best organizations still want stronger base models.
    - Bigger compute clusters in 2026 should keep pushing progress.

- **Compute economics**
  - A repeated point:
    - training cost is large,
    - but **serving/inference cost at scale can dominate**.
  - They discuss:
    - GPU scarcity,
    - TPUs vs Nvidia,
    - FP8/FP4,
    - tokens/sec/GPU,
    - Blackwell / gigawatt-scale data centers,
    - massive training failures at 10k–100k GPU scales.
  - Another theme:
    - small model / open-weight ecosystems matter partly because they reduce cost and can be deployed locally.
    - OpenAI and other big labs may release smaller or more efficient models partly to save on inference cost.

- **Tool use and agents**
  - GPT-OSS is highlighted as a model designed with **tool use** in mind.
  - Tool use is described as:
    - web search,
    - Python execution,
    - calculator access,
    - CLI / shell commands,
    - repository-aware coding.
  - Why it matters:
    - It reduces hallucinations by offloading exact operations to tools.
    - It enables agents to do real work instead of just generating text.
  - But:
    - trust and security are major blockers,
    - open models are harder to integrate seamlessly with tools than closed systems,
    - fully autonomous computer use is still brittle.

- **Long context**
  - Context length is still increasing, but they think the more important trend is not just bigger windows:
    - better compaction,
    - selective attention,
    - recursive language modeling,
    - sparse attention,
    - agent-managed memory.
  - Claude’s “compaction” behavior is mentioned as a practical example.
  - They expect context windows to keep growing, but not infinitely; better memory management will matter more.

- **Continual learning and memory**
  - **Continual learning** = updating model weights over time based on new feedback.
  - **In-context learning** = stuffing extra information into the prompt/context without changing weights.
  - Their view:
    - both are useful,
    - but continual learning at personal-user level is likely too expensive.
    - More likely near-term: strong memory systems and rich context.
  - They discuss LoRA / adapter-style fine-tuning as a partial workaround.

- **Data quality, synthetic data, and licensing**
  - Data quality is framed as one of the most important hidden levers in current AI progress.
  - Topics mentioned:
    - OCR extraction from PDFs,
    - data curation,
    - Common Crawl filtering,
    - Reddit, Stack Exchange, Wikipedia, GitHub as different sources,
    - synthetic data as rephrasing / summarization / structured transformation, not just “fake data.”
  - Legal/licensing issues:
    - training on pirated books vs purchased books,
    - licensed-only data,
    - the Anthropic lawsuit and the reported **$1.5B** settlement judgment context,
    - importance of compensation frameworks akin to Spotify for creators.
  - They argue that data provenance and licensing will keep shaping model strategy.

- **Education / how to learn AI**
  - Strong recommendation:
    - build a small LLM from scratch on one GPU.
  - Why:
    - you learn what actually goes into the model,
    - you can verify outputs,
    - it gives an intuitive understanding of pretraining, attention, and fine-tuning.
  - They explicitly recommend:
    - start small,
    - reverse engineer a reference implementation,
    - use config files and weights to match behavior,
    - then read targeted papers.
  - They caution against diving straight into big libraries like Hugging Face Transformers if the goal is conceptual understanding, because the codebase is too complex.

- **Open-source / open-weight politics**
  - A major portion of the episode is about the importance of **American open models**.
  - Nathan Lambert’s **ATOM project** is described as a US initiative for genuinely open-weight models and infrastructure.
  - He argues:
    - open models are important for research, education, talent development, and ecosystem control.
    - if the US doesn’t invest, Chinese open models will dominate mindshare and deployment.
  - The White House AI Action Plan is mentioned as supportive of open source/open weight models.
  - They see open models as the only realistic path for broad education and for future researchers to learn and contribute.

- **LLama / Meta**
  - Llama is described as the pioneering open-weight Western model family.
  - They think Meta’s later Llama strategy became distorted by benchmark-maxing and internal politics.
  - The original promise of Llama was:
    - usable,
    - modifiable,
    - trusted,
    - not necessarily the absolute benchmark leader.
  - The guests are uncertain whether Llama will continue as a major open-weight force.

- **Agents, coding, and the near future**
  - They think the next obvious improvements are:
    - more capable coding assistants,
    - more useful project-level code generation,
    - better debugging,
    - better docs, figures, and explanations,
    - more reliable computer use.
  - They are bullish on AI making software development much faster, but not necessarily fully autonomous yet.
  - A likely near-term role for developers:
    - more design/specification/product management,
    - less manual line-by-line coding.

- **AGI / ASI timelines**
  - They reject crisp AGI/ASI thresholds as overly fuzzy.
  - Better framing:
    - can AI replace most digital remote work?
    - can it become a superhuman coder?
    - can it automate AI research?
  - Their view:
    - superhuman coding may come sooner than people think,
    - full AI research automation is farther out and messier,
    - “jagged” capability is the right mental model.
  - AI 2027-style forecasts are useful as scenario exercises, but not gospel.

- **Robotics and world models**
  - They briefly pivot to robotics and world models.
  - Main points:
    - robotics is getting supercharged by LLM tooling and infrastructure,
    - but embodied systems are much harder than chat or coding,
    - in-home consumer robots are far less likely near-term than industrial or logistics automation,
    - safety is a huge unresolved issue.
  - World models are discussed as a promising area for richer simulation and planning.

- **Societal / human impact**
  - They repeatedly stress that:
    - AI can be good and transformative,
    - but it also risks burnout, social harm, slop, misinformation, and over-automation.
  - Concerns discussed:
    - mental health impacts,
    - over-reliance,
    - job loss and human suffering,
    - ads and monetization,
    - the need for agency and human connection.
  - They argue the antidote is:
    - use AI actively,
    - build with it,
    - maintain agency,
    - keep real-world human skills and relationships.

- **Bubbles, hype, and Silicon Valley**
  - Silicon Valley is described as a powerful bubble/echo chamber.
  - That bubble can be productive — a “reality distortion field” that accelerates buildout.
  - But it can also cause overconfidence and blind spots.
  - They urge readers to stay connected to the broader world: history, literature, different geographies, and non-tech perspectives.

- **Business / consolidation**
  - They expect continued consolidation:
    - acquisitions,
    - licensing deals,
    - huge funding rounds,
    - possible IPOs from some Chinese and maybe US players.
  - They discuss:
    - Grok / xAI,
    - Scale AI,
    - Cursor,
    - Anthropic,
    - OpenAI,
    - possible future public listings.
  - But they do not see a winner-take-all market yet.

- **Final stance**
  - The episode is broadly optimistic about AI’s technical progress and societal upside, but cautious about:
    - safety,
    - labor disruption,
    - hype,
    - cultural narrowing,
    - and the limits of current systems.
  - The speakers think the next few years will be defined less by a giant architecture breakthrough and more by compounding gains in:
    - data,
    - post-training,
    - tool use,
    - systems,
    - and model/product integration.

### Assessment
Durability: **medium** — The conceptual discussion of transformers, post-training, tool use, RLVR, and AI education will stay relevant, but many concrete model references, pricing guesses, and 2025/2026 company dynamics will age quickly. Content type: **mixed** — part interview, part technical explainer, part industry analysis, part opinionated forecasting. Density: **high** — it is packed with specific model names, training methods, benchmarks, products, and market judgments, though the transcript is conversational and repetitive in places. Originality: **commentary** — this is an informed discussion synthesizing current AI developments rather than a primary research paper. Reference style: **refer-back** — useful for revisiting the model landscape, scaling-law arguments, and terminology like RLVR, mid-training, and tool use. Scrape quality: **partial** — the transcript captured a large amount of the conversation, but it is clearly noisy/transcribed, with repetition, garbled names, and no visual context, slides, or full formatting.
