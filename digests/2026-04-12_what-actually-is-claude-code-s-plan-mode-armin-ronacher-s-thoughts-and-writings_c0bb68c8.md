---
url: https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/
title: What Actually Is Claude Code’s Plan Mode? | Armin Ronacher's Thoughts and Writings
scraped_at: '2026-04-12T07:43:28Z'
word_count: 1917
raw_file: raw/2026-04-12_what-actually-is-claude-code-s-plan-mode-armin-ronacher-s-thoughts-and-writings_c0bb68c8.txt
tldr: Armin Ronacher explains that Claude Code’s “Plan Mode” is mostly a short, prompt-driven workflow wrapped around a hidden markdown plan file plus UI/harness behavior—not a fundamentally different planning system.
key_quote: Plan mode is just one of many examples where I think that because we are already so used to writing or talking to machines, bringing in more complexity in the user interface takes away some of the magic.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Armin Ronacher
- Peter
- Mario
tools:
- Claude Code
- Amp
- pi
libraries: []
companies: []
tags:
- agentic-workflows
- prompt-engineering
- developer-tools
- user-experience
- ai-agents
---

### TL;DR
Armin Ronacher explains that Claude Code’s “Plan Mode” is mostly a short, prompt-driven workflow wrapped around a hidden markdown plan file plus UI/harness behavior—not a fundamentally different planning system.

### Key Quote
"Plan mode is just one of many examples where I think that because we are already so used to writing or talking to machines, bringing in more complexity in the user interface takes away some of the magic."

### Summary
- **What the post is about**
  - A December 17, 2025 essay by Armin Ronacher about investigating Claude Code’s Plan Mode.
  - Motivated by curiosity after hearing others praise Plan Mode, despite the author usually working in “YOLO mode” with full permissions.

- **Author’s prior workflow**
  - He traditionally avoids Plan Mode because, in earlier Claude Code behavior, it did not inherit all tool permissions and kept asking for approvals.
  - Instead, he prefers a collaborative workflow:
    - the model asks clarifying questions
    - he answers them in an editor
    - they iterate until the result is acceptable
    - the handoff often happens through a markdown file

- **What Plan Mode actually appears to be**
  - A plan is essentially a **markdown file** written to Claude’s plans folder.
  - The plan itself has **no special structure beyond text**.
  - The main differences from a user manually prompting for a plan are:
    - recurring reminders that the agent is in **read-only mode**
    - a hidden file-based workflow for writing and later reading the plan
    - a prompt at exit time that tells the user the plan is ready for approval
  - The author says the tool seems to use the **edit file tool to modify its own plan file**.
  - Entering/exiting Plan Mode is itself treated as a **tool/state-machine flow**.

- **Prompt mechanics described in the post**
  - The injected prompt reinforces:
    - “Plan mode is active”
    - no edits, non-readonly tools, commits, or system changes are allowed
    - the plan file is the only editable file
  - It also provides a structured workflow with phases:
    - **Phase 1: Initial Understanding**
      - read code
      - ask questions
      - understand request and relevant files
    - **Phase 2: Design**
      - create an implementation approach
      - gather background context and filenames
      - request a detailed implementation plan
    - **Phase 3: Review**
      - review plans and align with user intent
      - read critical files
      - clarify ambiguities
    - **Phase 4: Final Plan**
      - write the final plan to the plan file
      - keep it concise but executable
      - include paths of critical files
  - Ronacher emphasizes that this is **short predefined prompt text**, not some large hidden mechanism.

- **What is and isn’t enforced**
  - He says he initially assumed the tools might truly become read-only, but concluded it is mostly:
    - prompt reinforcement
    - tool availability changes
    - workflow guidance
  - The “exit plan mode” tool is described as something to use only when planning code changes, not for research tasks.

- **His evaluation of the UX**
  - He sees Plan Mode as mostly:
    - a structured prompt
    - some system reminders
    - a few examples
  - He thinks much of the value could be replicated by a custom prompt alone, though not the exact UX.
  - The hidden file is useful because it can be edited and reviewed.
  - He values a disk file more than an integrated modal UI because it gives him more control and transparency.

- **Main thesis / takeaway**
  - The post argues that Claude Code’s Plan Mode feels special, but under the hood it is largely **prompt scaffolding plus workflow UI**, not deep magic.
  - The author is interested in the broader question of when agent UX must be enforced by the harness versus when it can emerge naturally from prompting alone.

### Assessment
This is a **mixed** piece: part firsthand technical inspection, part opinionated UX reflection. Durability is **medium-high** because the conceptual point about prompt scaffolding versus harness-enforced behavior is fairly timeless, but some implementation details are tied to Claude Code as of December 2025. Density is **medium**: it contains concrete observations about prompts, file behavior, and tool flow, but remains readable and reflective rather than deeply technical. Originality is **primary source / commentary**, since it reports the author’s own inspection of Claude Code and his interpretation of the UX. It’s best used as a **refer-back** piece if you care about agent workflow design, plan-mode UX, or how much behavior comes from prompts versus tooling. Scrape quality is **good**: the article text appears complete, including the closing footnote, though the actual prompt is summarized rather than reproduced verbatim.
