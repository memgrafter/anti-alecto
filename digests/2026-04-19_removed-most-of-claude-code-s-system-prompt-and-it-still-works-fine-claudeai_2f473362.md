---
url: https://www.reddit.com/r/ClaudeAI/comments/1odd0pw/removed_most_of_claude_codes_system_prompt_and_it/
title: 'Removed most of Claude Code’s system prompt and it still works fine : ClaudeAI'
scraped_at: '2026-04-19T21:27:05Z'
word_count: 2167
raw_file: raw/2026-04-19_removed-most-of-claude-code-s-system-prompt-and-it-still-works-fine-claudeai_2f473362.txt
tldr: r/ClaudeAI thread where `u/Dramatic_Squash_3502` reports shrinking Claude Code’s system prompt from 15.7k tokens to 6.1k and the TodoWrite tool description from 2,160 to 80 tokens, then asks whether the trimmed prompt still works; commenters debate prompt optimization, reliability, and whether smaller prompts hurt accuracy or speed.
key_quote: Got it trimmed from 15.7k (8%) to 6.1k tokens (3%).
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Dramatic_Squash_3502
- lucianw
- SpyMouseInTheHouse
- Odd_knock
- inventor_black
- Zulfiqaar
- ruloqs
- DanishWeddingCookie
- BankruptingBanks
- vigorthroughrigor
- realzequel
- rodaddy
- WildTechnomancer
- RadSwag21
tools:
- Claude Code
- tweakcc
- auto-compact
libraries: []
companies:
- Anthropic
- Piebald-AI
- bl-ue
tags:
- prompt-engineering
- claude-code
- system-prompts
- llm-optimization
- ai-agent-tools
---

### TL;DR
r/ClaudeAI thread where `u/Dramatic_Squash_3502` reports shrinking Claude Code’s system prompt from 15.7k tokens to 6.1k and the TodoWrite tool description from 2,160 to 80 tokens, then asks whether the trimmed prompt still works; commenters debate prompt optimization, reliability, and whether smaller prompts hurt accuracy or speed.

### Key Quote
“Got it trimmed from 15.7k (8%) to 6.1k tokens (3%).”

### Summary
- **Source / context**
  - Reddit thread in **r/ClaudeAI**
  - **Title:** “Removed most of Claude Code’s system prompt and it still works fine”
  - **Author:** `u/Dramatic_Squash_3502`
  - **Score:** 88, **comment count:** 43
  - The OP links to **tweakcc v2.0.0** and later to a public repo: **`bl-ue/tweakcc-system-prompts`**

- **Main claim from the OP**
  - `u/Dramatic_Squash_3502` says they used `tweakcc` to edit Claude Code’s system prompt.
  - They reduced the system prompt from **15.7k tokens (8%) to 6.1k tokens (3%)**.
  - They also trimmed the **TodoWrite** tool description from **2,160 tokens to 80 tokens**.
  - After testing “all morning,” they say it appears to be **working fine**.

- **Thread topics**
  - Whether Claude Code’s large system prompt is actually necessary
  - Risks of removing system instructions from first-party coding agents
  - Whether shorter prompts improve or hurt speed, reliability, and output quality
  - How to inspect / edit tool prompts with `tweakcc`
  - Whether system prompts are optimized for a model’s fine-tuning / reliability target
  - Auto-compact settings and token-cost management in Claude Code

