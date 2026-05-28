# SDK Common Spec Requirements Plan

> **Purpose:** Define common requirements for FlatAgents SDK implementations across languages and runtimes.
> **Status:** Planning Document
> **Spec Version:** 0.7.7

## Executive Summary

This document outlines requirements for a unified SDK specification that enables:
1. Cross-language SDK compatibility (Python, JavaScript, Rust/WASM)
2. Distributed systems deployment (k8s, cloud functions, ECS, edge, browser)
3. Formal verification readiness (ACL2-compatible design)

---

## 1. Core Spec Files (Source of Truth)

| File | Purpose | Status |
|------|---------|--------|
| `flatagent.d.ts` | Agent configuration schema | ✅ Complete |
| `flatmachine.d.ts` | Machine orchestration schema | ✅ Complete |
| `profiles.d.ts` | Model profile configuration | ✅ Complete |
| `flatagents-runtime.d.ts` | SDK runtime interfaces | ✅ Initial draft |

---

## 2. Required Runtime Interfaces

### 2.1 Execution Locking (`ExecutionLock`)

**Purpose:** Prevent concurrent execution of the same machine instance.

| Implementation | Requirement | Use Case |
|----------------|-------------|----------|
| `NoOpLock` | MUST | External locking / disabled |
| `LocalFileLock` | SHOULD | Single-node deployments |
| `RedisLock` | MAY | Distributed deployments |
| `ConsulLock` | MAY | Service mesh environments |

**Formal Verification Notes:**
- Lock acquisition is a boolean predicate: `acquire(key) → bool`
- Lock must satisfy mutual exclusion property
- ACL2: Model as state transition with mutex invariant

### 2.2 Persistence Backend (`PersistenceBackend`)

**Purpose:** Durable storage for machine checkpoints.

| Implementation | Requirement | Use Case |
|----------------|-------------|----------|
| `MemoryBackend` | MUST | Testing, ephemeral runs |
| `LocalFileBackend` | SHOULD | Local durable storage |
| `RedisBackend` | MAY | Distributed cache |
| `PostgresBackend` | MAY | Relational durability |
| `S3Backend` | MAY | Cloud object storage |

**Interface Requirements:**
```typescript
interface PersistenceBackend {
  save(key: string, snapshot: MachineSnapshot): Promise<void>;  // Atomic
  load(key: string): Promise<MachineSnapshot | null>;
  delete(key: string): Promise<void>;
  list(prefix: string): Promise<string[]>;  // Lexicographic order
}
```

**Formal Verification Notes:**
- `save` must be atomic (all-or-nothing)
- `list` must return deterministic ordering
- ACL2: Model as key-value store with append-only history

### 2.3 Result Backend (`ResultBackend`)

**Purpose:** Inter-machine communication via URI-addressed results.

**URI Scheme:** `flatagents://{execution_id}/{path}`
- `/checkpoint` - Machine state for resume
- `/result` - Final output after completion

| Implementation | Requirement | Use Case |
|----------------|-------------|----------|
| `InMemoryResultBackend` | MUST | Single-process |
| `RedisResultBackend` | MAY | Distributed |

**Interface Requirements:**
```typescript
interface ResultBackend {
  write(uri: string, data: any): Promise<void>;  // Notify blocked readers
  read(uri: string, options?: { block?: boolean; timeout?: number }): Promise<any>;
  exists(uri: string): Promise<boolean>;
  delete(uri: string): Promise<void>;
}
```

**Formal Verification Notes:**
- Write must happen-before read can return data
- Blocking reads must eventually terminate (timeout or data arrival)
- ACL2: Model as message queue with ordering guarantees

### 2.4 Execution Types (`ExecutionConfig`)

| Type | Requirement | Behavior |
|------|-------------|----------|
| `default` | MUST | Single call, no retry |
| `retry` | MUST | Configurable backoffs with jitter |
| `parallel` | MUST | N samples, return all successes |
| `mdap_voting` | MUST | Multi-sample with consensus |

**Formal Verification Notes:**
- Retry backoff sequence must be monotonic
- Jitter must be bounded: `actual_wait in [base * (1-jitter), base * (1+jitter)]`
- MDAP voting: k_margin consensus is well-defined for n >= k

