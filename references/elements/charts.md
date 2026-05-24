# Charts — SVG + CSS + Canvas

Static charts use pure SVG and CSS (no library). Canvas charts (radar, bubble, treemap, waffle) require an external library — load it conditionally, only when that chart type is used.

## When to use each

| Data shape | Chart | Renderer |
|-----------|-------|----------|
| Parts of a whole, 3–8 segments | **pie** (default) — donut only on explicit request | SVG |
| Parts of a whole, 2–5 segments, horizontal space | horizontal segmented bar | CSS |
| Comparing ≤10 discrete values | horizontal bar | CSS |
| Progress toward a goal | progress ring or progress bar | SVG / CSS |
| Multi-attribute comparison across 5–8 axes | **radar / spider** | Chart.js (canvas) |
| 3-variable scatter (x, y, bubble size) | **bubble** | Chart.js (canvas) |
| Hierarchical parts of a whole, 6+ segments | **treemap** | D3 (SVG) |
| Holder / allocation distribution at a glance | **waffle** | raw canvas |
| Hierarchical levels by magnitude, 3–6 tiers | **pyramid** | SVG |
| Ranked horizontal bar with emphasis flag on value | **arrow-flag bar** | CSS |
| Cyclical / oscillating values over time with peak callouts | **wave (multi-line sine)** | SVG |
| Multi-category radial spread, 3–7 categories | **rainbow arc** | SVG |
| Target vs actual / goal vs progress per category | **bullet bar** | CSS |

Heuristic: if any pie segment exceeds 75%, switch to a horizontal segmented bar. If allocation has 6+ categories with similar sizes, use treemap over donut.

## CDN loading (canvas charts only)

Add to `<head>` **only** when the output includes a canvas chart. Never add globally.

```html
<!-- Chart.js: radar and bubble charts -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>

<!-- D3: treemap (and sankey-flow / network-graph snippets) -->
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

## Color resolution helper

CSS variables (including `color-mix()`) cannot be passed directly to Chart.js or canvas APIs. Use this helper at the top of every canvas chart script block:

```js
function resolveColor(v) {
  const c = document.createElement('canvas');
  c.width = c.height = 1;
  const x = c.getContext('2d');
  x.fillStyle = v; x.fillRect(0,0,1,1);
  const [r,g,b] = x.getImageData(0,0,1,1).data;
  return { rgb: `rgb(${r},${g},${b})`, rgba: a => `rgba(${r},${g},${b},${a})` };
}
const root = getComputedStyle(document.documentElement);
const c1 = resolveColor(root.getPropertyValue('--accent-1').trim());
const c2 = resolveColor(root.getPropertyValue('--accent-2').trim());
const tp = resolveColor(root.getPropertyValue('--text-primary').trim());
const tm = resolveColor(root.getPropertyValue('--text-muted').trim());
```

## Playwright export rule

All canvas charts must set `data-canvas-ready="true"` on the element after drawing completes. Chart.js: add it after `new Chart(...)`. D3: add it after layout computation. Raw canvas: add it at the end of the draw function. No `async`/`await` — draw synchronously on `DOMContentLoaded`.

## Pie chart (default)

Solid pie. No center hole. Segments are filled with **shades of `--accent-1` only** — never `--accent-2`, never any other accent, never any other hex. The shade ladder is fixed (below). Apply darkest → lightest, biggest → smallest segment, so the eye reads weight before label.

```html
<!-- Pie via stroked circle: r=50, stroke-width=100 fills center → edge.
     Circumference = 2 * π * 50 ≈ 314.159. -->
