---
url: https://news.ycombinator.com/item?id=46684958
title: 'Nanolang: A tiny experimental language designed to be targeted by coding LLMs | Hacker News'
scraped_at: '2026-04-19T21:32:57Z'
word_count: 3653
raw_file: raw/2026-04-19_nanolang-a-tiny-experimental-language-designed-to-be-targeted-by-coding-llms-hac_fe8b7fb3.txt
tldr: Hacker News discusses Nanolang, a tiny language built to be targeted by coding LLMs, and the thread mostly debates whether a custom language is actually better for LLMs than existing languages plus better tooling and constraints.
key_quote: One novel part here is every function is required to have tests that run at compile time.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: skim-once
scrape_quality: good
people:
- JamesTRexx
- Scramblejams
- Jordan Hubbard
- simonw
- spicybright
- abraxas
- thorum
- sheepscreek
- Claude Opus 4.5
- Claude Code
tools:
- Claude
- Claude Opus 4.5
- Claude Code
- llm
- nanolang
- nano
- toon
libraries: []
companies:
- NVIDIA
- FreeBSD
- GitHub
tags:
- large-language-models
- programming-languages
- ai-coding
- developer-tools
- hacker-news-discussion
---

### TL;DR
Hacker News discusses **Nanolang**, a tiny language built to be targeted by coding LLMs, and the top comment by **u/JamesTRexx** jokes that using it to clone the `nano` editor would require typing `nano nano.nano`, while the thread mostly debates whether a custom language is actually better for LLMs than existing languages plus better tooling and constraints.

### Key Quote
> "One novel part here is every function is required to have tests that run at compile time."

### Summary
- **Thread type:** Hacker News discussion of the GitHub project **jordanhubbard/nanolang**.
- **Author / score:** Posted by **Scramblejams**, with **232 points**, **25 top-level comments**, and **180 total comments** captured.
- **Top comment (verbatim):** "So, then if I want to use a certain terminal text editor to create a clone of it in nanolang, I'd end up typing nano nano.nano on the command line.I might accidentally summon a certain person from Ork."
- **Top commenter:** `u/JamesTRexx`

**Thread topics:**
- Whether a tiny, LLM-friendly language is actually useful
- The idea of requiring tests at compile time
- Whether LLMs do better with unfamiliar languages or just better-represented ones
- Tooling, grammar, and compiler feedback as the real bottleneck
- Broader speculation about AI-native programming languages

**Main discussion points:**
- Several commenters like the **clean / lisp-like syntax** and the design choice to reduce traps.
- A recurring claim is that **LLM performance depends more on training-data coverage and tooling** than on inventing a brand-new language.
- **u/spicybright** highlights the unusual feature that **every function must have tests that run at compile time**, but doubts that this alone justifies a custom language over something like **Lua** or **Python** with added constraints.
- **u/abraxas** suggests that a more **AST-like language**, perhaps a **strictly typed Lisp**, might be even better for LLMs.
- **u/thorum** notes that **Jordan Hubbard** developed the project and argues that language performance for LLMs likely scales with how much code in that language exists in training data.
- **u/simonw** reports an experiment: he found a `MEMORY.md` file in the repo, used it as a system prompt for **Claude Opus 4.5** to generate a **Mandelbrot fractal CLI tool**, and found the first attempt failed, but then **Claude Code** in the repo was able to fix the program.
- **u/sheepscreek** says the design feels clean and fewer-trap, but finds the mix of **s-expressions and imperative style** unusual; they also describe how agentic coding frees humans to explore more ambitious hobby projects.
- Some commenters argue the whole idea is a **dead end** or at least not the best short-term path, because:
  - LLMs are already strong at syntax when given the grammar
  - **existing languages** plus **better compiler feedback / tests / tooling** may matter more
  - agentic coding loops can bootstrap new languages from docs and examples
- There is a strong subthread arguing about whether **RL can help** with novel programming languages:
  - one side claims RL and verification can improve code generation
  - the other side says claims need evidence and that a brand-new language with almost no examples is not a solved training target
- A few commenters point to adjacent ideas:
  - **toon** as a JSON alternative with better LLM performance
  - transpilation / AST-to-AST layers to reuse existing language knowledge
  - future AI systems potentially inventing their own languages

**Overall tone:**
- Mostly skeptical but curious.
- The project is treated as an interesting experiment rather than an obviously practical breakthrough.
- The strongest consensus is that **feedback loops, compiler errors, and tooling** may matter more than the language’s novelty alone.

### Assessment
This is a **mixed** content thread: part project announcement, part technical debate, part speculative opinion. Durability is **medium**: the exact LLM/tooling arguments may age as models improve, but the broader question of whether custom languages help agents is likely to remain relevant. Density is **high** because the comments contain concrete examples, model names, repo files, and real workflows, though the discussion is also sprawling and repetitive in places. Originality is **mostly commentary / synthesis**, not primary research, with one notable first-hand experiment from **u/simonw**. This is best treated as **skim-once / refer-back** material: useful for understanding the discourse around LLM-friendly languages, but not a deep technical reference. Scrape quality is **good** for the thread structure and comments, though it’s still a capture rather than the full live page; any linked images, code, or external context from the GitHub repo and gist are not included here.