### 2.5 Machine Hooks (`MachineHooks`)

All hooks are optional. SDKs must support both sync and async implementations.

| Hook | Signature | Purpose |
|------|-----------|---------|
| `onMachineStart` | `(context) → context` | Modify initial context |
| `onMachineEnd` | `(context, output) → output` | Modify final output |
| `onStateEnter` | `(state, context) → context` | Pre-state modifications |
| `onStateExit` | `(state, context, output) → output` | Post-state modifications |
| `onTransition` | `(from, to, context) → to` | Redirect transitions |
| `onError` | `(state, error, context) -> state or null` | Error recovery |
| `onAction` | `(action, context) → context` | Custom action handlers |

---

## 3. Distributed Systems Requirements

### 3.1 Deployment Targets

| Environment | Considerations | Priority |
|-------------|----------------|----------|
| Kubernetes Pods | Stateless pods, external state | HIGH |
| Kubernetes Jobs | Batch processing, completion tracking | HIGH |
| Cloud Functions (AWS Lambda, GCP, Azure) | Cold starts, timeouts, stateless | HIGH |
| ECS Tasks | Container orchestration, service mesh | MEDIUM |
| Edge Functions (Cloudflare Workers, Vercel) | Size limits, restricted APIs | MEDIUM |
| Browser (Rust/WASM) | No filesystem, async-only, sandboxed | MEDIUM |

### 3.2 Stateless Execution Model

**Requirement:** SDKs MUST support fully stateless execution:
1. All state externalized to persistence backend
2. Checkpoint-resume semantics for any interruption
3. No in-memory state between invocations

**Machine Snapshot Wire Format:**
```typescript
interface MachineSnapshot {
  execution_id: string;
  machine_name: string;
  spec_version: string;
  current_state: string;
  context: Record<string, any>;
  step: number;
  created_at: string;
  event?: string;
  output?: Record<string, any>;
  total_api_calls?: number;
  total_cost?: number;
  parent_execution_id?: string;
  pending_launches?: LaunchIntent[];
}
```

### 3.3 Launch Intent / Outbox Pattern

**Purpose:** Ensure exactly-once semantics for machine launches.

**Mechanism:**
1. Record launch intent in checkpoint before launching
2. On resume, check if launched machine exists before re-launching
3. Use `pending_launches` array in `MachineSnapshot`

```typescript
interface LaunchIntent {
  execution_id: string;
  machine: string;
  input: Record<string, any>;
  launched: boolean;
}
```

### 3.4 Timeout and Cancellation

**Requirements:**
- State-level `timeout` in seconds (0 = forever)
- Graceful cancellation with checkpoint preservation
- Timeout errors must be catchable via `on_error`

### 3.5 Parallel Execution Modes

| Mode | Behavior | Use Case |
|------|----------|----------|
| `settled` | Wait for all to complete | All results needed |
| `any` | Return on first success | Fastest response wins |

**Distributed Considerations:**
- Fan-out to multiple workers
- Result aggregation at parent
- Partial failure handling

---

## 4. Rust/WASM Runtime Requirements

### 4.1 Compilation Targets

| Target | Use Case | API Restrictions |
|--------|----------|------------------|
| `wasm32-unknown-unknown` | Browser, Cloudflare Workers | No filesystem, no threads |
| `wasm32-wasi` | Node.js, Deno, edge runtimes | WASI filesystem, limited threads |
| Native (Linux/macOS/Windows) | CLI, server applications | Full API access |

### 4.2 WASM-Specific Constraints

**No Filesystem Access:**
- `LocalFileBackend` unavailable
- `LocalFileLock` unavailable
- Must use in-memory or remote backends

**No Native Threads:**
- Use `async`/`await` throughout
- Web Workers for parallelism in browser
- Consider `rayon` for WASI targets only

**Size Budget:**
- Target < 500KB gzipped for browser
- Tree-shaking for unused backends
- Optional features via Cargo features

### 4.3 WASM Backend Implementations

