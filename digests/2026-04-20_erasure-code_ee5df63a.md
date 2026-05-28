---
url: https://en.wikipedia.org/wiki/Erasure_code
title: Erasure code
scraped_at: '2026-04-20T01:22:26Z'
word_count: 2290
raw_file: raw/2026-04-20_erasure-code_ee5df63a.txt
tldr: Erasure coding is a forward-error-correction technique that lets a message be recovered from any sufficient subset of encoded symbols, with Reed–Solomon, RAID parity, and fountain codes as key practical examples for storage and transmission.
key_quote: “the original message can be recovered from a subset of the n symbols”
durability: high
content_type: reference
density: high
originality: synthesis
reference_style: deep-study
scrape_quality: good
people:
- Irving Reed
- Gustave Solomon
- Luigi Rizzo
- Sir Arthur C. Clarke
tools:
- Jerasure
- Feclib
- zfec
libraries: []
companies:
- Apache Hadoop
- Microsoft Azure
- Facebook
- Backblaze
tags:
- erasure-coding
- forward-error-correction
- raid
- reed-solomon
- distributed-storage
---

### TL;DR
Erasure coding is a forward-error-correction technique that lets a message be recovered from any sufficient subset of encoded symbols, with Reed–Solomon, RAID parity, and fountain codes as key practical examples for storage and transmission.

### Key Quote
“the original message can be recovered from a subset of the n symbols”

### Summary
- **Definition**
  - An erasure code converts a message of **k symbols** into a longer codeword of **n symbols**.
  - Recovery works when the receiver knows **which symbols were lost** and has enough of the remaining symbols.
  - The **code rate** is **r = k/n**.
  - **Reception efficiency** is **k’/k**, where **k’** is the number of symbols required for recovery.

- **History and context**
  - Erasure coding was invented by **Irving Reed** and **Gustave Solomon** in **1960**.
  - Common erasure codes include:
    - **Reed–Solomon codes**
    - **LDPC codes**
    - **Turbo codes**
  - In modern data storage, three main redundancy strategies are contrasted:
    - **Replication**
    - **RAID**
    - **Erasure coding**
  - The article distinguishes **RAID** as typically attached to a **single host** and thus with a different failure model, while **erasure coding** usually implies redundancy across **multiple hosts** (sometimes described as **RAIS**).

- **Optimal erasure codes**
  - **Optimal erasure codes** are those where **any k of the n symbols** are enough to reconstruct the message.
  - These are exactly **maximum distance separable (MDS) codes**.
  - The simplest case is **parity check**:
    - With **n = k + 1**, one checksum symbol is appended.
    - If one symbol is erased, it can be recovered by summing the others.
    - The article notes **RAID 5** as a common XOR-based parity-check application.

- **Polynomial interpolation / Reed–Solomon style construction**
  - A toy example called **“err-mail”** shows redundancy via points on a line.
  - The general method uses:
    - A **finite field**
    - A **Lagrange polynomial** of degree **k**
    - Sending evaluations at additional points **p(k)...p(n−1)**
  - If the receiver gets at least **k symbols**, polynomial interpolation recovers the message.
  - The article says this is implemented in practice by **Reed–Solomon codes**, using a **Vandermonde matrix**.
  - Most practical erasure codes are **systematic**: the original data appears unchanged among the transmitted symbols.
  - Secret-sharing erasure schemes typically do **not** use systematic codes.

- **Near-optimal erasure codes**
  - These require only **(1 + ε)k** symbols for recovery, rather than exactly **k**.
  - Smaller **ε** usually means more CPU work.
  - The article emphasizes the tradeoff:
    - **Better rate / less overhead**
    - versus **more computational complexity**
  - These schemes can still encode/decode in **linear time** in practical algorithms.
  - **Fountain codes** are presented as a major example of **near-optimal, rateless erasure codes**:
    - They can generate effectively unlimited redundancy symbols.
    - Decoding begins after slightly more than **k** encoded symbols are received.
  - **Regenerating codes** are discussed as a response to the cost of repairing lost fragments in distributed storage.

