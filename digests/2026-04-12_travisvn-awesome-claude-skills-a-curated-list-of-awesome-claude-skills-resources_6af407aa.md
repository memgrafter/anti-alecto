---
url: https://github.com/travisvn/awesome-claude-skills?tab=readme-ov-file#individual-skills
title: 'travisvn/awesome-claude-skills: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows — particularly Claude Code'
scraped_at: '2026-04-12T09:38:16Z'
word_count: 2509
raw_file: raw/2026-04-12_travisvn-awesome-claude-skills-a-curated-list-of-awesome-claude-skills-resources_6af407aa.txt
tldr: A curated, regularly updated GitHub directory of official and community Claude Skills, explaining what Skills are, how they work, how to create them, and how they compare to prompts, projects, subagents, and MCP.
key_quote: Claude Skills teach Claude how to **perform tasks in a repeatable way**
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Jesse Vincent
- Simon Willison
- Travisvn
tools:
- Claude Code
- Playwright
- Skill_Seekers
- ffuf
- CodeQL
- Semgrep
libraries:
- anthropic
companies:
- Anthropic
- Expo
- Trail of Bits
- shadcn/ui
tags:
- claude-skills
- claude-code
- ai-workflows
- prompt-engineering
- model-context-protocol
---

### TL;DR
A curated, regularly updated GitHub directory of official and community Claude Skills, explaining what Skills are, how they work, how to create them, and how they compare to prompts, projects, subagents, and MCP.

### Key Quote
“Claude Skills teach Claude how to **perform tasks in a repeatable way**”

### Summary
- **What this page is**
  - A README for **travisvn/awesome-claude-skills**, a curated list of Claude Skills, resources, and tools for customizing Claude workflows, especially **Claude Code**.
  - Badge indicates it was **updated Feb 2026**.
  - The page is organized into:
    - Introduction to Skills
    - Getting started
    - Official skills
    - Community skills
    - Creating your first skill
    - Docs/resources
    - Recent updates
    - Comparisons to other approaches
    - Tutorials/blog posts
    - Security
    - Troubleshooting
    - FAQ

- **What Claude Skills are**
  - Skills are **specialized folders** containing instructions, scripts, and resources.
  - They are discovered and loaded dynamically when relevant.
  - Purpose: make Claude do tasks in a **repeatable**, procedural way.

- **How Skills work**
  - The README describes a **progressive disclosure architecture**:
    - **Metadata loading**: about **100 tokens** to scan available skills.
    - **Full instructions**: under **5k tokens** when a skill is relevant.
    - **Bundled resources**: files/executable code load only when needed.
  - This keeps multiple skills available without filling the context window.

- **Getting started**
  - **Claude.ai web**
    - Go to **Settings > Capabilities**
    - Enable **Skills**
    - Browse/upload skills
    - For **Team/Enterprise**, an admin must enable Skills org-wide first
  - **Claude Code CLI**
    - Add marketplace skills:
      - `/plugin marketplace add anthropics/skills`
    - Add a local skill:
      - `/plugin add /path/to/skill-directory`
  - **Claude API**
    - Skills are available via **`/v1/skills`**
    - Links to the Skills API docs and includes a short Python snippet using `anthropic.Client`

- **Official Skills listed**
  - **Document skills**: `docx`, `pdf`, `pptx`, `xlsx`
  - **Design & creative**: `algorithmic-art`, `canvas-design`, `slack-gif-creator`
  - **Development**: `frontend-design`, `web-artifacts-builder`, `mcp-builder`, `webapp-testing`
  - **Communication**: `brand-guidelines`, `internal-comms`
  - **Skill creation**: `skill-creator`
  - Each entry gives a short capability description, e.g.:
    - `pdf`: extract text/tables, create/merge/split PDFs, handle forms
    - `frontend-design`: avoid generic “AI slop” and make bold design decisions
    - `mcp-builder`: guide for high-quality MCP servers

- **Community skills**
  - Warns that Skills can execute **arbitrary code** in Claude’s environment.
  - Highlights collections/libraries like:
    - **`obra/superpowers`**: a core skills library for Claude Code with 20+ skills; includes commands like `/brainstorm`, `/write-plan`, `/execute-plan`
    - **`obra/superpowers-lab`**: experimental skills that may change over time
  - Individual skills listed include:
    - iOS simulator automation
    - ffuf web fuzzing for pentesting
    - Playwright browser automation
    - d3.js visualization
    - scientific workflows
    - web asset generation
    - autonomous startup orchestration (`loki-mode`)
    - Trail of Bits security skills
    - frontend slide generation
    - Expo skills
    - shadcn/ui context/pattern enforcement
  - Tool listed:
    - **`Skill_Seekers`** for converting documentation websites into Claude Skills

