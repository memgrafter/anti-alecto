---
url: https://github.com/memgrafter/flatmachines/blob/main/sdk/examples/iterated_prisoners_dilemma_controller/config/match_machine.yml
title: Match Machine
scraped_at: '2026-05-03T04:48:21Z'
word_count: 154
raw_file: raw/2026-05-03_match-machine_f6722bf0.txt
tldr: A FlatMachines YAML config defines the `ipd-match` state machine for an iterated prisoner’s dilemma game, orchestrating two player submachines across rounds, scoring each round, and exporting the full match history and cooperation/defection stats at the end.
key_quote: 'rounds_total: ''{{ input.rounds_total | default(10) }}'''
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- flatmachines
libraries: []
companies:
- FlatMachines
tags:
- state-machine
- iterated-prisoners-dilemma
- yaml-config
- game-theory
- workflow-orchestration
---

### TL;DR
A FlatMachines YAML config defines the `ipd-match` state machine for an iterated prisoner’s dilemma game, orchestrating two player submachines across rounds, scoring each round, and exporting the full match history and cooperation/defection stats at the end.

### Key Quote
"rounds_total: '{{ input.rounds_total | default(10) }}'"

### Summary
- This is a **FlatMachines** configuration file (`spec: flatmachine`, `spec_version: 2.0.0`) titled **“Match Machine”**.
- It defines a match-level machine named **`ipd-match`** for an **iterated prisoner’s dilemma** example.
- The initial **context** tracks:
  - `rounds_total` with a default of **10** unless overridden by input
  - current `round`, `done` flag
  - move histories for both players: `moves_a`, `moves_b`
  - combined `history`
  - `totals` for A and B
  - cooperation/defection counters and rates for both players
  - `last_round`, `last_move_a`, `last_move_b`
- It references two submachines:
  - `player_a: ./player_machine.yml`
  - `player_b: ./player_machine.yml`

#### State flow
- **`start`**
  - Marked as `type: initial`
  - Immediately transitions to **`play_round`**
- **`play_round`**
  - Runs both player machines in parallel/sequence as machine entries:
    - `player_a` gets:
      - `role: Player A`
      - its own history: `context.moves_a`
      - opponent history: `context.moves_b`
      - opponent last move: `context.last_move_b`
    - `player_b` gets:
      - `role: Player B`
      - its own history: `context.moves_b`
      - opponent history: `context.moves_a`
      - opponent last move: `context.last_move_a`
  - Uses `mode: settled`
  - Passes round metadata into the machine:
    - `round: context.round`
    - `rounds_total: context.rounds_total`
  - Captures outputs back into context:
    - `move_a`, `decision_raw_a`
    - `move_b`, `decision_raw_b`
  - Then transitions to **`score_round`**
- **`score_round`**
  - Executes `action: score_round`
  - Uses hooks named **`ipd-match-hooks`**
  - If `context.done == true`, transitions to **`done`**
  - Otherwise loops back to **`play_round`**
- **`done`**
  - Marked `type: final`
  - Outputs the completed match data:
    - `rounds_total`
    - `history`
    - `totals`
    - `moves_a`, `moves_b`
    - `cooperation_count`, `defection_count`
    - `cooperation_rate`, `defection_rate`

#### What this file is for
- It is essentially the **orchestrator** for an iterated prisoner’s dilemma match.
- It does **not** contain the player strategy itself; that lives in `player_machine.yml`.
- It defines:
  - how each round is run
  - what information each player receives
  - where decisions are stored
  - when scoring happens
  - what match statistics are returned at completion

### Assessment
This is a **reference/configuration** file with **high durability** because it describes a reusable machine workflow rather than a transient event. The content type is **reference** with some **tutorial-like structure** for a state machine setup. Density is **medium-high**: it is compact but includes concrete state names, context variables, machine wiring, and output fields. It is a **primary source** for the match machine configuration, not commentary or synthesis. Best used as a **refer-back** item when implementing or debugging the iterated prisoner’s dilemma example. Scrape quality is **good**: the YAML appears complete and readable, with no obvious missing sections or code blocks.
