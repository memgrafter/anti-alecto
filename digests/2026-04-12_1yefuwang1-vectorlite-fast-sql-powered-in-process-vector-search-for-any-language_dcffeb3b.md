---
url: https://github.com/1yefuwang1/vectorlite
title: '1yefuwang1/vectorlite: Fast, SQL powered, in-process vector search for any language with an SQLite driver'
scraped_at: '2026-04-12T07:30:23Z'
word_count: 5258
raw_file: raw/2026-04-12_1yefuwang1-vectorlite-fast-sql-powered-in-process-vector-search-for-any-language_dcffeb3b.txt
tldr: Vectorlite is a beta SQLite extension that adds fast, in-process approximate vector search via HNSW, with SQL APIs, Python/npm packaging, and benchmarks showing big speedups over brute-force SQLite vector search at the cost of recall and some limitations.
key_quote: “Vectorlite is a [Runtime-loadable extension](https://www.sqlite.org/loadext.html) for SQLite that enables fast vector search based on [hnswlib](https://github.com/nmslib/hnswlib) and works on Windows, MacOS and Linux.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Yefu Wang
tools:
- SQLite
- hnswlib
- apsw
- npm
- CMake
- Ninja
- highway
libraries:
- vectorlite
- vectorlite-py
companies: []
tags:
- vector-search
- sqlite-extension
- approximate-nearest-neighbors
- benchmarking
- python-packaging
---

### TL;DR
Vectorlite is a beta SQLite extension that adds fast, in-process approximate vector search via HNSW, with SQL APIs, Python/npm packaging, and benchmarks showing big speedups over brute-force SQLite vector search at the cost of recall and some limitations.

### Key Quote
“Vectorlite is a [Runtime-loadable extension](https://www.sqlite.org/loadext.html) for SQLite that enables fast vector search based on [hnswlib](https://github.com/nmslib/hnswlib) and works on Windows, MacOS and Linux.”

### Summary
- **What it is**
  - A runtime-loadable SQLite extension for vector search.
  - Uses **hnswlib** for approximate nearest neighbors (ANN).
  - Cross-platform: **Windows-x64, Linux-x64, MacOS-x64, MacOS-arm64**.
  - Distributed as **Python wheels** and **npm packages**.
  - Intended to work with **any language that has a SQLite driver**.

- **Core SQL API**
  - Utility functions:
    - `vectorlite_info()` — prints version/build info and chosen SIMD target.
    - `vector_from_json(json_string)` — JSON array TEXT → float32 vector BLOB.
    - `vector_to_json(vector_blob)` — vector BLOB → JSON array TEXT.
    - `vector_distance(vector_blob1, vector_blob2, distance_type_str)` — computes `l2`, `cosine`, or `ip`.
  - Virtual table usage:
    - Create a vector index with:
      - vector column name
      - dimension
      - distance type
      - HNSW parameters
      - optional index file path for persistence
    - Example pattern:
      - `create virtual table my_table using vectorlite(my_embedding float32[3], hnsw(max_elements=100));`
  - Querying:
    - `knn_param(vector_blob, k, ef)` configures query vector, neighbor count, and optional HNSW `ef`.
    - `knn_search(vector_name, knn_parameter)` is used in the `WHERE` clause.
    - Example:
      - `select rowid, distance from my_table where knn_search(my_embedding, knn_param(vector_from_json('[3,4,5]'), 2));`
  - Metadata filtering:
    - Supports `rowid in (...)` pushdown with `knn_search()` when SQLite is **>= 3.38**.
    - The README emphasizes this as “metadata filter” support.

- **Installation / quick start**
  - Python:
    - `pip install vectorlite-py apsw numpy`
  - Node.js:
    - `npm i vectorlite`
  - For other languages, extract the platform-specific extension binary from the wheel archive.
  - Python quick-start example uses:
    - `apsw.Connection(':memory:')`
    - `conn.enable_load_extension(True)`
    - `conn.load_extension(vectorlite_py.vectorlite_path())`
  - The example creates a virtual table, inserts `float32` numpy vectors, converts vectors to JSON, and runs KNN queries.

- **Highlights claimed by the author**
  - Faster ANN search than **sqlite-vec** and **sqlite-vss**.
  - SIMD-accelerated distance computation using Google’s **highway** library.
  - On the author’s CPU (i5-12600KF with AVX2), distance implementation is claimed to be **1.5x–3x faster than hnswlib** for dimensions >= 256.
  - Supports hnswlib distance types: **l2**, **cosine**, **ip**.
  - Full control over HNSW parameters.
  - Supports saving/loading indexes and loading existing hnswlib index files.
  - Supports JSON serialization/deserialization of vectors.

- **Benchmark section**
  - Benchmarks compare:
    - vectorlite ANN
    - vectorlite brute force via `vector_distance`
    - **hnswlib**
    - **sqlite-vss**
    - **sqlite-vec**
  - Dataset sizes: **3000** and **20000** vectors.
  - Dimensions tested: **128, 512, 1536, 3000**.
  - Benchmarks use randomly generated vectors and 10-NN queries.
  - Main reported results:
    - vectorlite ANN is **much faster** than sqlite-vec, especially as dataset size grows.
    - vectorlite ANN is roughly **on par with hnswlib** for recall and often query speed, but insertion is slower because of SQLite overhead.
    - brute-force via `vector_distance` is 100% accurate but slower for search.
    - sqlite-vss is much slower on inserts and not benchmarked at 20000 vectors because index creation took too long.
  - The README includes large raw benchmark tables with exact insert/search times and recall rates.

- **Important caveats / limitations**
  - Project is explicitly **beta** and may have breaking changes.
  - Only **float32** vectors are supported.
  - **No transactions** supported.
  - The vector index is held **in memory**.
  - Deletion marks vectors deleted but does not free memory.
  - Only **one vector column** per table.
  - `rowid` must be explicitly provided on insert; auto-generated rowid is discouraged / not meaningful here.
  - `rowid` range is constrained by hnsw label type.
  - Metadata filter needs **SQLite >= 3.38**.
  - Some query combinations with multiple `rowid` or multiple `knn_search` constraints are not supported, though `or` combinations can work.
  - A roadmap notes planned support for:
    - user-defined metadata/rowid filter
    - multi-vector document search and epsilon search
    - multithreaded search
    - more package managers
    - more vector types like `float16` and `int8`

- **Build / contributing**
  - Prerequisites:
    - CMake >= 3.22
    - Ninja
    - C++17 compiler
    - Python 3
  - Build extension:
    - clone with submodules
    - run `bootstrap_vcpkg.py`
    - install dev requirements
    - use `build.sh` or `build_release.sh`
  - Build wheel:
    - `python3 -m build -w`

### Assessment
This is a **mixed** content type: mostly **reference/docs** with tutorial-style quick start, plus a substantial benchmark/report section and some roadmap/limitations. Durability is **medium** because the concepts (SQLite extension, HNSW, vector search) are durable, but the package status, benchmarks, platform support, and beta caveats are version-dependent and could age quickly. Density is **high** because it includes specific SQL syntax, installation commands, supported features, benchmark numbers, and limitations. It is **primary source** documentation from the project itself, so it’s useful for evaluating the author’s claims but should be treated as promotional and benchmark-selected rather than neutral. Reference style is **refer-back** if you plan to use the API, install it, or compare it against sqlite-vec/sqlite-vss; otherwise it can be skimmed once for capability and tradeoffs. Scrape quality is **good** overall: the main README content, examples, limitations, roadmap, and benchmark tables are present, though rendered images and the linked external motivation article aren’t embedded here.
