---
url: https://github.com/NVIDIA/ncx-infra-controller-core
title: 'NVIDIA/ncx-infra-controller-core: NCX Infra Controller - Hardware Lifecycle Management and multitenant networking'
scraped_at: '2026-04-19T08:04:23Z'
word_count: 171
raw_file: raw/2026-04-19_nvidia-ncx-infra-controller-core-ncx-infra-controller-hardware-lifecycle-managem_964b891f.txt
tldr: NVIDIA’s NCX Infra Controller (NICo) is an experimental API-based microservice for zero-touch bare-metal lifecycle management with DPU-enforced isolation, aimed at secure, site-local infrastructure automation for AI cloud deployments.
key_quote: “NCX Infra Controller (NICo) delivers zero-touch lifecycle automation for bare-metal systems that secures datacenter infrastructure at its foundation.”
durability: medium
content_type: mixed
density: low
originality: primary
reference_style: skim-once
scrape_quality: good
people: []
tools:
- DevSpace
libraries: []
companies:
- NVIDIA
tags:
- bare-metal-management
- infrastructure-automation
- multitenant-networking
- zero-trust
- ai-infrastructure
---

### TL;DR
NVIDIA’s NCX Infra Controller (NICo) is an experimental API-based microservice for zero-touch bare-metal lifecycle management with DPU-enforced isolation, aimed at secure, site-local infrastructure automation for AI cloud deployments.

### Key Quote
“NCX Infra Controller (NICo) delivers zero-touch lifecycle automation for bare-metal systems that secures datacenter infrastructure at its foundation.”

### Summary
- **What it is**
  - NCX Infra Controller (NICo) is an **API-based microservice** for **site-local, zero-trust, bare-metal lifecycle management**.
  - It emphasizes **DPU-enforced isolation** as part of securing infrastructure.
  - NVIDIA positions it as a way to **automate bare-metal lifecycle complexity** to help build **next-generation AI Cloud offerings**.

- **Primary purpose**
  - Automate bare-metal infrastructure operations with **zero-touch lifecycle automation**.
  - Provide a foundation for **secure datacenter infrastructure**.
  - Support **multitenant networking** and hardware lifecycle management as part of the project’s broader scope.

- **Getting started / where to look**
  - The README points to the **NCX Infra Controller overview** for architecture and capabilities.
  - It points to a **Site Setup guide** for setting up a site for NICo.
  - It points to a **Building Containers guide** for container build details.
  - It also links to **Local Development with DevSpace** for running NICo locally with mock systems.

- **Status / warning**
  - The project is explicitly labeled **experimental** and a **preview release**.
  - NVIDIA warns it is provided **“as is”** with **no warranties**.
  - Features, APIs, and configurations may change **without notice**, so production use requires careful testing in non-critical environments first.

### Assessment
This is a **mixed** reference/announcement-style repository README with a strong product pitch and onboarding pointers rather than deep technical documentation. Its **durability is medium-low** because it’s tied to a specific experimental NVIDIA project and preview release state, which may evolve quickly. The **density is low to medium**: it gives a concise high-level description and links out to more detailed docs, but does not include implementation details, APIs, or examples here. It appears to be **primary source** material from NVIDIA, so it’s authoritative for the project’s intended purpose and status. Best used **skim-once** to identify whether the project is relevant, with **refer-back** value mainly for the linked setup and overview docs. **Scrape quality is good** for the provided content: the core README text and links are present, though the linked documentation content itself is not included.