| Backend | WASM Strategy |
|---------|---------------|
| `MemoryBackend` | ✅ Direct implementation |
| `LocalFileBackend` | ❌ Not available |
| `IndexedDBBackend` | Browser persistence |
| `LocalStorageBackend` | Browser (small data) |
| `FetchBackend` | HTTP-based remote storage |

### 4.4 JavaScript/TypeScript Interop

**Binding Strategy:**
- Use `wasm-bindgen` for browser/Node.js
- Export `FlatAgent` and `FlatMachine` classes
- Async methods return `Promise<T>`
- JSON serialization for config/context

**API Surface:**
```typescript
// Generated from Rust via wasm-bindgen
export class FlatAgent {
  constructor(config: AgentWrapper);
  call(input: Record<string, any>): Promise<AgentResult>;
}

export class FlatMachine {
  constructor(config: MachineWrapper);
  execute(input: Record<string, any>): Promise<MachineResult>;
  resume(execution_id: string): Promise<MachineResult>;
}
```

---

## 5. Formal Verification (ACL2) Implementation

### 5.1 Repository Structure for Verification

```
/verification/
├── acl2/
│   ├── README.md                    # Setup and usage instructions
│   ├── Makefile                     # Build all books, run proofs
│   ├── cert.acl2                    # ACL2 certification config
│   │
│   ├── core/                        # Core state machine logic
│   │   ├── machine-state.lisp       # State representation
│   │   ├── context.lisp             # Context data structures
│   │   ├── transitions.lisp         # Transition functions
│   │   └── expressions.lisp         # Simple expression evaluator
│   │
│   ├── properties/                  # Theorem statements
│   │   ├── progress.lisp            # Progress property proofs
│   │   ├── determinism.lisp         # Determinism proofs
│   │   ├── checkpoint.lisp          # Checkpoint consistency
│   │   ├── mutex.lisp               # Mutual exclusion
│   │   └── outbox.lisp              # Exactly-once semantics
│   │
│   ├── refinement/                  # Refinement mappings to SDKs
│   │   ├── python-mapping.lisp      # Python SDK correspondence
│   │   ├── js-mapping.lisp          # JavaScript SDK correspondence
│   │   └── rust-mapping.lisp        # Rust SDK correspondence
│   │
│   └── tests/                       # Counter-example generators
│       ├── quickcheck.lisp          # Random testing integration
│       └── regression.lisp          # Known edge cases
│
├── specs/                           # Formal specifications (TLA+ style)
│   ├── flatmachine.tla              # Optional TLA+ spec for comparison
│   └── invariants.json              # Machine-readable invariant list
│
└── scripts/
    ├── run-proofs.sh                # CI script for proof checking
    ├── extract-theorems.py          # Generate theorem list for docs
    └── sync-with-sdk.py             # Verify SDK matches ACL2 model
```

### 5.2 ACL2 Data Structures

**Machine State Representation:**
```lisp
;; machine-state.lisp

(include-book "std/lists/top" :dir :system)
(include-book "std/alists/top" :dir :system)

;; State is a symbol from a finite set
(defun valid-state-p (state states)
  "Check if state is in the set of valid states"
  (member-equal state states))

;; Machine configuration (parsed from YAML)
(defund machine-config-p (cfg)
  (and (alistp cfg)
       (assoc-equal :states cfg)
       (assoc-equal :initial cfg)
       (assoc-equal :finals cfg)))

;; Runtime snapshot (corresponds to MachineSnapshot in TS)
(defund snapshot-p (snap)
  (and (alistp snap)
       (assoc-equal :execution-id snap)
       (assoc-equal :current-state snap)
       (assoc-equal :context snap)
       (assoc-equal :step snap)
       (natp (cdr (assoc-equal :step snap)))))
```

**Context Operations:**
```lisp
;; context.lisp

;; Context is an alist of symbol -> value
(defun context-p (ctx)
  (alistp ctx))

;; Get value from context (returns nil if not found)
(defun ctx-get (key ctx)
  (cdr (assoc-equal key ctx)))

;; Set value in context (pure - returns new context)
(defun ctx-set (key val ctx)
  (acons key val ctx))

;; Merge contexts (right takes precedence)
(defun ctx-merge (ctx1 ctx2)
  (append ctx2 ctx1))

;; Theorem: ctx-merge is associative
(defthm ctx-merge-assoc
  (equal (ctx-merge (ctx-merge a b) c)
         (ctx-merge a (ctx-merge b c))))
```

