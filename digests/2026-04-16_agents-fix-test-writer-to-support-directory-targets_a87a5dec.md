---
url: https://github.com/robbintt/skills-flatagents/agents/pull/1?session_id=8ee314e9-4aa0-43e3-bb68-2381d276b73b
title: Agents · Fix test_writer to support directory targets
scraped_at: '2026-04-16T03:57:06Z'
word_count: 1975
raw_file: raw/2026-04-16_agents-fix-test-writer-to-support-directory-targets_a87a5dec.txt
tldr: This pull request extends `test_writer` so it can generate and run coverage-based tests for either a single Python file or an entire source directory, with new tests for directory handling, test-file discovery, and `__pycache__` exclusion.
key_quote: Add directory support to test_writer
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- robbintt
- Copilot
tools: []
libraries: []
companies:
- GitHub
tags:
- test-automation
- code-coverage
- python-testing
- github-pull-request
- filesystem
---

### TL;DR
This pull request extends `test_writer` so it can generate and run coverage-based tests for either a single Python file or an entire source directory, with new tests for directory handling, test-file discovery, and `__pycache__` exclusion.

### Key Quote
"Add directory support to test_writer"

### Summary
- **What changed**
  - The PR updates `test_writer` to support **directory targets** in addition to single-file targets.
  - It adds a new test module: `tests/test_hooks.py`.

- **Core code changes in `test_writer/src/test_writer/hooks.py`**
  - Adds new context fields in `test_writer/machine.yml`:
    - `source_dir`
    - `is_directory`
  - In `_init_coverage`:
    - Detects whether `target_file` is a directory with `target.is_dir()`.
    - If directory mode:
      - Recursively collects all `*.py` files with `rglob("*.py")`
      - Excludes:
        - files starting with `test_`
        - files ending with `_test.py`
        - anything under `__pycache__`
      - Concatenates source from all discovered files into `ctx["source_code"]`, adding file markers like `# === relative/path.py ===`
      - Stores `ctx["source_dir"] = str(target)`
      - Uses a project-level test file path derived from the directory name: `tests/test_<dir_name>.py`
    - If file mode:
      - Keeps the old behavior:
        - reads the single file into `ctx["source_code"]`
        - sets `source_dir` to the file’s parent directory
        - looks for an existing test file via `find_test_file`
        - otherwise generates a new test filename
  - Coverage handling changes:
    - For directories, baseline and updated coverage come from the report’s **overall totals** (`totals["percent_covered"]`)
    - Missing lines are aggregated across all files in the report
    - For single files, the existing `get_file_coverage(...)` logic is preserved
  - `_write_and_run_tests` now calls `run_tests(..., source_dir=ctx["source_dir"])` instead of deriving the directory from `target_file`
  - `_check_coverage` is similarly updated to use `ctx["source_dir"]` and directory-wide totals when in directory mode

- **Tests added in `tests/test_hooks.py`**
  - Verifies `_init_coverage` with a single file:
    - source is loaded correctly
    - `source_dir` is set to the parent directory
    - coverage and missing lines are captured as expected
  - Verifies `_init_coverage` with a directory:
    - multiple Python files are combined into `source_code`
    - total coverage is used
    - uncovered lines are aggregated
  - Verifies directory filtering:
    - excludes `test_*.py`
    - excludes `*_test.py`
    - excludes files under `__pycache__`
  - Verifies error handling:
    - raises `FileNotFoundError` when a directory contains no Python files
    - raises `FileNotFoundError` when the target file doesn’t exist
  - Verifies `_check_coverage` works in both:
    - directory mode
    - single-file mode
  - Verifies `_write_and_run_tests` uses `ctx["source_dir"]` when invoking `run_tests`

- **Review/follow-up change in patch 3**
  - Improves `__pycache__` filtering:
    - changes the exclusion check from ` "__pycache__" not in str(f)` to ` "__pycache__" not in f.parts`
  - Makes directory-mode test file naming more specific:
    - from fixed `tests/test_project.py`
    - to `tests/test_<dir_name>.py`
    - with fallback `project` when directory name is `"."`
  - Adds a dedicated test confirming `__pycache__` content is excluded

### Assessment
This is a **mixed** PR that is mostly a **tutorial/reference-level code change** with accompanying tests. Durability is **medium**: the idea of supporting directory targets is broadly useful, but the implementation is tied to the current `test_writer` architecture and coverage-report schema, so it may age with the project. Content density is **high**, since the diff contains concrete control-flow changes, file paths, exclusion rules, and test cases. Originality is **primary source**, because this is the actual patch and test suite rather than a summary of others’ work. It is best used as a **refer-back** reference if you need to understand how directory support was added, how test discovery works, or how coverage is aggregated. Scrape quality is **good** overall: the patch content and tests are present, including the follow-up review fix, though it is still only the diff and not the full surrounding repository context.
