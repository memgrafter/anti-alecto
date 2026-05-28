---
url: https://dynomight.net/bayes/
title: https://dynomight.net/bayes/
scraped_at: '2026-05-10T04:28:50Z'
word_count: 2512
raw_file: raw/2026-05-10_https-dynomight-net-bayes_0fe6c172.txt
tldr: Dynomight’s “Bayes is not a phase” argues that Bayesian reasoning is just a formalization of everyday thinking about uncertain facts, that much of the “is it real?” debate is semantic, and that while it’s theoretically optimal, building formal Bayesian models is often too hard and risky to be practical.
key_quote: Bayesian reasoning isn’t math . It’s a concept.
durability: high
content_type: mixed
density: high
originality: commentary
reference_style: deep-study
scrape_quality: good
people: []
tools: []
libraries: []
companies: []
tags:
- bayesian-reasoning
- uncertainty
- decision-making
- probability
- rationality
---

### TL;DR
Dynomight’s “Bayes is not a phase” argues that Bayesian reasoning is just a formalization of everyday thinking about uncertain facts, that much of the “is it real?” debate is semantic, and that while it’s theoretically optimal, building formal Bayesian models is often too hard and risky to be practical.

### Key Quote
“Bayesian reasoning isn’t math . It’s a concept.”

### Summary
- **Article theme:** A defense of Bayesian reasoning against the idea that it’s a weird rationalist fad.
- **Core thesis:**  
  - Bayesian reasoning is not an exotic alternate logic; it’s a formal way of handling uncertainty that people already use instinctively.
  - The post argues that the controversy mostly comes from mixing up two kinds of uncertainty:
    - **Aleatoric uncertainty**: randomness in the world itself
    - **Epistemic uncertainty**: uncertainty in your knowledge about fixed facts
- **Examples used to build intuition:**
  - **Lupus test:** a positive test can still be weak evidence if the disease is rare.
  - **Coin flips:** 16 heads out of 20 does not necessarily mean the coin is biased if the prior expectation is that it is a normal penny.
  - **AGI in 5 years / plant consciousness:** shows how subjective priors and updates can produce “Bayesian” probabilities in uncertain real-world judgments.
- **Why Bayes helps:**
  - The coin-in-a-jar examples show why Bayesian-style reasoning can produce the correct decision under uncertainty.
  - **Gold coin / fake coin wager:**  
    - One gold coin worth **$1000**
    - **4 worthless fake coins**
    - If you choose a random coin before seeing it, expected value is **$200**, so paying **$125** is good.
    - If you see a coin land heads first, the expected value becomes **$1000/9 ≈ $111.11**, so paying **$125** is bad.
  - The point: even when the underlying fact is fixed, treating your uncertainty probabilistically leads to better decisions.
- **Why it’s controversial:**
  - Real-world Bayesian estimates often depend on subjective choices:
    - what counts as the relevant reference class
    - which prior distribution to use
    - which evidence to include and how to weight it
  - Examples like drug trials and AGI forecasting show that different reasonable assumptions can produce very different probabilities.
- **Main semantic argument:**
  - The post says people argue over whether Bayesian probabilities are “real,” but this is often a terminology dispute.
  - It suggests separating strict physical probabilities from broader subjective/probabilistic beliefs would dissolve much of the debate.
- **Why not always be Bayesian:**
  - In complex real-world cases, Bayesian modeling can be computationally hard and fragile.
  - The post claims Bayesian reasoning outside simple cases requires:
    - slow and unreliable algorithms
    - difficult model specification
    - careful handling of distributions and parameters
    - risk of bad outputs from one mistaken assumption
  - It bluntly claims Bayesian reasoning is in a complexity class “slightly worse than the famous NP-complete class.”
- **Author’s practical conclusion:**
  - Formal Bayesian reasoning is theoretically ideal when assumptions can be specified cleanly.
  - In practice, for most people and most problems, normal human judgment is safer.
  - Still, Bayesian thinking is useful as a guide for updating beliefs and checking assumptions.

### Assessment
This is a **mixed** opinion/technical essay with fairly high durability: the conceptual distinction between aleatoric and epistemic uncertainty is timeless, but the examples (AGI, specific health topics, rationalist culture references) age faster. It is **dense** with concrete examples and argument structure, and it reads as **primary commentary** rather than a literature synthesis. For **recall**, it’s a strong mental model piece about Bayes as everyday reasoning; for **decide**, it’s worth rereading if you want the author’s practical critique of formal Bayesian modeling; for **evaluate**, the conceptual points are durable but the complexity-class claim and practical limitations are rhetorical and should be treated cautiously; for **find**, this is a good match if you’re looking for Dynomight’s Feb 2025 post “Bayes is not a phase,” especially the $1000 gold coin / 4 fake coins / $125 example and the claim that Bayesian reasoning is “slightly worse than” NP-complete. Scrape quality is **good**: the main article text and key examples appear present, though the page is cluttered with site navigation and related links.
