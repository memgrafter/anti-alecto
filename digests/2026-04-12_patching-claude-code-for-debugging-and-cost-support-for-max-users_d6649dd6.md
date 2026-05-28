---
url: https://mariozechner.at/posts/2025-08-06-cc-antidebug/
title: Patching Claude Code for debugging and /cost support for Max users
scraped_at: '2026-04-12T07:26:08Z'
word_count: 709
raw_file: raw/2026-04-12_patching-claude-code-for-debugging-and-cost-support-for-max-users_d6649dd6.txt
tldr: The post shows how the author patched Claude Code to bypass its anti-debugging checks and to make `/cost` display token usage for Max users, then packaged the patch as an npm tool called `@mariozechner/cc-antidebug`.
key_quote: Claude Code will update every now and then. You'll need to reapply the patch.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mario Zechner
tools:
- Claude Code
- Biome
- npm
- npx
- VS Code
libraries: []
companies:
- Claude
tags:
- debugging
- nodejs
- cli-tools
- npm-packages
- reverse-engineering
---

### TL;DR
The post shows how the author patched Claude Code to bypass its anti-debugging checks and to make `/cost` display token usage for Max users, then packaged the patch as an npm tool called `@mariozechner/cc-antidebug`.

### Key Quote
"Claude Code will update every now and then. You'll need to reapply the patch."

### Summary
- The author says Claude Code is useful but has two “annoyances”:
  - it exits when it detects debugging-related environment variables, which breaks Node.js debugging workflows
  - the `/cost` command hides token usage and cost details for Pro/Max users instead of showing them
- The debugging issue appears when using the Claude Code TypeScript SDK from a Node.js app:
  - the SDK spawns Claude Code as a child process
  - debugger-related env vars inherited from tools like VS Code’s JavaScript Debug Terminal trigger Claude Code’s anti-debugging check
  - Claude Code then immediately exits
- The `/cost` issue is that when signed in with a Pro or Max plan, Claude Code suppresses cost info and shows a message indicating the plan already covers usage
- The author’s method is to treat Claude Code like a patchable binary:
  - format the executable with Biome to make the code readable
  - search for strings and checks related to debugging, such as `--inspect-brk`
  - locate the anti-debugging function and replace the checks with no-ops using regex-based patching
  - do the same for the `/cost` message by finding the string `"With your Claude Max subscription, no need to monitor cost — your subscription includes Claude Code usage"` and replacing the logic so cost/token usage is shown
- The resulting tool is **`cc-antidebug`**, published on npm
- It supports two usage modes:
  - **CLI patch/restore**
    - `npx @mariozechner/cc-antidebug patch`
    - `npx @mariozechner/cc-antidebug restore`
  - **Programmatic use in Node.js**
    - `npm install @mariozechner/cc-antidebug`
    - import `patchClaudeBinary` and `restoreClaudeBinary`
    - patch before debugging, restore afterward
- The author notes that Claude Code updates over time, so patches may need to be reapplied after upgrades
- The post ends by suggesting that once patched, Claude Code can even be debugged interactively and modified further if other annoyances are found

### Assessment
This is a mixed technical/opinion post with a strong hands-on tutorial flavor and a humorous, irreverent tone. Durability is **medium**: the general ideas about patching minified JavaScript and working around debugger detection are broadly useful, but the specifics are tied to Claude Code behavior and the 2025-08-06 version context. Content density is **medium-high**, with concrete commands, package names, and implementation details, though some of the prose is playful and less operationally precise. It is a **primary source** for the author’s own tool and approach rather than a synthesis of external research. It works best as a **refer-back** reference if you want the package name, commands, or the general patching strategy. Scrape quality is **good**: the main sections, code snippets, commands, and key claims are present, and no obvious major sections appear missing.
