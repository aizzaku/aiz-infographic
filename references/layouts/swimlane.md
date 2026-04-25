# Swimlane Layout

A process broken across **multiple actors / systems**, where the story is not just "what happens" but "who does what, when, and what hands off to whom". Horizontal lanes, one actor per lane, time flowing left → right. A sibling of `process-flow` — use when the handoffs matter as much as the steps.

## When to use

- Multi-party protocols (user → frontend → wallet → contract → oracle → …)
- Cross-functional processes (product → design → eng → QA → release)
- Request/response choreographies
- Token flows where multiple contracts interact

## When NOT to use

- Linear single-actor processes → use `process-flow`.
- Branching decision trees → use `flowchart`.
- Timelines with no actors, just events → use `timeline` or `roadmap`.
- More than 6 lanes → swimlanes stop being readable; pivot to a sequence diagram or pair of swimlanes per-phase.

## Required elements

`connectors.md` (arrows + masked labels are mandatory), `text.md`, `layout.md`, `decorative.md`, `icons.md`, optionally `data-widgets.md`, `annotation.md` for callouts on the handoff step.

## Section order

```
┌───────────────────────────────────┐
│ Header strip                      │
├───────────────────────────────────┤
│ Hero section                      │
├───────────────────────────────────┤
│ Optional: actor legend            │  who each lane is
├───────────────────────────────────┤
│ Swimlane grid                     │  N lanes × K time columns
├───────────────────────────────────┤
│ Legend strip (node roles)         │
├───────────────────────────────────┤
│ Footer                            │
└───────────────────────────────────┘
```

## Grid structure

One row per actor, one column per time step (or aligned step group). Handoffs are arrows that cross row boundaries.

```html
<section class="section swimlane-section">
  <div class="swimlane">
    <!-- actor header column -->
    <div class="lane-header">User</div>
    <div class="lane-header">Frontend</div>
    <div class="lane-header">Contract</div>
    <div class="lane-header">Oracle</div>

    <!-- grid: 4 lanes × 4 columns = 16 cells; lay out in row-major -->
    <div class="lane-cells">
      <!-- Row: User -->
      <div class="lane-cell role-primary">
        <div class="step-num">01</div>
        <div class="step-body">Initiate claim</div>
      </div>
      <div class="lane-cell"></div>
      <div class="lane-cell"></div>
      <div class="lane-cell"></div>

      <!-- Row: Frontend -->
      <div class="lane-cell"></div>
      <div class="lane-cell role-primary">
        <div class="step-num">02</div>
        <div class="step-body">Sign + send tx</div>
      </div>
      <div class="lane-cell"></div>
      <div class="lane-cell"></div>

      <!-- Row: Contract -->
      <div class="lane-cell"></div>
      <div class="lane-cell"></div>
      <div class="lane-cell role-focal">
        <div class="step-num">03</div>
        <div class="step-body">Verify eligibility</div>
      </div>
      <div class="lane-cell"></div>

      <!-- Row: Oracle -->
      <div class="lane-cell"></div>
      <div class="lane-cell"></div>
      <div class="lane-cell"></div>
      <div class="lane-cell role-external">
        <div class="step-num">04</div>
        <div class="step-body">Provide proof</div>
      </div>
    </div>
  </div>
</section>

<style>
.swimlane {
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: 12px;
}
.lane-header {
  padding: 12px;
  font: 700 12px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-secondary);
  border-right: 1px solid color-mix(in srgb, var(--text-muted) 30%, transparent);
  display: flex;
  align-items: center;
}
.lane-cells {
  display: grid;
  grid-template-columns: repeat(4, 1fr);  /* K time columns */
  grid-auto-rows: 80px;
  gap: 8px;
}
.lane-cell {
  padding: 12px;
  display: flex;
  gap: 8px;
  align-items: center;
  border-radius: var(--radius-card);
}
.lane-cell:empty {
  background: transparent;
  border: none;
}
.lane-cell .step-num {
  flex: 0 0 auto;
  width: 28px; height: 28px;
  border-radius: 50%;
  background: color-mix(in srgb, var(--accent-1) 15%, var(--panel));
  color: var(--accent-1);
  font: 400 14px/28px 'Bebas Neue', sans-serif;
  text-align: center;
  letter-spacing: 0.04em;
}
.lane-cell .step-body {
  font: 400 12px/1.3 'Montserrat', sans-serif;
  color: var(--text-primary);
}
</style>
```

Overlay handoff arrows as an SVG absolutely positioned on top of `.lane-cells`, with each arrow's label using the masking pattern from `connectors.md`:

```html
<svg class="handoff-overlay" viewBox="0 0 800 400" preserveAspectRatio="none">
  <path d="M 180 40 L 220 120"
        stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)"
        stroke-width="1.5"
        fill="none"
        marker-end="url(#ah)"/>
  <g transform="translate(200, 80)">
    <rect x="-24" y="-8" width="48" height="14" rx="2" fill="var(--canvas)"/>
    <text x="0" y="3" text-anchor="middle"
          font-family="Montserrat" font-weight="700" font-size="9"
          letter-spacing="0.06em"
          fill="var(--text-secondary)">SIGNED TX</text>
  </g>
  <defs>
    <marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z"
            fill="color-mix(in srgb, var(--accent-1) 60%, transparent)"/>
    </marker>
  </defs>
</svg>

<style>
.handoff-overlay {
  position: absolute;
  inset: 0;
  pointer-events: none;
}
.swimlane-section { position: relative; }
</style>
```

## Composition rules

- **Coral the handoff, not the step.** Apply `.role-focal` to the single step/cell representing the handoff that introduces the most coupling, latency, or failure risk — the one the viewer most needs to internalize. Do NOT focal every row's terminal step. One focal per diagram.
- **Handoff arrows cross lane boundaries only.** Arrows inside a lane are redundant with column order — time already flows left→right.
- **Every handoff arrow is labeled.** The label describes the payload ("SIGNED TX", "CLAIM PROOF", "APPROVAL"), not the action. Labels carry masking rects per `connectors.md`.
- **External actors use `.role-external`.** Oracles, third-party services, bridges. Dashed border signals "out of our control" without needing a separate legend for it.
- **Lane order = call order** where possible. User at top, then frontend, then contract, then downstream services — reading order mirrors request flow.
- **Density budget**: ≤ 6 lanes, ≤ 8 time columns, ≤ 12 populated cells. Past that, the lanes stop being readable — split into phases.
- **4px grid**: cell width and gap divisible by 4. Arrow endpoints land on cell edges, not cell interiors (otherwise the handoff looks mid-step).

## Anti-patterns

- Don't stack two actors in one lane. One lane, one actor — else use `flowchart`.
- Don't draw arrows between every pair of cells in time-adjacent columns. Only draw arrows for actual handoffs. Implicit continuation within a lane is visible from column position.
- Don't use arrow color to encode anything. All handoff arrows are the same accent at 60% (see `connectors.md`). Encoding via roles goes on the *cells*, not the arrows.
- Don't omit the actor column. A grid of cells with no left-hand labels is just a flowchart — and a confusing one.
