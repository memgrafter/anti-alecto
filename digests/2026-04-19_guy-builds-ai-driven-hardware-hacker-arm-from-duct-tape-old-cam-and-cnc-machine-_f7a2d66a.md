---
url: https://news.ycombinator.com/item?id=47800033
title: Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine | Hacker News
scraped_at: '2026-04-19T22:05:59Z'
word_count: 2484
raw_file: raw/2026-04-19_guy-builds-ai-driven-hardware-hacker-arm-from-duct-tape-old-cam-and-cnc-machine-_f7a2d66a.txt
tldr: Hacker News thread on `gainsec/autoprober` (posted by `scaredpelican`, 224 points) debates whether the project is really just a flying-probe-style oscilloscope probe on a 3-axis CNC machine, and whether the “AI” does anything substantive beyond orchestrating the probe.
key_quote: How does this only have a single star.This is genuinely mind blowing.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- scaredpelican
- sanieldoe
- deanputney
- Unsponsoredio
- Animats
- chromacity
- numpad0
- uSoldering
- nullc
- claytonia
- kubizu
tools:
- autoprober
- Claude
- SPICE
- Huntron Access 2
- Proboter
libraries: []
companies:
- Hacker News
- Gainsec
- Schutzwerk
tags:
- flying-probe
- pcb-testing
- reverse-engineering
- ai-agents
- hardware-hacking
---

### TL;DR
Hacker News thread on `gainsec/autoprober` (posted by `scaredpelican`, 224 points) debates whether the project is really just a flying-probe-style oscilloscope probe on a 3-axis CNC machine, and whether the “AI” does anything substantive beyond orchestrating the probe.

### Key Quote
"How does this only have a single star.This is genuinely mind blowing."

### Summary
- **Thread context**
  - HN item ID `47800033`
  - Title: **“Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine”**
  - Posted by `scaredpelican`
  - Linked repo: `https://github.com/gainsec/autoprober`
  - 224 points, 21 top-level comments, 46 comments captured

- **Top comment (verbatim):** `"How does this only have a single star.This is genuinely mind blowing."`
- **Top commenter:** `u/scaredpelican`
- **Thread topics:**
  - Whether this is basically a **flying probe** setup built from a 3-axis CNC machine and oscilloscope probe
  - What the **AI** actually does: pin finding, ingestion of project data, probing, diagnosis, or just workflow orchestration
  - Whether the project is useful for **PCB testing**, **reverse engineering**, or both
  - Comparisons to **commercial flying-probe machines** and production test workflows
  - Concerns about **precision, reliability, and non-determinism** when an agent drives physical hardware

- **Main reaction in the thread**
  - Many commenters are impressed by the hacky hardware build and low-cost approach.
  - Several are skeptical or confused about the novelty, especially around the AI component.
  - A recurring theme is that the underlying hardware resembles an existing **flying probe** machine, which can already be bought commercially.

- **Supportive / impressed comments**
  - `u/sanieldoe`: “Limitation breeds creativity indeed”
  - `u/deanputney`: calls it “nuts” and wonders how much commercial flying-probe machines already do
  - `u/Unsponsoredio`: says the repo could be a strong CV signal and notes the cost ratio versus commercial setups (“under 500 bucks” vs. 5-figure proprietary systems)

- **Skeptical / clarifying comments**
  - `u/Animats` asks what the AI actually does, noting that a 3-axis CNC with an oscilloscope probe is basically a **flying probe**
  - `u/chromacity` says it feels like two different projects: PCB testing with an agent, and circuit reverse engineering
  - `u/numpad0` thinks the author may be overselling an “instant solution” to a research-team-sized problem
  - `u/uSoldering` argues the demo is misleading, saying real PCB photography/probing is hard and the video seems to show “photos of a photo being piped into an agent”

- **Technical points raised**
  - `u/nullc` suggests adding a spring-loaded linear sensor to maintain constant probe force
  - `u/_flux` asks how a single probe is useful; `u/s_m_t`, `u/Majromax`, and `u/SAI_Peregrinus` explain the ground/reference model of oscilloscope probing
  - `u/contingencies` and `u/Animats` discuss how production PCB tests are typically done with known nets, Gerbers, and continuity checks—often without AI
  - `u/claytonia` worries about the gap between probabilistic AI and sub-millimeter hardware precision

- **Related references mentioned in comments**
  - Commercial flying probe machines: `Huntron Access 2`
  - Open-source similar project: `Proboter` from Schutzwerk
  - A linked demo video is mentioned by several commenters, but the thread capture does not include the actual media

### Assessment
This is a **mixed** content thread: part praise, part technical skepticism, part meta-commentary on AI hardware demos. Durability is **medium** because the specific repo, demo, and HN discourse can age quickly as the project evolves, but the underlying questions about flying-probe testing, agent control of hardware, and what counts as “AI-driven” are fairly durable. Density is **medium-high**: the comments contain concrete references to flying-probe machines, PCB test workflows, ground/reference probing, and comparison to commercial tools, though much of the discussion is speculative because the thread capture does not fully show the project’s implementation. Originality is **commentary/synthesis** rather than a primary source; the thread mostly reacts to an external repo and demo. Reference style is **refer-back** if you want to recall the debate over whether the repo is a genuine hardware test innovation or just clever orchestration around an existing flying-probe idea. Scrape quality is **partial**: the HN text capture includes thread metadata and many comments, but not the underlying repo content, demo video, or images, so it cannot confirm whether the project actually performs the claimed probing behavior.
