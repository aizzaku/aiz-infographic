# Connectors — Arrows, Timelines, Flow Paths

Straight arrows default (87% of DNA). Curved only for flows that need it. Timeline spines horizontal by default (88%).

## Straight arrow (inline)

```html
<span class="arrow-h"></span>

<style>
.arrow-h {
  display: inline-block;
  width: 32px;
  height: 10px;
  position: relative;
  color: color-mix(in srgb, var(--accent-1) 60%, transparent);
}
.arrow-h::before {
  content: '';
  position: absolute;
  left: 0; top: 50%;
  width: 100%; height: 1px;
  background: currentColor;
  transform: translateY(-50%);
}
.arrow-h::after {
  content: '';
  position: absolute;
  right: 0; top: 50%;
  border: 5px solid transparent;
  border-left-color: currentColor;
  transform: translateY(-50%);
}
</style>
```

Phosphor alternative for bolder flows: `<i class="ph-bold ph-arrow-right" style="color: var(--accent-1);"></i>`.

## Vertical arrow

Swap `arrow-h` → `arrow-v`, rotate the arrowhead 90°, use it between stacked cards.

## Step connector (for process-flow)

Between numbered steps:

```html
<div class="step">
  <div class="step-num">01</div>
  <div class="step-body">
    <h3 class="card-title">Stake</h3>
    <p class="body">Deposit tokens into the staking contract.</p>
  </div>
</div>
<div class="step-connector"></div>
<div class="step">…</div>

<style>
.step {
  display: grid;
  grid-template-columns: 48px 1fr;
  gap: 16px;
  align-items: start;
}
.step-num {
  width: 48px; height: 48px;
  border-radius: 50%;
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--accent-1) 40%, transparent);
  color: var(--accent-1);
  font: 400 22px/48px 'Bebas Neue', sans-serif;
  text-align: center;
  letter-spacing: 0.04em;
}
.step-connector {
  width: 1px;
  height: 24px;
  margin-left: 24px;
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--accent-1) 40%, transparent),
    transparent);
}
</style>
```

## Timeline spine (horizontal)

```html
<div class="timeline">
  <div class="timeline-spine"></div>
  <div class="timeline-nodes">
    <div class="tnode"><span class="tdot"></span><span class="tlabel">TGE</span><span class="tdate">Q3 2026</span></div>
    <div class="tnode"><span class="tdot"></span><span class="tlabel">Cliff ends</span><span class="tdate">+6mo</span></div>
    <div class="tnode"><span class="tdot"></span><span class="tlabel">25% unlocked</span><span class="tdate">+12mo</span></div>
    <div class="tnode"><span class="tdot"></span><span class="tlabel">100% unlocked</span><span class="tdate">+24mo</span></div>
  </div>
</div>

<style>
.timeline { position: relative; padding: 12px 0 20px; }
.timeline-spine {
  position: absolute;
  top: 22px; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg,
    transparent,
    color-mix(in srgb, var(--accent-1) 50%, transparent),
    transparent);
}
.timeline-nodes {
  display: flex;
  justify-content: space-between;
  position: relative;
}
.tnode { display: flex; flex-direction: column; align-items: center; gap: 6px; width: 80px; text-align: center; }
.tdot {
  width: 10px; height: 10px;
  border-radius: 50%;
  background: var(--accent-1);
  box-shadow: 0 0 12px color-mix(in srgb, var(--accent-1) 40%, transparent);
  margin-top: 18px;
}
.tlabel {
  font: 700 11px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.05em;
  color: var(--text-primary);
}
.tdate {
  font: 400 10px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
}
</style>
```

## Vertical timeline

Swap horizontal spine → vertical, stack nodes. Useful for roadmap layouts (phase 2).

## Curved flow arrow (SVG)

For circular or feedback loops:

```html
<svg width="200" height="120" viewBox="0 0 200 120">
  <path d="M 20 60 Q 100 10 180 60"
        fill="none"
        stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)"
        stroke-width="2"
        marker-end="url(#arrowhead)"/>
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="color-mix(in srgb, var(--accent-1) 60%, transparent)"/>
    </marker>
  </defs>
</svg>
```

## Arrow labels — always masked

When a label sits **on or near** a connector (arrow, flow path, timeline spine), it must carry an opaque background rect so the stroke doesn't bleed through the text. This is a hard rule in SVG and DOM contexts alike — no exceptions for "short labels" or "thin lines".

### SVG pattern

Render the masking rect first, then the text, inside a `<g>`:

```html
<g class="arrow-label" transform="translate(120, 60)">
  <rect x="-28" y="-10" width="56" height="18" rx="2"
        fill="var(--canvas)"/>
  <text x="0" y="4" text-anchor="middle"
        font-family="Montserrat" font-weight="700" font-size="10"
        letter-spacing="0.05em"
        fill="var(--text-secondary)">
    CLAIMS
  </text>
</g>
```

- `rect` width = text width + 8px horizontal padding (measure via `getBBox()` or estimate).
- `fill="var(--canvas)"` for top-level spines; use `var(--panel)` if the label sits over a panel.
- `rx="2"` keeps the rect square-ish; don't pill the mask — that reads as a badge.

### DOM pattern (inline arrow labels)

