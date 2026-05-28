---
url: https://github.com/lujiaxuan0520/Test-Time-Tool-Evol/blob/main/src/tool_library.py
title: Test-Time-Tool-Evol/src/tool_library.py at main · lujiaxuan0520/Test-Time-Tool-Evol
scraped_at: '2026-04-19T06:42:25Z'
word_count: 315
raw_file: raw/2026-04-19_test-time-tool-evol-src-tool-library-py-at-main-lujiaxuan0520-test-time-tool-evo_8a01d8a1.txt
tldr: A small Python `ToolLibrary` class that stores `AtomicTool` objects, persists them to JSON, optionally builds SentenceTransformer embeddings for tool descriptions, and evicts the least-used/oldest tool when capacity is exceeded.
key_quote: 'tools_sorted = sorted( self.tools.values(), key=lambda x: (x.hit_count, x.created_at) )'
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- sentence-transformers
- torch
libraries:
- AtomicTool
companies: []
tags:
- python
- data-structures
- persistence
- embeddings
- tooling
---

### TL;DR
A small Python `ToolLibrary` class that stores `AtomicTool` objects, persists them to JSON, optionally builds SentenceTransformer embeddings for tool descriptions, and evicts the least-used/oldest tool when capacity is exceeded.

### Key Quote
"tools_sorted = sorted(\n            self.tools.values(),\n            key=lambda x: (x.hit_count, x.created_at)\n        )"

### Summary
- **Purpose:** Manages a collection of `AtomicTool` instances in memory, with optional persistence and semantic-search support.
- **Core state:**
  - `self.tools: Dict[str, AtomicTool]` stores tools by name.
  - `self.max_size` limits library size.
  - `self.save_path` points to a JSON file for persistence.
  - `self.embedder` is an optional SentenceTransformer-like model.
  - `self.tool_names`, `self.tool_descriptions`, `self.tool_embs` cache metadata and embeddings.
- **Initialization (`__init__`):**
  - Loads existing tools from `save_path` if present.
  - If an embedder is provided, immediately computes embeddings.
- **Description building (`_build_descriptions`):**
  - Creates per-tool text by combining `tool.description` with input parameters.
  - If `input_params` is a dict, formats them as `key: value`; otherwise converts them to string.
- **Embedding update (`_update_embeddings`):**
  - Skips if there is no embedder or no tools.
  - Chooses `cuda` if available, otherwise `cpu`.
  - Moves the embedder to the device, encodes descriptions with:
    - `normalize_embeddings=True`
    - `batch_size=8`
    - `show_progress_bar=False`
  - Moves the model back to CPU afterward and clears CUDA cache if needed.
- **Adding tools (`add_tool`):**
  - If the library is full and the tool is new, it evicts one tool first.
  - The new tool is inserted/overwritten by name.
  - Saves the updated library to disk.
  - Recomputes embeddings if an embedder exists.
- **Lookup (`get_tool`):**
  - Returns a tool by name or `None` if absent.
- **Embedding access (`get_embeddings`):**
  - Returns a tuple of `(tool_names, tool_descriptions, tool_embs)`.
- **Eviction policy (`_evict_lowest_hit_tool`):**
  - Sorts by `(hit_count, created_at)` and removes the “lowest” tool.
  - This means lowest usage is prioritized for removal; ties go to the older/earlier-created entry depending on `created_at` ordering.
  - Logs a removal message with name, hits, and creation time.
- **Persistence (`_save_to_file`):**
  - Writes the tool dictionary as JSON using each tool’s `to_dict()`.
  - Creates parent directories if needed.
  - Uses `ensure_ascii=False` and pretty indentation.
- **Loading (`_load_from_file`):**
  - Reads JSON from `save_path` if it exists.
  - Reconstructs tools with `AtomicTool.from_dict(...)`.
  - Catches exceptions and logs a load failure.

### Assessment
This is a **mixed** utility/reference file with a strong **tutorial-like** implementation flavor, and it is relatively **high-durability** because the patterns it uses—JSON persistence, capacity-based eviction, and optional embedding generation—are broadly reusable. The content is **dense** and fairly specific, with concrete method names and implementation details, but it is **primary source** code rather than commentary. It’s best used as a **refer-back** reference when you need to remember how this library stores, loads, evicts, and embeds tools. Scrape quality is **good**: the full Python file appears captured, including imports, class methods, and comments, though there are no surrounding docs or related files to provide context.
