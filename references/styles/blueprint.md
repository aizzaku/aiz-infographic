# blueprint — Engineering Schematic Style

Concept: Engineering schematic. Every element is a technical drawing. Data lives in annotation marks and dimensions.

## When to use

- Technical architecture diagrams
- Protocol specs and internals
- Engineering-focused content
- Standards / RFC-style visuals
- System diagrams with components, relationships, and measurements

## CSS variables

```css
:root {
  /* canvas */
  --canvas:        #0A1628;   /* deep engineering navy */
  --panel:         #0D1E38;   /* slightly lighter navy */
  --elevated:      #0F2545;

  /* lines */
  --line-structure: #1E3A5F;  /* structural lines */
  --line-active:    #5B9BD5;  /* highlighted / active lines */

  /* text */
  --text-primary:   #8AB4D4;  /* primary labels */
  --text-secondary: #4A7FA0;  /* secondary labels */
  --text-muted:     #1E3A5F;  /* dim / tertiary */
  --on-accent:      #0A1628;

  /* accent — blue line work only */
  --accent-1: #5B9BD5;
  --accent-2: #8AB4D4;

  /* semantic */
  --positive: #4A9B6E;
  --negative: #9B4A4A;

  /* spacing */
  --gap-section:   32px;
  --gap-element:   16px;
  --gap-card:      12px;
  --pad-container: 24px;

  /* radius — none */
  --radius-card:  0px;
  --radius-pill:  0px;
  --radius-btn:   0px;
}
```

## Typography

Monospace for all labels, codes, and dimensions. Small-caps for section headers. ALL CAPS for node and component names.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap">
```

| Role | Weight | Case | Size |
|------|--------|------|------|
| Hero title / drawing title | 700 | ALL CAPS | 20-28px |
| Section header | 700 | SMALL-CAPS | 13-16px |
| Node / component name | 700 | ALL CAPS | 12-14px |
| Label / dimension | 400 | as-is | 11-13px |
| Reference / code | 400 | as-is | 10-11px |

No serif, no decorative fonts. Letter-spacing: 0 for monospace (handled automatically).

## Layout rules

### Grid overlay (signature)

Faint 8px or 16px grid on the canvas background:

```css
.infographic-canvas {
  background-image:
    linear-gradient(color-mix(in srgb, var(--line-active) 4%, transparent) 1px, transparent 1px),
    linear-gradient(90deg, color-mix(in srgb, var(--line-active) 4%, transparent) 1px, transparent 1px);
  background-size: 16px 16px;
  background-color: var(--canvas);
}
```

### Shapes: outlines only

No fills anywhere. All shapes are outlines at 0.5-1px.

```css
.bp-node {
  background: transparent;
  border: 1px solid var(--line-structure, #1E3A5F);
  border-radius: 0;
  padding: 12px 16px;
}
.bp-node-active {
  border-color: var(--line-active, #5B9BD5);
}
```

### Reference numbers

```html
<span class="bp-ref">[REF-001]</span>
<span class="bp-ref">[DWG-A4]</span>

<style>
.bp-ref {
  font: 400 10px/1 'JetBrains Mono', monospace;
  color: var(--text-secondary, #4A7FA0);
  letter-spacing: 0.04em;
}
</style>
```

### Dimension annotations

```html
<div class="bp-dim">
  <span class="bp-dim-line">--- 240px ---</span>
</div>

<style>
.bp-dim-line {
  font: 400 10px/1 'JetBrains Mono', monospace;
  color: var(--text-secondary, #4A7FA0);
  letter-spacing: 0.04em;
}
</style>
```

### Crosshairs at key nodes

```html
<span class="bp-crosshair">+</span>
<!-- or use Unicode: ⊕ for filled crosshair -->

<style>
.bp-crosshair {
  color: var(--line-active, #5B9BD5);
  font: 700 14px/1 'JetBrains Mono', monospace;
}
</style>
```

### Grid coordinates

Margin labels (column A-F, row 1-6):

```html
<div class="bp-coord-label">A3</div>
<style>
.bp-coord-label {
  font: 400 9px/1 'JetBrains Mono', monospace;
  color: var(--text-muted, #1E3A5F);
  letter-spacing: 0.06em;
}
</style>
```

### Title block

Bottom of the canvas, always present:

```html
<div class="bp-title-block">
  <span class="bp-tb-project">PROTOCOL ARCHITECTURE</span>
  <span class="bp-tb-num">DWG-001</span>
  <span class="bp-tb-date">2026-05-20</span>
  <span class="bp-tb-rev">REV A</span>
</div>

<style>
.bp-title-block {
  display: grid;
  grid-template-columns: 1fr auto auto auto;
  gap: 16px;
  border-top: 1px solid var(--line-structure, #1E3A5F);
  padding: 8px 0 4px;
  font: 400 10px/1 'JetBrains Mono', monospace;
  color: var(--text-secondary, #4A7FA0);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.bp-tb-project { color: var(--text-primary, #8AB4D4); }
</style>
```

### Annotation leaders

Thin dashed lines from label to element, for callouts:

```css
.bp-annotation {
  border: 1px dashed color-mix(in srgb, var(--line-active) 50%, transparent);
  padding: 6px 10px;
  font: 400 10px/1.4 'JetBrains Mono', monospace;
  color: var(--text-secondary);
}
```

### Dashed lines for secondary components

```css
.bp-secondary {
  border-style: dashed;
  border-width: 1px;
  border-color: var(--line-structure, #1E3A5F);
}
```

## Decorative DNA

No fills, no gradients, no glow, no rounded corners, no icons, no color beyond the blue ramp.

No glow:

```css
.hero-title { text-shadow: none; }
.kpi-card   { box-shadow: none; }
```

## Gradient text

Disabled. All text is flat from the blue ramp (`--text-primary`, `--text-secondary`, `--text-muted`).

## Badge override

Use `status-pill` variant from `badges.md` with 0 border-radius and monospace font. Reference-style text: `[NOMINAL]`, `[CRITICAL]`.

## Step-connector override

Square badges (outline only, no fill), `--line-active` border, monospace step numbers.

## Style verification checklist

- [ ] Canvas has grid overlay at 16px intervals
- [ ] All shapes outline-only (no fills, `background: transparent`)
- [ ] 0.5-1px lines only — no thick borders
- [ ] Monospace exclusively
- [ ] Reference numbers on key elements: `[REF-xxx]`
- [ ] Title block at canvas bottom
- [ ] No color beyond the blue ramp
- [ ] No rounded corners

## When NOT to use

- Marketing / consumer-facing content — use aizfographics-style
- Gaming / playful content — use retro
- Corporate reports — use corporate or ash