<svg class="pie" viewBox="0 0 200 200" width="200" height="200">
  <!-- background disc (negative space, very faint) -->
  <circle cx="100" cy="100" r="50" fill="none"
          stroke="color-mix(in srgb, var(--text-primary) 6%, transparent)"
          stroke-width="100"/>
  <!-- Segment 1 — 40% — shade 100 (pure accent-1) -->
  <circle cx="100" cy="100" r="50" fill="none"
          stroke="var(--accent-1)"
          stroke-width="100"
          stroke-dasharray="125.66 314.16"
          stroke-dashoffset="0"
          transform="rotate(-90 100 100)"/>
  <!-- Segment 2 — 25% — shade 75 -->
  <circle cx="100" cy="100" r="50" fill="none"
          stroke="color-mix(in srgb, var(--accent-1) 75%, var(--canvas))"
          stroke-width="100"
          stroke-dasharray="78.54 314.16"
          stroke-dashoffset="-125.66"
          transform="rotate(-90 100 100)"/>
  <!-- Segment 3 — 20% — shade 55 -->
  <circle cx="100" cy="100" r="50" fill="none"
          stroke="color-mix(in srgb, var(--accent-1) 55%, var(--canvas))"
          stroke-width="100"
          stroke-dasharray="62.83 314.16"
          stroke-dashoffset="-204.20"
          transform="rotate(-90 100 100)"/>
  <!-- Segment 4 — 15% — shade 35 -->
  <circle cx="100" cy="100" r="50" fill="none"
          stroke="color-mix(in srgb, var(--accent-1) 35%, var(--canvas))"
          stroke-width="100"
          stroke-dasharray="47.12 314.16"
          stroke-dashoffset="-267.03"
          transform="rotate(-90 100 100)"/>
  <!-- … additional segments … -->
  <!-- Hairline divider ring on top for segment edges (optional, recommended) -->
  <circle cx="100" cy="100" r="100" fill="none"
          stroke="color-mix(in srgb, var(--canvas) 100%, transparent)"
          stroke-width="0"/>
</svg>
```

**Formula:** `stroke-dasharray = [percent × 314.16, 314.16]`. `stroke-dashoffset = -cumulative_percent × 314.16`. Each segment rotates -90° so 0% starts at 12 o'clock. Labels go OUTSIDE the pie (legend strip or leader lines), never inside — solid fills leave no room for centered text.

### Mono-accent shade ladder (binding for all parts-of-a-whole charts)

Pies, segmented bars, treemaps, waffles, and any other parts-of-a-whole chart use **only these shades of `--accent-1`** — in this order, largest → smallest segment:

| Order | Shade | CSS |
|---|---|---|
| 1 | 100 | `var(--accent-1)` |
| 2 | 75  | `color-mix(in srgb, var(--accent-1) 75%, var(--canvas))` |
| 3 | 55  | `color-mix(in srgb, var(--accent-1) 55%, var(--canvas))` |
| 4 | 35  | `color-mix(in srgb, var(--accent-1) 35%, var(--canvas))` |
| 5 | 22  | `color-mix(in srgb, var(--accent-1) 22%, var(--canvas))` |
| 6 | 14  | `color-mix(in srgb, var(--accent-1) 14%, var(--canvas))` |
| 7 | 8   | `color-mix(in srgb, var(--accent-1) 8%,  var(--canvas))` |
| 8 | 5   | `color-mix(in srgb, var(--accent-1) 5%,  var(--canvas))` |

Rules:
- Never use `--accent-2`, `--positive`, `--negative`, or any other hex in a parts-of-a-whole chart. Hue stays constant; only luminosity varies.
- If a chart needs more than 8 segments, you've exceeded the cap — split into two charts or switch to treemap.
- Legend dots use the exact same shade mix as the corresponding segment.
- Semantic colors (`--positive` for gains, `--negative` for losses) are still allowed in non-chart contexts (status pills, deltas, KPI trend arrows) — the mono-accent rule applies to part-of-whole geometry only.

### Donut variant (only on explicit user request)

If the user explicitly asks for a donut, switch to `r=80, stroke-width=28` (circumference 502.65) and keep the same mono-accent shade ladder. Otherwise, default to pie.

## Horizontal segmented bar (tokenomics-friendly)

```html
<div class="hseg-bar">
  <div class="hseg" style="--pct: 40; background: var(--accent-1);">
    <span class="hseg-label">Community</span>
    <span class="hseg-value">40%</span>
  </div>
  <div class="hseg" style="--pct: 25; background: color-mix(in srgb, var(--accent-1) 75%, var(--canvas));">
    <span class="hseg-label">Ecosystem</span>
    <span class="hseg-value">25%</span>
  </div>
  <div class="hseg" style="--pct: 20; background: color-mix(in srgb, var(--accent-1) 55%, var(--canvas));">
    <span class="hseg-label">Team</span>
    <span class="hseg-value">20%</span>
  </div>
  <div class="hseg" style="--pct: 15; background: color-mix(in srgb, var(--accent-1) 35%, var(--canvas));">
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
  <li><span class="swatch" style="background: color-mix(in srgb, var(--accent-1) 75%, var(--canvas));"></span>Ecosystem <strong>25%</strong></li>
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

