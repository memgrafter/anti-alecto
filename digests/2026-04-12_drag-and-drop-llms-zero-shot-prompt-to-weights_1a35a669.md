---
url: https://arxiv.org/html/2506.16406
title: 'Drag-and-Drop LLMs: Zero-Shot Prompt-to-Weights'
scraped_at: '2026-04-12T07:21:52Z'
word_count: 8892
raw_file: raw/2026-04-12_drag-and-drop-llms-zero-shot-prompt-to-weights_1a35a669.txt
tldr: DnD (Drag-and-Drop LLMs) is a zero-shot prompt-to-weights method that generates task-specific LoRA adapters directly from unlabeled prompts, avoiding per-task fine-tuning while improving performance on unseen reasoning, coding, math, and multimodal benchmarks.
key_quote: “Can we utilize parameter generation to effectively ‘drag-and-drop’ LLMs’ weights towards configurations better suited for a given novel task?”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: partial
people:
- Josh Achiam
- Steven Adler
- Sandhini Agarwal
- Lama Ahmad
- Ilge Akkaya
- Florencia Leoni Aleman
- Diogo Almeida
- Janko Altenschmidt
- Sam Altman
- Shyamal Anadkat
- Aaron Grattafiori
- Abhimanyu Dubey
- Abhinav Jauhri
- Abhinav Pandey
- Abhishek Kadian
- Ahmad Al-Dahle
- Aiesha Letman
- Akhil Mathur
- Alan Schelten
- Alex Vaughan
- An Yang
- Baosong Yang
- Beichen Zhang
- Binyuan Hui
- Bo Zheng
- Bowen Yu
- Chengyuan Li
- Dayiheng Liu
- Fei Huang
- Haoran Wei
- Edward J Hu
- Phillip Wallis
- Zeyuan Allen-Zhu
- Yuanzhi Li
- Weizhu Chen
- Kai Wang
- Dongwen Tang
- Yang You
- Nils Reimers
- Iryna Gurevych
- Jacob Devlin
- Ming-Wei Chang
- Kenton Lee
- Kristina Toutanova
tools:
- A100
- AdamW
- ARC-e
- ARC-c
- BoolQ
- OBQA
- HellaSwag
- PIQA
- WinoGrande
- HumanEval
- LiveCodeBench
- gsm8K
- MATH
- Math-Vision
- Math-Vista
libraries:
- LoRA
- PEFT
- Sentence-BERT
- SentenceBERT
- Qwen2.5
- Qwen2.5-VL
- T5
- GloVe
- BERT
companies:
- Qwen
- OpenAI
- DeepSeek
- Llama
- AI2
tags:
- large-language-models
- parameter-efficient-fine-tuning
- lora
- parameter-generation
- zero-shot-learning
---

### TL;DR
DnD (Drag-and-Drop LLMs) is a zero-shot prompt-to-weights method that generates task-specific LoRA adapters directly from unlabeled prompts, avoiding per-task fine-tuning while improving performance on unseen reasoning, coding, math, and multimodal benchmarks.

### Key Quote
“Can we utilize parameter generation to effectively ‘drag-and-drop’ LLMs’ weights towards configurations better suited for a given novel task?”

### Summary
- **Core idea**
  - Reframes LoRA adaptation as a **prompt-conditioned weight generation** problem instead of gradient-based training.
  - Takes a **batch of unlabeled task prompts**, encodes them with a lightweight text encoder, and feeds them into a **hyper-convolutional decoder** that outputs the full LoRA weight updates.
  - Goal: eliminate **per-task optimization** for new datasets.

- **Why this matters**
  - Traditional PEFT/LoRA still requires a separate training run for every new task.
  - The paper argues that if a model can learn the mapping from **prompts → adapter weights**, it can specialize in **seconds** rather than hours/days.

- **Method details**
  - **Training data**: pairs of prompt batches and corresponding LoRA checkpoints collected from multiple datasets.
  - **Prompt embeddings**: default encoder is **Sentence-BERT (all-MiniLM-L6-v2)**.
  - **Generator**: a cascaded **hyper-convolutional decoder**.
  - **Objective**: minimize **MSE** between generated weights and tokenized checkpoint weights.
  - **Inference**: sample prompts from a new dataset, embed them, generate LoRA weights in one forward pass, then evaluate the resulting adapted model.
  - The paper emphasizes **prompt-checkpoint pairing** as the key mechanism for learning dataset-to-parameter correlations.

