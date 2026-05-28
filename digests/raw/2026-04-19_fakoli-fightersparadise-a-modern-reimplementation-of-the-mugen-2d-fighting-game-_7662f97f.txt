<p align="center">
  <img src="assets/banner.png" alt="Fighters Paradise Banner" width="100%">
</p>

# Fighters Paradise

<p align="center">
  A modern reimplementation of the <a href="https://en.wikipedia.org/wiki/Mugen_(game_engine)">MUGEN</a> 2D fighting game engine in Rust, with full backward compatibility for existing MUGEN content (.sff, .air, .cns, .cmd, .def, .snd files).
</p>

<p align="center">
  <strong>Status: Early Development (v0.1.0)</strong> — Sprites render, animations play, characters walk and jump. Core engine systems are still in progress.
</p>

## Demo

```bash
# Playable character (walk, jump, crouch with keyboard)
cargo run -p fp-app -- kfm.sff kfm.air

# With command input recognition
cargo run -p fp-app -- kfm.sff kfm.air kfm.cmd

# Static sprite viewer
cargo run -p fp-app -- kfm.sff

# Test pattern (no files needed)
cargo run -p fp-app
```

**Controls:**
| Input | Keys |
|-------|------|
| Move | W/A/S/D or Arrow keys |
| Punch (A/B/C) | U / I / O |
| Kick (X/Y/Z) | J / K / L |
| Start | Enter |
| Quit | Escape |

## Building

### Prerequisites

- **Rust** (edition 2021) — [install via rustup](https://rustup.rs/)
- **SDL2** — required for windowing and input
  - macOS: `brew install sdl2`
  - Ubuntu/Debian: `apt install libsdl2-dev`
  - Windows: download from [libsdl.org](https://www.libsdl.org/download-2.0.php)

### Build & Run

```bash
cargo build --workspace          # Build everything
cargo run -p fp-app              # Run with test pattern
cargo test --workspace           # Run all tests (131 tests)
cargo clippy --workspace         # Lint (must pass with zero warnings)
```

## Architecture

Cargo workspace with 14 crates under `crates/`:

```
fp-app (binary)
  ├── fp-engine         (game loop, round flow)
  │     ├── fp-character  (character struct, state machine)
  │     │     ├── fp-vm       (bytecode VM for expressions)
  │     │     ├── fp-combat   (HitDef, damage, guard)
  │     │     ├── fp-physics  (gravity, friction, AABB)
  │     │     └── fp-input    (command recognition)
  │     ├── fp-stage      (backgrounds, camera)
  │     ├── fp-ui         (lifebars, menus, motif)
  │     └── fp-audio      (SFX, BGM)
  ├── fp-render         (wgpu sprite renderer)
  ├── fp-formats        (all file parsers)
  └── fp-core           (shared types, math, errors)
```

### Design Principles

- **Fixed 60Hz timestep** — MUGEN runs at exactly 60 ticks/second for fighting game determinism
- **GPU palette lookup** — 256-color indexed sprites with shader-based palette swap (no texture re-upload)
- **Never crash on bad content** — parsers substitute safe defaults for malformed community content
- **Struct-based entities** — MUGEN entities have fixed properties; bytecode VM needs direct field access

## Development Progress

### Completed

| Phase | Milestone | What Works |
|-------|-----------|------------|
| 1 | Draw a Sprite | SFF v2 parser, wgpu renderer, SDL2 window, palette shader |
| 2 | Animate a Character | AIR parser, animation controller, frame timing, blend modes, collision boxes |
| 3 | Move a Character | Input buffering, CMD parser, physics (gravity/walking/jumping), hardcoded state machine |

### Crate Status

| Crate | Status | Tests | Purpose |
|-------|--------|-------|---------|
| `fp-core` | Done | 15 | Shared types (Vec2, Rect, SpriteId, FpError) |
| `fp-formats` | Partial | 59 | File parsers — SFF v2, AIR, DEF, CMD done; CNS, SND, FNT pending |
| `fp-render` | Done | 22 | wgpu sprite renderer with palette lookup shader |
| `fp-input` | Done | 18 | Input buffering (60-frame ring buffer) + command matching |
| `fp-physics` | Partial | 8 | Euler integration + ground plane; AABB collision pending |
| `fp-app` | Done | 9 | SDL2 window, 60Hz game loop, playable character |
| `fp-vm` | Stub | — | Bytecode compiler + stack VM for expressions |
| `fp-combat` | Stub | — | HitDef, damage, juggle, guard |
| `fp-character` | Stub | — | Character struct + CNS-driven state machine |
| `fp-stage` | Stub | — | Stage loading, backgrounds, camera |
| `fp-audio` | Stub | — | Sound mixer, BGM, SFX |
| `fp-ui` | Stub | — | Lifebars, menus, select screen |
| `fp-storyboard` | Stub | — | Cutscene system |
| `fp-engine` | Stub | — | Game coordinator + round flow |

### Roadmap

| Phase | Milestone | Key Crates |
|-------|-----------|------------|
| 4 | Evaluate Expressions | `fp-vm` + CNS parser in `fp-formats` |
| 5 | Data-Driven States | `fp-character` — replace hardcoded state machine with CNS |
| 6 | Hit Things | `fp-combat` — hitboxes, damage, juggle, guard |
| 7 | Stage & Camera | `fp-stage` — backgrounds, parallax, camera tracking |
| 8 | Sound | `fp-audio` + SND parser — SFX and BGM playback |
| 9 | UI & Menus | `fp-ui` + FNT parser — lifebars, select screen, menus |
| 10 | Full Rounds | `fp-engine` — round flow, win conditions, 2-player |
| 11 | Storyboard | `fp-storyboard` — cutscenes and intros |

## MUGEN Compatibility

Fighters Paradise aims to load and run existing MUGEN characters and stages. Supported file formats:

| Format | Extension | Type | Parser Status |
|--------|-----------|------|---------------|
| SFF v2 | .sff | Binary | Done (RLE5, RLE8, LZ5 compression) |
| AIR | .air | Text | Done (frames, collision boxes, blend modes) |
| CMD | .cmd | Text | Done (command sequences, timing) |
| DEF | .def | Text | Done (INI-style configuration) |
| CNS | .cns | Text | Planned (Phase 4) |
| SND | .snd | Binary | Planned (Phase 8) |
| FNT | .fnt | Binary | Planned (Phase 9) |

## Project Structure

```
FightersParadise/
├── crates/
│   ├── fp-core/          # Shared types, math, error handling
│   ├── fp-formats/       # All MUGEN file format parsers
│   │   └── src/
│   │       ├── sff/      # SFF v2 sprite container parser
│   │       ├── air.rs    # AIR animation file parser
│   │       ├── cmd.rs    # CMD command file parser
│   │       └── def.rs    # DEF configuration file parser
│   ├── fp-render/        # wgpu rendering pipeline
│   │   └── src/shaders/  # WGSL palette lookup shader
│   ├── fp-input/         # Input system
│   │   └── src/
│   │       ├── state.rs  # Button/Direction/InputState types
│   │       ├── buffer.rs # 60-frame ring buffer
│   │       └── command.rs # Command matching engine
│   ├── fp-physics/       # Physics simulation
│   ├── fp-app/           # Application binary (entry point)
│   └── ...               # Stub crates for future phases
├── docs/
│   ├── architecture.md   # Architecture overview
│   └── format-specs/     # MUGEN format specifications
│       └── sff-v2.md     # SFF v2 format spec
└── Cargo.toml            # Workspace root
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

Fighters Paradise is an independent project. MUGEN is a trademark of Elecbyte. This project does not include any Elecbyte code or assets.