## Radar / Spider chart (Chart.js)

**Use case:** Compare 2 protocols or options across 5–8 labelled dimensions (security, decentralization, fees, speed, UX). The polygon shape makes relative strengths/weaknesses immediately legible.

**Max datasets:** 3 (beyond that, fill areas overlap illegibly).

```html
<!-- Requires Chart.js in <head> -->
<div style="max-width: 400px; margin: 0 auto;">
  <canvas id="radar-1" width="400" height="400"></canvas>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  function resolveColor(v) {
    const c = document.createElement('canvas'); c.width = c.height = 1;
    const x = c.getContext('2d'); x.fillStyle = v; x.fillRect(0,0,1,1);
    const [r,g,b] = x.getImageData(0,0,1,1).data;
    return { rgb: `rgb(${r},${g},${b})`, rgba: a => `rgba(${r},${g},${b},${a})` };
  }
  const root = getComputedStyle(document.documentElement);
  const c1 = resolveColor(root.getPropertyValue('--accent-1').trim());
  const c2 = resolveColor(root.getPropertyValue('--accent-2').trim());
  const tp = resolveColor(root.getPropertyValue('--text-primary').trim());
  const tm = resolveColor(root.getPropertyValue('--text-muted').trim());

  const el = document.getElementById('radar-1');
  new Chart(el, {
    type: 'radar',
    data: {
      labels: ['Security', 'Decentralization', 'Speed', 'Fees', 'UX', 'Liquidity'],
      datasets: [
        {
          label: 'Protocol A',
          data: [85, 70, 60, 90, 75, 80],
          borderColor: c1.rgb, backgroundColor: c1.rgba(0.2),
          borderWidth: 2, pointBackgroundColor: c1.rgb, pointRadius: 4,
        },
        {
          label: 'Protocol B',
          data: [60, 90, 80, 65, 55, 70],
          borderColor: c2.rgb, backgroundColor: c2.rgba(0.2),
          borderWidth: 2, pointBackgroundColor: c2.rgb, pointRadius: 4,
        }
      ]
    },
    options: {
      animation: false,
      responsive: false,
      scales: {
        r: {
          min: 0, max: 100,
          ticks: { display: false },
          grid: { color: tm.rgba(0.25) },
          pointLabels: {
            color: tp.rgb,
            font: { family: "'Montserrat', sans-serif", size: 11, weight: '700' },
          },
          angleLines: { color: tm.rgba(0.25) },
        }
      },
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            color: tp.rgb,
            font: { family: "'Montserrat', sans-serif", size: 11 },
            boxWidth: 12, padding: 16,
          }
        }
      }
    }
  });
  el.dataset.canvasReady = 'true';
});
</script>
```

---

## Bubble chart (Chart.js)

**Use case:** 3-variable comparison — x-axis, y-axis, and bubble radius each encode a different metric (e.g. TVL × APY × market cap). Shows outliers and clusters across 3 dimensions at once.

**Max bubbles per dataset:** 12 (beyond that, labels and circles overlap).

