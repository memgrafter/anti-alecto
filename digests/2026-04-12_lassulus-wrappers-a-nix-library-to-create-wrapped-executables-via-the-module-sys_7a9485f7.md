---
url: https://github.com/Lassulus/wrappers
title: 'Lassulus/wrappers: A Nix library to create wrapped executables via the module system'
scraped_at: '2026-04-12T07:20:55Z'
word_count: 1546
raw_file: raw/2026-04-12_lassulus-wrappers-a-nix-library-to-create-wrapped-executables-via-the-module-sys_7a9485f7.txt
tldr: wrappers is a Nix library for building wrapped executables and reusable wrapper modules, so the same package configuration can be shared across NixOS, home-manager, nix-darwin, devenv, and systemd use cases.
key_quote: A Nix library to create wrapped executables via the module system.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Vimjoyer
- viperML
tools:
- NixOS
- home-manager
- nix-darwin
- devenv
- systemd
- xkcd
libraries:
- nixpkgs
companies: []
tags:
- nix
- modules
- executable-wrapping
- systemd
- configuration-management
---

### TL;DR
`wrappers` is a Nix library for building wrapped executables and reusable wrapper modules, so the same package configuration can be shared across NixOS, home-manager, nix-darwin, devenv, and systemd use cases.

### Key Quote
"A Nix library to create wrapped executables via the module system."

### Summary
- `wrappers` provides two main APIs:
  - `lib.wrapPackage`: low-level wrapper builder for a package executable
  - `lib.wrapModule`: higher-level module-based wrapper definition with typed options
- It also ships `wrapperModules`, a collection of prebuilt wrappers for common apps like:
  - `mpv`
  - `notmuch`
  - and others
- The project’s motivation is to avoid rewriting near-identical modules for multiple platform/module systems:
  - NixOS
  - home-manager
  - nix-darwin
  - devenv
- The README explicitly references [xkcd 927](https://xkcd.com/927/), reinforcing the “yet another config system” pain point
- There is a recommended explanatory video linked from Vimjoyer: “Homeless Dotfiles with Nix Wrappers”

#### `wrapPackage`
- Wraps a package executable with:
  - extra runtime inputs on `PATH`
  - environment variables
  - command-line flags / args
  - pre- and post-hooks
  - passthru attributes
  - aliases
  - file patching/exclusion controls
- Important options include:
  - `package`
  - `exePath`
  - `binName`
  - `runtimeInputs`
  - `env`
  - `flags`
  - `args`
  - `flagSeparator` (`" "` by default, `"="` also supported)
  - `preHook`
  - `postHook`
  - `filesToPatch`
  - `filesToExclude`
  - `patchHook`
- `flags` can be:
  - `true` → flag without value
  - `"string"` → flag with a value
  - `false` / `null` → omitted
- If `args` is provided, it overrides flag auto-generation
- It preserves original outputs like man pages and completions
- It uses `lndir` to maintain directory structure
- It handles multi-output derivations correctly
- Desktop files are patched by default for `Exec=` and `Icon=` references

#### Example: direct package wrapping
- The README shows wrapping `pkgs.curl` with:
  - `jq` as a runtime dependency
  - `CURL_CA_BUNDLE` set to `cacert`
  - `--silent`
  - `--connect-timeout 30`
- It also shows wrapping a specific executable, e.g. `ls` from `coreutils`, and renaming it to `my-ls`

#### `wrapModule`
- `wrapModule` creates reusable wrapper modules that integrate with the Nix module system
- It supports:
  - typed configuration options
  - generated documentation via `options`
  - `apply`, which instantiates/extends the wrapper configuration
- Built-in config fields include:
  - `pkgs`
  - `package`
  - `extraPackages`
  - `flags`
  - `flagSeparator`
  - `args`
  - `env`
  - `preHook`
  - `postHook`
  - `passthru`
  - `filesToPatch`
  - `filesToExclude`
  - `patchHook`
  - read-only `wrapper`
  - read-only `apply`
- Optional modules can be imported from `wlib.modules.<name>`, including:
  - `systemd`
- Custom types include `wlib.types.file`, which supports:
  - `content`
  - derived `path`

#### Module-system integration
- The wrapper system uses `lib.evalModules`
- It supports standard module features like:
  - imports
  - conditionals
  - `mkIf`
- The evaluated config is exposed as `config`
- Module metadata is available in `options`

#### Extending configs
- The `apply` function can extend an existing wrapper configuration with additional modules/settings
- The README demonstrates this with `mpv`:
  - initial config adds `mpris` and an `mpv.conf`
  - extended config adds another script and more config
  - the final wrapped package is accessed via `.wrapper`

#### Example prebuilt modules
- **mpv**
  - supports config files and script management
  - example adds:
    - `mpvScripts.mpris`
    - `mpvScripts.thumbnail`
    - `mpv.conf`
    - `input.conf`
    - `--save-position-on-quit`
- **notmuch**
  - supports INI-style configuration for mail/database settings
  - example sets:
    - `database.path`
    - `database.mail_root`
    - `user.name`
    - `user.primary_email`

#### systemd support
- Importing `wlib.modules.systemd` generates systemd service files for the wrapper
- The systemd options are passed through from NixOS service-style configuration
- `ExecStart`, `Environment`, `PATH`, `preStart`, and `postStop` are derived automatically from the wrapper
- Outputs are available as:
  - `config.outputs.systemd-user`
  - `config.outputs.systemd-system`
- The README shows how to use the generated units in:
  - NixOS user services
  - NixOS system services
  - home-manager via `xdg.dataFile`
- Important note: NixOS does not activate services from `[Install]` sections alone; you still need `wantedBy` so NixOS creates the `.wants` symlink

#### Alternatives and long-term goal
- An alternative project mentioned is `wrapper-manager` by viperML
- The author says that project is more focused on one module system and exporting wrappers, while `wrappers` aims for:
  - more granular per-package modules
  - a community collection of wrapper modules
- Long-term goal:
  - upstream this schema into `nixpkgs`
  - potentially provide an optional `module.nix` for every package
  - enable consistent wrapper configuration across platforms

### Assessment
This is a high-density technical reference for a Nix library, with strong practical examples and fairly durable concepts, though some specifics may evolve with Nixpkgs and module-system conventions. The content type is mixed, but primarily tutorial/reference: it explains both how to use `wrapPackage`/`wrapModule` and what the library is for. Originality is primary source, since it is the project README written by the author, not a third-party commentary. It is best used as a refer-back reference rather than a one-time skim, because it includes API details, option semantics, and platform integration examples. Scrape quality looks good overall: the README structure, code examples, and section content are present, though embedded images/video previews are only linked, not meaningfully captured as content.
