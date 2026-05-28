---
url: https://docs.sillytavern.app/usage/core-concepts/chatfilemanagement/
title: Chat File Management | docs.ST.app
scraped_at: '2026-04-12T07:21:04Z'
word_count: 448
raw_file: raw/2026-04-12_chat-file-management-docs-st-app_cb5f100e.txt
tldr: SillyTavern’s chat file management docs explain how to import, export, branch, checkpoint, and rename chats, with the key warning that renaming a chat can break checkpoint links because they reference the chat file name.
key_quote: Checkpoints are clones of the current chat, in that they copy all messages from the given chat up to a certain point, and they store a link to the source (by chat file name).
durability: medium
content_type: reference
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- CAI Tools
libraries: []
companies:
- Character.AI
- SillyTavern
tags:
- chat-management
- file-management
- data-export
- chat-import
- checkpoints
---

### TL;DR
SillyTavern’s chat file management docs explain how to import, export, branch, checkpoint, and rename chats, with the key warning that renaming a chat can break checkpoint links because they reference the chat file name.

### Key Quote
“Checkpoints are clones of the current chat, in that they copy all messages from the given chat up to a certain point, and they store a link to the source (by chat file name).”

### Summary
- This page describes the main ways to manage AI chat files in SillyTavern.
- Some of the options are also available in the **“Manage chat files”** dialog, accessible from the **bottom left options menu**.

- **Solo Chats vs Group Chats**
  - A **Solo chat** is the simplest workflow: click a character card and start chatting.
  - You can create a **group chat** using the **“Create New Chat Group”** button.
  - Group chats include multiple characters who interact with each other and with you.

- **Chat import**
  - SillyTavern can import chats from **Character.AI**.
  - For Character.AI chats and bots, the docs recommend the **CAI Tools** browser extension:
    - https://github.com/irsat000/CAI-Tools
  - Other supported import sources listed:
    - **TavernAI (original)** — https://github.com/TavernAI/TavernAI
    - **Text Generation WebUI (oobabooga)** — https://github.com/oobabooga/text-generation-webui
    - **Agnai** — https://github.com/agnaistic/agnai
    - **KoboldAI Lite** — https://github.com/LostRuins/lite.koboldai.net
    - **RisuAI** — https://github.com/kwaroran/RisuAI

- **Export as .jsonl**
  - In **Manage chat files**, each chat entry has an export button.
  - This export format is meant to be **re-imported as-is**.
  - It preserves **all metadata** and is suitable for **sharing or migrating chats**.
  - It **does not include images or file attachments**.
  - Privacy warning: inspect the exported JSONL and remove anything you do not want to share.

- **Export as .txt**
  - There is also a simplified **plain text export** via **“Download chat as plain text document”**.
  - This format is **not re-importable** because it loses important metadata.

- **Checkpoints**
  - Checkpoints are **clones of a chat up to a certain point**.
  - They copy all messages through a selected message and keep a link back to the source chat via **chat file name**.
  - Two creation actions are available from the **three-dots menu** on each message:
    - **Create Branch**: clones the chat up to that message and immediately switches to it.
    - **Create Checkpoint**: clones the chat up to that message, asks for a name, and creates it without switching.
  - The docs compare them to:
    - **Create Branch** = “open link in new tab”
    - **Create Checkpoint** = “open link in new tab in the background”
  - To return to the parent from a checkpoint:
    - Open the **burger menu** next to the message box
    - Click **“Back to parent chat”**

- **Rename Chat**
  - Chats are automatically named with their **start date and time** by default.
  - You can rename a chat by clicking the **pencil icon** and typing a new name.
  - Important limitation: renaming a chat **breaks links from checkpoints**, since they are connected by the chat file name.

### Assessment
This is a **reference** page with some **tutorial** elements, aimed at helping users manage SillyTavern chat files in everyday use. The content is **medium-durability**: the concepts of importing/exporting, branching, and checkpoints are fairly stable, but the exact UI labels and supported tools could change with app versions. It’s **medium-density** and practical, with specific menu paths, feature names, and caveats rather than broad explanation. The page is a **primary source** from the SillyTavern docs, so it’s good for confirming current intended behavior, though it should still be checked against the live UI if you rely on exact controls. As a reference, it’s best used **refer-back** rather than deep study. The scrape quality appears **good**: the main sections and warnings are present, with no obvious missing code blocks or images.
