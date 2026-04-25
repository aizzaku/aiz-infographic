# Charts — SVG + CSS, No External Libraries

Pure SVG and CSS. No Chart.js, no D3, no runtime chart framework. Every chart is inlined in the HTML.

## When to use each

| Data shape | Chart |
|-----------|-------|
| Parts of a whole, 3–8 segments | donut or pie |
| Parts of a whole, 2–5 segments, horizontal space | horizontal segmented bar |
| Comparing ≤10 discrete values | horizontal bar |
| Time series or cumulative growth | stacked area or simple line |
| Progress toward a goal | progress ring or progress bar |
| Categorical comparison | grouped bar |

Heuristic: if any pie segment exceeds 75%, switch to a horizontal segmented bar.

## Donut chart

```html
<svg class="donut" viewBox="0 0 200 200" width="200" height="200">
  <circle cx="100" cy="100" r="80" fill="none"
          stroke="color-mix(in srgb, var(--text-primary) 8%, transparent)"
          stroke-width="28"/>
  <!-- one <circle> per segment; stroke-dasharray = [segment, remaining] of circumference -->
  <!-- circumference = 2 * π * 80 ≈ 502.65 -->
  <circle cx="100" cy="100" r="80" fill="none" stroke="var(--accent-1)"
          stroke-width="28"
          stroke-dasharray="201.06 502.65"
          stroke-dashoffset="0"
          transform="rotate(-90 100 100)"/>
  <circle cx="100" cy="100" r="80" fill="none" stroke="var(--accent-2)"
          stroke-width="28"
          stroke-dasharray="125.66 502.65"
          stroke-dashoffset="-201.06"
          transform="rotate(-90 100 100)"/>
  <!-- … additional segments … -->
  <text x="100" y="96" text-anchor="middle"
        font-family="Bebas Neue" font-size="36" fill="var(--text-primary)"
        letter-spacing="0.05em">1B</text>
  <text x="100" y="118" text-anchor="middle"
        font-family="Montserrat" font-weight="400" font-size="12"
        fill="var(--text-muted)" letter-spacing="0.1em"
        style="text-transform: uppercase;">Total supply</text>
</svg>
```

**Formula:** `stroke-dasharray = [percent * circumference, circumference]`. `stroke-dashoffset = -cumulative_percent * circumference`. Each segment rotates -90° so 0% starts at 12 o'clock.

## Horizontal segmented bar (tokenomics-friendly)

```html
<div class="hseg-bar">
  <div class="hseg" style="--pct: 40; background: var(--accent-1);">
    <span class="hseg-label">Community</span>
    <span class="hseg-value">40%</span>
  </div>
  <div class="hseg" style="--pct: 25; background: var(--accent-2);">
    <span class="hseg-label">Ecosystem</span>
    <span class="hseg-value">25%</span>
  </div>
  <div class="hseg" style="--pct: 20; background: color-mix(in srgb, var(--accent-1) 60%, transparent);">
    <span class="hseg-label">Team</span>
    <span class="hseg-value">20%</span>
  </div>
  <div class="hseg" style="--pct: 15; background: color-mix(in srgb, var(--accent-2) 60%, transparent);">
    <span class="hseg-label">Investors</span>
    <span class="hseg-value">15%</span>
  </div>
</div>

<style>
.hseg-bar {
  display: flex;
  width: 100%;
  height: 56px;
  border-radius: var(--radius-card);
  overflow: hidden;
}
.hseg {
  flex: var(--pct);
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 12px;
  color: var(--on-accent);
  font: 700 12px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.hseg-value {
  font: 400 18px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.04em;
  margin-top: 4px;
}
</style>
```

## Horizontal bar (ranked comparison)

```html
<div class="hbar-chart">
  <div class="hbar-row">
    <span class="hbar-label">Relay</span>
    <div class="hbar-track">
      <div class="hbar-fill" style="--pct: 82;"></div>
    </div>
    <span class="hbar-value">82%</span>
  </div>
  <!-- repeat -->
</div>

<style>
.hbar-chart { display: flex; flex-direction: column; gap: 8px; }
.hbar-row {
  display: grid;
  grid-template-columns: 120px 1fr 48px;
  align-items: center;
  gap: 12px;
  font: 700 13px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.hbar-track {
  height: 14px;
  background: color-mix(in srgb, var(--text-primary) 6%, transparent);
  border-radius: 7px;
  overflow: hidden;
}
.hbar-fill {
  width: calc(var(--pct) * 1%);
  height: 100%;
  background: linear-gradient(90deg, var(--accent-1), var(--accent-2));
}
.hbar-value {
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
  text-align: right;
}
</style>
```

## Progress ring

```html
<svg class="progress-ring" viewBox="0 0 120 120" width="120" height="120">
  <circle cx="60" cy="60" r="50" fill="none"
          stroke="color-mix(in srgb, var(--text-primary) 8%, transparent)"
          stroke-width="10"/>
  <circle cx="60" cy="60" r="50" fill="none" stroke="var(--accent-1)"
          stroke-width="10"
          stroke-linecap="round"
          stroke-dasharray="219.9 314.16"
          stroke-dashoffset="0"
          transform="rotate(-90 60 60)"/>
  <text x="60" y="66" text-anchor="middle"
        font-family="Bebas Neue" font-size="28"
        fill="var(--accent-1)">70%</text>
</svg>
```

`dasharray = percent * 2 * π * r`. For r=50, circumference ≈ 314.16.

## Legend pattern

```html
<ul class="chart-legend">
  <li><span class="swatch" style="background: var(--accent-1);"></span>Community <strong>40%</strong></li>
  <li><span class="swatch" style="background: var(--accent-2);"></span>Ecosystem <strong>25%</strong></li>
</ul>

<style>
.chart-legend { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; }
.chart-legend li {
  display: flex; align-items: center; gap: 10px;
  font: 400 14px/1.2 'Montserrat', sans-serif;
  color: var(--text-secondary);
}
.chart-legend li strong {
  margin-left: auto;
  font-weight: 700;
  color: var(--text-primary);
  font-variant-numeric: tabular-nums;
}
.swatch {
  width: 12px; height: 12px;
  border-radius: 2px;
  flex-shrink: 0;
}
</style>
```

## Rules

- Values are always labeled on or next to the chart. Never require viewers to guess.
- Colors come from the active style's accent pair (and analogous colors for ≥4 segments).
- Never use rainbow/cross-hue palettes unless the data requires maximum distinction (then pull from the 6-pair primaries).
- Never animate proportions — chart values are static. (Number counters animate in `data-widgets.md`.)
- Donut center text doubles as the primary metric. Use it.
