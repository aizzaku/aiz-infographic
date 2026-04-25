# Layout — Grid, Containers, Sections

Structural atoms. CSS Grid + Flexbox. Works with any style.

## Canvas wrapper

Every infographic lives inside `.infographic-canvas`:

```html
<div class="infographic-canvas">
  <section class="hero">…</section>
  <section class="body-section">…</section>
  …
  <footer class="footer">…</footer>
</div>
```

```css
.infographic-canvas {
  width: 100%;
  max-width: 1080px;
  aspect-ratio: 3 / 4;      /* override per dimension preset */
  margin: 0 auto;
  padding: var(--pad-container);
  background: var(--canvas);
  color: var(--text-primary);
  font-family: 'Montserrat', sans-serif;
  display: flex;
  flex-direction: column;
  gap: var(--gap-section);
  box-sizing: border-box;
}
```

Aspect ratios per preset:

```css
.infographic-canvas.portrait-tall   { aspect-ratio: 9 / 16; }
.infographic-canvas.portrait-medium { aspect-ratio: 3 / 4;  }
.infographic-canvas.landscape       { aspect-ratio: 16 / 9; }
.infographic-canvas.square          { aspect-ratio: 1 / 1;  }
```

## Section containers

```css
.section {
  display: flex;
  flex-direction: column;
  gap: var(--gap-element);
}

.section-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: var(--gap-element);
  padding-bottom: 8px;
  border-bottom: 1px solid color-mix(in srgb, var(--text-primary) 8%, transparent);
}
```

## Grid recipes

### 1-column (stacked)

```css
.grid-1 { display: grid; grid-template-columns: 1fr; gap: var(--gap-card); }
```

### 2-column (equal)

```css
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--gap-card);
}
```

### 2-column (asymmetric 60/40 or 66/33)

```css
.grid-2-asym { display: grid; grid-template-columns: 2fr 1fr; gap: var(--gap-element); }
.grid-2-wide { display: grid; grid-template-columns: 3fr 2fr; gap: var(--gap-element); }
```

### 3-column

```css
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--gap-card); }
```

### Auto-fit (responsive density)

```css
.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--gap-card);
}
```

### Hero with sidebar

```css
.hero-with-side {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: var(--gap-element);
  align-items: center;
}
```

## KPI strip (3–6 equal cells)

```css
.kpi-strip {
  display: grid;
  grid-template-columns: repeat(var(--kpi-count, 4), 1fr);
  gap: var(--gap-card);
}
```

Set `--kpi-count` inline: `style="--kpi-count: 3"`.

## Section dividers

Solid thin line (solid-line is 90% of DNA):

```css
.divider {
  height: 1px;
  background: color-mix(in srgb, var(--text-primary) 8%, transparent);
  margin: 0;
}
```

Accent-tinted:
```css
.divider-accent {
  height: 1px;
  background: linear-gradient(90deg,
    transparent,
    color-mix(in srgb, var(--accent-1) 40%, transparent),
    transparent);
}
```

## Legend strip

A horizontal row of colored/dashed swatches + labels that explains a color encoding, node-role mapping, or chart series. Always placed at the **bottom** of the section it belongs to — separated by a hairline divider, never floating inside the visualization, never above the content.

### Pattern

```html
<section class="section">
  <h2 class="section-title">Protocol flow</h2>
  <!-- …visualization… -->

  <div class="legend-strip">
    <span class="legend-item">
      <span class="legend-swatch swatch-focal"></span>
      <span class="legend-label">Focal path</span>
    </span>
    <span class="legend-item">
      <span class="legend-swatch swatch-primary"></span>
      <span class="legend-label">Primary nodes</span>
    </span>
    <span class="legend-item">
      <span class="legend-swatch swatch-external"></span>
      <span class="legend-label">External / upstream</span>
    </span>
    <span class="legend-item">
      <span class="legend-swatch swatch-optional"></span>
      <span class="legend-label">Optional</span>
    </span>
  </div>
</section>

<style>
.legend-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 16px 24px;
  padding-top: 12px;
  margin-top: 12px;
  border-top: 1px solid color-mix(in srgb, var(--text-muted) 30%, transparent);
}
.legend-item {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.legend-swatch {
  width: 16px; height: 12px;
  border-radius: 2px;
  display: inline-block;
}
.legend-label {
  font: 700 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-secondary);
}

/* Swatches mirror the role classes in data-widgets.md */
.swatch-focal {
  background:
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 30%, transparent),
      color-mix(in srgb, var(--accent-1) 50%, transparent));
  border: 1px solid color-mix(in srgb, var(--accent-1) 50%, transparent);
}
.swatch-primary {
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--accent-1) 40%, transparent);
}
.swatch-secondary {
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--text-muted) 40%, transparent);
}
.swatch-external {
  background: transparent;
  border: 1px dashed color-mix(in srgb, var(--text-muted) 60%, transparent);
}
.swatch-optional {
  background: color-mix(in srgb, var(--panel) 60%, transparent);
  border: 1px dashed color-mix(in srgb, var(--accent-1) 40%, transparent);
}
.swatch-positive {
  background: color-mix(in srgb, var(--positive) 12%, var(--panel));
  border: 1px solid color-mix(in srgb, var(--positive) 50%, transparent);
}
.swatch-negative {
  background: color-mix(in srgb, var(--negative) 12%, var(--panel));
  border: 1px solid color-mix(in srgb, var(--negative) 50%, transparent);
}
</style>
```

### Rules

- **Bottom only.** Never at the top of a section. Legends answer "what did I just see"; they don't prime the viewer.
- **Separated by a hairline divider** using `--text-muted` at 30% — never an accent-colored divider (that competes).
- **Only render when needed.** If every color is self-explanatory (e.g. the only accent is the hero title), no legend. Don't pad sections with a legend for its own sake.
- **Label style**: Montserrat 700, 10px, uppercase, `--text-secondary`. Same family used for badges.
- **Swatch shape**: 16 × 12 rectangle with 2px radius. Never circles (circles read as status dots, not swatches) and never full-width pills.
- **Order**: most-important → least-important, matching reading order of the visualization above.

## Rules

- Never use absolute positioning for core layout. Use grid/flex.
- Every section is a flex column with `gap: var(--gap-element)`.
- Don't nest more than 3 levels of grid. Flatten with utility classes instead.
- For asymmetric balance, prefer 2-col asymmetric over 3-col symmetric.
- When a section uses color-coded nodes/roles, place a legend strip at its bottom (see "Legend strip" above).