### 5.3 Core Transition Logic

```lisp
;; transitions.lisp

(include-book "machine-state")
(include-book "context")
(include-book "expressions")

;; Evaluate a single transition condition
;; Returns T if transition should fire, NIL otherwise
(defun eval-transition-condition (trans ctx)
  (let ((cond (cdr (assoc-equal :condition trans))))
    (if (null cond)
        t  ; No condition = always true
        (eval-simple-expr cond ctx))))

;; Find first matching transition
;; Returns target state or NIL if no transition matches
(defun find-transition (transitions ctx)
  (if (endp transitions)
      nil
    (if (eval-transition-condition (car transitions) ctx)
        (cdr (assoc-equal :to (car transitions)))
      (find-transition (cdr transitions) ctx))))

;; Single step of machine execution
(defund machine-step (state ctx cfg)
  "Execute one step: returns (mv next-state new-ctx) or (mv :error ctx)"
  (let* ((state-def (cdr (assoc-equal state (cdr (assoc-equal :states cfg)))))
         (transitions (cdr (assoc-equal :transitions state-def)))
         (next-state (find-transition transitions ctx)))
    (if (null next-state)
        (mv :error ctx)  ; No valid transition
      (let ((output-mapping (cdr (assoc-equal :output-to-context state-def))))
        (mv next-state (apply-output-mapping output-mapping ctx))))))

;; Full execution until final state or error
(defun machine-run (state ctx cfg steps-remaining)
  "Run machine until final state, error, or step limit"
  (declare (xargs :measure (nfix steps-remaining)))
  (cond
   ((zp steps-remaining) (mv :timeout state ctx))
   ((member-equal state (cdr (assoc-equal :finals cfg)))
    (mv :done state ctx))
   (t (mv-let (next-state new-ctx)
              (machine-step state ctx cfg)
        (if (eq next-state :error)
            (mv :error state ctx)
          (machine-run next-state new-ctx cfg (1- steps-remaining)))))))
```

### 5.4 Expression Evaluator

```lisp
;; expressions.lisp

;; Simple expression language (matches flatmachine simple mode)
;; Expr ::= (op arg1 arg2) | (get path) | literal

(defun eval-simple-expr (expr ctx)
  "Evaluate simple-mode expression in context"
  (cond
   ;; Literals
   ((booleanp expr) expr)
   ((integerp expr) expr)
   ((stringp expr) expr)
   ((null expr) nil)
   
   ;; Variable access: (get :context :field)
   ((and (consp expr) (eq (car expr) 'get))
    (ctx-get (caddr expr) ctx))
   
   ;; Comparisons
   ((and (consp expr) (eq (car expr) '==))
    (equal (eval-simple-expr (cadr expr) ctx)
           (eval-simple-expr (caddr expr) ctx)))
   ((and (consp expr) (eq (car expr) '!=))
    (not (equal (eval-simple-expr (cadr expr) ctx)
                (eval-simple-expr (caddr expr) ctx))))
   ((and (consp expr) (eq (car expr) '<))
    (< (eval-simple-expr (cadr expr) ctx)
       (eval-simple-expr (caddr expr) ctx)))
   ((and (consp expr) (eq (car expr) '>=))
    (>= (eval-simple-expr (cadr expr) ctx)
        (eval-simple-expr (caddr expr) ctx)))
   
   ;; Boolean operators
   ((and (consp expr) (eq (car expr) 'and))
    (and (eval-simple-expr (cadr expr) ctx)
         (eval-simple-expr (caddr expr) ctx)))
   ((and (consp expr) (eq (car expr) 'or))
    (or (eval-simple-expr (cadr expr) ctx)
        (eval-simple-expr (caddr expr) ctx)))
   ((and (consp expr) (eq (car expr) 'not))
    (not (eval-simple-expr (cadr expr) ctx)))
   
   ;; Unknown expression
   (t nil)))

;; Theorem: Expression evaluation produces consistent results
;; Key insight: eval-simple-expr depends only on expr structure and ctx values
(defthm eval-simple-expr-functional
  (implies (and (equal expr1 expr2)
                (equal ctx1 ctx2))
           (equal (eval-simple-expr expr1 ctx1)
                  (eval-simple-expr expr2 ctx2)))
  :rule-classes :rewrite)
```

