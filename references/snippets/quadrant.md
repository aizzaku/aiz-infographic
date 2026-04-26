# Quadrant (2×2) Snippet

Two-axis matrix with 4 labeled cells. The "consultant special" — positioning, strategy, risk profile. One cell is focal; the other three are referenced.

## When to use

- Positioning map ("speed × safety", "cost × scale", "yield × risk")
- Strategy classification (2×2 against two axes)
- Portfolio breakdown (BCG growth × share)
- Risk register (likelihood × impact)

## When NOT to use

- > 4 real categories → use `comparison` or `grid-cards`.
- Categorical axes (not continuous/polar) → it's a table, use `comparison`.
- Plotting many items inside cells → use scatter chart inside `statistical`.

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| poster | centerpiece | Best — quadrant wants square space + focal hierarchy |
| bento-box | card-tall (square) | Compact 2×2 |
| editorial | body-column | Inline figure |

## Required elements

`text.md`, `layout.md`, `decorative.md`, `connectors.md` (axis arrows). Optional `data-widgets.md`, `annotation.md`.

## HTML pattern

```html
<div class="quadrant">
  <span class="q-y-label">{y-axis high →}</span>
  <span class="q-x-label">{x-axis high →}</span>

  <div class="q-axis q-axis-y"></div>
  <div class="q-axis q-axis-x"></div>

  <div class="q-cell q-cell-tl role-secondary">
    <h3 class="q-cell-title">Niche specialists</h3>
    <p class="body">Short descriptor.</p>
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
.q-axis { position: absolute; background: color-mix(in srgb, var(--text-muted) 60%, transparent); }
.q-axis-x { left: 48px; right: 0; bottom: 24px; height: 1px; }
.q-axis-y { left: 48px; top: 0; bottom: 24px; width: 1px; }
.q-axis-x::after, .q-axis-y::after {
  content: ''; position: absolute; border: 4px solid transparent;
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
.q-x-label, .q-y-label {
  position: absolute;
  font: 700 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--text-muted);
}
.q-x-label { right: 8px; bottom: 4px; }
.q-y-label { left: 32px; top: 4px; transform: rotate(-90deg); transform-origin: left top; }
.q-cell { padding: 20px; display: flex; flex-direction: column; gap: 8px; }
.q-cell-title {
  font: 700 14px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.05em;
  color: var(--text-primary);
  margin: 0;
}
</style>
```

## Composition rules

- One `.role-focal` cell per quadrant. The other three are `.role-primary` or `.role-secondary`. Never two focals.
- Axis labels: one short phrase each. "High yield", "High risk" — not full sentences.
- Never use arrow glyphs in label text (the axis line carries the arrow).
- 4px grid alignment.
- If cells need more than 2 sentences of detail, promote to a strip below the matrix — don't cram inside cells.

## Anti-patterns

- Color-coding all four cells differently — use roles, not a 4-color palette.
- Tilting / isometric projection — flat, rectangular, clean.
- Tiny charts inside cells (limit: 1 KPI + descriptor; more → use `dashboard`).
- Quadrant when axes have no natural high/low gradient — that's `comparison`.
