---
url: https://docs.chub.ai/docs/advanced-setups/lorebooks
title: Lorebooks | Chub AI Guide
scraped_at: '2026-04-18T05:02:22Z'
word_count: 999
raw_file: raw/2026-04-18_lorebooks-chub-ai-guide_58c310d6.txt
tldr: Chub AI’s lorebooks are keyword-triggered prompt injections that let you feed backstory, worldbuilding, and other context into chats without permanently spending token space.
key_quote: “A lorebook is a series of defined keywords that, when activated, insert specific content into the prompt.”
durability: medium
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Chub AI
- GitBook
libraries: []
companies:
- Chub AI
- GitBook
tags:
- prompt-engineering
- knowledge-base
- chatbots
- token-management
- documentation
---

### TL;DR
Chub AI’s lorebooks are keyword-triggered prompt injections that let you feed backstory, worldbuilding, and other context into chats without permanently spending token space.

### Key Quote
“A lorebook is a series of defined keywords that, when activated, insert specific content into the prompt.”

### Summary
- **What lorebooks are**
  - A lorebook is a set of defined keywords that, when mentioned in chat, inject associated content into the prompt.
  - They’re used to provide the AI with character backstory, setting, environment, and other context without putting all of it into the character definition.
  - When a lorebook is attached to a character, it is called a **Characterbook**.

- **How keyword triggering works**
  - If a message contains a matching keyword, the corresponding lorebook entry is inserted into the prompt.
  - Example given: keyword **“Apple”** with content like `{{char}} really loves Apples and will do anything to get one.`
  - Default matching is:
    - **case-insensitive**
    - **whole-word only**
  - So `apple` and `aPPle` match, but `Applebottom` does not.

- **Lorebook settings in Chat Settings**
  - **Scan Depth**: how many recent messages are checked for keywords, starting from the end of chat history.
    - Example: a scan depth of 2 generally covers your last message and the character’s last message.
  - **Token Budget**: how many tokens lorebook content is allowed to consume total.
    - Once the budget is reached, later matching keywords are ignored.

- **Creating lorebooks / character books**
  - Lorebooks can be created using the **Lorebook Creator** at `chub.ai/create_lorebook`.
  - Character books can be created in the **Character Creator**.
  - Character book fields described:
    - **Title**: label only; not used in prompting.
    - **Description**: label only; not used in prompting.
    - **Scan Depth & Token Budget**: default values for the character book, but user Chat Settings override them if set.
    - **Recursive Scanning**: allows entries to trigger other entries or be triggered by them, supporting chained/dependent lore.

- **Entry properties**
  - **Keywords**: main trigger words.
  - **Secondary Keywords**: additional trigger conditions; may be required depending on selective logic.
  - **Content**: the actual prompt text sent to the AI.
  - **Insertion Order**: determines insertion priority order; lower values are inserted higher and thus may get less attention from the model.
  - **Case Sensitivity**: whether keyword matching respects case.
  - **Priority**: determines which entries get removed first if token budget is exceeded.
  - **Selective & Selective Logic**:
    - Can require both primary and secondary keywords.
    - Example: with `Apple` + `Banana` and logic `NOT`, insert if `Apple` is found and `Banana` is not found.
  - **Constant**: always insert the entry regardless of keyword triggers, as long as token budget allows.
  - **Probability**: chance the entry is inserted when triggered.

- **How to use lorebooks**
  - In **Chat Settings**, import a lorebook by path.
  - For character books, **“Use V2 Spec.”** must be enabled.
  - Steps:
    1. Go to **Chat Settings**
    2. Find a lorebook in the **lorebook repository**
    3. Use **Copy Path** from the card’s kebab menu
    4. Paste the path into the field and confirm
  - Example path format: `lorebooks/bartelby/example-lorebook`

### Assessment
This is a **tutorial/reference** page with medium durability: the core concept of keyword-triggered lorebooks is fairly stable, but the instructions are tied to Chub AI’s current UI, settings names, and “Use V2 Spec” workflow, so some details may change over time. The content is fairly dense and practical, with specific terms and configuration fields that make it useful for **refer-back** use rather than a one-time skim. It appears to be a **primary source** documentation page from Chub AI, which makes it directly relevant and generally trustworthy for its own platform. Scrape quality is **good** overall: the main text and structure are captured, though the page includes image placeholders rather than the actual screenshots, so some UI detail is lost.