```html
<!-- Requires Chart.js in <head> -->
<div style="width: 100%;">
  <canvas id="bubble-1" width="560" height="320"></canvas>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  function resolveColor(v) {
    const c = document.createElement('canvas'); c.width = c.height = 1;
    const x = c.getContext('2d'); x.fillStyle = v; x.fillRect(0,0,1,1);
    const [r,g,b] = x.getImageData(0,0,1,1).data;
    return { rgb: `rgb(${r},${g},${b})`, rgba: a => `rgba(${r},${g},${b},${a})` };
  }
  const root = getComputedStyle(document.documentElement);
  const c1 = resolveColor(root.getPropertyValue('--accent-1').trim());
  const c2 = resolveColor(root.getPropertyValue('--accent-2').trim());
  const tp = resolveColor(root.getPropertyValue('--text-primary').trim());
  const tm = resolveColor(root.getPropertyValue('--text-muted').trim());

  const el = document.getElementById('bubble-1');
  new Chart(el, {
    type: 'bubble',
    data: {
      datasets: [
        {
          label: 'Protocol A',
          // x = TVL (Bn), y = APY (%), r = bubble radius (scale to market cap)
          data: [{ x: 2.4, y: 18, r: 24 }, { x: 4.1, y: 12, r: 16 }],
          backgroundColor: c1.rgba(0.7), borderColor: c1.rgb, borderWidth: 2,
        },
        {
          label: 'Protocol B',
          data: [{ x: 1.2, y: 28, r: 20 }, { x: 3.6, y: 9, r: 12 }],
          backgroundColor: c2.rgba(0.7), borderColor: c2.rgb, borderWidth: 2,
        }
      ]
    },
    options: {
      animation: false,
      responsive: false,
      scales: {
        x: {
          title: { display: true, text: 'TVL (Bn)', color: tm.rgb, font: { family: "'Montserrat', sans-serif", size: 11 } },
          ticks: { color: tm.rgb, font: { family: "'Montserrat', sans-serif", size: 10 } },
          grid: { color: tm.rgba(0.15) },
        },
        y: {
          title: { display: true, text: 'APY %', color: tm.rgb, font: { family: "'Montserrat', sans-serif", size: 11 } },
          ticks: { color: tm.rgb, font: { family: "'Montserrat', sans-serif", size: 10 } },
          grid: { color: tm.rgba(0.15) },
        }
      },
      plugins: {
        legend: {
          position: 'bottom',
          labels: { color: tp.rgb, font: { family: "'Montserrat', sans-serif", size: 11 }, boxWidth: 12 }
        },
        tooltip: {
          callbacks: { label: ctx => `${ctx.dataset.label}: TVL ${ctx.raw.x}B · APY ${ctx.raw.y}% · Mkt ${ctx.raw.r}` }
        }
      }
    }
  });
  el.dataset.canvasReady = 'true';
});
</script>
```

---

## Treemap (D3, SVG)

**Use case:** Hierarchical allocation where area encodes magnitude — more expressive than a donut when there are 6+ categories or when relative size matters more than exact angles.

**Max leaves:** 16. Beyond that, small cells become illegible.

```html
<!-- Requires D3 in <head> -->
<div id="treemap-1" style="width: 100%; aspect-ratio: 16 / 9;"></div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  function resolveColor(v) {
    const c = document.createElement('canvas'); c.width = c.height = 1;
    const x = c.getContext('2d'); x.fillStyle = v; x.fillRect(0,0,1,1);
    const [r,g,b] = x.getImageData(0,0,1,1).data;
    return `rgb(${r},${g},${b})`;
  }
  const root = getComputedStyle(document.documentElement);
  const c1 = resolveColor(root.getPropertyValue('--accent-1').trim());
  const c2 = resolveColor(root.getPropertyValue('--accent-2').trim());
  const tp = root.getPropertyValue('--text-primary').trim();

  const data = {
    name: 'root',
    children: [
      { name: 'Community', value: 40 },
      { name: 'Ecosystem', value: 25 },
      { name: 'Team',      value: 20 },
      { name: 'Investors', value: 15 },
    ]
  };

  const wrap = document.getElementById('treemap-1');
  const W = wrap.clientWidth || 640;
  const H = Math.round(W * 9 / 16);

  const colorScale = d3.scaleOrdinal()
    .range([c1, c2, d3.interpolateRgb(c1, c2)(0.33), d3.interpolateRgb(c1, c2)(0.66)]);

  const hierarchy = d3.hierarchy(data).sum(d => d.value);
  d3.treemap().size([W, H]).padding(4).round(true)(hierarchy);

  const svg = d3.select(wrap).append('svg')
    .attr('width', W).attr('height', H).style('display', 'block');

  const cell = svg.selectAll('g')
    .data(hierarchy.leaves()).join('g')
    .attr('transform', d => `translate(${d.x0},${d.y0})`);

  cell.append('rect')
    .attr('width',  d => d.x1 - d.x0)
    .attr('height', d => d.y1 - d.y0)
    .attr('rx', 6)
    .attr('fill', d => colorScale(d.data.name))
    .attr('fill-opacity', 0.88);

  cell.filter(d => (d.x1 - d.x0) > 64 && (d.y1 - d.y0) > 40)
    .append('text')
    .attr('x', 12).attr('y', 28)
    .attr('fill', '#ffffff')
    .attr('font-family', "'Montserrat', sans-serif")
    .attr('font-weight', '700').attr('font-size', '13')
    .text(d => d.data.name);

  cell.filter(d => (d.x1 - d.x0) > 64 && (d.y1 - d.y0) > 56)
    .append('text')
    .attr('x', 12).attr('y', 50)
    .attr('fill', 'rgba(255,255,255,0.8)')
    .attr('font-family', "'Bebas Neue', sans-serif")
    .attr('font-size', '22')
    .text(d => `${d.data.value}%`);

  wrap.dataset.canvasReady = 'true';
});
</script>
```

