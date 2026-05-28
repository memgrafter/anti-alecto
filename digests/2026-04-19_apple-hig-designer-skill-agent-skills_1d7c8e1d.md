---
url: https://agent-skills.md/skills/jamesrochabrun/skills/apple-hig-designer
title: apple-hig-designer Skill | Agent Skills
scraped_at: '2026-04-19T08:05:14Z'
word_count: 2086
raw_file: raw/2026-04-19_apple-hig-designer-skill-agent-skills_1d7c8e1d.txt
tldr: A practical Apple HIG cheat sheet for designing native-feeling SwiftUI/UIKit iOS interfaces, covering Apple’s design principles, common components, typography, colors, spacing, accessibility, SF Symbols, motion, and platform-specific best practices.
key_quote: '"Design is not just what it looks like and feels like. Design is how it works." - Steve Jobs'
durability: high
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Steve Jobs
tools:
- SwiftUI
- UIKit
- VoiceOver
- SF Symbols
libraries: []
companies:
- Apple
tags:
- ios-design
- human-interface-guidelines
- swiftui
- accessibility
- mobile-ui
---

### TL;DR
A practical Apple HIG cheat sheet for designing native-feeling SwiftUI/UIKit iOS interfaces, covering Apple’s design principles, common components, typography, colors, spacing, accessibility, SF Symbols, motion, and platform-specific best practices.

### Key Quote
"Design is not just what it looks like and feels like. Design is how it works." - Steve Jobs

### Summary
- This is a reference-style guide for building iOS apps that follow Apple’s Human Interface Guidelines, with emphasis on:
  - native-feeling UI
  - accessibility
  - semantic colors
  - system typography
  - consistent spacing
  - platform-appropriate patterns

- **What the skill does**
  - Generates SwiftUI and UIKit components
  - Validates designs against Apple HIG
  - Checks accessibility concerns like VoiceOver, Dynamic Type, and contrast
  - Promotes Apple design principles: **Clarity, Deference, Depth**
  - Encourages use of semantic colors, SF Symbols, and the 8-point grid

- **Apple’s design principles**
  - **Clarity**: keep content focused and readable; avoid clutter and over-decoration
  - **Deference**: UI should support content, not compete with it
  - **Depth**: use layered visuals and motion to communicate hierarchy and relationships

- **Core iOS UI components and patterns**
  - **NavigationBar**: for top-level navigation/actions; large titles for top views, inline for detail views, keep toolbar items limited
  - **TabBar**: for top-level destinations; 3–5 tabs max, concise labels, SF Symbols icons
  - **List**: for scrollable content; shows `List`, `Section`, `NavigationLink`, and styles like `.plain`, `.insetGrouped`, `.sidebar`
  - **Sheet**: modal presentation with detents such as `.medium` and `.large`

- **Form controls**
  - **Button**: primary/secondary/tertiary hierarchy using `.borderedProminent`, `.bordered`, `.plain`
    - minimum touch target: **44x44**
    - use verbs for labels
    - destructive actions should require confirmation
  - **TextField / SecureField**: includes content types like `.username`, `.password`, `.emailAddress`, `.telephoneNumber`, `.creditCardNumber`
  - **Toggle**: for binary settings only; label should describe what it controls
  - **Picker**: demonstrates `.menu`, `.segmented`, `.wheel`, `.inline`; segmented is recommended for 2–5 options

- **Cards and containers**
  - Shows a sample `CardView` using padding, rounded corners, system background, and shadow
  - Reinforces that cards should feel elevated without becoming visually noisy

- **Typography**
  - Recommends Apple’s **San Francisco** system font
  - Lists Dynamic Type text styles and approximate sizes:
    - `.largeTitle` 34pt
    - `.title` 28pt
    - `.title2` 22pt
    - `.title3` 20pt
    - `.headline` / `.body` 17pt
    - down to `.caption2` 11pt
  - Advises:
    - use semantic text styles
    - support Dynamic Type
    - keep body text at least 17pt
    - avoid too many font sizes
    - avoid disabling Dynamic Type

- **Colors**
  - Strong focus on **semantic colors** that adapt automatically to light/dark mode:
    - `.label`, `.secondaryLabel`, `.systemBackground`, `.separator`, etc.
  - Includes system accent colors like `.systemBlue`, `.systemRed`, etc.
  - Notes how to define custom adaptive colors in Assets.xcassets
  - Gives contrast targets:
    - normal text: **4.5:1**
    - large text: **3:1**
    - UI components: **3:1**
    - critical text: aim for **7:1**

- **Spacing and layout**
  - Uses the **8-point grid system**
  - Shows common spacing values: 8, 16, 24, 32, etc.
  - Emphasizes respecting safe areas
  - Reiterates minimum interactive size of **44x44 points**
  - Suggests spacing scales such as 8 (tight), 16 (standard), 24 (loose)

- **Accessibility**
  - **VoiceOver**: use `.accessibilityLabel`, `.accessibilityValue`, `.accessibilityHint`, combine grouped elements, hide decorative content
  - **Dynamic Type**: use system fonts or custom fonts relative to text styles
  - **Color blindness**: don’t rely on color alone; pair color with icons/shapes/text
  - **Reduce Motion**: disable or simplify animations when the setting is enabled
  - **Increase Contrast**: adapt text colors for high-contrast mode
  - **Dark Mode**: use semantic colors, test both schemes, avoid pure black and automatic color inversion

- **SF Symbols**
  - Treats SF Symbols as Apple’s primary icon system
  - Shows usage for plain, colored, scaled, multicolor, and hierarchical symbols
  - Recommends using system symbols when available and keeping visual weight consistent

- **App icons**
  - Lists important icon sizes for iOS and watchOS
  - Advises:
    - simple recognizable shapes
    - fill the icon canvas
    - test on device
    - avoid text, photos, hardware mimicry, and translucency

- **Animation and motion**
  - Includes examples of spring, linear, and easeInOut animations
  - Shows a drag gesture example with spring reset
  - Best practices:
    - keep animations under 0.3 seconds
    - use spring animations for interactive elements
    - respect Reduce Motion
    - provide feedback for interactions

- **Best practices and state patterns**
  - Navigation:
    - hierarchical = `NavigationStack`
    - flat = `TabView`
    - content-driven = media-like flows
  - Feedback:
    - visual, haptic, and audio feedback
  - Loading / error / empty states:
    - includes example SwiftUI views for each
    - uses `ProgressView`, error icons/messages, and prominent retry/add actions

- **Platform considerations**
  - **iPhone**: diverse screen sizes, portrait/landscape, safe areas, one-handed use
  - **iPad**: multitasking, sidebars, keyboard shortcuts, external displays
  - **Apple Watch**: glanceable information, minimal interaction, larger touch targets, Digital Crown support, Always-On awareness

### Assessment
This is a **high-durability** reference/tutorial hybrid: most of the guidance is rooted in Apple’s long-running Human Interface Guidelines and general UX principles, so it should remain useful for a long time, though some code details and platform conventions may drift with newer iOS/SwiftUI versions. The content type is **mixed**, but primarily **reference** with tutorial-style SwiftUI examples. Density is **high** because it packs many specific rules, component patterns, code snippets, and accessibility constraints into one page. It appears to be a **synthesis** rather than a primary source, likely an agent skill distilled from Apple HIG concepts into a practical cheat sheet. Best used as **refer-back** material when designing iOS interfaces or checking compliance, not deep-study. **Scrape quality is good** overall: the text seems complete and well-structured, with code blocks and sections preserved, though formatting is somewhat flattened and may have lost some visual hierarchy.
