# Swimlane Snippet

Process broken across multiple actors / systems. Horizontal lanes, one actor per lane, time flowing left → right. Use when handoffs matter as much as the steps.

## When to use

- Multi-party protocols (user → frontend → wallet → contract → oracle)
- Cross-functional processes (product → design → eng → QA → release)
- Request/response choreographies
- Token flows where multiple contracts interact

## When NOT to use

- Linear single-actor → use `process-flow`.
- Branching trees → use `flowchart`.
- Events without actors → use `timeline`/`roadmap`.
- > 6 lanes → split per-phase.

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| poster | centerpiece | Best — swimlanes need wide horizontal space |
| bento-box | card-wide (`1/-1`) | Compact 3-4 lane swimlane, full-bleed |
| dashboard | panel-large (w-12) | Process across the panel |

## Required elements

`connectors.md` (arrows + masked labels mandatory), `text.md`, `layout.md`, `decorative.md`, `icons.md`. Optional `data-widgets.md`, `annotation.md`.

## HTML pattern (grid + SVG handoff overlay)

```html
<div class="swimlane-section">
  <div class="swimlane">
    <div class="lane-header">User</div>
    <div class="lane-header">Frontend</div>
    <div class="lane-header">Contract</div>
    <div class="lane-header">Oracle</div>

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

  <!-- Handoff overlay -->
  <svg class="handoff-overlay" viewBox="0 0 800 400" preserveAspectRatio="none">
    <defs>
      <marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
        <path d="M0,0 L8,4 L0,8 z" fill="color-mix(in srgb, var(--accent-1) 60%, transparent)"/>
      </marker>
    </defs>
    <path d="M 180 40 L 220 120"
          stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)"
          stroke-width="1.5" fill="none" marker-end="url(#ah)"/>
    <g transform="translate(200, 80)">
      <rect x="-24" y="-8" width="48" height="14" rx="2" fill="var(--canvas)"/>
      <text x="0" y="3" text-anchor="middle"
            font-family="Montserrat" font-weight="700" font-size="9"
            letter-spacing="0.06em"
            fill="var(--text-secondary)">SIGNED TX</text>
    </g>
  </svg>
</div>

<style>
.swimlane-section { position: relative; }
.swimlane {
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: 12px;
}
.lane-header {
  padding: 12px;
  font: 700 12px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--text-secondary);
  border-right: 1px solid color-mix(in srgb, var(--text-muted) 30%, transparent);
  display: flex; align-items: center;
}
.lane-cells {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 80px;
  gap: 8px;
}
.lane-cell {
  padding: 12px;
  display: flex; gap: 8px; align-items: center;
  border-radius: var(--radius-card);
}
.lane-cell:empty { background: transparent; border: none; }
.lane-cell .step-num {
  flex: 0 0 auto;
  width: 28px; height: 28px;
  border-radius: 50%;
  background: color-mix(in srgb, var(--accent-1) 15%, var(--panel));
  color: var(--accent-1);
  font: 400 14px/28px 'Bebas Neue', sans-serif;
  text-align: center; letter-spacing: 0.04em;
}
.lane-cell .step-body {
  font: 400 12px/1.3 'Montserrat', sans-serif;
  color: var(--text-primary);
}
.handoff-overlay { position: absolute; inset: 0; pointer-events: none; }
</style>
```

## Composition rules

- Apply `.role-focal` to the **single** step representing the highest-coupling/risk handoff. Never two focals.
- Handoff arrows cross lane boundaries only. Arrows inside a lane are redundant with column order.
- Every handoff arrow is labeled with the payload ("SIGNED TX", "CLAIM PROOF", "APPROVAL"), not the action. Labels carry masking rects per `connectors.md`.
- External actors (oracles, third-party services, bridges) use `.role-external` (dashed border).
- Lane order = call order. User at top, then frontend, then contract, then downstream services.
- Density budget: ≤ 6 lanes, ≤ 8 time columns, ≤ 12 populated cells.
- 4px grid + pixel-locked: cell width and gap divisible by 4. Arrow endpoints land on cell edges.

## Anti-patterns

- Two actors in one lane → use `flowchart`.
- Drawing arrows between every time-adjacent cell — only actual handoffs get arrows.
- Encoding meaning in arrow color (all handoffs use the same accent at 60%).
- Omitting the actor column — without left-hand labels it's just a confusing flowchart.
