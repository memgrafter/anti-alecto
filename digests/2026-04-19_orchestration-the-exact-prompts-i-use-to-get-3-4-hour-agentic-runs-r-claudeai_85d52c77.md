---
url: https://www.reddit.com/r/ClaudeAI/comments/1s0nktx/orchestration_the_exact_prompts_i_use_to_get_34/
title: 'Orchestration -- the exact prompts I use to get 3-4 hour agentic runs : r/ClaudeAI'
scraped_at: '2026-04-19T21:54:23Z'
word_count: 2334
raw_file: raw/2026-04-19_orchestration-the-exact-prompts-i-use-to-get-3-4-hour-agentic-runs-r-claudeai_85d52c77.txt
tldr: In this r/ClaudeAI thread, u/lucianw argues that long-running agentic coding works best with simple markdown-based orchestration plus fresh second-opinion reviewers, while top commenter u/child-eater404 praises it as the first practical alternative to “50-agent black box” systems.
key_quote: “this is actually the first orchestration post that doesn’t feel like “just trust my 50-agent black box bro””
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- u/lucianw
- u/child-eater404
- u/justserg
- u/Efficient-Piccolo-34
- u/Skynet_5656
- u/Jerrybezerk
- u/mcouthon
- u/Longjumping-Past-342
- u/Only-Fisherman5788
- u/cron_featurecreep
- u/Striking_Big8138
- u/ry8
tools:
- Claude
- Codex
libraries: []
companies:
- Anthropic
tags:
- agentic-coding
- ai-orchestration
- workflow-design
- validation-loops
- code-review
---

### TL;DR
In this r/ClaudeAI thread, u/lucianw argues that long-running agentic coding works best with simple markdown-based orchestration plus fresh second-opinion reviewers, while top commenter u/child-eater404 praises it as the first practical alternative to “50-agent black box” systems.

### Key Quote
“this is actually the first orchestration post that doesn’t feel like “just trust my 50-agent black box bro””

### Summary
- **Top comment (verbatim):** "this is actually the first orchestration post that doesn’t feel like “just trust my 50-agent black box bro”"
- **Top commenter:** `u/child-eater404`
- **Thread topics:**
  - Using a small, readable markdown orchestration prompt instead of large agent swarms
  - Separating planning and implementation into milestone files like `PLAN.md` and `PLAN-M3.md`
  - Forcing validation and second-opinion reviews from fresh agents to reduce hallucinations
  - Whether parallel/swarms-style agent setups are actually useful for coding work
  - Keeping architecture and “better engineering” work as a separate milestone stream

- **Original poster’s workflow:**
  - Claims to get **3–4 hour autonomous coding runs** with decent-quality code.
  - Uses a **25-line markdown orchestration prompt** rather than a large framework or black-box agent system.
  - Starts from `PLAN.md`, which defines milestone structure and orchestration instructions for planning.
  - Prompts an agent to read `@PLAN.md`, ask questions, then produce a milestone plan into `PLAN-M3.md`.
  - `PLAN-M3.md` includes instructions for **implementation orchestration**: steps, implementation order, and validation.
  - During implementation, the agent makes **four separate second-opinion requests** to another agent (Claude/Codex) on:
    - KISS / simplicity
    - codebase style alignment
    - correctness
    - whether it satisfies milestone goals
  - If objections arise, the agent must address them before finishing.
  - After each milestone, he runs a separate **“better engineering” milestone** using `AGENTS.md` to enforce clean architecture standards.

- **What the author says about his role:**
  - He does **not** read the AI-written plans closely because they are meant for other AIs.
  - He **does** read second-agent reviews and uses them to decide what to do next.
  - He sees his job as **overseeing architecture and quality**, not feature implementation.
  - He says AIs are already good enough at feature work, but still lack taste for architecture and engineering quality.

- **Why he prefers this approach:**
  - He distrusts “50-agent black box” systems that obscure what is essential.
  - He wants a workflow that is **simple, transparent, and reproducible**.
  - He argues that long-running quality depends more on **the loops around the agent** than on optimizing the agent itself.
  - He believes structural validation is more effective than just telling the model to “be careful.”

- **Important details from comments/discussion:**
  - Several commenters agree that the main insight is to optimize **review/validation loops** rather than the agent alone.
  - One commenter notes that agents are “extremely confident liars,” and validation should be structural, not just prompt-based.
  - Another says parallel agents only work well when tasks are fully isolated; shared files create merge conflicts that erase any speed gains.
  - The author replies that he is **not using swarms/parallel agents for code writing**, calling that a failed experiment.
  - He says parallelism rarely works within a milestone because most tasks are not truly independent.
  - He also says swarms haven’t reliably solved the “agent should refactor instead of hacking” problem.
  - A commenter asks what the 25-line orchestration prompt looks like; the author says it is general and depends on supporting files like:
    - `LEARNINGS.md` for general engineering wisdom
    - `ARCHITECTURE.md` for project-specific wisdom
  - He mentions using hooks/reminders to keep these files updated.

- **Tone and stance of the thread:**
  - Mostly supportive of the author’s minimalist, transparent workflow.
  - Skeptical of heavy multi-agent frameworks and noisy “orchestrator” marketing.
  - Strong emphasis on **review, validation, and clean architecture** over raw automation.

### Assessment
This is a **mixed** content thread that is highly relevant if you’re evaluating practical agentic coding workflows, especially around orchestration, validation, and review loops. Durability is **medium**: the core ideas about structured validation and avoiding black-box agent swarms are fairly durable, but the specifics are tied to current Claude/Codex practices and recent agent tooling. Content density is **high**, with concrete workflow details, file names, prompts, and opinionated commentary. Originality is mostly **commentary** and practical synthesis from an experienced engineer rather than a formal study. It is best used as **refer-back** material if you’re designing your own agent workflow or comparing orchestration strategies. Scrape quality is **good overall**: the post, major comment themes, and several comment excerpts are captured, though the thread is truncated in places and the quoted prompt contents are only partially reproduced.