- **Top comment (verbatim):** “I accidentally ran this experiment for about a week, about 1200 requests from many different people. (when I say "accidentally" I mean that a bug meant that Claude Code's system prompt was being dropped entirely). Results: removing Claude's system prompt caused P50 duration (TTLT) to increase from about 6s to 9s, and P75 to increase from 8s to 11.5s. Removing Claude's system prompt anecdotally increased its wordiness, e.g. in answer to "why is the sky blue?" its output was 30 lines rather than 5 lines. But I didn't see this in aggregate: it caused only an insignificant increase in number of output tokens, from P50 of 280 tokens to 290 tokens. Up until some time in September, Claude Code's system prompt used to have about fifty lines of text telling it to be terse, with lots of examples. They've replaced all those lines with just one single sentence, "Your responses should be short and co”
- **Top commenter:** `u/lucianw`

- **Key viewpoints**
  - **`u/lucianw`** says they accidentally ran a week-long real-world test where Claude Code’s system prompt was dropped entirely.
    - Reported results:
      - **P50 duration / TTLT:** about **6s → 9s**
      - **P75 duration:** about **8s → 11.5s**
      - Wordiness sometimes increased, but aggregate output token count barely changed:
        - **P50 output tokens:** about **280 → 290**
    - They also note Claude Code used to have a much longer terseness prompt, later replaced by a short instruction.
  - **`u/SpyMouseInTheHouse`** argues cutting system prompts is usually a bad idea.
    - Claims prompt/context engineering matters and that these instructions support alignment and accuracy.
    - Warns that “looking fine” may hide subtle regressions.
  - **`u/Odd_knock`** speculates Anthropic may optimize prompts for a reliability target and that a different workflow might not need the same prompt shape.
  - **`u/Zulfiqaar`** raises the concern that models may be fine-tuned against specific prompts, so deviating could reduce performance even if the prompt is shorter.
  - **`u/inventor_black`** asks for more testing and follow-up.
  - Several comments focus on practical usage: how to inspect prompts, disable auto-compact, and whether Claude should be terse or more expressive.

- **Notable follow-up from the OP**
  - `u/Dramatic_Squash_3502` says the trimmed prompt made Claude feel more like consumer Claude: **friendlier, more emojis, more tokens**.
  - After reading `u/lucianw`’s comment, they added a terseness instruction:
    - “Be very terse and concise. Do not use any niceties, greetings, pre/postfixes, pre/post ambles. Do not write any emoji.”
  - They report this made Claude Code feel “normal again” while keeping the prompt compact.

- **Concrete repo / tooling details**
  - OP says `tweakcc` extracts prompt components into text files under:
    - `~/.tweakcc/system-prompts`
  - They also say auto-compact can be disabled via:
    - `/config` → “Auto-compact”
  - These details are useful if someone wants to reproduce the experiment or inspect Claude Code’s prompt structure.

- **Experimental numbers mentioned later in the thread**
  - OP later says they ran a simple timing test with:
    - command: `claude –p “Please read the codebase, develop a thorough understanding of the said codebase, and then tell me all abou it.”`
    - comparison between **default system prompt** and **minimal custom prompt**
    - **29 runs each**
  - The reported result is **truncated in the scrape**, but the OP claims the minimal prompt was **about 24% faster**.
  - They also mention their longer task example:
    - about **24 Rust integration tests**
    - around **3k lines of code**
    - `> /cost` output showed **Total cost: $10.84**
    - **API duration:** `1h 5m 53s`
    - **wall duration:** `4h 40m 1s`
    - **2843 lines added, 294 removed**
  - Important: this is included, but the key timing claim is **incomplete/truncated** in the source scrape.

### Assessment
This is a **mixed** Reddit discussion with a practical experiment at the center and lots of commentary around prompt engineering, model behavior, and product design. **Durability is medium**: the specific Claude Code prompt lengths, model behavior, and `/config` details are tied to a particular product/version and may age quickly, but the broader debate about prompt trimming versus reliability is more lasting. **Density is medium-high** because it contains specific token counts, timing numbers, command paths, and a follow-up benchmark, though some of the most important timing evidence is truncated. **Originality is mixed**: the OP provides original anecdotal experimentation, while several top replies are commentary/speculation or a small amount of firsthand telemetry from `u/lucianw`. For **reference style**, this is best as **refer-back** if you care about Claude Code prompt tuning or system-prompt minimalism, and **skim-once** if you only want the general debate. **Scrape quality is partial**: the thread structure is mostly intact, but the top comment quote is cut off mid-sentence (“co…”), and the later “24% faster” benchmark is incomplete, so those are weaker as verification anchors than the OP’s main token-reduction claims.
