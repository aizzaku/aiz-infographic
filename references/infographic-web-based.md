---
name: infographic-web-based
description: Web-based HTML/CSS infographic: browser screenshot approach for simple visual infographics — demoted from `infographic` skill.
---

# Web-Based Infographics (Browser Screenshot)

*This content was demoted from the `infographic` skill → §14 of `aiz-infographic/SKILL.md`.*

## Overview

Create infographics as standalone HTML files rendered to PNG via `browser_navigate` + `browser_vision`. This is the simpler path — best for card grids, layout-based visuals, and quick screen captures.

## Pipeline

1. **Gather content** — `web_extract` or `browser_navigate` for URLs; user input for concepts
2. **Create HTML** — self-contained single `.html` file
3. **Render** — `browser_navigate` to `file:///tmp/<name>-infographic.html`, then `browser_vision` for screenshot
4. **Copy** — `cp` the screenshot to `/tmp/<name>-infographic.png`
5. **Deliver** — include `MEDIA:/absolute/path.png`

## Design Rules

**Dimensions:** 1080px wide (fits Telegram, Discord, email). Height is flexible.

**Font:** Inter from Google Fonts (import in `<style>`). JetBrains Mono for code/API keys.

**Dark theme by default:** background `#0a0a0f`, text `#e8e8f0`. Use light theme only if user requests it.

**Glow orbs:** Subtle `filter: blur(80px)` divs in purple/cyan/pink for depth. 2-3 max.

**Subtle grid:** CSS grid pattern overlay (`rgba(120,80,255,0.03)` lines at 40px intervals).

**Color accents:** Different gradient top-borders on cards (cyan, magenta, green, orange) to differentiate sections.

**Section titles:** Uppercase, letter-spacing 2px, colored (`#7850ff` purple), centered.

**Dividers:** `linear-gradient(90deg, transparent, rgba(120,80,255,0.3), transparent)` — thin, not heavy.

## Layout Patterns

### 2x2 Card Grid — for feature/tool listings
```css
.tools-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.tool-card { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 28px 24px; }
```

### Horizontal Steps — for processes/workflows (1 → 2 → 3 → 4)
- Numbered circles with gradient backgrounds, arrows between steps

### Pill/Tag Row — for lists of replaced items, features, etc
- Rounded pills with subtle borders, optional strikethrough for "replaced" items

### Benefits Grid — 3-4 column row for value propositions
- Small icons, bold titles, dim descriptions

## Pitfalls

- `web_extract` may fail if Firecrawl credits are exhausted — fall back to `browser_navigate` + `browser_snapshot`
- Google Fonts import requires internet — if rendering offline, use system font fallback (`font-family: 'Inter', sans-serif, system-ui`)
- `browser_vision` screenshot captures visible viewport only — if infographic is taller than viewport, the full HTML body renders as a single page (no scroll needed)
- In Telegram responses — use `MEDIA:/absolute/path` format, not markdown images

## Tips

- Keep content concise — infographics are scannable, not essay-length
- Use monospace font for API keys, code snippets, commands
- Strikethrough (`text-decoration: line-through; color: #ff6b6b`) on API keys visually communicates "no longer needed"

## Template Structure

```html
<!DOCTYPE html>
<html><head><style>
  /* Import Inter, dark background, grid overlay */
  /* .content { padding: 60px; position: relative; z-index: 1; } */
  /* .header { text-align: center; } */
  /* .section-title { uppercase, purple #7850ff, centered, letter-spacing } */
  /* .tools-grid → 2x2 cards with colored top borders */
  /* .divider → gradient line */
  /* .steps → horizontal numbered flow */
  /* .benefits → 4-col icon grid */
  /* .footer → centered brand + URL */
</style></head><body><!-- content --></body></html>
```
