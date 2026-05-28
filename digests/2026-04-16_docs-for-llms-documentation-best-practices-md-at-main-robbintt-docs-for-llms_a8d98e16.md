---
url: https://github.com/robbintt/docs-for-llms/blob/main/documentation-best-practices.md
title: docs-for-llms/documentation-best-practices.md at main · robbintt/docs-for-llms
scraped_at: '2026-04-16T03:54:40Z'
word_count: 1100
raw_file: raw/2026-04-16_docs-for-llms-documentation-best-practices-md-at-main-robbintt-docs-for-llms_a8d98e16.txt
tldr: A practical guide to writing technical documentation for LLMs that front-loads value, keeps examples short and runnable, uses tables and links strategically, and prioritizes quick-start usability over exhaustive explanation.
key_quote: Write documentation as if every reader will leave after 30 seconds. Because they will.
durability: high
content_type: tutorial
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries: []
companies: []
tags:
- technical-documentation
- docs-writing
- llm-workflows
- best-practices
- developer-experience
---

### TL;DR
A practical guide to writing technical documentation for LLMs that front-loads value, keeps examples short and runnable, uses tables and links strategically, and prioritizes quick-start usability over exhaustive explanation.

### Key Quote
"Write documentation as if every reader will leave after 30 seconds. Because they will."

### Summary
- The document argues that human readers scan docs quickly, so the most important information must appear immediately.
- **Core principle: front-load value**
  - Put a **Quick Start within the first ~50 lines**.
  - Follow the sequence **Installation → Authentication → First Command**.
  - Show **working code before explanation**.
- **Before Quick Start, include only three essentials**
  - A one-sentence **context-setting intro**.
  - **Prerequisites** such as required versions or environment support.
  - **Common errors** with direct fixes, ideally in Troubleshooting or right after Quick Start.
- **Recommended doc structure**
  - Quick Start: 20–40 lines
  - Key Capabilities: 10–15 lines
  - Table of Contents: 5–20 lines
  - Core Concepts: 50–100 lines
  - API Reference: the rest
  - It explicitly says to skip sections that do not apply and prefers a short useful doc over a long abandoned one.
- **Code examples should be short and copy-pasteable**
  - Target **5–20 lines per block**.
  - Examples should be complete enough to run, short enough to read, and annotated after the code.
  - It gives a TypeScript example of registering a tool and says to avoid sprawling examples with too many concerns.
- **Tables vs prose**
  - Use **tables** for flags, comparisons, configuration references, and shortcuts.
  - Use **prose** for concepts, sequential steps, architecture, and warnings.
- **Cross-linking strategy**
  - Prefer **anchor links** for staying in the same doc.
  - Use **relative links** for internal related docs.
  - Use **absolute links** for external resources.
  - Link to the **smallest useful target**, not a huge file.
- **Security warnings**
  - Put warnings **before** dangerous content.
  - Format them distinctly so skimming readers can’t miss them.
- **What not to document**
  - Avoid internal implementation details unless the doc is specifically about internals.
  - Don’t restate obvious behavior.
  - Don’t document every edge case in the main docs.
  - Keep history/changelog content out of main docs.
- **File organization guidance**
  - Give separate pages to major features, APIs, and configuration references.
  - Keep minor config, simple file formats, and platform notes inline.
  - If a topic needs more than **100 lines** of explanation, it should likely be its own file.
- **Working Example Test**
  - Before publishing, verify that examples can be copied, run, produce visible output, and that the expected output is documented.
  - The message is blunt: **untested documentation is broken documentation**.
- **Summary table of principles**
  - Quick Start first because most users only need that.
  - Keep examples short.
  - Use tables for scanability.
  - Use anchor links for navigation.
  - Put warnings before danger.
  - Test every example.
- **Scope boundary**
  - The guide explicitly excludes docs-program management topics such as versioning, maintenance signals, accessibility, internationalization, SEO, feedback systems, interactive examples, audience segmentation, review processes, and tooling.
  - It frames itself strictly as guidance on **how to write documentation**, not how to manage a documentation program.

### Assessment
This is a **high-durability** reference/documentation piece with a **mixed** content type leaning strongly toward **tutorial/reference**. It is fairly **dense**, packed with concrete structure recommendations, line-count targets, and formatting rules, making it useful as a practical style guide rather than a philosophical essay. The work reads like **synthesis/commentary** rather than primary research: it distills observed best practices into prescriptive guidance. It is best used as a **refer-back** resource when drafting or reviewing docs, especially for AI-assisted documentation workflows. **Scrape quality is good**: the full text appears captured, including examples, table content, and the scope-exclusion section, with no obvious missing code blocks or major sections.
