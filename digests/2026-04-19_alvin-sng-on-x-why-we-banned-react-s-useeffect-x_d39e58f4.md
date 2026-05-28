---
url: https://x.com/alvinsng/status/2033969062834045089
title: 'Alvin Sng on X: "Why we banned React''s useEffect" / X'
scraped_at: '2026-04-19T07:01:00Z'
word_count: 1227
raw_file: raw/2026-04-19_alvin-sng-on-x-why-we-banned-react-s-useeffect-x_d39e58f4.txt
tldr: Alvin Sng argues that Factory banned direct `useEffect` in React to reduce bugs and complexity, replacing most cases with derived state, event handlers, data-fetching libraries, a named `useMountEffect`, and `key`-based remounts.
key_quote: “Banning the hook forces the logic to be declarative and predictable.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Alvin Sng
- Guillermo Rauch
- Seb
- Theo
- Peter Steinberger
tools:
- React
- useEffect
- useQuery
- useMountEffect
libraries: []
companies:
- Factory
tags:
- react
- frontend-architecture
- side-effects
- state-management
- code-quality
---

### TL;DR
Alvin Sng argues that Factory banned direct `useEffect` in React to reduce bugs and complexity, replacing most cases with derived state, event handlers, data-fetching libraries, a named `useMountEffect`, and `key`-based remounts.

### Key Quote
“Banning the hook forces the logic to be declarative and predictable.”

### Summary
- The post describes Factory’s frontend rule: **no direct `useEffect` calls**.
- To allow the rare legitimate mount-time side effect, they wrap `useEffect(..., [])` in a named helper:
  ```ts
  export function useMountEffect(effect: () => void | (() => void)) {
    useEffect(effect, []);
  }
  ```
- The core argument is that most `useEffect` usage is a workaround for better React primitives:
  - derived state should be computed directly
  - user actions should live in event handlers
  - fetching should use dedicated data-fetching libraries
  - one-time external sync should use `useMountEffect`
  - reset/restart behavior should use `key`, not dependency choreography
- The author says the rule emerged from **production bugs**, especially:
  - brittle dependency arrays that hide coupling
  - infinite loops from state-update/effect chains
  - “dependency hell” from time-based control flow
  - debugging difficulty around “why did this run?”
- The post gives five replacement patterns:

  1. **Derive state, don’t sync it**
     - Example: compute `filteredProducts = products.filter(...)` instead of storing filtered state in an effect.
     - Warns against effects that do `setX(deriveFromY(y))`.

  2. **Use data-fetching libraries**
     - Example: `useQuery(['product', productId], () => fetchProduct(productId))`
     - Argument: effect-based fetching reimplements caching, retries, cancellation, and staleness handling, and can race.

  3. **Use event handlers, not effects**
     - Example: call `postLike()` directly in `onClick`
     - Warns against using state as a trigger flag for an effect.

  4. **Use `useMountEffect` for true mount-time sync**
     - Good for DOM integration, third-party widgets, browser subscriptions.
     - Recommends conditional mounting instead of guarding inside effects.

  5. **Reset with `key`, not effect orchestration**
     - If a component should start fresh when an ID changes, key it by that ID so React remounts it cleanly.

- The author frames the rule as a **forcing function for cleaner architecture**:
  - parents own orchestration and lifecycle boundaries
  - children assume preconditions are already met
  - components become simpler and side effects become less hidden
- The post closes by saying the team saw:
  - fewer infinite loops
  - fewer race-condition regressions
  - faster onboarding
- It recommends enforcing the rule with:
  - lint rules
  - clear agent guidance in `AGENTS.md`
  - and a product/tooling push to mass-fix violations

### Assessment
This is a **mixed** opinion-and-practice post with a strong prescriptive stance, but it’s also grounded in concrete code examples and engineering experience. Durability is **medium**: the architectural advice is broadly reusable, but it is firmly tied to React’s current hook model and ecosystem patterns. Density is **high** because it packs several actionable rules, anti-patterns, and code snippets into one thread. Originality is best described as **commentary** rather than primary research: it’s the author’s team practice and rationale, not an empirical study, though it does include anecdotal outcomes from production. It’s best used as a **refer-back** reference if you want the specific replacement patterns and heuristics. Scrape quality is **partial**: the thread text is mostly intact, but some embedded linked media/images and the referenced “React guide” appear truncated or missing, so a full reread would be needed for exact context around those visuals and links.