- **Applications in storage systems**
  - Erasure coding is now standard in reliable storage.
  - The article lists use in:
    - **Apache Hadoop**
    - **Linux RAID-6**
    - **Microsoft Azure**
    - **Facebook cold storage**
    - **Backblaze Vaults**
  - The main storage motivation is lower overhead than replication.
  - For distributed storage, the key property is that a stripe of **k data blocks** plus **r parity blocks** can tolerate up to **r failures**, as long as **k of k+r chunks** remain available.
  - This is contrasted with full replication, which requires much more storage overhead to survive the same number of failures.

- **Concrete example: RS(10,4)**
  - **10 MB** of data is split into **ten 1 MB blocks**.
  - **Four 1 MB parity blocks** are added.
  - The system can tolerate **4 concurrent failures**.
  - Storage overhead is **14/10 = 1.4×**.
  - The article compares this with a fully replicated system needing **50/10 = 5.0×** overhead for the same failure tolerance.
  - The **Hitchhiker scheme** is mentioned as a way to reduce reconstruction computation and transfer, and it is available as an HDFS codec with a manually defined policy.

- **Hot-data / performance uses**
  - Erasure coding is not only for “cold” storage; it can also help with **hot data**.
  - **RAID 5** is presented as a classic example where parity coding gives single-drive failure protection with fewer drives than mirroring.
  - The spare capacity can be used for more data and potentially better performance.
  - The article also mentions **RAID 6** and generalized RAID notation:
    - **RAID7.x**: x redundancy drives, recover from x drive failures
    - **RAID N+M**: N data drives and M redundancy drives
  - **EC-Cache** is cited as a distributed cache example where splitting objects into data and redundancy units can improve load balancing without excessive memory waste.

- **Examples list**
  - Near-optimal codes:
    - **Tornado codes**
    - **LDPC codes**
  - Near-optimal fountain/rateless codes:
    - **Fountain code**
    - **Online codes**
    - **LT codes**
    - **Raptor codes**
    - **Network codes**
    - **Triangular codes**
  - Optimal codes:
    - **XOR parity**
    - **Reed–Solomon codes**
    - **Parchive**
    - **RAID 6 variants**
    - **zfec** in Tahoe-LAFS
    - **Erasure Resilient Systematic Code**
    - **Regenerating codes**
    - Other **MDS codes**

- **Related concepts**
  - **Forward error correction**
  - **Secret sharing** is explicitly distinguished from erasure coding
  - **Binary erasure channel**
  - **Spelling alphabet**

- **External links / tools**
  - **Jerasure**: free software library for Reed–Solomon and Cauchy erasure coding with SIMD optimizations.
  - **Luigi Rizzo’s software FEC**: describes optimal erasure correction codes.
  - **Feclib**: a near-optimal extension using band matrices and CPU register optimizations.
  - **Coding for Distributed Storage wiki**: regenerating and rebuilding codes.
  - **ECIP**: an early Internet use of FEC, described as first used commercially for live video of **Sir Arthur C. Clarke** in Sri Lanka to UIUC in Indiana.

### Assessment
This is a **mixed reference/technical overview** with some explanatory tutorial-like examples, and it is fairly durable at the conceptual level: the core ideas of erasure coding, MDS codes, parity, Reed–Solomon, and fountain codes are **high-durability** concepts, though specific storage-system examples and product mentions can age. The content is **medium-to-high density** because it combines definitions, math intuition, implementation notes, storage use cases, and example systems in one page. Its originality is best described as a **reference synthesis**: it is encyclopedic, aggregating standard knowledge rather than presenting new results. The best use is **deep-study** if you want a broad conceptual map, or **refer-back** when you need terminology, examples, or distinctions like RAID vs multi-host erasure coding. Scrape quality is **good**: the main article sections, formulas, examples, and external links are present, though the extract does not include a populated references list and may omit any media/formatting details beyond the text shown.
