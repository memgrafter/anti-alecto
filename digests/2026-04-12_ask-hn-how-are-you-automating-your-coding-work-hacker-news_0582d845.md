---
url: https://news.ycombinator.com/item?id=46710108
title: 'Ask HN: How are you automating your coding work? | Hacker News'
scraped_at: '2026-04-12T07:33:13Z'
word_count: 4254
raw_file: raw/2026-04-12_ask-hn-how-are-you-automating-your-coding-work-hacker-news_0582d845.txt
tldr: 'A Hacker News thread where developers compare how they use LLMs for coding: the strongest pattern is not “let the model write everything,” but codifying workflows into tests, scripts, docs, and guardrails so agents can check work quickly, while humans review more and learn to stop arguing with the model when manual fixes are faster.'
key_quote: The big mistake I see people make is not knowing when to quit.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Claude
- Gemini
- Mistral
- Toad
- OpenRouter
- Skyportal.ai
- Ralph
tools:
- Claude Code
- Cursor
- Gemini
- uv
- pytest
- Playwright
- agentbox
- open Dev
- MESA
- llvmpipe
- softpipe
- Copilot CLI
- Mistral Vibe
- Toad
libraries: []
companies:
- Hacker News
- OpenAI
- Google
- Anthropic
tags:
- ai-coding
- llm-workflows
- coding-agents
- test-driven-development
- code-review
---

### TL;DR
A Hacker News thread where developers compare how they use LLMs for coding: the strongest pattern is not “let the model write everything,” but codifying workflows into tests, scripts, docs, and guardrails so agents can check work quickly, while humans review more and learn to stop arguing with the model when manual fixes are faster.

### Key Quote
“**The big mistake I see people make is not knowing when to quit.**”

### Summary
- The thread centers on **practical coding-agent workflows** rather than hype: people describe using Claude Code, Cursor, Gemini, and API-based tooling to speed up implementation, review, and repo exploration.
- A recurring idea is **codification**:
  - Turn prompt-like instructions into **executable checks** rather than leaving them in context.
  - Example: write a `skill.md` into **hundreds of lines of code with a shebang**, so the model can run it as a script and see errors without carrying the whole explanation in context.
  - Use **TDD** as codification: one commenter proposes a **10ms timeout on every unit test** so the suite stays parallelizable and avoids I/O or slow hidden dependencies.
  - Another example: use a script to verify frontend code matches a **design system** before committing.
- Several commenters emphasize **“checkable” over “chatty”**:
  - Prefer existing linting/testing tools that return **exact, reusable messages**.
  - Avoid wasting context on instructions that can be enforced mechanically.
- A concrete workflow example:
  - One developer uses **Claude Code for web** with Python projects set up so **`uv run pytest`** runs cleanly.
  - They tell Claude to **run `uv run pytest`, then implement ...**, using the test suite as the work loop.
  - They use **Claude on an iPhone** to get much of an idea implemented before returning to a laptop.
- There’s a lot of **project-structure and metadata talk**:
  - People mention maintaining **`CLAUDE.md`**, **`AGENTS.md`**, and later **`SKILLS.md`** as evolving instruction files.
  - One person says they use Claude to write the spec, then let it run, and when context gets cramped have it build **SKILLS.md**; later it can rewrite **CLAUDE.md**.
  - Another says they prepare custom **AGENTS.md** with a wizard tool.
- A major theme is that **AI is most useful when the task is mechanical or bounded**:
  - “If I know what I want to code and it’s a purely mechanical exercise,” let Claude do it.
  - For unknown/ill-defined work, people still prefer reading code, sketching ideas, and thinking manually first.
  - Some use LLMs more like an **extra-smart pair reviewer**: “is it safe to pass null here?”, “can this function panic?”
- Multiple commenters stress the need to **know when to stop**:
  - A strong anecdote compares over-prompting to circling a parking lot for 15 minutes to find a close spot when the first spot would have been faster.
  - Another commenter says they spent too long trying to steer Gemini into fixing an inconsistency and should have just fixed it manually.
- The thread repeatedly warns that **agent output is not trustworthy enough to skip human review**:
  - “Every line of code was written by me even if it wasn’t written by me.”
  - People say they review all generated code and won’t commit anything they wouldn’t have written themselves.
  - Several commenters note that AI often rewrites code in ways that don’t match project conventions, misses deeper implications, or produces weak tests.
- There’s a broad consensus that **review work shifts rather than disappears**:
  - LLMs increase velocity, but often move effort from writing code to **reviewing code**, checking tests, and deciding when to hand-code.
  - One maintainer says AI has increased PR volume and bolder contributions, but code review does not scale indefinitely.
- A few commenters describe **tooling and environment setups**:
  - One uses a VM-based setup called **agentbox** with a dedicated container per project, multiple CLI agents, and a dashboard over tmux sessions.
  - Another mentions using **MESA/llvmpipe/softpipe** for software rendering in headless VMs.
  - One says they use a modified **open Dev** setup with OpenRouter and free models.
- There’s a split between **development help** and **ops / experimentation automation**:
  - One ML engineer uses an ops-side agent for spinning up systems, configuring ML stacks, running experiments, and collecting metrics.
  - Another commenter says AI helps them run experiments, inspect dependencies, and understand legacy codebases or incomplete docs.
- Some commenters are optimistic about **documentation and internal knowledge work**:
  - They automate doc updates after releases or big merges.
  - They use LLMs to explore dependencies, explain long error messages, or reconstruct how closed systems work.
- There is also skepticism and criticism:
  - Some say LLMs are **bad at assembly** and inconsistent on complex pointer-heavy or nontrivial code.
  - One commenter argues that the real bottleneck is still **trust and correctness**, not raw generation speed.
  - Another says AI-generated tests can become **technical debt** unless the task is extremely trivial and well-trodden.
- One durable meta-point: **LLMs work best when you already understand the desired shape of the solution**.
  - “Stay a step ahead of the automation” is echoed with an airplane/autopilot analogy: don’t let the agent run unattended without a mental model of where it’s going.
  - This is paired with the idea that current AI use is often less about writing and more about **directing, reviewing, and constraining**.

### Assessment
This is a **mixed** HN discussion with high practical density but uneven attribution and thread structure, so it’s best treated as a **reference** for recurring workflows and cautionary heuristics rather than a single authoritative tutorial. **Durability: medium** — the core advice about codifying checks, reviewing AI output, and knowing when to stop is likely durable, but the model/tool names (`Claude Code`, `Gemini Pro 3`, `Opus 4.5`, `uv run pytest`, `CLAUDE.md`, `SKILLS.md`) are version- and product-sensitive and may age quickly. **Content type: mixed** because it combines opinion, anecdote, and concrete workflow tips. **Density: high** — there are many specific examples, commands, and process patterns packed into the comments. **Originality: mixed** — mostly commentary and synthesis from multiple commenters, with some firsthand workflow reports rather than a single primary source argument. **Reference style: refer-back** — useful to revisit when designing AI-assisted coding workflows, repo guardrails, or review processes. **Recall/Decide/Evaluate/Find value:** high on recall and findability because the thread contains memorable anchors like “codification,” `uv run pytest`, and the parking-lot analogy; good for deciding whether to read deeper if you’re designing coding-agent workflows; moderate evaluation value because it reflects current practitioner sentiment but not systematic evidence. **Scrape quality: partial** — this is a raw comment dump without clear ordering, speaker labels, or thread context, and it likely omits the structure of the original HN conversation; that makes nuance, attribution, and reply chains harder to trust even though the text itself is rich.
