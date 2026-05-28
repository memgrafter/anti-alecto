---
url: https://github.com/abhinavs/moonwalk
title: 'abhinavs/moonwalk: A fast & minimal Jekyll blog theme with clean dark mode'
scraped_at: '2026-04-12T10:36:51Z'
word_count: 1269
raw_file: raw/2026-04-12_abhinavs-moonwalk-a-fast-minimal-jekyll-blog-theme-with-clean-dark-mode_ea03631d.txt
tldr: Moonwalk is a minimal, fast Jekyll blog theme with built-in light/dark mode, strong SEO/accessibility defaults, optional social/share features, and flexible home-page layouts for blogs, navbars, and portfolio cards.
key_quote: Fast (very minimal CSS) - 100/100 on performance, accessibility, best practices and SEO
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Riccardo Graziosi
- abhinav
tools:
- Jekyll
- Jekyll Feed
- Soopr
- Netlify
- Vercel
- AWS
libraries: []
companies:
- GitHub
- Netlify
- Vercel
- AWS
- Soopr
tags:
- jekyll-theme
- blogging
- dark-mode
- seo
- static-site-generator
---

### TL;DR
Moonwalk is a minimal, fast Jekyll blog theme with built-in light/dark mode, strong SEO/accessibility defaults, optional social/share features, and flexible home-page layouts for blogs, navbars, and portfolio cards.

### Key Quote
“Fast (very minimal CSS) - 100/100 on performance, accessibility, best practices and SEO”

### Summary
- **What it is**
  - An open-source Jekyll theme called **moonwalk**: “a fast and minimalistic blog theme with clean dark mode.”
  - Designed for blogs and personal sites, with a demo linked at `abhinavs.github.io/moonwalk/`.
  - Original base theme is **no style please!** by Riccardo Graziosi.

- **Core features**
  - **Light/dark mode** with a theme switcher that respects `prefers-reduced-motion`.
  - Multiple content layouts:
    - **Vertical list**
    - **Horizontal list**
    - **Card list**
  - Built-in **landing page** support with navbar, footer, and portfolio sections.
  - **Responsive/mobile friendly** and **accessible**:
    - ARIA labels
    - keyboard-friendly navigation
  - **SEO-oriented**:
    - auto-generated sitemap
    - RSS feed via **Jekyll Feed**
  - GitHub-style Markdown Alerts:
    - NOTE, TIP, IMPORTANT, WARNING, CAUTION
  - Optional UI enhancements:
    - reading progress bar
    - back-to-top button
    - previous/next post navigation
    - table of contents via `toc: true`
    - code block copy button
  - Syntax highlighting works in both light and dark mode.
  - Share-related extras via **Soopr**:
    - auto-generated social share images
    - share and like buttons
    - short URLs

- **Performance claim**
  - The theme advertises a **100/100 Lighthouse score** for:
    - performance
    - accessibility
    - best practices
    - SEO
  - A Lighthouse report image is referenced as evidence.

- **Quick installation**
  1. Fork the repository.
  2. `cd moonwalk`
  3. Run `bin/bootstrap`
  4. Optionally sign up for Soopr and add `publish_token` to `_config.yml`
  - Windows note: may require **Ruby 3.0.x** instead of **3.1.x**; a separate Windows installation guide is linked.

- **Running locally**
  - `bin/start` starts a development server at `http://127.0.0.1:4000`

- **Deployment**
  - Can be deployed on cloud/static hosts such as **AWS**, **Netlify**, and **Vercel**.
  - Includes a **Netlify deploy button** for one-click deployment.
  - For gem use or **GitHub Pages**, there is a dedicated guide.

- **Customization**
  - Most site settings are configured in `_config.yml`:
    - blog name
    - author
    - theme appearance (light/dark/auto)
    - date formatting
  - Further layout/CSS customization can be done using standard Jekyll theme overriding.
  - Home page structure is controlled through `_data/home.yml`:
    - **vertical list** entries
    - **card list** (`project_entries`)
    - **horizontal lists** (`navbar_entries`, `footer_entries`)
  - Vertical list entries can nest, link, show post lists, or render plain text.
  - Card entries support `title`, `desc`, `url`, and `highlight`.

- **Built-in layouts**
  - `post` for content
  - `blog` for post listings
  - `home` for the landing page
  - The site’s `index.md` can be switched between `home` and `blog`.

- **Theme styling**
  - The document gives sample CSS variables for customizing:
    - light mode colors
    - dark mode colors
  - This suggests the theme is intentionally easy to retheme without heavy CSS work.

- **Development workflow**
  - `bin/bootstrap` or `make setup` to install dependencies
  - `bin/start` or `make serve` to run the dev server with live reload
  - `bin/build` or `make build` to create a production build
  - Notes that only certain directories are bundled into the theme gem:
    - `_layouts`
    - `_includes`
    - `_sass`
    - `_data`
    - `assets`
  - Custom directories require editing the regexp in `moonwalk.gemspec`.

- **Project context**
  - License: **MIT**
  - Contributing and development instructions are linked.
  - The author also links to several other projects and personal/social pages.

### Assessment
This is a **mixed reference/tool** page with a **highly durable** core idea but some **version-sensitive** implementation details. The content is moderately dense and mostly practical, aimed at users who want to install, customize, or extend a Jekyll theme. It appears to be **primary-source documentation/announcement** from the theme author rather than commentary or aggregation. It is best used as a **refer-back** reference for setup, customization, and feature lookup rather than deep study. Scrape quality is **good**: the main README sections, commands, configuration examples, and code block for GitHub alerts are present, though image assets themselves are only referenced, not embedded.
