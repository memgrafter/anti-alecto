---
url: https://arxiv.org/abs/2510.04950
title: '[2510.04950] Mind Your Tone: Investigating How Prompt Politeness Affects LLM Accuracy (short paper)'
scraped_at: '2026-04-19T07:36:55Z'
word_count: 362
raw_file: raw/2026-04-19_2510-04950-mind-your-tone-investigating-how-prompt-politeness-affects-llm-accura_fae8e06c.txt
tldr: This short arXiv paper reports that, on 50 multiple-choice questions rewritten into five tone levels, ruder prompts produced slightly higher ChatGPT 4o accuracy than polite ones, with results ranging from 80.8% for “Very Polite” to 84.8% for “Very Rude.”
key_quote: “Contrary to expectations, impolite prompts consistently outperformed polite ones, with accuracy ranging from 80.8% for Very Polite prompts to 84.8% for Very Rude prompts.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- ChatGPT 4o
libraries: []
companies: []
tags:
- prompt-engineering
- llm-evaluation
- human-ai-interaction
- natural-language-processing
---

### TL;DR
This short arXiv paper reports that, on 50 multiple-choice questions rewritten into five tone levels, **ruder prompts produced slightly higher ChatGPT 4o accuracy than polite ones**, with results ranging from 80.8% for “Very Polite” to 84.8% for “Very Rude.”

### Key Quote
“Contrary to expectations, impolite prompts consistently outperformed polite ones, with accuracy ranging from 80.8% for Very Polite prompts to 84.8% for Very Rude prompts.”

### Summary
- **Topic:** How **prompt politeness / tone** affects **LLM accuracy** on multiple-choice questions.
- **Research question:** Whether changing the tone of a prompt from polite to rude changes model performance.
- **Dataset construction:**
  - Built **50 base questions** spanning **mathematics, science, and history**
  - Rewrote each question into **five tone variants**:
    - Very Polite
    - Polite
    - Neutral
    - Rude
    - Very Rude
  - Total of **250 unique prompts**
- **Model evaluated:** **ChatGPT 4o**
- **Method:**
  - Compared accuracy across tone conditions
  - Used **paired sample t-tests** to assess statistical significance
- **Main finding:**
  - **Impolite prompts outperformed polite ones**
  - Accuracy ranged from:
    - **80.8%** for **Very Polite**
    - up to **84.8%** for **Very Rude**
- **Interpretation offered by the authors:**
  - The result conflicts with earlier studies that found rudeness harmed performance
  - Suggests **newer LLMs may respond differently to tonal variation**
  - Raises broader questions about the **social/pragmatic dimensions of human-AI interaction**
- **Scope/limitations visible from the abstract:**
  - This is a **short paper**
  - Only **one model** is mentioned (**ChatGPT 4o**)
  - Only **50 base questions** were used, so the study is relatively small
  - The abstract does not provide effect sizes, p-values, or details on prompt wording beyond tone categories

### Assessment
This is a **research** paper with **medium durability**: the underlying question about prompt pragmatics is likely to remain interesting, but the specific numbers and the conclusion may age as models change. The content is **high-density** for an abstract, with concrete counts, categories, and accuracy figures, and it is **primary source** work rather than synthesis or commentary. It is best used as a **refer-back** reference if you’re tracking prompt engineering or human-AI interaction studies. **Scrape quality is partial**: the abstract and bibliographic metadata are present, but the full paper, tables, statistical details, and any figures/code/data are not included here.
