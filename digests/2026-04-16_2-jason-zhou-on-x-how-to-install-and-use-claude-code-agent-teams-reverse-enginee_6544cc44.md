---
url: https://x.com/jasonzhou1993/status/2020086991740891526?s=46
title: '(2) Jason Zhou on X: "How to install and use Claude Code Agent Teams (Reverse-engineered)" / X'
scraped_at: '2026-04-16T05:26:25Z'
word_count: 906
raw_file: raw/2026-04-16_2-jason-zhou-on-x-how-to-install-and-use-claude-code-agent-teams-reverse-enginee_6544cc44.txt
tldr: This X thread reverse-engineers Claude Code’s new “Agent Teams” feature, showing how to enable it, how it differs from sub-agents, and why its shared task/message system can outperform isolated agents for complex debugging—at the cost of more tokens and slower execution.
key_quote: '“Agent Teams introduce: *Shared task lists* *Message & communication between agents* *Explicit lifecycle control (startup, shutdown)*”'
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Jason Zhou
tools:
- Claude Code
- tmux
- iTerm2
libraries: []
companies:
- Anthropic
tags:
- ai-agents
- claude-code
- reverse-engineering
- debugging
- developer-tools
---

### TL;DR
This X thread reverse-engineers Claude Code’s new “Agent Teams” feature, showing how to enable it, how it differs from sub-agents, and why its shared task/message system can outperform isolated agents for complex debugging—at the cost of more tokens and slower execution.

### Key Quote
“Agent Teams introduce: *Shared task lists* *Message & communication between agents* *Explicit lifecycle control (startup, shutdown)*”

### Summary
- **What the thread is about**
  - Jason Zhou claims Claude Code has shipped a major upgrade called **Agent Teams**.
  - He says he **reverse-engineered** the feature by inspecting logs, model calls, and filesystem changes.
  - The core idea is that **3–5 Claude Code instances** can collaborate on one project with shared context and messaging.

- **How to enable it**
  - Update Claude Code to the latest version.
  - Enable an experimental flag by editing `~/.claude/settings.json`:
    ```json
    {
      "env": {
        "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
      }
    }
    ```
  - Restart the terminal after saving.
  - Start a new Claude Code session and explicitly ask it to create an agent team.

- **Suggested prompting pattern**
  - Example prompt: ask Claude Code to create a team with different perspectives, such as:
    - one teammate on UX
    - one on technical architecture
    - one as devil’s advocate
  - The thread says Claude Code will then create teammates automatically.

- **Recommended UI / environment**
  - He says Agent Teams work best when you can watch them in parallel using:
    - **tmux**, or
    - **iTerm2 on macOS**
  - iTerm2 setup mentioned:
    - install iTerm2
    - go to **Settings → General → Magic**
    - enable **Python API**
    - restart iTerm2
  - Then launch Claude Code with:
    ```bash
    claude --teammate-mode tmux
    ```
  - This opens:
    - one pane for the team lead
    - separate panes for each teammate
  - You can watch activity live and send direct messages to agents.

- **Old model vs new model**
  - **Old model: sub-agents / Task tool**
    - main agent calls task tool
    - sub-agent spins up
    - sub-agent works in isolation
    - session terminates
    - only a summary returns to the main agent
  - **New model: Agent Teams**
    - shared task lists
    - agent-to-agent communication
    - explicit lifecycle control like startup and shutdown

- **Internal tools described**
  - **TeamCreate**
    - creates a team folder under `.claude/teams/`
    - team scaffolding exists before agents are assigned
  - **TaskCreate**
    - creates new todo tasks, not agent sessions
    - tasks are stored as JSON under `.claude/tasks/team-id`
    - tracked fields include:
      - task ID
      - description
      - status: `pending`, `in_progress`, `complete`, `deleted`
      - owner
      - dependencies (`blocks`, `blocked_by`)
    - tasks can be assigned top-down by the team lead or self-claimed by agents
  - **Task tool**
    - still used to activate agents
    - now accepts new parameters like `name` and `team_name`
    - when those are provided, it uses Agent Teams instead of a simple sub-agent subprocess
  - **taskUpdate**
    - used by each agent to claim and update tasks
  - **sendMessage**
    - allows direct messages between agents and broadcasts to all teammates
    - messages are written to `.claude/teams/<team_id>/inbox/`
    - each agent has its own inbox
    - messages are injected into conversation history as teammate messages
  - **shutdown_request / shutdown_response**
    - team lead can request a teammate shutdown
    - teammate confirms shutdown
    - the author suspects a `postToolCall` hook is used to terminate sessions automatically

- **Use case where it shines**
  - The thread highlights a **deep debugging** scenario from official docs:
    - if an app exits after one message instead of staying connected,
    - spawn 5 agent teammates,
    - have them investigate different hypotheses,
    - let them challenge each other like a scientific debate,
    - update a findings doc with the consensus.
  - The author says this kind of workflow is where Agent Teams clearly beat sub-agents.

- **Author’s evaluation**
  - He says the feature **works great** in his testing.
  - But he warns about the trade-off:
    - **more token consumption**
    - **slower speed**
  - He does **not** think Agent Teams directly replace sub-agents yet.
  - He speculates they could be combined with some kind of loop mechanism for very long-running agentic tasks.

### Assessment
Durability is **medium**: the conceptual comparison between isolated sub-agents and collaborative agent teams is useful beyond this specific release, but the installation steps, feature flag, file paths, and CLI flags are tied to a particular Claude Code version and are likely to change. Content type is **mixed**—part tutorial, part reverse-engineered technical commentary, part opinionated evaluation. Density is **high**, since it includes concrete commands, flags, directory paths, tool names, and behavioral claims. Originality is **commentary/synthesis** with some reverse-engineering claims rather than official documentation, so it should be treated as informed but not authoritative. Reference style is **refer-back** if you are exploring Claude Code agent workflows or debugging the feature; otherwise skim-once is enough. Scrape quality is **partial**: the text captures the thread’s main points and code snippets, but image content and any linked media are not available, so some visual examples and context may be missing.
