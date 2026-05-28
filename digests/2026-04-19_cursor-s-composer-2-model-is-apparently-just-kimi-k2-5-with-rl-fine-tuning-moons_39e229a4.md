---
url: https://www.reddit.com/r/singularity/comments/1ryrs2w/cursors_composer_2_model_is_apparently_just_kimi/
title: 'Cursor’s ‘Composer 2’ model is apparently just Kimi K2.5 with RL fine-tuning. Moonshot AI says they never paid or got permission : r/singularity'
scraped_at: '2026-04-19T21:55:26Z'
word_count: 2747
raw_file: raw/2026-04-19_cursor-s-composer-2-model-is-apparently-just-kimi-k2-5-with-rl-fine-tuning-moons_39e229a4.txt
tldr: Reddit thread about the claim that Cursor’s “Composer 2” is really Kimi K2.5 with RL fine-tuning, where top commenter `u/peakedtooearly` says Cursor has little future and would rather use VS Code + Codex, while the thread splits over whether the real issue is unfair commercial use, missing attribution, or just open-model fine-tuning being normal.
key_quote: I don't think there is much of a future for Cursor.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: skim-once
scrape_quality: partial
people:
- u/likeastar20
- u/peakedtooearly
- Moonshot AI
- Cursor
- Kimi
tools:
- Cursor
- VS Code
- Codex
- Claude Code
- Copilot
- Zed
libraries: []
companies:
- Moonshot AI
- Cursor
- OpenAI
- Anthropic
- GitHub
tags:
- ai-models
- open-source-ai
- licensing
- cursor
- code-assistants
---

### TL;DR
Reddit thread about the claim that Cursor’s “Composer 2” is really Kimi K2.5 with RL fine-tuning, where top commenter `u/peakedtooearly` says Cursor has little future and would rather use VS Code + Codex, while the thread splits over whether the real issue is unfair commercial use, missing attribution, or just open-model fine-tuning being normal.

### Key Quote
"I don't think there is much of a future for Cursor."

### Summary
- **Top comment (verbatim):** "I don't think there is much of a future for Cursor. Once the Codex plugin was available I barely use anything they have. I'm actually thinking of just going back to VS + Codex."
- **Top commenter:** `u/peakedtooearly`
- **Thread topics:**
  - Whether Cursor’s “Composer 2” is actually Kimi K2.5 under the hood
  - Whether Cursor violated Moonshot’s modified MIT-style attribution requirement
  - Whether fine-tuning an open model is legitimate versus misleading branding
  - Whether users are better off switching to VS Code + Codex / Claude Code
  - Broader suspicion about “proprietary” AI models that may just be open weights with branding

- The post claims Cursor’s “Composer 2” model is apparently just **Kimi K2.5 with RL fine-tuning**, and that **Moonshot AI says they never paid or got permission**.
- The thread’s central split is less about the engineering itself and more about:
  - **Attribution / license compliance**: multiple commenters point to a modified MIT-style clause requiring prominent UI display of **“Kimi K2.5”** for sufficiently large commercial products.
  - **Commercial misrepresentation**: several users say Cursor sold Composer 2 as a proprietary leap when it may have been a repackaged open model.
  - **Normal fine-tuning vs deception**: some argue using open weights + RL fine-tuning is standard practice, but hiding the base model from users and investors is the real problem.
- A major side discussion is practical migration away from Cursor:
  - Many commenters say they’ve moved to **VS Code + Codex**, **Claude Code**, **Copilot**, or **Zed**.
  - Cursor is repeatedly described as mainly valuable for **autocomplete/tab completion**, while others say the rest can be replicated in VS Code with plugins or CLIs.
- There is also a broader ideological argument:
  - Some commenters defend open models and say this is why open weights matter.
  - Others dismiss the complaint as hypocrisy, arguing Chinese models are also distilled from frontier US models.
  - A few commenters focus specifically on the distinction between **training on outputs** and **post-training a model and presenting it as your own**.
- The most concrete technical/legal detail in the thread is the alleged license condition:
  - For commercial products with **more than 100 million monthly active users** or **more than $20 million/month revenue**, the UI must prominently display **“Kimi K2.5”**.
  - Commenters debate whether Cursor crossed that threshold and whether showing the model in hidden request JSON satisfies attribution.

### Assessment
This is a **mixed** social-thread capture with moderate-to-high density because it concentrates a licensing controversy, product-switching anecdotes, and model-ethics arguments into a single discussion. **Durability is medium**: the specific Cursor/Moonshot allegation is time-sensitive, but the broader themes—open-model fine-tuning, attribution, and AI vendor trust—will remain relevant. **Originality is commentary** rather than primary evidence; the thread mostly reacts to an external claim, and the linked proof itself is not included, so verification is limited. As a reference, it is best used **skim-once to refer-back** if you want the shape of the debate or the exact licensing-attribution angle, not for deep technical study. **Scrape quality is partial**: the discussion comments are well captured, but the underlying post, images, and any external evidence/tweets are not present, so the thread is comment-heavy speculation rather than a complete source record. Overall, it’s worth saving for the **licensing/attribution dispute and the “Cursor vs VS Code + Codex” migration sentiment**, not for rigorous proof of the underlying model claim.
