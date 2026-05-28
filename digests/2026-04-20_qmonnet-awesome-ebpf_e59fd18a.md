---
url: https://github.com/qmonnet/awesome-ebpf
title: qmonnet/awesome-ebpf
scraped_at: '2026-04-20T04:26:20Z'
word_count: 5459
raw_file: raw/2026-04-20_qmonnet-awesome-ebpf_e59fd18a.txt
tldr: qmonnet/awesome-ebpf is a curated, continuously maintained resource list of eBPF documentation, tutorials, tooling, projects, kernel code references, and community links covering networking, tracing, observability, security, and related ecosystems.
key_quote: A curated list of awesome projects related to eBPF.
durability: high
content_type: mixed
density: high
originality: synthesis
reference_style: deep-study
scrape_quality: good
people:
- Quentin Monnet
- Daniel Borkmann
- David Miller
- Toke Høiland-Jørgensen
- Jesper Dangaard Brouer
- Adrian Ratiu
- Brendan Gregg
- Thomas Graf
- John Fastabend
tools:
- bcc
- bpftool
- iproute2
- libbpf
- bpftrace
- clang
- llvm
- tc
- XDP
- Cilium
- Falco
- Tracee
- Pixie
- Hubble
libraries:
- cilium/ebpf
- libbpfgo
- aya
- redbpf
- uBPF
- rbpf
companies:
- Cilium
- Cloudflare
- Facebook
- Netronome
- Suricata
- Apache
- Sysinternals
tags:
- ebpf
- linux-kernel
- network-programming
- observability
- security
---

### TL;DR
`qmonnet/awesome-ebpf` is a curated, continuously maintained resource list of eBPF documentation, tutorials, tooling, projects, kernel code references, and community links covering networking, tracing, observability, security, and related ecosystems.

### Key Quote
> “A curated list of awesome projects related to eBPF.”

### Summary
- This repository is an **“awesome list”** for eBPF: a structured index of high-quality resources rather than original technical content.
- It opens with a short explanation of **BPF/eBPF history and purpose**:
  - classic BPF (cBPF) originated as an in-kernel packet filter used by tools like `tcpdump`
  - eBPF is the modern Linux evolution with safety checks, JIT compilation, maps, helper functions, and broader use cases
  - common uses mentioned include **XDP**, **tracing/monitoring**, and **cgroup-based access control**
- It explicitly points readers to **ebpf.io** and says the ecosystem changes quickly, inviting feedback to keep the list current.

- The list is organized into major sections:
  - **Reference Documentation**
  - **Articles and Presentations**
  - **Tutorials**
  - **Examples**
  - **Workflow tools and utilities**
  - **Projects related to eBPF**
  - **Security**
  - **The code**
  - **Development and community**
  - **Other lists of resources**
- Under each section it links to canonical resources and briefly describes what each covers.

- Major resource categories:
  - **Reference docs**
    - `ebpf.io`, `docs.ebpf.io`, Cilium’s BPF/XDP guide, kernel docs, man pages like `bpf(2)` and `bpf-helpers(7)`, RFC 9669, and kernel-version feature references
  - **Articles/presentations**
    - introductions to eBPF, tracing, BPF internals, XDP, BTF, cBPF, hardware offload, and application examples
  - **Tutorials**
    - bcc tutorials, libbpf-bootstrap, XDP hands-on tutorials, libbpf-based examples, and newer step-by-step community guides
  - **Examples**
    - kernel samples, selftests, bcc examples/tools, and sample repositories for networking and tracing programs
  - **Workflow/tools**
    - `bcc`, `iproute2`, LLVM/clang, `libbpf`, `bpftool`, user-space eBPF runtimes, and language bindings for Go, Rust, Zig, and wasm-based tooling
  - **Projects**
    - networking projects like **Cilium**, **Katran**, **Calico**, **merbridge**, **Suricata** integrations, and observability/security tools like **Pixie**, **Hubble**, **Falco**, **Tracee**, **Tetragon**, and others
  - **Security**
    - offensive and defensive eBPF material, rootkit discussions, detection tools, and BPF LSM-based security agents
  - **Code / kernel internals**
    - pointers to the key kernel source files for BPF implementation, verifier, JITs, tracing, networking hooks, seccomp, and XDP attach paths
  - **Development/community**
    - bpf-next, netdev, xdp-newbies, contribution docs, and XDP project coordination
  - **Other lists**
    - links to additional curated reading lists and docs collections

- The content is broad but not deeply explanatory itself:
  - it is mainly a **navigation hub**
  - each entry is annotated enough to tell you whether the link is about **intro material, internals, tooling, hands-on tutorials, or production projects**
- It also includes a **security-focused section** warning by implication that eBPF can be abused as well as used defensively, with examples of offensive BPF/rootkit research.

### Assessment
This is a **high-durability reference** list: the broad concepts and canonical documentation links will stay useful for a long time, though some project links and version-specific notes can age quickly. It is primarily a **reference** and **mixed factual catalog**, not a tutorial or opinion piece. The density is **high** because it packs a large number of specific links, projects, and kernel references into a single page, though most items are concise annotations rather than substantive explanations. Originality is mostly **synthesis/curation** rather than primary research: its value comes from organizing the ecosystem into a single map. Best used as **deep-study / refer-back** material when you need to find the right doc, tutorial, project, or code path. Scrape quality looks **good**: the page structure, section headings, and most entries appear captured, including the contribution/license notes, though linked media and external content obviously aren’t embedded.
