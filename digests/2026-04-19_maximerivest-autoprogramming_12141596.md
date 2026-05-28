---
url: https://github.com/MaximeRivest/autoprogramming
title: MaximeRivest/autoprogramming
scraped_at: '2026-04-19T07:26:04Z'
word_count: 1729
raw_file: raw/2026-04-19_maximerivest-autoprogramming_12141596.txt
tldr: AutoProgramming is a Python framework that turns a typed function schema into an optimizable, packageable `.ap` program, then uses an agent to mutate prompts, models, parsers, and even classical ML/rule-based code until validation scores improve.
key_quote: “Define your inputs and outputs, and let AutoProgramming generate the code for you.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- MaximeRivest
tools:
- OpenAI
- scikit-learn
- transformers
libraries:
- autoprogramming
- difflib
companies:
- GitHub
tags:
- program-generation
- prompt-optimization
- agentic-workflows
- python-frameworks
- machine-learning-inference
---

### TL;DR
AutoProgramming is a Python framework that turns a typed function schema into an optimizable, packageable `.ap` program, then uses an agent to mutate prompts, models, parsers, and even classical ML/rule-based code until validation scores improve.

### Key Quote
“Define your inputs and outputs, and let AutoProgramming generate the code for you.”

### Summary
- **What it is**
  - A GitHub project named **AutoProgramming** by **MaximeRivest**.
  - Core idea: define a program by specifying **inputs, outputs, and types**, then let the framework generate and optimize the implementation.
  - Uses **type annotations** and **docstrings** as the schema/descriptions.

- **Basic usage**
  - Example:
    ```py
    import autoprogramming as ap

    class Answer(str): ...
    class Summary(str): ..

    @ap.program
    def my_program(question: str) -> tuple[Answer, Summary]: ...
    ```
  - You can initialize a program manually with:
    - `instructions`
    - `descriptions`
    - `demos`
    - `model` (example shown: `gpt-4.1`)
    - `adapter` (example: `XMLAdapter()`)
    - `temperature`
    - `max_tokens`

- **Optimization workflow**
  - `.optimize(data=train_df)` runs a coding agent that iteratively improves the program.
  - The agent:
    - creates a workspace like `translate.ap/`
    - writes `schema.py`, `metric.py`, training/validation data, and multiple candidate implementations in `candidates/`
    - evaluates each candidate and stores per-row scores in `scores.json`
    - uses a **reflect → copy → edit → evaluate** loop
  - Example candidate files are full Python modules containing:
    - SDK calls
    - prompt text
    - parsing logic
    - model selection
  - It explicitly says the approach is inspired by **GEPA**.

- **Illustrative example**
  - A translation task is shown:
    - input: `english: str`
    - output: `French(str)`
  - Candidate 0 uses an OpenAI chat completion call with `gpt-4.1-nano`.
  - A metric based on `difflib.SequenceMatcher` scores prediction similarity to expected output.
  - Candidate 1 improves the system prompt by asking for simpler, more direct phrasing.
  - The framework keeps the better candidate and activates it with:
    - `prg.best()`
    - `prg.activate("candidate_1")`

- **Agent API**
  - Exposed helpers include:
    - `prg.schema`
    - `prg.eval("candidate_0")`
    - `prg.eval("candidate_0", per_instance=True)`
    - `prg.run("candidate_0", english="Hello")`
    - `prg.best()`
    - `prg.activate("candidate_1")`
    - `prg.data.train`, `prg.data.val`, `prg.data.sample(20)`
  - Main idea: candidate development is just **file operations on `candidates/*.py`**.

- **How `.ap` programs are used**
  - A `.ap` directory is a **Python package**.
  - You can import and call the generated program like a normal function:
    ```py
    from translate_ap import translate
    translate("Hello, how are you?")
    ```
  - Return values are typed wrappers like `French`, which are subclasses of `str`.

- **Logging, retraining, distillation**
  - Programs can log inputs/outputs to JSONL via `translate.enable_logging()`.
  - Logged traffic can later be used to:
    - re-optimize: `translate.optimize(data="logs")`
    - distill into a smaller model: `translate.distill(model="gpt-4.1-nano", data="logs", output="translate-ft.ap")`

- **Distribution**
  - The `.ap` directory can be distributed like any Python package:
    - `pip install ./translate.ap`
    - copy the directory
    - zip it

- **How the agent builds a program**
  - The framework says the agent asks four questions:
    1. What goes in, what comes out? (schema)
    2. Do you have examples?
    3. What does “good” mean? (metric)
    4. Any constraints? (cost, offline, external APIs, etc.)
  - Then it searches freely.

- **Search space / candidate types**
  - The agent can explore multiple implementation styles:
    - **LLM prompting**
    - **Classical ML** (`scikit-learn`, pickled model)
    - **Regex/rule-based**
    - **Deep learning** (`transformers`, MarianMT)
    - **Decomposed pipelines** that combine methods
  - The key claim: the agent doesn’t care how a candidate works, only that it satisfies the schema and optimizes the metric.

- **Exploration strategy**
  - Four phases are described:
    - **Phase 1: Baseline sweep** — cheap heuristic, cheapest LLM, pretrained model
    - **Phase 2: Targeted mutation** — inspect low-scoring rows, trace failures, edit the best candidate
    - **Phase 3: Structural exploration** — try a different paradigm if progress stalls
    - **Phase 4: Pareto selection** — preserve candidates that are best on specific rows, not just globally best
  - Includes budget guidance:
    - ~10% baseline
    - ~60% targeted mutation
    - ~20% structural alternatives
    - ~10% final reevaluation
  - Stops mutating after 3 consecutive failures to improve.

### Assessment
This is a **mixed** technical/reference-style project page with tutorial-like examples and a fairly dense architecture description. Durability is **medium**: the underlying concepts (schema-driven program generation, agentic prompt optimization, evaluation loops) are durable, but concrete model names like **gpt-4.1**, **gpt-4.1-nano**, and the specific workspace layout/agent behavior may age with the project. Density is **high** because it includes many concrete code samples, API calls, file layouts, and workflow rules. Originality is best described as **primary source** for the project’s design and behavior, though it references **GEPA** as inspiration. Reference style is **refer-back** or **deep-study** depending on whether you want to implement or evaluate the framework. Scrape quality is **good**: the content appears complete and includes the main prose and code examples; no obvious missing sections are indicated, though any images or repository files outside the README are not captured here.
