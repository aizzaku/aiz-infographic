# Fishbone Layout (Ishikawa Diagram)

Cause-and-effect diagram. Central "spine" leads to an outcome on the right, with categorized causes branching off as ribs above and below.

## When to use

- Root cause analysis ("what contributed to X outcome?")
- Failure post-mortem visualization
- Multi-factor problem decomposition
- "Why X happened" — structured version

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`, `connectors.md` (angled lines).

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│   Category A     Category C   │
│     \               \         │
│      \               \        │
│   ────┴─────────┴─────>[Effect]│
│      /               /        │
│     /               /         │
│   Category B     Category D   │
├──────────────────────────────┤
│ Per-cause detail (optional)  │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## HTML pattern (SVG-based spine with CSS labels)

```html
<div class="fishbone">
  <svg viewBox="0 0 1000 400" class="fb-spine">
    <!-- main spine -->
    <line x1="50" y1="200" x2="900" y2="200"
          stroke="var(--accent-1)" stroke-width="2"/>
    <!-- arrowhead -->
    <polygon points="900,200 880,190 880,210"
             fill="var(--accent-1)"/>

    <!-- rib 1 (top-left) -->
    <line x1="200" y1="60" x2="280" y2="200"
          stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)" stroke-width="1.5"/>
    <!-- rib 2 (bottom-left) -->
    <line x1="200" y1="340" x2="280" y2="200"
          stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)" stroke-width="1.5"/>
    <!-- rib 3 (top-right) -->
    <line x1="500" y1="60" x2="580" y2="200"
          stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)" stroke-width="1.5"/>
    <!-- rib 4 (bottom-right) -->
    <line x1="500" y1="340" x2="580" y2="200"
          stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)" stroke-width="1.5"/>
  </svg>

  <div class="fb-effect">
    <span class="fb-effect-label">Liquidity drop</span>
  </div>

  <div class="fb-rib" style="--x: 15%; --y: 8%;">
    <div class="fb-cat">Market</div>
    <ul class="fb-causes">
      <li>BTC correction</li>
      <li>Sector rotation</li>
    </ul>
  </div>
  <div class="fb-rib" style="--x: 15%; --y: 70%;">
    <div class="fb-cat">Protocol</div>
    <ul class="fb-causes">
      <li>High fees</li>
      <li>Slow finality</li>
    </ul>
  </div>
  <div class="fb-rib" style="--x: 45%; --y: 8%;">
    <div class="fb-cat">Incentives</div>
    <ul class="fb-causes">
      <li>Emission cut</li>
      <li>Lower APR</li>
    </ul>
  </div>
  <div class="fb-rib" style="--x: 45%; --y: 70%;">
    <div class="fb-cat">Competitor</div>
    <ul class="fb-causes">
      <li>New L2 launched</li>
      <li>Higher yields</li>
    </ul>
  </div>
</div>

<style>
.fishbone {
  position: relative;
  aspect-ratio: 5 / 2;
  width: 100%;
}
.fb-spine { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; }
.fb-effect {
  position: absolute;
  right: 4%; top: 50%;
  transform: translateY(-50%);
  padding: 12px 18px;
  background:
    linear-gradient(var(--elevated), var(--elevated)) padding-box,
    linear-gradient(135deg, var(--accent-1), var(--accent-2)) border-box;
  border: 2px solid transparent;
  border-radius: var(--radius-card);
  box-shadow: 0 0 24px color-mix(in srgb, var(--accent-1) 24%, transparent);
  z-index: 1;
}
.fb-effect-label {
  font: 700 14px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--accent-1);
}
.fb-rib {
  position: absolute;
  left: var(--x); top: var(--y);
  z-index: 1;
  max-width: 140px;
}
.fb-cat {
  font: 700 12px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent-1);
  margin-bottom: 4px;
}
.fb-causes {
  list-style: none;
  padding: 0;
  margin: 0;
  font: 400 11px/1.3 'Montserrat', sans-serif;
  color: var(--text-secondary);
}
.fb-causes li { margin-bottom: 2px; }
</style>
```

## Composition rules

- **4–6 categories** (ribs). Fewer feels incomplete; more becomes unreadable.
- **Effect on the right**, labeled and boxed with accent styling.
- **Categories alternate above/below spine** for visual balance.
- **2–4 causes per rib.** One cause per rib is sparse; 5+ is cramped.
- **Standard categories for root-cause analysis**: People, Process, Technology, Environment, Measurement, Materials — or domain-specific equivalents.

## Dimension guidance

Landscape (16:9) is ideal. The spine wants horizontal space.

## Anti-patterns

- Don't use fishbone for process flows (no causation, just sequence). Use `process-flow.md`.
- Don't use when there's no single effect — fishbone converges; mind-map doesn't.
- Don't make ribs the same size as the spine. Ribs are subordinate.
