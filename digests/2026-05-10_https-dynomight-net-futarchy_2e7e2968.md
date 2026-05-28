---
url: https://dynomight.net/futarchy/
title: https://dynomight.net/futarchy/
scraped_at: '2026-05-10T04:27:09Z'
word_count: 2775
raw_file: raw/2026-05-10_https-dynomight-net-futarchy_2e7e2968.txt
tldr: Dynomight argues that futarchy fails because conditional prediction markets estimate P(A|B), not the causal effect P(A|do(B)), so even a smart market cannot directly tell you what will happen if you actually choose an action.
key_quote: Conditional prediction markets reveal probabilistic relationships, not causal relationships.
durability: high
content_type: opinion
density: high
originality: commentary
reference_style: deep-study
scrape_quality: good
people:
- Dynomight
- Robyn Denholm
- Elon Musk
- Robin Hanson
- Anders_H
tools: []
libraries: []
companies:
- Tesla
tags:
- prediction-markets
- futarchy
- causal-inference
- decision-making
- forecasting
---

### TL;DR
Dynomight argues that futarchy fails because conditional prediction markets estimate **P(A|B)**, not the causal effect **P(A|do(B))**, so even a smart market cannot directly tell you what will happen if you actually choose an action.

### Key Quote
“Conditional prediction markets reveal probabilistic relationships, not causal relationships.”

### Summary
- **Topic:** A critique of **futarchy** and conditional prediction markets as decision tools.
- **Main thesis:** Even if conditional prediction markets are perfectly efficient, they still generally do **not** tell you the causal effect of an action. They reveal what happens **when you observe a condition**, not what happens **if you intervene** to make that condition happen.
- **Core distinction:**
  - **P(A|B)** = probability of A given B
  - **P(A|do(B))** = probability of A if you actively make B happen
  - The post argues futarchy confuses these two.
- **Why the Tesla/Musk example fails:**
  - A market predicting Tesla stock under “Musk fired” may be influenced by confounders:
    - firing Musk might signal bad hidden information
    - firing him could correlate with other harmful actions by decision-makers
    - future actions can be conditioned on, but that still doesn’t isolate causality
- **Vitamin D analogy:**
  - People with high vitamin D levels have better outcomes, but that does **not** mean simply taking vitamin D has the same effect.
  - Randomized trials are needed for causal effects.
- **Why letting the market choose the action doesn’t fix it:**
  - The post gives a coin-flip thought experiment showing that once market prices determine whether a bet “activates,” the market itself changes incentives.
  - You may rationally bid more than your estimate because you’re betting on the market’s ability to discriminate between states.
- **Why ordering is not preserved:**
  - The post constructs an example where you would rationally pay more for a contract on a coin you think is **less likely** to be heads, because you expect the market to learn hidden structure better than you can.
  - So market prices don’t reliably preserve your own ranking of expected outcomes.
- **Why payout redesign doesn’t solve it:**
  - The post sketches a general theorem: no payout function can force truthful bidding in a way that turns arbitrary conditional markets into causal decision tools.
  - The argument uses two distributions that produce the same expected payout under the market design but imply different causal expected values.
- **Bottom line:**
  - Conditional prediction markets are still useful as **observational evidence**, but they should not be treated as causal oracles.
  - The author says the flaw is recognized in parts of the literature, but is often underappreciated in futarchy discussions.
- **What the author suggests next:**
  - There are ways to recover causal estimates from data, and analogous mechanisms may exist for markets—but they are not free or automatic.

### Assessment
This is a **high-durability** opinion/technical essay with a strong conceptual core that should remain relevant as long as people discuss prediction markets, futarchy, and causal inference. It is **dense** and mostly a **commentary/synthesis** piece, though it includes original argumentation, examples, and a theorem-style proof sketch. It’s best used as a **refer-back** or **deep-study** reference if you care about the causal-vs-conditional distinction in market design. Scrape quality is **good**: the main post content, examples, and proof sketch are present, though some surrounding site navigation and link formatting are noisy.
