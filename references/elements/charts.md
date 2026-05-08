# Charts — SVG + CSS + Canvas

Static charts use pure SVG and CSS (no library). Canvas charts (radar, bubble, treemap, waffle) require an external library — load it conditionally, only when that chart type is used.

## When to use each

| Data shape | Chart | Renderer |
|-----------|-------|----------|
| Parts of a whole, 3–8 segments | donut or pie | SVG |
| Parts of a whole, 2–5 segments, horizontal space | horizontal segmented bar | CSS |
| Comparing ≤10 discrete values | horizontal bar | CSS |
| Progress toward a goal | progress ring or progress bar | SVG / CSS |
| Multi-attribute comparison across 5–8 axes | **radar / spider** | Chart.js (canvas) |
| 3-variable scatter (x, y, bubble size) | **bubble** | Chart.js (canvas) |
| Hierarchical parts of a whole, 6+ segments | **treemap** | D3 (SVG) |
| Holder / allocation distribution at a glance | **waffle** | raw canvas |

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
    <li><span class="swatch" style="background: var(--accent-2);"></span>Ecosystem <strong>25%</strong></li>
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
