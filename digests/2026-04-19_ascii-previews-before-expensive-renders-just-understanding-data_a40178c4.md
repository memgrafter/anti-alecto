---
url: https://understandingdata.com/posts/ascii-previews-before-expensive-renders/
title: ASCII Previews Before Expensive Renders - Just Understanding Data
scraped_at: '2026-04-19T07:50:33Z'
word_count: 1591
raw_file: raw/2026-04-19_ascii-previews-before-expensive-renders-just-understanding-data_a40178c4.txt
tldr: Use a cheap ASCII preview or storyboard as a human approval gate before expensive image/video generation so you catch misunderstandings before paying for full renders.
key_quote: The cheapest render is the one you never make.
durability: high
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- claude-haiku-4-5-20251001
- DALL-E 3
- GPT Image
- Sora
- Runway
libraries: []
companies: []
tags:
- generative-ai
- human-in-the-loop
- media-generation
- cost-optimization
- workflow-design
---

### TL;DR
Use a cheap ASCII preview or storyboard as a human approval gate before expensive image/video generation so you catch misunderstandings before paying for full renders.

### Key Quote
“The cheapest render is the one you never make.”

### Summary
- The article argues that **image and video generation are expensive enough that you should not render first and validate later**.
- Core idea: before calling a costly generative API, ask a cheap language model to produce:
  - an **ASCII layout preview** for images
  - an **ASCII storyboard sequence** for video
- A human reviews the preview and either:
  - approves it, then the expensive render runs, or
  - requests changes while the workflow is still in the cheap text domain.

- Problem framing:
  - Generative media calls can cost from **$0.02–$0.20+ per image**
  - Video generation can cost **dollars per clip**
  - Repeated trial-and-error can quickly waste money and time
  - The article gives a concrete example where three image render attempts cost **$0.24** and multiple full-render latencies, versus about **$0.083** using preview-first iteration plus only one final render

- Pattern recommended:
  - Insert a **preview step before any expensive generative call**
  - The preview is meant to capture:
    - composition
    - element placement
    - spatial relationships
    - pacing and transitions for video
  - The preview uses only **language model tokens**, which are much cheaper than rendering media

- For images:
  - Generate a **single ASCII diagram**
  - Pair it with a written description of:
    - colors
    - style
    - mood
    - lighting
    - details that ASCII cannot express
  - Example use case: a landing page hero image with a rocket launching from a laptop screen
  - This lets the user request changes like “move the rocket to the left third” before any pixels are rendered

- For video:
  - Generate an **ASCII storyboard** with several keyframes
  - Each frame should include:
    - timestamp ranges
    - scene composition
    - camera notes
    - action descriptions
    - transition notes
  - Example use case: a 15-second product demo of a user dragging a widget onto a dashboard
  - This lets the user review pacing and narrative flow before rendering

- Implementation section:
  - Shows a TypeScript-style flow:
    - define a `RenderRequest`
    - generate a `Preview`
    - send preview to a human callback `onPreview`
    - only call `executeRender(request)` if approved
  - The preview generation uses a cheap model:
    - example shown: `claude-haiku-4-5-20251001`
  - Two system prompts are included:
    - `IMAGE_PREVIEW_PROMPT`
    - `VIDEO_STORYBOARD_PROMPT`

- Cost comparison table:
  - ASCII preview (Haiku): about **$0.001**, ~1K input + ~1K output tokens, **<1s**
  - DALL-E 3 image generation: **$0.04–$0.12**, **10–20s**
  - GPT Image: **$0.02–$0.19**, **10–30s**
  - Sora/Runway video: **$0.50–$5.00**, **30s–5min**
  - Main point: **one wasted video render can pay for hundreds of previews**

- When to use the pattern:
  - Use previews when:
    - render cost is above **$0.05**
    - the prompt is ambiguous or multi-element
    - there is no reference image
    - you’re iterating repeatedly
    - you’re batch generating many assets
  - Skip previews when:
    - the task is very simple and well understood
    - you’re only tweaking minor parameters
    - the user explicitly says to skip
    - render cost is trivial

- Extensions proposed:
  - **Structured preview data** instead of pure ASCII, so a frontend can render a wireframe
  - **Batch preview for video**, where the user approves/rejects keyframes individually
  - **Progressive refinement**:
    - ASCII preview → approve layout
    - SVG wireframe → approve proportions
    - low-res render → approve colors/style
    - full render → final output
  - The article says most errors are best caught at the cheapest stage

- Bottom line:
  - The article is a practical workflow recommendation for **AI products or agents that generate media**
  - Its central claim is that **human-in-the-loop preview gates reduce wasted spend and reduce mismatch between intent and final output**

### Assessment
Durability: **high** — the pattern is conceptual and should remain useful as long as expensive generative media exists, though the specific model names and prices will age quickly. Content type: **tutorial/mixed** — it combines a workflow recommendation, implementation sketch, and cost argument. Density: **high** — it includes concrete examples, code, prompts, and price comparisons. Originality: **commentary/synthesis** — it presents a pattern and implementation approach rather than reporting primary research. Reference style: **refer-back** — useful as a design pattern to revisit when building image/video generation workflows. Scrape quality: **good** — the main text, examples, code snippets, prompts, and comparison table are present; no major sections appear missing from the provided content.
