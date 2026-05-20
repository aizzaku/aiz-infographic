# grok-dark — Brutalist Monochrome Style

Source: xAI brand identity — monochrome, brutalist by design, rejects all tech-brand softness
Concept: Absolute monochrome. True black field, maximum-weight condensed type, zero color. Raw capability through contrast alone.

```
canvas-fit: [bento-box, poster, editorial]
```

## When to use

- Grok or xAI product and model infographics
- Analyses of Grok capabilities or xAI research
- Any content explicitly requesting the Grok or xAI brand style
- Auto-selected when content is primarily about Grok models or xAI products

## CSS variables

```css
:root {
  /* canvas — as close to true black as exists without being #000 */
  --canvas:        #080808;
  --panel:         #111111;
  --elevated:      #1A1A1A;

  /* no color — pure monochrome */
  --accent-1:      #F5F5F5;   /* set to primary text to avoid broken color-mix calls */
  --accent-2:      #888888;
  --on-accent:     #080808;

  /* text */
  --text-primary:   #F5F5F5;
  --text-secondary: #888888;
  --text-muted:     #3A3A3A;

  /* borders */
  --border-default: rgba(255,255,255,0.08);
  --border-strong:  rgba(255,255,255,0.16);

  /* semantic — no color; convey via position and weight only */
  --positive: #F5F5F5;
  --negative: #888888;

  /* spacing — compressed */
  --gap-section:   20px;
  --gap-element:   12px;
  --gap-card:      8px;
  --pad-container: 20px;

  /* radius — ZERO everywhere */
  --radius-card:  0px;
  --radius-pill:  0px;
  --radius-btn:   0px;
}
```

## Typography

Condensed heavy sans. Inter at weight 900, or system-ui at weight 900 for true condensed effect.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap">
```

| Role | Font | Weight | Case | Size | Notes |
|------|------|--------|------|------|-------|
| Hero | Inter | 900 | ALL CAPS | 48-64px | letter-spacing 0.10-0.14em |
| Section label | Inter | 700 | ALL CAPS | 11px | letter-spacing 0.12em, text-secondary |
| Card title | Inter | 700 | ALL CAPS | 14-16px | letter-spacing 0.08em |
| Body | Inter | 400 | Sentence | 13px | line-height 1.5, text-secondary |
| Metadata | Inter | 500 | Sentence | 10px | text-muted, letter-spacing 0.08em |
| Code | monospace | 400 | as-is | 12px | for data or code refs |

ALL CAPS for all headlines — no exceptions. Weight 900 for display type.

## Decorative DNA

### Vertical bar dividers (signature element)

Between major section columns — the canonical Grok structural marker:

```css
.grok-vbar {
  width: 2px;            /* or 3px for major section separation */
  background: var(--text-primary);
  align-self: stretch;
  flex-shrink: 0;
}
```

Not horizontal rules. Vertical bars at 2-3px solid text-primary between columns.

### Cards

Hard rectangles. No softness.

```css
.card {
  background: var(--panel);
  border: 1px solid var(--border-default);
  border-radius: 0;      /* ZERO — absolute rule */
  padding: 16px;
}
```

### Tags / badges

Hard rectangle, text-primary border, no fill:

```css
.tag {
  background: transparent;
  border: 1px solid var(--text-primary);
  border-radius: 0;      /* no rounding */
  color: var(--text-primary);
  font: 700 10px/1 'Inter', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 3px 8px;
}
```

No pill shapes, no circles, no status dots — squares only.

### No gradient, no glow, no shadow

```css
/* NEVER in grok-dark */
/* text-shadow, box-shadow, background gradient, filter */
```

## Layout rules

```
alignment:     left-aligned, no centering
border-radius: ZERO everywhere — absolute, no exceptions
dividers:      2-3px solid text-primary VERTICAL bars between major sections
cards:         hard rectangles, no softness
spacing:       compressed — no breathing room
hero:          ALL CAPS, weight 900, full width
```

## Gradient text

Disabled entirely. No gradient text anywhere.

## Style verification checklist

- [ ] Canvas is `#080808` — cool near-black, no warmth
- [ ] Zero border-radius everywhere — no exceptions
- [ ] ALL CAPS for all headline text
- [ ] Weight 900 for display type
- [ ] Vertical bar dividers (2-3px) between sections — not horizontal rules
- [ ] No color of any kind
- [ ] No glow, shadow, or gradient

## Forbidden

No color accent of any kind. No border-radius anywhere (0 is absolute). No gradient text. No rounded shapes (including pills, circles, status dots). No warmth. No shadow or glow. No lowercase display type.
