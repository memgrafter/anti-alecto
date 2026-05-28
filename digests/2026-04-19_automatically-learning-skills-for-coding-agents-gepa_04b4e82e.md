---
url: https://gepa-ai.github.io/gepa/blog/2026/02/18/automatically-learning-skills-for-coding-agents/
title: Automatically Learning Skills for Coding Agents - GEPA
scraped_at: '2026-04-19T07:17:34Z'
word_count: 1137
raw_file: raw/2026-04-19_automatically-learning-skills-for-coding-agents-gepa_04b4e82e.txt
tldr: GEPA introduces gskill, an automated pipeline that uses SWE-smith-generated tasks and GEPA’s `optimize_anything` loop to learn repository-specific coding skills that significantly improve task success and speed, and transfer across agents/models.
key_quote: “With fully automated learning pipeline for skills, downstream agents benefit from the learned skills for free.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- GEPA
- optimize_anything
- SWE-smith
- Mini-SWE-Agent
- Claude Code
- Claude Haiku 4.5
- Claude Sonnet 4.5
libraries:
- gpt-5-mini
companies: []
tags:
- coding-agents
- machine-learning
- software-engineering
- automation
- llm-agents
---

### TL;DR
GEPA introduces **gskill**, an automated pipeline that uses SWE-smith-generated tasks and GEPA’s `optimize_anything` loop to learn repository-specific coding skills that significantly improve task success and speed, and transfer across agents/models.

### Key Quote
“With fully automated learning pipeline for skills, downstream agents benefit from the learned skills for free.”

### Summary
- **What it is**
  - A blog post announcing **gskill**, a fully automated pipeline for learning skills for any GitHub repository.
  - The learned skills are stored as agent-readable files, including a repo-specific **`SKILL.md`** under **`.claude/skills/{repo_name}/SKILL.md`** for Claude Code.

- **Core idea**
  - gskill combines two pieces:
    - **GEPA’s `optimize_anything`**: an optimization API for evolving any textual artifact, including skills.
    - **SWE-smith**: a data-generation pipeline that creates **verifiable software engineering tasks** for a given GitHub repository.
  - The post frames SWE-smith as turning a static repository into an **active training environment** by producing tasks with testable feedback.

- **How the learning loop works**
  - Start with a set of skills, possibly empty.
  - Evaluate an agent on generated tasks.
  - Use a stronger LLM to reflect on results and feedback.
  - Update the skill text.
  - Repeat until convergence.

- **Experimental setup**
  - Repositories tested: **Jinja** and **Bleve**.
  - Agent baseline: **Mini-SWE-Agent** powered by **gpt-5-mini**.
  - Task generation:
    - About **300 SWE-smith tasks per repository**
    - Split into roughly **200 train**, **50 validation**, and **60 test** tasks
  - Learned skills were then transferred to **Claude Code** and tested with:
    - **Claude Haiku 4.5**
    - **Claude Sonnet 4.5**

- **Results on Mini-SWE-Agent**
  - After under **300 rollouts**:
    - **Jinja** resolve rate: **55% → 82%**
    - **Bleve** resolve rate: **24% → 93%**
  - The post emphasizes the large gains on the weaker baseline.

- **Transfer to Claude Code**
  - Learned skills were evaluated on the same task set, installed as repository skills in Claude Code.
  - Reported outcomes:
    - On **Bleve**, **Claude Haiku 4.5** improved from **79.3% to 100% pass rate** and ran faster.
    - On **Jinja**, **Claude Haiku 4.5** improved from **93.9% to 98.5%**.
    - For **Claude Sonnet 4.5**, pass rate was already near saturation, but task duration still improved substantially.
  - The article argues that skills learned on one model/agent can transfer to another.

- **Examples of learned skills**
  - For Bleve, examples include:
    - **Run tests early and iterate from failures**
      - Start broad: `cd /testbed && go test ./...`
      - Narrow to a package: `go test ./path/to/pkg`
      - Run a single test: `go test ./path/to/pkg -run TestName -count=1`
    - **Make minimal, reviewable changes and verify continuously**
      - Change one behavior at a time
      - Re-run the smallest reproducing test after each change
      - Add focused unit tests where coverage is missing
      - Avoid scratch `main.go` files in the repo root
  - The post says these are especially helpful for SWE-smith-style bug-fixing tasks.

- **Main takeaways**
  - Learned skills can produce **very large gains on weaker agents**.
  - Skills **transfer across models and agent harnesses**.
  - Skills improve **speed/cost**, not just accuracy.
    - Example from the conclusion: on **Bleve with Claude Haiku 4.5**, average task duration dropped from **173s to 142s** while pass rate rose from **79.3% to 98.3%**.

- **Future directions**
  - Scale beyond SWE-smith’s simpler tasks.
  - Evolve more than just a **`SKILL.md`** file, including executable scripts.
  - Extend the approach to **non-SWE tasks** such as computer use.
  - The post points readers to the official docs for **`optimize_anything`** and **GEPA**.

### Assessment
This is a **mixed** announcement/technical writeup with a strong tutorial-like recipe section and experimental claims. **Durability: medium** — the high-level idea of automated skill learning is likely to remain relevant, but the specific results, model names, repository choices, and file paths are tied to current tooling and versions. **Content type: mixed**. **Density: high** because it includes concrete pipeline components, task counts, exact pass-rate numbers, command examples, and transfer results. **Originality: primary source** — it reports the authors’ own system and experiments rather than summarizing others. **Reference style: refer-back** — useful for revisiting the pipeline design, experimental setup, or specific performance figures. **Scrape quality: good** — the main article content, key numbers, and example skill snippets are present; the formatting is somewhat repetitive and some bullet structure is flattened, but the substantive text appears intact.
