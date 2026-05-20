# openai-dark — Minimal Authority Style

Source: OpenAI 2025 rebrand — OpenAI Sans by ABC Dinamo, brand docs at openai.com/brand
Concept: Minimal authority. Near-black with a warm off-white cast. A single light tone against the dark field. Data as large, light-weight numerals. Communicates through restraint.

```
canvas-fit: [bento-box, editorial, poster, dashboard]
```

## When to use

- OpenAI product or model infographics
- Comparisons or analyses of OpenAI products (GPT, Sora, o-series)
- Any content explicitly requesting the OpenAI style
- Auto-selected when content is primarily about OpenAI models, products, or research

## CSS variables

```css
:root {
  /* canvas — near-black, no color cast */
  --canvas:        #0A0A0A;
  --panel:         #141414;   /* barely distinguishable from canvas */
  --elevated:      #1C1C1C;

  /* no accent color — this is structural */
  --accent-1:      #EBEBEB;   /* set to primary text to avoid broken color-mix calls */
  --accent-2:      #888888;
  --on-accent:     #0A0A0A;

  /* text */
  --text-primary:   #EBEBEB;
  --text-secondary: #888888;
  --text-muted:     #444444;

  /* borders */
  --border-default: rgba(255,255,255,0.08);
  --border-subtle:  rgba(255,255,255,0.04);

  /* semantic */
  --positive: #EBEBEB;  /* no green in this style — use weight instead */
  --negative: #888888;

  /* spacing — generous */
  --gap-section:   48px;
  --gap-element:   24px;
  --gap-card:      16px;
  --pad-container: 32px;

  /* radius */
  --radius-card:  8px;
  --radius-pill:  4px;
  --radius-btn:   4px;
}
```

## Typography

One font throughout. OpenAI Sans falls back to Inter — load Inter as the web font.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap">
```

| Role | Font | Weight | Case | Size | Notes |
|------|------|--------|------|------|-------|
| Hero numeral | Inter | 300 | as-is | 48-72px | letter-spacing -0.03em — the signature |
| Section label | Inter | 500 | UPPERCASE | 11px | letter-spacing 0.12em, text-secondary |
| Card title | Inter | 500 | UPPERCASE | 13-15px | letter-spacing 0.08em |
| Body | Inter | 400 | Sentence | 14px | line-height 1.6 |
| Metadata | Inter | 400 | Sentence | 11px | text-muted, letter-spacing 0.04em |

**Weight 300 only for display type.** Never bold or heavy for large numerals. This is the defining rule.

## Decorative DNA

### Hero numerics (primary visual element)

```css
.hero-numeral {
  font: 300 64px/1 'Inter', system-ui, sans-serif;
  letter-spacing: -0.03em;
  color: var(--text-primary);
  font-variant-numeric: tabular-nums;
}
```

This is the ONLY visual emphasis — no color, no glow, no gradient. The number IS the graphic.

### Section dividers (only decoration permitted)

```css
.section-divider {
  border: none;
  border-top: 0.5px solid rgba(255,255,255,0.08);
  margin: 0;
}
```

### Cards

```css
.card {
  background: var(--panel);
  border: 0.5px solid rgba(255,255,255,0.08);
  border-radius: var(--radius-card, 8px);
  padding: 24px;
}
```

No gradient borders. No glow. No shadow. Minimal surface distinction.

### Labels

```css
.label-above {
  font: 500 11px/1 'Inter', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--text-secondary);
  margin-bottom: 4px;
}
```

Labels always appear ABOVE the value, never below.

### Icons

Functional only: Phosphor Bold, 16px, `var(--text-secondary)`. No decorative icons.

## Layout rules

```
alignment:   left-aligned, no centering
hero:        large number (weight 300) + small label below — number IS the graphic
sections:    separated by 0.5px hairlines, not spatial gaps
cards:       minimal — surface bg, 0.5px border-default, max 8px radius
spacing:     generous — negative space does the heavy lifting
grid:        max 3-col; OpenAI layouts breathe, never dense
```

## Gradient text

Disabled entirely. No gradient text anywhere.

## Style verification checklist

- [ ] No accent color used — `--accent-1` only called inside CSS formulas, never for pure color emphasis
- [ ] Display numerals at weight 300 — never 700 or 900
- [ ] Dividers are 0.5px hairlines — not gaps alone
- [ ] Generous spacing: `--gap-section: 48px`
- [ ] Max 3 columns
- [ ] No glow, shadow, or gradient anywhere

## Forbidden

No accent color whatsoever. No gradient text. No glow, bloom, or shadow. No bold weight (700+) for display numerals (300 only). No border-radius above 8px. No colored card backgrounds — surface tint only. No decorative elements.
