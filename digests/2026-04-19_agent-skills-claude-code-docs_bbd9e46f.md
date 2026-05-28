---
url: https://code.claude.com/docs/en/skills
title: Agent Skills - Claude Code Docs
scraped_at: '2026-04-19T04:02:11Z'
word_count: 5274
raw_file: raw/2026-04-19_agent-skills-claude-code-docs_bbd9e46f.txt
tldr: Claude Code “skills” are reusable, file-based prompts plus optional assets/scripts that extend Claude’s behavior, with controls for discovery, invocation, permissions, subagents, arguments, and sharing.
key_quote: “Skills extend what Claude can do. Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit.”
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Claude Code
- GitHub CLI
libraries: []
companies:
- Anthropic
- Claude Code
tags:
- ai-agents
- documentation
- prompt-engineering
- developer-tools
- workflow-automation
---

### TL;DR
Claude Code “skills” are reusable, file-based prompts plus optional assets/scripts that extend Claude’s behavior, with controls for discovery, invocation, permissions, subagents, arguments, and sharing.

### Key Quote
“Skills extend what Claude can do. Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit.”

### Summary
- **What skills are**
  - A skill is a directory centered on a required `SKILL.md` file.
  - Skills let you package instructions for repeated workflows, instead of pasting the same playbook into chat.
  - They load only when used, so they are lighter than keeping the same content in `CLAUDE.md`.
  - Claude Code says custom commands have been merged into skills.

- **Standards and scope**
  - Claude Code skills follow the open standard at **Agent Skills** (`agentskills.io`).
  - Claude Code extends the standard with:
    - **invocation control**
    - **subagent execution**
    - **dynamic context injection**

- **Bundled skills**
  - Claude Code includes built-in bundled skills available in every session:
    - `/simplify`
    - `/batch`
    - `/debug`
    - `/loop`
    - `/claude-api`
  - These are described as **prompt-based** skills rather than fixed-logic commands.

- **Getting started / first skill**
  - Create a directory like:
    - `mkdir -p ~/.claude/skills/explain-code`
  - Add `SKILL.md` with YAML frontmatter and markdown instructions.
  - Example skill shown:
    - name: `explain-code`
    - description: explains code with visual diagrams and analogies
    - intended to trigger on questions like “how does this work?”
  - Test either by:
    - letting Claude trigger it automatically from matching text, or
    - invoking it directly: `/explain-code src/auth/login.ts`

- **Where skills live**
  - Skill location determines scope:
    - **Enterprise**: all users in an organization
    - **Personal**: `~/.claude/skills/<skill-name>/SKILL.md`
    - **Project**: `.claude/skills/<skill-name>/SKILL.md`
    - **Plugin**: `<plugin>/skills/<skill-name>/SKILL.md`
  - Priority order when names collide:
    - enterprise > personal > project
  - Plugin skills are namespaced as `plugin-name:skill-name`.

- **Discovery and live updates**
  - Claude Code watches skill directories for changes.
  - Editing/adding/removing a skill in watched directories takes effect in the current session.
  - If a top-level skills directory did not exist when the session started, Claude Code must be restarted for it to be watched.
  - It also discovers nested `.claude/skills/` directories in subfolders, useful for monorepos.
  - Skills in directories added via `--add-dir` are also loaded automatically.
  - Other `.claude/` config from added directories is not loaded by default.
  - CLAUDE.md from `--add-dir` directories requires `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`.

- **Skill content and frontmatter**
  - `SKILL.md` has:
    - YAML frontmatter at top
    - markdown instructions below
  - Frontmatter fields documented include:
    - `name`
    - `description`
    - `when_to_use`
    - `argument-hint`
    - `disable-model-invocation`
    - `user-invocable`
    - `allowed-tools`
    - `model`
    - `effort`
    - `context`
    - `agent`
    - `hooks`
    - `paths`
    - `shell`
  - The docs recommend at least a strong `description`, because Claude uses it to decide when to load the skill.
  - The combined `description` + `when_to_use` text is capped at **1,536 characters** in the skill listing.

- **Types of skill content**
  - **Reference content**
    - Provides knowledge Claude applies inline while working.
    - Example: API conventions, style guides, domain rules.
  - **Task content**
    - Provides step-by-step instructions for a specific workflow like deploy, commit, or code generation.
    - Often intended for manual use with `/skill-name`.
    - `disable-model-invocation: true` prevents automatic triggering.

