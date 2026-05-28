---
url: https://x.com/YizheZhangNLP/status/2041590447106355323
title: 'Yizhe Zhang on X: "1/6 The "Self-Improvement" Paradox Can an LLM get smarter using only its own raw, unverified outputs? No verifiers. No teachers. No RL. We found the answer is an emphatic YES. Introducing SimpleSD: Embarrassingly Simple Self-Distillation. By simply sampling solutions from a https://t.co/1NUf1gbWut" / X'
scraped_at: '2026-04-19T07:30:58Z'
word_count: 134
raw_file: raw/2026-04-19_yizhe-zhang-on-x-1-6-the-self-improvement-paradox-can-an-llm-get-smarter-using-o_48b93f0a.txt
tldr: Yizhe Zhang announces SimpleSD, a self-distillation method where an LLM is fine-tuned on its own sampled outputs—without verifiers, teachers, or RL—and reports large gains on LiveCodeBench v6 across multiple model sizes and families.
key_quote: Can an LLM get smarter using only its own raw, unverified outputs? No verifiers. No teachers. No RL. We found the answer is an emphatic YES.
durability: high
content_type: announcement
density: high
originality: primary
reference_style: skim-once
scrape_quality: partial
people:
- Yizhe Zhang
- Navdeep Jaitly
tools:
- X
- GitHub
- Hugging Face
libraries: []
companies:
- Apple
tags:
- self-distillation
- large-language-models
- machine-learning
- code-generation
- model-training
---

### TL;DR
Yizhe Zhang announces **SimpleSD**, a self-distillation method where an LLM is fine-tuned on its **own sampled outputs**—without verifiers, teachers, or RL—and reports large gains on **LiveCodeBench v6** across multiple model sizes and families.

### Key Quote
“**Can an LLM get smarter using only its own raw, unverified outputs? No verifiers. No teachers. No RL. We found the answer is an emphatic YES.**”

### Summary
- This is an **X thread announcement** introducing a paper and code release for **SimpleSD: Embarrassingly Simple Self-Distillation**.
- Core idea:
  - Sample solutions from a model using **specific temperature and truncation settings**.
  - Fine-tune the same model on those exact sampled solutions.
  - No external verifier, no human teacher, and no reinforcement learning are used.
- Reported result:
  - **Qwen3-30B** improved from **42.4% to 55.3%** on **LiveCodeBench v6**.
  - The author describes this as roughly a **30% improvement**.
- Claimed generality:
  - Gains are said to be **universal across model sizes**: **4B, 8B, 30B**.
  - Gains are also said to hold across **model families**: **Llama** and **Qwen**.
  - The thread claims the method helps more on **harder problems**, with larger gains as difficulty increases.
- Attribution and links:
  - The post credits colleagues including **Navdeep Jaitly**.
  - It points to:
    - the **paper** on arXiv: **arxiv.org/abs/2604.01193**
    - the **code**: **github.com/apple/ml-ssd**
    - **Hugging Face models**: **huggingface.co/collections/ap...**
- Overall framing:
  - The thread is positioned as a proof that **self-generated training data alone** can improve an LLM, challenging the intuition that model outputs are too noisy to teach the model itself.

### Assessment
This is a **mixed announcement/research snippet** with **high durability** in the sense that the general self-distillation idea may remain relevant, though the specific benchmark and model results are tied to current model versions and could age quickly. The content is **high-density** but very short, giving a compact set of claims rather than detailed methods or evidence. It is best treated as a **primary-source announcement** pointing to a paper and code rather than a full technical explanation. Use it as a **skim-once / refer-back** reference if you want the headline result, but you’d need the paper for serious evaluation. **Scrape quality is partial**: the thread capture only includes the first post and metadata, not the full 6-post conversation or any image contents, so important context may be missing.
