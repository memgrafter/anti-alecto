---
url: https://www.reddit.com/r/PygmalionAI/comments/13ckrrr/how_do_i_export_and_import_a_chat_from_sillytavern/
title: 'how do i export and import a chat from sillytavern? : PygmalionAI'
scraped_at: '2026-04-19T21:25:37Z'
word_count: 339
raw_file: raw/2026-04-19_how-do-i-export-and-import-a-chat-from-sillytavern-pygmalionai_6e1a0578.txt
tldr: 'A Reddit thread in r/PygmalionAI about moving SillyTavern chats after reinstalling/updating: `u/throwaway_is_the_way` says to copy the old `public/chats` folder into the new SillyTavern folder, while `u/Professional_Ad_9436` only explains how to export chats from the UI and says they don’t know how to import them.'
key_quote: Copy and paste the old chats folder into the updated sillytavern folder.
durability: medium
content_type: mixed
density: low
originality: commentary
reference_style: skim-once
scrape_quality: good
people:
- u/nagitokomaeda2
- u/Professional_Ad_9436
- u/throwaway_is_the_way
tools:
- SillyTavern
libraries: []
companies: []
tags:
- sillytavern
- chat-migration
- reddit-support
- data-export
- file-structure
---

### TL;DR
A Reddit thread in r/PygmalionAI about moving SillyTavern chats after reinstalling/updating: `u/throwaway_is_the_way` says to copy the old `public/chats` folder into the new SillyTavern folder, while `u/Professional_Ad_9436` only explains how to export chats from the UI and says they don’t know how to import them.

### Key Quote
"Copy and paste the old chats folder into the updated sillytavern folder."

### Summary
- **Context / problem**
  - The original poster, `u/nagitokomaeda2`, had installed the new version of SillyTavern after an update.
  - Their created characters were missing in the new install, but they were able to export/import characters.
  - They specifically wanted to know how to export and import the chat history as well.

- **Top comment (verbatim):** "Sillytavern folder -> public folder -> chats folder. Copy and paste the old chats folder into the updated sillytavern folder. For future reference, the 'characters' folder in public also has all your old characters."
- **Top commenter:** `u/throwaway_is_the_way`
- **Thread topics:**
  - How to migrate SillyTavern chat histories after updating/reinstalling
  - Where SillyTavern stores chat files on disk
  - Whether chats can be exported/imported through the UI
  - Preserving old characters as well as chats during migration

- **Main answers given**
  - `u/Professional_Ad_9436` says that on phone you can use **“manage chat files”** and then click the small export icon (described as a sheet with an arrow “out”) to export chats.
  - That commenter explicitly says they **do not know how to import chats**.
  - `u/throwaway_is_the_way` gives the practical file-path answer:
    - go to the SillyTavern folder
    - then `public`
    - then `chats`
    - copy the old `chats` folder into the updated SillyTavern install
  - They also note that `public/characters` contains the old characters too.

- **What the thread is useful for**
  - If you want a quick migration fix for SillyTavern, the main actionable advice is to copy the old `public/chats` folder over.
  - The thread also confirms that at least one user knows the export UI path, but the import process is not clearly explained in the replies here.

### Assessment
This is a low-stakes, practical **mixed** thread with a narrow support question and a short answer set. **Durability** is medium: the folder path concept may stay useful, but it depends on SillyTavern’s current file structure and could change with future versions. **Content type** is mostly tutorial/help, with a little peer-to-peer commentary. **Density** is low-to-medium: only a couple of comments, but the file-path answer is specific and actionable. **Originality** is mostly community commentary and troubleshooting rather than primary documentation. **Reference style** is skim-once to refer-back for a quick migration fix. **Scrape quality** is good for the visible thread content: the post and both prominent replies are captured, with no obvious missing sections in the supplied text.
