---
url: https://piechowski.io/post/git-commands-before-reading-code/
title: https://piechowski.io/post/git-commands-before-reading-code/
scraped_at: '2026-04-19T20:07:31Z'
word_count: 769
raw_file: raw/2026-04-19_https-piechowski-io-post-git-commands-before-reading-code_cad5bdde.txt
tldr: The article argues that five simple Git commands can quickly reveal a new codebase’s biggest risks—churn hotspots, bus factor, bug clusters, momentum, and firefighting—before you read any source files.
key_quote: Five git commands that tell you where a codebase hurts before you open a single file.
durability: high
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Ally Piechowski
tools:
- git
libraries: []
companies:
- Microsoft Research
tags:
- git
- codebase-audit
- software-maintenance
- debugging
- developer-productivity
---

### TL;DR
The article argues that five simple Git commands can quickly reveal a new codebase’s biggest risks—churn hotspots, bus factor, bug clusters, momentum, and firefighting—before you read any source files.

### Key Quote
“Five git commands that tell you where a codebase hurts before you open a single file.”

### Summary
- The author, Ally Piechowski, describes a first-pass codebase audit workflow that starts in the terminal rather than in the editor.
- The goal is to use Git history as a diagnostic tool to identify:
  - files with the highest change frequency,
  - contributor concentration and maintenance risk,
  - bug-prone areas,
  - whether the project is accelerating or losing momentum,
  - signs of frequent crisis work like reverts and hotfixes.

- **1) What changes the most**
  - Command: `git log --format=format: --name-only --since="1 year ago" | sort | uniq -c | sort -nr | head -20`
  - Purpose: find the 20 most-changed files in the last year.
  - Interpretation:
    - High churn can mean active development, but if a file is also disliked or hard to own, it may be a major drag on the team.
    - The author cites a 2005 Microsoft Research study claiming churn-based metrics predicted defects better than complexity metrics alone.
    - They recommend cross-referencing the top churn files with bug hotspots; files that are both high-churn and high-bug are the biggest risk.

- **2) Who built this**
  - Command: `git shortlog -sn --no-merges`
  - Purpose: rank contributors by commit count.
  - Interpretation:
    - If one person accounts for 60% or more of commits, that suggests a high bus factor.
    - If the top contributor is absent from the last 6 months (`--since="6 months ago"`), the author treats that as an immediate red flag for the client.
    - They also check whether many people contributed historically but only a few are still active, suggesting the builders and maintainers are different.
  - Caveat:
    - Squash merges can distort authorship because the output reflects who merged commits, not necessarily who wrote them.

- **3) Where do bugs cluster**
  - Command: `git log -i -E --grep="fix|bug|broken" --name-only --format='' | sort | uniq -c | sort -nr | head -20`
  - Purpose: find files mentioned in bug-related commits.
  - Interpretation:
    - Compare bug clusters against churn hotspots.
    - Files appearing in both lists are described as the highest-risk code: they break often and keep getting patched rather than properly fixed.
  - Limitation:
    - This depends on commit message quality; vague messages like “update stuff” reduce usefulness.

- **4) Is this project accelerating or dying**
  - Command: `git log --format='%ad' --date=format:'%Y-%m' | sort | uniq -c`
  - Purpose: count commits by month across the repo history.
  - Interpretation:
    - A steady rhythm suggests health.
    - A sudden drop by half may indicate someone left.
    - A declining trend over 6–12 months suggests the team is losing momentum.
    - Repeating spikes followed by quiet periods suggest release batching rather than continuous shipping.
  - The author emphasizes this is “team data, not code data.”

- **5) How often is the team firefighting**
  - Command: `git log --oneline --since="1 year ago" | grep -iE 'revert|hotfix|emergency|rollback'`
  - Purpose: count crisis-related commits.
  - Interpretation:
    - A few such commits per year are normal.
    - Frequent reverts/hotfixes suggest low trust in the deploy process and possibly weak tests, poor staging, or difficult rollbacks.
    - Zero results may mean stability, or just poor commit message habits.

- Overall takeaway:
  - These commands take only a few minutes and do not replace reading the code.
  - They help you decide where to focus first and what questions to ask while reading.
  - The author frames this as the first hour of a broader codebase audit, with more steps to follow later.

### Assessment
This is a **tutorial/opinion hybrid** with a **high** durability level because the commands and the reasoning behind them are broadly applicable across Git-based codebases, though some interpretations depend on team practices like squash merges and commit-message discipline. The content is **medium-high density**, with concrete commands, thresholds, and practical heuristics rather than broad advice. It is **primarily commentary** from Ally Piechowski, informed by experience and one cited research finding, not a formal reference guide. Best used as **refer-back** material when auditing unfamiliar repositories. Scrape quality is **good**: the main article text and all five commands are present, though formatting is plain and there are no missing code blocks or images that appear essential.
