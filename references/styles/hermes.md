# hermes — Dark Forest Terminal Style

Source: `hermes-v2026-4-30-highlights.html` (canonical release infographic, Nous Research)
Concept: Dark forest terminal. Data is a CLI agent release. Two-accent gold+sage system, gradient borders on every card, three-font stack.

```
canvas-fit: [bento-box, dashboard, poster]
```

## When to use

- Hermes / Nous Research release infographics
- AI agent or model capability comparisons
- Any content explicitly requesting the Hermes brand style
- Auto-selected when content is about Hermes models, Nous Research, or Hermes agent features

## CSS variables

```css
:root {
  /* canvas — darkest green-black */
  --canvas:        #060D0A;
  --panel:         #0F2018;
  --elevated:      #172B1E;
  --on-accent:     #060D0A;

  /* accent pair — antique gold + sage green */
  --accent-1:      #CEBF85;
  --accent-2:      #72A888;

  /* text — warm parchment */
  --text-primary:   #E8D9B0;
  --text-secondary: #C8BB90;
  --text-muted:     #8A7F60;

  /* semantic */
  --positive: #00D018;
  --negative: #D0002D;

  /* spacing */
  --gap-section:   24px;
  --gap-element:   16px;
  --gap-card:      14px;
  --pad-container: 28px;

  /* radius */
  --radius-card:  10px;
  --radius-pill:  6px;
  --radius-btn:   8px;
}
```

## Typography

Three-font stack: display + body + mono.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;700&family=JetBrains+Mono:wght@400;700&display=swap">
```

| Role | Font | Weight | Case | Size | Notes |
|------|------|--------|------|------|-------|
| Hero title | Bebas Neue | 400 | UPPERCASE | 96px | gradient text, letter-spacing 0.03em |
| Hero eyebrow | Montserrat | 700 | UPPERCASE | 11px | letter-spacing 0.18em, accent-1 |
| Hero subtitle | Montserrat | 700 | UPPERCASE | 16px | letter-spacing 0.12em, text-secondary |
| KPI value | Bebas Neue | 400 | as-is | 56px | accent-1 |
| KPI label | Montserrat | 700 | UPPERCASE | 10px | letter-spacing 0.12em, text-secondary |
| Card number | Bebas Neue | 400 | as-is | 52px | gradient accent-1→accent-2, opacity 0.7 |
| Card title | Montserrat | 700 | UPPERCASE | 18px | letter-spacing 0.06em, text-primary |
| Body | Montserrat | 400 | Sentence | 13px | line-height 1.55 |
| Feature text | Montserrat | 400 | Sentence | 12px | line-height 1.55 |
| Badge | Montserrat | 700 | UPPERCASE | 11px | letter-spacing 0.05em |
| Code block | JetBrains Mono | 700 | as-is | 13px | letter-spacing 0.02em, accent-1 |
| Big stat | Bebas Neue | 400 | as-is | 80px | gradient text |

**No Inter font.** Body is Montserrat, code is JetBrains Mono.

## Gradient text

Used on: hero title, card numbers, big stats, section labels. Direction: `linear-gradient(28deg, var(--accent-1) 30%, var(--accent-2) 100%)`.

```css
.gradient-text {
  background: linear-gradient(28deg, #CEBF85 30%, #72A888 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}
```

## Decorative DNA

### Gradient border — the key Hermes signature

Every card uses a gradient border via the `padding-box / border-box` technique:

```css
/* Standard card */
.card {
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-2) 40%, transparent),
      color-mix(in srgb, var(--accent-1) 20%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card, 10px);
  box-shadow: 0 0 28px color-mix(in srgb, var(--accent-1) 5%, transparent);
}