- **String substitutions and arguments**
  - Skills support:
    - `$ARGUMENTS`
    - `$ARGUMENTS[N]`
    - `$N`
    - `${CLAUDE_SESSION_ID}`
    - `${CLAUDE_SKILL_DIR}`
  - If you pass arguments but don’t reference `$ARGUMENTS`, Claude Code appends them as `ARGUMENTS: ...`.
  - Example:
    - `/migrate-component SearchBar React Vue`
    - expands positional placeholders accordingly.

- **Supporting files**
  - Skills can include extra files besides `SKILL.md`:
    - templates
    - examples
    - scripts
    - reference docs
  - The docs recommend keeping `SKILL.md` under **500 lines** and moving detailed material into separate files.
  - Supporting files are meant to keep the main skill focused while avoiding unnecessary context loading.

- **Invocation control**
  - By default, both user and Claude can invoke skills.
  - `disable-model-invocation: true`
    - only the user can invoke the skill
    - useful for side-effect workflows like `/deploy`
  - `user-invocable: false`
    - only Claude can invoke the skill
    - useful for background knowledge skills
  - The docs show a matrix clarifying when each mode loads into context.

- **Skill lifecycle**
  - When a skill is invoked, its rendered content enters the conversation as a single message and stays for the rest of the session.
  - Claude Code does not reread the file on later turns.
  - After auto-compaction, the most recent invocation of each skill may be reattached, but token budgets can drop older skills.
  - If a skill seems to stop influencing behavior, the docs suggest:
    - strengthening the description/instructions
    - using hooks for deterministic enforcement
    - reinvoking after compaction if needed

- **Permissions and tool access**
  - `allowed-tools` grants permission to specified tools while the skill is active.
  - It does not remove other tool access; general permission settings still apply.
  - Example: a `commit` skill can allow `git add`, `git commit`, `git status` without repeated approval.
  - You can also control access more broadly via permission rules:
    - disable all skills
    - allow/deny specific skills like `Skill(commit)` or `Skill(deploy *)`

- **Advanced patterns**
  - **Inject dynamic context**
    - Use `!command` or fenced `!` blocks to run shell commands before the skill is sent to Claude.
    - Example: fetch PR diff/comments via `gh pr diff` and inject the output.
    - This is preprocessing; Claude only sees the rendered result.
  - **Run skills in a subagent**
    - `context: fork` runs the skill in isolation.
    - `agent:` chooses the subagent type, like `Explore`.
    - Best for explicit task-oriented skills.
  - **Extended thinking**
    - The docs note you can enable it by including the word **“ultrathink”** anywhere in skill content.

- **Sharing skills**
  - Skills can be distributed through:
    - project repos (`.claude/skills/`)
    - plugins
    - managed/organization-wide settings

- **Visual output example**
  - The page includes a detailed example of a `codebase-visualizer` skill.
  - It uses a Python script to generate an interactive HTML file called `codebase-map.html`.
  - The visualization includes:
    - collapsible directory tree
    - file sizes
    - file-type colors
    - summary stats
    - bar chart of file types
  - This illustrates the pattern: skill instructions orchestrate, scripts do heavy lifting.

- **Troubleshooting**
  - If a skill doesn’t trigger:
    - improve keywords in the description
    - verify it appears in available skills
    - rephrase the request
    - invoke directly
  - If it triggers too often:
    - make the description more specific
    - use `disable-model-invocation: true`
  - If descriptions get cut short:
    - shorten descriptions
    - front-load key use cases
    - optionally raise `SLASH_COMMAND_TOOL_CHAR_BUDGET`

### Assessment
This is a **reference** page with some tutorial elements, and it’s fairly **high-durability** because it documents a configuration system and workflow patterns rather than time-sensitive news. The content is **high-density** and mostly **primary source** documentation from Claude Code/Anthropic, so it’s trustworthy for how the feature is intended to work, though it may age as the product evolves. It’s best used as a **refer-back** resource when creating or troubleshooting skills, especially for frontmatter, invocation rules, and advanced patterns like subagents and dynamic context. Scrape quality is **good**: the page structure, examples, and the long code sample are present, though the rendered page metadata/navigation clutter is also included.
