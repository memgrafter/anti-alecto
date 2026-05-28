---
url: https://arxiv.org/html/2603.28990v1#S3
title: 'Drop the Hierarchy and Roles: How Self-Organizing LLM Agents Outperform Designed Structures'
scraped_at: '2026-04-19T08:24:14Z'
word_count: 5397
raw_file: raw/2026-04-19_drop-the-hierarchy-and-roles-how-self-organizing-llm-agents-outperform-designed-_f5cfae43.txt
tldr: A large computational study of 25,000+ multi-agent LLM tasks argues that the best coordination setup is neither full hierarchy nor full autonomy, but a hybrid “Sequential” protocol where agent order is fixed while role choice remains self-organized.
key_quote: “Effective self-organization requires both a capable model and the right protocol—neither alone suffices.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- S. Budyonny
- E. Latypova
- K. Ruppel
- Claude
- Anthropic
- Q. Chen
- S. Hong
- Q. Wu
- Y. Li
- X. Yuan
- Z. Chen
- H. Li
- C. Qian
- Y. Wang
- M. Wooldridge
- A. Dorri
- R. Jurdak
- Y. Shoham
- K. Leyton-Brown
- S. A. Kauffman
- E. Bonabeau
- M. Dorigo
- G. Theraulaz
- M. Zhuge
- J. Wang
- W. Chen
- Y. Talebirad
- A. Nadiri
- Z. Xi
tools:
- OpenRouter
libraries: []
companies:
- Meta
- OpenAI
- Google
- Anthropic
- GigaChat
- DeepSeek
- GLM
tags:
- multi-agent-systems
- llm-agents
- coordination-protocols
- self-organization
- agent-governance
---

### TL;DR
A large computational study of 25,000+ multi-agent LLM tasks argues that the best coordination setup is neither full hierarchy nor full autonomy, but a hybrid “Sequential” protocol where agent order is fixed while role choice remains self-organized.

### Key Quote
“Effective self-organization requires both a capable model and the right protocol—neither alone suffices.”

### Summary
- **Core thesis:** Multi-agent LLM systems perform best when they combine:
  - a **capable foundation model**
  - a **minimal but useful coordination protocol**
  - **no pre-assigned fixed roles**
- The paper claims an **“endogeneity paradox”**:
  - **Too much control**: centralized “Coordinator” structure underperforms
  - **Too much freedom**: fully autonomous “Shared” protocol underperforms
  - **Best result**: **Sequential** protocol, where the **ordering is fixed** but each agent **autonomously selects roles and may abstain**
- The study spans:
  - **25,000+ task runs**
  - **20,810 unique configurations**
  - **8 LLM models**
  - **4–256 agents**
  - **8 coordination protocols**
  - **4 task complexity levels (L1–L4)**
- Models tested include:
  - Closed-source: **Claude Sonnet 4.6, GPT-5.4, GPT-4o, GPT-4.1-mini, Gemini-3-flash, GigaChat 2 Max**
  - Open-source: **DeepSeek v3.2, GLM-5**
- Main findings:
  - **Sequential outperforms Coordinator and Shared** on quality and balance metrics
  - **Scaling to 256 agents** shows **sub-linear cost growth** and **no quality degradation**
  - **Role invention is highly dynamic**:
    - 5,006 unique roles from 8 agents in one setting
    - agents do not settle into stable fixed positions
  - Agents show **voluntary self-abstention** when they judge they are not useful
  - The system forms **shallow, spontaneous hierarchies** rather than deep rigid ones
- **Capability threshold claim:**
  - Self-organization works best only for **strong models**
  - For weaker models, **rigid structure can outperform autonomy**
  - The paper argues self-organization needs:
    1. self-reflection
    2. deep reasoning
    3. instruction following
- **Protocol comparison:**
  - **Coordinator**: centralized agent assigns roles
  - **Sequential**: agents act in fixed order and see predecessors’ outputs
  - **Broadcast**: agents first announce intentions, then decide
  - **Shared**: all agents act simultaneously with shared memory of past tasks
- **Task complexity effects:**
  - L4 adversarial tasks are much harder and show lower quality
  - Hierarchy depth increases somewhat with complexity, suggesting the system forms more structure when needed
- **Closed vs open source:**
  - Open-source models, especially **DeepSeek v3.2**, are reported to achieve near-closed-source quality at lower cost
- **Broader design implication:**
  - The author argues practitioners should define **mission and values**, choose a good **protocol**, and invest in **model quality**, rather than assigning human-style roles
- **Governance proposal:**
  - A **three-ring constitutional framework**:
    - **Ring 1:** human-controlled mission/values
    - **Ring 2:** shared human+system standards and audits
    - **Ring 3:** autonomous coordination protocols

### Assessment
This is a **research/technical** paper with a **mixed** tone: empirical claims plus strong design opinion. Durability is **medium** because the conceptual framing around autonomy vs coordination may last, but the concrete results depend on specific LLM versions, API behavior, and synthetic task design. Density is **high**: it contains many protocols, models, metrics, experimental blocks, and statistical claims. Originality is **primary source**, since it reports its own experiment rather than summarizing others. It is best treated as **refer-back** material if you work on multi-agent LLM coordination, protocol design, or agent governance. Scrape quality is **partial**: the text is extensive and includes many sections, but many equations, symbols, and some table values appear missing or garbled, so the exact quantitative details are not fully reliable from this capture alone.
