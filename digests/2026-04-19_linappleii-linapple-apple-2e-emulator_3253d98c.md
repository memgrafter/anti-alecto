---
url: https://github.com/linappleii/linapple
title: 'linappleii/linapple: Apple 2e emulator'
scraped_at: '2026-04-19T06:56:26Z'
word_count: 1166
raw_file: raw/2026-04-19_linappleii-linapple-apple-2e-emulator_3253d98c.txt
tldr: LinApple is an Apple ][/+/e emulator whose README doubles as a practical operator’s guide, covering startup flags, keyboard shortcuts, disk/snapshot handling, video drivers, and config-file search order.
key_quote: LinApple is an emulator for Apple ][, Apple ][+, Apple //e, and Enhanced Apple //e computers.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- maxolasersquad
tools:
- LinApple
libraries: []
companies:
- AppleWin
- SourceForge
tags:
- emulator
- apple-ii
- command-line
- configuration
- retro-computing
---

### TL;DR
LinApple is an Apple ][/+/e emulator whose README doubles as a practical operator’s guide, covering startup flags, keyboard shortcuts, disk/snapshot handling, video drivers, and config-file search order.

### Key Quote
“LinApple is an emulator for Apple ][, Apple ][+, Apple //e, and Enhanced Apple //e computers.”

### Summary
- **What it is**
  - LinApple is an emulator for Apple ][, Apple ][+, Apple //e, and Enhanced Apple //e.
  - It began as a Linux port of AppleWin, was uploaded from SourceForge to GitHub by `maxolasersquad`, and later moved to the `linappleii` namespace where development continues.

- **Command-line options**
  - `-h|--help`: print options and exit.
  - `--conf path/to/file.conf`: use only the specified config file; skips normal config search.
  - `-1|--d1 path/to/image1.dsk`: load disk image into FDD1 drive 0.
  - `-2|--d2 path/to/image2.dsk`: load disk image into FDD1 drive 1.
  - `-b|--autoboot`: boot automatically instead of showing the splash screen.
  - `-f`: fullscreen mode.
  - `-l`: log output to `AppleWin.log` (untested).
  - `--benchmark`: load benchmark (untested).
  - Example given: `linapple --d1 example.dsk -f --autoboot`.
  - Note: some command-line options have not been fully tested.

- **Using the emulator**
  - Clicking in the window captures the mouse; any function key releases it.
  - Important keys and actions:
    - `F1`: help screen
    - `Ctrl+F2`: cold reboot
    - `Shift+F2`: reload configuration file and cold reboot
    - `Ctrl+F10`: hot reset
    - `F12`: quit
    - `F3` / `F4`: load disk images into slot 6 drives 1/2
    - `F5`: swap slot 6 drives
    - `Alt+F3` / `Alt+F4`: load slot 6 disk images from FTP server
    - `Shift+F3` / `Shift+F4`: attach hard disk images to slot 7 drives 1/2
    - `Alt+Shift+F3` / `Alt+Shift+F4`: attach slot 7 hard disk image from FTP server
    - `Ctrl+F3` / `Ctrl+F4`: eject slot 6 disk images
    - `Ctrl+Shift+F3` / `Ctrl+Shift+F4`: eject slot 7 hard disk images
    - `F6`: toggle fullscreen
    - `Shift+F6`: toggle character set / keyboard-video ROM rocker switch for Apple IIe and enhanced models
    - `F7`: debugger
    - `F8`: save screenshot as bitmap
    - `Shift+F8`: save runtime config changes back to config file
    - `F9`: cycle video modes
    - `Shift+F9`: “Budget video” for smoother music/audio
    - `F10`: load snapshot file
    - `F11`: save snapshot file
    - `Ctrl+0-9`: load snapshot `n`
    - `Ctrl+Shift+0-9`: save snapshot `n`
    - `Pause`: pause/resume emulation
    - `Scroll Lock`: toggle full-speed emulation
    - `Numpad +`: increase emulation speed
    - `Numpad -`: decrease emulation speed
    - `Numpad *`: reset emulation speed
    - `RtCtrl+Numpad`: adjust pdl trim X/Y (`4,6` for X; `2,8` for Y)
  - Warning: fullscreen does not properly exit in multi-monitor setups because of an SDL 1.2 bug.
  - First-run guidance: press `F3` to select a disk image; if needed, use `Ctrl+F2` to restart with the disk inserted.

- **Video drivers**
  - The README lists driver support and caveats:
    - `x11`: all resolutions; debugger panel may glitch or core dump; keyboard OK.
    - `fbcon`: up to `1280x720` on Raspberry Pi; debugger panel OK; keyboard OK.
    - `dispmanx`: works at `1920x1080` 16:9, `1280x720` 16:9, `800x600` 4:3, and `640x480` 4:3; debugger panel OK; keyboard OK.
    - `kmsdrm`: all resolutions, but debugger panel = none and keyboard = none.
  - Warning: debugger panel only works in fullscreen.

- **Apple II command refresher**
  - `CATALOG`: list disk files and file types (`A` Applesoft BASIC, `B` binary, `I` Integer BASIC, `T` text).
  - `RUN file`: run an Applesoft or Integer BASIC file.
  - `BRUN file`: run a binary file, though not all binaries will work.
  - `EXEC file`: execute commands from a text file as if typed.
  - `LOAD file`: load BASIC file into memory.
  - `LIST`: list the current program.
  - References are provided for DOS 3.3 and ProDOS 8 manuals.

- **Configuration system**
  - LinApple uses INI files; `linapple.conf.sample` documents all options.
  - Load order:
    1. Program defaults
    2. If `--conf` is used, that file only
    3. Otherwise system-wide config from `$XDG_CONFIG_DIRS`  
       - typically `/etc/xdg/linapple/linapple.conf`
    4. Then user config from `$XDG_CONFIG_HOME`  
       - typically `~/.config/linapple/linapple.conf`
  - Environment variables:
    - `XDG_CONFIG_HOME`: user-specific config base directory; defaults to `$HOME/.config`
    - `XDG_CONFIG_DIRS`: system preference-ordered config directories; defaults to `/etc/xdg`
  - The README notes partial conformity with the XDG Base Directory Specification.

### Assessment
This is a **reference/tutorial** README with moderate-to-high technical density: it is practical, command-heavy, and optimized for users already trying to run the emulator rather than for conceptual explanation. **Durability is medium** because the core emulator workflow is stable, but details like SDL 1.2 fullscreen behavior, driver support, and “untested” flags are version- and platform-sensitive. **Content type** is mixed, with reference sections dominating and a small amount of historical context. **Originality** is mostly primary-source documentation for the project, not synthesis or commentary. **Reference style** is strongly **refer-back**: it’s the kind of page you’d revisit for keybindings, launch flags, config lookup order, or driver caveats. **Scrape quality** is good: the README text appears intact and includes the main tables and sections needed for later lookup.
