# glasspaper — Frosted Panel Style

Concept: Frosted panels floating on a deep dark field. Depth through opacity layering, never blur.

Semi-transparent cards on a deep blue-navy or purple-navy base. Hierarchy built entirely from fill opacity — no visible dividers. No backdrop-filter. No glow.

## When to use

- Dashboard-style layouts with layered data
- Data with natural hierarchy (nested metrics, contained sub-sections)
- Elegant, modern dark-theme infographics without the density of forge/terminal
- Any context where depth and layering matter more than precision

## CSS variables

```css
:root {
  /* canvas — two valid base colors, choose by warmth */
  --canvas:          #0D1B2A;   /* default: cool blue-navy */
  /* --canvas:       #1A0A2E;   warm variant: purple-navy */

  /* card fills — opacity only, never flat colors */
  --panel:           rgba(255,255,255,0.06);
  --elevated:        rgba(255,255,255,0.03);

  /* card borders */
  --border-primary:  rgba(255,255,255,0.12);
  --border-secondary: rgba(255,255,255,0.06);

  /* text — always tinted, never pure white */
  --text-primary:    #C9B8F0;   /* pale violet-white */
  --text-secondary:  #8AB4D4;   /* pale blue */
  --text-muted:      rgba(255,255,255,0.25);
  --on-accent:       #0D1B2A;

  /* accent — chosen per infographic from the standard pairs */
  --accent-1: #C9B8F0;          /* default: pale violet */
  --accent-2: #8AB4D4;          /* default: pale blue */

  /* semantic */
  --positive: #00D018;
  --negative: #D0002D;

  /* spacing */
  --gap-section:     32px;
  --gap-element:     16px;
  --gap-card:        12px;
  --pad-container:   24px;

  /* radius — the one theme where soft edges are correct */
  --radius-card:  7px;
  --radius-pill:  5px;
  --radius-btn:   6px;
}
```

## Typography

Sans-serif for body. Monospace for values and codes. Hierarchy via opacity, not size.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | Inter | 700 | UPPERCASE | 48-64px |
| Section title | Inter | 700 | UPPERCASE | 18-22px |
| Card title | Inter | 600 | UPPERCASE | 14-16px |
| Value / metric | JetBrains Mono | 700 | as-is | 20-36px |
| Body | Inter | 400 | Sentence | 13-15px |
| Caption / code | JetBrains Mono | 400 | as-is | 11-12px |

## Decorative DNA

### Card layering (primary depth technique)

Two levels of opacity. Never more than 2.

```css
/* Outer card */
.card-outer {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 7px;
  padding: 20px;
}

/* Inner card (nested) */
.card-inner {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 5px;
  padding: 14px;
}
```

### No backdrop-filter

```css
/* NEVER */
/* backdrop-filter: blur(12px); */
/* -webkit-backdrop-filter: blur(12px); */
```

Frosted effect is achieved through fill opacity alone.

### No glows or drop shadows

```css
/* NEVER */
/* box-shadow: 0 0 20px rgba(var(--accent-1), 0.3); */
/* filter: drop-shadow(...); */
```

### Spacing as separator

Sections are separated by gap only. No visible divider lines, no `<hr>`, no border-bottom between sections.

### Gradient text (permitted)

Subtle, same-hue:

```css
.gradient-text {
  background: linear-gradient(135deg, #C9B8F0, #8AB4D4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

## Badge / status pill

Use `inline-tag` variant from `badges.md`. Opacity-based, no border.

```css
.inline-tag {
  background: rgba(255,255,255,0.10);
  color: var(--text-primary, #C9B8F0);
  border-radius: 4px;
  padding: 3px 8px;
}
```

## Progress bar

Use `rounded-bar` variant from `progress-bars.md`. Accent fill with soft radius.

## Step-connector

Circle badges, semi-transparent connector line at `rgba(255,255,255,0.20)`.

## Style verification checklist

- [ ] Canvas is `#0D1B2A` or `#1A0A2E` — not pure black, not generic dark
- [ ] Card fills are `rgba(255,255,255,x)` — never flat `#hex` backgrounds on cards
- [ ] Text is tinted, not pure white (`#C9B8F0` or `#8AB4D4`)
- [ ] `border-radius` on all cards: 6-8px
- [ ] No `backdrop-filter: blur` anywhere
- [ ] No glow effects, no drop shadows
- [ ] Spacing separates sections — no visible divider elements

## What to avoid

`backdrop-filter: blur`, glow effects, pure white text, pure black background (#000 or #111), hard borders on cards, monospace-only typography.