- **Benchmarks and settings**
  - Backbones: **Qwen2.5** family.
  - Tasks:
    - **Common sense reasoning**: Qwen2.5-0.5B; datasets include ARC-e, ARC-c, BoolQ, OBQA, HellaSwag, PIQA, WinoGrande.
    - **Coding**: Qwen2.5-1.5B and 7B; evaluated on **HumanEval** and **LiveCodeBench**.
    - **Math**: Qwen2.5-1.5B and 7B; evaluated on **gsm8K** and **MATH**.
    - **Multimodal**: Qwen2.5-VL-3B; evaluated on **Math-Vision** and **Math-Vista**.
  - Default prompt batch sizes vary by task (e.g. **128** for common sense, **64/32** for others).

- **Main reported results**
  - Claims **up to 12,000× lower overhead** than full fine-tuning.
  - Reports **up to 30% performance gains** over the strongest training LoRAs on unseen datasets.
  - Examples from the tables:
    - Common sense average accuracy improvement over training LoRAs: **21.0** points.
    - Cross-domain science test: **45.3 vs 35.6** average accuracy.
    - Coding/HumanEval: DnD improves pass@1 from **17.6 to 32.7** on average.
    - Math/gsm8K: **66.3 vs 42.9** average accuracy.
    - Multimodal: DnD also improves over training LoRAs, though gains are smaller on some multimodal metrics.
  - The method is reported to transfer from **0.5B to 7B** backbones.

- **Ablations and findings**
  - **Prompt-only conditioning** works better than prompt+answer on common sense tasks; answers can hurt when they are too repetitive or low-diversity.
  - **Sentence-BERT** is the default and performs well; **GloVe** and **T5** also work reasonably; **Qwen2.5-7B** as conditioner performed poorly/fail in this setup.
  - More and more diverse training datasets improve performance; DnD struggles when training data is too sparse.
  - For math, **answers can help** when they are diverse and complex, but the authors still recommend **prompts** because they are shorter and more practical.
  - A better pairing strategy is to randomly sample from a pool of conditions each iteration rather than fixed one-condition-per-parameter pairing.
  - Compared with **RPG** (a prior parameter generation method), DnD generalizes better to **open-set / unseen datasets**.

- **Efficiency and scalability**
  - Reported generation time on one A100 80G GPU is very small:
    - Common sense: **0.11 s**
    - Math: **0.53 s (1.5B)** / **0.73 s (7B)**
    - Coding: **0.70 s (1.5B)** / **0.73 s (7B)**
    - Multimodal: **0.61 s**
  - Memory usage ranges from about **9.59 GB** to **20.48 GB** depending on task and model size.
  - The paper claims DnD can outperform:
    - training LoRAs,
    - few-shot tuning,
    - in-context learning,
    - and in some cases even **full-shot tuning** when compared against lightly tuned checkpoints.

- **Broader claim / takeaway**
  - The paper argues that **neural network weights can be treated as a data modality**.
  - DnD is presented as evidence that **gradient descent is not strictly necessary** for effective task adaptation if the model can learn a good prompt-to-weight map.

- **Limitations and future directions mentioned by the authors**
  - Scaling parameter generation to much larger models (**7B–70B**) likely needs new architecture/algorithm ideas.
  - Reusing existing pretrained checkpoints from the internet could improve practicality.
  - Generating structurally diverse models for different hardware settings is an open challenge.

### Assessment
This is a **research** paper with high information density and strong specificity, so it is useful as a **deep-study** reference rather than a skim-only piece. Its durability is **medium**: the conceptual contribution around prompt-conditioned parameter generation is potentially long-lived, but the concrete results are tied to specific models, datasets, and the 2024–2025 PEFT/LLM landscape. The originality is primarily **primary source** research, not a synthesis. Scrape quality is **partial**: the main narrative, tables, appendix details, and many results are present, but several equations are rendered incompletely/missing symbols, and some tables/formatting are partially broken.