---

## Waffle chart (raw canvas)

**Use case:** Show a distribution across 2–5 segments as a 10×10 grid of 100 colored cells. Better than a donut when exact counts matter (each cell = 1%) or when the aesthetic calls for a grid-based, data-dense look.

**Constraint:** Values must sum to 100. Round before rendering — any remainder fills as the last segment.

```html
<div style="display: flex; gap: 32px; align-items: center; flex-wrap: wrap;">
  <canvas id="waffle-1" width="352" height="352"></canvas>
  <ul class="chart-legend">
    <li><span class="swatch" style="background: var(--accent-1);"></span>Community <strong>40%</strong></li>
    <li><span class="swatch" style="background: color-mix(in srgb, var(--accent-1) 75%, var(--canvas));"></span>Ecosystem <strong>25%</strong></li>
    <li><span class="swatch" style="background: color-mix(in srgb, var(--accent-1) 45%, transparent);"></span>Team <strong>20%</strong></li>
    <li><span class="swatch" style="background: color-mix(in srgb, var(--text-muted) 60%, transparent);"></span>Investors <strong>15%</strong></li>
  </ul>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  function resolveColor(v) {
    const c = document.createElement('canvas'); c.width = c.height = 1;
    const x = c.getContext('2d'); x.fillStyle = v; x.fillRect(0,0,1,1);
    const [r,g,b] = x.getImageData(0,0,1,1).data;
    return { rgb: `rgb(${r},${g},${b})`, rgba: a => `rgba(${r},${g},${b},${a})` };
  }
  const root = getComputedStyle(document.documentElement);
  const c1 = resolveColor(root.getPropertyValue('--accent-1').trim());
  const c2 = resolveColor(root.getPropertyValue('--accent-2').trim());
  const tm = resolveColor(root.getPropertyValue('--text-muted').trim());

  const segments = [
    { value: 40, color: c1.rgb },
    { value: 25, color: c2.rgb },
    { value: 20, color: c1.rgba(0.45) },
    { value: 15, color: tm.rgba(0.55) },
  ];

  const canvas = document.getElementById('waffle-1');
  const ctx = canvas.getContext('2d');
  const cellSize = 32, gap = 3.5, cols = 10, radius = 5;

  let cell = 0;
  segments.forEach(seg => {
    for (let i = 0; i < Math.round(seg.value); i++, cell++) {
      const col = cell % cols;
      const row = Math.floor(cell / cols);
      const x = col * (cellSize + gap);
      const y = row * (cellSize + gap);
      ctx.fillStyle = seg.color;
      ctx.beginPath();
      ctx.roundRect(x, y, cellSize, cellSize, radius);
      ctx.fill();
    }
  });
  canvas.dataset.canvasReady = 'true';
});
</script>
```

---

## Rules

- Values are always labeled on or next to the chart. Never require viewers to guess.
- Colors come from the active style's accent pair (and analogous colors for ≥4 segments).
- Never use rainbow/cross-hue palettes unless the data requires maximum distinction (then pull from the 6-pair primaries).
- Never animate proportions — chart values are static. (Number counters animate in `data-widgets.md`.)
- Donut center text doubles as the primary metric. Use it.
- Canvas charts: always `animation: false` (Chart.js) or synchronous layout (D3). Never rely on requestAnimationFrame for the initial render — Playwright screenshots immediately after page load.

---

## Pyramid chart

Hierarchical levels by magnitude — apex = smallest/most-exclusive, base = largest/foundation. Use for hierarchies, funnels with named tiers, or layered concepts.

