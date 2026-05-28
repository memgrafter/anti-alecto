---
url: https://dylanbutler.dev/blog/protect-your-shed/
title: Protect Your Shed | @dbut2
scraped_at: '2026-04-19T07:30:42Z'
word_count: 1035
raw_file: raw/2026-04-19_protect-your-shed-dbut2_6ee6ea4b.txt
tldr: The article argues that enterprise engineering teaches scale and reliability, but personal side projects are essential for staying curious, experimenting freely, and avoiding burnout.
key_quote: Protect your personal projects at all costs.
durability: high
content_type: opinion
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Dylan Butler
tools:
- Cloud Spanner
- Go
- GCP
libraries: []
companies: []
tags:
- software-engineering
- side-projects
- career-growth
- burnout
- experimentation
---

### TL;DR
The article argues that enterprise engineering teaches scale and reliability, but personal side projects are essential for staying curious, experimenting freely, and avoiding burnout.

### Key Quote
"Protect your personal projects at all costs."

### Summary
- Uses a **skyscraper vs. backyard shed** metaphor:
  - **Skyscraper** = enterprise software: permits, design reviews, testing, coordination, scale, rigor.
  - **Shed** = personal projects: fast, informal, experimental, self-directed.
- The author says their **six years as an engineer** were split between:
  - **Day job**: building banking systems at enterprise scale.
  - **Night projects**: side projects and homelab tinkering.
- Main thesis:
  - The **enterprise work taught structural discipline, defensive design, and how to engineer at scale**.
  - The **personal projects kept them motivated, curious, and still feeling like an engineer**.
- On large-scale engineering:
  - A lot of the work is not coding, but **design docs, test plans, and architecture reviews**.
  - Working with systems like **Cloud Spanner** gave exposure to **globally distributed, strongly consistent databases** that can’t really be simulated on a laptop.
  - Scale teaches you to think about **failure modes before features**.
  - The downside is **rigidity**: limited freedom to choose tools or experiment with foundations.
- On side projects:
  - Early side projects were “messy” and unstructured, but over time they absorbed patterns from work.
  - Example: a **homelab** that evolved from **a single container on a single machine** into **a managed cluster with automated deployments and infrastructure as code**.
  - Side projects let the author apply enterprise-grade discipline in a context with total freedom.
- On experimentation:
  - Building for yourself makes mistakes cheap: the cost of failure is usually **a wasted evening**, not customer impact.
  - The author built a **Game Boy Advance emulator in Go** to learn how hardware works.
  - They also tried unfamiliar tools and services outside work to understand tradeoffs without needing approval.
  - Most experiments did **not** become startup ideas, but they produced:
    - new patterns
    - lessons in what not to do
    - broader technical awareness
- On motivation and burnout:
  - Enterprise work can become repetitive and draining.
  - Side projects keep software development feeling **fun** and preserve the builder identity.
  - The author argues that without personal projects, engineers risk becoming only employees executing business needs.
- On transfer of learning:
  - Skills learned in the “shed” can later inform workplace decisions.
  - The author gives an example of learning **containerization and cloud infrastructure on GCP at home**, which helped them ramp up faster at work.
  - Trying tools independently first means you can later make **informed judgments instead of guesses**.
- Final message:
  - Don’t treat your day job as your entire craft.
  - **Protect your personal projects** because they sustain curiosity, experimentation, and long-term love of building software.

### Assessment
This is a high-level **opinion/essay** with a strong personal-reflection angle rather than a technical tutorial. Its **durability is high** because the core ideas—side projects, burnout, learning through experimentation, and scale vs. freedom—are broadly timeless, though some examples (like Cloud Spanner, GCP, and containerization workflows) are tied to contemporary engineering practices. The **density is medium**: it is readable and narrative-driven, but still includes concrete examples such as a homelab, a Game Boy Advance emulator in Go, and Cloud Spanner. It is **original commentary** based on the author’s own experience, not a synthesis of external sources. Best treated as **refer-back** reading for motivation and career perspective rather than deep technical study. **Scrape quality is good**: the full article text appears captured, with no obvious missing sections, code blocks, or media.
