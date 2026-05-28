---
url: https://github.com/VenTheZone/pi-dots/blob/main/pi-dotfiles/skills/visual-explainer/SKILL.md
title: pi-dots/pi-dotfiles/skills/visual-explainer/SKILL.md at main · VenTheZone/pi-dots
scraped_at: '2026-04-19T08:26:24Z'
word_count: 5105
raw_file: raw/2026-04-19_pi-dots-pi-dotfiles-skills-visual-explainer-skill-md-at-main-venthezone-pi-dots_9096c7a1.txt
---

### TL;DR
This SKILL.md defines a “visual-explainer” workflow for turning technical content into self-contained, browser-opened HTML pages with strong visual hierarchy, strict anti-slop design rules, and detailed guidance for Mermaid diagrams, tables, timelines, dashboards, and slide decks.

### Key Quote
“Visual is always default.”

### Summary
- **Purpose and scope**
  - The `visual-explainer` skill is meant to generate **beautiful, self-contained HTML pages** that explain systems, code changes, plans, data, comparisons, and technical concepts.
  - It should be used for requests like:
    - diagrams
    - architecture overviews
    - diff reviews
    - plan reviews
    - project recaps
    - comparison tables
    - other visual explanations
  - It also applies proactively when the assistant is about to produce a **complex ASCII table**:
    - 4+ rows or 3+ columns → use HTML instead of terminal box-drawing tables.

- **Metadata / compatibility**
  - Skill name: `visual-explainer`
  - Author: `nicobailon`
  - Version: `0.5.1`
  - License: MIT
  - Requires a browser to view generated HTML.
  - Optional support for **surf-cli** to generate AI images.

- **Core philosophy**
  - “Visual is always default.”
  - Even prose-heavy content should be transformed into a visual structure:
    - cards
    - diagrams
    - grids
    - tables
    - callouts
  - The document repeatedly emphasizes that the goal is **understanding through design**, not dumping text into HTML.

- **Available commands**
  - The skill references prompt templates in `./commands/`.
  - Listed commands include:
    - `generate-web-diagram`
    - `generate-visual-plan`
    - `generate-slides`
    - `diff-review`
    - `plan-review`
    - `project-recap`
    - `fact-check`
    - `share`
  - These can be exposed as slash commands in pi-style workflows.

- **Workflow for creating pages**
  - The assistant should:
    - **Think briefly** and commit to a direction rather than defaulting to a generic style.
    - Determine:
      - who the audience is
      - what kind of content it is
      - what aesthetic to use
  - Must **read reference templates** before generating:
    - `./templates/architecture.html`
    - `./templates/mermaid-flowchart.html`
    - `./templates/data-table.html`
    - `./templates/slide-deck.html`
    - `./references/css-patterns.md`
    - `./references/libraries.md`
    - `./references/responsive-nav.md` for 4+ sections
  - The workflow is intentionally prescriptive: the skill wants repeatable structure without generic-looking output.

- **Rendering approach by content type**
  - **Mermaid** is preferred for:
    - flowcharts
    - sequence diagrams
    - data flow diagrams
    - ER/schema diagrams
    - state machines
    - mind maps
    - class diagrams
    - C4-style architecture diagrams
  - **CSS Grid cards** are preferred for text-heavy architecture overviews.
  - **HTML tables** should be used for structured data/comparisons/audits.
  - **CSS timelines** for timelines/roadmaps.
  - **CSS Grid + Chart.js** for dashboards.
  - For **15+ elements**, use a **hybrid** approach:
    - a simple Mermaid overview
    - detailed CSS cards below
  - It warns against forcing large, complex systems into a single Mermaid diagram.

- **Mermaid rules**
  - Always use:
    - `theme: 'base'`
    - custom `themeVariables`
    - `layout: 'elk'` for complex graphs
  - Use `flowchart TD` by default; `LR` only for simple linear flows.
  - Use `<br/>` for line breaks in labels, not `\n`.
  - Never use bare `<pre class="mermaid">`.
    - Must use the full `diagram-shell` with zoom/pan controls and click-to-expand.
  - Mermaid diagrams should include:
    - zoom controls
    - drag panning
    - reset/expand behavior
  - It also warns about Mermaid styling collisions, especially avoiding page-level `.node` CSS.

- **Optional imagery**
  - If `surf-cli` is available, the skill can generate AI images and embed them as base64.
  - Suggested uses:
    - hero banners
    - conceptual illustrations
    - decorative accents
  - It explicitly says to skip images when Mermaid or CSS suffices, and to degrade gracefully if surf is unavailable.

