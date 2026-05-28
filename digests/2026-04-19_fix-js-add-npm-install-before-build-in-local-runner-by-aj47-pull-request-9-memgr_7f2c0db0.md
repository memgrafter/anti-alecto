---
url: https://github.com/memgrafter/flatagents/pull/9/changes
title: 'fix(js): add npm install before build in local runner by aj47 · Pull Request #9 · memgrafter/flatmachines'
scraped_at: '2026-04-19T07:50:40Z'
word_count: 85
raw_file: raw/2026-04-19_fix-js-add-npm-install-before-build-in-local-runner-by-aj47-pull-request-9-memgr_7f2c0db0.txt
tldr: This PR fixes the JavaScript local runner by inserting `npm install` before `npm run build` so the local Flatmachines SDK can build with its dependencies installed.
key_quote: 'fix(js): add npm install before build in local runner'
durability: medium
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- AJ
tools:
- npm
libraries:
- '@memgrafter/flatmachines'
companies:
- memgrafter
tags:
- javascript
- build-system
- npm
- pull-request
- local-development
---

### TL;DR
This PR fixes the JavaScript local runner by inserting `npm install` before `npm run build` so the local Flatmachines SDK can build with its dependencies installed.

### Key Quote
"fix(js): add npm install before build in local runner"

### Summary
- This is a one-line patch to `sdk/examples/coding_machine_cli/js/run.sh`.
- In the `LOCAL_INSTALL=true` branch, the script now does:
  - `cd "$JS_SDK_PATH"`
  - `npm install`
  - `npm run build`
  - `cd "$SCRIPT_DIR"`
- The stated goal is to make the local Flatmachines SDK build step work reliably before the script points the example project at the local package via:
  - `npm pkg set dependencies.@memgrafter/flatmachines="file:../../../js/packages/flatmachines"`
- The change is small and narrowly scoped: only one insertion, no other files modified.
- The patch metadata shows:
  - Commit `d64e9655cc0b15a43e4fb34a9b69894352be976b`
  - Author: AJ `<yspdev@gmail.com>`
  - Date: Sat, 28 Mar 2026 21:35:19 -0700
- Practical implication: anyone using the local JS runner for `coding_machine_cli` should now avoid build failures caused by missing installed packages in the SDK directory.

### Assessment
Durability is **medium** because this is a version-specific build-script fix tied to the repository’s JS setup and local runner workflow; it may become stale if the build process or package manager workflow changes. Content type is **tutorial/reference** in the sense that it documents a concrete script adjustment rather than arguing a point. Density is **high** for its size: it includes the exact file path, command insertion, and the local-install flow. Originality is **primary source** because this is the actual patch diff from the pull request, not a summary or commentary. Reference style is **refer-back** since it’s most useful when checking why a local build step was changed or diagnosing similar runner issues. Scrape quality is **good** for the patch itself, but limited to the diff excerpt; no surrounding discussion, review comments, or full file contents beyond the changed hunk are included.
