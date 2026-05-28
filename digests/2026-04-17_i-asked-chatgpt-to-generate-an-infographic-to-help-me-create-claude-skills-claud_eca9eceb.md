---
url: https://www.reddit.com/r/ClaudeAI/comments/1pxl99v/i_asked_chatgpt_to_generate_an_infographic_to/
title: 'I asked ChatGPT to generate an infographic to help me create Claude Skills : ClaudeAI'
scraped_at: '2026-04-17T05:29:49Z'
word_count: 523
raw_file: raw/2026-04-17_i-asked-chatgpt-to-generate-an-infographic-to-help-me-create-claude-skills-claud_eca9eceb.txt
tldr: A Reddit user shares a two-prompt workflow for turning an existing document template into a reusable Claude Skill by first reverse-engineering the template’s full design spec and then using that spec to enforce pixel-perfect document generation.
key_quote: You will be reverse-engineering a document template to extract its complete design specification.
durability: low
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- u/frankentag
- u/MongoloidAu
tools:
- chatgpt
- claude skills
- skills creator
libraries: []
companies: []
tags:
- prompt-engineering
- claude-ai
- document-templates
- workflow-automation
---

### TL;DR
A Reddit user shares a two-prompt workflow for turning an existing document template into a reusable Claude Skill by first reverse-engineering the template’s full design spec and then using that spec to enforce pixel-perfect document generation.

### Key Quote
“You will be reverse-engineering a document template to extract its complete design specification.”

### Summary
- This is a short r/ClaudeAI thread by **u/frankentag** titled **“I asked ChatGPT to generate an infographic to help me create Claude Skills”**.
- The poster says they’ve been experimenting with **Claude Skills** and created a **simple infographic/checklist** to standardize their workflow for converting an existing template into a reusable skill.
- The workflow is presented as **two prompts**:
  - **Prompt 1: Reverse-engineer the design template**
    - Analyze a provided document template and extract a **complete design specification**.
    - Use `<scratchpad>` tags for step-by-step analysis.
    - Capture:
      - **Typography**: font families, sizes, weights, line heights, letter spacing, alignment
      - **Colors**: all colors and where they apply
      - **Layout & spacing**: margins, padding, spacing, page dimensions
      - **Visual elements**: logos, icons, borders, backgrounds
      - **Formatting & style**: headings, paragraphs, lists, tables, special styling
      - **Structural elements**: header/footer, columns, repeating patterns
    - Return the result inside `<design_specification>` tags.
  - **Prompt 2: Convert the template into a Claude Skill**
    - Use the **“Skills Creator”** skill to create a new skill.
    - The new skill should force all generated documents to **strictly follow the template** with **pixel-perfect accuracy**.
    - The extracted design details should be **embedded and enforced as binding requirements**.
- The post frames this as a **reliably working standard workflow** for the author.
- The only visible comment is a brief reaction from **u/MongoloidAu**: “Its very interesting what you do.”
- No substantive debate, corrections, or alternate methods appear in the captured thread.

### Assessment
This is a **mixed** Reddit post that is mostly a **tutorial/how-to** with a light social-thread wrapper. The content is **low-to-medium durability** because it depends on current Claude Skills tooling and prompt conventions, which may change as the product evolves. It is **medium density**: the thread is short, but the prompts are highly specific and practical. It appears to be **original work / firsthand workflow sharing** rather than a synthesis of others’ ideas. It’s best used as a **refer-back** reference if you’re trying to reproduce the prompt pattern, not as deep study. **Scrape quality is partial**: the post text and one visible comment are captured, but the infographic itself is not included, and the thread only reports 2 comments with just 1 shown here.
