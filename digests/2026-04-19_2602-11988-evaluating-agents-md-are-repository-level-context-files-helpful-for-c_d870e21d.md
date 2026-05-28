---
url: https://arxiv.org/abs/2602.11988
title: '[2602.11988] Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?'
scraped_at: '2026-04-19T07:05:33Z'
word_count: 385
raw_file: raw/2026-04-19_2602-11988-evaluating-agents-md-are-repository-level-context-files-helpful-for-c_d870e21d.txt
tldr: This arXiv paper tests whether repository-level context files like `AGENTS.md` actually help coding agents and finds they usually hurt task success while increasing inference cost.
key_quote: Across multiple coding agents and LLMs, we find that context files tend to reduce task success rates compared to providing no repository context, while also increasing inference cost by over 20%.
durability: medium
content_type: fact
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Thibaud Gloaguen
tools: []
libraries: []
companies: []
tags:
- software-engineering
- coding-agents
- arxiv
- evaluation
- repository-context
---

### TL;DR
This arXiv paper tests whether repository-level context files like `AGENTS.md` actually help coding agents and finds they usually hurt task success while increasing inference cost.

### Key Quote
“Across multiple coding agents and LLMs, we find that context files tend to reduce task success rates compared to providing no repository context, while also increasing inference cost by over 20%.”

### Summary
- **Topic:** Evaluation of `AGENTS.md`-style repository context files for coding agents.
- **Core question:** Are repo-level context files, whether **LLM-generated** or **developer-written**, helpful for real-world coding tasks?
- **Why this matters:** Agent developers strongly encourage using context files, but the paper says there had been **no rigorous investigation** into whether they actually improve performance.
- **Evaluation setup:**
  - **Setting 1:** Established **SWE-bench** tasks from popular repositories, paired with **LLM-generated context files** created according to agent-developer recommendations.
  - **Setting 2:** A **new collection of issues** from repositories that already contain **developer-committed context files**.
- **Main findings:**
  - Across multiple coding agents and LLMs, context files **reduced task success rates** relative to giving agents **no repository context**.
  - They also increased **inference cost by over 20%**.
  - Behaviorally, both LLM-generated and developer-provided context files pushed agents toward **broader exploration**:
    - more thorough testing
    - more file traversal
  - Agents generally **followed the instructions** in these files.
- **Interpretation / conclusion:**
  - The authors conclude that **unnecessary requirements** in context files make tasks harder.
  - They recommend that human-written context files include **only minimal requirements**.

### Assessment
**Durability:** Medium. The underlying question about whether repo context helps agents is likely durable, but the concrete results may age as coding agents and prompting strategies change. **Content type:** research. **Density:** high; the abstract packs in the setup, comparison conditions, behavioral observations, and the main quantitative claim about cost. **Originality:** primary source, since this is the paper’s own experimental report. **Reference style:** refer-back, especially if you want to cite the finding that `AGENTS.md`-style files may harm performance. **Scrape quality:** good for the abstract and metadata, but partial overall because only the arXiv page text is present; the full paper, figures, tables, and methods are not included here.
