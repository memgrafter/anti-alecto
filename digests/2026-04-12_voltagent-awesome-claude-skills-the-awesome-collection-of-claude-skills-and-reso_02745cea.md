---
url: https://github.com/VoltAgent/awesome-claude-skills
title: 'VoltAgent/awesome-claude-skills: The awesome collection of Claude Skills and resources.'
scraped_at: '2026-04-12T09:43:50Z'
word_count: 10528
raw_file: raw/2026-04-12_voltagent-awesome-claude-skills-the-awesome-collection-of-claude-skills-and-reso_02745cea.txt
tldr: A large curated GitHub index of 1,086+ Claude Skills and related agent-skill resources, organized by vendor, domain, and tool compatibility, with explicit security warnings and path conventions for multiple AI coding assistants.
key_quote: Unlike many bulk-generated skill repositories, this collection focuses on real-world Agent Skills created and used by actual engineering teams, not mass AI-generated stuff.
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Anthropic
- VoltAgent
- Composio
- Supabase
- Google Gemini
- Google Labs
- Google Workspace CLI
- Stripe
- Courier
- CallStack
- Better Auth
- Tinybird
- HashiCorp
- Sanity
- Firecrawl
- Neon
- ClickHouse
- Remotion
- Replicate
- Typefully
- Vercel
- Cloudflare
- Netlify
- Hugging Face
- Trail of Bits
- Sentry
- Microsoft
- fal.ai
- WordPress
- OpenAI
- Figma
- Binance
- Notion
- Resend
- Addy Osmani
- Corey Haines
- Kim Barrett
- Dean Peters
- Paweł Huryn
- Garry Tan
tools:
- Claude Code
- Codex
- Antigravity
- Gemini CLI
- Cursor
- GitHub Copilot
- OpenCode
- Windsurf
- n8n
libraries:
- Playwright
- React
- Tailwind
- PptxGenJS
- OpenXML SDK
- FastAPI
- Zustand
companies:
- VoltAgent
- Anthropic
- Composio
- Supabase
- Google
- Stripe
- Courier
- CallStack
- Better Auth
- Tinybird
- HashiCorp
- Sanity
- Firecrawl
- Neon
- ClickHouse
- Remotion
- Replicate
- Typefully
- Vercel
- Cloudflare
- Netlify
- Hugging Face
- Trail of Bits
- Sentry
- Microsoft
- fal.ai
- WordPress
- OpenAI
- Figma
- Binance
- Notion
- Resend
- Google Chrome
- Y Combinator
tags:
- agent-skills
- curated-index
- ai-coding-assistants
- security-notice
- developer-resources
---

### TL;DR
A large curated GitHub index of 1,086+ Claude Skills and related agent-skill resources, organized by vendor, domain, and tool compatibility, with explicit security warnings and path conventions for multiple AI coding assistants.

### Key Quote
"Unlike many bulk-generated skill repositories, this collection focuses on real-world Agent Skills created and used by actual engineering teams, not mass AI-generated stuff."

### Summary
- This is a **curated directory/repository** of agent skills, not a single skill itself.
- It claims to be **hand-picked** and focused on “real-world Agent Skills” from engineering teams and communities rather than bulk AI-generated content.
- The repository lists **official skills** from many organizations, including:
  - Anthropic / Claude
  - VoltAgent
  - Composio
  - Supabase
  - Google Gemini / Google Labs / Google Workspace CLI
  - Stripe
  - Courier
  - CallStack
  - Better Auth
  - Tinybird
  - HashiCorp / Terraform
  - Sanity
  - Firecrawl
  - Neon
  - ClickHouse
  - Remotion
  - Replicate
  - Typefully
  - Vercel
  - Cloudflare
  - Netlify
  - Hugging Face
  - Trail of Bits
  - Sentry
  - Microsoft
  - fal.ai
  - WordPress
  - OpenAI
  - Figma
  - Binance
  - Notion
  - Resend
  - Addy Osmani / Google Chrome web quality
  - MongoDB
- The repo states it is compatible with multiple agents/tools:
  - Claude Code
  - Codex
  - Antigravity
  - Gemini CLI
  - Cursor
  - GitHub Copilot
  - OpenCode
  - Windsurf
  - and others
- The page is structured as an **index with many headings and bullet lists**, covering:
  - Official Claude Skills
  - Skills by individual companies/teams
  - Community skills
  - Context engineering
  - Specialized domains
  - n8n automation
- It also includes a long list of **community-contributed skills**, grouped by topic such as:
  - Vector databases
  - Marketing
  - Productivity and collaboration
  - Development and testing
  - Context engineering
  - Specialized domains
  - n8n automation
- A **security notice** warns that listed skills are only curated, **not audited**:
  - Skills may change after being added
  - Users should review source code and risks themselves
  - It explicitly mentions risks like:
    - prompt injections
    - tool poisoning
    - hidden malware payloads
    - unsafe data handling patterns
  - Suggested tools include:
    - Snyk Skill Security Scanner
    - Agent Trust Hub
- It includes a **path reference table** for where skills belong in different assistants:
  - Antigravity: `.agent/skills/` and `~/.gemini/antigravity/skills/`
  - Claude Code: `.claude/skills/` and `~/.claude/skills/`
  - Codex: `.agents/skills/` and `~/.agents/skills/`
  - Cursor: `.cursor/skills/` and `~/.cursor/skills/`
  - Gemini CLI: `.gemini/skills/` and `~/.gemini/skills/`
  - GitHub Copilot: `.github/skills/` and `~/.copilot/skills/`
  - OpenCode: `.opencode/skills/` and `~/.config/opencode/skills/`
  - Windsurf: `.windsurf/skills/` and `~/.codeium/windsurf/skills/`
- There is a **Skill Quality Standards** section with guidance:
  - Describe skills in third person
  - Use specific keywords
  - Keep top-level metadata under ~100 tokens
  - Keep skill bodies under 500 lines
  - Load large docs on demand
  - Avoid absolute paths
  - Declare scoped tools explicitly
- The repo invites **contributions via PRs**, but says not to submit very fresh skills and prefers **community-adopted, proven** skills.
- It is licensed under **MIT License**.
- The page includes promotional links to VoltAgent and related collections, plus social/banner images.

### Assessment
Durability is **medium**: the general idea of a curated skill index is fairly stable, but the exact repository contents, counts like “1086+,” linked skills, and compatibility/path guidance are tied to current ecosystem versions and could change frequently. Content type is **mixed**, with reference-list structure plus some opinionated curation and a security warning. Density is **high** because the page packs a very large number of named skills, categories, and implementation conventions into one document. Originality is **synthesis**: it aggregates and categorizes skills from many primary sources rather than presenting original technical research. Reference style is **refer-back**: this is most useful as a directory to revisit when looking for a specific skill or provider. Scrape quality is **good** overall—the page structure, headings, lists, warnings, and tables are present—but the embedded images are not informative in text form, and this summary necessarily compresses a very large index of links rather than reproducing every item in full.
