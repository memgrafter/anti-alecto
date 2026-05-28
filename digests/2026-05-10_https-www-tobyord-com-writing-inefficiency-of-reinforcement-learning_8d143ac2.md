---
url: https://www.tobyord.com/writing/inefficiency-of-reinforcement-learning
title: https://www.tobyord.com/writing/inefficiency-of-reinforcement-learning
scraped_at: '2026-05-10T04:31:10Z'
word_count: 2660
raw_file: raw/2026-05-10_https-www-tobyord-com-writing-inefficiency-of-reinforcement-learning_8d143ac2.txt
tldr: Toby Ord argues that frontier-model RL training is vastly less information-efficient than pre-training—potentially by 1,000,000x on long-horizon tasks—so the new AI scaling era may produce narrower gains, less generality, and slower real progress than the pre-training boom.
key_quote: “the new scaling paradigm for AI reduces the amount of information a model can learn from per hour of training by a factor of 1,000 to 1,000,000.”
durability: high
content_type: opinion
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Toby Ord
- Dario Amodei
- Steve Newman
- DeepMind
- OpenAI
tools:
- GPT-1
- GPT-3
- GPT-4
- GPT-4.5
- o1
- o3
- GPT-5
- DeepSeek-R1
- METR
libraries: []
companies:
- Anthropic
- OpenAI
- DeepMind
- METR
- DeepSeek
tags:
- reinforcement-learning
- ai-scaling
- llm-training
- information-theory
- model-generalization
---

### TL;DR
Toby Ord argues that frontier-model RL training is vastly less information-efficient than pre-training—potentially by 1,000,000x on long-horizon tasks—so the new AI scaling era may produce narrower gains, less generality, and slower real progress than the pre-training boom.

### Key Quote
“the new scaling paradigm for AI reduces the amount of information a model can learn from per hour of training by a factor of 1,000 to 1,000,000.”

### Summary
- **Article type:** opinion/analysis essay with quantitative back-of-the-envelope estimates about AI training efficiency.
- **Main thesis:** the industry’s shift from scaling **pre-training** to scaling **reinforcement learning (RL)** and **inference compute** changes the economics of AI progress in a profound way, because RL on long tasks conveys far less information per unit of compute than next-token prediction.
- **Core comparison: pre-training vs RL**
  - Pre-training (next-token prediction) gives roughly one token of target information per token generated during training.
  - Ord argues the upper bound is about **16 bits per token** early on, and more like **~3 bits per token** later in training, based on token vocab sizes and GPT-4 scale sanity checks.
  - RL on machine-checkable tasks often requires **thousands to millions of tokens** before revealing a **single bit** of success/failure information.
- **Numbers and examples used**
  - GPT-3 has about **50,000 tokens** in its vocabulary; GPT-4 about **100,000**, implying ~16 bits to identify a token in the abstract.
  - GPT-4 is estimated at about **10^12 parameters** (~3 × 10^13 bits) trained on about **10^13 tokens**, which Ord says implies roughly **3 bits of model capacity per token** of training data.
  - DeepSeek-R1 reasoning chains are cited at up to **32,000 tokens**, with early AIME-solving episodes around **12,000 tokens** and a May 2025 release around **23,000 tokens** per task.
  - For frontier RL tasks like METR’s HCAST, models reportedly used about **16 million tokens total** per task, with o3 reaching about **50% success** on tasks that take humans **~1.5 hours**.
  - Ord’s rough conclusion: at the frontier, RL may deliver **less than 1 bit per 10,000 tokens**, and in some settings **less than 1 bit per million output tokens**.
- **Implication for compute efficiency**
  - On current margins, RL may provide around a **millionth as much information per FLOP** as pre-training.
  - This gap likely gets worse as tasks become longer and more agentic, because the reward signal becomes more delayed and sparse.
- **Caveats Ord emphasizes**
  - These are **upper bounds** on information that could be learned, not guarantees about actual learning.
  - RL can sometimes be improved by **intermediate rewards** or richer feedback, including more than binary success/failure.
  - The value of information depends on the task: some bits are more useful than others.
- **Why RL can still look impressive**
  - RL is good at producing **deep competence in narrow domains** and can push models beyond human performance on selected benchmarks.
  - Historical examples: **Atari** and **Go** agents achieved superhuman performance but did not transfer broadly; DeepMind found RL on one game often harmed learning another.
- **Why breadth may suffer**
  - Pre-training exposed models to enormous variety across the internet, producing broad, often surprising general capabilities.
  - RL training is more targeted, so Ord expects less “hidden” cross-domain capability and fewer emergent abilities outside the training target.
  - He argues future gains may be more benchmark-specific, with less generalization across untrained areas.
- **Bottom line**
  - Ord sees the AI field entering a new era where progress can still be real, but it may be **narrower, more expensive, and less broadly transformative** than pre-training-era scaling suggested.
  - He frames this as an “important juncture” where old intuitions about AI scaling may stop holding.

### Assessment
This is a high-durability conceptual essay with a mixed content type: it is an opinionated, quantitative analysis rather than a pure tutorial or reference. It is fairly dense, with many concrete numbers, examples, and compute/information-theoretic estimates, but it is still partly speculative because it extrapolates from incomplete public data on frontier RL training. The piece is original commentary/synthesis by Toby Ord, not a primary empirical study, though it cites model behavior and external research like METR and DeepSeek as supporting evidence. It’s best used as a refer-back piece for arguments about RL inefficiency, the pre-training-to-RL transition, and why frontier AI progress may become less general. Scrape quality is partial-to-good: the main article text is present, but the page also includes obvious website/editorial boilerplate (“Contact Us,” form placeholders, navigation chrome), and no figures or images are fully captured beyond inline mentions like “View fullsize.”
