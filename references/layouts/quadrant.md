# Quadrant (2×2) Layout

Two-axis matrix with 4 labeled cells. The "consultant special" — used to position competitors, strategies, risk profiles, or product archetypes along two dimensions. One cell is the focal quadrant; the other three are referenced.

## When to use

- Positioning map ("speed × safety", "cost × scale", "yield × risk")
- Strategy classification (2×2 of options against two axes)
- Portfolio breakdown (BCG-style growth × share)
- Risk register (likelihood × impact)

## When NOT to use

- You have > 4 real categories → use `comparison` or `grid-cards`.
- Axes are not genuinely continuous/polar — a 2×2 with categorical axes is just a table, use `comparison`.
- You need to plot many items inside the cells → that's a scatter plot, use `charts` in `statistical`.

## Required elements

`text.md`, `layout.md`, `decorative.md`, `connectors.md` (for axis arrows), optionally `data-widgets.md` for in-cell KPIs, `annotation.md` for margin callouts on one or two cells.

## Section order

```
┌───────────────────────────────────┐
│ Header strip                      │
├───────────────────────────────────┤
│ Hero section                      │
├───────────────────────────────────┤
│ Optional: axis definitions        │  what "high X" and "high Y" mean
├───────────────────────────────────┤
│                                   │
│     2×2 matrix with axis labels   │
│                                   │
├───────────────────────────────────┤
│ Cell detail strip (optional)      │  one short line per cell
├───────────────────────────────────┤
│ Legend strip (if roles used)      │
├───────────────────────────────────┤
│ Footer                            │
└───────────────────────────────────┘
```

## Matrix structure

```html
<section class="section quadrant-section">
  <div class="quadrant">
    <span class="q-y-label">{y-axis high →}</span>
    <span class="q-x-label">{x-axis high →}</span>

    <div class="q-axis q-axis-y"></div>
    <div class="q-axis q-axis-x"></div>

    <div class="q-cell q-cell-tl role-secondary">
      <h3 class="q-cell-title">Niche specialists</h3>
      <p class="body">Short descriptor of this quadrant.</p>
    </div>
    <div class="q-cell q-cell-tr role-focal">
      <h3 class="q-cell-title">Category leaders</h3>
      <p class="body">Short descriptor.</p>
    </div>
    <div class="q-cell q-cell-bl role-secondary">
      <h3 class="q-cell-title">Laggards</h3>
      <p class="body">Short descriptor.</p>
    </div>
    <div class="q-cell q-cell-br role-primary">
      <h3 class="q-cell-title">Fast followers</h3>
      <p class="body">Short descriptor.</p>
    </div>
  </div>
</section>

<style>
.quadrant {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 16px;
  padding: 32px 32px 32px 56px;
  min-height: 480px;
}

/* Axis lines — always 1px, text-muted 60%, arrow-headed */
.q-axis {
  position: absolute;
  background: color-mix(in srgb, var(--text-muted) 60%, transparent);
}
.q-axis-x {
  left: 48px; right: 0;
  bottom: 24px;
  height: 1px;
}
.q-axis-y {
  left: 48px;
  top: 0; bottom: 24px;
  width: 1px;
}
.q-axis-x::after,
.q-axis-y::after {
  content: '';
  position: absolute;
  border: 4px solid transparent;
}
.q-axis-x::after {
  right: -2px; top: 50%;
  border-left-color: color-mix(in srgb, var(--text-muted) 60%, transparent);
  transform: translateY(-50%);
}
.q-axis-y::after {
  left: 50%; top: -2px;
  border-bottom-color: color-mix(in srgb, var(--text-muted) 60%, transparent);
  transform: translateX(-50%);
}

/* Axis labels — one short phrase each, sentence case, muted */
.q-x-label,
.q-y-label {
  position: absolute;
  font: 700 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-muted);
}
.q-x-label {
  right: 8px;
  bottom: 4px;
}
.q-y-label {
  left: 32px;
  top: 4px;
  transform: rotate(-90deg);
  transform-origin: left top;
}

.q-cell {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.q-cell-title {
  font: 700 14px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-primary);
  margin: 0;
}
</style>
```

## Composition rules

- **One focal cell per quadrant.** Use `.role-focal` on the one cell that is the "answer" the infographic is pointing at. The other three are `.role-primary` or `.role-secondary`. Never two focal cells — the point of a 2×2 is that the viewer can see the winner.
- **Axis labels are one short phrase each.** "High yield", "High risk" — not "Higher expected annual percentage return". Montserrat 700, 10px, uppercase. Axes at the top-right (x) and top-left rotated (y).
- **Never use arrow glyphs in the label text.** The axis line carries the arrow; the label names the dimension. Writing `"High →"` is double-encoding.
- **Cells are 4px-grid aligned.** Padding 20px, gap 16px, title 14px — all divisible by 4.
- **Cell detail strip.** If each cell needs more than two sentences of supporting detail, promote the detail out into a strip below the matrix with one row per cell — don't cram it inside the cell.
- **Quadrant labels stay inside the cell.** Floating labels over grid lines look accidental.

## Anti-patterns

- Don't color-code all four cells differently — that's pie-chart logic, not 2×2 logic. Use roles, not a 4-color palette.
- Don't tilt the matrix or use isometric projection. Flat, rectangular, clean.
- Don't insert tiny charts inside cells. One KPI + short descriptor is the limit; anything more needs the `dashboard` layout.
- Don't use quadrant when the axes don't have a natural "high/low" orientation. "Red vs blue" on an axis is a category, not a gradient — use `comparison`.
