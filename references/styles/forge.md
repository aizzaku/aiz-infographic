# forge — Industrial Smelting Style

Concept: Industrial smelting floor. Data is a batch report from a furnace. Dense, compressed, zero waste.

> **Font-rule override.** This style uses 1 font (JetBrains Mono only), overriding the SKILL.md "2 fonts default." Industrial batch reports are monospace top-to-bottom — units, values, timestamps all share the same face. Adding a body font softens the dense-data identity.

## When to use

- Industrial data, manufacturing metrics
- Batch processing / pipeline reports
- Dense financial or operational dashboards
- Protocol yield and throughput metrics
- Any content that benefits from a heavy, compressed, no-whitespace aesthetic

## CSS variables

```css
:root {
  /* canvas */
  --canvas:        #0F0A04;   /* warm brown-black */
  --panel:         #150D05;
  --elevated:      #1C1205;

  /* text */
  --text-primary:   #F0A050;  /* primary values — amber */
  --text-secondary: #C06010;  /* labels */
  --text-muted:     #6B4A20;  /* metadata */
  --on-accent:      #0F0A04;

  /* accent */
  --accent-1: #E07B20;        /* ember orange — active values and yield metrics */
  --accent-2: #E07B20;        /* single accent, no pair rotation in this theme */

  /* borders */
  --border: #2A1800;

  /* semantic */
  --positive: #8BC34A;        /* yield up, nominal */
  --negative: #D84315;        /* critical, failure */

  /* dim structural */
  --dim: #3A1800;

  /* spacing — compressed, no whitespace decoration */
  --gap-section:   16px;
  --gap-element:   8px;
  --gap-card:      4px;
  --pad-container: 12px;

  /* radius — none */
  --radius-card:  0px;
  --radius-pill:  0px;
  --radius-btn:   0px;
}
```

## Typography

Monospace only. Compressed line-height. Units always attached to values.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap">
```

| Role | Weight | Case | Size | Line-height |
|------|--------|------|------|-------------|
| Batch header / title | 700 | UPPERCASE | 16-20px | 1.2 |
| Item label | 700 | UPPERCASE | 11-12px | 1.2 |
| Value | 400 | as-is | 14-16px | 1.2 |
| Metadata | 400 | as-is | 10-11px | 1.2 |

Units always abbreviated and attached: `1,420C`, `68% YIELD`, `284 atm`.

## Layout rules

### Dense grid (primary structure)

Two-column key/value layout as the default unit. No whitespace as decoration.

```html
<div class="forge-batch">
  <div class="forge-header">
    <span class="forge-id">BATCH-2047</span>
    <span class="forge-temp">1,420C</span>
    <span class="forge-pressure">284 atm</span>
    <span class="forge-status badge-pill badge-active">NOMINAL</span>
  </div>
  <div class="forge-divider">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</div>
  <div class="forge-rows">
    <div class="forge-row">
      <span class="forge-key">RUN TIME</span>
      <span class="forge-val">04:22:18</span>
    </div>
    <div class="forge-row">
      <span class="forge-key">YIELD</span>
      <span class="forge-val">68%</span>
    </div>
    <div class="forge-row">
      <span class="forge-key">OUTPUT</span>
      <span class="forge-val">2,840 kg</span>
    </div>
  </div>
</div>

<style>
.forge-batch {
  background: var(--panel, #150D05);
  border: 1px solid var(--border, #2A1800);
  border-radius: 0;
  padding: 12px;
  font-family: 'JetBrains Mono', monospace;
}

.forge-header {
  display: flex;
  gap: 16px;
  align-items: center;
  margin-bottom: 6px;
}

.forge-id {
  font: 700 12px/1 monospace;
  color: var(--text-primary, #F0A050);
  letter-spacing: 0.04em;
}

.forge-temp, .forge-pressure {
  font: 400 11px/1 monospace;
  color: var(--text-secondary, #C06010);
}

.forge-divider {
  font: 400 10px/1 monospace;
  color: var(--dim, #3A1800);
  margin: 6px 0;
  letter-spacing: -0.02em;
}

.forge-rows { display: flex; flex-direction: column; gap: 4px; }

.forge-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 8px;
}

.forge-key {
  font: 700 11px/1.2 monospace;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-secondary, #C06010);
}

.forge-val {
  font: 400 13px/1 monospace;
  color: var(--text-primary, #F0A050);
  font-variant-numeric: tabular-nums;
  text-align: right;
}
</style>
```

### Yield / fill bars

No rounded ends. Flat rectangle. No gradient on fill. Use `flat-bar` from `progress-bars.md`.

For text-mode yield bars (like batch summary header):

```html
<div class="forge-yield-bar">
  <span class="forge-key">YIELD</span>
  <span class="forge-fill">[████████░░░░]</span>
  <span class="forge-val">68%</span>
</div>

<style>
.forge-yield-bar {
  display: flex;
  gap: 10px;
  align-items: center;
  font-family: monospace;
}
.forge-fill { color: var(--accent-1, #E07B20); letter-spacing: -0.02em; }
</style>
```

### Status labels

ALL CAPS in small-caps style. Use `status-pill` badge variant from `badges.md`.

```css
.badge-pill {
  font: 700 10px/1 monospace;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  border-radius: 0;    /* hard edge in forge */
}
```

## Decorative DNA

Hard rectangles only. No rounding anywhere. Dense column grids.

```css
/* All cards */
.card {
  background: var(--panel);
  border: 1px solid var(--border, #2A1800);
  border-radius: 0;
  padding: 12px;
}
```

No gradient borders. No glow. No glow. No icons (weight carried by data density).

## Gradient text

Disabled.

## Progress bar override

Use `flat-bar` variant from `progress-bars.md`. No rounded ends. Fill color: `var(--accent-1)` (#E07B20). No gradient.

## Badge override

Use `status-pill` variant. ALL CAPS, border-radius 0, monospace font.

## Step-connector override

Square badges, monospace labels, ember orange fill.

## Style verification checklist

- [ ] All borders use `#2A1800`, not generic dark colors
- [ ] No rounded corners anywhere
- [ ] Monospace only — no sans-serif, no serif
- [ ] Dense layout: `--gap-card: 4px`, `--pad-container: 12px`
- [ ] No gradients on fills or borders
- [ ] No icons
- [ ] Units attached to values (`1,420C`, `68%`, not `1420` and `°C`)

## What to avoid

Whitespace as decoration, rounded corners, soft colors, blue tones, any non-orange accent, gradients, icons, glow effects.