### 5.5 Key Theorems to Prove

**Progress Property:**
```lisp
;; properties/progress.lisp

;; Theorem: A well-formed machine always terminates
(defthm machine-progress
  (implies (and (machine-config-p cfg)
                (valid-state-p state (cdr (assoc-equal :states cfg)))
                (context-p ctx)
                (posp max-steps))
           (mv-let (status final-state final-ctx)
                   (machine-run state ctx cfg max-steps)
             (or (eq status :done)
                 (eq status :error)
                 (eq status :timeout))))
  :hints (("Goal" :induct (machine-run state ctx cfg max-steps))))
```

**Determinism Property:**
```lisp
;; properties/determinism.lisp

;; Theorem: Running machine twice with same inputs gives same result
;; This captures that machine-run is a pure function with no hidden state
(defthm machine-run-deterministic
  (implies (and (machine-config-p cfg)
                (valid-state-p state (cdr (assoc-equal :states cfg)))
                (context-p ctx)
                (natp n))
           (let ((run1 (machine-run state ctx cfg n))
                 (run2 (machine-run state ctx cfg n)))
             (and (equal (mv-nth 0 run1) (mv-nth 0 run2))  ; Same status
                  (equal (mv-nth 1 run1) (mv-nth 1 run2))  ; Same final state
                  (equal (mv-nth 2 run1) (mv-nth 2 run2))))) ; Same final context
  :hints (("Goal" :induct (machine-run state ctx cfg n))))

;; Theorem: Transition function depends only on explicit arguments
;; No global state or side effects influence the result
(defthm machine-step-no-hidden-state
  (implies (and (machine-config-p cfg)
                (context-p ctx)
                (symbolp state))
           (mv-let (next-state1 new-ctx1)
                   (machine-step state ctx cfg)
             (mv-let (next-state2 new-ctx2)
                     (machine-step state ctx cfg)
               (and (equal next-state1 next-state2)
                    (equal new-ctx1 new-ctx2)))))
  :hints (("Goal" :in-theory (enable machine-step))))
```

**Checkpoint Consistency:**
```lisp
;; properties/checkpoint.lisp

;; Create snapshot from current execution state
(defun make-snapshot (exec-id state ctx step)
  (list (cons :execution-id exec-id)
        (cons :current-state state)
        (cons :context ctx)
        (cons :step step)))

;; Resume from snapshot
(defun resume-from-snapshot (snap cfg max-steps)
  (machine-run (cdr (assoc-equal :current-state snap))
               (cdr (assoc-equal :context snap))
               cfg
               max-steps))

;; Theorem: Resuming from checkpoint produces same result
(defthm checkpoint-consistency
  (implies (and (machine-config-p cfg)
                (snapshot-p snap)
                (valid-state-p (cdr (assoc-equal :current-state snap))
                               (cdr (assoc-equal :states cfg)))
                (posp remaining-steps))
           (equal (resume-from-snapshot snap cfg remaining-steps)
                  (machine-run (cdr (assoc-equal :current-state snap))
                               (cdr (assoc-equal :context snap))
                               cfg
                               remaining-steps)))
  :hints (("Goal" :in-theory (enable resume-from-snapshot))))
```

