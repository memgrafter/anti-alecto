---
url: https://www.reddit.com/r/ClaudeAI/comments/1rzyqqt/found_3_instructions_in_anthropics_docs_that/
title: 'Found 3 instructions in Anthropic''s docs that dramatically reduce Claude''s hallucination. Most people don''t know they exist. : r/ClaudeAI'
scraped_at: '2026-04-19T21:54:39Z'
word_count: 2696
raw_file: raw/2026-04-19_found-3-instructions-in-anthropic-s-docs-that-dramatically-reduce-claude-s-hallu_ac1624d8.txt
tldr: A r/ClaudeAI thread by u/ColdPlankton9273 argues that three Anthropic doc instructions—let Claude say “I don’t know,” require citations, and use direct quotes for grounding—significantly reduce hallucinations, but commenters debate whether those guardrails should be default because they trade away creativity and cost more tokens.
key_quote: Allow Claude to say I don't know
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- ColdPlankton9273
- EdelinePenrose
- ClaudeAI-mod-bot
- iamgladiator
- fredjutsu
- xkcd327
tools:
- Claude
- Claude.md
- research mode
- ChatGPT
libraries: []
companies:
- Anthropic
tags:
- hallucination-reduction
- prompt-engineering
- claude-ai
- citations
- research-workflow
---

### TL;DR
A r/ClaudeAI thread by u/ColdPlankton9273 argues that three Anthropic doc instructions—let Claude say “I don’t know,” require citations, and use direct quotes for grounding—significantly reduce hallucinations, but commenters debate whether those guardrails should be default because they trade away creativity and cost more tokens.

### Key Quote
“Allow Claude to say I don't know”

### Summary
- **Top comment (verbatim):** "what is the difficulty for claude to internally always apply these guardrails and behaviors? i want to understand why anthropic is choosing to have the users manually include these guard rails."
- **Top commenter:** `u/EdelinePenrose`
- **Thread topics:**
  - Why Anthropic doesn’t make anti-hallucination guardrails default
  - How to implement a “research mode” / toggle in Claude
  - Tradeoff between factual accuracy and creativity
  - Whether citation grounding should be optional or always-on
  - Token/context costs of verification-heavy prompts

- OP says they found Anthropic’s “Reduce Hallucinations” docs and highlighted three system-prompt instructions:
  - **Allow Claude to say “I don’t know”** so it can admit uncertainty instead of filling gaps with plausible-sounding fiction.
  - **Verify with citations** so claims need a source; unsupported claims should be removed or retracted.
  - **Use direct quotes for factual grounding** so the model anchors on exact wording before summarizing or analyzing.
- OP says each instruction helps individually, but **all three together “fundamentally change the output quality.”**
- OP notes a cited tradeoff: **arXiv 2307.02185** reportedly found that strict citation constraints reduce creative output, so they don’t want these constraints always on.
- OP built a **toggle / “research mode”** to enable these instructions when they want grounded, source-backed answers and turn them off for freer generation.
- OP links to Anthropic’s docs page:  
  `https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations`
- OP later adds a repo for the mode toggle:  
  `https://github.com/assafkip/research-mode`

- **Main discussion pattern in comments:**
  - Many users agree the instructions are useful for fact-finding and research.
  - The biggest objection is that Anthropic should expose this as a built-in **mode switch** instead of making users discover and manually add it.
  - Several commenters argue the default behavior is intentionally more creative/helpful because these models serve broad consumer use cases, not just research.
  - Others say the lack of default grounding makes Claude too willing to invent answers when it lacks information.

- **Notable comment themes:**
  - **Why not default?**  
    - One top reply says the answer is the **tradeoff between accuracy and creativity**.
    - Another says forcing these rules on everyone would hurt users who want brainstorming, fiction, coding, or open-ended generation.
  - **How to use it?**  
    - Multiple commenters ask whether the instructions belong at the start of every conversation, in settings, or as a project-level instruction.
    - OP says they’ll package it into a skill/repo.
  - **Context/window concerns:**  
    - One user warns that Claude may not reliably follow `Claude.md` once the context window fills up.
  - **Token efficiency:**  
    - One commenter notes that verifying every claim with citations can consume more tokens and degrade performance.
    - Another suggests using smaller sub-agents for citation-finding to reduce cost.
  - **Practical use cases:**  
    - Users say the strict mode is good for documentation, note transcription, and fact-checking.
    - Others point out it can be too cautious for brainstorming or creative tasks.
  - **Extra refinement suggestion:**  
    - One commenter recommends adding “if you make an inference, label it explicitly as inference” to distinguish sourced facts from educated guesses.

- **Tone of the thread:**
  - Mostly positive toward the “research mode” idea.
  - The strongest disagreement is not whether hallucination reduction is useful, but **whether it should be universal or optional**.
  - Some comments drift into broader AI ethics / copyright arguments, but the core discussion remains about grounding, citations, and mode switching.

### Assessment
This is a high-density, current, mixed-content social thread: a practical user-discovery post with a strong product/workflow angle, plus a long comment debate about defaults, accuracy, creativity, and token cost. Durability is **medium** because the specific Anthropic docs, repo, and cited paper may age, but the underlying pattern—optional grounding modes versus general-purpose creativity—should remain relevant. It’s mostly **commentary** rather than primary research, though it includes a useful pointer to Anthropic’s docs and an arXiv reference. Good for **skimming and reference-back** if you want the exact prompts, the repo link, or the argument for a “research mode.” Scrape quality is **good**: the main post, prominent comments, and a long discussion sample are present, though this is still a thread capture rather than the full live discussion.
