---
url: https://openai.com/index/introducing-gpt-5-4/
title: Introducing GPT-5.4 | OpenAI
scraped_at: '2026-04-19T06:45:47Z'
word_count: 3310
raw_file: raw/2026-04-19_introducing-gpt-5-4-openai_1df3c91e.txt
tldr: OpenAI announces GPT‑5.4, a new frontier model for ChatGPT, API, and Codex that emphasizes professional work, computer use, tool search, coding, and factual accuracy, while also introducing GPT‑5.4 Pro for maximum performance.
key_quote: GPT‑5.4 is our most capable and efficient frontier model for professional work.
durability: medium
content_type: announcement
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Playwright
- Codex
- ChatGPT
- API
- ChatGPT for Excel
- MCP Atlas
libraries: []
companies:
- OpenAI
- Zapier
- Scale
- ChatGPT Atlas
tags:
- ai-models
- computer-use
- agentic-workflows
- api-pricing
- benchmark-evaluation
---

### TL;DR
OpenAI announces GPT‑5.4, a new frontier model for ChatGPT, API, and Codex that emphasizes professional work, computer use, tool search, coding, and factual accuracy, while also introducing GPT‑5.4 Pro for maximum performance.

### Key Quote
“GPT‑5.4 is our most capable and efficient frontier model for professional work.”

### Summary
- **What launched**
  - **GPT‑5.4** is now rolling out in **ChatGPT (as GPT‑5.4 Thinking)**, the **API**, and **Codex**.
  - **GPT‑5.4 Pro** is also being released in **ChatGPT and the API** for maximum performance on complex tasks.
  - OpenAI says GPT‑5.4 combines recent advances in **reasoning, coding, and agentic workflows**.

- **Core product claims**
  - Stronger at **professional work** such as spreadsheets, presentations, documents, legal analysis, and financial modeling.
  - In ChatGPT, **GPT‑5.4 Thinking** can provide an **upfront plan of its thinking**, letting users steer mid-response.
  - Better **deep web research**, especially for narrow/specific questions, while maintaining context over longer reasoning.
  - In Codex and the API, GPT‑5.4 is presented as OpenAI’s **first general-purpose model with native, state-of-the-art computer-use capabilities**.
  - Supports up to **1M tokens of context** for long-horizon agent workflows.
  - Adds **tool search** in the API so models can look up tool definitions only when needed, reducing prompt bloat and cost.
  - OpenAI says GPT‑5.4 is its **most token-efficient reasoning model yet**, using significantly fewer tokens than GPT‑5.2.

- **Benchmark highlights**
  - **GDPval**: **83.0%** wins or ties vs GPT‑5.2’s **70.9%**.
  - **SWE-Bench Pro (Public)**: **57.7%** vs **55.6%** for GPT‑5.2.
  - **OSWorld-Verified**: **75.0%**, up from **47.3%** for GPT‑5.2; OpenAI says this surpasses reported human performance (**72.4%**).
  - **Toolathlon**: **54.6%** vs **46.3%** for GPT‑5.2.
  - **BrowseComp**: **82.7%** vs **65.8%** for GPT‑5.2.
  - For legal work, OpenAI quotes **BigLaw Bench** performance of **91%**.
  - For spreadsheet modeling, GPT‑5.4 scores **87.3%** vs **68.4%** for GPT‑5.2.
  - Human raters preferred GPT‑5.4 presentations **68.0%** of the time over GPT‑5.2.

- **Computer-use and browser-use details**
  - Works with **Playwright** and also with mouse/keyboard actions from screenshots.
  - Behavior can be steered with **developer messages**.
  - Developers can set **custom confirmation policies** for different risk tolerances.
  - On **WebArena-Verified**, GPT‑5.4 reaches **67.3%** with DOM + screenshots.
  - On **Online-Mind2Web**, it gets **92.8%** using screenshot-based observations alone.
  - Improved visual perception also helps with **document parsing** and image understanding.

- **Visual input changes**
  - OpenAI introduces a new **original image input detail** level.
  - Supports up to **10.24M total pixels** or **6000-pixel max dimension**.
  - The **high detail** level now supports up to **2.56M total pixels** or a **2048-pixel max dimension**.
  - OpenAI says this improves localization, image understanding, and click accuracy.

- **Tooling and API changes**
  - The new **computer tool** is the API path for computer-use workflows.
  - **Tool search** reduces token usage by fetching tool definitions only when needed.
  - In one benchmark using **36 MCP servers**, tool search reduced token usage by **47%** with the same accuracy.
  - GPT‑5.4 improves tool calling accuracy and efficiency in multi-step workflows.

- **Speed and coding**
  - In Codex, **/fast mode** with GPT‑5.4 can deliver up to **1.5x faster token velocity**.
  - Developers can get similar speed in the API via **priority processing**.
  - OpenAI says GPT‑5.4 is better at **frontend tasks**, with more aesthetic and functional outputs.
  - An experimental Codex skill called **“Playwright (Interactive)”** is released to visually debug web and Electron apps.

- **Research, safety, and cybersecurity**
  - OpenAI treats GPT‑5.4 as **High cyber capability** under its Preparedness Framework.
  - Deployment includes safeguards such as:
    - expanded cyber safety stack
    - monitoring systems
    - trusted access controls
    - asynchronous blocking for higher-risk requests on **Zero Data Retention (ZDR)** surfaces
  - OpenAI says false positives may still occur while safeguards are refined.
  - The post also discusses **Chain-of-Thought monitorability** and introduces an open-source evaluation called **CoT controllability**.
  - OpenAI says GPT‑5.4 Thinking’s ability to control its CoT is low, which it frames as safer because reasoning is harder to hide.

- **Availability and pricing**
  - **ChatGPT Plus, Team, and Pro** users get **GPT‑5.4 Thinking** first, replacing GPT‑5.2 Thinking.
  - **GPT‑5.2 Thinking** remains available for **three months** in Legacy Models, then retires on **June 5, 2026**.
  - **Enterprise and Edu** can enable early access via admin settings.
  - **GPT‑5.4 Pro** is available to **Pro and Enterprise** plans.
  - In the API:
    - **gpt-5.4**: **$2.50 / M input tokens**, **$0.25 / M cached input tokens**, **$15 / M output tokens**
    - **gpt-5.4-pro**: **$30 / M input tokens**, **$180 / M output tokens**
  - OpenAI notes GPT‑5.4 is priced higher than GPT‑5.2, but token efficiency may reduce total cost in practice.

- **Assessment of the model according to OpenAI**
  - Stronger across:
    - professional knowledge work
    - coding
    - computer use
    - tool use
    - web search
    - long-context reasoning
    - abstract reasoning
  - OpenAI emphasizes that GPT‑5.4 is especially useful for **long-running agentic tasks** with fewer manual interventions.

### Assessment
Durability: **medium** — the conceptual framing around agentic workflows, computer use, tool search, and professional knowledge work should remain useful, but the specific model claims, benchmark scores, pricing, and rollout details will age quickly. Content type: **announcement / mixed**. Density: **high** — it is packed with product claims, benchmark results, pricing, rollout details, and safety notes. Originality: **primary source** — this is OpenAI’s own launch post with quoted internal and external eval claims. Reference style: **refer-back** — useful if you want specifics like availability, prices, benchmark numbers, or feature names. Scrape quality: **good** — the post appears substantially captured, including the benchmark tables, rollout details, pricing, and footnote; some formatting is flattened, but the substantive content seems intact.
