---
url: https://docs.sillytavern.app/usage/core-concepts/worldinfo/
title: World Info | docs.ST.app
scraped_at: '2026-04-11T04:57:16Z'
word_count: 4676
raw_file: raw/2026-04-11_world-info-docs-st-app_b6f47652.txt
tldr: World Info (Lorebooks) in SillyTavern is a dynamic prompt injection system that inserts specific text blocks into the AI's context based on keyword triggers, regex patterns, or vector similarity, with granular controls over activation probability, position, budget, and recursion.
key_quote: It functions like a dynamic dictionary that only inserts relevant information from World Info entries when keywords associated with the entries are present in the message text.
durability: medium
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- kingbri
- Alicat
- Trappu
tools:
- SillyTavern
- Vector Storage
- Quick Replies
- JavaScript
libraries: []
companies: []
tags:
- sillytavern
- world-info
- prompt-engineering
- context-management
- regex
---

### TL;DR
World Info (Lorebooks) in SillyTavern is a dynamic prompt injection system that inserts specific text blocks into the AI's context based on keyword triggers, regex patterns, or vector similarity, with granular controls over activation probability, position, budget, and recursion.

### Key Quote
"It functions like a dynamic dictionary that only inserts relevant information from World Info entries when keywords associated with the entries are present in the message text."

### Summary
**Core Concept**
World Info (WI) dynamically inserts lore or instructions into the prompt when specific triggers (keywords, regex) appear in the chat. It acts as a supplemental context manager to guide the AI without guaranteeing output.

**Lore Sources**
Lorebooks can be attached at different levels, activated in this order:
1.  **Chat Lore:** Specific to a single conversation.
2.  **Persona Lore:** Active whenever a specific user persona is selected.
3.  **Character Lore:** Bound to a specific character card (embeddable).
4.  **Global Lore:** Default fallback lore.

*Insertion Strategy:* Can be set to "Sorted Evenly" (mixed), "Character Lore First," or "Global Lore First."

**Entry Configuration**
- **Keys:** Keywords or JavaScript-style regex (e.g., `/(?:rain|storm)/i`). Regex supports `\x01` prefix to target specific speakers.
- **Optional Filters:** Logic gates (AND ANY/ALL, NOT ANY/ALL) to refine triggers.
- **Content:** The actual text injected into the prompt.
- **Insertion Order:** Numeric priority (lower numbers first).
- **Insertion Position:** Before/After Char Defs, Before/After Examples, Top/Bottom of Author's Note, specific Depth, or specific Roles (System/User/Assistant).
- **Outlets:** Stores content in a named variable (e.g., `{{outlet::Name}}`) for manual placement in the prompt via macros.
- **Strategy:**
    - 🔵 Constant (always on).
    - 🟢 Normal (keyword triggered).
    - 🔗 Vectorized (similarity matching via Vector Storage extension).
- **Probability:** % chance to insert if triggered (0-100).
- **Inclusion Groups:** Ensures only one entry from a group triggers (based on Weight or Priority). Supports "Group Scoring" to favor entries with more keyword matches.
- **Timed Effects:**
    - *Sticky:* Stays active for N messages.
    - *Cooldown:* Cannot trigger for N messages.
    - *Delay:* Waits N messages before becoming eligible.
- **Character Filter:** Restricts activation to specific character names or tags (Include/Exclude mode).
- **Triggers:** Limits activation to specific generation types (Normal, Continue, Swipe, Impersonate, etc.).

**Global Activation Settings**
- **Scan Depth:** How many recent messages to check (0 = disabled/recurse only).
- **Include Names:** Adds speaker names to the scan buffer.
- **Context % / Budget:** Token limit for WI insertion.
- **Recursion:** Allows WI entries to trigger other WI entries.
    - *Modes:* Non-recursable, Prevent further recursion, Delay until recursion.
- **Matching Options:** Case-sensitivity, Whole word matching (breaks languages like Chinese/Japanese if enabled).

**Advanced Features**
- **Vector Storage:** Uses embeddings to match entries semantically instead of via keywords. Requires the Vector Storage extension.
- **Automation ID:** Links WI entry to STscripts/Quick Replies for automated execution.

### Assessment
- **Durability**: Medium. While the core logic of World Info is stable, SillyTavern is actively developed (references v1.12.6), and UI locations or specific extension dependencies may shift over time.
- **Content type**: Reference / Tutorial. It documents software features and configuration options.
- **Density**: High. The text is packed with specific definitions, logic rules (e.g., Inclusion Groups), regex examples, and UI instructions.
- **Originality**: Primary source. This is the official documentation for the software.
- **Reference style**: Refer-back. Users will likely consult this to look up specific settings (e.g., "How does Group Scoring work?") rather than reading it linearly.
- **Scrape quality**: Good. The content appears complete, capturing all sections, logic descriptions, and caveats (like the limitations on Outlets).
