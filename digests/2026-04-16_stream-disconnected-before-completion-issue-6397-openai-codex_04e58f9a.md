---
url: https://github.com/openai/codex/issues/6397
title: 'Stream disconnected before completion · Issue #6397 · openai/codex'
scraped_at: '2026-04-16T03:58:50Z'
word_count: 389
raw_file: raw/2026-04-16_stream-disconnected-before-completion-issue-6397-openai-codex_04e58f9a.txt
tldr: A closed Codex CLI bug report about intermittent “stream disconnected before completion” errors, seemingly triggered around image uploads and later treated as stale/possibly duplicate, with support asking users to file `/feedback` and include logs/session details.
key_quote: 'stream disconnected before completion: An error occurred while processing your request. You can retry your request, or contact us through our help center at help.openai.com if the error persists.'
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- rajan-openai
- nos1609
- crimpproduction
- etraut-openai
- codeofdusk
tools:
- codex-cli
- VS Code
- Codex Action
libraries: []
companies:
- OpenAI
- GitHub
- Azure
tags:
- bug-report
- codex-cli
- error-handling
- image-upload
- azure
---

### TL;DR
A closed Codex CLI bug report about intermittent “stream disconnected before completion” errors, seemingly triggered around image uploads and later treated as stale/possibly duplicate, with support asking users to file `/feedback` and include logs/session details.

### Key Quote
"stream disconnected before completion: An error occurred while processing your request. You can retry your request, or contact us through our help center at help.openai.com if the error persists."

### Summary
- **Issue metadata**
  - GitHub issue: **openai/codex #6397**
  - Title: **“Stream disconnected before completion”**
  - State: **closed**
  - Author: **rajan-openai**
- **Environment reported**
  - **codex-cli 0.56.0**
  - **ChatGPT Enterprise** subscription, signing in with ChatGPT
  - Model: **gpt-5-codex-mini medium**
  - Platform: **Darwin 24.6.0 arm64 arm**
- **Bug description**
  - The user saw: **“stream disconnected before completion”**
  - Full message included: **“An error occurred while processing your request. You can retry your request, or contact us through our help center at help.openai.com if the error persists.”**
  - A **request ID** was provided: **9533aa9c-0b12-47f6-bf85-773edc1f24fa**
- **Reproduction notes**
  - The issue started when the user **uploaded an image**, though they were **unsure whether that was the trigger**
  - Uploaded thread ID: **019a63b6-9bb3-7201-ad62-f4c3f9cfb9d8**
- **Expected behavior**
  - The command should have run normally
- **Additional context from comments**
  - GitHub Actions flagged likely duplicates: **#5130, #5037, #4983, #4381**
  - Another user reported the error happening **roughly everyday, same time this week**
  - A separate commenter said they saw the same error in **VS Code**
  - The original reporter later said the error **stopped appearing**
  - OpenAI staff requested users run **`/feedback`** in the CLI to send logs and session details
  - The issue was marked **stale** and **closed**
  - A later commenter said they saw a similar intermittent issue on **Azure**, with **“response.failed event received”**
  - Staff replied that since the report was closed, users should open a **new bug report** with logs and thread ID, and also consider reporting to the **Azure team**
- **Practical takeaway**
  - This looks like an **intermittent service/runtime failure**, not a deterministic CLI bug
  - The most actionable advice in the thread is to **use `/feedback`**, include **logs/session details**, and reference the **thread ID**
  - The comments suggest it may have overlapped with **similar duplicate issues** and possibly **Azure-related behavior**

### Assessment
This is a **mixed** content item: primarily an **announcement/bug report** with troubleshooting comments. Durability is **medium** because the specific issue is tied to a particular Codex CLI version (**0.56.0**) and may become stale, but the pattern of “stream disconnected before completion” and the recommended debugging workflow (`/feedback`, logs, thread ID) remain useful. Density is **medium**: it contains concrete environment details, error strings, IDs, and resolution notes, but little deep diagnosis. Originality is mostly **primary source** since it captures the reporter’s exact issue and staff responses, though some comments are clearly support guidance. It’s best used as **refer-back** material for matching a similar error, checking whether it was already reported, or recalling the suggested escalation path. Scrape quality is **good**: the key fields, body, and top comments are present, though there’s no evidence of missing code blocks or images beyond the referenced upload/thread.
