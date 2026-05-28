---
url: https://x.com/doodlestein/status/2041660563005100220
title: 'Jeffrey Emanuel on X: "A while back, I posted this concept for my ntm agent orchestration tool that would let you spin up a swarm of agents using various harnesses where each agent could follow a different "mode of reasoning" (see the quoted post for what that means). I didn''t really do much with it https://t.co/X1Wwh71TZX" / X'
scraped_at: '2026-04-19T07:30:31Z'
word_count: 804
raw_file: raw/2026-04-19_jeffrey-emanuel-on-x-a-while-back-i-posted-this-concept-for-my-ntm-agent-orchest_2b48adcf.txt
tldr: Jeffrey Emanuel describes an NTM-based multi-agent analysis system that spawns a swarm of AI agents, each constrained to a different reasoning mode, then synthesizes their findings into a structured “fresh eyes” review of a project.
key_quote: “a single analytical perspective has blind spots. Multiple independent perspectives triangulate toward truth.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Jeffrey Emanuel
- Claude
- Claude Code
tools:
- ntm
- Claude Code
libraries: []
companies:
- X
tags:
- multi-agent-systems
- ai-orchestration
- reasoning-modes
- software-analysis
- epistemology
---

### TL;DR
Jeffrey Emanuel describes an NTM-based multi-agent analysis system that spawns a swarm of AI agents, each constrained to a different reasoning mode, then synthesizes their findings into a structured “fresh eyes” review of a project.

### Key Quote
“a single analytical perspective has blind spots. Multiple independent perspectives triangulate toward truth.”

### Summary
- This X post is a product/concept update about **ntm**, Jeffrey Emanuel’s **tmux-based multi-agent orchestrator**.
- The core idea: instead of asking one AI to review a project, the system:
  - profiles the target project,
  - selects a set of reasoning modes from a taxonomy of about **80 modes**,
  - launches a **swarm of agents**,
  - constrains each agent to reason in one mode,
  - then **synthesizes** their outputs into a markdown report.
- The author says this finally became practical after realizing a **Claude Code skill** could serve as the interface:
  - you ask Claude Code to invoke `/modes-of-reasoning-project-analysis`,
  - a “lead agent” studies the project,
  - it selects the most relevant and complementary modes,
  - and then manages the swarm through ntm.
- The system is meant to create a kind of **“fresh eyes review on steroids”** or a forced **gestalt shift**, so each agent notices things a single perspective would miss.
- Claude’s own summary in the post breaks the process into **7 phases**:
  1. **Context Pack** — profile structure, tech stack, maturity
  2. **Mode Selection** — choose 10 modes from 7 taxonomy axes
  3. **Spawn Swarm** — launch agents via NTM
  4. **Dispatch Prompts** — give each agent a mode-specific constraint
  5. **Monitor** — watch convergence / early stopping
  6. **Score & Collect** — each agent returns structured findings
  7. **Synthesize** — classify results by confidence:
     - **Kernel**: 3+ modes agree
     - **Supported**: 2 modes agree
     - **Hypothesis**: 1 mode only
     - **Disputed**: disagreement requiring resolution
- Claimed benefits and use cases:
  - **Pre-release audits**: adversarial, probabilistic, and ethical checks before shipping
  - **Architecture decisions**: compare tradeoffs through different reasoning lenses
  - **Breaking groupthink**: surface objections via a “Kill Thesis” operator card
  - **Due diligence**: inspect unfamiliar codebases or projects from multiple angles
  - **Finding unknown unknowns**: a “Blind Spot Scan” asks what underrepresented reasoning axes would reveal
- The differentiator, per the post, is **structured epistemic diversity**:
  - not multiple agents repeating the same review,
  - but agents cognitively constrained to different reasoning styles,
  - with a formal synthesis protocol tracking agreement, disagreement, and blind spots.
- The post also includes screenshots and a quoted earlier post teasing “wild stuff” for ntm.

### Assessment
This is a **mixed** content type: part product announcement, part technical concept pitch, part explanatory demo. Durability is **medium** because the underlying idea of multi-perspective analysis is fairly timeless, but the specifics are tied to current tools like **Claude Code**, **ntm**, and the author’s own skill/site, so it could age as the tooling evolves. Density is **medium-high** since it contains a fairly elaborate system description, named phases, taxonomy counts, and example use cases, though it is still promotional and conceptual rather than implementation-heavy. Originality is mostly **primary source**: it presents the author’s own system and framing, with some AI-generated explanation embedded. Reference style is **refer-back** if you’re interested in agent orchestration, swarm workflows, or reasoning-mode taxonomies; otherwise **skim-once**. Scrape quality is **partial**: the text capture includes the main conversation and quoted summary, but the images/screenshots themselves are not visible here, so any visual details from the post are missing.
