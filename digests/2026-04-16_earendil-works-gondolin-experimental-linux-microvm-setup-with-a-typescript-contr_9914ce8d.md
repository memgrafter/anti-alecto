---
url: https://github.com/earendil-works/gondolin/tree/main
title: 'earendil-works/gondolin: Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox'
scraped_at: '2026-04-16T03:57:36Z'
word_count: 679
raw_file: raw/2026-04-16_earendil-works-gondolin-experimental-linux-microvm-setup-with-a-typescript-contr_9914ce8d.txt
tldr: Gondolin is an experimental Linux micro-VM sandbox for AI agents that combines QEMU or optional `krun` isolation with host-controlled network, filesystem, and secret access, all programmable through a TypeScript/JavaScript control plane.
key_quote: Local Linux micro-VMs with programmable network and filesystem control.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- QEMU
- krun
- libkrun
- npx
libraries:
- '@earendil-works/gondolin'
companies:
- earendil-works
tags:
- micro-vms
- agent-sandboxing
- linux-security
- qemu
- typecript-javascript
---

### TL;DR
Gondolin is an experimental Linux micro-VM sandbox for AI agents that combines QEMU or optional `krun` isolation with host-controlled network, filesystem, and secret access, all programmable through a TypeScript/JavaScript control plane.

### Key Quote
"Local Linux micro-VMs with programmable network and filesystem control."

### Summary
- **What it is**
  - `earendil-works/gondolin` is an agent sandbox for running generated code in disposable local Linux micro-VMs.
  - It is designed to reduce exfiltration risk when AI agents run code that may need network access and credentials.
  - The host enforces policy over network and filesystem access, and that policy can be customized in JavaScript.

- **Core model**
  - Default VM backend: **QEMU**
  - Optional experimental backend: **`krun` / libkrun**
  - The guest code runs inside the VM, while the host mediates:
    - HTTP/TLS egress
    - secret injection
    - filesystem behavior
    - SSH and ingress options
    - snapshots and resume

- **Quick SDK example**
  - The sample uses:
    - `import { VM, createHttpHooks } from "@earendil-works/gondolin";`
    - `createHttpHooks({ allowedHosts: ["api.github.com"], secrets: {...} })`
    - `VM.create({ httpHooks, env })`
    - `vm.exec(...)` to run a shell command inside the VM
  - The example shows a `curl` request to GitHub’s API using a placeholder token in the guest, while the real `GITHUB_TOKEN` is only injected by the host for allowed destinations.
  - It notes that string commands are executed as `/bin/sh -lc "..."`.

- **CLI quick start**
  - Launch a shell session with:
    - `npx @earendil-works/gondolin bash`
  - Manage sessions with:
    - `npx @earendil-works/gondolin list`
    - `npx @earendil-works/gondolin attach <session-id>`
    - `npx @earendil-works/gondolin snapshot <session-id>`
    - `npx @earendil-works/gondolin bash --resume <snapshot-id-or-path>`

- **Images and runtime assets**
  - Guest assets include kernel/initramfs/rootfs and optional krun boot artifacts.
  - These are about **~200MB+** and are fetched automatically on first use via `builtin-image-registry.json`.
  - Default image when none is specified:
    - `GONDOLIN_DEFAULT_IMAGE`
    - default value: `alpine-base:latest`

- **Requirements**
  - **macOS**:
    - `brew install qemu node`
  - **Linux (Debian/Ubuntu)**:
    - `sudo apt install qemu-system-arm nodejs npm`
  - Optional `krun` runner build:
    - `make krun-runner`

- **`krun` backend notes**
  - Published installs include platform-specific optional runner packages for supported targets.
  - The local runner is staged under `.cache/` rather than globally installed.
  - The helper binary is built at:
    - `host/krun-runner/zig-out/bin/gondolin-krun-runner`
  - On macOS, the build ad-hoc signs the runner with the `com.apple.security.hypervisor` entitlement.
  - When available, Gondolin auto-detects the runner for `--vmm krun`.
  - For Linux krun build prerequisites, the repo lists:
    - `build-essential curl git make pkg-config clang lld xz-utils`
    - `libclang-dev llvm-dev libcap-ng-dev`
    - Rust via `rustup` with a modern toolchain supporting **edition 2024**
    - Zig **0.15.2**
  - Krun mode requires boot assets from the selected image manifest:
    - `assets.krunKernel`
    - optional `assets.krunInitrd`
  - Custom kernels/initrds can be supplied via explicit `sandbox.imagePath` asset objects.

- **Feature highlights**
  - Disposable local micro-VMs for agent tasks
  - Programmable HTTP/TLS egress policy with allowlists and request/response hooks
  - Secret injection without exposing secrets to the guest
  - Programmable VFS mounts via JavaScript
  - Ingress gateway to expose guest HTTP services on the host (`--listen`, `vm.enableIngress()`)
  - Attach to a running VM shell
  - SSH support:
    - host to guest via `vm.enableSsh()`
    - optional guest to upstream allowlisted SSH egress
  - Disk checkpoints/snapshots with resume
  - Custom image builds using an Alpine-based pipeline and optional OCI rootfs source
  - Configurable DNS modes:
    - `synthetic`
    - `trusted`
    - `open`
  - Rootfs modes:
    - `readonly`
    - `memory`
    - `cow`

- **Documentation and repo structure**
  - Main docs:
    - Introduction
    - CLI
    - SDK
    - Secrets Handling
    - SSH
    - Custom Images
    - Architecture Overview
    - VM Backends (QEMU vs krun)
    - Security Design
    - Limitations
  - Repository guides:
    - `host/README.md` for installation, CLI, SDK examples
    - `guest/README.md` for Zig build and image/initramfs pipeline
    - `images/` for canonical image release configs
    - `host/examples` for end-to-end examples

- **Pi extension**
  - There is a `Pi + Gondolin` extension in `host/examples/pi-gondolin.ts`
  - It runs pi tools inside a micro-VM and mounts the project at `/workspace`

- **Other notes**
  - The repo explicitly says it was built with help from coding agents.
  - License: **Apache-2.0**
  - Issue tracker and documentation links are provided.

### Assessment
This is a **mixed** reference/announcement-style repository overview with some tutorial content. Durability is **medium** because the core ideas—micro-VM isolation, secret brokering, policy-controlled egress—are fairly timeless, but the installation instructions, backend support, and version-sensitive build requirements (for example `krun`, Zig 0.15.2, edition2024, and platform-specific packaging) will age. The content is fairly **dense** and specific, especially around CLI commands, backend setup, and security features, and it reads mostly as **primary source** documentation from the project maintainers rather than commentary or synthesis. As a reference, it is best for **skimming and occasional re-checking**, especially when deciding whether the project’s architecture or setup fits a sandboxing use case. Scrape quality is **good**: the main README content appears captured cleanly, including code blocks, requirements, feature lists, and links, though repository-linked subpages and images are not included in full.
