---
url: https://lobste.rs/s/kvvxkl/enclosure_feedback_loop_how_llms
title: The Enclosure feedback loop, or how LLMs sabotage existing programming practices by privatizing a public good | Lobsters
scraped_at: '2026-04-12T10:33:29Z'
word_count: 2749
raw_file: raw/2026-04-12_the-enclosure-feedback-loop-or-how-llms-sabotage-existing-programming-practices-_64352c94.txt
tldr: 'The thread argues that LLMs create an “enclosure feedback loop”: private chatbot debugging sessions generate proprietary training data, which makes corporate models better and open alternatives weaker, shrinking the programming commons over time.'
key_quote: “LLMs are a power transfer mechanism.”
durability: high
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Sam Altman
- Simon
- Michiel
tools:
- Claude Code
- Codex CLI
- grep
- strace
- xyproblem.info
- Google Books
- Stack Overflow for Teams
companies:
- Stack Overflow
- Anthropic
- OpenAI
- Google
- Bing
- DuckDuckGo
- Reddit
- Discord
- Telegram
- Mercor
- Outlier
tags:
- llms
- programming-communities
- data-enclosure
- open-source
- training-data
---

### TL;DR
The thread argues that LLMs create an “enclosure feedback loop”: private chatbot debugging sessions generate proprietary training data, which makes corporate models better and open alternatives weaker, shrinking the programming commons over time.

### Key Quote
“LLMs are a power transfer mechanism.”

### Summary
- This Lobsters thread discusses an article about how LLMs may be “sabotaging existing programming practices” by privatizing what used to be public learning and support spaces.
- Core thesis repeated throughout the discussion:
  - Stack Overflow and similar public Q&A spaces once acted as a semi-commons for programming knowledge.
  - As people move debugging and help-seeking into private, corporate chatbot sessions, those interactions become hidden, proprietary training data.
  - That creates a feedback loop: better private models attract more use, which yields more training data, which makes them even better.
  - Open models and public knowledge bases lose relative competitiveness because they do not get equivalent access to this fresh interaction data.
- Several commenters frame this as an “enclosure” problem:
  - Not just loss of access to information, but loss of the social/public infrastructure that generated and refined it.
  - One commenter explicitly connects it to “intellectual sovereignty” and says, “AI is a power transfer mechanism.”
- There is debate over whether Stack Overflow was actually the key data source:
  - Some argue LLMs no longer need Stack Overflow specifically because they can inspect codebases directly, run tools like `grep`, `strace`, and even test binaries or libraries through coding agents.
  - Others respond that the issue is not model capability but ownership: the old public corpus mattered because it was public; even if models can now explore code on their own, the resulting private interactions still intensify enclosure.
- Human-run public help spaces are contrasted with LLMs:
  - LLMs are described as instant, helpful, and polite, but also sycophantic or too agreeable.
  - Some participants argue human systems need the ability to say “no,” criticize unethical ideas, or push back on bad engineering choices.
  - Others worry commercial and open model operators alike may not have trustworthy ethical judgment.
- The thread also touches on moderation and community dynamics:
  - Stack Overflow is described as optimized for searchable answers rather than directly helping askers.
  - Its governance and moderation made it a public resource, but also contributed to hostility that pushed people elsewhere.
  - People note that programming communities had already been moving toward Slack, Discord, and other “walled garden” spaces before LLMs.
- The conversation explores whether Stack Overflow-style content is still essential:
  - Some think modern coding agents can answer hard questions by exploring repositories and executing experiments, even without direct training examples for every new library.
  - Others counter that software knowledge still evolves, and future tools will need some source of fresh human knowledge, blogs, bug trackers, and public discussion.
- There are side references to:
  - “training copyleft” as a proposed response: allow LLM training on code, but require resulting models to be free software.
  - Google search and “enshittification” as an analogy for feedback loops and competitive advantage.
  - Outsourced human experts being paid to generate or refine coding training data for model companies.

### Assessment
This is a high-durability **mixed** discussion: the specific references to current model behavior, Stack Overflow, and recent training practices are time-sensitive, but the broader ideas about enclosure, network effects, and commons-vs-platform control are durable. The thread is **commentary/opinion** rather than a primary research source, though it cites practical observations from current coding-agent workflows. It is fairly **dense** in arguments and examples, but uneven because it is a fragmented comment thread with some tangents. For later use, it’s best as a **refer-back** item: useful for recalling the main enclosure/feedback-loop thesis and the main counterarguments, not for authoritative factual grounding. **Scrape quality is partial**: this is clearly a stitched-together fragment of comments, with missing context, missing parent posts, and no original article body visible here, so confidence in completeness is limited.