- **Styling system**
  - Typography is treated as a core design element.
  - Recommended font pairings include:
    - DM Sans + Fira Code
    - Instrument Serif + JetBrains Mono
    - IBM Plex Sans + IBM Plex Mono
    - Bricolage Grotesque + Fragment Mono
    - Plus Jakarta Sans + Azeret Mono
  - Forbidden as primary body fonts:
    - Inter
    - Roboto
    - Arial
    - Helvetica
    - system-ui alone
  - The page should define semantic CSS custom properties such as:
    - `--bg`
    - `--surface`
    - `--border`
    - `--text`
    - `--text-dim`
    - multiple accent colors
  - It encourages subtle depth differences, not dramatic visual noise.
  - It forbids generic or overused color schemes:
    - indigo/violet Tailwind defaults
    - cyan-magenta-pink neon palettes
    - gradient text
    - animated glowing shadows
  - Recommended palettes include:
    - terracotta + sage
    - teal + slate
    - rose + cranberry
    - amber + emerald
    - deep blue + gold

- **Aesthetic guidance**
  - Pick a real aesthetic and commit:
    - Blueprint
    - Editorial
    - Paper/ink
    - Monochrome terminal
    - or a named IDE theme
  - Avoid generic “AI dashboard” styling.
  - The skill stresses:
    - asymmetry
    - hierarchy
    - varied card depth
    - meaningful background atmosphere
    - purposeful animation only
  - It repeatedly warns against:
    - neon dashboard looks
    - gradient meshes
    - uniform card grids
    - perfect symmetry
    - emoji section headers
    - three-dot code block chrome

- **Tables**
  - Structured data should use real `<table>` elements.
  - Key features:
    - sticky headers
    - alternating rows
    - sticky first column when needed
    - horizontal scrolling wrapper
    - good column width management
    - row hover states
  - Status indicators should be styled spans, not emoji.
  - This section strongly encourages transforming any terminal-style table into a proper HTML table.

- **Implementation plans**
  - For implementation plans, the page should not dump entire source files.
  - Instead:
    - show file structure with descriptions
    - show key snippets only
    - use collapsible sections if necessary
  - Suggested structure:
    1. overview
    2. flow diagram
    3. file structure
    4. key implementation details
    5. API/interface summary
    6. usage examples

- **Documentation visualization**
  - READMEs and docs should be transformed visually:
    - features → cards
    - install steps → numbered flow
    - endpoints/commands → table
    - config → table
    - comparisons → panels or tables
    - warnings → callouts
  - The goal is to **extract structure**, not merely reformat prose.

- **Slide deck mode**
  - Slide decks are an **opt-in alternate medium**, not automatic.
  - Triggered by:
    - `/generate-slides`
    - `--slides`
    - explicit request for a slide deck
  - Before generating slides, it says to read:
    - `./references/slide-patterns.md`
    - `./templates/slide-deck.html`
    - `./references/css-patterns.md`
    - `./references/libraries.md`
  - Slides must be:
    - one viewport tall
    - non-scrolling
    - larger type
    - narrative-driven
  - Every section/data point from the source must be covered; the deck should expand if necessary rather than omit content.
  - It defines 10 slide types:
    - Title
    - Section Divider
    - Content
    - Split
    - Diagram
    - Dashboard
    - Table
    - Code
    - Quote
    - Full-Bleed
  - If `surf-cli` is available, the skill encourages generating multiple images for slides.

- **File format and output location**
  - Every output is a single self-contained `.html` file.
  - No external assets except CDN fonts/libraries.
  - Save files in:
    - `~/.agent/diagrams/`
  - The file should then be opened in the browser and the path shared with the user.

- **Sharing**
  - Pages can be deployed publicly via Vercel using:
    - `bash {{skill_dir}}/scripts/share.sh <html-file>`
  - The share flow can produce a live URL and a claim URL.
  - This is described as zero-auth and immediately viewable.

- **Quality checks**
  - The skill includes a checklist before delivery:
    - squint test
    - swap test
    - light/dark mode check
    - completeness check
    - no overflow
    - Mermaid zoom controls present
    - file opens cleanly
  - It emphasizes browser usability and layout stability.

- **Anti-patterns / “AI slop” warnings**
  - The document is unusually explicit about what to avoid.
  - Forbidden patterns include:
    - generic fonts
    - violet/indigo Tailwind accents
    - neon gradients
    - gradient text
    - glowing shadows
    - emoji headers
    - overly uniform card layouts
    - three-dot code chrome
  - It even defines a “slop test”:
    - if the page looks like an AI-generated template, it should be redesigned.

### Assessment
This is a **reference/guide** document with high practical density and strong prescriptive rules. Durability is **medium**: the underlying design principles are fairly timeless, but several details depend on specific tooling, file paths, templates, and versioned conventions (`version 0.5.1`, Mermaid behavior, surf-cli, Vercel deployment workflow). The content is **mixed** but mostly tutorial/reference, since it combines workflow instructions, styling constraints, content-type routing, and quality standards. Originality is **primary source** for the skill’s own operating rules, though it also synthesizes patterns from templates and libraries it references. It is a **refer-back** document rather than skim-once, because future use likely involves checking exact requirements for diagrams, tables, Mermaid setup, or anti-slop constraints. Scrape quality is **good**: the full markdown content appears intact, including tables, examples, code blocks, and long guidance sections.
