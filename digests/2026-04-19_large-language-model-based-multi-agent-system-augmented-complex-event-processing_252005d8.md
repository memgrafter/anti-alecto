---
url: https://arxiv.org/html/2501.00906v2
title: Large Language Model Based Multi-Agent System Augmented Complex Event Processing Pipeline for Internet of Multimedia Things
scraped_at: '2026-04-19T07:19:16Z'
word_count: 14188
raw_file: raw/2026-04-19_large-language-model-based-multi-agent-system-augmented-complex-event-processing_252005d8.txt
tldr: This paper presents a proof-of-concept that combines AutoGen multi-agent LLM orchestration with Kafka pub/sub to build an autonomous complex event processing pipeline for video query processing, while also surveying LLM agent systems and evaluating latency/accuracy trade-offs across agent counts, video complexity, and resolution.
key_quote: Adding more than four agents led to excessive and redundant communications, further exacerbating latency without significant improvements in functionality.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Q. Wu
- H. Kokkonen
- Z. Zou
- M. Satyanarayanan
- S. Rasal
- B. Pan
- J. Chen
- Y. Qin
- L. Lovén
tools:
- AutoGen
- Kafka
- Auto-GPT
- LangChain
- GPT-4o
libraries:
- LLaMA
- GPT-4
- ToolBench
companies:
- IBM
- Meta
- OpenAI
- Business Finland
- Research Council of Finland
tags:
- multi-agent-systems
- large-language-models
- complex-event-processing
- publish-subscribe
- video-analytics
---

### TL;DR
This paper presents a proof-of-concept that combines AutoGen multi-agent LLM orchestration with Kafka pub/sub to build an autonomous complex event processing pipeline for video query processing, while also surveying LLM agent systems and evaluating latency/accuracy trade-offs across agent counts, video complexity, and resolution.

### Key Quote
"Adding more than four agents led to excessive and redundant communications, further exacerbating latency without significant improvements in functionality."

### Summary
- **What the paper is about**
  - A proof-of-concept (POC) for augmenting **Complex Event Processing (CEP)** with **Large Language Model (LLM)-based multi-agent systems**.
  - Focuses on **video query processing** in an **Internet of Multimedia Things** setting.
  - Integrates **AutoGen** with **Kafka** message brokers to bridge LLM agents and existing pub/sub infrastructure.

- **Main research questions**
  - **RQ1:** What does the current landscape of **single-agent and multi-agent LLM systems** look like?
  - **RQ2:** How can LLMs be integrated into multi-agent systems to augment CEP pipelines while meeting QoS requirements?

- **Core contributions**
  - A **survey and gap analysis** of LLM-based autonomous agent applications.
  - A **POC CEP pipeline** that unifies **AutoGen + Kafka** for event-driven video analytics.
  - A discussion of **lessons learned** from deploying multi-agent systems for CEP.

- **Background themes covered**
  - **Distributed AI / computing continuum:** cloud, edge, fog, and IoT resources used together for lower-latency processing.
  - **Publish/subscribe paradigm:** publishers, subscribers, topics, and brokers as the messaging backbone.
  - **LLMs / foundation models:** transformer-based models, multimodal capabilities, and their relevance for reasoning/planning.
  - **AutoGen framework:** used as the multi-agent orchestration layer.

- **AutoGen agents described**
  - **Conversable Agent:** base class for inter-agent communication, code generation/execution, automated replies.
  - **Assistant Agent:** LLM-backed autonomous assistant.
  - **User Proxy Agent:** human-facing proxy that can solicit input and trigger execution.
  - The paper also distinguishes:
    - **LLM-backed agents**
    - **Human-backed agents**
    - **Tool-backed agents**

- **Survey / related work**
  - Covers both **single-agent** systems (e.g. **Auto-GPT**, **LangChain**) and **multi-agent** systems.
  - Multi-agent examples include:
    - **MAPE-K-based self-adaptive MAS**
    - **LLM Harmony**
    - **AgentCoord**
    - **AgentLite**
    - **MetaGPT**
    - **ChatDev**
    - **SOCRATEST**
    - **Smurfs**
    - **ToolLLM** / **ToolBench** with **16,464 APIs across 49 categories**
    - Robotics, cybersecurity, network slicing, and design applications
  - The paper frames a major gap as the need for **tool-using, modular, interoperable LLM-MAS frameworks** that can fit existing infrastructures.

- **System design / architecture**
  - The architecture has three broad parts:
    - **Central Coordination Unit**: AutoGen orchestrates agent routing and tool calls.
    - **End Users**: issue natural-language video queries.
    - **Cloud and Edge Instances**: cloud hosts the model; edge/pub-sub infrastructure moves data.
  - The workflow uses **Kafka topics** such as `camera-1` to route frames.
  - The system emphasizes using **existing verified tools/functions** rather than dynamically generating code, to reduce breakage, latency, and security risk.
  - Supports both **synchronous** and **asynchronous** query handling.

