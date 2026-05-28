---
url: https://github.com/TheTom/llama-cpp-turboquant/pull/45#issuecomment-4188305136
title: 'feat: TQ4_1S weight compression (Metal only, needs CUDA port) by TheTom · Pull Request #45 · TheTom/llama-cpp-turboquant'
scraped_at: '2026-04-19T07:29:52Z'
word_count: 2090
raw_file: raw/2026-04-19_feat-tq4-1s-weight-compression-metal-only-needs-cuda-port-by-thetom-pull-request_fef6cdeb.txt
tldr: 'PR #45 adds TQ3_1S and TQ4_1S weight compression for TurboQuant using WHT rotation + Lloyd-Max centroids, initially Metal-only, with later CUDA and HIP/ROCm ports, and shows substantial size reductions while preserving or improving real-world decode performance on several models.'
key_quote: Compressed GGUFs will **not run correctly** on CUDA/HIP until those backends are ported.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: partial
people:
- TheTom
- signalnine
tools:
- llama-quantize
libraries: []
companies:
- GitHub
- Claude Code
tags:
- quantization
- llm-inference
- gpu-kernels
- metal
- cuda
---

### TL;DR
PR #45 adds TQ3_1S and TQ4_1S weight compression for TurboQuant using WHT rotation + Lloyd-Max centroids, initially Metal-only, with later CUDA and HIP/ROCm ports, and shows substantial size reductions while preserving or improving real-world decode performance on several models.

### Key Quote
“Compressed GGUFs will **not run correctly** on CUDA/HIP until those backends are ported.”

### Summary
- **What the PR is**
  - Feature PR: `feat: TQ4_1S weight compression (Metal only, needs CUDA port)`
  - Introduces **TQ3_1S** (3-bit, 4.0 BPW) and **TQ4_1S** (4-bit, 5.0 BPW) weight quantization.
  - Uses **WHT rotation + Lloyd-Max centroids**.
  - Works as **post-training quantization**:
    - no retraining
    - no calibration data
    - no model modification required

- **Implementation details**
  - V2.1 fused **Metal** kernel:
    - zero threadgroup memory
    - cooperative SIMD rotation via `simd_shuffle_xor`
    - `NR0=8`
  - Quantization command:
    - `llama-quantize --allow-requantize --tensor-type-file config.txt`
  - Runtime dequant kernels are **Metal-specific** at the time of the original PR.
  - The quantization tool itself works on any platform, but compressed GGUF runtime support required backend ports for CUDA/HIP.

- **Model results reported in the PR body**
  - Qwen2.5-1.5B: `-27%` size reduction, `+1.9%` PPL delta, `96%` decode, `6/6` NIAH
  - Qwen3.5-27B: `-28%`, `+1.3%`, `99%`, `3/3`
  - Qwen3.5-35B MoE: `-37%`, `+1.4%`, `102%`, no NIAH
  - Qwen2.5-72B: `-38%`, `+3.9%`, `95%`, `3/3`
  - Phi-4 14B: `-36%`, `+1.0%`, `254%`, `3/3`
  - Llama 3.1 70B Premium: `-29%`, `+5.8%`, `fast`, `3/3`
  - Llama 3.1 70B Hybrid: `-42%`, `+16%`, `133%`, `3/3`

- **Important Llama-family caveat**
  - The author says Llama-family models show **6–8x higher per-layer error amplification** when WHT-rotated FFN tensors are used.
  - Recommendation:
    - **Hybrid**: TQ4 attention + Q4_K FFN
    - **Premium**: TQ4 attention + Q5_K/Q6_K FFN
  - Claim: both beat `Q4_K_M` in quality and speed at similar size.
  - Full investigation linked in the paper.

- **Merge blockers / TODOs**
  - CUDA port of V2.1 kernel
  - HIP/ROCm testing
  - Regression tests for existing TurboQuant KV functionality
  - Community validation on untested model families

- **Regression and compatibility work**
  - Multiple follow-up comments report regression testing on Apple Silicon:
    - no breaking changes to existing TurboQuant KV cache functionality
    - no slowdown for standard quant types
    - `q8_0`, `q4_0`, `Q2_K` changes were within measurement noise
  - The PR also includes a fix for an upstream conflict:
    - upstream added activation rotation for KV cache quantization
    - it caused crashes on Phi-4 due to graph hash table overflow
    - the fork disables upstream rotation by default via `LLAMA_ATTN_ROT_DISABLE=0` to re-enable

- **CUDA port status and performance**
  - `signalnine` reports a CUDA port on branch `feature/tq4-weight-cuda`
  - CUDA implementation includes:
    - dequant for TQ4_1S/TQ3_1S
    - fused `mul_mat_vec` kernel with pre-rotated activations via `__shfl_xor_sync`
    - `mmvq` exclusion for fused dispatch
    - `llama-quantize` registration for the new types
  - Benchmark on RTX 5090 for Qwen2.5-7B TQ4_1S:
    - cuBLAS path: `20 t/s`
    - fused kernel: `69 t/s`
    - PPL matches at `8.82`
  - TheTom suggests further CUDA optimizations:
    - NR0 multi-row CTA with shared activation reuse
    - hot-loop load deduplication
    - `__restrict__` qualifiers and vectorized loads

- **Further kernel iteration**
  - Later change (`aa7c82a`) replaces a two-phase global-memory approach with a **single-phase shared-memory kernel**
  - All 8 warps cooperatively WHT-rotate activations into shared memory, then each warp processes a row from shared memory
  - Goal: remove global scratch buffer, avoid extra kernel launch, and avoid CUDA graph incompatibility
  - The author notes Pascal (1080 Ti) remains memory-bandwidth-bound around ~20 t/s

- **Community benchmark on CUDA**
  - On 2x RTX 4090 with Qwen3.5-27B:
    - Q8_0 baseline: `29.23 t/s`
    - Config I: `20.63 t/s` (`70.6%` of Q8_0)
    - Config I + KV turbo4: `20.51 t/s`
  - Model size dropped by `28%`
  - Prefill ran at `80.6%` of Q8_0
  - This benchmark used the V12 shared-memory kernel

- **HIP/ROCm support**
  - AMD HIP/ROCm support added in commit `03b11e9`
  - No kernel changes required for the port
  - Changes include CUDA→HIP stream-capture mappings, visibility macros, and Windows/POSIX compatibility fixes
  - Benchmarked on RX 9070 XT (RDNA 4):
    - Qwen2.5-1.5B-Instruct Config I: `135 t/s` TG128 vs `104 t/s` for Q8_0
    - Reported as **30% faster** than Q8_0, with `27%` smaller model
    - PPL increased slightly from `11.119` to `11.316`

### Assessment
This is a **mixed technical/announcement thread** with unusually high density: it combines the original PR description, regression-test updates, performance engineering notes, CUDA/HIP port status, and benchmark results across multiple hardware platforms. **Durability is medium** because the concepts and kernel strategies are useful beyond this specific PR, but many details are tied to a particular codebase state, branch names, commits, and backend support status. The content is highly **specific and evidence-heavy**, making it good for reference if you want to track TurboQuant’s TQ4_1S/TQ3_1S evolution, but some parts are version-sensitive and may be stale if the repository has moved on. **Originality is mixed**: the PR body is primary source, while much of the thread is iterative engineering commentary and community validation. Best used as a **refer-back** or **deep-study** reference if you care about quantization kernels, backend portability, or the performance tradeoffs of WHT-rotated weight compression. Scrape quality is **good but partial**: it captures the core PR body and many comment highlights, but some tables are truncated and at least one benchmark section is cut off mid-row.
