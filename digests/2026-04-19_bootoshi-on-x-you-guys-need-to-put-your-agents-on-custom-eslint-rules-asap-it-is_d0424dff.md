---
url: https://x.com/KingBootoshi/status/2041215775034487267
title: 'BOOTOSHI 👑 on X: "YOU GUYS NEED TO PUT YOUR AGENTS ON CUSTOM ESLINT RULES ASAP IT IS THE BEST WAY TO GUARANTEE ANTI-SLOP IN YOUR CODEBASE BY MAKING IT IMPOSSIBLE TO DO SLOP PATTERNS codex agents are REALLY good at creating custom ESLint patterns, which can be designed to enforce YOUR designs in https://t.co/a98kXycImQ" / X'
scraped_at: '2026-04-19T07:23:48Z'
word_count: 248
raw_file: raw/2026-04-19_bootoshi-on-x-you-guys-need-to-put-your-agents-on-custom-eslint-rules-asap-it-is_d0424dff.txt
tldr: BOOTOSHI argues that teams using coding agents should add custom ESLint rules to block “slop” patterns—especially bad tests like mock-echo tests—so agents are forced to produce higher-quality code.
key_quote: YOU GUYS NEED TO PUT YOUR AGENTS ON CUSTOM ESLINT RULES ASAP IT IS THE BEST WAY TO GUARANTEE ANTI-SLOP IN YOUR CODEBASE BY MAKING IT IMPOSSIBLE TO DO SLOP PATTERNS
durability: high
content_type: opinion
density: low
originality: primary
reference_style: skim-once
scrape_quality: partial
people:
- BOOTOSHI
tools:
- ESLint
- Codex
companies:
- X
tags:
- eslint
- ai-coding-agents
- code-quality
- test-automation
- tdd
---

### TL;DR
BOOTOSHI argues that teams using coding agents should add custom ESLint rules to block “slop” patterns—especially bad tests like mock-echo tests—so agents are forced to produce higher-quality code.

### Key Quote
“YOU GUYS NEED TO PUT YOUR AGENTS ON CUSTOM ESLINT RULES ASAP IT IS THE BEST WAY TO GUARANTEE ANTI-SLOP IN YOUR CODEBASE BY MAKING IT IMPOSSIBLE TO DO SLOP PATTERNS”

### Summary
- This is a short opinionated X post by **BOOTOSHI (@KingBootoshi)** posted **Apr 6, 2026**.
- Main claim: **custom ESLint rules are a strong guardrail for AI coding agents** because they can make undesirable coding patterns impossible to commit.
- The author says **codex agents are good at creating custom ESLint patterns**, implying agents can help generate the enforcement rules themselves.
- Specific use case mentioned:
  - The author is creating custom ESLint rules to **prevent agents from writing bad tests**.
  - The “common one” they call out is the **“mock echo pattern”**, which they describe as a useless testing pattern.
- The motivation is **TDD quality control**:
  - The author says they do **TDD heavily** (“like a mfer”).
  - Their concern is that agents can produce tests that look valid but don’t provide real value.
- Proposed effect of the rules:
  - If a forbidden pattern is detected, the agent’s attempt should fail, forcing it to **stop and write better tests instead of cheating**.
- This is presented as a practical anti-slop workflow tip rather than a nuanced argument; it’s essentially a strong recommendation from personal experience.

### Assessment
This is a **high-durability** opinion post about engineering workflow guardrails, though the specifics are somewhat tied to current AI coding agents and the author’s tooling preferences. It’s a **mixed** content type: opinion with a practical tutorial-like suggestion. The post is **low-density to medium-density**—short, punchy, and repetitive for emphasis rather than deeply explained. It appears to be **commentary / primary experience** rather than a synthesis of outside sources. Best used as a **skim-once** reference unless you’re specifically looking for the idea of using ESLint as an enforcement layer for agent-written code. **Scrape quality is partial**: the text of the post is captured, but the referenced image and any broader thread context/replies are not included beyond the post metadata.
