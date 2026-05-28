---
url: https://news.ycombinator.com/item?id=38725953
title: When I open a large pdf on arxiv (100+ MB, not uncommon for ML papers focused on... | Hacker News
scraped_at: '2026-04-19T21:33:58Z'
word_count: 658
raw_file: raw/2026-04-19_when-i-open-a-large-pdf-on-arxiv-100-mb-not-uncommon-for-ml-papers-focused-on-ha_9d36001a.txt
tldr: 'HN thread about why large arXiv PDFs take 10+ seconds to open: u/IlliOnato suggests arXiv may be generating/caching PDFs server-side, u/upbeat_general says the delay seems network/server-bound, and u/10000truths says the PDF format itself often forces a full download unless it’s linearized.'
key_quote: The default PDF format puts the xref table at the end of the file, forcing a full download before rendering can take place.
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: skim-once
scrape_quality: good
people:
- ansk
- IlliOnato
- upbeat_general
- arccy
- 10000truths
tools:
- Chrome
- arXiv
libraries: []
companies: []
tags:
- arxiv
- pdf
- document-rendering
- caching
- web-performance
---

### TL;DR
HN thread about why large arXiv PDFs take 10+ seconds to open: **u/IlliOnato** suggests arXiv may be generating/caching PDFs server-side, **u/upbeat_general** says the delay seems network/server-bound, and **u/10000truths** says the PDF format itself often forces a full download unless it’s linearized.

### Key Quote
“**The default PDF format puts the xref table at the end of the file, forcing a full download before rendering can take place.**”

### Summary
- **Top comment (verbatim):** "It may be even that the time is taken to generate a PDF.The format in which articles are submitted and stored in arXive is LaTeX. PDF is automatically generated from it.Probably arXiv does some caching of PDFs so they don't have to be generated anew every time they are requested, but I don't know how this caching works."
- **Top commenter:** `u/IlliOnato`
- **Thread topics:**
  - Why large arXiv PDFs have long initial load times
  - Whether the bottleneck is network, server-side generation, or browser rendering
  - How PDF structure affects progressive rendering
  - arXiv caching/CDN behavior
  - Possibility of HTML or progressively rendered text alternatives

- The original poster says large arXiv PDFs can be 100+ MB and take **10+ seconds** before anything renders except a loading bar.
- They ask whether:
  - the delay is **network-bound**
  - **Chrome is slow** at rendering big PDFs
  - PDFs need to be **fully downloaded** before rendering
- They also argue that a **progressively rendered HTML doc** would be a big usability improvement for reading paper text immediately.

- **u/IlliOnato**:
  - Suggests the delay might come from **generating the PDF**, since arXiv submissions are in **LaTeX** and PDFs are auto-generated.
  - Notes arXiv probably caches PDFs, but says they don’t know the details.

- **u/upbeat_general**:
  - Says they have the same issue and think it is **network-bound / slow arXiv servers**.
  - Links arXiv’s cache FAQ: `https://info.arxiv.org/help/faq/cache.html`
  - Mentions difficulty setting up a caching server despite arXiv theoretically supporting it.

- **u/arccy** replies that it “might be faster now with fastly,” implying a CDN/cache improvement, but this is only a brief speculative aside.

- **u/10000truths**:
  - Explains that in the **default PDF format**, the **xref table is at the end of the file**, so the reader may need the whole file before rendering starts.
  - Notes **PDF-1.2+** supports **linearized PDFs**, which allow earlier rendering.
  - Says many PDF exporters have an option like **“optimize for web”** to enable this.

- Overall, the thread converges on a few plausible causes:
  - **server/network delay**
  - **PDF generation/caching behavior**
  - **PDF file structure** preventing incremental rendering
- There is **no definitive answer** in the thread; it’s mostly informed speculation plus one concrete technical explanation about PDF layout.

### Assessment
This is a **mixed** content thread with moderate durability: the PDF-format explanation is relatively timeless, but comments about arXiv’s servers, caching, and Fastly are somewhat time-sensitive and may change. The density is **medium** because the thread is short but includes a useful technical point about xref tables and linearized PDFs. Originality is mostly **commentary** rather than primary source, with one comment providing a technical explanation and others offering anecdotal guesses. It’s best used as a **skim-once / refer-back** note for remembering the likely causes of slow PDF opening. Scrape quality is **good** for the captured text and comment content, though it’s limited to a small number of comments and likely omits broader thread context.
