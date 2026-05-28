---
url: https://github.com/jooaobrum/experimenta-ml
title: 'jooaobrum/experimenta-ml: This repository contains the files for the ML Auto Recipes project, which is the main objective to use agentic flows with Claude to find the best model.'
scraped_at: '2026-04-19T08:07:13Z'
word_count: 1271
raw_file: raw/2026-04-19_jooaobrum-experimenta-ml-this-repository-contains-the-files-for-the-ml-auto-reci_58eed0dc.txt
tldr: A proof-of-concept “agentic AutoML” repo for tabular binary classification where Claude Code iteratively rewrites a single `experiment.py` file, guided by `mission.yaml` and a fixed evaluator, to search data-cleaning, split, feature, and model “recipes” rather than just model hyperparameters.
key_quote: “Classic AutoML is dead. Now, you describe a problem, the agent explores it.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- karpathy
tools:
- Claude Code
libraries:
- pandas
- numpy
- scikit-learn
- lightgbm
- xgboost
- scipy
- pyyaml
companies: []
tags:
- automl
- tabular-classification
- agentic-workflows
- feature-engineering
- machine-learning-ops
---

### TL;DR
A proof-of-concept “agentic AutoML” repo for tabular binary classification where Claude Code iteratively rewrites a single `experiment.py` file, guided by `mission.yaml` and a fixed evaluator, to search data-cleaning, split, feature, and model “recipes” rather than just model hyperparameters.

### Key Quote
“Classic AutoML is dead. Now, you describe a problem, the agent explores it.”

### Summary
- **What it is**
  - `jooaobrum/experimenta-ml` is an agent-driven ML experimentation engine for **tabular classification**.
  - It is inspired by `karpathy/autoresearch`.
  - The project’s main goal is to use **agentic flows with Claude** to find the best model/recipe.

- **Core thesis**
  - The repo argues that most real-world ML gains come from:
    - correct data cleaning
    - realistic train/test splits
    - feature engineering grounded in domain knowledge
    - group-aware and time-aware aggregation
  - So instead of searching only model architectures, the agent searches an entire **“recipe”**:
    - data policy
    - split strategy
    - feature engineering
    - model configuration

- **How the system works**
  - User writes a `mission.yaml`.
  - Claude reads it, profiles the data, runs EDA, writes a baseline, then enters a **hill-climbing loop**:
    - inspect failure cases
    - propose feature/cleaning changes
    - rerun evaluator
    - keep or revert changes
  - The workflow is intentionally **lightweight**:
    - no Python orchestration layer
    - user opens **Claude Code** in the project directory and tells it to read `PROGRAM.md` and `mission.yaml` and run the loop

- **Setup**
  - Clone repo and install editable package:
    - `git clone <this-repo>`
    - `cd ml-auto-recipes`
    - `pip install -e .`
  - Required dependencies listed:
    - `pandas`
    - `numpy`
    - `scikit-learn`
    - `lightgbm`
    - `xgboost`
    - `scipy`
    - `pyyaml`

- **How to run an experiment**
  - Put training data in an accessible path, e.g. `data/myproject/train.csv`
  - Create `mission.yaml` with:
    - `project_name`
    - `task_type: binary_classification`
    - `target_column`
    - `train_path`
    - `primary_metric`
    - `trial_budget`
    - `allowed_models` such as `lr`, `lgbm`, `xgb`
    - seeds
    - hard constraints like minimum metric or max latency
  - Most important field: **`domain_knowledge`**
    - unit of analysis
    - group structure
    - temporal dynamics
    - leakage risks
    - feature priors
    - evaluation nuances

- **Example domain knowledge the repo encourages**
  - Group-aware problems:
    - account-level churn prediction
    - account-aware splitting
    - account-level aggregations
  - Time-aware problems:
    - use time-based splits to avoid leakage
    - model feature decay over time
  - Leakage prevention:
    - drop columns created after the outcome
  - Business nuance:
    - false negatives may be more costly
    - performance may need segment-level tracking

