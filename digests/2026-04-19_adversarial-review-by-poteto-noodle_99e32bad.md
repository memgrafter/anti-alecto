---
url: https://skills.sh/poteto/noodle/adversarial-review
title: adversarial-review by poteto/noodle
scraped_at: '2026-04-19T08:13:50Z'
word_count: 556
raw_file: raw/2026-04-19_adversarial-review-by-poteto-noodle_99e32bad.txt
tldr: A workflow for adversarial code review that uses opposite-model CLI reviewers with distinct lenses (Skeptic, Architect, Minimalist) to challenge changes and return a synthesized verdict without modifying code.
key_quote: Spawn reviewers on the opposite model to challenge work.
durability: medium
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- codex exec
- claude -p
- mktemp
libraries: []
companies: []
tags:
- code-review
- developer-workflow
- cli-tools
- software-engineering
- testing
---

### TL;DR
A workflow for adversarial code review that uses opposite-model CLI reviewers with distinct lenses (Skeptic, Architect, Minimalist) to challenge changes and return a synthesized verdict without modifying code.

### Key Quote
"Spawn reviewers on the opposite model to challenge work."

### Summary
- **What this is:** A procedural guide for running adversarial reviews of code changes using reviewers on the *opposite* model, specifically to avoid same-model bias.
- **Core idea:** The review is supposed to be genuinely adversarial: reviewers attack the work from different lenses grounded in “brain principles,” then a lead judgment filters false positives and style-only complaints.
- **Reviewers/lenses:**
  - **Skeptic** — challenges assumptions and correctness
  - **Architect** — evaluates design and structural choices
  - **Minimalist** — pushes for simplicity and avoiding unnecessary complexity
- **Reviewer count scales by change size:**
  - **Small**: under 50 lines, 1–2 files → 1 reviewer
  - **Medium**: 50–200 lines, 3–5 files → 2 reviewers
  - **Large**: 200+ lines or 5+ files → 3 reviewers
- **Hard constraint:** reviewers must be spawned via the opposite model’s CLI:
  - If you are **Claude**, use `codex exec`
  - If you are **Codex**, use `claude -p`
  - It explicitly forbids using subagents, the Agent tool, or internal delegation mechanisms because they would use the same model and undermine adversarial review
- **Inputs required before review:**
  - Read `brain/principles.md` and all wikilinked principle files
  - Read `references/reviewer-lenses.md`
  - Determine the review scope from context such as diffs, plans, or user messages
  - State the author’s intent explicitly before reviewers begin
- **Execution details:**
  - Create a temp directory with `mktemp -d /tmp/adversarial-review.XXXXXX`
  - Write each reviewer’s output to files like `skeptic.md`, `architect.md`, `minimalist.md`
  - Use background execution and monitor output
  - Default to read-only; only use `--profile edit` if tests are needed
- **Verification and output handling:**
  - Confirm which CLI was used by printing `reviewer_cli=codex|claude`
  - List reviewer output files before reading them
  - If any output file is missing or empty, explicitly report that failure
  - Deduplicate overlapping findings
  - Produce a synthesized verdict in the format from `references/verdict-format.md`
  - Append a **Lead Judgment** section stating which findings are accepted or rejected and why
- **Purpose of the deliverable:** not a code change, but a review verdict that focuses on whether the work achieves the stated intent.

### Assessment
Durability is **medium**: the underlying review pattern and anti-bias rationale are fairly durable, but the exact commands, CLI names, file paths, and model-specific instructions are tied to current tooling. Content type is **tutorial/reference**. Density is **high** because it gives concrete execution steps, constraints, thresholds, and file/command names in a compact format. Originality is mostly **primary source** in the sense that it defines a specific workflow, though it also reflects a broader adversarial-review pattern. This is best used as **refer-back** material since the exact procedure and constraints matter when performing the workflow. Scrape quality is **good** overall: the core instructions, thresholds, and command examples are present, though the referenced linked files (`brain/principles.md`, `references/reviewer-lenses.md`, `references/verdict-format.md`) are not included here.
