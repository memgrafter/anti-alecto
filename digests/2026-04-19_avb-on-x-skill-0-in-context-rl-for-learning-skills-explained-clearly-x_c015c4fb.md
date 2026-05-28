---
url: https://x.com/neural_avb/status/2041524183499428217
title: 'AVB on X: "SKILL-0: In Context RL for Learning Skills, explained clearly" / X'
scraped_at: '2026-04-19T07:31:46Z'
word_count: 2085
raw_file: raw/2026-04-19_avb-on-x-skill-0-in-context-rl-for-learning-skills-explained-clearly-x_c015c4fb.txt
tldr: 'A breakdown of the LongCat team’s SKILL-RL → SKILL-0 pipeline: first build a SkillBank from trajectories and teacher-distilled lessons, then use RL/GRPO with a curriculum that gradually removes skill prompts so the model internalizes those skills into its weights.'
key_quote: Skills are lazily loaded prompts.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: deep-study
scrape_quality: partial
people:
- LongCat team
- AVB
- OpenAI o3
tools:
- GRPO
- GEPA
- Mem0
- MemRL
- Qwen2.5-VL
- GPT-4o
- Gemini-2.5-Pro
- Qwen-3
- Qwen-3.5
libraries: []
companies:
- LongCat
- OpenAI
- Qwen
- Anthropic
tags:
- reinforcement-learning
- skill-discovery
- large-language-models
- vision-language-models
- agent-training
---

### TL;DR
A breakdown of the LongCat team’s SKILL-RL → SKILL-0 pipeline: first build a SkillBank from trajectories and teacher-distilled lessons, then use RL/GRPO with a curriculum that gradually removes skill prompts so the model internalizes those skills into its weights.

### Key Quote
> “Skills are lazily loaded prompts.”

### Summary
- This X thread is a paper breakdown of the LongCat team’s work on **SKILL-RL** and **SKILL-0**, framed as a path toward “vertical intelligence” rather than generic API use.
- Core idea:
  - **SKILL-RL** discovers and organizes reusable skills from environment interactions.
  - **SKILL-0** trains a policy to absorb those skills into model weights via **in-context reinforcement learning** and **GRPO**.
- The thread’s setup:
  - Use a **harness** around a local/open-source model.
  - Make the task environment **verifiable** so success/failure can be checked programmatically.
  - Use **SKILL-RL** to auto-discover skills.
  - Use **SKILL-0** to distill those skills into the model so inference becomes cheaper and skill prompts can be removed.
- The thread defines skills as a structured package of procedural knowledge/instructions, optionally with executable resources, typically stored as markdown files like `SKILL.md` in a skill directory.
- **SKILL-RL pipeline** described in the thread:
  - Collect raw trajectories from the environment, including both **successful and failed** attempts.
  - Distill trajectories into lessons:
    - successes → critical decision points
    - failures → “failure lessons” explaining what went wrong and what should have happened
  - Use a teacher LLM to synthesize these lessons into **1–3 actionable skills** in a fixed schema.
  - Organize them into a hierarchical **SkillBank** with:
    - **general skills** like exploration, state tracking, goal tracking
    - **task-specific skills** with preconditions, constraints, and failure modes
- **SKILL-0 pipeline** described in the thread:
  - Start from the SkillBank produced by SKILL-RL.
  - Represent skills as markdown files in a structure like `skills/{task_name}/{skill_category}.md`.
  - During training, retrieve a subset of relevant skills for each rollout.
  - Use **context rendering** to compress environment history + selected skill files into a compact RGB image, which is then encoded by a vision encoder.
  - Feed the prompt text plus rendered context to the model.
  - Apply a **dynamic curriculum** that progressively reduces the number of skills available, eventually reaching **skill-free inference**.
- The two example domains highlighted:
  - **ALFWorld**
    - Tasks mentioned: Pick & Place, Look At, Clean, Heat, Cool, Pick Two
    - Requires navigation, object interaction, and state tracking
  - **Search-QA**
    - Benchmarks mentioned: TriviaQA, PopQA, HotpotQA, 2Wiki, MuSiQue, Bamboogle
    - Requires deciding when to search, query refinement, and multi-hop aggregation
- Model/training details called out:
  - The seed model is **Qwen2.5-VL**
  - The approach assumes **open-source/self-hosted models** because weights must be updated
  - For closed-source models, the thread suggests prompt optimization methods like **GEPA** instead of weight updates
  - The paper compares SKILL-0 against prompting, GRPO, memory-based methods like **Mem0** and **MemRL**, and Skill-RL itself
- Claimed takeaway:
  - SKILL-0 can outperform several alternative approaches by combining skill discovery, curriculum learning, and RL-based internalization.
  - The author presents this as evidence that smaller local models (3B/7B-class) may become practical for narrow, high-value tasks.

### Assessment
This is a **mixed** content type: mostly an **opinionated technical thread** that summarizes two research papers rather than presenting original research itself. Durability is **medium**: the conceptual pipeline of skills → skill bank → curriculum RL is relatively durable, but the specific model names, benchmarks, and claims about current model comparisons will age quickly as versions change. Density is **high** because the thread packs a lot of named methods, environments, benchmarks, and implementation details into a single post. Originality is best described as **commentary/synthesis**: it interprets and explains the LongCat team’s papers rather than serving as a primary source. For **recall**, this summary preserves the thread’s structure well: SKILL-RL builds the SkillBank, SKILL-0 internalizes it, and curriculum removal of skill prompts is the key mechanism. For **decide**, it’s worth re-reading if you care about agent training pipelines, skill libraries, or RL-based distillation into local VLMs; less so if you only wanted a surface-level explanation. For **find**, the strongest identifiers are **LongCat**, **SKILL-RL**, **SKILL-0**, **Qwen2.5-VL**, **ALFWorld**, **Search-QA**, **GRPO**, **Mem0/MemRL**, and the markdown skill-file pattern `skills/{task_name}/{skill_category}.md`. Scrape quality is **partial**: the text is mostly captured, but several details seem to come from linked screenshots/diagrams that are not visible here, so some schema and table-specific nuances may be missing.