- **Creating a new skill**
  - Recommends using **`skill-creator`** as the easiest path.
  - Manual skill structure:
    - `my-skill/`
      - `SKILL.md`
      - `scripts/`
      - `resources/`
  - `SKILL.md` needs YAML frontmatter with:
    - `name`
    - `description`
  - Best practices:
    - Keep descriptions concise
    - Write clear actionable instructions
    - Include examples
    - Version with git tags
    - Document dependencies
    - Test thoroughly

- **Documentation and resources**
  - Official getting-started links:
    - “What are Skills?”
    - “Using Skills in Claude”
  - Official docs/resources:
    - Claude Skills announcement
    - Engineering deep dive: “Equipping Agents with Skills”
    - Claude Developer Platform docs
    - Skills API docs
    - Official `anthropics/skills` repo
    - Claude Cookbooks skills examples

- **Recent updates**
  - **Nov 13, 2025**: Anthropic published **Skills Explained**
  - **Oct 16, 2025**: Claude Skills officially announced
  - **Oct 16, 2025**: Initial skills released
  - **Oct 18, 2025**: Community repo **obra/superpowers** emerged
  - **Oct 17, 2025**: Tutorials appeared on DEV.to and Medium

- **Skills vs other approaches**
  - Quick comparison table:
    - **Skills**: reusable procedural knowledge
    - **Prompts**: one-time instructions
    - **Projects**: persistent workspace knowledge
    - **Subagents**: independent task execution with restricted tool access
    - **MCP**: external data/API integration
  - Key guidance:
    - Use Skills when you want portable expertise across Claude instances
    - Use Subagents for independent workflows and permissions
    - Skills and MCP can be combined
  - Additional comparisons:
    - Skills vs MCP: Skills are task workflows; MCP is for external integration
    - Skills vs system prompts: Skills are structured, reusable, on-demand, and composable

- **Tutorials and articles**
  - Written tutorials:
    - “How to Create Your First Claude Skill”
    - “How to Use Skills in Claude Code”
  - Articles/blog posts:
    - Official “Skills Explained”
    - Simon Willison’s technical analysis of Claude Skills

- **Security and trust**
  - Strong warning: **only install skills from trusted sources**
  - Suggested practices:
    - Review `SKILL.md` and scripts
    - Audit before production/enterprise use
    - Use version control and code review
    - Apply least privilege
    - Test in non-production
  - Notes specific risks:
    - Malicious code
    - Prompt injection amplification
    - Sandboxing limitations
  - Mentions a security research article titled **“Weaponizing Claude Code Skills”**

- **Troubleshooting**
  - Common issues:
    - Skills not appearing: check Capabilities settings and admin enablement
    - Skills not loading: verify YAML frontmatter and file structure
    - Permission errors: check admin settings and file permissions
    - Execution failures: inspect dependencies and logs
  - Known issue mentioned:
    - **Linux path bug (Oct 18, 2025)** in Agent SDK using hardcoded macOS paths
  - Help resources:
    - Official skills repo issues
    - Claude docs
    - Community discussions

- **FAQ highlights**
  - Skills use about **100 tokens** for scanning and under **5k tokens** when loaded.
  - Skills and Agent Skills are the same thing.
  - Skills are available for **Pro, Max, Team, and Enterprise**; **free tier does not have access**.
  - Skills can call external APIs through scripts, though MCP may be better for complex integration.
  - No additional cost beyond Claude subscription for official skills.
  - No official paid marketplace yet.

### Assessment
This is a **mixed reference/guide** page with a strong practical focus and decent density: it mixes official docs, community listings, tutorials, comparisons, and security guidance into a single curated README. **Durability: medium** because the core concepts of Claude Skills are likely to last, but many details are version- and release-dependent (e.g. the Feb 2026 update badge, November/October 2025 news, current URLs, and specific community repos). **Content type: mixed** with reference, tutorial, and announcement elements. **Originality: synthesis** rather than primary research, since it aggregates official docs, community resources, and external articles. **Reference style: refer-back**—useful for locating a skill, checking installation paths, or comparing Skills to MCP/subagents. **Scrape quality: good**; the text appears complete enough to preserve the major sections, though images and any interactive GitHub rendering/details blocks may not be fully represented.
