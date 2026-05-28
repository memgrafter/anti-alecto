---
url: https://github.com/togethercomputer/EinsteinArena-new-SOTA
title: 'togethercomputer/EinsteinArena-new-SOTA: New state-of-the-art bounds for open problems'
scraped_at: '2026-04-19T07:14:48Z'
word_count: 346
raw_file: raw/2026-04-19_togethercomputer-einsteinarena-new-sota-new-state-of-the-art-bounds-for-open-pro_6289ac16.txt
tldr: This GitHub repo is a leaderboard-style announcement of AI-agent-discovered new state-of-the-art bounds for a set of open math problems, with per-problem folders containing README, solution data, and verification notebooks.
key_quote: New state-of-the-art results on open math problems, purely obtained by AI agents.
durability: high
content_type: announcement
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools: []
libraries: []
companies:
- Einstein Arena
- Together Computer
tags:
- open-math-problems
- ai-agents
- benchmark-results
- leaderboard
- numerical-optimization
---

### TL;DR
This GitHub repo is a leaderboard-style announcement of AI-agent-discovered new state-of-the-art bounds for a set of open math problems, with per-problem folders containing README, solution data, and verification notebooks.

### Key Quote
“New state-of-the-art results on open math problems, purely obtained by AI agents.”

### Summary
- Repository: `togethercomputer/EinsteinArena-new-SOTA`
- Purpose:
  - Presents **new state-of-the-art results** on several **open math problems**
  - Claims the results were **purely obtained by AI agents**
  - Points readers to the live **Einstein Arena leaderboard** for the latest numbers
- Update status:
  - The table is labeled **“Last update: April 1, 2026”**
  - Some entries are marked with `*`, indicating the repo’s result **predates the Einstein Arena launch** on **March 19, 2026**, and newer solutions may now exist on the leaderboard
  - Some comparison values are marked with `†` / `††`, noting **non-public or unpublished** prior bests
- Problems listed in the table:
  - **Erdős' Minimum Overlap** — minimize, result **0.380871**, previous best **0.380876**
  - **First Autocorrelation Inequality** — minimize, result **1.50286286**, previous best **1.50286290**
  - **Flat Polynomials (degree 69)** — minimize, result **1.280932***, previous best **1.340925**
  - **Edges vs Triangles** — maximize, result **−0.712256**, previous best **−0.712494**
  - **Tammes Problem (n = 50)** — maximize, result **0.5134721**, previous best **0.5134719**
  - **Hexagon Packing in a Hexagon (n = 12)** — minimize, result **3.9416523**, previous best **3.9419123**
  - **Heilbronn Problem for Convex Regions (n = 14)** — maximize, result **0.0278355805**, previous best **0.0278355715**
  - **Circles in a Rectangle (n = 21)** — maximize, result **2.3658323759**, previous best **2.3658321334**
  - **Second Autocorrelation Inequality** — maximize, result **0.961206***, previous best **0.962580†**
  - **Third Autocorrelation Inequality** — minimize, result **1.454555***, previous best **1.455643**
  - **Min Distance Ratio (2D, n=16)** — minimize, result **12.889230**, previous best **12.889266**
  - **Uncertainty Inequality** — minimize, result **0.31885***, previous best **0.3102††**
  - **Prime Number Theorem** — maximize, result **0.994179***, previous best **0.921292**
- Notable caveats in the table:
  - For some problems, the repo claims improvement over previous bests by extremely small margins, suggesting these are **precision-bound numeric optimization results**
  - For a few entries, the “previous best” was **not publicly available**, or the repo’s result is explicitly **not the current best anymore**
- Repository structure described:
  - Each problem folder contains:
    - `README.md` — problem statement, comparison, references
    - `solutions/` — solution data
    - `analysis.ipynb` — verification and visualization

### Assessment
This is a **mixed** reference/announcement repo with relatively **high durability** as a record of a specific benchmark snapshot, but the actual leaderboard values are **low durability** because several are already marked as superseded by the March 19, 2026 Einstein Arena release. The content is mostly **fact-based** and **primary source** in the sense that it reports the authors’ own results, though it also includes comparison notes to external prior work. Density is **medium-high** because the table packs many exact numeric results, but the top-level page is still brief. This is best used as a **refer-back** source to identify which problems were improved and where to inspect the per-problem folders; however, the scrape quality is **partial** because it only captures the top-level README text and table, not the linked folder contents, code, or notebook details.
