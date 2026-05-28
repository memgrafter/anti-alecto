---
url: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/changing-the-ai-model
title: Changing the AI model for GitHub Copilot coding agent - GitHub Docs
scraped_at: '2026-04-19T07:47:04Z'
word_count: 173
raw_file: raw/2026-04-19_changing-the-ai-model-for-github-copilot-coding-agent-github-docs_e735fa13.txt
tldr: GitHub Docs explains where you can manually choose a model for Copilot cloud/coding agent, and lists the currently supported options, with Auto as the fallback when model picking isn’t available.
key_quote: Where a model picker is not available, Auto will be used automatically.
durability: medium
content_type: reference
density: low
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- GitHub Copilot
- GitHub Mobile
- Raycast
libraries: []
companies:
- GitHub
tags:
- github-copilot
- ai-model-selection
- coding-agent
- documentation
- reference
---

### TL;DR
GitHub Docs explains where you can manually choose a model for Copilot cloud/coding agent, and lists the currently supported options, with Auto as the fallback when model picking isn’t available.

### Key Quote
“Where a model picker is not available, Auto will be used automatically.”

### Summary
- This page is a short GitHub Docs reference for **changing the AI model used by GitHub Copilot cloud agent / coding agent**.
- It notes that **different models may perform better depending on the task**, so model choice can affect response quality.
- **Model selection is only supported in specific entry points**:
  - Assigning an issue to Copilot on **GitHub.com**
  - Mentioning **@copilot** in a pull request comment on **GitHub.com**
  - Starting a task from:
    - the **agents tab**
    - the **agents panel**
    - **GitHub Mobile**
    - the **Raycast launcher**
- If the interface **does not show a model picker**, Copilot will use **Auto** automatically.
- The page references related docs:
  - **About GitHub Copilot cloud agent**
  - **Asking GitHub Copilot to create a pull request**
  - **About Copilot auto model selection**
- Supported model choices listed on the page:
  - **Auto**
  - **Claude Sonnet 4.5**
  - **Claude Opus 4.5**
  - **Claude Opus 4.6**
  - **Claude Opus 4.7**
  - **GPT-5.2-Codex**
- The note on **Auto** says GitHub will choose the best model based on **availability** and to help **reduce rate limiting**.

### Assessment
This is a **reference** page with **high durability** only in the general sense of how model selection works, but the actual model list is **medium/low durability** because it is version- and availability-dependent and will likely change over time. The content is mostly **fact** and very concise, with **low-to-medium density** since it mainly enumerates supported entry points and model names rather than explaining behavior in depth. It appears to be a **primary source** from GitHub Docs, so it is authoritative for current product behavior, though the scrape looks **good** and complete for the visible text, with no missing code blocks or major sections apparent.
