---
url: https://github.com/gainsec/autoprober
title: https://github.com/gainsec/autoprober
scraped_at: '2026-04-19T20:09:53Z'
word_count: 1100
raw_file: raw/2026-04-19_https-github-com-gainsec-autoprober_bd327385.txt
tldr: AutoProber is a source-available hardware-control stack for automating flying-probe-style PCB probing with a CNC, microscope, and oscilloscope, with an explicit safety model centered on continuously monitoring oscilloscope Channel 4 as an independent stop condition.
key_quote: Treat it as a machine-control system, not a normal web app.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Jon 'GainSec' Gaines
tools:
- Flask
- uv
- mjpg_streamer
libraries: []
companies:
- GainSec
tags:
- pcb-testing
- machine-control
- hardware-automation
- safety-engineering
- cnc
---

### TL;DR
AutoProber is a source-available hardware-control stack for automating flying-probe-style PCB probing with a CNC, microscope, and oscilloscope, with an explicit safety model centered on continuously monitoring oscilloscope Channel 4 as an independent stop condition.

### Key Quote
"Treat it as a machine-control system, not a normal web app."

### Summary
- **What it is**
  - A “hardware hacker’s flying probe automation stack” for taking a new target from initial identification to safe probing of individual pins.
  - Includes Python control code, a Flask dashboard, CAD files, docs, and config files needed to build a custom AutoProber.
  - Source-available release candidate under the PolyForm Noncommercial 1.0.0 license.

- **Main workflow**
  - Instruct the agent to ingest the project and confirm all connected hardware is functioning.
  - Run homing and calibration after setup is ready.
  - Attach the custom probe and microscope header.
  - When a new target is placed, the system:
    - finds the target on the plate,
    - captures individual microscope frames while recording XYZ positions,
    - identifies pads, pins, chips, and other features,
    - stitches and annotates the map,
    - adds probe targets to the dashboard for human approval,
    - probes only the approved targets.
  - Hardware can be controlled through the web dashboard, Python scripts, or by the agent itself.

- **Safety model**
  - The project emphasizes that this is machine-control hardware, not a standard web app.
  - Key safety requirements:
    - GRBL `Pn:P` is ignored; the CNC probe pin is **not** trusted as an endstop.
    - An independent safety endstop is read from oscilloscope **Channel 4**.
    - Channel 4 must be monitored continuously during any motion.
    - Any Channel 4 trigger, ambiguous voltage, CNC alarm, or real X/Y/Z limit pin is a stop condition.
    - The agent/operator must stop and report; no automatic recovery motion is performed.
  - Readers are directed to `docs/safety.md` and `docs/operations.md`.

- **Repository layout**
  - `apps/` — operator scripts and Flask dashboard entrypoint
  - `autoprober/` — reusable Python package for CNC, scope, microscope, logging, safety
  - `dashboard/` — single-page web dashboard
  - `docs/` — architecture, device references, operations, safety guidance
  - `cad/` — printable STL files for the custom toolhead
  - `config/` — example environment/config files
  - `AGENTS.md` — agent/operator safety rules
  - `LICENSE` — PolyForm Noncommercial 1.0.0 and commercial contact
  - `pyproject.toml`, `uv.lock` — Python project metadata and locked dependencies

- **Hardware stack**
  - GRBL-compatible 3018-style CNC controller over USB serial
  - USB microscope via `mjpg_streamer`
  - Siglent oscilloscope over LAN/SCPI for:
    - Channel 4 safety monitoring
    - Channel 1 measurement
  - Optical endstop wired to external 5V supply and oscilloscope Channel 4
  - Optional network-controlled outlet for lab power
  - Printable custom toolhead parts in `cad/`

- **Reference parts**
  - The repo lists example parts used in the prototype build:
    - Optical end stop
    - USB microscope
    - SainSmart Genmitsu 3018-PROVer V2
    - Matter Smart Power Strip
    - Siglent SDS1104X-E oscilloscope
    - Dupont wires
    - Pen spring or similar light compression spring
    - 3D printer for toolhead parts
  - Optional parts include universal oscilloscope probes, 5V USB power brick, and a USB 2.0 pigtail cable.
  - It cautions that listings, dimensions, voltage, and connector compatibility should be verified before buying.

- **Architecture**
  - The system architecture shows:
    - Operator → Web Dashboard → Python Apps → CNC / Microscope / Scope / Optional outlet
    - Endstop signal → Scope Channel 4 → Apps
    - Pogo measurement → Scope Channel 1 → Apps
  - Runtime flow:
    - Preflight → verify C4 clear → monitored motion → capture → stitch/map → manual probe review → approved bounded probe motion
  - STOP state:
    - Triggered by C4 events, CNC alarms, or real limit pin events
    - Logs voltage/status/action
    - Waits for explicit operator clearing; no automatic recovery

- **Quick start and configuration**
  - Install dependencies with:
    - `uv sync`
  - Launch dashboard:
    - `PYTHONPATH=. python3 apps/dashboard.py`
  - Dashboard defaults to port `5000`.
  - Configuration begins from `config/autoprober.example.env`.
  - Important environment variables include:
    - `AUTOPROBER_LOG_PATH`
    - `AUTOPROBER_RUNTIME_ROOT`
    - `AUTOPROBER_MICROSCOPE_SNAPSHOT_URL`
    - `AUTOPROBER_SCOPE_HOST`
    - `AUTOPROBER_SCOPE_PORT`
  - It warns not to publish lab-specific IPs, hostnames, credentials, calibration files, or target images.

- **Main workflows**
  - Run preflight checks.
  - Verify Channel 4 is clear.
  - Home and calibrate only when setup is ready.
  - Capture microscope frames with monitored motion.
  - Generate/import target maps for review.
  - Approve probe candidates manually.
  - Execute probe motion only after measuring and storing microscope-to-probe offset.

- **Exclusions and limitations**
  - The release candidate intentionally excludes trial captures, stitched target images, uploads, backups, `.venv`, `__pycache__`, Playwright artifacts, runtime logs, calibration cache, flat-field images, and machine-specific SSH/deploy state.
  - Current limitations:
    - microscope-to-pogo XY offset must be measured before real probing
    - calibration must be generated on the machine that will move
    - dashboard should not be exposed to untrusted networks

- **License and use**
  - Noncommercial use is allowed under PolyForm Noncommercial License 1.0.0.
  - Commercial use requires a separate paid license.
  - It is intended for authorized lab work only, and the repo explicitly warns not to use it to probe, damage, or analyze systems without permission.

### Assessment
This is a **mixed** technical/reference repository with tutorial-like quick-start material and a strong safety/operations emphasis. Durability is **medium**: the core machine-control and safety patterns are broadly useful, but hardware choices, runtime assumptions, and the release-candidate status make parts of it version- and lab-specific. Density is **high** because it packs architecture, workflow, configuration, safety rules, and hardware BOM pointers into a compact README. Originality is a **primary source** snapshot from the project authors, not a synthesis. It’s best used as **refer-back** material if you plan to build or operate the stack, though the README is also sufficient for a skim-once overview. Scrape quality is **good**: the main textual content, architecture diagrams, workflow, licensing, and configuration details are present; the embedded images are referenced but not viewable here, and deeper docs/code are not included in the scrape.
