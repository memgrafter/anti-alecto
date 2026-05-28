---
url: https://github.com/fakoli/FightersParadise
title: 'fakoli/FightersParadise: A modern reimplementation of the MUGEN 2D fighting game engine in Rust'
scraped_at: '2026-04-19T08:22:10Z'
word_count: 1102
raw_file: raw/2026-04-19_fakoli-fightersparadise-a-modern-reimplementation-of-the-mugen-2d-fighting-game-_7662f97f.txt
tldr: Fighters Paradise is an early-stage Rust reimplementation of the MUGEN 2D fighting engine that already renders sprites, plays animations, and supports basic movement while targeting broad compatibility with existing MUGEN asset formats.
key_quote: 'Status: Early Development (v0.1.0) — Sprites render, animations play, characters walk and jump. Core engine systems are still in progress.'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- cargo
- rust
- rustup
- sdl2
- wgpu
libraries: []
companies:
- Elecbyte
tags:
- game-engine
- rust
- fighting-games
- reverse-engineering
- compatibility
---

### TL;DR
Fighters Paradise is an early-stage Rust reimplementation of the MUGEN 2D fighting engine that already renders sprites, plays animations, and supports basic movement while targeting broad compatibility with existing MUGEN asset formats.

### Key Quote
“Status: Early Development (v0.1.0) — Sprites render, animations play, characters walk and jump. Core engine systems are still in progress.”

### Summary
- **What it is**
  - An open-source project called **Fighters Paradise**.
  - Described as a **modern reimplementation of the MUGEN 2D fighting game engine in Rust**.
  - Aims for **full backward compatibility** with common MUGEN files:
    - `.sff`, `.air`, `.cns`, `.cmd`, `.def`, `.snd`

- **Current status**
  - Marked **Early Development (v0.1.0)**.
  - Working now:
    - sprites render
    - animations play
    - characters can walk and jump
  - Many core systems are still incomplete.

- **Demo / usage**
  - Example commands:
    - `cargo run -p fp-app -- kfm.sff kfm.air`
    - `cargo run -p fp-app -- kfm.sff kfm.air kfm.cmd`
    - `cargo run -p fp-app -- kfm.sff`
    - `cargo run -p fp-app`
  - Controls:
    - Move: `W/A/S/D` or arrow keys
    - Punch: `U / I / O`
    - Kick: `J / K / L`
    - Start: `Enter`
    - Quit: `Escape`

- **Build requirements**
  - Needs **Rust 2021** and **SDL2**
  - SDL2 install notes:
    - macOS: `brew install sdl2`
    - Ubuntu/Debian: `apt install libsdl2-dev`
    - Windows: download from libsdl.org
  - Build/test commands:
    - `cargo build --workspace`
    - `cargo run -p fp-app`
    - `cargo test --workspace` (claimed **131 tests**)
    - `cargo clippy --workspace`

- **Architecture**
  - Cargo workspace with **14 crates**.
  - Main layers:
    - `fp-app` for the executable
    - `fp-engine` for game loop and round flow
    - `fp-character` for state machines and character behavior
    - `fp-vm` for expression bytecode VM
    - `fp-combat` for damage/hit handling
    - `fp-physics` for gravity, friction, collision
    - `fp-input` for command recognition
    - `fp-stage` for backgrounds/camera
    - `fp-ui` for lifebars/menus
    - `fp-audio` for SFX/BGM
    - `fp-render` for wgpu rendering
    - `fp-formats` for parsers
    - `fp-core` for shared types and math
  - Several crates are still **stubs**.

- **Design principles**
  - **Fixed 60Hz timestep** for deterministic fighting-game behavior
  - **GPU palette lookup** for indexed sprites without re-uploading textures
  - **Never crash on bad content**; malformed community content should fall back to safe defaults
  - **Struct-based entities** because MUGEN uses fixed properties and direct field access

- **Development progress**
  - Completed phases:
    - **Phase 1:** Draw a Sprite
    - **Phase 2:** Animate a Character
    - **Phase 3:** Move a Character
  - Milestones mention working support for:
    - SFF v2 parser
    - AIR parser
    - CMD parser
    - wgpu renderer
    - SDL2 window
    - palette shader
    - input buffering
    - physics basics
  - Crate status shows:
    - Done: `fp-core`, `fp-render`, `fp-input`, `fp-app`
    - Partial: `fp-formats`, `fp-physics`
    - Stub: `fp-vm`, `fp-combat`, `fp-character`, `fp-stage`, `fp-audio`, `fp-ui`, `fp-storyboard`, `fp-engine`

- **Roadmap**
  - Phase 4: evaluate expressions (`fp-vm` + CNS parser)
  - Phase 5: data-driven states (`fp-character`)
  - Phase 6: combat/hit detection (`fp-combat`)
  - Phase 7: stage & camera
  - Phase 8: sound (`fp-audio` + SND parser)
  - Phase 9: UI & menus (`fp-ui` + FNT parser)
  - Phase 10: full rounds (`fp-engine`)
  - Phase 11: storyboard/cutscenes

- **Compatibility / supported formats**
  - **Done**:
    - SFF v2 (`.sff`) including RLE5, RLE8, LZ5 compression
    - AIR (`.air`)
    - CMD (`.cmd`)
    - DEF (`.def`)
  - **Planned**:
    - CNS (`.cns`)
    - SND (`.snd`)
    - FNT (`.fnt`)

- **Project structure / docs**
  - Repository includes:
    - `crates/` for Rust workspace crates
    - `docs/architecture.md`
    - `docs/format-specs/sff-v2.md`
  - Also notes the repository root Cargo setup and parser submodules.

- **License / attribution**
  - Licensed under **MIT**.
  - States it is **independent** and does **not include Elecbyte code or assets**.
  - Notes MUGEN is a trademark of Elecbyte.

### Assessment
This is a **mixed reference/announcement** document with high utility for evaluating the project’s maturity and architecture. **Durability is medium** because it is tied to a specific early version (**v0.1.0**) and an active roadmap, so details like crate status, test counts, and supported formats may change quickly. **Density is high**: it packs concrete commands, crate breakdowns, supported file formats, and roadmap phases into a fairly structured README. **Originality is primary source**, since it describes the project in its own repository rather than summarizing elsewhere. It’s best used as a **refer-back** reference if you want to assess whether the project is worth tracking, checking compatibility claims, or understanding the codebase layout. **Scrape quality is good** overall: the main README content appears intact, including tables and code blocks, though any linked images, deeper docs, or code samples outside the README are not included here.
