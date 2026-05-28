---
url: https://github.com/VTSTech/ACP-Agent-Control-Panel/blob/main/ACP-Specification.md
title: ACP-Agent-Control-Panel/ACP-Specification.md at main · VTSTech/ACP-Agent-Control-Panel
scraped_at: '2026-04-19T08:02:49Z'
word_count: 12094
raw_file: raw/2026-04-19_acp-agent-control-panel-acp-specification-md-at-main-vtstech-acp-agent-control-p_7c0989cf.txt
tldr: ACP 1.0.6 is a draft REST/JSON-RPC specification for an AI-agent sidecar that logs, monitors, controls, and recovers agent sessions, with multi-agent A2A support, token tracking, file/shell/TODO management, and session context recovery.
key_quote: ACP provides a standardized way to monitor, control, and recover AI agent sessions through a RESTful HTTP API.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- VTSTech
- Community Contributors
tools:
- cloudflared
libraries:
- jsonrpc2
companies:
- GitHub
tags:
- ai-agents
- api-specification
- session-management
- observability
- multi-agent-systems
---

### TL;DR
ACP 1.0.6 is a draft REST/JSON-RPC specification for an AI-agent sidecar that logs, monitors, controls, and recovers agent sessions, with multi-agent A2A support, token tracking, file/shell/TODO management, and session context recovery.

### Key Quote
“ACP provides a standardized way to monitor, control, and recover AI agent sessions through a RESTful HTTP API.”

### Summary
- **What ACP is**
  - The Agent Control Panel (ACP) is presented as a monitoring and observability protocol for AI agents.
  - It is explicitly contrasted with MCP and A2A: ACP is for **sidecar-style monitoring/control**, not tool injection or primary agent-to-agent transport.
  - The spec is **Version 1.0.6**, **Status: Draft**, authored by **VTSTech, Community Contributors**.

- **Core design goals**
  - Sidecar architecture: ACP runs alongside the agent, not between agent and user.
  - REST-first API, with JSON-RPC 2.0 added for A2A compatibility.
  - Stateless server with persistent JSON storage.
  - “Log-first” workflow: agents must log actions before executing them.
  - Mandatory integration: actions, shell commands, and TODO changes must be tracked.

- **What it tracks and controls**
  - **Activity tracking**: READ, WRITE, EDIT, BASH, TODO, SKILL, API, SEARCH, CHAT, A2A.
  - **Token estimation**: approximate usage via a ~3.5 chars/token heuristic.
  - **STOP ALL**: emergency stop flag to cancel running activities.
  - **TODO state**
  - **Shell history**
  - **File management**
  - **Context recovery** via session summaries and AI notes.
  - **Remote access** via optional cloudflared tunnel.
  - **Agent registry** and **inter-agent messaging** introduced in 1.0.4.

- **Data model**
  - Session state is stored in a single JSON file (`agent_activity.json`) containing:
    - running/history activities
    - stop flag/reason
    - token totals
    - TODOs
    - shell history
    - AI notes
    - primary agent, per-agent token breakdown
    - file-read token deduplication
    - agents registry
    - A2A messages/contexts
  - Important evolution:
    - `primary_agent` owns the main context window
    - `agent_name` is identity; `model_name` is separate execution model metadata
    - ownership enforcement: only the owning agent may complete its activity, otherwise HTTP 403

- **Activity object**
  - Includes fields like:
    - `id`, `action`, `target`, `details`, `status`
    - timestamps, token counts, result/error, duration
    - `priority` and arbitrary `metadata`
  - `CHAT` was added to capture conversational/cognitive token usage without tool execution.

- **A2A support**
  - ACP 1.0.4 adds:
    - **Agent Registry**: register/list/unregister agents and expose capabilities/status
    - **A2A Messaging**: send/history endpoints using message queue semantics
    - **A2A Contexts**: `contextId` groups related tasks
    - **A2A Task mapping**: ACP activities map to A2A task states
    - **AgentSkill** and **AgentCard** models for discovery/compliance
  - A2A messages support:
    - request / response / notification
    - priorities normal / high / urgent
    - TTL and expiration
  - A2A hints are returned in activity responses to notify agents of pending messages.

- **API surface**
  - Authentication: HTTP Basic Auth required for all endpoints.
  - CSRF protection: optional, off by default, enabled via `GLMACP_CSRF_ENABLED=true`.
  - Core endpoints include:
    - `/api/status`, `/api/running`, `/api/history`, `/api/all`
    - `/api/start`, `/api/complete`, `/api/action`, `/api/stop`, `/api/resume`
    - `/api/shutdown`, `/api/reset_session`, `/api/reset`
    - `/api/todos/*`, `/api/shell/*`
    - `/api/summary`, `/api/summary/export`, `/api/notes/*`
    - `/api/files/*`
    - `/api/system`, `/api/session`, `/api/session/refresh`
    - `/api/csrf-token`, `/api/whoami`
    - `/api/nudge`, `/api/agents/*`, `/api/a2a/*`
    - JSON-RPC endpoints at `/jsonrpc`, `/a2a`, `/api/jsonrpc`
  - `/api/action` is the recommended combined endpoint for completing the previous activity and starting a new one in one request.

- **Workflow the spec expects agents to follow**
  - Bootstrap first:
    - check `/api/status`
    - call `/api/whoami`
    - register agent capabilities
    - log a bootstrap CHAT activity
  - Before every task:
    - check stop flag
    - log activity first, then perform the action, then complete it
  - Shell commands should be logged to both activity and shell history.
  - TODO state should be synchronized with ACP.
  - Agents should check A2A hints and retrieve pending messages when present.

- **Context recovery**
  - ACP supports restoring session state after compression or restart using:
    - `/api/summary`
    - `/api/summary/export`
    - `acp_session_summary.md`
    - AI notes and TODOs
  - Notes can be categorized as decision, insight, context, warning, or todo.

- **Security and limitations**
  - Basic Auth is required; rate limiting exists for failed logins.
  - File access is protected against path traversal in v1.0.6 via `sanitize_path()`.
  - File viewing/upload sizes are limited.
  - CSRF is optional rather than mandatory, which is convenient for dev but weaker for exposed deployments.
  - The spec emphasizes safe multi-agent ownership, orphan filtering, and session integrity.

- **Version history highlights**
  - **1.0.1**: CHAT action, `content_size`, priorities, metadata, `/api/activity/{id}`, `/api/whoami`, activity hints.
  - **1.0.2**: nudge API, orphan warnings, shutdown workflow.
  - **1.0.3**: `model_name`, file deduplication, duration stats, batch operations, cloudflared tunnel, per-agent tokens.
  - **1.0.4**: agent registry, A2A messaging, AgentSkill/AgentCard, A2A context support, full reset.
  - **1.0.5**: `primary_agent` in whoami, nudges only to primary agent.
  - **1.0.6**: shell history, TODO toggle, CORS preflight handler, path traversal fixes, session metadata additions, restart and A2A bug fixes.

### Assessment
This is a **mixed reference/specification document** with high procedural density and many concrete API details, schemas, and versioned changes. Its durability is **medium**: the conceptual model of agent observability, ownership, and session recovery is fairly durable, but the exact endpoints, environment variables, and version-specific behavior are tied to this particular implementation and may evolve quickly. The document is **primary source** material for the ACP project rather than a synthesis or commentary, and it is best used as a **refer-back** reference rather than a one-time skim because it contains extensive endpoint schemas, workflow requirements, and changelog details. Scrape quality appears **good** overall: the content is complete enough to reconstruct the spec structure, including tables, code blocks, and the changelog, though diagrams are represented as text and any visual formatting from GitHub may be simplified.
