---
url: https://www.reddit.com/r/ChatbotRefugees/comments/1pmj2ic/chatticaai_just_launched_on_the_google_play_store/
title: 'ChatticaAI Just launched on the Google Play Store! take a look and give it a try! (iOS early Jan) : ChatbotRefugees'
scraped_at: '2026-04-17T05:19:44Z'
word_count: 1755
raw_file: raw/2026-04-17_chatticaai-just-launched-on-the-google-play-store-take-a-look-and-give-it-a-try-_c2911035.txt
tldr: ChatticaAI is a newly launched Android/iOS mobile chat app that emphasizes privacy and user-owned API keys, local storage, and optional image generation, with the developer actively answering setup questions and bug reports in-thread.
key_quote: Everything stored locally on your phone. Nothing touches my servers because I don't have any
durability: medium
content_type: announcement
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- AM_Interactive
- KaelithVeyra
- Rich_Can_6507
- ReplacementTommy
- call-lee-free
- GnomieNomi
- TeiniX
- OpenRouter
tools:
- ChatticaAI
- Google Play Store
- App Store
- OpenRouter
- OpenAI
- Anthropic
- nanoGPT
- LM Studio
- Stable Diffusion
- SillyTavern
libraries: []
companies:
- OpenAI
- Anthropic
- Google
- Apple
tags:
- mobile-apps
- ai-chat
- privacy
- api-keys
- image-generation
---

### TL;DR
ChatticaAI is a newly launched Android/iOS mobile chat app that emphasizes privacy and user-owned API keys, local storage, and optional image generation, with the developer actively answering setup questions and bug reports in-thread.

### Key Quote
“Everything stored locally on your phone. Nothing touches my servers because I don't have any”

### Summary
- **What was announced**
  - The developer, **u/AM_Interactive**, announced that **ChatticaAI** had just launched on the **Google Play Store** after a couple months of closed beta.
  - The post later adds that **iOS went live as well** via the App Store link.
  - The app had about **150 downloads at the time of posting**.
  - The app is **18+ rated**, **free to use**, and requires **no account**.

- **Core pitch**
  - Built as an alternative to apps that:
    - store conversations on their own servers,
    - charge tokens/coins/subscriptions,
    - and focus only on chat with weak image generation.
  - The developer claims the app is designed so **everything is stored locally** and **nothing goes through the developer’s servers**.

- **Main features listed**
  - **Bring your own API keys** for:
    - OpenRouter
    - OpenAI
    - Anthropic
    - nanoGPT
    - LM Studio
  - **Local storage** for chats.
  - **Image generation support**:
    - connect your own Stable Diffusion install,
    - or use an image API.
  - **Automatic image replies and background generation**
  - **LoRA fetching** from local Stable Diffusion install
  - **AI character/scenario creator**
  - **Import existing characters** via **PNG/JSON**
  - **Lorebooks**
  - **Session summaries**
  - **Tracking**
  - **Story mode**
  - **Texting mode**

- **Developer claims and positioning**
  - The developer says they get **better image results than SillyTavern** using ChatticaAI.
  - They frame the app as a privacy-first UI layer rather than a hosted AI service.
  - In comments, they explain that Chattica is essentially the **UI** and that the **API key/provider handles model access**.

- **Important setup/usage details from comments**
  - For users confused about models/API keys:
    - You sign up with a third-party provider like **OpenRouter**, **nanoGPT**, or **z.ai**.
    - You obtain an **API key** from that provider.
    - ChatticaAI uses that key to send messages to the provider’s LLMs.
  - For casual users who want simple setup, the developer suggests the **$8/month nanoGPT subscription**, which they say includes **2000 message and image replies per day**.
  - Suggested model/image combo mentioned:
    - **Deepseek** or **GLM 4.6** for chat
    - **juggernaut XL** for images

- **Performance / hardware comment**
  - When asked whether a powerful phone is needed, the developer says **no**.
  - They report testing on a **Samsung Galaxy A16 ($175 new)** and say the app is relatively light on-device, mainly keeping the last **~50 messages** on screen and relying on the model context window.

- **Community reactions**
  - Several commenters express enthusiasm and say they plan to try it, especially once iOS is available.
  - One user says they’ve used it for **two days** and are “blown away.”
  - Another user says the app was easier to use than expected, especially because labels and descriptions explain things like **prompt caching**.
  - A few commenters are confused about **LoRAs**, **models**, or whether their phone can handle local use.
  - One commenter complains that image generation requires payment; the developer responds by adding a **two-week free trial** to premium monthly.
  - A bug report mentions chat replies being **truncated after ~27 tokens / ~50 characters**; the developer asks for logging and provider details and says this seems like an edge case.
  - A criticism about the app not working leads the developer to explain the **forced tutorial** is there to ensure the user enters an API key.

- **Notable policy/stores issue**
  - A deleted comment asks about Brazil; the developer replies that they are **not willing to provide personal/business information** required there and that the country’s taxes/policy would leave them with only **27% of revenue**.

### Assessment
This is a **mixed announcement + support thread** with a fairly high density of practical setup details, pricing hints, and developer responses. **Durability is medium** because the launch, store availability, pricing, and platform-specific access can go stale quickly, but the broader ideas—BYO API keys, local storage, privacy-first chat UI—are more durable. The content type is mainly **announcement** with some **tutorial/reference** elements in the comments. **Density is medium-high** due to specific feature lists, model/provider names, pricing, and troubleshooting detail. It is **primary source** material since the developer is directly describing the product and answering questions. Best used as **refer-back** material if you want launch context, feature list, or the developer’s stated privacy model. **Scrape quality is good** overall: the post and comment discussion are captured well, though as with any Reddit scrape, image attachments and the full breadth of the thread may be incomplete.
