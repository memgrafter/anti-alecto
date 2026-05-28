---
url: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
title: About GitHub Copilot coding agent - GitHub Docs
scraped_at: '2026-04-19T07:46:56Z'
word_count: 1945
raw_file: raw/2026-04-19_about-github-copilot-coding-agent-github-docs_5e831622.txt
tldr: GitHub’s Copilot cloud agent is an autonomous, GitHub Actions–powered coding assistant that can research repos, plan changes, edit code, run tests, and open pull requests, with customization, metrics, and several repository/feature limitations.
key_quote: Copilot cloud agent can work independently in the background to complete tasks, just like a human developer.
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- GitHub Actions
- GitHub Copilot
- GitHub Issues
- Visual Studio Code
- Azure Boards
- JIRA
- Linear
- Slack
- Teams
- MCP
libraries: []
companies:
- GitHub
tags:
- ai-agents
- copilot
- github-actions
- pull-requests
- developer-tools
---

### TL;DR
GitHub’s Copilot cloud agent is an autonomous, GitHub Actions–powered coding assistant that can research repos, plan changes, edit code, run tests, and open pull requests, with customization, metrics, and several repository/feature limitations.

### Key Quote
“Copilot cloud agent can work independently in the background to complete tasks, just like a human developer.”

### Summary
- **What it is**
  - Copilot cloud agent is the renamed “Copilot coding agent.”
  - It works autonomously in a GitHub Actions-powered ephemeral development environment.
  - It can research a repository, create implementation plans, fix bugs, implement features, improve test coverage, update docs, address technical debt, and resolve merge conflicts.

- **How you use it**
  - Trigger it from GitHub.com via the agents panel or other entry points.
  - It can:
    - research, plan, and make changes on a branch before a PR is created,
    - open a new pull request directly from GitHub Issues or Visual Studio Code,
    - respond to `@copilot` comments on existing pull requests,
    - handle security alerts assigned through security campaigns.
  - It evaluates the task based on the prompt you provide.

- **How it works**
  - Copilot gets its own temporary dev environment to explore code, make changes, run tests, and run linters.
  - On GitHub.com, it can do deeper research, planning, and iteration before a PR is opened.
  - In cloud-agent integrations like Azure Boards, JIRA, Linear, Slack, or Teams, it only supports creating a pull request directly.

- **Why it differs from IDE AI assistants**
  - Traditional IDE assistants work locally and still leave many manual steps to the developer: branching, committing, pushing, opening PRs, writing descriptions, and iterating.
  - Copilot cloud agent does those steps on GitHub, making work more transparent and easier to collaborate on.
  - Every step is captured in commits and logs, and teams can inspect the process.

- **Cloud agent vs. IDE agent mode**
  - Cloud agent: runs in GitHub Actions, works from issues or Copilot Chat prompts, can research, plan, edit a branch, and optionally open a PR.
  - IDE agent mode: makes autonomous edits directly in your local development environment.

- **Common workflow uses**
  - Offload straightforward backlog issues by assigning “Copilot” as assignee.
  - Use it for “nice to have” improvements like refactors, logging, or test coverage.
  - Have it start scaffold work that you later continue manually.
  - Use it for repository research and planning before writing code.
  - Create custom agents specialized for roles like frontend, documentation, or testing.

- **Measurement and admin reporting**
  - Enterprise admins and organization owners can use Copilot usage metrics APIs to track:
    - number of PRs created and merged,
    - PRs created by Copilot cloud agent that were merged,
    - median time to merge.
  - These metrics help assess adoption and throughput impact.

- **Integrations and availability**
  - It can be invoked from third-party tools via Copilot integrations.
  - It must be enabled before use.
  - Available on GitHub Copilot Pro, Pro+, Business, and Enterprise.
  - Business and Enterprise require admin policy enablement.
  - Repository owners can opt repositories out.

- **Model selection and repository knowledge**
  - Depending on how the task is started, you may be able to choose the AI model.
  - You can improve its effectiveness with:
    - **custom instructions** stored in repo files or org settings,
    - **Copilot Memory** (public preview, Pro/Pro+), which stores useful repo-specific details.

- **Customization options**
  - **Custom instructions**: guide build/test/validation behavior.
  - **MCP servers**: connect external data sources and tools.
  - **Custom agents**: specialized variants for different work.
  - **Hooks**: run shell commands at key execution points for validation, logging, scanning, or automation.
  - **Skills**: add specialized instructions, scripts, and resources.

- **Usage costs**
  - Uses GitHub Actions minutes and Copilot premium requests.
  - Work within monthly allowances without extra charges.

- **Important limitations**
  - Can only modify one repository per task.
  - By default, it only sees context from the repository it’s working on.
  - Can only work on one branch and one pull request per task.
  - May be blocked by some rulesets or branch protection rules, especially rules about commit authors.
  - Does not honor content exclusions; it can see and update files that admins intended Copilot to ignore.
  - Only works with repositories hosted on GitHub.

- **Extra resource**
  - The page ends by pointing to a hands-on exercise: “Expand your team with Copilot cloud agent Skills.”

### Assessment
This is a high-durability reference/doc page with medium-to-high density and mostly factual, product-specific information. It’s primarily a reference for understanding what Copilot cloud agent does, how it differs from IDE agent mode, how to enable/customize it, and what limitations apply. The content is a primary-source GitHub doc, so it’s trustworthy, but some details are version- and product-plan-dependent and could change over time. Best used as a refer-back reference rather than a one-time skim, especially for setup, capabilities, and constraints. Scrape quality is good overall: the main sections and bullet points are present, though any linked subpages, screenshots, or deeper procedural examples are not included here.
