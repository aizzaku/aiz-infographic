# KPI Panel Grid Snippet

> **Renamed from `dashboard` snippet** for disambiguation — the dashboard *canvas* still exists. This snippet is the section-level panels grid that plugs into any canvas slot.

Mixed-width widget grid on a 12-column base. Use when a section needs to host multiple parallel panels (KPIs, mini charts, breakdowns) with rhythmic size variation.

## When to use

- A section that hosts 4-12 parallel widgets (mini charts + KPIs + breakdowns)
- Inside a `bento-box` card-wide slot when one card needs to itself contain a panel grid
- Inside an `editorial` body-column when prose pauses for a stats interlude
- Inside the dashboard canvas to fill its body slot (the canvas declares the header strip; this snippet fills the panels area)

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| dashboard | body (panels area) | Native fit — canvas hosts header, snippet fills panels |
| bento-box | card-wide (`1/-1`) | Mini panel-grid inside one bento card |
| editorial | body-column | Stats interlude between prose paragraphs |
| poster | support cluster | 2-4 panels stacked alongside the centerpiece |

## Required elements

`data-widgets.md`, `charts.md`, `text.md`, `layout.md`, `decorative.md`, `icons.md`.

## HTML pattern

```html
<div class="dashboard-grid">

  <!-- KPI row: 4 cells, span 3 each -->
  <div class="widget kpi-widget w-3">
    <span class="widget-title">TVL</span>
    <div class="big-number-value">$42M</div>
    <div class="trend trend-up"><i class="ph-bold ph-trend-up"></i>+12%</div>
  </div>
  <div class="widget kpi-widget w-3">…</div>
  <div class="widget kpi-widget w-3">…</div>
  <div class="widget kpi-widget w-3">…</div>

  <!-- Chart row: 8/4 split -->
  <div class="widget w-8">
    <div class="widget-header">
      <span class="widget-title">Volume · 30d</span>
      <span class="caption">rolling daily</span>
    </div>
    <!-- inline SVG line/area chart -->
  </div>
  <div class="widget w-4">
    <div class="widget-header"><span class="widget-title">Top chains</span></div>
    <!-- horizontal bar chart -->
  </div>

  <!-- Comparison row: 6/6 -->
  <div class="widget w-6">
    <div class="widget-header"><span class="widget-title">User growth</span></div>
  </div>
  <div class="widget w-6">
    <div class="widget-header"><span class="widget-title">Asset breakdown</span></div>
  </div>
</div>

<style>
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--gap-card);
}
.w-3  { grid-column: span 3; }
.w-4  { grid-column: span 4; }
.w-6  { grid-column: span 6; }
.w-8  { grid-column: span 8; }
.w-12 { grid-column: span 12; }

.widget {
  padding: 16px;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 18%, transparent),
      color-mix(in srgb, var(--accent-1) 36%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
  min-height: 120px;
}
.widget-header {
  display: flex; justify-content: space-between; align-items: baseline;
  margin-bottom: 10px;
}
.widget-title {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--text-muted);
}
.kpi-widget .big-number-value {
  font: 400 48px/1 'Bebas Neue', sans-serif;
  color: var(--text-primary);
  margin: 4px 0 6px;
}
.trend {
  font: 700 11px/1 'Montserrat', sans-serif;
  letter-spacing: 0.05em; text-transform: uppercase;
  display: inline-flex; align-items: center; gap: 4px;
}
.trend-up   { color: var(--positive); }
.trend-down { color: var(--negative); }
</style>
```

## Widget count guidance

| Slot width | Ideal widget count |
|---|---|
| Editorial body-column | 4-6 widgets |
| Bento card-wide | 4-6 widgets |
| Dashboard canvas body | 8-14 widgets |
| Poster support cluster | 2-4 widgets |

## Composition rules

- Visual rhythm: alternate sizes. Mix `w-3 / w-6 / w-8`. All-equal widgets feel flat.
- KPIs always at the top row, span 3 each (4 KPIs × span-3 = 12 cols).
- Charts in the middle band. Eye flow: headline → detail → breakdown.
- Every widget has a tiny title in `--text-muted` uppercase. The number does the talking.
- Trend indicators on KPIs (up/down + %) when time dimension matters.
- 12-col grid only, never 3-col. 12 divides cleanly into 2/3/4/6.
- One legend at the bottom, not per-widget.
- Empty widgets forbidden. Drop the widget if no data.

## Anti-patterns

- Mixing widget border treatments (some outlined, some filled).
- Decorative dividers between widgets — gap and gradient borders are the divider.
- Widget titles in primary text color — competes with the number.
- Charts without axis labels or units.
