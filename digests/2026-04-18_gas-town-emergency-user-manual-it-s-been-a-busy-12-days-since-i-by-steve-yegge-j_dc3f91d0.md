---
url: https://steve-yegge.medium.com/gas-town-emergency-user-manual-cf0e4556d74b
title: Gas Town Emergency User Manual. It’s been a busy 12 days since I… | by Steve Yegge | Jan, 2026 | Medium
scraped_at: '2026-04-18T05:02:52Z'
word_count: 3188
raw_file: raw/2026-04-18_gas-town-emergency-user-manual-it-s-been-a-busy-12-days-since-i-by-steve-yegge-j_dc3f91d0.txt
tldr: Steve Yegge’s “Gas Town Emergency User Manual” is a candid, highly specific field guide to using his still-rough AI agent orchestration system, focusing on how he manages work across the Mayor, crew, polecats, convoys, tmux, and PR sheriffs while warning that the software is not yet safe for general use.
key_quote: “Gas Town’s User Safety Index has been upgraded from ‘randomly rips user’s face off’ to ‘randomly kicks user in groin,’ which I think you’ll agree is still a good reason not to use it yet”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Steve Yegge
- Gene Kim
- Devin
tools:
- tmux
- Medium
libraries: []
companies:
- Gas Town
- Beads
tags:
- ai-agents
- workflow
- developer-tools
- tmux
- code-review
---

### TL;DR
Steve Yegge’s “Gas Town Emergency User Manual” is a candid, highly specific field guide to using his still-rough AI agent orchestration system, focusing on how he manages work across the Mayor, crew, polecats, convoys, tmux, and PR sheriffs while warning that the software is not yet safe for general use.

### Key Quote
“Gas Town’s User Safety Index has been upgraded from ‘randomly rips user’s face off’ to ‘randomly kicks user in groin,’ which I think you’ll agree is still a good reason not to use it yet”

### Summary
- Published Jan 13, 2026; framed as an “Emergency User Manual” about a very early, rapidly evolving Gas Town release.
- Yegge says Gas Town has accelerated quickly since launch:
  - over 100 PRs merged
  - nearly 50 contributors
  - 44k lines of code added
  - total size now 189k lines of Go code
  - 2,684 commits since Dec. 15
- He explicitly warns it is **not ready for general users**:
  - version 0.3.0 is described as “comparatively stable,” but still rough
  - mentions bugs like a “Serial Killer Murder Mystery” where stale-worker cleanup was incorrectly killing active crews
  - other issues include stalled workers, lost/orphaned workers, and “heresies” (wrong architectural beliefs that spread through the codebase)
- The post is organized around Yegge’s three-loop model from his **Vibe Coding** book with Gene Kim:
  - **Outer Loop**: days to weeks
  - **Middle Loop**: hours to days
  - **Inner Loop**: seconds to minutes
- **Outer Loop advice**
  - Upgrade Gas Town daily if experimenting or contributing
  - Learn `tmux`; it’s presented as essential for managing multiple agents
  - Bring your own workflow instead of expecting a fixed one
- **Middle Loop advice**
  - The **Mayor** is sufficient as a starting point and can file/fix issues or delegate
  - Entry points: `gt may at` and `gt crew at`
  - **Polecats** can work without the Refinery, Witness, or Deacon if tasks are well specified
  - It’s okay to run only one or two workers when blocked by serial dependencies
  - Run regular town cleanups for stale beads, workers, processes, and untracked files
- **Inner Loop advice**
  - Use **Convoys** for swarm work on well-defined, spec’d epics
  - Don’t watch agents work live; instead, read carefully when they finish and act on their results
  - Use `gt handoff` frequently to reset sessions after each task unless more context is needed
- **Crew workflow**
  - The post spends significant time on long-lived **Crew** members: named agents on each rig used for design, PR review, implementation planning, and code review
  - Yegge describes a setup with:
    - the Mayor in the center
    - Gas Town crew on one side
    - Beads crew on the other
  - Crew members are cycled through via tmux, given tasks one by one, and allowed to work independently
  - This is described as a “second workflow” beyond the Mayor/polecat convoy model
- **PR Sheriff**
  - A new ad-hoc role where a designated crew member automatically checks open PRs on startup
  - It splits them into easy wins vs. those needing human review
  - Easy PRs are slung to other crew for merging/cleanup
  - This automates a recurring maintenance sweep and keeps the system busy while the maintainer does other work
- **Invisible garden / quality control**
  - Because you don’t inspect all generated code directly, quality is maintained through repeated **code review sweeps** and **bug-fix sweeps**
  - Gas Town is framed as excelling at generating and then consuming lots of work in cycles
  - Persistent “heresies” are fought by encoding guiding principles in agent onboarding/priming
  - Examples of such principles include:
    - Zero Framework Cognition
    - GUPP
    - MEOW
    - Discovery over Tracking
    - Beads as the Universal Data Plane
- The closing tone is celebratory but cautionary:
  - early adopters are thanked for using it despite risk
  - Yegge says videos are coming soon
  - he implies the project is still unstable but is moving toward a real product

### Assessment
This is a **mixed** first-person technical/product essay with tutorial-like workflow guidance and a lot of promotional framing. Durability is **medium**: the general ideas about agent workflows, tmux-based orchestration, human-in-the-loop review, and swarm task decomposition are fairly timeless, but the specific commands (`gt may at`, `gt crew at`, `gt handoff`), roles, bugs, and version status are highly tied to the current Gas Town implementation as of Jan 2026. Density is **high** because it includes concrete operational advice, role names, commands, and architecture concepts, though it is also stylistically playful and repetitive in places. Originality is **primary source** since this is Yegge describing his own system and his own workflow. Reference style is best as **refer-back** if you’re using Gas Town or studying its workflow model, though a casual reader could skim it once for the conceptual structure. Scrape quality is **good** overall: the text content and structure are present, including headings and bullet points, but the embedded images themselves are not meaningfully captured beyond placeholders and captions.
