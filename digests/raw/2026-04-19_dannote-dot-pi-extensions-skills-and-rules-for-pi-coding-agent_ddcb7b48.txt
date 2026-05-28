# dot-pi

Extensions, skills, and rules for [Pi](https://github.com/badlogic/pi-mono) coding agent.

## Demos

| Code Search | LSP |
|---|---|
| <a href="https://asciinema.org/a/HsHEscCk5Fq7s6Ym"><img src="https://asciinema.org/a/HsHEscCk5Fq7s6Ym.svg" width="400"></a> | <a href="https://asciinema.org/a/0cG65zf3s94wFSdt"><img src="https://asciinema.org/a/0cG65zf3s94wFSdt.svg" width="400"></a> |
| **Question** | **Web Fetch** |
| <a href="https://asciinema.org/a/E48GyE7AE3FRuk6U"><img src="https://asciinema.org/a/E48GyE7AE3FRuk6U.svg" width="400"></a> | <a href="https://asciinema.org/a/9oRM5g9BHrv00GnD"><img src="https://asciinema.org/a/9oRM5g9BHrv00GnD.svg" width="400"></a> |
| **Web Search** | **Voice Input** |
| <a href="https://asciinema.org/a/EPAESVHwuQOqyfB3"><img src="https://asciinema.org/a/EPAESVHwuQOqyfB3.svg" width="400"></a> | <a href="https://asciinema.org/a/holUXauSMlm8tnP6"><img src="https://asciinema.org/a/holUXauSMlm8tnP6.svg" width="400"></a> |

## Installation

```bash
pi install git:github.com/dannote/dot-pi
pi install npm:pi-subagents   # optional: subagent delegation (scout, planner, worker, etc.)
pi install npm:pi-context      # optional: agentic context window management
```

Use `pi config` to enable/disable individual extensions and skills.

Some extensions require external tools or API keys:

| Dependency | Required by |
|---|---|
| [ast-grep](https://ast-grep.github.io) (`brew install ast-grep`) | `ast-grep.ts` |
| [Exa AI](https://exa.ai) API key (`EXA_API_KEY`) | `websearch/` |
| [ElevenLabs](https://elevenlabs.io) API key (`ELEVENLABS_API_KEY`) | `voice-input/` |

## Extensions

| Extension | Description |
|---|---|
| `ast-grep.ts` | AST-based code search and rewrite |
| `background.ts` | Run long-running processes in background |
| `bash-completion/` | Intelligent bash completions for shell commands |
| `codesearch.ts` | Search public GitHub code via [grep.app](https://grep.app) |
| `context7/` | Search library documentation via [Context7](https://context7.com) |
| `confirm-destructive.ts` | Confirm before destructive actions (clear session, create PRs/issues) |
| `critic/` | Shadow reviewer that evaluates agent output |
| `env-json/` | Load environment variables from `~/.pi/agent/env.jsonc` |
| `lsp/` | Language Server Protocol (definition, references, hover, rename) |
| `notify.ts` | Desktop notifications on task completion |
| `permission-gate.ts` | Block dangerous bash commands |
| `question.ts` | Let the LLM ask user questions with selectable options |
| `rules.ts` | Load rule files from `~/.pi/agent/rules/` |
| `voice-input/` | Voice recording with ElevenLabs STT (Ctrl+R) |
| `webfetch/` | Fetch URL content and convert to markdown/text/html |
| `websearch/` | Web search via [Exa AI](https://exa.ai) |
| `worktrees/` | Git worktree management for parallel work |

<details>
<summary>Experimental extensions (not installed by default)</summary>

| Extension | Description |
|---|---|
| `decision-guidance.ts` | Decision-time guidance based on trajectory analysis |
| `plan-mode/` | Read-only plan mode toggle with step tracking |
| `provider/` | Dynamic provider registration from remote config |
| `sandbox/` | OS-level sandboxing for bash commands (WIP) |
| `subagent/` | Subagent delegation (superseded by [pi-subagents](https://www.npmjs.com/package/pi-subagents)) |

To enable an experimental extension:

```json
{
  "source": "git:github.com/dannote/dot-pi",
  "extensions": ["+extensions/plan-mode"]
}
```

</details>

## Skills

| Skill | Description |
|---|---|
| `agent-browser` | Browser automation with [agent-browser](https://github.com/vercel-labs/agent-browser) CLI |
| `ai-news` | Curated AI news digest from X/Twitter list |
| `applescript` | AppleScript and JXA automation for macOS |
| `bird` | X/Twitter CLI for tweets, threads, search, and social graph |
| `chat-to-skill` | Convert current chat session into a reusable skill |
| `github-issues` | Work with GitHub Issues via `gh` CLI — view, triage, fix, close |
| `keyboard-layout-decoder` | Decode text typed with wrong keyboard layout (Russian ↔ English) |
| `skill-discovery` | Discover agent skills on GitHub |

## Rules

Rules are not distributed via packages. Symlink desired rules into `~/.pi/agent/rules/`:

```bash
ln -s /path/to/dot-pi/rules/typescript.md ~/.pi/agent/rules/
```

| Rule | Description |
|---|---|
| `bun.md` | Use Bun instead of Node.js/npm |
| `comments.md` | Avoid redundant comments |
| `commit-messages.md` | Follow existing repo commit style |
| `delete-files.md` | Use `rm -f` to delete files |
| `git-hosting.md` | Use `gh`/`glab` CLI instead of fetching URLs |
| `pull-requests.md` | PR workflow: study templates, preview before submit |
| `ripgrep.md` | Prefer `rg` over `grep` |
| `skills-cli.md` | Run skill commands from skill directory |
| `typescript.md` | TypeScript naming, type safety, imports, async |

## License

MIT
