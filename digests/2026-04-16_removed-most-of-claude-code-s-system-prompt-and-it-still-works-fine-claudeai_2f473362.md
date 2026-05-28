---
url: https://www.reddit.com/r/ClaudeAI/comments/1odd0pw/removed_most_of_claude_codes_system_prompt_and_it/
title: 'Removed most of Claude Code’s system prompt and it still works fine : ClaudeAI'
scraped_at: '2026-04-16T06:28:36Z'
word_count: 2167
raw_file: raw/2026-04-16_removed-most-of-claude-code-s-system-prompt-and-it-still-works-fine-claudeai_2f473362.txt
tldr: A r/ClaudeAI thread where the OP says they trimmed Claude Code’s system prompt from 15.7k tokens to 6.1k with `tweakcc` and it still “works fine,” followed by a debate about whether removing system-prompt instructions improves, harms, or merely changes Claude Code’s behavior.
key_quote: “Got it trimmed from 15.7k (8%) to 6.1k tokens (3%).”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Dramatic_Squash_3502
- lucianw
- SpyMouseInTheHouse
- Odd_knock
- Zulfiqaar
- inventors_black
- hotpotato87
- count023
- vigorthroughrigor
- ruloqs
- DanishWeddingCookie
- portugese_fruit
- realzequel
- mrFunkyFireWizard
- rodaddy
- WildTechnomancer
- RadSwag21
tools:
- tweakcc
- Claude Code
- Task
- /config
- /cost
libraries: []
companies:
- Anthropic
- Piebald-AI
- Windsurf
tags:
- claude-code
- system-prompts
- prompt-engineering
- llm-evaluation
- developer-tools
---

### TL;DR
A r/ClaudeAI thread where the OP says they trimmed Claude Code’s system prompt from 15.7k tokens to 6.1k with `tweakcc` and it still “works fine,” followed by a debate about whether removing system-prompt instructions improves, harms, or merely changes Claude Code’s behavior.

### Key Quote
“Got it trimmed from 15.7k (8%) to 6.1k tokens (3%).”

### Summary
- **Original post by u/Dramatic_Squash_3502**
  - Says `tweakcc` v2.0.0 from the `Piebald-AI/tweakcc` project now supports editing Claude Code’s system prompt.
  - The OP experimented with aggressively shortening the prompt:
    - from **15.7k tokens (8%)** down to **6.1k tokens (3%)**
    - the **TodoWrite** tool description was cut from **2,160 tokens to 80 tokens**
  - Claims they tested it “all morning” and it was still “working fine.”
- **What “working fine” meant in the thread**
  - Later the OP clarified that Claude Code was still:
    - using todo lists correctly
    - using sub-agents / the **Task** tool correctly
    - completing long tasks, including a job they described as lasting **1+ hour**
  - The OP also said the reduced prompt made Claude feel **less stiff and formal** because tone instructions were removed.
- **Evidence / follow-up from u/lucianw**
  - A top comment says they had an accidental week-long experiment where Claude Code’s system prompt was dropped entirely because of a bug.
  - Reported results over about **1200 requests**:
    - **P50 duration (TTLT)** increased from about **6s to 9s**
    - **P75** increased from about **8s to 11.5s**
    - Claude became more verbose in some individual outputs, but aggregate output tokens changed only slightly:
      - **P50 output tokens** went from **280 to 290**
  - Lucian also notes Claude Code’s system prompt used to include many lines telling it to be terse, but by September this had reportedly been replaced with a single sentence.
- **Main objections / cautions in comments**
  - Several commenters argue that removing or simplifying system prompts is risky:
    - prompts may be tuned for reliability and alignment
    - models may be sensitive to wording changes
    - deleting instructions can degrade performance in subtle ways even if behavior “looks fine”
  - One commenter emphasizes that prompt/context engineering matters and that system prompts are not just token bloat.
- **Speculation about optimization**
  - A commenter wonders whether Anthropic has already optimized the prompts for a target reliability.
  - Another points out that first-party coding agents may depend on prompts that were specifically paired with training/fine-tuning.
- **Useful concrete tips surfaced in the thread**
  - `tweakcc` can extract Claude Code system-prompt components into files under:
    - `~/.tweakcc/system-prompts`
  - To disable auto-compact:
    - run `/config`
    - find **“Auto-compact enabled”**
  - The OP later linked a repo for their minimal prompt experiments:
    - `https://github.com/bl-ue/tweakcc-system-prompts`
- **Example task and cost data from the OP**
  - The OP cited a long coding task involving:
    - **24 integration tests in Rust**
    - roughly **3k lines of code**
  - They pasted a `/cost` summary showing:
    - **Total cost: $10.84**
    - **Total duration (API): 1h 5m 53s**
    - **Total duration (wall): 4h 40m 1s**
    - **2843 lines added, 294 removed**
- **Other side discussions**
  - One user says using a smaller model like **Haiku 4.5** outperformed Sonnet 4.5 for a particular refactor, while another pushes back that smaller models generally have less reasoning capacity.
  - A thread also discusses whether “under engineering” vs “overengineering” applies when simplifying system prompts.

### Assessment
This is a **mixed** Reddit discussion: part anecdotal experiment report, part technical debate, part community troubleshooting. **Durability: medium** — it is tied to Claude Code, `tweakcc`, and specific prompt behavior that may change with future versions, though the broader lesson about prompt sensitivity is longer-lived. **Content type: mixed** rather than a clean tutorial or research note. **Density: medium-high** because the OP provides token counts, tool names, timing claims, and later follow-up measurements, while commenters add several distinct viewpoints. **Originality: mostly commentary with some primary-source anecdote** — the OP’s own experiment and the lucianw telemetry report are original observations, but the thread overall is still discussion rather than a formal study. **Reference style: refer-back** if you want the exact tool names, prompt sizes, and the `/config` auto-compact tip; otherwise skim-once. **Scrape quality: partial** — the capture includes the OP, prominent comments, and a discussion sample, but as with most Reddit thread captures, lower-ranking replies, full nested context, and any removed content may be incomplete.