**Always render labels OUTSIDE the bands** on a side rail. Inside-band labels get clipped by the slanted edges and become illegible — especially the apex (a true triangle has no usable inner width).

```html
<div class="pyramid-wrap">
  <div class="pyramid">
    <div class="pyramid-row" style="--w: 30%; --shade: 100%;"></div>
    <div class="pyramid-row" style="--w: 50%; --shade: 75%;"></div>
    <div class="pyramid-row" style="--w: 70%; --shade: 55%;"></div>
    <div class="pyramid-row" style="--w: 90%; --shade: 35%;"></div>
  </div>
  <div class="pyramid-side">
    <div class="pyramid-side-row" style="--shade: 100%;">
      <span class="pyramid-side-name">Founders</span>
      <span class="pyramid-pct">2%</span>
    </div>
    <div class="pyramid-side-row" style="--shade: 75%;">
      <span class="pyramid-side-name">Core team</span>
      <span class="pyramid-pct">8%</span>
    </div>
    <div class="pyramid-side-row" style="--shade: 55%;">
      <span class="pyramid-side-name">Contributors</span>
      <span class="pyramid-pct">20%</span>
    </div>
    <div class="pyramid-side-row" style="--shade: 35%;">
      <span class="pyramid-side-name">Community</span>
      <span class="pyramid-pct">70%</span>
    </div>
  </div>
</div>

<style>
.pyramid-wrap { display: grid; grid-template-columns: 1.2fr 1fr; gap: 32px; align-items: center; }
.pyramid { display: flex; flex-direction: column; align-items: center; gap: 4px; }
.pyramid-row {
  width: var(--w); height: 60px;
  background: color-mix(in srgb, var(--accent-1) var(--shade), var(--canvas));
  clip-path: polygon(12% 0, 88% 0, 100% 100%, 0 100%);
}
.pyramid-row:first-child { clip-path: polygon(50% 0, 100% 100%, 0 100%); }
.pyramid-side { display: flex; flex-direction: column; gap: 8px; }
.pyramid-side-row {
  display: grid; grid-template-columns: 14px 1fr auto; gap: 14px;
  align-items: center; height: 60px;
}
.pyramid-side-row::before {
  content: ""; width: 10px; height: 10px; border-radius: 50%;
  background: color-mix(in srgb, var(--accent-1) var(--shade), var(--canvas));
}
.pyramid-side-name {
  font: 700 16px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.05em;
  color: var(--text-primary);
}
.pyramid-pct { font: 400 28px/1 'Bebas Neue', sans-serif; color: var(--accent-1); }
</style>
```

**Rules:**
- 3-6 tiers. More than 6 reads as a bar chart.
- Shades follow the mono-accent ladder (100 → 75 → 55 → 35 → 22 → 14), apex darkest.
- Apex tier uses a true triangle clip-path; other tiers are trapezoids.
- Side rail uses leader dots matching each band's shade. Aligns row-for-row with bands at equal height.
- Do NOT place labels inside the bands. The clip-path will eat them.

---

## Arrow-flag horizontal bar

Horizontal bar where the right edge terminates in a chevron / flag holding the value. Replaces a separate value column.

Each row has a fixed label column on the left, then a track that **reserves padding-right room for the flag** so it never overflows the container at 100% values.

```html
<div class="aflag-list">
  <div class="aflag-row">
    <span class="aflag-label">Solana</span>
    <div class="aflag-track">
      <div class="aflag-bar" style="--pct: 90%;"><span class="aflag-flag">90%</span></div>
    </div>
  </div>
  <div class="aflag-row">
    <span class="aflag-label">BNB</span>
    <div class="aflag-track">
      <div class="aflag-bar" style="--pct: 72%; --shade: 75%;"><span class="aflag-flag">72%</span></div>
    </div>
  </div>
</div>

<style>
.aflag-list { display: flex; flex-direction: column; gap: 12px; }
.aflag-row { display: grid; grid-template-columns: 110px 1fr; gap: 14px; align-items: center; }
.aflag-label {
  font: 700 13px/1 'Montserrat', sans-serif;
  letter-spacing: 0.05em; text-transform: uppercase;
  color: var(--text-primary);
}
.aflag-track {
  position: relative;
  height: 22px;
  background: var(--elevated);
  border-radius: 4px;
  padding-right: 64px; /* reserves room for the flag */
}
.aflag-bar {
  position: relative;
  height: 100%; width: var(--pct);
  background: color-mix(in srgb, var(--accent-1) var(--shade, 100%), var(--canvas));
  border-radius: 4px 0 0 4px;
}
.aflag-flag {
  position: absolute; top: 50%; left: 100%;
  transform: translate(0, -50%);
  padding: 4px 14px 4px 10px;
  background: var(--accent-1); color: var(--on-accent);
  font: 700 12px/1 'Montserrat', sans-serif; letter-spacing: 0.04em;
  font-variant-numeric: tabular-nums;
  clip-path: polygon(0 0, calc(100% - 8px) 0, 100% 50%, calc(100% - 8px) 100%, 0 100%);
}
</style>
```