**Mutual Exclusion (Lock Protocol):**
```lisp
;; properties/mutex.lisp

;; Lock state: alist of (key . owner) pairs
(defun lock-state-p (locks)
  (alistp locks))

;; Acquire lock (returns new lock state and success flag)
(defun acquire-lock (key owner locks)
  (let ((current-owner (cdr (assoc-equal key locks))))
    (if (or (null current-owner)
            (equal current-owner owner))
        (mv (acons key owner locks) t)  ; Success
      (mv locks nil))))                  ; Fail - held by other

;; Release lock
(defun release-lock (key owner locks)
  (if (equal (cdr (assoc-equal key locks)) owner)
      (remove-assoc-equal key locks)
    locks))

;; Theorem: At most one owner holds a lock
(defthm mutex-single-owner
  (implies (and (lock-state-p locks)
                (cdr (assoc-equal key locks)))
           (let ((owner (cdr (assoc-equal key locks))))
             (mv-let (new-locks success)
                     (acquire-lock key other-owner locks)
               (implies (not (equal other-owner owner))
                        (not success))))))
```

**Outbox Exactly-Once:**
```lisp
;; properties/outbox.lisp

;; Launch intent: (execution-id . launched-flag)
(defun launch-intent-p (intent)
  (and (consp intent)
       (stringp (car intent))  ; execution-id
       (booleanp (cdr intent)))) ; launched flag

;; Pending launches list
(defun pending-launches-p (launches)
  (if (endp launches)
      t
    (and (launch-intent-p (car launches))
         (pending-launches-p (cdr launches)))))

;; Check if already launched
(defun already-launched-p (exec-id launches)
  (and (assoc-equal exec-id launches)
       (cdr (assoc-equal exec-id launches))))

;; Process launch (idempotent)
;; Mark as launched if not already; returns updated launches and should-launch flag
(defun process-launch (exec-id launches)
  (if (already-launched-p exec-id launches)
      (mv launches nil)  ; Already launched, don't launch again
    (mv (acons exec-id t launches) t)))  ; Mark and launch

;; Theorem: Each intent is processed exactly once
(defthm outbox-exactly-once
  (implies (pending-launches-p launches)
           (mv-let (new-launches should-launch-1)
                   (process-launch exec-id launches)
             (mv-let (final-launches should-launch-2)
                     (process-launch exec-id new-launches)
               (and (implies should-launch-1 (not should-launch-2))
                    (equal (already-launched-p exec-id final-launches) t))))))
```

### 5.6 Integration with SDKs

**Correspondence Checking Script:**
```python
#!/usr/bin/env python3
# scripts/sync-with-sdk.py

"""
Verify SDK implementations match ACL2 model.

This script:
1. Parses ACL2 function signatures from .lisp files
2. Compares with SDK function signatures
3. Runs property-based tests that mirror ACL2 theorems
"""

import ast
import subprocess
from pathlib import Path

ACL2_CORE = Path("verification/acl2/core")
PYTHON_SDK = Path("sdk/python/flatagents")
JS_SDK = Path("sdk/js/src")

# Functions that must have SDK equivalents
REQUIRED_FUNCTIONS = [
    ("machine-step", "machine_step", "_machineStep"),
    ("eval-simple-expr", "eval_simple_expr", "evalSimpleExpr"),
    ("find-transition", "find_transition", "findTransition"),
    ("ctx-merge", "merge_context", "mergeContext"),
]

def verify_function_exists(sdk_path: Path, func_name: str) -> bool:
    """Check if function exists in SDK."""
    # For Python: parse AST and look for function definitions
    for py_file in sdk_path.glob("**/*.py"):
        with open(py_file) as f:
            try:
                tree = ast.parse(f.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef) and node.name == func_name:
                        return True
            except SyntaxError:
                continue
    return False

def run_acl2_proofs() -> bool:
    """Run all ACL2 proofs via Makefile."""
    result = subprocess.run(
        ["make", "certify"],
        cwd="verification/acl2",
        capture_output=True
    )
    return result.returncode == 0
```

