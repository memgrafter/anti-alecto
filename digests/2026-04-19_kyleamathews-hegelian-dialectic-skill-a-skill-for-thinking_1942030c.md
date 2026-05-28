---
url: https://github.com/KyleAMathews/hegelian-dialectic-skill
title: 'KyleAMathews/hegelian-dialectic-skill: A skill for thinking'
scraped_at: '2026-04-19T08:11:15Z'
word_count: 2610
raw_file: raw/2026-04-19_kyleamathews-hegelian-dialectic-skill-a-skill-for-thinking_1942030c.txt
tldr: A GitHub README for an AI “dialectic skill” that uses two fully committed subagents plus an orchestrator to stress-test a question, decompose both sides, and synthesize a richer third position through recursive rounds.
key_quote: “This isn't artificial intelligence — it's an artificial belief system that frees you to think.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- KyleAMathews
- Douglas Adams
- Venkatesh Rao
- Elizabeth Eisenstein
- Boyd
- Hegel
- Christopher Alexander
- Socrates
- Peirce
- Galinsky
- Pollock
- Aquinas
- Du
tools:
- Claude Code
- Cursor
- Windsurf
libraries: []
companies:
- GitHub
tags:
- ai-agents
- dialectic
- reasoning
- decision-making
- prompt-engineering
---

### TL;DR
A GitHub README for an AI “dialectic skill” that uses two fully committed subagents plus an orchestrator to stress-test a question, decompose both sides, and synthesize a richer third position through recursive rounds.

### Key Quote
“**This isn't artificial intelligence — it's an artificial belief system that frees you to think.**”

### Summary
- **What it is**
  - A project called **“The Electric Monks — Dialectic Skill”** by **KyleAMathews**.
  - It is meant for **coding agents with subagent spawning and web search** such as **Claude Code, Cursor, Windsurf**, etc.
  - The goal is to help users think better by automating expensive parts of reasoning.

- **Core idea**
  - The system uses **two AI subagents (“Electric Monks”)** that each take a fully committed position on a topic.
  - A third **orchestrator**:
    - interviews the user to surface the real contradiction,
    - researches the topic,
    - generates position-specific prompts,
    - compares and decomposes the arguments into atomic parts,
    - finds cross-domain connections,
    - synthesizes a new position.
  - The result is described as a **semi-lattice**: overlapping connections that no single linear argument would produce.

- **Why it claims to work**
  - It targets three bottlenecks in reasoning:
    1. **Belief** — once you commit to a side, you can’t fully inhabit its negation.
    2. **Research breadth** — it’s hard for humans to survey enough relevant material.
    3. **Structural comparison** — decomposing and comparing arguments at a fine-grained level is cognitively hard.
  - LLMs are presented as able to handle all three at scale.

- **When to use it**
  - For questions where you:
    - are stuck on a vision and can’t entertain alternatives,
    - feel torn between competing obligations,
    - can argue many sides but can’t commit,
    - suspect you’re optimizing the wrong thing,
    - have contradictory values,
    - want to question entrenched assumptions.
  - Suggested domains include:
    - **technical architecture**
    - **product strategy**
    - **philosophy**
    - **personal decisions**

- **How to use it**
  - Create a working directory like `dialectics/`, with one subdirectory per topic.
  - Install the skill into `.claude/skills/hegelian-dialectic-skill`.
  - Start your agent and invoke `/dialectic I want to explore: [topic]`.
  - The skill produces multiple markdown files per round, such as:
    - `round_1_context_briefing.md`
    - `round_1_monk_a.md`
    - `round_1_monk_b.md`
    - `round_1_determinate_negation.md`
    - `round_1_sublation.md`
    - `round_1_validation.md`
    - later rounds and a `dialectic_queue.md`
  - The process is intentionally heavy: **10–15 minutes per round minimum**, and at least **3 rounds** are expected.

- **Workflow phases**
  - **Phase 1: Elenctic interview + research**
    - Socratically surfaces hidden assumptions and the true tension.
  - **Phase 2: Generate Monk prompts**
    - Creates two calibrated, position-specific prompts.
  - **Phase 3: Spawn the Monks**
    - Two isolated agents produce strong, non-hedged, fully committed essays.
  - **Phase 4: Determinate negation**
    - The orchestrator identifies each side’s failure mode, shared assumptions, and contradictions.
    - It also applies a Boyd-style “destructive deduction” and “creative induction” to recombine atomic parts.
  - **Phase 5: Sublation (Aufhebung)**
    - Produces a synthesis that cancels, preserves, and elevates both sides.
    - The text emphasizes this is **not compromise**.
  - **Phase 6: Validation**
    - The Monks and a hostile auditor test whether the synthesis is genuinely elevated or just disguised compromise.
  - **Phase 7: Recursion**
    - Each synthesis creates new contradictions; the process repeats.
    - The README claims the real value emerges in **Rounds 2–3**, not Round 1.

- **Theoretical grounding**
  - **Venkatesh Rao / Electric Monks**
    - Reducing belief load is presented as a major way to speed cognition.
  - **Boyd / Destruction and Creation**
    - Claims you must break domains apart and recombine them to get genuine novelty.
    - Uses Gödel, Heisenberg, and entropy as arguments against purely inward refinement.
  - **Eisenstein / typographic fixity**
    - The printing press enabled side-by-side comparison; LLMs go further by automating structural comparison.
  - **Hegel**
    - **Determinate negation**: specific failure modes matter.
    - **Sublation**: a synthesis that makes the original debate obsolete.
  - **Christopher Alexander**
    - Natural systems are **semi-lattices**, not trees.
    - The skill aims to construct semi-lattice-like understanding from multiple linear arguments.
  - Additional references include:
    - **Socratic elenchus**
    - **Peirce’s abduction**
    - **Galinsky’s perspective-taking**
    - **multi-agent debate literature**
    - **Pollock’s defeasible reasoning**
    - **Aquinas**

- **Tone and intent**
  - The README is highly conceptual and ambitious, framing the skill as a tool for **deep reasoning**, not simple debate.
  - It explicitly warns that the first round is mostly calibration and that users should keep iterating.
  - It positions the user as a **co-pilot** who can interrupt and correct the process.

- **Other notable details**
  - The project is licensed under **MIT**.
  - The README includes a worked example path structure and command snippets for setup.
  - It emphasizes that the dialectic queue persists across sessions, making the process resumable.

### Assessment
This is a **mixed** content type: partly **tool/documentation**, partly **philosophical manifesto**, and partly **tutorial**. Durability is **medium**: the underlying ideas about dialectic reasoning, synthesis, and perspective-taking are fairly durable, but the implementation is tied to current agent workflows, Claude-style subagents, and the broader LLM ecosystem. Density is **high** because the README packs a lot of theoretical framing, workflow detail, and terminology into a single document. Originality is mostly **commentary/synthesis**: it assembles ideas from Rao, Boyd, Hegel, Alexander, Eisenstein, and others into one operating model rather than presenting new empirical research. It is best used as a **refer-back** reference if you want to understand or run the workflow; it is not a skim-once artifact because the phase structure, file layout, and theoretical rationale are likely the parts you’d revisit. Scrape quality is **good**: the content appears complete, including headings, usage instructions, theory sections, and code blocks, with no obvious missing sections beyond whatever may exist in the repository outside this README.
