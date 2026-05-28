---
url: https://github.com/fakoli/sekoudoumbouya
title: 'fakoli/sekoudoumbouya: Building bridges between bytes – infrastructure case studies & technical musings'
scraped_at: '2026-04-19T08:23:42Z'
word_count: 487
raw_file: raw/2026-04-19_fakoli-sekoudoumbouya-building-bridges-between-bytes-infrastructure-case-studies_4bcdb5cd.txt
tldr: README for Sekou Doumbouya’s Astro-based portfolio site, covering setup, content organization, deployment options, dynamic GitHub data fetching, and an `llms.txt` file for AI-friendly parsing.
key_quote: “Building bridges between bytes – infrastructure case studies & technical musings”
durability: medium
content_type: reference
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Sekou Doumbouya
tools:
- Astro
- Tailwind CSS
- GitHub API
- GitHub Pages
- GitHub Actions
- llms.txt
libraries:
- MDX
companies:
- GitHub
tags:
- portfolio-website
- astro
- github-pages
- content-management
- ai-optimization
---

### TL;DR
README for Sekou Doumbouya’s Astro-based portfolio site, covering setup, content organization, deployment options, dynamic GitHub data fetching, and an `llms.txt` file for AI-friendly parsing.

### Key Quote
“Building bridges between bytes – infrastructure case studies & technical musings”

### Summary
- This is the README for a personal portfolio website for Sekou Doumbouya.
- The site is described as:
  - “A high-performance, accessible, and SEO-optimized portfolio website built with Astro”
  - Intended to showcase senior engineering leadership, cloud architecture projects, and technical writing
- Tech stack:
  - Astro 5.0
  - Tailwind CSS
  - MDX and type-safe content collections
  - GitHub Pages / static hosting
  - SEO features including sitemap, Open Graph tags, and JSON-LD structured data
- Getting started:
  - Requires Node.js v18+ and npm or yarn
  - Standard setup is `git clone`, `cd sekoudoumbouya`, `npm install`
  - Development server runs with `npm run dev` at `http://localhost:4321`
  - Production build is `npm run build`, outputting to `dist/`
- Content management:
  - Uses Astro Content Collections for type-safe content
  - Projects live in `src/content/projects/` as `.md` or `.mdx`
    - Required fields: `title`, `publishDate`, `description`, `organization`, `role`, `impactSummary`, `primaryTech`
    - Optional fields: `featured`, `scale`, `outcomes`, `contributions`
  - Blog posts live in `src/content/blog/` as `.md` or `.mdx`
    - Required fields: `title`, `publishDate`, `description`
    - Supports drafts via `draft: true`
  - Experience data is stored in JSON under `src/content/experience/`
- Dynamic GitHub repository data:
  - The homepage “My Projects” section fetches live repository data from the GitHub API at build time
  - Data can include star counts, descriptions, primary language, and topic tags
  - If the API is unavailable or rate-limited, the site falls back to cached static data
  - Adding `GITHUB_TOKEN` to `.env` enables higher-rate-limit live fetching
- Deployment and configuration:
  - Supports both root-domain deployment and GitHub Pages subpath deployment
  - Example env vars:
    - `SITE=https://sekoudoumbouya.com` and `PUBLIC_BASE_PATH=/`
    - `SITE=https://fakoli.github.io/` and `PUBLIC_BASE_PATH=/sekoudoumbouya`
  - Notes GitHub Pages deployment via GitHub Actions or manual configuration
- AI/LLM optimization:
  - Includes `public/llms.txt` to help AI models parse and summarize the professional profile accurately
- License and contribution:
  - Licensed under MIT
  - Contributions are welcomed via `CONTRIBUTING.md`

### Assessment
Durability is **medium** because the general portfolio-site structure, Astro setup, and content organization are stable, but specific implementation details like Astro 5.0, GitHub Pages deployment, and GitHub API behavior can age as the stack evolves. The content type is **reference** with some **tutorial** elements, since it mainly documents how the repository is organized and how to build and deploy it. Density is **medium**: it is compact but includes concrete commands, folder paths, environment variables, and field names. Originality is **primary source**, since this is the project’s own README rather than commentary or aggregation. For usefulness, it is **high** for recall and finding the repository again, and **medium-high** for deciding whether to reread, since it clearly tells you what the repo is and how to work with it without needing the full code immediately. Scrape quality is **good**: the main README content appears fully captured, including setup, content structure, deployment, and AI/LLM notes, with no obvious missing sections from the provided text.
