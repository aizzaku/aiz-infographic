# openclaw — Dark Hacker Terminal Style

Source: `openclaw-v2026-3-22-infographic.html` (canonical release infographic)
Concept: Dark hacker terminal meets product launch. Data is a release log. Blue-tinted near-black field, single hot-red accent owns all signal.

```
canvas-fit: [bento-box, editorial, poster]
```

## When to use

- OpenClaw release infographics or changelogs
- Product launch announcements in the OpenClaw ecosystem
- Any content explicitly requesting the OpenClaw brand style
- Auto-selected when content is about OpenClaw releases, features, or updates

## CSS variables

```css
:root {
  /* canvas — blue-tinted near-black, NOT pure #000 */
  --canvas:        #0A0A0C;
  --panel:         #111116;   /* card background — same blue cast */
  --elevated:      #16161C;   /* inner / nested surfaces */

  /* borders */
  --border-default: rgba(255,255,255,0.07);
  --border-accent:  rgba(255,77,77,0.30);

  /* accent — the only color in the system */
  --accent-1:      #FF4D4D;
  --accent-2:      #FF4D4D;
  --accent-dim:    rgba(255,77,77,0.15);
  --accent-glow:   rgba(255,77,77,0.40);
  --on-accent:     #0A0A0C;

  /* text */
  --text-primary:   #F0F0F5;
  --text-secondary: rgba(240,240,245,0.70);
  --text-muted:     rgba(240,240,245,0.38);

  /* semantic */
  --positive: #00D018;
  --negative: #FF4D4D;

  /* spacing */
  --gap-section:   28px;
  --gap-element:   16px;
  --gap-card:      8px;
  --pad-container: 20px;

  /* radius */
  --radius-card:  6px;
  --radius-pill:  4px;
  --radius-btn:   4px;
}
```

## Typography

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700&display=swap">
```

| Role | Font | Weight | Case | Size | Letter-spacing |
|------|------|--------|------|------|----------------|
| Hero title | Bebas Neue | 400 | UPPERCASE | 56px | 0.02em |
| Col label | Bebas Neue | 400 | UPPERCASE | 11px | 0.14em |
| Stat value | Bebas Neue | 400 | as-is | 30px | 0.02em |
| Item title | Inter | 600 | Sentence | 11.5px | normal |
| Item desc | Inter | 400 | Sentence | 10px | normal |
| Body | Inter | 400 | Sentence | 13-14px | normal |
| Footer | Inter | 400 | Sentence | 10px | 0.04-0.06em |

**No gradient text** — accent (#FF4D4D) for emphasis only, never gradient.

## Layout rules

```
alignment:    left-aligned throughout
hero:         full-width Bebas Neue 56px, white + accent on release number/version
stats-strip:  5-column grid, 1px gap, bg = border-default, each cell = surface
              stat value: Bebas Neue 30px accent, label 9.5px muted small-caps
content:      3-column equal grid
col-label:    Bebas Neue 11px accent, border-bottom 1px border-accent, icon + text
item:         icon (15px accent) + title + desc, 8px padding, surface bg, default border
footer:       hairline border-top, left = link (accent), right = metadata (muted)
```

## Decorative DNA

### Card borders

Standard card: `rgba(255,255,255,0.07)`. Alert/breaking card: `rgba(255,77,77,0.20)`.

```css
.card {
  background: var(--panel);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-card, 6px);
}
```

No gradient borders — OpenClaw uses solid hairlines only.

### Breaking item treatment

Structural distinction for breaking changes — not decorative:

```css
.item-breaking {
  background: rgba(255,77,77,0.05);
  border: 1px solid rgba(255,77,77,0.20);
}
.item-breaking .item-title { color: #FFA0A0; }
.item-breaking .item-icon  { color: #FF4D4D; }
```

### Signature background

```css
.infographic-canvas {
  background-color: var(--canvas);
  background-image:
    /* SVG grid: white stroke 0.5px, opacity 0.03 */
    url("data:image/svg+xml,%3Csvg width='40' height='40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M 40 0 L 0 0 0 40' fill='none' stroke='white' stroke-width='0.5' opacity='0.03'/%3E%3C/svg%3E");
}

/* Radial accent glow — top-right and bottom-left */
.canvas-glow-tr {
  position: absolute;
  top: -80px; right: -120px;
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(255,77,77,0.07), transparent 70%);
  pointer-events: none;
}
.canvas-glow-bl {
  position: absolute;
  bottom: -80px; left: -120px;
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(255,77,77,0.04), transparent 70%);
  pointer-events: none;
}
```

### Badge system

```css
.badge {
  background: var(--accent-dim);
  border: 1px solid var(--border-accent);
  border-radius: 3px;
  color: var(--accent-1);
  font: 700 11px/1 'Inter', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 3px 8px;
}
.badge-date {
  background: transparent;
  border: 1px solid var(--border-default);
  color: var(--text-muted);
}
```

### Stats strip

```css
.stats-strip {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1px;
  background: var(--border-default);
}
.stat-cell {
  background: var(--panel);
  padding: 16px;
}
.stat-value {
  font: 400 30px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.02em;
  color: var(--accent-1);
}
.stat-label {
  font: 400 9.5px/1 'Inter', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  font-variant-caps: small-caps;
}
```

## Style verification checklist

- [ ] Canvas is `#0A0A0C` — blue-tinted, never warm black or pure `#000`
- [ ] Single accent: `#FF4D4D` only — no second color
- [ ] No gradient text anywhere
- [ ] No border-radius above 6px
- [ ] Breaking items use the structural tint treatment

## Forbidden

No warm tones — the blue cast in the black must be maintained. No second accent color. No rounded corners above 6px. No gradient text. No filled background on accent badges — always `accent-dim`.