- **What the agent does over iterations**
  - Iteration 0:
    - profile data
    - run EDA
    - write numeric-only logistic regression baseline
  - Later iterations:
    - inspect error analysis
    - test cleaning and encoding ideas
    - test group feature hypotheses
    - refine hyperparameters on the best recipe
  - Every change is evaluated and either **kept or reverted**

- **Two main contracts**
  - `experiment.py`
    - the only mutable artifact
    - must define:
      - `prepare_data(df, target_col)` returning train/test split data
      - `build_pipeline()` returning an unfitted sklearn pipeline or compatible estimator
    - can contain custom imputation, encodings, interactions, LightGBM, ensembles, etc.
  - `evaluator.py`
    - fixed judge, never modified
    - computes:
      - primary metric
      - `roc_auc`, `f1`, `precision`, `recall`, `balanced_accuracy`, `ks_stat`, `brier_score`
      - segment metrics
      - hard-constraint checks
      - latency on 1000 rows

- **Why domain knowledge matters**
  - The repo emphasizes that generic AutoML heuristics are easy; context-specific reasoning is hard.
  - It gives examples:
    - **semiconductor manufacturing**: defects are lot-relative, not just globally extreme
    - **fraud detection**: signal is relative to merchant behavior and time of day
    - **healthcare**: a “normal” lab value may be abnormal for a patient baseline
  - Domain knowledge is used for:
    - EDA hypotheses
    - split strategy
    - feature ideas
    - error analysis
    - leakage guards

- **Output artifacts**
  - Each run writes to `outputs/run_<id>/`
  - Includes:
    - `mission_snapshot.yaml`
    - `profile.json`
    - EDA scripts/results
    - per-experiment diagnostics
    - experiment ledger
    - exact evaluated `experiment.py` files
    - `final_experiment.py`
    - `final_pipeline.pkl`
    - `report.md`

- **Final report contents**
  - Mission summary
  - Dataset profile
  - Experiment counts and outcomes
  - Baseline vs best comparison
  - What helped and failed
  - Domain knowledge findings
  - Final recommendation
  - Suggested next steps

- **Scope and limitations**
  - Supported:
    - tabular binary classification
    - logistic regression, LightGBM, XGBoost
    - group/time/stratified splits
    - reproducible tracking
  - Not supported:
    - multi-class
    - regression
    - deep learning
    - unrestricted imports
    - cloud/distributed execution
    - deployment automation
  - The repo explicitly says this is a **proof of concept**, not a replacement for a full-time data scientist.

- **Key files**
  - `PROGRAM.md` — permanent behavioral contract
  - `mission.yaml` — run-specific instructions and domain knowledge
  - `experiment.py` — mutable experiment file
  - `ml_agent/evaluator.py` — fixed evaluator
  - `RECIPES.md` — playbook of problem patterns

- **Design principles**
  - one mutable file
  - fixed judge
  - domain knowledge first
  - data/features before model
  - track everything
  - optimize for a usable recipe/pipeline/report, not just a score

### Assessment
This is a **mixed** content type: part tool/repository documentation, part opinionated manifesto about why agentic AutoML should focus on recipes rather than model search. Durability is **medium**: the conceptual framing around domain knowledge, leakage, and split strategy is fairly durable, but the implementation depends on current Claude Code workflows and specific library choices like LightGBM/XGBoost. Density is **high** because it includes architecture, workflow, YAML schema, file contracts, output structure, and design principles. Originality is mostly **primary source** with some synthesis/inspiration from `karpathy/autoresearch`. It’s best used as **refer-back** material if you are evaluating or adopting the project, since the repo’s value is in its workflow and contracts. Scrape quality is **good**: the main README content, examples, and structure appear intact, though this summary cannot verify code files or linked docs beyond the provided text.
