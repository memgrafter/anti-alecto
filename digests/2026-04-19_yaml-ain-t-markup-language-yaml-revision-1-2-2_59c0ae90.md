---
url: https://yaml.org/spec/1.2.2/#23-scalars
title: YAML Ain’t Markup Language (YAML™) revision 1.2.2
scraped_at: '2026-04-19T07:52:46Z'
word_count: 19073
raw_file: raw/2026-04-19_yaml-ain-t-markup-language-yaml-revision-1-2-2_59c0ae90.txt
tldr: 'YAML 1.2.2 §2.3 explains scalar syntax and behavior: plain, single-quoted, double-quoted, literal (`|`), and folded (`>`), plus how indentation, line folding, escaping, and chomping rules affect what text is actually preserved.'
key_quote: “Scalar content can be written in block notation, using a literal style (indicated by “|”) where all line breaks are significant.”
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Oren Ben-Kiki
- Clark Evans
- Ingy döt Net
- Kyrylo Simonov
- YAML Language Development Team
tools: []
libraries: []
companies:
- YAML Language Development Team
tags:
- yaml
- data-serialization
- text-formatting
- syntax
- specifications
---

### TL;DR
YAML 1.2.2 §2.3 explains scalar syntax and behavior: plain, single-quoted, double-quoted, literal (`|`), and folded (`>`), plus how indentation, line folding, escaping, and chomping rules affect what text is actually preserved.

### Key Quote
“Scalar content can be written in block notation, using a literal style (indicated by “|”) where all line breaks are significant.”

### Summary
- This is **section 2.3 “Scalars”** from the YAML 1.2.2 specification.
- It defines the main scalar presentation styles:
  - **Plain scalars**: unquoted, most readable, but most restricted and context-sensitive.
  - **Single-quoted scalars**: printable text with only one escape mechanism—`''` for an embedded single quote.
  - **Double-quoted scalars**: the most expressive style; supports escape sequences like `\n`, `\t`, `\u0041`, `\U00000041`.
  - **Literal block scalars** (`|`): preserve line breaks exactly as content.
  - **Folded block scalars** (`>`): fold line breaks into spaces except where blank lines or indentation preserve them.
- It describes how YAML scalars interact with:
  - **Indentation**: determines block structure and the content scope of block scalars.
  - **Line folding**: long lines may be wrapped; in folded style, line breaks usually become spaces.
  - **Chomping**: controls trailing newlines/empty lines in block scalars.
    - `|-` = strip final newline
    - `|` / `>` default = clip
    - `|+` / `>+` = keep trailing newlines
- It includes the key restriction that **plain scalars cannot freely contain indicators** like `:`, `#`, `-`, `[`, `]`, `{`, `}`, `,` in ambiguous positions, which is why quoting is often needed.
- The section’s examples show how the same logical value can be represented very differently depending on style, especially for:
  - comments vs content,
  - URLs and timestamps in plain scalars,
  - multi-line text in folded vs literal blocks,
  - leading/trailing spaces and tabs in quoted scalars.
- It also shows that **block scalars are presentation-sensitive**: indentation and chomping affect what text is included, but are not meant to carry application data.
- For practical YAML use, this subsection is the core reference for deciding:
  - when to use **plain vs quoted** scalars,
  - when to use **literal vs folded** blocks,
  - how to preserve newlines or normalize them,
  - how to avoid parser ambiguity.

### Assessment
This is a **high-durability reference** document: YAML 1.2.2 is a standards text, and section 2.3 on scalars is foundational, though some details are version- and spec-dependent. The content type is **reference/mixed** rather than tutorial, because it mixes normative rules with illustrative examples. Density is **high**: there are many precise rules, indicators, and edge cases packed into the section. Originality is **primary source**, since it is the specification itself. It’s best used as **refer-back** material when you need exact scalar behavior or want to confirm syntax rules. Scrape quality is **good** for this section: the excerpt contains substantial scalar-related material and examples, though it is a long partial capture of the broader spec and may omit some page structure or surrounding navigation.
