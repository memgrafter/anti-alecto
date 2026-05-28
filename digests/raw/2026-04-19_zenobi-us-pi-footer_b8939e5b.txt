# pi-footer

A composable footer for [`pi`](https://pi.dev) with provider-driven data and a compiled pipeline renderer.


- Template-based footer rendering with dynamic data from context providers.
- Context **providers** (data sources) that resolve values from the current state (e.g. model, git, time).
- Context transforms that reshape provider values (e.g. humanise, colorize).
- Left/right alignment + flex growth.
- Built-in providers for model, git, cwd/path, and time.
- Debug command for inspecting pipeline execution.
- API to register custom providers and transforms from other extensions.

## Usage

```sh
pi install @zenobius/pi-footer
```

## Quick start (60 seconds)

Create `~/.pi/agent/pi-footer.json`:

```json
{
  "$schema": "https://raw.githubusercontent.com/zenobi-us/pi-footer/main/config.schema.json",
  "template": [
    [
      "{path}",
      {
        "items": ["{model_provider}.{model_name}"],
        "align": "right"
      }
    ]
  ]
}
```

Then run:

```txt
/pi-footer reload
```

## Advanced template example

```json
{
  "$schema": "https://raw.githubusercontent.com/zenobi-us/pi-footer/main/config.schema.json",
  "template": [
    [
      "{model_provider}.{model_name} [{model_context_window}:{model_context_used | humanise_percent | context_used_color}]",
      "{path}",
      { "items": ["[{git_worktree_name}:{git_branch_name}]"], "align": "right" }
    ],
    [
      {
        "items": [
          "ctx:{model_context_used_tokens | humanise_number} in:{usage_tokens_read | humanise_number} out:{usage_tokens_write | humanise_number} $:{usage_cost_usd | round(4)} mode:{model_thinking_mode} plan:{usage_plan}"
        ],
        "align": "right"
      }
    ]
  ]
}
```

Renders:

```txt
openai-codex.gpt-4.0 [200k:64%] /mnt/Store/Projects/Mine/Github/pi-footer              [my-worktree:main]
ctx:128,400 in:110,002 out:18,398 $:0.2321 mode:normal plan:pro
```

## Architecture (provider → transform → transform)

> You can skip this section unless you are building custom providers/transforms.

Each `{ ... }` expression in a template is compiled into a pipeline.

Example:

```txt
{ model_context_used | humanise_percent | context_used_color }
```

Execution flow:

1. `model_context_used` provider resolves raw value (e.g. `64`)
2. `humanise_percent` updates text to `"64%"`
3. `context_used_color` applies theme color based on numeric value
4. Pipeline returns final text

Pipelines are parsed once (cached by template string) and executed each render.

---

## Template syntax

### Basic

```txt
{provider_key}
```

Literal sources are also supported:

```txt
{"static text"}
```

### Value transforms (pipelines)

```txt
{model_context_used | humanise_percent | context_used_color}
{"words" | fg("error")}
```

### Args: literal vs context reference

- **Quoted args** are literals:
  - `fg('accent')` → literal string `accent`
- **Unquoted args** are context refs:
  - `clamp(0, model_context_window)`

If an unquoted ref key does not exist, it falls back to the raw token string.

---

## Built-in providers

### Core

- `{time}` – current local time
- `{cwd}` – current directory name
- `{path}` – full current working directory path
- `{model_name}` – active model id
- `{model_provider}` – active model provider
- `{model_context_used}` – context usage as number `0..100`
- `{model_context_used_tokens}` – raw used context tokens
- `{model_context_window}` – context window (e.g. `200k`)
- `{model_thinking_level}` – current thinking level
- `{model_thinking_mode}` – best-effort compatibility alias for thinking mode (`-` when unavailable)
- `{usage_tokens_read}` – latest assistant read tokens (`input + cacheRead`)
- `{usage_tokens_write}` – latest assistant write tokens (`output + cacheWrite`)
- `{usage_cost_usd}` – cumulative branch/session assistant cost in USD
- `{usage_plan}` – best-effort account plan/tier from runtime metadata (`-` when unavailable)

### Git

- `{git_branch_name}`
- `{git_worktree_name}`
- `{git_status}` (structured object)
- `{recent_commits}` (structured object)


---

## Built-in transforms

- `humanise_time`
- `humanise_percent` (alias: `humanise_percentage`)
- `humanise_amount`
- `humanise_number`
- `round(n)`
- `clamp(min,max)`
- `fg('themeColor')`
- `bg('themeColor')`
- `thinking_level_icons('ascii' | 'unicode')`
- `git_status_icons('ascii' | 'unicode')`
- `context_used_color` (alias: `model_context_colors`)

`context_used_color` thresholds:

- `< 50` → success
- `50..79` → warning
- `>= 80` → error

---

## Template layout config

- A template is an array of rows.
- Each row can be a string, an array of strings, an array of template objects, or a mix. 
- Template objects support additional layout config (alignment, separator, flex growth).
- Before rendering, all strings are parsed into template objects (caching by string value) and compiled into pipelines. They align to the left by default.

Set in `services/config/defaults.ts` or override via `Config.template`.

> Note: The built-in default template remains intentionally compact for backwards compatibility; the expanded example below shows how to opt into `path`, token usage, cost, and plan fields.

Example:

`~/.pi/agent/pi-footer.json`

```json
{
  "$schema": "https://raw.githubusercontent.com/zenobi-us/pi-footer/main/config.schema.json",
  "template": [
    [
      "{path}",
      {
        "items": [
          "{model_provider}.{model_name} [{model_context_window}:{model_context_used | humanise_percent | context_used_color}]",
          "[{git_worktree_name}:{git_branch_name}]"
        ],
        "align": "right",
        "separator": " "
      }
    ],
    [
      {
        "items": [
          "ctx:{model_context_used_tokens | humanise_number}",
          "in:{usage_tokens_read | humanise_number}",
          "out:{usage_tokens_write | humanise_number}",
          "$:{usage_cost_usd | round(4)}",
          "mode:{model_thinking_mode}",
          "plan:{usage_plan}"
        ],
        "align": "right"
      }
    ]
  ]
}
```

Supported object item fields:

- `items: (string | FooterTemplateObjectItem)[]`
- `separator?: string`
- `align?: 'left' | 'right'`
- `flexGrow?: boolean`

---

## JSON Schema

The config schema is published as a JSON Schema document at:

- `https://raw.githubusercontent.com/zenobi-us/pi-footer/main/config.schema.json`

You can also use the normalized/internal shape schema at:

- `https://raw.githubusercontent.com/zenobi-us/pi-footer/main/resolved-config.schema.json`

Schemas are generated from `src/services/config/schema.ts` via:

```bash
mise run generate-schema
```

---

## Extension API usage

Providing more context values and transforms is a common use case for other extensions. 

For example: 

- a project management extension might want to provide current task/issue info from the active branch or project directory.
- a cost-tracking extension might want to provide more detailed cost breakdowns or projections based on current usage patterns.
- a system monitoring extension might want to provide resource usage stats or alerts.
- a subagent extension might want to track how many subagents are currently active and provide that as context.

```ts
import { Footer } from '@zenobius/pi-footer';

export default function yourCustomPiValuesExtension(): void {
  // Add provider
  Footer.registerContextValue('custom_value', ({ ctx }) => ctx.cwd.length);

  // Add pipeline transform
  Footer.registerContextTransform('custom_format', (state) => {
    if (state.source !== 'custom_value') return state;

    const value = `len=${state.value}`;

    return {
      ...state,
      value,
      text: value,
    };
  });
}
```

---

## Commands

- `/pi-footer` – show command help
- `/pi-footer providers` – show a scrollable list of registered context providers
- `/pi-footer debug {expr}` – inspect template pipeline execution for an expression
- `/pi-footer reload` – reload `~/.pi/agent/pi-footer.json` and rerender footer
- `/pi-footer <subcommand> [args]` – run extension-registered subcommands (e.g. `quota`)

Example:

```txt
/pi-footer debug {model_context_used | humanise_percent | context_used_color}
/pi-footer quota
```
