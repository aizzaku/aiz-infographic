# blueprint — Technical Style

Architectural-blueprint feel. Monochrome cyan-on-dark-blue, technical diagram aesthetic. Evokes precision, engineering, specs.

## When to use

- Technical architecture diagrams
- Protocol specs and internals
- Engineering-focused content
- Standards / RFC-style visuals

## CSS variables

```css
:root {
  --canvas:        #0A1628;
  --panel:         #0F1F38;
  --elevated:      #16294A;

  --text-primary:   #D4E9FF;
  --text-secondary: #8AB0D4;
  --text-muted:     #4A6B8E;
  --on-accent:      #0A1628;

  --accent-1: #42D4F4;
  --accent-2: #42D4F4;

  --positive: #00D018;
  --negative: #FF5555;

  --gap-section: 32px;
  --gap-element: 18px;
  --gap-card:    14px;
  --pad-container: 28px;

  --radius-card: 2px;
  --radius-pill: 2px;
  --radius-btn:  2px;
}
```

## Typography

### Pair: JetBrains Mono + Inter

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | JetBrains Mono | 700 | UPPERCASE | 48–60px |
| Section title | JetBrains Mono | 700 | UPPERCASE | 18–22px |
| Card title | Inter | 700 | UPPERCASE | 14–16px |
| Body | Inter | 400 | Sentence | 13–15px |
| Caption / spec code | JetBrains Mono | 400 | Sentence / code | 11–12px |

## Gradient text

Disabled — blueprint style uses flat `--accent-1` for all emphasis.

## Decorative DNA

### Borders

1px solid `--accent-1` at 40% opacity. Sharp corners (2px radius). No gradient borders — blueprint is about crisp lines.

```css
.card {
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--accent-1) 40%, transparent);
  border-radius: 2px;
}
```

### Grid lines (signature)

Faint cyan grid overlay on background — the canonical blueprint look:

```css
.infographic-canvas {
  background-image:
    linear-gradient(color-mix(in srgb, var(--accent-1) 6%, transparent) 1px, transparent 1px),
    linear-gradient(90deg, color-mix(in srgb, var(--accent-1) 6%, transparent) 1px, transparent 1px);
  background-size: 40px 40px;
  background-color: var(--canvas);
}
```

### Callouts

Dashed outlines for "notes" or annotations:

```css
.annotation {
  border: 1px dashed color-mix(in srgb, var(--accent-1) 50%, transparent);
  padding: 8px 12px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--text-secondary);
}
```

### No glow

```css
.hero-title { text-shadow: none; }
.kpi-card   { box-shadow: none; }
```

Precision doesn't glow.

## Component DNA

- **Hero**: boxed, left-aligned, with measurement-style tick marks on the top edge (optional).
- **Badges**: rectangular, not pill. 2px radius.
- **Cards**: outlined only. Crosshair corners (optional — small `+` marks at each corner).
- **Connectors**: straight, thin, 1px, with dashed variants for "logical" vs "physical" relationships.

## When to use

- Specs, technical architecture
- Protocol internals
- Engineering diagrams
- "Under the hood" explainers

## When NOT to use

- Marketing / consumer-facing content → use aizfographics-style
- Gaming / playful content → use aizfographics-style or retro
- Corporate reports → use corporate style
