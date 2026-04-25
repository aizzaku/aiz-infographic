# Circular Flow Layout

Cyclical processes where output feeds back into input. The "flywheel" visualization — endless loop, no starting point, each step amplifies the next.

## When to use

- Token flywheels (emissions → rewards → activity → demand → emissions)
- Protocol feedback loops
- Economic cycles
- Community growth loops
- Habit / engagement loops

## Required elements

`connectors.md` (curved arrows), `text.md`, `layout.md`, `decorative.md`, `icons.md`, optionally `data-widgets.md`.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│      ↗  [Step 1]  ↘           │
│     [St4]       [St2]          │
│      ↖  [Step 3]  ↙           │
├──────────────────────────────┤
│ Central outcome (optional)   │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## HTML pattern (absolute-positioned nodes on a ring)

```html
<div class="cflow">
  <div class="cflow-ring">
    <svg viewBox="0 0 400 400" class="cflow-arrows">
      <defs>
        <marker id="cfarrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
          <path d="M0,0 L8,4 L0,8 z" fill="color-mix(in srgb, var(--accent-1) 60%, transparent)"/>
        </marker>
      </defs>
      <!-- curved arcs between nodes; adjust paths to ring radius -->
      <path d="M 260 80 A 140 140 0 0 1 320 200"
            stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)"
            stroke-width="2" fill="none" marker-end="url(#cfarrow)"/>
      <!-- 3 more arcs -->
    </svg>

    <div class="cnode" style="--x: 50%; --y: 10%;">
      <i class="ph-bold ph-coins"></i>
      <div class="cnode-title">Emissions</div>
    </div>
    <div class="cnode" style="--x: 90%; --y: 50%;">
      <i class="ph-bold ph-gift"></i>
      <div class="cnode-title">Rewards</div>
    </div>
    <div class="cnode" style="--x: 50%; --y: 90%;">
      <i class="ph-bold ph-lightning"></i>
      <div class="cnode-title">Activity</div>
    </div>
    <div class="cnode" style="--x: 10%; --y: 50%;">
      <i class="ph-bold ph-trend-up"></i>
      <div class="cnode-title">Demand</div>
    </div>

    <div class="cflow-center">
      <div class="cflow-center-label">Flywheel</div>
      <div class="cflow-center-sub">$TOKEN</div>
    </div>
  </div>
</div>

<style>
.cflow { display: flex; justify-content: center; }
.cflow-ring {
  position: relative;
  width: 100%;
  max-width: 520px;
  aspect-ratio: 1 / 1;
}
.cflow-arrows { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; }
.cnode {
  position: absolute;
  left: var(--x); top: var(--y);
  transform: translate(-50%, -50%);
  padding: 12px 18px;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 30%, transparent),
      color-mix(in srgb, var(--accent-1) 50%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
  display: flex; flex-direction: column; align-items: center; gap: 4px;
  min-width: 120px;
  z-index: 1;
}
.cnode i { color: var(--accent-1); font-size: 22px; }
.cnode-title {
  font: 700 13px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  text-align: center;
}

.cflow-center {
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
.cflow-center-label {
  font: 400 28px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.06em;
  color: var(--accent-1);
  text-shadow: 0 0 16px color-mix(in srgb, var(--accent-1) 30%, transparent);
}
.cflow-center-sub {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  margin-top: 4px;
}
</style>
```

## Node count

- **3 nodes**: triangle — simple cycle.
- **4 nodes**: standard (12/3/6/9 o'clock positions).
- **5–6 nodes**: rich cycles — evenly distributed around the ring.
- **7+**: too many; the loop metaphor breaks down. Use `process-flow` instead.

## Composition rules

- **Arrows all go the same direction** (all clockwise or all counter-clockwise). Mixed directions destroy the cycle reading.
- **Central element optional but powerful.** The token/product/user that benefits from the cycle lives in the center.
- **Every node has a verb or noun.** Short labels — 1–2 words.
- **No start / end marker.** The cycle is cyclical — no arrow origin point.
- **Square canvas ideal.** Rings need symmetric space.

## Anti-patterns

- Don't use circular-flow for one-way processes. That's `process-flow.md`.
- Don't break the cycle. If step 3 sometimes doesn't lead to step 4, it's not a flywheel.
- Don't cram text inside the ring center. Keep it short — the ring is the message.