- **Concrete workflow example**
  - User asks: *“Are there any red vehicles visible in camera 1, camera 2, camera 3, camera 4, camera 5?”*
  - A simplified two-agent setup uses:
    - **User Proxy Agent**
    - **Conversable / tool-backed Engineer Agent**
  - The Engineer agent:
    - consumes from Kafka
    - extracts frames
    - reconstructs video
    - calls the model
    - returns the answer
  - The example appendix shows explicit tool calls:
    - `kafka_consume`
    - `frame_extraction`
    - `create_video_from_frames`
    - `call_model`

- **Experiments**
  - **Experiment 1: Increasing number of AutoGen agents**
    - 2 agents: **5–8 s** latency, **1–2 s** overhead
    - 3 agents: **12–16 s** latency, **8–10 s** overhead
    - 4 agents: **22–25 s** latency, **12–16 s** overhead
    - More than 4 agents caused redundant communication and little functional gain.
    - The paper argues **4 agents** is the best balance for this use case.
  - **Speaker selection optimization**
    - AutoGen speaker modes discussed: **Auto, Manual, Round-Robin, Random**
    - The paper proposes a **keyword-based structured speaker selection** approach using agents such as **Reflection**, **Engineer-1**, and **Engineer-2**.
  - **Experiment 2: Increasing video complexity**
    - Five levels of video complexity, from a single car in a simple scene to crowded, bright, multi-vehicle urban scenes.
    - Scores generally drop as complexity increases.
    - Table 3 values:
      - **Correctness:** 0.8, 0.8, 0.9, 0.7, 0.6
      - **Detailed Orientation:** 0.7, 0.7, 0.8, 0.6, 0.5
      - **Contextual Understanding:** 0.9, 0.9, 0.9, 0.8, 0.7
      - **Temporal Understanding:** 0.8, 0.8, 1.0, 0.7, 0.6
      - **Consistency:** 1.0, 1.0, 1.0, 1.0, 0.9
    - The main pattern is that **consistency stays high**, while detailed accuracy degrades on harder videos.
  - **Experiment 3: Video complexity + resolution**
    - Tested at **1080p, 720p, 360p, 144p**
    - Lower resolution consistently reduced total latency and GPT model-call time.
    - Example Level 1:
      - Total duration falls from **13.37 s** at 1080p to **8.2 s** at 144p
      - GPT call latency falls from **10.2 s** to **5.3 s**
    - Similar latency reductions are reported for Levels 2–5.

- **Main findings**
  - More agents increase capability but also **increase latency** due to communication overhead.
  - The system performs better on **simpler videos** and degrades on dense, cluttered scenes.
  - Lower video resolution improves speed but can reduce detail/accuracy.
  - The system is presented as a feasible way to integrate LLM agents into existing CEP/pub-sub infrastructure.

- **Limitations**
  - Adding agents can cause **loss or mutation of information** across prompts.
  - Keyword-driven speaker selection becomes hard to manage as the number of agents grows.
  - The implementation does **not fully exploit federated learning or edge computing**.
  - The design relies heavily on **predefined workflows and tool configurations**, limiting adaptability to novel scenarios.
  - The paper acknowledges LLM-MAS as a **young and evolving area**.

- **Conclusion**
  - The paper argues that AutoGen + Kafka can form a workable **LLM-augmented CEP pipeline** for multimedia IoT/video query tasks.
  - It positions the work as a bridge between **LLM orchestration** and **existing distributed systems infrastructure**.
  - Future work: improve inter-agent communication efficiency, scale to more agents, and integrate **federated learning** / **edge computing** more deeply.

### Assessment
This is a **mixed** research paper with both a survey component and a systems/experimentation component. **Durability is medium**: the architectural ideas around pub/sub, multi-agent orchestration, and CEP are fairly durable, but the specific framework choices, model references, and performance numbers are tied to a 2025-era prototype and will age as AutoGen, Kafka integrations, and LLMs evolve. **Content type** is **mixed** (survey + technical proof-of-concept + experimental results). **Density is high**: it contains many named systems, tables, agent roles, metrics, and implementation details. **Originality** is mostly **primary source**, since it presents an implemented POC and measured results, though the survey portion is clearly synthesized from prior work. **Reference style** is best as **refer-back** rather than deep-study for general architecture recall, but deep-study could be useful if you are comparing LLM agent orchestration patterns or CEP integration strategies. **Scrape quality is good but partial**: the text includes the abstract, main sections, tables, appendix code-like conversation flow, and references, but figure visuals are missing and some table/number formatting is messy; still, the key experimental values and agent/tool names were captured well enough for reliable identification.
