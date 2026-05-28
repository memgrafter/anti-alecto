---
url: https://www.youtube.com/watch?v=Io_GqmbNBbY
title: DeepMind’s New AI Just Changed Science Forever - YouTube
scraped_at: '2026-04-19T07:43:48Z'
word_count: 1508
raw_file: raw/2026-04-19_deepmind-s-new-ai-just-changed-science-forever-youtube_3a401ca3.txt
tldr: Two Minute Papers summarizes DeepMind’s “Alethia” system, claiming it can help produce publishable research by combining a generator-verifier loop, longer reasoning, and search tools, with examples including four Erdős problems and co-authoring parts of new math papers.
key_quote: “now, it can help a person create publishable level research.”
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Dr. Karoly Zsolnai-Feher
- DeepMind
- Erdős
- Lambda
tools:
- Gemini Advanced
- Deep Think
- Alethia
- Google
- Lambda GPU Cloud
libraries: []
companies:
- DeepMind
- Lambda
tags:
- ai-research
- scientific-discovery
- machine-reasoning
- math-problems
- llm-tools
---

### TL;DR
Two Minute Papers summarizes DeepMind’s “Alethia” system, claiming it can help produce publishable research by combining a generator-verifier loop, longer reasoning, and search tools, with examples including four Erdős problems and co-authoring parts of new math papers.

### Key Quote
“now, it can help a person create publishable level research.”

### Summary
- This is a **Two Minute Papers** episode hosted by Dr. Karoly Zsolnai-Feher reacting to a DeepMind research result about an AI agent called **Alethia**.
- The core claim: the system can do **research on novel problems**, not just solve benchmark-style tasks.
- The episode contrasts:
  - **Math Olympiad problems**: hard, but constrained and solvable with known tools.
  - **Open research problems**: may be unsolved, possibly impossible, and have no training data.
- The method is described as a **generator + verifier** setup:
  - A generator proposes candidate solutions.
  - A verifier checks them and rejects bad ones.
  - Promising solutions are refined through repeated review/polish cycles.
- The speaker emphasizes why this is hard:
  - AI still hallucinates when pushed into genuinely novel territory.
  - Open research lacks labeled training data for “what works.”
- Three key implementation points are highlighted:
  - **Natural-language verification** rather than formal math-language checking.
  - **More compute / longer thinking**, with the claim that a stronger base model made the system about as smart as one from 6 months earlier but using **100x less compute**.
  - **Tool/search use**, including reading and combining information from many research papers without degenerating into nonsense.
- Reported results:
  - It reportedly solved **four open Erdős problems**.
  - It helped human scientists write parts of **five research papers** total.
  - Examples mentioned include work on **calculating constants in arithmetic geometry** and **finding new limits for interacting particles**.
- The video says the papers were checked by independent math experts and “it checks out,” while noting the work is still **submitted for peer review** and not yet fully finalized by publication standards.
- The host’s framing is strongly celebratory and forward-looking:
  - This is presented as a new level of AI-assisted science.
  - The episode suggests progress may soon move from “somewhat novel” to “ground-breaking” work, though that is still out of reach for now.
- The latter part of the transcript includes a **sponsor ad for Lambda GPU Cloud** and a mention of running the **DeepSeek AI model (671 billion parameters)** on Lambda infrastructure.

### Assessment
This is a **mixed** piece: part news/commentary, part promotional video, and part technical summary of a research claim. Durability is **medium**: the broad idea of AI-assisted research is likely to remain relevant, but the concrete capabilities, model names, and performance claims are tied to a specific moment in the field. Density is **medium**: there are several concrete facts and numbers, but they’re wrapped in enthusiastic narration and sponsor padding rather than presented as a clean technical breakdown. Originality is **commentary** rather than primary source; it summarizes and interprets a DeepMind development instead of presenting the research directly. Reference style is **skim-once** if you just want the headline takeaway, or **refer-back** if you want the specific claims about Alethia, Erdős problems, and compute efficiency. Scrape quality is **partial**: the transcript captures the spoken narration and sponsor plug, but not the underlying paper text, figures, citations, or any on-screen visuals that would help verify the claims more rigorously.
