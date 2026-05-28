---
url: https://mitchellh.com/writing/github-changesets
title: Reorient GitHub Pull Requests Around Changesets – Mitchell Hashimoto
scraped_at: '2026-04-19T08:42:36Z'
word_count: 1103
raw_file: raw/2026-04-19_reorient-github-pull-requests-around-changesets-mitchell-hashimoto_6dfd1e6b.txt
tldr: Mitchell Hashimoto argues GitHub pull requests should be reworked from a single mutable branch into versioned, immutable “changesets” so review feedback stays attached to the exact code state it was written for.
key_quote: GitHub pull requests today is effectively one giant mutable changeset. This is a mess!
durability: high
content_type: opinion
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Mitchell Hashimoto
tools:
- git
companies:
- GitHub
- Gerrit
- Phabricator
tags:
- github
- pull-requests
- code-review
- git-workflow
- developer-experience
---

### TL;DR
Mitchell Hashimoto argues GitHub pull requests should be reworked from a single mutable branch into versioned, immutable “changesets” so review feedback stays attached to the exact code state it was written for.

### Key Quote
"GitHub pull requests today is effectively one giant mutable changeset. This is a mess!"

### Summary
- **Main thesis:** GitHub PRs are frustrating at scale because they treat a branch as one continuously mutating review object; Mitchell proposes replacing that model with **versioned changesets**.
- **Problem with current PRs:**
  - Review comments can become outdated as soon as new commits are pushed.
  - Feedback can become partially invalid or confusing when lines move or disappear.
  - Review timestamps do not reliably indicate which commit/state was reviewed.
  - WIP commits meant to address feedback become visible immediately, forcing awkward review workflows.
  - It is hard to inspect prior PR states or compare one set of commits to another without rebuilding diffs locally.
- **Proposed solution: changesets**
  - A PR would have versions like **v1, v2, v3...**
  - Each version is **immutable** and tied to the branch state at a specific time.
  - New pushes or force-pushes create a **new changeset**, while previous versions remain available forever.
  - Review feedback attaches to a specific changeset, so later updates do not invalidate the review context.
  - Future changesets can mark unresolved comments from prior versions so earlier feedback is not lost.
- **Implementation idea:**
  - Each changeset could map to a distinct Git ref, e.g.:
    - current PRs: `refs/pr/1234`
    - proposed changeset: `refs/pr/1234/v2`
  - This would let people check out and inspect individual versions locally with Git.
- **Workflow benefits:**
  - Reviewers approve a **changeset**, not a floating branch state.
  - Contributors can present multiple alternative approaches in one PR.
  - Maintainers could choose a non-latest changeset to merge if desired.
- **Positioning / context:**
  - Mitchell says the idea is **not original**; it draws from established Git workflows and systems like **Gerrit**, **Phabricator**, and **email-based patch review**.
  - He argues it could be introduced in a **non-breaking** way because current PRs already behave like a single mutable changeset.
- **Conclusion:** He believes this one feature would significantly improve GitHub’s review experience, especially for large open source projects and large organizations.

### Assessment
This is an **opinion/commentary** piece with some workflow design analysis, and its durability is **high** because it argues from long-lived review-system principles rather than transient GitHub news. The content is **medium-density**: concise but specific, with concrete UX problems, a proposed data model, and example refs. It is **original as commentary** but explicitly based on prior art from Gerrit, Phabricator, and Git-based review practices rather than presenting new research. Best used as a **refer-back** reference if you want to recall the argument for versioned PR review; it is not a tutorial or implementation guide. **Scrape quality is good**: the main article and footnotes are present, and no obvious sections or code blocks seem missing.
