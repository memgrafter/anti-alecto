---
url: https://github.com/cyxzdev/Uncodixfy/blob/main/SKILL.md
title: Uncodixfy/SKILL.md at main · cyxzdev/Uncodixfy
scraped_at: '2026-04-19T06:49:36Z'
word_count: 1900
raw_file: raw/2026-04-19_uncodixfy-skill-md-at-main-cyxzdev-uncodixfy_fca16e5a.txt
tldr: Uncodixfy is a style guide for making AI-generated frontend UI look less “AI” by banning common dashboard tropes and pushing for plain, functional, human-designed layouts.
key_quote: This document exists to teach you how to act as non-Codex as possible when building UI.
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries: []
companies:
- Linear
- Raycast
- Stripe
- GitHub
tags:
- frontend-ui
- design-systems
- ui-patterns
- style-guide
- ai-generated-code
---

### TL;DR
`Uncodixfy` is a style guide for making AI-generated frontend UI look less “AI” by banning common dashboard tropes and pushing for plain, functional, human-designed layouts.

### Key Quote
> "This document exists to teach you how to act as non-Codex as possible when building UI."

### Summary
- This is a GitHub `SKILL.md` file named **`uncodixfy`**, intended to be used whenever generating **HTML, CSS, React, Vue, Svelte, or other frontend UI code**.
- Its core purpose is to prevent the default “Codex UI” look:  
  - soft gradients  
  - floating panels / glassmorphism  
  - eyebrow labels  
  - decorative copy  
  - oversized rounded corners  
  - dramatic shadows  
  - hero sections inside dashboards  
  - excessive animation
- The document repeatedly frames its guidance as **what not to do**: the “banned patterns” are meant to serve as red flags, while “normal implementations” are the blueprint.
- It gives a long “Keep It Normal” checklist covering common UI elements:
  - **Sidebars**: fixed width, solid background, simple border-right
  - **Headers**: plain hierarchy, no eyebrow labels or gradient text
  - **Buttons/cards/forms/tables/tabs/badges/avatars/icons**: all should be simple, restrained, and functional
  - **Layout**: predictable structure, standard spacing, no creative asymmetry or floating shells
  - **Motion**: short, subtle transitions only
- There is a strong “Hard No” section banning many familiar AI-dashboard aesthetics:
  - pill overload
  - glassmorphism
  - generic dark SaaS compositions
  - fake charts and decorative quota panels
  - gradients used to fake taste
  - transform animations on hover
  - dramatic shadows
  - label/badge-heavy UI
  - blue-heavy palettes and “premium dark mode” looks
- It explicitly bans **headlines of any sort** in certain internal UI contexts, showing example HTML that is considered unacceptable:
  - `<small>` headers
  - decorative section copy
  - “team note” style callouts
  - rounded `span`s
- A later “Specifically Banned” section lists mistakes the author wants to avoid, with examples like:
  - 20–32px border radii everywhere
  - 280px sidebars with top brand blocks
  - glass cards around charts
  - KPI grids as the default dashboard
  - right-side “Today” rails
  - nested panel variants
  - nav badges and trend indicators
- The guide also gives a **color-selection rule**:
  1. Prefer the project’s existing colors if they can be found in nearby files.
  2. Otherwise, choose from one of the provided palettes.
  3. Do not invent random color combinations unless asked.
- It includes **10 dark** and **10 light** predefined palettes, such as:
  - Dark: Midnight Canvas, Obsidian Depth, Slate Noir, Void Space, Onyx Matrix
  - Light: Cloud Canvas, Pearl Minimal, Ivory Studio, Alabaster Pure, Frost Bright
- Overall, the document is a **prescriptive anti-pattern guide** for UI generation: it tries to force the model away from generic AI-looking interfaces and toward restrained, conventional, product-like designs inspired by **Linear, Raycast, Stripe, and GitHub**.

### Assessment
This is a **reference** document with **high durability** in its general design principles, though some specifics may age with UI trends or framework conventions. Its content type is mostly **tutorial/reference** with a strong opinionated tone, and the density is **high** because it packs many concrete do/don’t rules into one file. It appears to be **primary source** guidance from the repository author rather than a synthesis of outside material. It’s best used as a **refer-back** card when generating UI, especially for checking banned patterns and palette choices. Scrape quality is **good**: the full text structure, examples, and color tables are present, with no obvious missing sections beyond what was included in the page text.
