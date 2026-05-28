---
url: https://github.com/clawsouls/soulspec/blob/main/soul-spec-v0.5.md
title: soulspec/soul-spec-v0.5.md at main · clawsouls/soulspec
scraped_at: '2026-04-19T08:03:03Z'
word_count: 2476
raw_file: raw/2026-04-19_soulspec-soul-spec-v0-5-md-at-main-clawsouls-soulspec_389fa0b6.txt
tldr: ClawSouls Package Spec v0.5 defines the JSON manifest and companion files for “soul” packages, adding multi-framework compatibility, tool/skill declarations, lifecycle/deprecation support, progressive disclosure, and new embodied-agent/robotics fields.
key_quote: Token budgets matter. A marketplace listing doesn't need AGENTS.md.
durability: medium
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- TomLee
- RoboticsLab
tools:
- browser
- exec
- web_search
- github
libraries: []
companies:
- ClawSouls
- OpenClaw
- Clawdbot
- ZeroClaw
- Cursor
- Windsurf
- Continue.dev
- ROS2
- NVIDIA Isaac
- Webots
- Gazebo
tags:
- json-manifest
- software-specification
- progressive-disclosure
- robotics
- metadata-schema
---

### TL;DR
ClawSouls Package Spec v0.5 defines the JSON manifest and companion files for “soul” packages, adding multi-framework compatibility, tool/skill declarations, lifecycle/deprecation support, progressive disclosure, and new embodied-agent/robotics fields.

### Key Quote
“**Token budgets matter. A marketplace listing doesn't need AGENTS.md.**”

### Summary
- **What this is**
  - A reference/spec document for `soul.json`, the manifest that describes a ClawSouls persona package.
  - Versioned as **spec v0.5**, with examples and change history back to v0.1.
  - The sample manifest describes a persona called **`senior-devops-engineer`**.

- **Core `soul.json` structure**
  - Required fields include:
    - `specVersion` (`"0.3"`, `"0.4"`, or `"0.5"`)
    - `name`, `displayName`, `version`, `description`
    - `author`
    - `license`
    - `tags`
    - `category`
    - `files.soul`
  - Example manifest includes:
    - `name: "senior-devops-engineer"`
    - `version: "1.0.0"`
    - `license: "Apache-2.0"`
    - `category: "work/devops"`
    - `repository: "https://github.com/clawsouls/souls"`
  - Optional sections add compatibility, tools, skills, file paths, examples, disclosure, deprecation, and repository metadata.

- **Major additions in v0.4 / v0.5**
  - `compatibility.frameworks`: declares which agent frameworks the soul is meant to work with, such as:
    - `openclaw`, `clawdbot`, `zeroclaw`, `cursor`, `windsurf`, `continue`
  - `allowedTools`: declares expected/permitted tools such as:
    - `browser`, `exec`, `web_search`, `github`
  - `recommendedSkills`: replaces legacy `skills: string[]` with structured entries that can include:
    - `name`
    - optional `version`
    - optional `required`
  - `disclosure.summary`: a short one-line summary for quick discovery
  - `deprecated` and `supersededBy`: lifecycle/deprecation support
  - `compatibility.openclaw` is now actually validated by SoulScan + CLI install
  - `compatibility.models` remains advisory rather than enforceable

- **Progressive disclosure model**
  - The spec formalizes 3 levels:
    - **Level 1 — Quick Scan**: `soul.json` only, mainly for discovery and filtering
    - **Level 2 — Full Read**: `SOUL.md` + `IDENTITY.md`
    - **Level 3 — Deep Dive**: `AGENTS.md`, `STYLE.md`, `HEARTBEAT.md`, `examples/`
  - The purpose is to reduce token usage while preserving depth.
  - `disclosure.summary` is the key Level 1 discovery hint.

- **Compatibility and ecosystem**
  - The spec is designed for any SOUL.md-compatible framework, but can explicitly list compatibility.
  - Missing `compatibility.frameworks` implies broad compatibility.
  - `minTokenContext` is mentioned as a new field in the change log and field table, though the sample manifest does not include it.
  - Tool transparency and framework filtering are intended for registry and validation workflows.

- **Deprecation and lifecycle**
  - Deprecated souls can be marked with:
    - `deprecated: true`
    - `supersededBy: "owner/name"`
  - Registry and CLI behavior:
    - show deprecation banners
    - warn on install
    - do not necessarily block use

- **License policy**
  - Only permissive licenses are allowed:
    - `Apache-2.0`, `MIT`, `BSD-2-Clause`, `BSD-3-Clause`, `CC-BY-4.0`, `CC0-1.0`, `ISC`, `Unlicense`
  - Copyleft and restrictive Creative Commons licenses are blocked.

- **Embodied agents / robotics extension**
  - v0.5 adds a substantial section for physical agents such as robots and IoT devices.
  - New optional fields:
    - `environment`: `"virtual"`, `"embodied"`, `"hybrid"`
    - `interactionMode`: `"text"`, `"voice"`, `"multimodal"`, `"gesture"`
    - `hardwareConstraints`
    - `safety.physical`
    - `sensors`
    - `actuators`
  - These fields are informational but intended to help frameworks adapt behavior safely and appropriately.
  - Examples include:
    - voice-first care companion robot
    - sensor schema with lidar, camera, microphone array, IMU, touch sensors
    - actuator schema for locomotion, arm, gripper, head, expression hardware
  - Robotics frameworks explicitly named:
    - `ros2`, `isaac`, `webots`, `gazebo`

- **Safety and validation emphasis**
  - The spec repeatedly frames certain fields as validation targets for **SoulScan**.
  - Security/safety checks include:
    - cross-validating declared tools against actual tool use
    - auditing recommended skills for excessive dependency
    - warning on framework spoofing
    - flagging embodied souls without `safety.physical`
    - requiring justification for `contactPolicy: "full-contact"`

- **Changelog and version history**
  - **v0.5 (2026-02-24)**:
    - embodied-agent fields
    - robotics platform identifiers
    - embodied safety audits
    - academic references
  - **v0.4 (2026-02-20)**:
    - multi-framework support
    - token context hint
    - allowed tools
    - recommended skills
    - disclosure summary
    - deprecation support
    - validation of `compatibility.openclaw`
  - **v0.3 (2026-02-16)**:
    - `specVersion`
    - rename to `soul.json`
    - publish confirmation requirement
    - license allowlist enforcement
  - **v0.2 / v0.1** are marked as internal development specs and not supported for new publications.

### Assessment
This is a **reference** document with high specificity and relatively high density, aimed at people implementing or publishing ClawSouls packages rather than casual readers. Its durability is **medium**: the abstract ideas around manifests, progressive disclosure, compatibility metadata, and safety declarations are fairly stable, but the exact spec versioning, framework names, and dates make it tied to a particular project state in early 2026. The content is a **mixed** technical/specification document: mostly normative docs with some rationale and changelog context. Originality is **primary source** because it defines the spec itself rather than summarizing others, though the robotics references section cites external papers. It is best used as **refer-back** material for authors, validators, or tooling implementers. Scrape quality appears **good** overall: the main sections, tables, examples, and changelog are present, though as a GitHub markdown scrape it may omit repository navigation/context and any rendered assets beyond the inline code blocks.
