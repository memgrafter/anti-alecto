---
url: https://docs.google.com/document/d/e/2PACX-1vT_YBcDeb6iPMyLKz2loRVqjrNYas4gpBB4yjT0kd6qqEqZFTnybJBmgCtQ9Xuh7EmAUk5825TRDZsT/pub
title: 'Interview Question: AI Inference Loop & Tool Registration'
scraped_at: '2026-04-19T07:00:43Z'
word_count: 1782
raw_file: raw/2026-04-19_interview-question-ai-inference-loop-tool-registration_853f6c65.txt
tldr: A structured interview prompt for testing whether a candidate truly understands the agent inference loop, tool registration, and the separation between the model, orchestrator, and tool runtime.
key_quote: the model never "sees" or "has" the function. It sees a JSON description and generates a structured request to call it.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- LangChain
- CrewAI
- AutoGen
libraries: []
companies: []
tags:
- ai-agents
- tool-calling
- interview-prep
- llm-orchestration
- software-architecture
---

### TL;DR
A structured interview prompt for testing whether a candidate truly understands the agent inference loop, tool registration, and the separation between the model, orchestrator, and tool runtime.

### Key Quote
"the model never \"sees\" or \"has\" the function. It sees a JSON description and generates a structured request to call it."

### Summary
- The document is an interview guide for a whiteboard-and-code question titled **“AI Inference Loop & Tool Registration.”**
- Core prompt to the candidate: explain how an AI agent completes a **multi-step task** from user message to final response, assuming access to external tools, then diagram it and show how you’d implement the loop in code.
- The exercise is intentionally open-ended and is meant to test **understanding of agent machinery**, not memorization of a framework.

- **Suggested interview timing:** 25–35 minutes total
  - 10–12 min whiteboard
  - 12–15 min code walkthrough
  - 5 min follow-ups

- **What a strong candidate should understand:**
  - The agent runs an **iterative loop**: prompt → inference → parse → execute → append → re-infer.
  - **Tool schemas** are passed along with the model call; the model chooses among them, but does not execute them.
  - The system has clear separation of concerns:
    - **Model** = stateless text generator / inference engine
    - **Orchestrator** = loop controller
    - **Runtime / executor** = actual tool execution
  - **State management** lives in the message array; each loop iteration appends to conversation history.
  - **Termination** happens when the model returns text with no tool call, or when max iterations / error thresholds are reached.
  - **Error handling** should consider tool failure, timeouts, and invalid outputs.

- **Expected diagram flow:**
  - User message enters the orchestrator
  - Orchestrator assembles message array including:
    - system prompt
    - tool schemas
    - prior messages
  - Orchestrator calls the LLM API
  - Response is parsed into either:
    - plain text, or
    - one or more tool calls
  - Tool calls are executed outside the model
  - Tool results are appended back to the message array
  - The loop returns to the LLM until a final text response is produced

- **Key conceptual requirements in the diagram:**
  - Explicit loop back from tool result append to another model call
  - Tool schemas shown as input to the LLM request
  - Tool execution shown outside the model
  - A visible stop condition when no tool call is returned

- **Example code shape expected:**
  - A `run_agent(...)` loop with:
    - initial messages
    - repeated `llm_client.chat(...)`
    - tool schemas passed in a `tools=` parameter
    - assistant response appended to history
    - tool calls extracted and executed
    - tool results appended with `tool_use_id`
  - A tool registry / dispatch layer mapping tool names to real functions
  - Error handling for unknown tools and runtime exceptions

- **Important implementation detail emphasized by the doc:**
  - Append the assistant response to the conversation **before** processing tool calls.
  - This is called out as the most common mistake.

- **Example tool schema pattern:**
  - Tools are represented as JSON schemas with:
    - `name`
    - `description`
    - `input_schema`
  - The tool registry maps names like `search_database`, `send_email`, and `get_calendar` to actual functions.

- **The central insight the interviewer is looking for:**
  - The model does **not** directly run functions or “access tools.”
  - It reads schemas and produces a structured tool request.
  - The orchestrator dispatches that request to real code.

- **Follow-up questions suggested by the doc:**
  - What if the model hallucinates a nonexistent tool?
  - How does the model choose among many tools?
  - What does the message array look like after several dependent tool calls?
  - How do you handle slow tools, infinite loops, and token/context limits?
  - How would you make this observable in production?
  - How is this different from a fine-tuned model that “just knows” the task?

- **Evaluation guidance included in the document:**
  - Senior/staff candidates should clearly explain the loop, write clean code, and proactively discuss production concerns.
  - Mid-level candidates should get the loop and tool registration right with limited prompting.
  - Junior candidates should at least understand the conceptual loop and model/orchestrator separation.

- **Common misconceptions the guide warns against:**
  - “The AI calls the function” — incorrect; the orchestrator does.
  - “You train the model on your tools” — incorrect; tools are registered at runtime.
  - “The model remembers what happened last time” — incorrect; the orchestrator maintains state.
  - Over-reliance on frameworks like LangChain/CrewAI/AutoGen without understanding what they do underneath.

### Assessment
This is a **reference/interview prep** document with high practical density and strong specificity. Its durability is **medium to high**: the exact examples, naming, and prompt wording may age with LLM API changes, but the underlying concepts—agent loops, tool schemas, orchestration, state management, and error handling—are durable. The content type is **mixed**, mostly instructional/reference with evaluation criteria. Originality is **primary source / authored guidance** rather than a synthesis of external material. It’s best used as **refer-back** material for interviewing or calibrating candidate depth. **Scrape quality is good**: the full text appears captured, including the prompt, example pseudocode, scoring signals, and follow-up questions, though formatting/diagram structure is flattened into plain text.
