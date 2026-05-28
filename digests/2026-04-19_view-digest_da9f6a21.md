---
url: https://ml-digest.ftl.cc/view/?id=2511.04032_detecting-silent-failures-in-multi-agentic-ai-trajectories_20260210_144146&from=%2Fsearch%2F%3Fq%3Dtools%2Bscripts%26ps%3D10%26sort%3Dnewest%26cursor%3DeyJ2IjoxLCJtIjoiZnRzIiwic3J0IjoibmV3ZXN0IiwicWgiOiIzZTAxYWMxMCIsInBzIjoxMCwicCI6OCwiYSI6IjI1MTEuMTExMjUiLCJpZCI6IjI1MTEuMTExMjVfdXRpbGl6aW5nLWxsbXMtZm9yLWluZHVzdHJpYWwtcHJvY2Vzcy1hdXRvbWF0aW9uLWEtY2FzZS1zdHVkeS1vbi1tb2RpZnlpbmctcmFwaWQtcHJvZ3JhbXNfMjAyNjAyMTBfMDIzNDQ4In0
title: View Digest
scraped_at: '2026-04-19T07:07:39Z'
word_count: 1692
raw_file: raw/2026-04-19_view-digest_da9f6a21.txt
tldr: This digest summarizes an arXiv paper on detecting “silent failures” in multi-agent LLM systems using OpenTelemetry traces and ML classifiers, with XGBoost reaching up to 98% accuracy and SVDD up to 96% on two curated benchmark datasets.
key_quote: “Path-level features such as tool_count, total_steps, unique_steps... are consistently ranked highest, highlighting their critical role in anomaly detection.”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Divya Pathak
- Harshit Kumar
- Anuska Roy
- Felix George
- Mudit Verma
- Pratibha Moogi
tools:
- OpenTelemetry
libraries:
- XGBoost
- Random Forest
- SVM
- Logistic Regression
- Naïve Bayes
- SVDD
- Isolation Forest
- K-Means
companies: []
tags:
- multi-agent-systems
- anomaly-detection
- observability
- machine-learning
- llm-agents
---

### TL;DR
This digest summarizes an arXiv paper on detecting “silent failures” in multi-agent LLM systems using OpenTelemetry traces and ML classifiers, with XGBoost reaching up to 98% accuracy and SVDD up to 96% on two curated benchmark datasets.

### Key Quote
“Path-level features such as tool_count, total_steps, unique_steps... are consistently ranked highest, highlighting their critical role in anomaly detection.”

### Summary
- **Paper:** *Detecting Silent Failures in Multi-Agentic AI Trajectories*  
  - **arXiv ID:** 2511.04032  
  - **Authors:** Divya Pathak, Harshit Kumar, Anuska Roy, Felix George, Mudit Verma, Pratibha Moogi
- **Problem addressed:** detecting silent failures in non-deterministic multi-agent AI systems, including:
  - drift
  - cycles
  - missing details
  - other logical failures that do **not** necessarily produce explicit errors
- **Core contribution:** the authors treat agentic-trajectory anomaly detection as a machine-learning problem and build a dataset curation pipeline around traced multi-agent executions.
- **Data collection:**
  - Multi-agent traces are instrumented with **OpenTelemetry**
  - Two benchmark datasets are curated:
    - **Stock Market:** 4,275 trajectories
    - **Research Writing:** 894 trajectories
- **Feature engineering:**
  - 16 features extracted across five categories:
    - token
    - latency
    - path
    - prompt/context
    - model features
  - Path-level features are especially important:
    - `tool_count`
    - `total_steps`
    - `unique_steps`
- **Labeling approach:**
  - Hybrid pipeline combining:
    - domain experts defining a “ground truth” trajectory
    - automated scripts to compare observed traces against that path
    - human-in-the-loop validation
  - Labels are binary: **Normal** vs **Anomaly**
- **Models benchmarked:**
  - **Supervised:** XGBoost, Random Forest, SVM, Logistic Regression, Naïve Bayes
  - **Semi-supervised:** SVDD, Isolation Forest
  - **Unsupervised:** K-Means
- **Main results:**
  - **XGBoost** achieves up to **98% accuracy**
  - **SVDD** achieves up to **96% accuracy**
  - The paper argues SVDD is a useful option when labeled anomaly data is scarce
- **Notable findings:**
  - Path-level features are the strongest signal for anomaly detection
  - Current methods still struggle with **false negatives**, especially when anomalous behavior closely resembles normal behavior
- **Mechanistic interpretation in the digest:**
  - Supervised models work by learning deviations in structural/resource features of trajectories
  - SVDD works by modeling normal behavior and flagging outliers
  - Labeling depends on assuming a single “correct” trajectory per prompt
- **Limitations called out:**
  - The “single ground truth trajectory” assumption may not scale to open-ended or creative tasks
  - Normal-data contamination can hurt semi-supervised methods
  - Results may not generalize to larger or different multi-agent architectures
- **Future work / open questions:**
  - better feature engineering for subtle drift
  - robust online unsupervised or semi-supervised detection
  - explicit detection of tool failures and context propagation failures

### Assessment
This is a **mixed** technical/reference digest centered on a recent research paper, with a relatively **high-durability** conceptual core but some **low-durability** model-performance details tied to this specific benchmark and arXiv version. The content is **high-density** and primarily **original research** summarized plus interpreted through a mechanistic lens. It is best used as **refer-back** material if you care about multi-agent observability, anomaly detection, or trace-based evaluation, and **deep-study** if you want the labeling pipeline, benchmark setup, or feature/model comparisons. Scrape quality looks **good overall**: it captures the paper metadata, main findings, methodological details, limitations, and future directions, though it is a digest rather than the full paper and may omit figures, tables, and exact experimental specifics.
