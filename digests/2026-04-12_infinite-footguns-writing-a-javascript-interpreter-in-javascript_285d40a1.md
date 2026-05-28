---
url: https://mariozechner.at/posts/2025-10-05-jailjs/
title: 'Infinite Footguns: Writing a JavaScript Interpreter in JavaScript'
scraped_at: '2026-04-12T07:25:58Z'
word_count: 2470
raw_file: raw/2026-04-12_infinite-footguns-writing-a-javascript-interpreter-in-javascript_285d40a1.txt
tldr: Mario Zechner describes building JailJS, a JavaScript-in-JavaScript interpreter for browser extensions that can execute dynamically generated code on pages with strict CSP, while warning that sandboxing arbitrary code—especially LLM-generated code—is still fundamentally fragile.
key_quote: Congratutions us, we just broke the web.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mario Zechner
- Bob Nystrom
- ESTree
- Babel
tools:
- JailJS
- Chrome extension API
- chrome.scripting.executeScript
- Babel standalone
- esbuild
- SandboxJS
libraries: []
companies:
- Chrome
tags:
- browser-extensions
- content-security-policy
- javascript-interpreters
- sandboxing
- llm-agents
---

### TL;DR
Mario Zechner describes building **JailJS**, a JavaScript-in-JavaScript interpreter for browser extensions that can execute dynamically generated code on pages with strict CSP, while warning that sandboxing arbitrary code—especially LLM-generated code—is still fundamentally fragile.

### Key Quote
“Congratutions us, we just broke the web.”

### Summary
- **Context / motivation**
  - The author built a browser extension where an LLM in the side panel can navigate pages by injecting JavaScript into the active tab.
  - This is useful for reading pages, interacting with forms/buttons, and saving results as markdown, with full browser-history observability.
  - Two major problems arise:
    - The injected code runs in the page’s JS context and can access sensitive page data like DOM, `localStorage`, cookies, and IndexedDB.
    - Many sites enforce **Content Security Policy (CSP)**, blocking `eval`, `new Function`, and script-tag injection.

- **Why static extension functions are allowed**
  - `chrome.scripting.executeScript({ func: myPredefinedFunction })` works because the function is **statically defined** in the extension and serializable.
  - But dynamically generated code from a user or LLM is not statically known, so the usual `eval`-style approaches may be blocked by CSP.

- **Core idea: interpret code instead of executing it directly**
  - The workaround is to bundle a **parser + interpreter** into a content script, which is itself static and can run on any page.
  - The extension sends code strings to the content script; the content script parses them into an AST and evaluates them locally.
  - Example flow:
    - `parse('2 + 2')` returns an AST
    - `new Interpreter().evaluate(ast)` returns `4`
  - This avoids `eval`, `new Function`, and inline script injection, so it works even on sites with strict CSP.

- **Implementation approach**
  - Parsing is delegated to **Babel standalone**, rather than writing a JavaScript parser from scratch.
  - The interpreter handles the AST using a large recursive `switch` over node types.
  - The article shows simplified handling for:
    - `NumericLiteral`
    - `Identifier`
    - `BinaryExpression`
    - `VariableDeclaration`
  - The interpreter tracks variable bindings using a **scope chain** (current scope + parent scopes up to global).

- **Language support**
  - JailJS reportedly covers **ES5** semantics.
  - Through Babel transpilation, it can also run code written in **ES6+**, **TypeScript**, and **JSX** by compiling them down to ES5 first.
  - The author notes missing support for more advanced features such as:
    - generators
    - ES6 modules
    - Proxies
    - Reflect
    - WeakRef
    - SharedArrayBuffer
    - Atomics

- **Sandboxing goals and limitations**
  - The interpreter can be given a controlled set of globals through its `scope`, such as:
    - `console`, `Math`, `JSON`, `Date`, `RegExp`
    - basic constructors like `Array`, `Object`
    - error types and utility globals like `parseInt`, `parseFloat`
  - Notably excluded by default:
    - `window`
    - `document`
    - `fetch`
    - `Function`
    - `eval`

- **Danger of exposing native objects**
  - If you expose `document` to interpreted code, malicious or prompt-injected code can still try to exfiltrate data:
    - read `document.cookie`
    - reach `document.defaultView` to get `window`
    - access `localStorage`
    - send data out via an image beacon or fetch-like mechanism
  - The author experiments with **Proxy-based filtering** to hide dangerous properties like `defaultView` and `ownerDocument`, but argues this becomes a never-ending cat-and-mouse game.

- **Safer alternative**
  - Instead of exposing raw browser objects, expose **narrow custom APIs** such as:
    - `getPageText()`
    - `findButtons()`
    - `clickButton(text)`
    - `fillInput(selector, value)`
  - This reduces attack surface, but:
    - you must be careful what you expose
    - you must teach the LLM the custom API
    - it may perform worse than using familiar DOM APIs

- **Escape risk**
  - The post mentions prototype pollution and other escape routes as examples of why full sandboxing is hard.
  - JailJS blocks some known escape attempts, but the author emphasizes that a complete, secure sandbox for arbitrary JS is extremely difficult.

- **Conclusion / evaluation**
  - JailJS successfully solves the **CSP problem**: arbitrary code can be executed in extension-injected contexts without using `eval` or script tags.
  - It does **not** fully solve the **sandboxing problem**: arbitrary interpreted code may still escape or leak data.
  - The author frames it as a practical but imperfect tool: “You win some, you lose some.”

### Assessment
This is a **mixed** technical/opinion post with strong implementation detail and a clear security warning. Durability is **medium**: the concepts around CSP, interpreters, and sandboxing are broadly timeless, but the browser-extension APIs, the specific `JailJS` implementation, and the 2025 context may age. Content density is **high**: it includes concrete code examples, CSP constraints, AST/interpreter structure, and sandbox design tradeoffs. Originality is **primary source** because it presents the author’s own project and rationale, not just a summary of others’ work. It is best used as **refer-back** material if you’re building browser automation, LLM agents, or sandboxed script execution; it’s not a skim-once overview. Scrape quality is **good** overall: the article text and code snippets appear captured, though the “Here you can see it in action” demonstration/video content is only mentioned, not included, and the post likely had embedded media or visual examples that are missing.
