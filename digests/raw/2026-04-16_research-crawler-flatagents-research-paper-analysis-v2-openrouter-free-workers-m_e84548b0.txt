# OpenRouter Free Tier Budget Planning (v2)

## Constraint

OpenRouter free requests are shared across both models:
- `openrouter/openai/gpt-oss-120b:free` (cheap/structured)
- `openrouter/openrouter/pony-alpha` (expensive/reasoning)

**Daily budget: ~1000 requests.** RPM cap: ~20.

## Calls per paper (three-phase split)

### Phase 1: Prep (cheap model, 1 request)
| Agent | Model | Requests |
|---|---|---|
| key_outcome_writer | cheap | 1 |
| **Total** | | **1** |

### Phase 2: Expensive (pony-alpha only, 3 requests — all parallel)
| Agent | Model | Requests |
|---|---|---|
| why_hypothesis_writer | expensive | 1 |
| reproduction_writer | expensive | 1 |
| open_questions_writer | expensive | 1 |
| **Total** | | **3** |

### Phase 3: Wrap (cheap model, 3-5 requests)
| Agent | Model | Requests |
|---|---|---|
| limits_confidence_writer | cheap | 1 |
| report_assembler | cheap | 1 |
| completeness_judge | cheap | 1 |
| targeted_repair (if needed) | cheap | 0-1 |
| re-judge (if repaired) | cheap | 0-1 |
| **Total** | | **3-5** |

### Combined: 7-9 requests/paper (3 expensive + 4-6 cheap)

## Why this split maximizes pony-alpha

In the old two-phase design, expensive and cheap calls were mixed in the
analysis phase. When pony-alpha was available, 40-60% of calls were cheap
(wasted opportunity). Now:

- **Phase 2 is 100% pony-alpha.** Every API call during the expensive phase
  hits pony-alpha. No cheap calls diluting the window.
- **Phases 1 and 3 are 100% cheap.** Run during downtime or as buffer fills.

## Daily capacity at 1000 req budget

### Scenario A: Maximize pony-alpha (steady state, buffer full)
1. Run expensive on 100 papers: 300 pony-alpha calls
2. Wrap 100 papers: 300-500 cheap calls
3. Prep 100 papers with remaining: 100 cheap calls
4. **Total: 700-900 calls, 100 papers complete**

### Scenario B: Cold start (build buffer first)
1. Prep 100 papers: 100 cheap calls
2. Run expensive on 75 papers: 225 pony-alpha calls
3. Wrap 75 papers: 225-375 cheap calls
4. **Total: 550-700 calls, 75 papers complete**

### Scenario C: Pony-alpha burst window
When pony-alpha becomes available after being down:
- All workers run expensive (3 req each, parallel within)
- 5 workers × 3 req = 15 pony-alpha calls per pass
- Each pass takes ~40s (parallel calls)
- ~22 passes/15min = ~330 pony-alpha calls = 110 papers through expensive

## Worker sizing (RPM-limited)

With 20 RPM shared cap:

| Phase | Calls/paper | Time/paper | Workers | Est. RPM |
|---|---|---|---|---|
| Expensive | 3 (parallel) | ~40s | 5 | ~7.5 |
| Expensive | 3 (parallel) | ~40s | 8 | ~12 |
| Wrap | 3-5 (sequential) | ~90s | 5 | ~2 |
| Prep | 1 | ~15s | 10 | ~4 |

Expensive phase has lowest RPM per worker (parallel calls complete together).

## Recommended operating modes

```bash
# Normal operation: balanced all phases
python run.py --workers 5 --daemon

# Maximize pony-alpha throughput
python run.py --workers 8 --daemon

# Fill buffer (cheap, high concurrency)
python run.py --workers 10 --prep-only --daemon

# Conservative (expensive model flaky)
python run.py --workers 3 --daemon
```
