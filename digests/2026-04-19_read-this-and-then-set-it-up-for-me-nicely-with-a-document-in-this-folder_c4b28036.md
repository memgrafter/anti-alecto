---
url: https://dicklesworthstone.github.io/misc_coding_agent_tips_and_scripts/cc_session_making_encrypted_gh_issues_system.html
title: Read this and then set it up for me nicely with a document in this folder…
scraped_at: '2026-04-19T07:00:31Z'
word_count: 821
raw_file: raw/2026-04-19_read-this-and-then-set-it-up-for-me-nicely-with-a-document-in-this-folder_c4b28036.txt
tldr: For public GitHub issues carrying secret content, the recommended off-the-shelf open-source approach is age with X25519 recipient keys, because it’s simpler than GPG, works well on Ubuntu, and is easy for agents to detect and decrypt locally.
key_quote: The best practical answer is age.
durability: high
content_type: tutorial
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people: []
tools:
- age
- GPG/OpenPGP
- SOPS
- minisign
- libsodium
- NaCl box
- Codex
libraries: []
companies:
- GitHub
tags:
- encryption
- github-issues
- public-key-cryptography
- ubuntu
- automation
---

### TL;DR
For public GitHub issues carrying secret content, the recommended off-the-shelf open-source approach is **age** with **X25519 recipient keys**, because it’s simpler than GPG, works well on Ubuntu, and is easy for agents to detect and decrypt locally.

### Key Quote
“The best practical answer is age.”

### Summary
- The piece argues for using **age** as the best practical encryption tool for a workflow where:
  - people post **public GitHub issues**,
  - the issue body contains an **encrypted message**,
  - an Ubuntu-based coding agent detects the encrypted block and decrypts it locally.
- The recommended model is **public-key encryption**, not sending a decryption key out of band:
  - you generate a long-term **age keypair**,
  - share the **public recipient key** (`age1...`) publicly,
  - senders encrypt messages to that public key,
  - your agent decrypts with your **private key** stored locally.
- Why age is preferred:
  - It is described as a **simple, modern and secure encryption tool**.
  - It uses **X25519** recipient keys, which satisfy the ECC requirement.
  - It is **CLI-friendly** and fits Unix-style automation.
  - It is considered operationally much easier than **GPG/OpenPGP** for “paste into an issue and decrypt automatically” workflows.
  - It is supported in adjacent tooling like **SOPS**, which explicitly recommends age over PGP when possible.
- Tools and alternatives discussed:
  - **GPG/OpenPGP**: technically possible, but too fragile and cumbersome for this use case.
  - **minisign**: not suitable because it is for **signing**, not encryption.
  - Custom ECC using **libsodium/NaCl box**: possible, but not the easiest off-the-shelf path because you’d need to build your own format and workflow.
- Suggested practical setup:
  - Install `age` on Ubuntu.
  - Store the private key somewhere like `~/.config/age/issuebot.key`.
  - Have agents scan issue bodies/comments for the marker:
    - `-----BEGIN AGE ENCRYPTED FILE-----`
  - If found, extract the armored block and decrypt with:
    - `age -d -i ~/.config/age/issuebot.key`
- Suggested sender workflow:
  - Publish your public key in your repo README.
  - Sender encrypts locally with:
    - `age -a -r age1yourpublickeyhere -o secret.age.txt plaintext.txt`
  - The `-a` flag produces **armored output**, making it easy to paste into GitHub issues.
- Caveat on security:
  - **Encryption does not prove authorship**.
  - If sender authenticity matters, pair age with a separate signature mechanism such as **minisign** or **SSH signing**.
- Bottom line:
  - Use **age + X25519** for encryption.
  - Optionally add **signatures** for authenticity.
  - This is presented as the best mix of **modern ECC, open source, Ubuntu automation, and simplicity**.

### Assessment
This is a **tutorial/opinion mix** with moderate-to-high density: it gives a concrete recommendation, rationale, and example commands/workflow rather than a broad survey. Durability is **medium-high** because the core guidance is about stable crypto/tooling tradeoffs, though specific tooling recommendations could age if ecosystem support changes. The content is primarily **commentary/synthesis** rather than original research, drawing on age, SOPS, and related tooling. It is best used as a **refer-back** reference if you’re designing a similar encrypted GitHub-issue workflow, especially for Ubuntu-based automation. Scrape quality appears **good**: the key ideas, commands, caveats, and alternatives are included, and nothing obvious seems missing beyond any external links or visuals.
