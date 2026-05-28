---
url: https://dynomight.net/dna/
title: https://dynomight.net/dna/
scraped_at: '2026-05-10T04:29:12Z'
word_count: 4319
raw_file: raw/2026-05-10_https-dynomight-net-dna_e9c0f226.txt
tldr: Dynomight’s “How much information is in DNA?” argues that the answer depends on which notion of information you mean, and concludes that a better-yet-still-uncertain measure is a proposed “phenotypic Kolmogorov complexity” that may put a human genome somewhere between about 60 MB and 750 MB of information.
key_quote: “Ultimately, I’ll argue that the intuitive idea of information in a genome is best captured by a new definition of a ‘bit’—one that’s unknowable with our current level of scientific knowledge.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: deep-study
scrape_quality: good
people:
- Andrey Kolmogorov
- Claude Shannon
- Mitochondrial Eve
tools: []
libraries: []
companies:
- Asimov Press
tags:
- genomics
- information-theory
- dna
- compression
- evolutionary-biology
---

### TL;DR
Dynomight’s “How much information is in DNA?” argues that the answer depends on which notion of information you mean, and concludes that a better-yet-still-uncertain measure is a proposed “phenotypic Kolmogorov complexity” that may put a human genome somewhere between about 60 MB and 750 MB of information.

### Key Quote
“Ultimately, I’ll argue that the intuitive idea of information in a genome is best captured by a new definition of a ‘bit’—one that’s unknowable with our current level of scientific knowledge.”

### Summary
- The article starts with the naive calculation:
  - Human DNA has about **3.1 billion base pairs**.
  - Each base pair has **4 possibilities** (A, T, C, G), so a base pair can encode **2 bits**.
  - A straight storage-space view gives about **6.2 billion bits** total.
- It then shows why that simple answer is misleading:
  - Humans are **diploid**, so you have two copies of most chromosomes.
  - Large parts of human DNA are **shared across people** or **repeated**.
  - DNA can be **compressed**, but the meaning of “compressed” changes the answer a lot.
- The piece distinguishes several notions of “information”:
  - **Storage-space definition**: count the possible states a sequence could hold.
  - **Kolmogorov complexity**: information is the length of the shortest program that outputs the sequence.
  - **Shannon information**: information depends on the probability of a sequence within a known distribution.
- On compression:
  - With a **reference genome**, DNA can be compressed by **more than 99%**, because most of your genome is shared with other humans.
  - Without a reference genome, current best compression is said to be about **25%**, and the author estimates that because you have two nearly identical chromosome sets, the effective compression might be around **62%**.
- On biological complexity:
  - Only about **1%** of DNA is exons that code for proteins.
  - Around **24%** is introns.
  - Large additional portions participate in **regulation**: promoters, enhancers, silencers, insulators.
  - DNA also contains structural regions like **centromeres** and **telomeres**, and many kinds of noncoding RNA genes.
  - Some regions are **pseudogenes** or other sequences that may look functional but are not clearly so.
- The article emphasizes why DNA is hard to interpret:
  - DNA is under constant pressure from **mutation**, replication errors, UV light, radiation, and chemicals.
  - Genomes contain lots of **repeats**, **transposons**, **retrotransposons**, and other mobile elements that create duplication and rearrangement.
  - Evolution often preserves DNA not because it is “extra,” but because it is important or because the system has become robust to variation.
- The author’s proposed solution:
  - Define DNA information as **phenotypic Kolmogorov complexity**: the shortest DNA-like representation that still produces a human with the same observable phenotype.
  - This is meant to capture not just exact sequence identity, but the minimal genome needed to produce “you.”
- The author’s estimate:
  - Human DNA could perhaps be reduced by **75% to 98%** and still produce a human-like phenotype.
  - That would imply roughly **480 million to 6 billion bits**, or about **60 MB to 750 MB**.
  - But the article stresses that this is highly uncertain; we do not yet know what much of DNA does.

### Assessment
This is a mixed science/essay piece with a fairly durable conceptual core but some numbers that will age as genomics and compression methods improve. The content type is **mixed**: part explanation, part opinionated synthesis, part technical essay. Density is **high** because it packs in information theory, genomics, and evolutionary biology examples, though the tone is conversational and humorous. It is mostly a **commentary/synthesis** piece rather than original research. Best used as **deep-study** if you want the conceptual framework for thinking about genome information, or **refer-back** for the author’s proposed distinction between storage, compression, and phenotype-based information. Scrape quality is **good**: the main article text is present, including the key argument and conclusion, though any figures, formatting, or linked diagrams are not captured here.
