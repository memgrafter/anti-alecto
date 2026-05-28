---
url: https://dynomight.net/scribbles/
title: https://dynomight.net/scribbles/
scraped_at: '2026-05-10T04:26:59Z'
word_count: 2034
raw_file: raw/2026-05-10_https-dynomight-net-scribbles_94d4c566.txt
tldr: Dynomight argues that for AI 2027-style forecasts, the real value comes less from formal math than from making assumptions explicit, and he demonstrates this with a “scribble-based” forecast of METR-style task horizons that yields median AGI-adjacent dates in the 2030s.
key_quote: the exercise of drawing the scribbles is great, because it forces you to be completely explicit, and your assumptions are completely legible.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Dynomight
- AI 2027
- METR
- IPCC
- Casey
tools:
- CSV
libraries: []
companies: []
tags:
- ai-forecasting
- epistemology
- forecasting-methods
- machine-learning
- ai-2027
---

### TL;DR
Dynomight argues that for AI 2027-style forecasts, the real value comes less from formal math than from making assumptions explicit, and he demonstrates this with a “scribble-based” forecast of METR-style task horizons that yields median AGI-adjacent dates in the 2030s.

### Key Quote
“the exercise of drawing the scribbles is great, because it forces you to be completely explicit, and your assumptions are completely legible.”

### Summary
- The post is a critique of **forecasting methods** in the context of **AI 2027** and a broader argument about when **intuition** is better than **formal mathematical models**.
- Core thesis:
  - Math/simulation is most useful when the system has **well-understood rules** and **complex emergent behavior**.
  - When the underlying mechanism is poorly understood or too hard to model reliably, **careful human intuition** may be more trustworthy than a fake-precise model.
- He contrasts two examples:
  - **Climate forecasting**: appropriate for heavy mechanistic modeling because the science is relatively well-understood and highly complex.
  - **Geopolitical proliferation / future world events**: harder to model mechanistically because the whole world would need to be simulated, and errors could be consequential.
- He then turns to **AI 2027’s forecast**, specifically the **Time horizon extension model**:
  - Based on a **METR report** measuring how long tasks take humans and how well AIs can complete them.
  - AIs are rated by the **human task length** they can finish **50% of the time**.
  - AI 2027 effectively asks when models will reach longer task horizons, with an adjusted success target of **80%** rather than 50%.
  - The team also adds adjustments for:
    - internal company models being better than released models
    - public models using less compute to save money
- Dynomight’s critique:
  - The AI 2027 forecast is mostly just projecting **one metric rising over time**.
  - He argues that the formal model is not doing much explanatory work beyond making the trend look more rigorous.
  - Still, he thinks the broader question is meaningful: if those task-horizon dots keep rising fast, AGI may indeed be near.
- He proposes his own method: **“scribble-based forecasting”**
  - Start by plotting the data.
  - Draw **50 plausible curves** by hand over the data.
  - Treat those curves as a probability distribution over futures.
  - Measure when each curve crosses task-horizon thresholds.
- His resulting table for thresholds:
  - **1 month**: 10th percentile **2028.7**, median **2032.3**, 90th percentile **2039.3**, **94% reached by 2050**
  - **1 year**: 10th percentile **2029.5**, median **2034.8**, 90th percentile **2041.4**, **88% reached by 2050**
  - **10 year**: 10th percentile **2029.2**, median **2037.7**, 90th percentile **2045.0**, **54% reached by 2050**
- He emphasizes that the point is not that his scribbles are “correct,” but that they are:
  - **explicit**
  - **legible**
  - easy to inspect and debate
- He ends by saying he built a **tool** for others to create their own scribble-based forecasts, with:
  - automatic plot and table generation
  - **CSV import/export**
  - the author’s own scribbles available as a starting point
  - a video demo
- Tone/stance:
  - skeptical of over-formalized forecasting
  - mildly sympathetic to AI 2027’s premise
  - pro-transparency and pro-heuristic methods when the model is too thin

### Assessment
This is an opinionated, fairly dense essay with a practical forecasting demo layered on top. Durability is **medium-high**: the broader argument about when to trust intuition versus formal models is timeless, but the AI 2027/METR specifics are version- and moment-dependent. Content type is **mixed**: part essay, part critique, part tutorial/tool announcement. Originality is **primary source**, since it presents the author’s own framing, example, and forecast method rather than summarizing others. It’s best used as a **deep-study** reference if you care about AI forecasting methods or epistemology, though the tool announcement and specific numbers will age as AI benchmarks change. Scrape quality is **good overall**: the main text and table are present, but the embedded figure/video/demo are not captured in full, so visual details are missing.
