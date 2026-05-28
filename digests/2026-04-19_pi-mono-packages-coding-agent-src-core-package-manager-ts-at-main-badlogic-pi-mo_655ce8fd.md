---
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/src/core/package-manager.ts#L1608
title: pi-mono/packages/coding-agent/src/core/package-manager.ts at main · badlogic/pi-mono
scraped_at: '2026-04-19T08:33:59Z'
word_count: 7277
raw_file: raw/2026-04-19_pi-mono-packages-coding-agent-src-core-package-manager-ts-at-main-badlogic-pi-mo_655ce8fd.txt
tldr: This TypeScript file implements `DefaultPackageManager`, a resource/package resolver that installs, updates, removes, and discovers extension-like content from npm, git, local paths, and filesystem conventions across user/project/temporary scopes.
key_quote: Project wins over user
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people: []
tools:
- npm
- git
- glob
- ignore
- minimatch
libraries: []
companies:
- pi-mono
tags:
- package-management
- resource-discovery
- npm
- git
- typescript
---

### TL;DR
This TypeScript file implements `DefaultPackageManager`, a resource/package resolver that installs, updates, removes, and discovers extension-like content from npm, git, local paths, and filesystem conventions across user/project/temporary scopes.

### Key Quote
"Project wins over user"

### Summary
- **What it is**
  - A core package/resource manager for the `pi-mono` coding agent.
  - Handles package sources from:
    - `npm:` specs
    - git URLs
    - local paths
  - Resolves four resource types:
    - `extensions`
    - `skills`
    - `prompts`
    - `themes`

- **Main responsibilities**
  - Install, remove, and update packages.
  - Persist package sources in global/user or project settings.
  - Resolve installed packages into concrete resource file paths.
  - Auto-discover resources from filesystem conventions.
  - Emit progress events for install/remove/update/clone/pull actions.

- **Offline mode**
  - Enabled via `PI_OFFLINE=1|true|yes`.
  - In offline mode, update checks and network-dependent refresh/install behavior are skipped or short-circuited.

- **Package resolution and precedence**
  - Packages are deduped by identity so the same package in both global and project settings keeps the **project** version.
  - Resource precedence ranking is explicit:
    - project + local settings
    - project + auto-discovered
    - user + local settings
    - user + auto-discovered
    - package resources last
  - Resolved resources are sorted so name-collision handling can prefer higher-precedence entries.

- **Resource discovery rules**
  - Extensions:
    - Prefer `package.json` `pi.extensions`
    - Otherwise look for `index.ts` or `index.js`
    - Otherwise recursively collect `.ts` / `.js` files
  - Skills:
    - Prefer `SKILL.md`
    - In `"pi"` mode, also accepts top-level `.md` files
    - Supports ancestor `.agents/skills` discovery for git-repo/project contexts
  - Prompts:
    - `.md` files
  - Themes:
    - `.json` files
  - Hidden files and `node_modules` are skipped.

- **Ignore handling**
  - Reads `.gitignore`, `.ignore`, and `.fdignore`.
  - Prefixes ignore rules based on directory depth so nested ignore files apply correctly.
  - Uses `ignore` plus `minimatch` for matching.

- **Pattern/filter support**
  - Supports plain include patterns plus override syntax:
    - `!pattern` = exclude
    - `+path` = force-include exact path
    - `-path` = force-exclude exact path
  - Used for both package manifests and local settings entries.
  - Empty filter arrays explicitly disable all resources of that type.

- **Install/update behavior**
  - **npm**
    - Global installs use `npm install -g`
    - Project installs use `--prefix`
    - Temporary installs go into hashed temp directories under `tmpdir()`
    - Pinned npm versions are detected and preserved
    - Update checks compare installed version to `npm view <package> version --json`
  - **git**
    - Clones into scope-specific directories
    - Checks out ref if provided
    - Runs `npm install --omit=dev` when a `package.json` exists
    - Updates fetch only the needed ref, then `reset --hard` and `clean -fdx`
    - Temporary git sources can be refreshed on demand
  - Local sources are just validated/resolved, not installed.

- **Update checks**
  - `checkForAvailableUpdates()` checks all configured packages with concurrency limit `4`.
  - Skips local and pinned packages.
  - For git packages, compares local `HEAD` with remote `HEAD` or upstream branch.
  - For npm packages, compares installed version against latest published version.

- **Settings integration**
  - Can add/remove sources to/from user or project settings.
  - Normalizes local paths relative to the correct base directory when persisting.
  - `listConfiguredPackages()` reports scope, whether the setting is filtered, and installed path.

- **Error/suggestion behavior**
  - When update targets don’t match configured packages, it throws a “No matching package found...” error.
  - It can suggest likely matching configured packages based on npm name or git host/path.

- **File system details**
  - Uses recursive directory walking with symlink checks.
  - Prunes empty parent directories after removing git packages.
  - Creates `.gitignore` files in install roots to keep package directories clean.
  - Uses hashed temp paths for temporary installs.

### Assessment
Durability is **medium**: the overall package-manager patterns are reusable, but the exact behavior is tied to this repository’s resource model, settings schema, and current install/update conventions. Content type is **mixed** but primarily **reference/tutorial** for maintainers of this codebase. Density is **high**, with many implementation details, path rules, and edge cases packed into one file. Originality is a **primary source** implementation rather than commentary or synthesis. Reference style is **deep-study** if you need to modify package discovery, update logic, or scope precedence; otherwise **refer-back** for specific behaviors like filtering or git/npm install semantics. Scrape quality is **good** overall: the code content appears complete in the provided excerpt, though I can’t verify surrounding file context, tests, or related docs from this scrape alone.
