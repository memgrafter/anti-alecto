---
url: https://info.arxiv.org/help/api/basics.html
title: arXiv API Basics - arXiv info
scraped_at: '2026-04-12T07:36:30Z'
word_count: 1341
raw_file: raw/2026-04-12_arxiv-api-basics-arxiv-info_83586792.txt
tldr: arXiv’s API Basics page explains how to query arXiv programmatically over HTTP, shows a sample Atom response, gives minimal examples in Perl/Python/Ruby/PHP, and points readers to the User’s Manual, mailing list, and terms of use.
key_quote: the purpose of the arXiv API is to allow programmatic access to the arXiv's e-print content and metadata.
durability: high
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Firefox
libraries:
- LWP::UserAgent
- urllib.request
- net/http
- uri
- file_get_contents
companies:
- Cornell University
- American Physical Society
- Journal for High Energy Physics
- H1 Collaboration
tags:
- api-documentation
- arxiv
- atom-feed
- http-requests
- programmatic-access
---

### TL;DR
arXiv’s API Basics page explains how to query arXiv programmatically over HTTP, shows a sample Atom response, gives minimal examples in Perl/Python/Ruby/PHP, and points readers to the User’s Manual, mailing list, and terms of use.

### Key Quote
“the purpose of the arXiv API is to allow programmatic access to the arXiv's e-print content and metadata.”

### Summary
- **What this page is**
  - Introductory documentation for the arXiv API on arXiv info.
  - Intended for application developers who want access to arXiv data, search, and linking features.
  - Advises users to review the **Terms of Use** before using the API.

- **What the arXiv API is for**
  - Provides programmatic access to arXiv e-print content and metadata.
  - Designed to enable “new and creative use” of the arXiv corpus with a low barrier to entry.
  - Context about arXiv:
    - Cornell University e-print archive, widely used in physics, mathematics, and computer science.
    - Serves as a major channel for sharing manuscripts before traditional publication.
    - Some manuscripts are later published elsewhere; others remain only on arXiv.

- **How to use it**
  - API calls are made with **HTTP GET or POST** requests.
  - The main access point is a URL with query parameters.
  - Example query:
    - `http://export.arxiv.org/api/query?search_query=all:electron`
  - More specific example:
    - `http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10`
    - Means: return the first 10 results matching `all:electron`.
  - Results are returned in **Atom 1.0**, an XML-based syndication format.
  - You can test queries directly in a browser; the page specifically mentions Firefox as rendering Atom well.

- **What the returned data looks like**
  - The page includes a full example Atom feed response.
  - Response elements shown include:
    - feed metadata (`title`, `id`, `updated`)
    - search metadata (`totalResults`, `startIndex`, `itemsPerPage`)
    - entry metadata:
      - paper `id`
      - `published` and `updated`
      - `title`
      - `summary`
      - `author`
      - `comment`
      - `journal_ref`
      - `primary_category`
      - links to HTML and PDF versions
  - Example paper in the sample response:
    - **“Multi-Electron Production at High Transverse Momenta in ep Collisions at HERA”**
    - H1 Collaboration
    - `hep-ex/0307015`
    - Shows how arXiv includes abstracts, metadata, and links.

- **Language examples**
  - The page gives minimal code snippets to fetch the API response in:
    - **Perl** using `LWP::UserAgent`
    - **Python** using `urllib.request`
    - **Ruby** using `net/http` and `uri`
    - **PHP** using `file_get_contents()`
  - The examples all call:
    - `http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1`
  - The page notes these examples only print raw Atom XML; more advanced usage is covered in the **User’s Manual**.
  - It also says if your favorite language is missing, you can send in an example for inclusion.

- **Documentation and community**
  - The **API User’s Manual** is the main deeper reference for interface details, Atom format, and advanced examples.
  - The page encourages joining the **arxiv-api discussion list / mailing list** for help, questions, and feedback.
  - It says the best way to learn and get support is to ask publicly in the forum.
  - The team wants project examples and invites users to send links to tools built with the API.

- **Projects using the API**
  - Mentioned examples:
    - **PaperRater.org** — web-based tool for open review and social reading
    - **ArXiv Analytics** — portal for reading and discussing arXiv eprints
    - **biblio.el** — downloads BibTeX entries from arXiv and other sources in Emacs

### Assessment
This is a **reference/tutorial** page with **high durability** for the conceptual basics of using the arXiv API, though some implementation details and example URLs may become stale if the API changes. The content is a **mixed** document: mostly documentation with a bit of institutional context and community guidance. It is **dense** in practical specifics, especially the sample query formats, Atom response structure, and code snippets. The material is largely **primary source** documentation from arXiv itself, so it is trustworthy for intended usage, though readers should still verify current endpoint behavior and terms of use. This is best used as a **refer-back** reference when implementing or checking basic API usage. The scrape quality is **good**: the main sections, examples, and code snippets are present, though any styling, formatting nuances, or interactive links are necessarily missing.
