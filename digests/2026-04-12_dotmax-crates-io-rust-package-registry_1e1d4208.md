---
url: https://crates.io/crates/dotmax
title: 'dotmax - crates.io: Rust Package Registry'
scraped_at: '2026-04-12T06:50:57Z'
word_count: 536
raw_file: raw/2026-04-12_dotmax-crates-io-rust-package-registry_1e1d4208.txt
tldr: '`dotmax` is a Rust crate (v0.1) for rendering images, GIFs/APNGs, video, webcam, and custom drawings as terminal braille with a one-line API, optional feature flags (`image`/`svg`/`video`), and interactive tuners for render quality.'
key_quote: Render anything in terminal braille. Images, GIFs, videos, webcam - one line of code.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- cargo
- ffmpeg
- crates.io
libraries:
- dotmax
companies: []
tags:
- rust
- terminal-graphics
- braille-rendering
- cli-tools
- multimedia
---

### TL;DR
`dotmax` is a Rust crate (v0.1) for rendering images, GIFs/APNGs, video, webcam, and custom drawings as terminal braille with a one-line API, optional feature flags (`image`/`svg`/`video`), and interactive tuners for render quality.

### Key Quote
"Render anything in terminal braille. Images, GIFs, videos, webcam - one line of code."

### Summary
- **What it is**
  - Crate: **`dotmax`** on crates.io.
  - Purpose: render visual media and graphics in terminal using **braille grids**.
  - License: **MIT OR Apache-2.0**.

- **Install / feature gating**
  - Example install: `cargo add dotmax --features image`
  - Feature flags:
    - `image`: PNG, JPG, GIF, APNG, BMP, WebP, TIFF
    - `svg`: SVG rendering
    - `video`: video + webcam (**requires FFmpeg**)
  - Cargo examples:
    - `dotmax = { version = "0.1", features = ["image"] }`
    - `dotmax = { version = "0.1", features = ["image", "svg"] }`
    - `dotmax = { version = "0.1", features = ["video"] }`

- **Quick API (high-level)**
  - `quick::show_file("photo.png")?` (auto-detects format)
  - `quick::show_image("photo.jpg")?` (static only)
  - `quick::show_webcam()?`, `quick::show_webcam_device(0)?`, `quick::show_webcam_device("/dev/video1")?`
  - `quick::load_image(...)` returns a `BrailleGrid`
  - `quick::show(&grid)?`, `quick::grid()?` for manual flows

- **Drawing + animation APIs**
  - Primitive drawing (from `dotmax::prelude::*`):
    - `draw_line`, `draw_circle`, `draw_rectangle`, then `show(&grid)?`
  - `AnimationLoop::new(width, height)`
    - configurable FPS (`.fps(30)`)
    - per-frame callback (`.on_frame(...)`) with `Ok(true)` to continue / `false` to stop
    - `.run()?` executes loop

- **Examples provided**
  - Basic: `hello_braille`, `bouncing_ball`, `shapes_demo`
  - Image: `load_image`, `dither_comparison`
  - Animated: `animated_gif`, `animated_apng`
  - Video: `video_player` (`--features video`)
  - Webcam: `webcam_viewer`, `webcam_tuner` (`--features video`)

- **Tuners (interactive render tuning)**
  - Purpose: visually tune dithering/threshold/brightness/contrast/gamma/color mode, then reuse chosen settings in code.
  - Commands:
    - Webcam tuner: `cargo run --example webcam_tuner --features video`
    - Video/Image tuner: `render_tuner` with `--features video|image`
  - Controls include:
    - `D` dithering mode (Floyd/Bayer/Atkinson/None)
    - `T` auto/manual threshold, `+/-`, `[/]` threshold adjustments
    - `B/b`, `C/c`, `G/g` for brightness/contrast/gamma
    - `M` mono/color, `R` reset, `H` help, `Q` quit
  - Notes:
    - Auto threshold uses **Otsu**
    - Threshold range stated as **0–255**

- **Performance claims**
  - Frame render (80×24): **~2μs**
  - Image load + render: **~10ms**
  - 60fps budget: **16.6ms**, with claim “we use **1.6μs**”

### Assessment
This is primarily **reference + tutorial-style** package-page content with concrete commands and API snippets. **Durability: medium** — core usage patterns and concepts (feature flags, quick API, drawing/animation model) should remain useful, but details like version (`0.1`), available examples, and performance numbers may age quickly. **Density: high** for a registry page: it includes install flags, API calls, command examples, tuner keybindings, and performance stats in compact form. **Originality: primary source** (author-maintained crate description/docs excerpt), not commentary. **Reference style: refer-back** — useful as a quick cheatsheet for setup, functions, and example commands. **Scrape quality: good** — appears complete with code blocks, feature table content, controls, and performance/license sections; no obvious missing critical sections.