```html
<span class="arrow-label">Claims</span>

<style>
.arrow-label {
  position: relative;
  display: inline-block;
  padding: 2px 6px;
  background: var(--canvas);
  color: var(--text-secondary);
  font: 700 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  z-index: 1;
}
</style>
```

Use on labels that overlap a `.step-connector`, timeline spine, or flow path.

### When to skip the mask

Only when the label is clearly off the stroke — e.g. a timeline `.tlabel` that sits below the dot with 8+px clearance from the spine. If in doubt, mask it.

## Pixel-locked sections (cross-cell connectors)

Any section that draws arrows, leaders, or overlays that must align to specific cell edges (swimlane handoffs, flowchart edges, anatomical pointers, quadrant axis callouts, annotation leaders into the grid) MUST be laid out pixel-locked, not responsively. **Infographics are posters, not web pages — we do not care about fluid reflow.**

Rules:

- The enclosing section gets a fixed `width` and `height` in px.
- Children inside it use absolute `top/left/width/height` in px on a 4px grid.
- Any overlay SVG uses `viewBox="0 0 <W> <H>"` with `preserveAspectRatio="none"` and explicit `width="<W>" height="<H>"` matching the container 1:1 — so SVG user units map to container pixels directly.
- Arrow endpoints are hand-authored px coordinates that land on cell **edges** (not cell centers, not interiors).
- SVG `<marker refX="<markerWidth>">` so the arrowhead tip sits exactly at the path endpoint.
- Do NOT try to make the grid itself responsive with `1fr` / `minmax` / `aspect-ratio` when connectors are involved — arrow geometry and cell geometry will desync. Fluid reflow is reserved for sections that are purely flow-of-text or unordered card grids with no overlays.

To fit the infographic inside smaller viewports, wrap the whole canvas (or just the pixel-locked section) in a scaler:

```css
.poster-scale-wrap {
  transform-origin: top left;
  /* JS sets transform: scale(min(vw/W, vh/H, 1)) on load + resize */
}
```

Snippets that trigger pixel-lock: `flowchart`, `fishbone`, `swimlane`, `anatomical`, `quadrant`, plus `annotation` leaders pointing into a pixel-locked grid. Bento-box is **not** pixel-locked (fluid grid by design — see `canvases/bento-box.md`); poster canvases host pixel-locked centerpieces inside otherwise-fluid wrapping.

## Fan connector (title → many)

A single source title on one side splays out to N row-targets on the other side via short orthogonal stubs (vertical spine + horizontal arms). Pattern from a "category → sub-items" decomposition.

```html
<div class="fan">
  <div class="fan__source">
    <div class="card-title">Mechanism</div>
  </div>
  <div class="fan__spine"></div>
  <div class="fan__rows">
    <div class="fan__row">
      <div class="fan__arm"></div>
      <div class="fan__target">Acquisition</div>
      <span class="badge-num">01</span>
    </div>
    <div class="fan__row">
      <div class="fan__arm"></div>
      <div class="fan__target">Activation</div>
      <span class="badge-num">02</span>
    </div>
    <div class="fan__row">
      <div class="fan__arm"></div>
      <div class="fan__target">Retention</div>
      <span class="badge-num">03</span>
    </div>
    <div class="fan__row">
      <div class="fan__arm"></div>
      <div class="fan__target">Referral</div>
      <span class="badge-num">04</span>
    </div>
  </div>
</div>

<style>
.fan { display: grid; grid-template-columns: 160px 24px 1fr; gap: 0; align-items: stretch; }
.fan__source {
  display: flex; align-items: center; justify-content: flex-end;
  padding-right: 12px;
}
.fan__spine {
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--accent-1) 60%, transparent),
    var(--accent-1));
  width: 2px;
  justify-self: center;
}
.fan__rows { display: flex; flex-direction: column; gap: 12px; }
.fan__row {
  display: grid; grid-template-columns: 32px 1fr auto; gap: 12px;
  align-items: center;
  height: 48px;
}
.fan__arm {
  height: 2px;
  background: color-mix(in srgb, var(--accent-1) 60%, transparent);
}
.fan__target {
  padding: 0 16px;
  height: 100%;
  display: flex; align-items: center;
  background: var(--elevated);
  border: 1px solid color-mix(in srgb, var(--accent-1) 25%, transparent);
  border-radius: 4px;
  font: 700 14px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.05em;
}
</style>
```

**Variants:**
- Spine on the **left** (default, title on left → targets on right).
- Spine on the **right** (title on right → targets on left). Mirror the grid columns.
- With or without numbered badges. Use badges when sequence matters.

**Rules:**
- 3-7 target rows. Below 3 = not a fan, just use arrows. Above 7 = use a grid instead.
- Spine length spans only the rows it connects to — don't extend it past the first or last row.
- Arm length: 24-32px. Consistent across all rows.
- Source title is one phrase, max 3 words.

## Rules

- Connector color is 60% opacity accent OR `var(--text-secondary)`. Never full-opacity accent — it competes with content.
- Never use connectors decoratively. Every arrow must signify a real relationship.
- Straight > curved unless the flow genuinely loops.
- Timeline nodes always labeled. Dots alone are meaningless.
- Arrow/flow labels always carry an opaque masking rect (see "Arrow labels — always masked" above).
- Keep connector stroke widths at 1 or 2px (divisible by 1; the 4px grid applies to spacing, not stroke weight).