**Rules:**
- Flag chevron is always darkest accent (100%); bar shade can vary per row.
- Bar height: 18-24px. Flag height matches bar height.
- One flag per row, anchored to the bar's right edge.
- Track always has `padding-right` ≥ 56px to keep the flag inside the container at 100% bar values.

---

## Wave chart (cyclical multi-line)

Multi-line sine-style chart with peak markers. For cyclical, seasonal, or oscillating data where the *shape* matters more than exact values.

**Keep all peaks ABOVE the baseline** so peak markers and their labels stay inside the viewBox. Use a baseline at y ≈ 75% of viewBox height and route peaks upward.

```html
<!-- viewBox 800×240, baseline y=180, peaks reach y ≈ 50–100 -->
<svg class="wave-chart" viewBox="0 0 800 240" width="100%" preserveAspectRatio="none">
  <!-- back wave (shade 35) -->
  <path d="M 0 180 Q 100 130, 200 180 Q 300 220, 400 180 Q 500 130, 600 180 Q 700 220, 800 180"
        fill="none" stroke="color-mix(in srgb, var(--accent-1) 35%, var(--canvas))" stroke-width="2"/>
  <!-- mid wave (shade 60) -->
  <path d="M 0 180 Q 100 110, 200 180 Q 300 210, 400 180 Q 500 110, 600 180 Q 700 210, 800 180"
        fill="none" stroke="color-mix(in srgb, var(--accent-1) 60%, var(--canvas))" stroke-width="2"/>
  <!-- front wave (accent 100), peaks at x=100/300/500/700 -->
  <path d="M 0 180 Q 100 60, 200 180 Q 300 100, 400 180 Q 500 80, 600 180 Q 700 50, 800 180"
        fill="none" stroke="var(--accent-1)" stroke-width="2.5"/>

  <!-- peak markers + leader lines + labels (all above baseline, inside viewBox) -->
  <g>
    <line x1="100" y1="60" x2="100" y2="38" stroke="var(--accent-1)" stroke-width="1"/>
    <circle cx="100" cy="60" r="6" fill="var(--accent-1)"/>
    <text x="100" y="30" text-anchor="middle"
          font-family="Bebas Neue" font-size="20" fill="var(--text-primary)">30%</text>
  </g>
  <!-- … repeat per peak … -->
</svg>
```

**Rules:**
- 1-3 stacked waves. More than 3 = visual mush.
- Each wave uses a different shade from the mono-accent ladder.
- Peak markers: solid circles in `--accent-1`, leader line up to the value label.
- Label every visible peak. Unlabeled peaks are wasted ink.
- All peaks and labels stay within viewBox bounds — never let labels fall above y=0 or below the viewBox height. If your data has troughs to label, expand the viewBox vertically; do not let them clip.

---

## Rainbow arc chart

Concentric half-arcs of varying length, each terminating in a labeled token. Multi-category radial spread.

**Compute endpoints from sweep angle θ.** Each arc starts at the left horizontal (180°) and sweeps clockwise by its own angle. For an arc of radius `r` centered at `(cx, cy)` starting at `(cx − r, cy)`:

```
endX = cx − r · cos(θ)
endY = cy − r · sin(θ)
```

With `cx=200, cy=240` and sweep angles `180°, 150°, 120°, 90°, 60°` at radii `160, 140, 120, 100, 80`, the endpoints are:

