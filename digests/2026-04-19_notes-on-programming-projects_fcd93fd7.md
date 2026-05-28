---
url: https://swtch.com/~rsc/worknotes/
title: Notes on Programming Projects
scraped_at: '2026-04-19T07:37:55Z'
word_count: 517
raw_file: raw/2026-04-19_notes-on-programming-projects_fcd93fd7.txt
tldr: Russ Cox’s “Notes on Programming Projects” lays out the coding norms, communication habits, and work style he expects from collaborators, emphasizing consistency with existing code, idiomatic style, minimal comments, simple efficient solutions, and frequent status updates.
key_quote: do what the rest of the code does.
durability: high
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Russ Cox
- Kernighan
- Pike
tools:
- CVS
libraries: []
companies: []
tags:
- coding-style
- software-collaboration
- code-review
- software-maintenance
- version-control
---

### TL;DR
Russ Cox’s “Notes on Programming Projects” lays out the coding norms, communication habits, and work style he expects from collaborators, emphasizing consistency with existing code, idiomatic style, minimal comments, simple efficient solutions, and frequent status updates.

### Key Quote
“do what the rest of the code does.”

### Summary
- This is a short set of working notes for people programming on projects with Russ Cox.
- It is framed as practical guidance on mechanics and collaboration, and explicitly points readers to Kernighan and Pike’s *The Practice of Programming* for deeper philosophy.

- **Style / consistency**
  - The strongest rule is: when modifying existing code, match the surrounding code’s style rather than imposing personal preferences.
  - Cox argues there is “only one right answer” in maintained code: follow the conventions already in the file/project.
  - He says inconsistent style is especially annoying when one section of a source file looks unrelated to the rest.

- **Plan 9 conventions listed**
  - No whitespace before opening braces.
  - No braces around single-line blocks (`if`, `for`, `while`).
  - Integer-valued functions return `-1` on error.
  - Variable and function names are all lowercase, with no underscores.
  - `enum` or `#define` constants use `Uppercase` or `UPPERCASE`.
  - `struct` names are capitalized, with matching `typedef`s.
  - Automatic/local variables are not initialized at declaration.

- **Idiomatic language use**
  - Use common coding idioms instead of unusual forms.
  - Example: prefer `a < 0` over `0 > a`.
  - Use conventional loop variable names like `i`, `j`, `k` rather than invented names like `lv1`, `lv2`, `lv3`.
  - The underlying idea is that code should “look natural” to people familiar with the codebase.

- **Comments**
  - If code is readable, it should not need many comments.
  - A brief comment above a function explaining what it does is welcomed.
  - When you encounter code whose reason is unclear, add a comment explaining the ambiguity or concern.
  - Comments should go on their own lines before the code they describe.
  - Comments are not a substitute for confusing code; unclear code should be rewritten to be clear.

- **Efficiency**
  - Prefer doing the simple thing.
  - Do not optimize unless the code is measurably slow.
  - If performance matters, improve data structures before making tiny micro-optimizations like “5% tweaks.”

- **CVS / version control**
  - The team will “probably use CVS,” described as more of a crude distributed file system than a real source control system.
  - Check-in messages should be brief summaries of changes, not essays.
  - If code needs explanatory comments, they belong in source files rather than in commit messages.

- **Critique and iteration**
  - Cox warns that he may suggest many changes, both small and large.
  - This should not be taken negatively; it often means the code is already good and is being refined further.
  - He uses the blunt phrase “you can’t polish a turd” to distinguish worthwhile refinements from hopeless code.

- **Communication**
  - Contributors should not disappear.
  - He expects regular email updates about status and occasional in-person conversation.

### Assessment
This is a practical, lightly opinionated reference note rather than a technical tutorial or formal policy document. Durability is **high** for the general advice on style, comments, simplicity, and communication, though some specifics are **low-to-medium** in durability because they mention Plan 9 conventions and CVS, which are version- and era-specific. The content type is **mixed**, leaning toward **reference** and **opinion**. Density is **medium**: short and readable, but packed with concrete norms and examples. Originality is **primary source**, since it is directly from Russ Cox outlining expectations for collaborators. It is best used as **refer-back** material for someone working in or reviewing code under these conventions, or **skim-once** if you mainly want the high-level principles. Scrape quality is **good**: the main sections and examples are present, though this appears to be a text-only capture and may omit any formatting nuances from the original page.
