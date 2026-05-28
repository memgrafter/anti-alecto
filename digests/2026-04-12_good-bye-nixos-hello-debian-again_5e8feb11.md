---
url: https://karl-voit.at/2025/08/30/end-of-my-nixos/
title: Good bye NixOS, Hello Debian (Again)!
scraped_at: '2026-04-12T07:20:33Z'
word_count: 3158
raw_file: raw/2026-04-12_good-bye-nixos-hello-debian-again_5e8feb11.txt
tldr: Karl Voit explains why he is abandoning NixOS after years of trying it on three hosts, citing severe Python workflow pain, configuration complexity, flaky documentation, moving-target tooling, and a final boot-loop incident, and says he has switched back to Debian 13 Trixie with GNOME 48.
key_quote: To start with Nix was one of my worst IT ideas so far.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Karl Voit
- Joshua Blais
tools:
- NixOS
- Nix
- NixShell
- Home Manager
- Xfce
- GNOME
- Debian 13 Trixie
- fwupdmgr
- grub
- AppImages
- Nautilus
libraries:
- NumPy
companies: []
tags:
- linux-distributions
- system-administration
- desktop-environments
- python-workflows
- configuration-management
---

### TL;DR
Karl Voit explains why he is abandoning NixOS after years of trying it on three hosts, citing severe Python workflow pain, configuration complexity, flaky documentation, moving-target tooling, and a final boot-loop incident, and says he has switched back to Debian 13 Trixie with GNOME 48.

### Key Quote
"To start with Nix was one of my worst IT ideas so far."

### Summary
- This is a personal post dated **2025-08-30** (updated **2025-08-31**) about leaving **NixOS** and reinstalling the last machine with **Debian 13 Trixie**.
- The author says his original hopes for NixOS were:
  - one setup for multiple hosts
  - fewer or no GUI settings
  - one configuration “until the end of my life”
  - easier setup on new hardware
  - up-to-date packages
- He lists NixOS’s advertised features as of 2025-08-30:
  - declarative configuration
  - atomic upgrades
  - rollbacks
  - reproducible system configurations
  - source-based model with binary cache
  - consistency
  - multi-user package management
  - flakes
  - nix-shell

- His main complaints:
  - **Too steep a learning curve**: he says you need to become a “Nix wizard” to maintain a system well, and this is not a weekend project.
  - **Getting help is hard to integrate**: advice from the Nix community often could not be plugged cleanly into his own setup.
  - **No clear standard structure**: he says there is no golden pattern for organizing Nix files, and many public configs are hard to adapt.
  - **Python was a major blocker**:
    - simple Python 3 scripts became difficult to run in the “usual way”
    - NixShell setups broke after Python package upgrades
    - even simple shell wrappers became 50+ line scripts
    - he says NixOS and Python were effectively a “no go” for his use case
  - **Desktop configuration friction**:
    - he used **Xfce**
    - many settings could only be changed indirectly via `xfconf.settings`
    - the mapping from settings to variables was tedious and often unclear
    - some settings appeared ineffective
    - syntax varied unpredictably (`True/False`, `0/1`, `-1/1`, etc.)
  - **Moving-target problem**:
    - Nix flakes were still marked **experimental** in **2025-08**
    - newer recommendations often conflicted with older/outdated approaches
    - some settings worked only at the NixOS system level and not in Home Manager
  - **Documentation problems**:
    - much of the documentation felt outdated or half-outdated
    - he says non-experts cannot rely on what they find
  - **Simple tasks felt hard**:
    - even basic host-specific config like `if $HOSTNAME==foobar then ...` was not straightforward
    - he found the indirection frustrating and time-consuming

- Other issues he lists:
  - base system used **over 30 GB** even after garbage collection, versus around **10 GB** on Debian
  - package availability sometimes forced difficult workarounds
  - unclear which packages were precompiled versus built locally
  - updates could take up to **2.5 hours** on a **Lenovo x260**, and still **5–15 minutes** on a **Lenovo T490**
  - rebuilds could fail if one source had issues
  - dependence on **GitHub/cloud sources** felt risky
  - he could not run **AppImages**
  - brightness control required entering the **root password**
  - his installer setup used the CPU rather than hardware acceleration for **LUKS passphrase verification**, causing a ~10-second boot delay
  - he mentions “personal drama” in the NixOS project

- Why he says NixOS’s “advantages” did not matter to him:
  - he did not care much about rollbacks, reproducibility, multi-user package management, or consistency in his own use case
  - he found **flakes** still experimental and **nix-shell** fragile for his needs
  - he felt NixOS solved problems he did not have and reintroduced old problems

- The final trigger for leaving:
  - a **fwupdmgr** firmware update for **intel ME** caused a **boot loop**
  - the machine could only boot into BIOS; other boot entries were broken
  - Nix rollbacks were useless because boot information itself was broken
  - he says a normal Linux rescue workflow with USB, mounting LVM/LUKS/ext partitions, chroot, and rebuilding initramfs/grub might have worked, but not easily on NixOS
  - he copied his data and moved on to **Debian 13**

- His new setup:
  - **Debian 13 Trixie**
  - **GNOME 48**
  - **Wayland**
  - he switched from a long-time **Xfce/XOrg** setup
  - reasons: curiosity, fresh perspective, and trying a major desktop environment
  - current remaining tasks:
    - OS-level text snippets
    - integrating shell tools into Nautilus
    - fixing inconsistent “focus follows mouse”
    - spellcheck integration
  - impressions:
    - GNOME is slower than Xfce
    - animation disabling helps somewhat
    - GNOME Shell’s thumbnail rendering is a performance annoyance
    - GNOME has better convenience features and a strong extensions ecosystem
    - GNOME is more visually appealing
    - he can see himself staying with it for now

- The post ends with related links/backlinks and reactions, including:
  - a Mastodon thread
  - a YouTube video criticizing NixOS
  - notes that the author had already voiced complaints in earlier Mastodon discussion
  - a comparison to another person who found a way to run Python scripts successfully on NixOS

### Assessment
This is a **mixed** but primarily **opinion/personal experience** post with a strong anti-NixOS stance, written as a reflective migration report rather than a neutral technical guide. **Durability: medium** — the broader lessons about complexity, documentation drift, and workflow friction are lasting, but many specifics are tied to NixOS, its ecosystem state in **2025-08**, and the author’s own setup. **Density: high** — it packs in many concrete complaints, version/date references, and examples such as Python/NixShell breakage, `xfconf.settings`, `fwupdmgr`, and boot-loop recovery. **Originality: primary source** — this is the author’s direct account and evaluation of his own migration. **Reference style: refer-back** — useful if you want a firsthand case study of why an experienced Linux user abandoned NixOS. **Scrape quality: good** — the main article content and major sections are present, though the “Related Articles, Reactions, Backlinks” area looks partially list-like and may omit full linked context, code, or embedded media.
