---
url: https://www.youtube.com/watch?v=mS9Lr43cIB4
title: Terence Tao - Mathematics in the Age of AI - YouTube
scraped_at: '2026-04-19T08:38:13Z'
word_count: 3301
raw_file: raw/2026-04-19_terence-tao-mathematics-in-the-age-of-ai-youtube_3c312131.txt
tldr: Terence Tao argues that mathematics is only now beginning to change in the AI era, and that the most promising advances come from combining large language models with formal verification, modular collaboration, and new workflows that can scale from single problems to millions of formalized subproblems.
key_quote: Basically, we can only use the AI as far as you can trust his outputs or at least check them any further.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Terence Tao
- Cauchy
- Jessica Wyn
tools:
- GitHub
- Lean
- Alpha Evolve
- Google DeepMind
libraries: []
companies:
- UCLA
- Google DeepMind
tags:
- mathematics
- artificial-intelligence
- formal-verification
- collaborative-workflows
- theorem-proving
---

### TL;DR
Terence Tao argues that mathematics is only now beginning to change in the AI era, and that the most promising advances come from combining large language models with formal verification, modular collaboration, and new workflows that can scale from single problems to millions of formalized subproblems.

### Key Quote
“Basically, we can only use the AI as far as you can trust his outputs or at least check them any further.”

### Summary
- Tao frames mathematics as a historically conservative field:
  - The discipline still relies on ideas and proofs that are centuries or millennia old.
  - He contrasts a 200-year-old Cauchy textbook with modern graduate texts, arguing mathematics has extraordinary continuity.
  - Unlike many sciences, math still heavily uses blackboards and chalk, and collaboration levels have traditionally been much lower.

- He says mathematics is beginning to change because of new technologies, including AI:
  - Math is starting to adopt larger-scale, more collaborative workflows.
  - There is growing interest in “survey” style work over hundreds or thousands of problems rather than one-at-a-time case studies.
  - “Citizen mathematics” is emerging, similar to citizen science in other fields.

- The key enabler for AI-assisted math is formal verification:
  - Formal verification lets a computer check whether a proof is correct in a rigorous language.
  - This filters out unreliable or malformed contributions and breaks the trust barrier.
  - It allows anonymous or untrusted collaborators to contribute, as long as their work can be formally checked.

- Example 1: the “equational theories” project at UCLA:
  - Tao launched it last year with 50 collaborators, many of whom were not professional mathematicians.
  - The project procedurally generated 22 million algebra questions.
  - A typical example: whether commutativity implies associativity; answer: no.
  - The project was completed in three months, with every statement either proved or disproved.
  - Tools/workflow:
    - A shared GitHub repository
    - The Lean proof assistant
    - A discussion board for human proofs, computer-generated proofs, and translations between them
  - Why it worked:
    - Highly modular structure
    - Clear metric/progress measure
    - Decentralized, spontaneous participation
    - Precision enabled by formal verification
  - Tao stresses that basic collaboration tools like GitHub and discussion platforms were essential, not just advanced AI.

- Example 2: collaboration with Google DeepMind on AI-assisted math:
  - Tao describes large language models as increasingly powerful but unreliable.
  - They can solve Olympiad problems and answer deep questions, but also make basic arithmetic mistakes.
  - The promising approach is to pair the LM with a verifier that checks outputs and feeds back errors for correction.
  - He mentions a tool called Alpha Evolve.
  - Preliminary work has improved bounds in packing problems, such as finding better packings for 11 hexagons in a container.
  - He says this is still early, and more results on infinite-dimensional optimization problems are forthcoming.

- His broader conclusion about AI in mathematics:
  - AI is already useful for secondary tasks:
    - Writing computer code
    - Literature review
    - Translation between mathematical jargon and general/scientific language
  - There are early proof-of-concept systems that generate conjectures and detect patterns from data.
  - But advanced uses require rigorous verification; AI alone is too risky.
  - The most productive near-term use may be not replacing mathematicians on hard creative work, but using AI to clear the “long tail” of medium-difficulty problems and escalate only the hard ones to experts.
  - He argues AI should enlarge the set of feasible objectives rather than compete with human mathematicians for the same tasks.

### Assessment
This is a high-durability, mixed-content talk that is part opinion, part technical overview, and part announcement of ongoing research. The density is high because Tao moves quickly through a lot of specific examples, tools, and project structure, though some details are necessarily incomplete due to the talk format. It is primary-source material: Tao is describing his own work and perspective, not summarizing others. This is best used as a refer-back reference for understanding his view of AI’s role in mathematics, especially the importance of formal verification and collaborative workflows. Scrape quality is partial: the transcript captures the main spoken content well, but likely misses slides, visuals, exact terminology in places, and the full specifics of the unreleased DeepMind paper.
