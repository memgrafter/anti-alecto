---
url: https://z.ai/blog/glm-4.6v
title: 'GLM-4.6V: Open Source Multimodal Models with Native Tool Use'
scraped_at: '2026-04-16T05:46:53Z'
word_count: 1368
raw_file: raw/2026-04-16_glm-4-6v-open-source-multimodal-models-with-native-tool-use_9e125d57.txt
tldr: Z.ai’s GLM-4.6V release introduces two open-source multimodal models—106B and 9B—with native multimodal tool use, 128K context, and strong performance on 20+ benchmarks for document, web, frontend, and long-video understanding.
key_quote: “Crucially, we integrate native Function Calling capabilities for the first time.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- V Team
- Wenyi Hong
- Wenmeng Yu
- Xiaotao Gu
- Guo Wang
- Guobing Gan
- Haomiao Tang
- Jiale Cheng
- Ji Qi
- Junhui Ji
- Lihang Pan
- Shuaiqi Duan
- Weihan Wang
- Yan Wang
- Yean Cheng
- Zehai He
- Zhe Su
- Zhen Yang
- Ziyang Pan
- Aohan Zeng
- Baoxu Wang
- Bin Chen
- Boyan Shi
- Changyu Pang
- Chenhui Zhang
- Da Yin
- Fan Yang
- Guoqing Chen
- Jiazheng Xu
- Jiale Zhu
- Jiali Chen
- Jing Chen
- Jinhao Chen
- Jinghao Lin
- Jinjiang Wang
- Junjie Chen
- Leqi Lei
- Letian Gong
- Leyi Pan
- Mingdao Liu
- Mingde Xu
- Mingzhi Zhang
- Qinkai Zheng
- Sheng Yang
- Shi Zhong
- Shiyu Huang
- Shuyuan Zhao
- Siyan Xue
- Shangqin Tu
- Shengbiao Meng
- Tianshu Zhang
- Tianwei Luo
- Tianxiang Hao
- Tianyu Tong
- Wenkai Li
- Wei Jia
- Xiao Liu
- Xiaohan Zhang
- Xin Lyu
- Xinyue Fan
- Xuancheng Huang
- Yanling Wang
- Yadong Xue
- Yanfeng Wang
- Yanzi Wang
- Yifan An
- Yifan Du
- Yiming Shi
- Yiheng Huang
- Yilin Niu
- Yuan Wang
- Yuanchang Yue
- Yuchen Li
- Yutao Zhang
- Yuting Wang
- Yu Wang
- Yuxuan Zhang
- Zhao Xue
- Zhenyu Hou
- Zhengxiao Du
- Zihan Wang
- Peng Zhang
- Debing Liu
- Bin Xu
- Juanzi Li
- Minlie Huang
- Yuxiao Dong
- Jie Tang
tools:
- Z.ai
- Zhipu Qingyan App
- GitHub
- HuggingFace
- ModelScope
- vLLM
- SGLang
libraries: []
companies:
- Z.ai
- Zhipu
tags:
- multimodal-models
- tool-use
- long-context
- open-source-ai
- multimodal-agents
---

### TL;DR
Z.ai’s GLM-4.6V release introduces two open-source multimodal models—106B and 9B—with native multimodal tool use, 128K context, and strong performance on 20+ benchmarks for document, web, frontend, and long-video understanding.

### Key Quote
“Crucially, we integrate native Function Calling capabilities for the first time.”

### Summary
- **What was released**
  - GLM-4.6V series, announced on **2025-12-08** as a **Research** post.
  - Two model variants:
    - **GLM-4.6V (106B)**: foundation model for cloud / high-performance cluster use
    - **GLM-4.6V-Flash (9B)**: lightweight model for local deployment and low-latency use
- **Core technical claims**
  - Training context window extended to **128K tokens**
  - Claimed **state-of-the-art performance among models of similar parameter scale** in multimodal understanding, logical reasoning, and long-context understanding
  - First GLM-4.6V release to include **native Function Calling** for multimodal tool use
- **Native multimodal tool use**
  - **Multimodal input as tool parameters**: images, screenshots, and document pages can be passed directly without first converting them to text
  - **Multimodal output comprehension**: the model can interpret tool outputs like search results, charts, rendered web screenshots, and retrieved product images
  - Goal: connect **perception → understanding → execution** in one loop
- **Highlighted scenarios**
  - **Rich-text content understanding and creation**
    - Reads papers, reports, and slides with text, charts, figures, tables, and formulas
    - Can autonomously crop key visuals during generation
    - Performs “visual audit” of candidate images and composes image-text interleaved articles for social media or knowledge bases
  - **Visual web search**
    - Recognizes intent, plans search, triggers text-to-image / image-to-text search tools
    - Fuses visual and textual retrieval results into a structured answer/report
  - **Frontend replication and visual interaction**
    - Upload a screenshot or design file and get high-fidelity **HTML/CSS/JS**
    - Supports interactive edits by circling a region and giving natural-language instructions like moving a button and changing its color
  - **Long-context understanding**
    - Claimed practical capacity of about **150 pages of complex documents**, **200 slide pages**, or a **one-hour video** in one inference pass
    - Example use cases: comparing **four public companies’ financial reports** and summarizing a full **football match** with goal events and timestamps
- **Techniques described**
  - **Continual pre-training** on long-context image-text data
  - Uses ideas from **Glyph** to improve visual-language compression alignment
  - Adds a **billion-scale multimodal perception and world knowledge dataset**
  - Extends **MCP (Model Context Protocol)** with:
    - **URL-based multimodal handling**
    - **Interleaved text-image output**
    - a **“Draft → Image Selection → Final Polish”** workflow
  - Trains tool invocation with **reinforcement learning**, including a **Visual Feedback Loop** inspired by **UI2Code^N**
- **Deployment / access**
  - Try and call it on **Z.ai**
  - Available through the **Zhipu Qingyan App**
  - API access via an **OpenAI-compatible API**
  - Model weights on **HuggingFace** and **ModelScope**
  - Supports inference with **vLLM** and **SGLang**
- **Citation note**
  - The page includes a BibTeX citation, but it is for **“GLM-4.5V and GLM-4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable Reinforcement Learning”** on arXiv (**2507.01006**), not a paper specifically titled GLM-4.6V

### Assessment
**Durability:** medium. The architectural ideas around native multimodal tool use, long-context modeling, and multimodal agent workflows are broadly relevant, but the benchmarks, model sizes, and deployment details are tied to a specific 2025 release and will age quickly. **Content type:** mixed, leaning research/announcement. **Density:** high, because it packs model specs, claimed benchmark results, deployment options, and technique descriptions into one page. **Originality:** primary source, since this is the vendor’s own release note and technical report summary, though the cited bibliography points to a related earlier paper on GLM-4.5V / GLM-4.1V-Thinking rather than this model alone. **Reference style:** refer-back; useful for checking exact model sizes, 128K context, tool-use claims, supported stacks like vLLM/SGLang, and the named application scenarios. **Scrape quality:** good overall; the text content is captured well, though any figures, charts, and the actual linked tech report content are not included, so some evidence for the claims may be missing.
