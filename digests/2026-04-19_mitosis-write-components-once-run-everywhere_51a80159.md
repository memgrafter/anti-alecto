---
url: https://mitosis.builder.io/
title: Mitosis - Write components once, run everywhere.
scraped_at: '2026-04-19T07:09:07Z'
word_count: 248
raw_file: raw/2026-04-19_mitosis-write-components-once-run-everywhere_51a80159.txt
tldr: Mitosis is a Builder.io tool that lets you write a component once in a Mitosis/JSX-like syntax and compile it into native components for multiple frameworks, including React, Vue, Angular, Svelte, and Qwik.
key_quote: Write components once, run everywhere.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: skim-once
scrape_quality: partial
people: []
tools:
- Mitosis
libraries:
- '@builder.io/mitosis'
- '@builder.io/qwik'
companies:
- Builder.io
tags:
- cross-framework
- component-compilation
- frontend-frameworks
- jsx
- ui-tooling
---

### TL;DR
Mitosis is a Builder.io tool that lets you write a component once in a Mitosis/JSX-like syntax and compile it into native components for multiple frameworks, including React, Vue, Angular, Svelte, and Qwik.

### Key Quote
“Write components once, run everywhere.”

### Summary
- The page is a product landing/demo for **Mitosis** from **Builder.io**.
- Its core promise is **framework portability**: author a component once, then generate framework-native code for:
  - **React**
  - **Vue**
  - **Angular**
  - **Svelte**
  - **Qwik**
  - and “many more frameworks”
- The example shows a simple component with:
  - local state initialized to **"Steve"**
  - an input field bound to that state
  - a static line of text
  - scoped red styling for the input
- The source example is written as **`mitosis.jsx`** using `useState` from `@builder.io/mitosis`, suggesting Mitosis uses a React-like authoring model.
- The page then shows framework-specific outputs:
  - **`component.vue`** uses Vue `<script setup>`, `ref`, template bindings, and scoped CSS.
  - **`angular.ts`** uses Angular `@Component`, template strings, and inline styles.
  - **`component.svelte`** uses Svelte `bind:value` and a `<style>` block.
  - **`qwik.tsx`** uses Qwik’s `component$`, `useStore`, and `useStylesScoped$`.
- The repeated example across outputs emphasizes that Mitosis is intended as a **compiler/transpiler for UI components**, not just a shared library.

### Assessment
This is a **high-durability** reference for the general idea of cross-framework component compilation, but it is also a **mixed** content type because it doubles as marketing/landing-page copy plus code examples. The page is fairly **dense** in that it demonstrates the same component in several target frameworks, which helps confirm the product’s behavior and positioning. It is **primary source** material for Mitosis’s own claims, so it’s useful for understanding the project’s intent, but it should be treated as promotional rather than neutral documentation. Best used as a **skim-once** or **refer-back** source when comparing framework output or recalling what Mitosis is. **Scrape quality: partial** — the content captured the headline and example code snippets, but not any surrounding explanation, navigation, documentation sections, or interactive demo context that may exist on the site.
