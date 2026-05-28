---
url: https://dynomight.net/more-chess/
title: https://dynomight.net/more-chess/
scraped_at: '2026-05-10T04:34:06Z'
word_count: 4217
raw_file: raw/2026-05-10_https-dynomight-net-more-chess_14bcd488.txt
tldr: Dynomight reports that recent OpenAI chat models can play much better chess than they first seemed to if prompted to “regurgitate” the whole move sequence and given a few examples, suggesting the gap with `gpt-3.5-turbo-instruct` is mostly about prompting/training format rather than a hard chess limitation.
key_quote: “If you do weird contortions to “trick” OpenAI chat models into behaving more like completion models, then they play much better.”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Dynomight
- OpenAI
- Daniel Gross
- Adam Karvonen
- Matthew Archer
- Nicholas Carlini
- Daniel Paleka
tools:
- Stockfish
libraries:
- llama-3.1-70b
companies:
- OpenAI
tags:
- llm-prompting
- chess
- instruction-tuning
- openai-models
- fine-tuning
---

### TL;DR
Dynomight reports that recent OpenAI chat models can play much better chess than they first seemed to if prompted to “regurgitate” the whole move sequence and given a few examples, suggesting the gap with `gpt-3.5-turbo-instruct` is mostly about prompting/training format rather than a hard chess limitation.

### Key Quote
“**If you do weird contortions to “trick” OpenAI chat models into behaving more like completion models, then they play much better.**”

### Summary
- The post revisits an earlier mystery: **why `gpt-3.5-turbo-instruct` plays chess surprisingly well** while newer chat models like `gpt-4o` and `gpt-4o-mini` initially look terrible.
- Dynomight argues against two popular explanations:
  - **OpenAI is cheating** by routing chess prompts to an external engine.
  - **LLMs can’t really play chess** and only memorize openings.
- Evidence against cheating:
  - `gpt-3.5-turbo-instruct` behaves differently depending on prompt wording and move history.
  - It is strong for an LLM, but still far below a chess engine.
  - Later OpenAI models can also improve substantially with the right prompting, which would be odd if only one model had a hidden chess-engine hook.
- Evidence that LLMs can play chess:
  - They rarely suggest illegal moves, even late in games.
  - They can handle **new board states** not seen in training examples.
  - The author says this is enough to reject the “they can’t play chess at all” view.

#### Baseline experiments
- Models were evaluated by having them continue games in **PGN-style notation** and play against **Stockfish**.
- `gpt-3.5-turbo-instruct` performed strongly.
- `gpt-4o` and `gpt-4o-mini` performed poorly under straightforward chat-style prompting.

#### Prompting experiments
- The author tests several ways to improve performance:
  - **Repeating the system prompt in the user prompt**
    - Small or unclear effect.
  - **Adding three in-context examples**
    - Huge improvement, especially surprising given how little data was added.
  - **Fine-tuning on 100 Stockfish self-play examples**
    - Helps.
  - **Combining examples + fine-tuning**
    - Strange interaction: examples help if fine-tuning is already present, but fine-tuning can hurt if examples are already present.
  - **Providing a list of legal moves**
    - Makes performance worse, not better.
- This is a recurring theme: **LLMs often improve with “completion-like” setups and degrade when over-constrained with extra explicit help**.

#### Main insight: “regurgitation”
- The most important trick was to prompt the model to:
  - **repeat the entire game so far**
  - then add **one new move**
- The idea is that this makes the model behave more like a **completion model** instead of a chat model.
- This improves `gpt-4o` and `gpt-4o-mini` notably.
- The author interprets this as evidence that the underlying base model is likely better at chess than the chat interface suggests.

#### Combined setup and comparison
- Best-performing recipe tested:
  - **regurgitation**
  - **examples**
  - other prompt additions mostly off
- Even then, `gpt-4o` still does **not fully match** `gpt-3.5-turbo-instruct`.
- In a 50-game match where `gpt-4o` (always white) played `gpt-3.5-turbo-instruct`:
  - **wins:** 10
  - **ties:** 5
  - **losses:** 35
- This was estimated as roughly **-191 Elo**, and after adjusting for white advantage, the author estimates the resulting setup around **1540 Elo**, still below `gpt-3.5-turbo-instruct`’s roughly **1750 Elo**.

#### Author’s theory
- Best guess:
  1. **OpenAI base models were trained on better/more curated chess data** than open models.
  2. **Instruction tuning/chat formatting weakens chess performance**, even if the base model would be strong.
- The author notes a possible clue from OpenAI literature: GPT-4 training reportedly included **PGN chess games filtered to players with Elo ≥ 1800**.
- For open models, the author suspects chess data is either less curated or less abundant.
- The post emphasizes that **prompt format matters enormously**, and the space of prompt/example/fine-tuning combinations is large and fragile.

#### Closing tone
- The post ends by framing this as a kind of **spell-casting / palace intrigue** problem rather than normal engineering.
- It links to prior chess-LLM work and includes updates correcting an earlier illegal move in an example.

### Assessment
This is a **mixed** technical/experimental essay with fairly high durability for its broader lessons about prompting, instruction tuning, and fragile LLM behavior, though the exact model-specific results are tied to the **Nov 2024** OpenAI API era and may age quickly as models change. The content is **high-density** and largely **primary-source commentary** based on the author’s experiments, not a neutral benchmark paper. It’s best treated as **refer-back** material if you care about LLM prompting, emergent chess ability, or OpenAI model behavior; the exact rankings and Elo estimates are likely to become stale, but the methodological point about chat-vs-completion behavior is more durable. Scrape quality is **good** overall: the article text, quoted prompts, results, and updates are present, though embedded charts/images are represented only as placeholders rather than fully rendered figures.
