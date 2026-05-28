# CrabCrust

## Project Summary

CrabCrust is a Rust toolkit for adding expressive, terminal-native animation to command-line workflows. It uses braille rendering and lightweight command wrappers to explore how CLI tools can communicate state with more personality and better visual feedback.

## Why This Exists

Most command-line tools tell you what happened after the fact. This project explores a more designed interaction model: what if terminal workflows could signal motion, progress, success, and intent while still staying inside the shell?

CrabCrust treats the terminal as an interface surface, not just a text stream. The work is intentionally experimental, but the goal is practical: clearer feedback, stronger affordances, and more memorable command experiences.

## Key Ideas or Features

- Braille-based graphics for high-density terminal rendering.
- Procedural animations for save, push, pull, download, merge, and celebratory states.
- Command wrappers that map shell actions to themed visual responses.
- Modular rendering and animation layers written in Rust.
- Experimental media conversion pipeline for GIF and video-driven terminal playback.
- Demo mode for testing animations outside wrapped commands.

## How It Works (High Level)

1. A command wrapper intercepts a workflow such as `git push` or `git commit`.
2. The executor runs the underlying command and preserves output plus exit code.
3. The animation engine selects and renders a procedural animation in parallel with the workflow.
4. The braille renderer converts motion into dense terminal graphics with color support.
5. Control returns to the shell with the original command result intact.

## Demo / Screenshots

<video src="https://github.com/newjordan/CrabCrust/raw/main/examples/crabcrust_in_action.mp4" controls></video>

The repository also includes animation examples and experimental DMD/video assets under [`examples/`](examples/) and [`docs/`](docs/).

## Getting Started

### Requirements

- Rust toolchain
- Cargo

### Run Locally

```bash
git clone https://github.com/newjordan/CrabCrust.git
cd CrabCrust
cargo build --release
cargo run -- demo all
```

### Wrap Git Commands

```bash
cargo run -- git commit -m "Prototype CLI feedback"
cargo run -- git push
```

Optional shell alias:

```bash
alias git="crabcrust git"
```

## Future Experiments

- Extend wrappers beyond Git into build, deploy, and agent workflows.
- Add configurable animation mappings for different command outcomes.
- Improve operator cues for failures, warnings, and long-running tasks.
- Explore accessibility and legibility patterns for terminal motion design.
