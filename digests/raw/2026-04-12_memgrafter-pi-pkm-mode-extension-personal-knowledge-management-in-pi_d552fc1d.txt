# pi-pkm-mode-extension

Personal knowledge management mode for **pi**.

## Quickstart
1. Install pi: `npm install -g @mariozechner/pi-coding-agent`
2. Install this extension: `pi install git:github.com/memgrafter/pi-pkm-mode-extension`
3. Create your pkm folder: `mkdir -p ~/code/pkm` (or any directory you choose)
4. Start pi with the extension: `pi -e /path/to/pi-pkm-mode-extension/extensions/pi-pkm-mode.ts`
6. In pi, run `/pkm on` (or just `/pkm`).
5. In pi, run: `Ask me my requirements and set up a personal knowledge management structure in ~/code/pkm.`

## Features

- `/pkm` toggle
- `/pkm on|off|status`
- `/pkm <text>` enables pkm mode and immediately sends `<text>`
- Optional startup flag:
  - `--pkm`
- If `pkm_path` (or `pkmPath`) is set in pi settings, pkm mode adds
  `My pkm is stored in <path>` to the pkm system prompt

## PKM path setting (optional)

Set either key in settings:

- Project: `.pi/settings.json`
- Global: `~/.pi/agent/settings.json`

```json
{
  "pkm_path": "~/code/pkm"
}
```

`pkm_path` takes precedence over `pkmPath` if both exist.
Project settings take precedence over global settings.

## Local usage

From this folder:

```bash
cd /Users/user/code/pi-pkm-mode-extension
pi -e ./extensions/pi-pkm-mode.ts
```

Or by absolute extension path:

```bash
pi -e /Users/user/code/pi-pkm-mode-extension/extensions/pi-pkm-mode.ts
```

Then in pi:

```text
/pkm
```

## Install as a package

```bash
pi install git:github.com/memgrafter/pi-pkm-mode-extension
# pinned
pi install git:github.com/memgrafter/pi-pkm-mode-extension@v0.1.0
```

Project-local install:

```bash
pi install -l git:github.com/memgrafter/pi-pkm-mode-extension
```