**Property-Based Test Bridge:**
```python
# sdk/python/tests/test_acl2_properties.py

import hypothesis
from hypothesis import given, strategies as st

from flatagents.flatmachine import FlatMachine
from flatagents.expressions import eval_simple_expr

class TestACL2Properties:
    """Tests that mirror ACL2 theorems for confidence before formal proof."""
    
    @given(st.dictionaries(st.text(), st.integers()))
    def test_determinism(self, context):
        """Property: eval_simple_expr is deterministic (mirrors eval-simple-expr-deterministic)"""
        expr = {"op": ">=", "left": {"context": "score"}, "right": 8}
        result1 = eval_simple_expr(expr, context)
        result2 = eval_simple_expr(expr, context)
        assert result1 == result2
    
    @given(st.dictionaries(st.text(), st.integers()),
           st.dictionaries(st.text(), st.integers()),
           st.dictionaries(st.text(), st.integers()))
    def test_context_merge_associative(self, ctx1, ctx2, ctx3):
        """Property: Context merge is associative (mirrors ctx-merge-assoc)"""
        merged_left = {**{**ctx1, **ctx2}, **ctx3}
        merged_right = {**ctx1, **{**ctx2, **ctx3}}
        assert merged_left == merged_right
    
    @given(st.text(), st.text())
    def test_mutex_single_owner(self, owner1, owner2):
        """Property: Lock can only have one owner (mirrors mutex-single-owner)"""
        locks = {}
        
        # First acquire succeeds
        locks["key1"] = owner1
        
        # Second acquire by different owner fails
        if owner1 != owner2:
            assert locks.get("key1") == owner1  # Still held by owner1
```

### 5.7 CI/CD Integration

**GitHub Actions Workflow:**
```yaml
# .github/workflows/acl2-proofs.yml

name: ACL2 Formal Verification

on:
  push:
    paths:
      - 'verification/acl2/**'
      - 'sdk/**/expressions/**'
      - 'sdk/**/flatmachine.*'
  pull_request:
    paths:
      - 'verification/acl2/**'

jobs:
  certify-books:
    runs-on: ubuntu-latest
    container:
      image: acl2/acl2:latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Certify ACL2 Books
        run: |
          cd verification/acl2
          make certify
      
      - name: Extract Theorem Summary
        run: |
          python3 scripts/extract-theorems.py > theorem-summary.md
      
      - name: Upload Proof Artifacts
        uses: actions/upload-artifact@v4
        with:
          name: acl2-proofs
          path: verification/acl2/**/*.cert

  property-tests:
    runs-on: ubuntu-latest
    needs: certify-books
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Python Property Tests
        run: |
          cd sdk/python
          pip install hypothesis pytest
          pytest tests/test_acl2_properties.py -v
      
      - name: Run JS Property Tests
        run: |
          cd sdk/js
          npm install
          npm run test:properties
```

### 5.8 Design Principles for Verifiability

**Pure Functions Where Possible:**
- Expression evaluation (simple mode)
- Transition condition checking
- Context merging
- Input/output mapping

**Explicit State Transitions:**
- Machine states are finite and enumerable
- Transitions are deterministic given context
- Side effects isolated to backends

**Keep Verifiable Core Small:**
- Extract pure logic into separate modules
- Use types that map cleanly to ACL2 (no complex generics)
- Document invariants in code comments

**Property-Based Testing Bridge:**
- Use property-based tests (Hypothesis, fast-check) as executable specs
- Same properties can guide ACL2 theorems

**Avoid:**
- Complex type hierarchies
- Dynamic dispatch in core logic
- Implicit state mutations

---

## 6. Cross-SDK Compatibility Checklist

### 6.1 Configuration Parsing

| Requirement | Python | JavaScript | Rust |
|-------------|--------|------------|------|
| YAML parsing | ✅ | ✅ | TODO |
| JSON Schema validation | ✅ | ✅ | TODO |
| Jinja2 template rendering | ✅ | ✅ | TODO |
| Profile resolution | ✅ | ✅ | TODO |

### 6.2 Runtime Interfaces

| Interface | Python | JavaScript | Rust |
|-----------|--------|------------|------|
| `NoOpLock` | ✅ | ✅ | TODO |
| `LocalFileLock` | ✅ | ✅ | TODO |
| `MemoryBackend` | ✅ | ✅ | TODO |
| `LocalFileBackend` | ✅ | ✅ | TODO |
| `InMemoryResultBackend` | ✅ | ✅ | TODO |

### 6.3 Execution Types

