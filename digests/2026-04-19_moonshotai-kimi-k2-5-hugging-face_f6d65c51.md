---
url: https://huggingface.co/moonshotai/Kimi-K2.5
title: moonshotai/Kimi-K2.5 · Hugging Face
scraped_at: '2026-04-19T03:55:20Z'
word_count: 3436
raw_file: raw/2026-04-19_moonshotai-kimi-k2-5-hugging-face_f6d65c51.txt
tldr: Moonshot AI’s Kimi-K2.5 is a 1T-parameter open-source multimodal agentic model with 32B activated parameters, 256K context, strong benchmark results, and official API/deployment guidance plus chat/video/tool-use examples.
key_quote: Kimi K2.5 is an open-source, native multimodal agentic model built through continual pretraining on approximately 15 trillion mixed visual and text tokens atop Kimi-K2-Base.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Kimi Team
- Tongtong Bai
- Yifan Bai
- Yiping Bao
tools:
- vLLM
- SGLang
- KTransformers
- Kimi Code CLI
libraries:
- transformers
companies:
- Moonshot AI
- Hugging Face
- OpenAI
- Anthropic
tags:
- multimodal-models
- agentic-ai
- model-deployment
- benchmark-evaluation
- machine-learning-model-cards
---

### TL;DR
Moonshot AI’s Kimi-K2.5 is a 1T-parameter open-source multimodal agentic model with 32B activated parameters, 256K context, strong benchmark results, and official API/deployment guidance plus chat/video/tool-use examples.

### Key Quote
“**Kimi K2.5 is an open-source, native multimodal agentic model built through continual pretraining on approximately 15 trillion mixed visual and text tokens atop Kimi-K2-Base.**”

### Summary
- **What it is**
  - Kimi-K2.5 is Moonshot AI’s open-source model card on Hugging Face for a **native multimodal agentic model**.
  - It is trained via continual pretraining on **~15 trillion mixed visual and text tokens** on top of **Kimi-K2-Base**.
  - It supports both **instant** and **thinking** modes, plus conversational and agentic workflows.

- **Key features**
  - **Native multimodality**: vision-language pretraining for visual knowledge, cross-modal reasoning, and tool use grounded in visual inputs.
  - **Coding with vision**: can generate code from UI designs and video workflows.
  - **Agent Swarm**: can decompose tasks into parallel sub-tasks with dynamically instantiated domain-specific agents.

- **Model summary / architecture**
  - **Architecture**: Mixture-of-Experts (MoE)
  - **Total parameters**: **1T**
  - **Activated parameters**: **32B**
  - **Layers**: 61 total, 1 dense layer
  - **Attention hidden dimension**: 7168
  - **MoE hidden dimension per expert**: 2048
  - **Attention heads**: 64
  - **Experts**: 384, with **8 selected per token**
  - **Shared experts**: 1
  - **Vocabulary size**: 160K
  - **Context length**: **256K**
  - **Attention mechanism**: MLA
  - **Activation**: SwiGLU
  - **Vision encoder**: MoonViT with **400M** parameters

- **Changelog**
  - **2026-01-29** update:
    - Removed the default system prompt because it could confuse users and cause unexpected behavior.
    - Fixed a chat-template token from `<|media_start|>` to `<|media_begin|>`.

- **Evaluation highlights**
  - The card includes a large benchmark table comparing Kimi K2.5 against **GPT-5.2**, **Claude 4.5 Opus**, **Gemini 3 Pro**, **DeepSeek V3.2**, and **Qwen3-VL-235B-A22B**.
  - Reported strengths include:
    - Strong reasoning/knowledge scores on **AIME 2025**, **HMMT 2025**, **GPQA-Diamond**, and **MMLU-Pro**
    - Strong image/video results on **MMMU-Pro**, **OCRBench**, **InfoVQA**, **VideoMMMU**, **VideoMME**, and **LongVideoBench**
    - Strong coding and agentic search results, including **SWE-Bench Verified**, **SWE-Bench Pro**, **LiveCodeBench**, **BrowseComp**, **WideSearch**, and **DeepSearchQA**
  - Kimi K2.5 also reports **Agent Swarm** variants for some search benchmarks, with higher scores than the non-swarm setup.
  - Many benchmark notes specify testing conditions, such as:
    - temperature = **1.0**
    - top-p = **0.95**
    - context length = **256k**
    - averaged over multiple runs for some benchmarks
    - some results re-evaluated under consistent conditions and marked with `*`

- **Quantization**
  - It uses the same **native INT4 quantization** approach as **Kimi-K2-Thinking**.

- **Deployment**
  - Official API is available at **platform.moonshot.ai**.
  - The service offers **OpenAI/Anthropic-compatible APIs**.
  - Recommended inference engines:
    - **vLLM**
    - **SGLang**
    - **KTransformers**
  - Minimum `transformers` version: **4.57.1**
  - Deployment examples are in the linked **Model Deployment Guide**.

- **Usage examples**
  - Shows Python examples using the OpenAI client for:
    - **chat completion**
    - **image input**
    - **video input**
  - The examples demonstrate:
    - how to request **thinking mode** responses
    - how to disable thinking for **instant mode**
    - how to pass image/video data as base64 data URLs
  - Notes:
    - Video chat is experimental and currently only supported in the official API.
    - Recommended `temperature`:
      - **1.0** for Thinking mode
      - **0.6** for Instant mode
    - Recommended `top_p`: **0.95**
    - For instant mode in third-party deployments, pass `{'chat_template_kwargs': {"thinking": False}}` in `extra_body`

- **Agent/tool use**
  - K2.5 supports **interleaved thinking and multi-step tool calls**, same design as **K2 Thinking**.
  - The card points users to K2 Thinking documentation for full examples.
  - It says Kimi K2.5 works best with **Kimi Code CLI** as its agent framework.

- **License and notices**
  - Both the code repository and model weights are under a **Modified MIT License**.
  - Third-party notices are linked separately.

- **Citation**
  - Includes a full BibTeX citation for the **Kimi K2.5 technical report**:
    - Title: **Kimi K2.5: Visual Agentic Intelligence**
    - Year: **2026**
    - arXiv: **2602.02276**

- **Other metadata**
  - **Downloads last month**: **5,273,881**
  - Tagged as **Safetensors**
  - Hugging Face page also links to:
    - model tree
    - spaces using the model
    - collection including the model
    - paper

### Assessment
This is a high-density, mostly primary-source model card/reference page with strong durability for the architecture, usage, and licensing details, but medium staleness for benchmark rankings and deployment advice because those depend on evolving models, APIs, and library versions. Content type is mixed: reference, tutorial, and announcement-style documentation. It is best used as a **refer-back** resource rather than a one-time skim, since it contains concrete commands, parameters, benchmark numbers, and caveats. Scrape quality is good: the core text, tables, usage code blocks, changelog, and citation are present, though rendered images and linked external docs are not embedded.