/* Focal card (hero-level) */
.card-focal {
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg, #CEBF85 35%, #72A888 55%) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card, 10px);
  box-shadow: 0 0 52px color-mix(in srgb, var(--accent-1) 14%, transparent);
}
```

No card without a gradient border — this is non-negotiable.

### Canvas background

```css
.infographic-canvas {
  background-color: var(--canvas);
  background-image:
    /* Soft top green glow */
    radial-gradient(ellipse 70% 30% at 50% 0%,
      color-mix(in srgb, var(--accent-2) 7%, transparent), transparent),
    /* Soft bottom green glow */
    radial-gradient(ellipse 60% 20% at 50% 100%,
      color-mix(in srgb, var(--accent-2) 4%, transparent), transparent);
}
```

### Noise texture

```html
<svg style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;opacity:0.04;mix-blend-mode:screen;" aria-hidden="true">
  <filter id="noise"><feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/></filter>
  <rect width="100%" height="100%" filter="url(#noise)"/>
</svg>
```

### Card anatomy

```html
<div class="card">
  <div class="card-header">
    <div class="card-left">
      <i class="ph-bold ph-lightning" style="font-size:22px;color:var(--accent-1);opacity:0.9;"></i>
      <span class="card-title">Feature Name</span>
    </div>
    <div class="card-num gradient-text">01</div>
  </div>
  <div class="card-body">
    <!-- body-text or feat-list or code-block or big-stat -->
  </div>
</div>

<style>
.card-header { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; }
.card-left { display:flex; align-items:center; gap:8px; }
.card-title { font:700 18px/1.2 'Montserrat',sans-serif; text-transform:uppercase; letter-spacing:0.06em; color:var(--text-primary); }
.card-num { font:400 52px/1 'Bebas Neue',sans-serif; opacity:0.7; }
</style>
```

### Feature list

```css
.feat-item { display:flex; align-items:flex-start; gap:8px; }
.feat-dot {
  width: 5px; height: 5px;
  border-radius: 50%;
  background: var(--accent-1);
  flex-shrink: 0;
  margin-top: 5px;
}
.feat-text { font:400 12px/1.55 'Montserrat',sans-serif; color:var(--text-primary); }
```

### Tool / platform badge

```css
.tool-badge {
  display:inline-flex; align-items:center; gap:6px;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, var(--accent-1) 25%, transparent);
  background: color-mix(in srgb, var(--accent-1) 8%, transparent);
  padding: 4px 10px;
}
.tool-num { font:400 14px/1 'Bebas Neue',sans-serif; color:var(--accent-1); }
.tool-label { font:700 10px/1 'Montserrat',sans-serif; text-transform:uppercase; letter-spacing:0.06em; color:var(--text-secondary); }
```

### Code block

```css
.code-block {
  background: var(--elevated);
  border-radius: 6px;
  padding: 10px 14px;
  font:700 13px/1.5 'JetBrains Mono',monospace;
  letter-spacing: 0.02em;
}
.code-prefix { color:var(--text-secondary); font-weight:400; }
.code-cmd    { color:var(--accent-1); }
```

## Layout rules

```
canvas-structure:  bento-grid, 4-column, gap 14px, padding 0 28px 28px
hero (s1):         full-width transparent row, border-bottom only — NO card bg
                   flex-row: hero-brand left, kpis right
row 2 (s2,s3):     2-col split (half + half)
row 3 (s4-s7):     4-col equal
row 4 (s8-s11):    4-col equal
row 5 (s12,s13):   2-col split
footer:            full-width, border-top, 3-column flex, all text muted uppercase
```

The hero row must have NO card background — it sits directly on the canvas.

## Style verification checklist

- [ ] Canvas is `#060D0A` — must have green cast, never pure black
- [ ] Every non-hero card has a gradient border (standard or focal version)
- [ ] Hero row has no card background
- [ ] Three fonts loaded: Bebas Neue, Montserrat, JetBrains Mono
- [ ] Gradient text on: hero title, card numbers, big stats
- [ ] No Inter font used anywhere

## Forbidden

No pure black canvas. No third accent color. No card without gradient border (except the hero row). No Inter font. No border-radius above 10px on cards, 6px on pills. No hero card background.