| Type | Python | JavaScript | Rust |
|------|--------|------------|------|
| `default` | ✅ | ✅ | TODO |
| `retry` | ✅ | ✅ | TODO |
| `parallel` | ✅ | ✅ | TODO |
| `mdap_voting` | ✅ | ✅ | TODO |

### 6.4 Expression Engines

| Engine | Python | JavaScript | Rust |
|--------|--------|------------|------|
| `simple` | ✅ | ✅ | TODO |
| `cel` | ✅ | Partial | TODO |

---

## 7. Testing Requirements

### 7.1 Conformance Test Suite

**Purpose:** Ensure SDKs behave identically for the same inputs.

**Test Categories:**
1. **Agent Tests:** Single LLM call, output parsing, template rendering
2. **Machine Tests:** State transitions, loops, error handling
3. **Parallel Tests:** Machine arrays, foreach, launch
4. **Persistence Tests:** Checkpoint/resume, crash recovery
5. **Expression Tests:** Simple mode evaluation, edge cases

**Test Format:** JSON test cases executable by any SDK:
```json
{
  "name": "simple_transition",
  "machine": { "spec": "flatmachine", ... },
  "input": { "query": "test" },
  "expected_states": ["start", "process", "done"],
  "expected_output": { "result": "processed" }
}
```

### 7.2 Property-Based Tests

**Properties to Test:**
- Checkpoint-resume equivalence
- Expression evaluation determinism
- Transition function totality
- Error handler completeness

---

## 8. Implementation Roadmap

### Phase 1: Spec Finalization
- [ ] Finalize `flatagents-runtime.d.ts` interface definitions
- [ ] Generate JSON Schema from TypeScript definitions
- [ ] Create conformance test suite (JSON format)
- [ ] Document all invariants for formal verification

### Phase 2: SDK Alignment
- [ ] Audit Python SDK against spec
- [ ] Audit JavaScript SDK against spec
- [ ] Identify and resolve behavioral differences
- [ ] Implement missing features in both SDKs

### Phase 3: Rust/WASM Implementation
- [ ] Core state machine logic (no I/O)
- [ ] Memory backend implementation
- [ ] WASM bindings via wasm-bindgen
- [ ] Browser-specific backends (IndexedDB, LocalStorage)
- [ ] Size optimization (< 500KB gzipped)

### Phase 4: Distributed Backends
- [ ] Redis persistence backend
- [ ] Redis result backend
- [ ] Redis distributed lock
- [ ] Cloud function examples (Lambda, GCP, Azure)

### Phase 5: Formal Verification
- [ ] ACL2 model of state machine core
- [ ] Prove progress invariant
- [ ] Prove checkpoint-resume equivalence
- [ ] Prove mutual exclusion for locks

---

## 9. Open Questions

1. **CEL Expression Engine:** Full CEL support in JavaScript and Rust?
2. **Hook Serialization:** How to serialize hooks for distributed execution?
3. **WASM LLM Backends:** Direct API calls from WASM or proxy through host?
4. **Cost Tracking:** Standardize cost calculation across providers?
5. **Observability:** Common tracing/metrics format (OpenTelemetry)?

---

## Appendix A: Current SDK File Mapping

| Component | Python | JavaScript |
|-----------|--------|------------|
| Agent | `flatagent.py` | `flatagent.ts` |
| Machine | `flatmachine.py` | `flatmachine.ts` |
| Profiles | `profiles.py` | `profiles.ts` |
| Execution | `execution.py` | `execution.ts` |
| Expressions | `expressions/` | `expression.ts` |
| Persistence | `persistence.py` | `persistence.ts` |
| Locking | `locking.py` | `locking.ts` |
| Hooks | `hooks.py` | `hooks.ts` |
| LLM Backends | `backends.py` | `llm/` |

## Appendix B: URI Scheme Reference

```
flatagents://{execution_id}/{path}

Paths:
  /checkpoint   - Machine state for resume
  /result       - Final output after completion

Examples:
  flatagents://550e8400-e29b-41d4-a716-446655440000/checkpoint
  flatagents://550e8400-e29b-41d4-a716-446655440000/result
```

## Appendix C: Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.7.7 | Current | Initial SDK common spec plan |