| Arc | r | θ | end |
|---|---|---|---|
| A | 160 | 180° | (360, 240) |
| B | 140 | 150° | (321, 170) |
| C | 120 | 120° | (260, 136) |
| D | 100 | 90°  | (200, 140) |
| E | 80  | 60°  | (160, 171) |

```html
<svg class="rainbow-arc" viewBox="0 0 400 280" width="400" height="280">
  <!-- A: r=160, θ=180° -->
  <path d="M 40 240 A 160 160 0 0 1 360 240" fill="none"
        stroke="var(--accent-1)" stroke-width="14"/>
  <!-- B: r=140, θ=150° -->
  <path d="M 60 240 A 140 140 0 0 1 321 170" fill="none"
        stroke="color-mix(in srgb, var(--accent-1) 75%, var(--canvas))" stroke-width="14"/>
  <!-- C: r=120, θ=120° -->
  <path d="M 80 240 A 120 120 0 0 1 260 136" fill="none"
        stroke="color-mix(in srgb, var(--accent-1) 55%, var(--canvas))" stroke-width="14"/>
  <!-- D: r=100, θ=90° -->
  <path d="M 100 240 A 100 100 0 0 1 200 140" fill="none"
        stroke="color-mix(in srgb, var(--accent-1) 35%, var(--canvas))" stroke-width="14"/>
  <!-- E: r=80, θ=60° -->
  <path d="M 120 240 A 80 80 0 0 1 160 171" fill="none"
        stroke="color-mix(in srgb, var(--accent-1) 22%, var(--canvas))" stroke-width="14"/>

  <!-- terminal tokens at each endpoint, same shade as their arc -->
  <g><circle cx="360" cy="240" r="14" fill="var(--accent-1)"/>
     <text x="360" y="245" text-anchor="middle" font-family="Montserrat"
           font-weight="700" font-size="13" fill="var(--on-accent)">A</text></g>
  <!-- … one per arc, fill matches the arc's stroke shade … -->
</svg>
```

**Rules:**
- 3-7 arcs. Fewer than 3 isn't worth this chart; more than 7 collides.
- Sort longest-to-shortest, outermost-to-innermost (or vice versa — pick one and stick to it).
- Always pair with a legend mapping token letter → category name.
- Mono-accent shade ladder per the parts-of-a-whole rule. Token fill matches its arc's stroke.
- Sweep angles must be ≤ 180° (large-arc-flag stays 0). If you need > 180°, switch to a full ring chart.

---

## Bullet bar (target vs actual)

Horizontal or vertical bar pair where a brighter "actual" fill sits inside a dim "target" track. Optional marker for goal threshold.

```html
<!-- Horizontal -->
<div class="bullet-row">
  <span class="bullet-label">Q1 Revenue</span>
  <div class="bullet-track">
    <div class="bullet-fill" style="width: 78%;"></div>
    <div class="bullet-marker" style="left: 90%;"></div>
  </div>
  <span class="bullet-value">78%</span>
</div>

<style>
.bullet-row { display: grid; grid-template-columns: 140px 1fr 60px; gap: 12px;
              align-items: center; margin-bottom: 10px; }
.bullet-label { font: 700 13px/1 'Montserrat', sans-serif; text-transform: uppercase;
                letter-spacing: 0.05em; color: var(--text-primary); }
.bullet-track { position: relative; height: 16px;
                background: color-mix(in srgb, var(--accent-1) 14%, var(--canvas));
                border-radius: 3px; overflow: hidden; }
.bullet-fill { height: 100%; background: var(--accent-1); border-radius: 3px 0 0 3px; }
.bullet-marker { position: absolute; top: -2px; bottom: -2px; width: 2px;
                 background: var(--text-primary); }
.bullet-value { font: 400 18px/1 'Bebas Neue', sans-serif; color: var(--accent-1);
                font-variant-numeric: tabular-nums; text-align: right; }
</style>
```

**Vertical variant:** swap `width` for `height` on `.bullet-fill`, rotate the grid into a column. Useful for dashboard panels with 4-8 KPIs in a row (like Image 3, BB).

**Rules:**
- Only two color stops: dim target track + bright actual fill. Never add a third.
- Marker (white tick) is optional and only shows when there's a *specific* goal threshold distinct from "100%".
- Cap at 8 bars per chart. More than 8 → use horizontal bar list.
