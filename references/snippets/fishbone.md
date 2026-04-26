# Fishbone (Ishikawa) Snippet

Cause-and-effect diagram. Central spine pointing to an outcome on the right, categorized causes branching off as ribs above and below.

## When to use

- Root cause analysis ("what contributed to X outcome?")
- Failure post-mortem visualization
- Multi-factor problem decomposition
- Structured "why X happened"

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| poster | centerpiece | Best — spine wants horizontal landscape space |
| bento-box | card-wide (`1/-1`) | Compact 4-rib fishbone, full-bleed |
| editorial | body-column | Inline figure |

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`, `connectors.md`.

## HTML pattern (SVG spine + CSS labels)

```html
<div class="fishbone">
  <svg viewBox="0 0 1000 400" class="fb-spine">
    <line x1="50" y1="200" x2="900" y2="200" stroke="var(--accent-1)" stroke-width="2"/>
    <polygon points="900,200 880,190 880,210" fill="var(--accent-1)"/>
    <line x1="200" y1="60"  x2="280" y2="200" stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)" stroke-width="1.5"/>
    <line x1="200" y1="340" x2="280" y2="200" stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)" stroke-width="1.5"/>
    <line x1="500" y1="60"  x2="580" y2="200" stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)" stroke-width="1.5"/>
    <line x1="500" y1="340" x2="580" y2="200" stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)" stroke-width="1.5"/>
  </svg>

  <div class="fb-effect"><span class="fb-effect-label">Liquidity drop</span></div>

  <div class="fb-rib" style="--x: 15%; --y: 8%;">
    <div class="fb-cat">Market</div>
    <ul class="fb-causes"><li>BTC correction</li><li>Sector rotation</li></ul>
  </div>
  <div class="fb-rib" style="--x: 15%; --y: 70%;">
    <div class="fb-cat">Protocol</div>
    <ul class="fb-causes"><li>High fees</li><li>Slow finality</li></ul>
  </div>
  <div class="fb-rib" style="--x: 45%; --y: 8%;">
    <div class="fb-cat">Incentives</div>
    <ul class="fb-causes"><li>Emission cut</li><li>Lower APR</li></ul>
  </div>
  <div class="fb-rib" style="--x: 45%; --y: 70%;">
    <div class="fb-cat">Competitor</div>
    <ul class="fb-causes"><li>New L2 launched</li><li>Higher yields</li></ul>
  </div>
</div>

<style>
.fishbone { position: relative; aspect-ratio: 5 / 2; width: 100%; }
.fb-spine { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; }
.fb-effect {
  position: absolute; right: 4%; top: 50%;
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
  text-transform: uppercase; letter-spacing: 0.05em;
  color: var(--accent-1);
}
.fb-rib { position: absolute; left: var(--x); top: var(--y); z-index: 1; max-width: 140px; }
.fb-cat {
  font: 700 12px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--accent-1);
  margin-bottom: 4px;
}
.fb-causes {
  list-style: none; padding: 0; margin: 0;
  font: 400 11px/1.3 'Montserrat', sans-serif;
  color: var(--text-secondary);
}
.fb-causes li { margin-bottom: 2px; }
</style>
```

## Composition rules

- 4-6 categories (ribs). Fewer feels incomplete; more becomes unreadable.
- Effect on the right, accent-styled box.
- Categories alternate above/below spine for balance.
- 2-4 causes per rib.
- Pixel-locked geometry — rib endpoints land on spine coordinates.
- Standard root-cause categories: People, Process, Technology, Environment, Measurement, Materials — or domain equivalents.

## Anti-patterns

- Process flows (no causation) → use `process-flow`.
- No single effect → use `mind-map`.
- Ribs same size as spine — ribs are subordinate.
