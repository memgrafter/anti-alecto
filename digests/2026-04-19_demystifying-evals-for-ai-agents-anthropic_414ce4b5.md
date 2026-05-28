---
url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
title: Demystifying evals for AI agents \ Anthropic
scraped_at: '2026-04-19T07:16:18Z'
word_count: 5875
raw_file: raw/2026-04-19_demystifying-evals-for-ai-agents-anthropic_414ce4b5.txt
tldr: Anthropic argues that agent evals should be built early, grounded in real failures, and designed with robust tasks, graders, and transcripts so teams can measure regressions, compare models, and improve agents without relying on guesswork.
key_quote: “Evals give the whole team a clear hill to climb, turning ‘the agent feels worse’ into something actionable.”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mikaela Grace
- Jeremy Hadfield
- Rodrigo Olivares
- Jiri De Jonghe
- David Hershey
- Gian Segato
- Mike Merrill
- Alex Shaw
- Nicholas Carlini
- Ethan Dixon
- Pedram Navid
- Jake Eaton
- Alyssa Baum
- Lina Tawfik
- Karen Zhou
- Alexander Bricken
- Sam Kennedy
- Robert Ying
tools:
- Harbor
- Braintrust
- autoevals
- LangSmith
- Langfuse
- Phoenix
- AX
- Claude Code
- Agent SDK
libraries: []
companies:
- Anthropic
- Descript
- Bolt
- SWE-bench Verified
- Terminal-Bench
- BrowseComp
- WebArena
- OSWorld
- Qodo
- METR
- iGent
- Cognition
- Sierra
- Vals.ai
- Macroscope
- PromptLayer
- Stripe
- Shopify
tags:
- ai-agents
- evaluation
- benchmarking
- llm-ops
- agent-testing
---

### TL;DR
Anthropic argues that agent evals should be built early, grounded in real failures, and designed with robust tasks, graders, and transcripts so teams can measure regressions, compare models, and improve agents without relying on guesswork.

### Key Quote
“Evals give the whole team a clear hill to climb, turning ‘the agent feels worse’ into something actionable.”

### Summary
- The post defines **agent evals** as automated tests for AI systems, focusing on **multi-turn, tool-using agents** where mistakes can compound across steps.
- It introduces core terminology:
  - **Task**: one test case with inputs and success criteria
  - **Trial**: one run of a task; multiple trials reduce variance
  - **Grader**: logic that scores performance; can include multiple assertions
  - **Transcript/trace/trajectory**: full record of the run, including tool calls and intermediate results
  - **Outcome**: final environment state, not just what the agent said
  - **Eval harness**: infrastructure that executes and grades evals end-to-end
  - **Agent harness/scaffold**: the system that lets the model act as an agent
  - **Eval suite**: a collection of related tasks
- Main thesis: teams often get by early with manual testing, but once agents scale, **without evals they end up “flying blind”**—reacting to user complaints, reproducing bugs manually, and missing regressions.
- Anthropic frames evals as valuable at every stage:
  - early: clarify what “success” means
  - later: preserve quality and catch regressions
  - during model upgrades: quickly compare options and adopt new models faster
- The article distinguishes **capability/quality evals** from **regression evals**:
  - capability evals start hard, with low pass rates, to measure what the agent can newly do
  - regression evals should be near-100% pass rate and protect existing behavior
  - capability evals that mature can be “graduated” into regression suites
- It recommends combining three grader types:
  - **Code-based graders**: fast, cheap, objective, reproducible; examples include string matching, static analysis, outcome verification, and tool-call verification
  - **Model-based graders**: flexible and nuanced; examples include rubric scoring, pairwise comparison, and multi-judge consensus
  - **Human graders**: gold standard for calibration, especially for subjective tasks, but expensive and slow
- It stresses that graders should often score **what the agent produced, not the exact path it took**, because rigid sequence-of-steps checks can be brittle and punish valid creative solutions.
- It explains two key metrics for stochastic agents:
  - **pass@k**: chance of at least one success in k tries
  - **pass^k**: chance all k trials succeed, useful when consistency matters
- The post walks through eval design by agent type:
  - **Coding agents**: usually best evaluated with deterministic tests, plus transcript-level grading for code quality and tool use; examples mentioned include **SWE-bench Verified** and **Terminal-Bench**
  - **Conversational agents**: need end-state checks plus rubrics for tone, empathy, and task completion; often require a simulated user; examples include **τ-Bench** and **τ2-Bench**
  - **Research agents**: harder to evaluate because correctness is contextual and subjective; useful graders include groundedness, coverage, and source-quality checks; **BrowseComp** is mentioned as a hard web-retrieval benchmark
  - **Computer/browser use agents**: evaluated in real or sandboxed environments by checking UI, filesystem, database, or backend state; examples include **WebArena** and **OSWorld**
- It gives several practical steps for building evals:
  - start early with **20–50 tasks** drawn from real failures
  - begin from manual checks, bug reports, and support tickets
  - write **unambiguous tasks** with reference solutions
  - build **balanced problem sets** so the agent is tested both when it should and shouldn’t act
  - use a **stable, isolated environment** to avoid flakiness and shared-state contamination
  - choose graders carefully and allow partial credit when appropriate
  - read transcripts to verify that failures are fair and graders are correct
  - watch for **saturation**, where a benchmark becomes too easy and stops measuring improvement
  - maintain eval suites over time with clear ownership and regular updates
- It includes concrete cautionary examples:
  - **Opus 4.5** “failed” a τ2-bench flight-booking task by finding a loophole that was actually better for the user, showing that static evals can miss superior solutions
  - **Opus 4.5 on CORE-Bench** reportedly jumped from **42% to 95%** after fixing grading/task issues and using a less constrained scaffold
  - **SWE-Bench Verified** is described as moving from around **30%** earlier in the year to **>80%** for frontier models, illustrating benchmark saturation
- The article ends with a broader evaluation stack beyond automated evals:
  - **production monitoring**
  - **A/B testing**
  - **user feedback**
  - **manual transcript review**
  - **systematic human studies**
  - Anthropic recommends combining these, with automated evals as the first line of defense and human review for calibration.
- It closes by noting that agent evaluation is still a **nascent, fast-evolving field**, and mentions several tools/frameworks:
  - **Harbor**: containerized eval runs and task/grader formats
  - **Braintrust**: offline evals plus production observability; `autoevals`
  - **LangSmith**: tracing, offline/online evals, dataset management
  - **Langfuse**: self-hosted alternative
  - **Arize Phoenix / AX**: tracing, debugging, evals, monitoring
- The final recommendation is pragmatic: pick a framework that fits, but focus most energy on **high-quality tasks and graders**, since tooling is only as good as the evals themselves.

### Assessment
This is a **high-durability** reference article with a **mixed** content type: part tutorial, part technical guidance, part product/engineering essay. It is **high-density** and **primary-source commentary/synthesis** from Anthropic’s engineering team, with examples drawn from their internal experience and named benchmarks/products. It’s best used as a **refer-back** resource rather than a one-time skim, especially if you’re building or evaluating AI agents. Scrape quality is **good**: the main article content, tables, examples, and concluding tool recommendations are present, though the formatting is plain text and any original visual layout/embedded media is not included.
