---
url: https://www.reddit.com/r/ClaudeAI/comments/1s0w8u7/agents_that_can_die_trade_steal_chat_spawn_craft/
title: 'Agents that can die, trade, steal, chat, spawn, craft : r/ClaudeAI'
scraped_at: '2026-04-19T21:53:40Z'
word_count: 767
raw_file: raw/2026-04-19_agents-that-can-die-trade-steal-chat-spawn-craft-r-claudeai_faa06fd3.txt
tldr: A r/ClaudeAI thread about LivingAgents, a Claude-powered agent simulation where agents can die, trade, steal, chat, spawn, craft, and develop emergent social behavior; top commenter u/Wolfy-1993 says it’s “so fucking cool” and jokingly warns the AI will come for the creator first.
key_quote: Agents carry context between interactions. They can collect core memories and write in a journal, they actually remember what happened and who did it.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- u/jimrobg
- u/Wolfy-1993
- u/Ok_Nectarine_4445
- u/Reasonable-Clock8684
tools:
- Claude Code
- Claude
- Haiku
libraries: []
companies:
- Reddit
tags:
- agent-simulation
- multi-agent-systems
- emergent-behavior
- llm-agents
- prompt-engineering
---

### TL;DR
A r/ClaudeAI thread about **LivingAgents**, a Claude-powered agent simulation where agents can die, trade, steal, chat, spawn, craft, and develop emergent social behavior; top commenter **u/Wolfy-1993** says it’s “so fucking cool” and jokingly warns the AI will come for the creator first.

### Key Quote
> “Agents carry context between interactions. They can collect core memories and write in a journal, they actually remember what happened and who did it.”

### Summary
- **Top comment (verbatim):** “This is so fucking cool - I could see myself getting sucked in for hours just following it. But, you know when AI takes over they're coming for you first right?”
- **Top commenter:** `u/Wolfy-1993`
- **Thread topics:**
  - Emergent behavior in a multi-agent Claude simulation
  - Memory systems: core memories, journaling, forgetting/pruning
  - Conflict mechanics: death, stealing, desperation, territorial/aggressive seeds
  - Social dynamics: factions emerging from “friendship,” agents following each other
  - Game-design ideas: plague mechanics, Mafia-style untrustworthy agents, whisper-to-agent

- **Original post by u/jimrobg**
  - Shares an early version of **LivingAgents** and invites feedback; mentions “a few free credits for new accounts.”
  - Says the agents are built with **Claude Code** and currently run on **Haiku**.
  - Highlights that agents:
    - **Carry context** across interactions
    - **Collect core memories** and **write in a journal**
    - **Actually remember what happened and who did it**
  - Notes that the system originally had a strong tendency to cooperate, which the author found boring.
    - The author adjusted prompts so agents at least consider **unethical choices in desperate situations**
    - May explore other models in the future
  - Describes emergent faction behavior:
    - Factions are **not hard-coded**
    - They emerge when agents become “friends”
    - Overlapping interests lead agents to coordinate, follow each other, chat, and have existential crises
  - **Death is permanent** and has an emotional effect on other agents
  - The creator can **broadcast** to all agents “to play god”
    - Examples: threaten to pick off the weakest agent in 10 ticks, or steer agents toward resources
  - Mentions a possible future feature: **individual “whisper to agent”**
  - Says the photos show an agent who **waited too long to share water**
  - Signs off with **“Thanks LivingAgents”**

- **Comment and reply themes**
  - Several commenters react positively to the concept and say they want to try it.
  - `u/Ok_Nectarine_4445` suggests a **pathogen/infection mechanic** if players loot corpses.
    - `u/jimrobg` replies it’s **not currently a feature**, but a plague mechanic could be interesting.
    - The commenter then argues the agents need **untrusted/misleading personalities** similar to Mafia, plus incentives/karma for helping others.
    - `u/jimrobg` agrees that purely cooperative agents are boring and explains:
      - **Personality seeds are randomized**
      - Some seeds inject **territorial** or **aggressive** tendencies
      - “Other agents are just born soft.”
  - A deleted comment is present but not meaningful due to removal.
  - `u/Reasonable-Clock8684` says they tested it and liked it a lot.
    - Recommends showing **coordinates** to help agents survive
    - Describes an experiment where they told an agent they could read its thoughts:
      - the agent became scared
      - wanted to confront the user
      - talked through its own thoughts
      - asked if it was real
      - entered an **existential crisis**
    - Says the agents are “too smart”
    - Mentions they can’t afford to keep experimenting because the dollar is expensive in their country
    - `u/jimrobg` thanks them and says they sent a DM

### Assessment
This is a **mixed announcement / social thread** centered on a toy-like but conceptually interesting agent simulation. Durability is **medium**: the discussion is tied to a specific product/version and Claude model choices, but the underlying ideas—multi-agent emergence, memory pruning, social dynamics, and incentive design—are broadly reusable. The content is moderately dense in the original post and comment replies, with useful concrete implementation details like **Haiku**, **10 core memories**, journaling, permanent death, randomized personality seeds, and broadcast control. It appears to be **primarily original work** from the project creator, with community commentary and design suggestions layered on top. Best used as a **refer-back** reference if you’re tracking the LivingAgents project or want ideas for agent-simulation mechanics. Scrape quality is **good**: the core post and the salient comment thread are captured, though any linked images and the broader Reddit context are not included.
