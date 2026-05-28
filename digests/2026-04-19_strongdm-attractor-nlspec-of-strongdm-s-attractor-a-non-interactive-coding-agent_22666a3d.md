---
url: https://github.com/strongdm/attractor
title: 'strongdm/attractor: nlspec of StrongDM''s Attractor, a non-interactive Coding Agent sufficient for use in a Software Factory'
scraped_at: '2026-04-19T07:09:14Z'
word_count: 113
raw_file: raw/2026-04-19_strongdm-attractor-nlspec-of-strongdm-s-attractor-a-non-interactive-coding-agent_22666a3d.txt
tldr: This repo is a meta-specification for building “Attractor,” StrongDM’s non-interactive coding agent, and points readers to three NLSpec documents plus a one-line prompt for asking a modern coding agent to implement it.
key_quote: 'NLSpec (Natural Language Spec): a human-readable spec intended to be directly usable by coding agents to implement/validate behavior.'
durability: medium
content_type: reference
density: low
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Claude Code
- Codex
- OpenCode
- Amp
- Cursor
libraries: []
companies:
- StrongDM
tags:
- coding-agents
- natural-language-specs
- software-factory
- llm-tools
- specification
---

### TL;DR
This repo is a meta-specification for building “Attractor,” StrongDM’s non-interactive coding agent, and points readers to three NLSpec documents plus a one-line prompt for asking a modern coding agent to implement it.

### Key Quote
"NLSpec (Natural Language Spec): a human-readable spec intended to be directly usable by coding agents to implement/validate behavior."

### Summary
- The repository is not the implementation of Attractor itself; it contains **NLSpecs** intended to describe how to build a similar system.
- Its stated goal is to help you build “your own version of Attractor” to create “your own software factory.”
- It notes that bringing your own:
  - **agentic loop**
  - **unified LLM SDK**
  
  is **not required**, but is **highly recommended** so you can “control the stack” and have a “strong foundation.”
- The repo links to three specification documents:
  - **Attractor Specification** (`./attractor-spec.md`)
  - **Coding Agent Loop Specification** (`./coding-agent-loop-spec.md`)
  - **Unified LLM Client Specification** (`./unified-llm-spec.md`)
- It gives a direct prompt for a modern coding agent:
  - `codeagent> Implement Attractor as described by https://github.com/strongdm/attractor`
- Terminology section defines **NLSpec** as a human-readable spec that coding agents can directly use to implement or validate behavior.

### Assessment
Durability is **medium**: the concept of a natural-language spec for coding agents is fairly durable, but the guidance is tied to current agent tooling and the repo’s specific Attractor framing. Content type is **reference** with a light **tutorial** flavor, since it mainly points to related specs and gives an implementation prompt. Density is **low**: the page is short and mostly organizational, with very little technical detail beyond the document names and the NLSpec definition. Originality is **primary source**, since this is the project’s own description of its specs and purpose. Reference style is **refer-back** if you’re interested in the linked spec docs or the Attractor concept itself; otherwise it’s mostly a skim-once landing page. Scrape quality is **good**: the text captured appears complete for this page, though the linked markdown spec contents are not included here.
