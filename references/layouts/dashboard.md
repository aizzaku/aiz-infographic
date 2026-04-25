# Dashboard Layout

Multiple simultaneous metrics and mini-charts. Tiled grid of widgets, each showing a slice of state. Static snapshot — not an interactive dashboard, a visual summary shaped like one.

## When to use

- Weekly / monthly stats summary
- Protocol health report (TVL + volume + active users + fees)
- Season recap (key numbers + top performers + highlights)
- Executive summary of an analytics report

## Required elements

`data-widgets.md` (KPI cards, progress bars, big numbers), `charts.md` (mini charts), `text.md`, `layout.md`, `decorative.md`, `icons.md`.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero strip (period + title)  │
├──────────────────────────────┤
│ KPI cells (3–6 big numbers)  │
├──────────────────────────────┤
│ ┌──────┐ ┌──────┐ ┌──────┐   │  chart + chart + list
│ └──────┘ └──────┘ └──────┘   │
├──────────────────────────────┤
│ ┌──────────┐ ┌──────────┐    │  comparison + breakdown
│ └──────────┘ └──────────┘    │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## Grid structure

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--gap-card);
}

.w-3  { grid-column: span 3; }  /* quarter-width widget */
.w-4  { grid-column: span 4; }  /* third */
.w-6  { grid-column: span 6; }  /* half */
.w-8  { grid-column: span 8; }  /* two-thirds */
.w-12 { grid-column: span 12; } /* full-width */

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
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
}
```

## Widget recipe

```html
<section class="section dashboard-grid">
  <!-- KPI row: 4 cells -->
  <div class="widget w-3">
    <div class="widget-header"><span class="widget-title">TVL</span></div>
    <div class="big-number-value">$42M</div>
    <div class="trend trend-up"><i class="ph-bold ph-trend-up"></i>+12%</div>
  </div>
  <div class="widget w-3">…</div>
  <div class="widget w-3">…</div>
  <div class="widget w-3">…</div>

  <!-- chart row: 8/4 split -->
  <div class="widget w-8">
    <div class="widget-header">
      <span class="widget-title">Volume · 30d</span>
      <span class="caption">rolling daily</span>
    </div>
    <!-- inline SVG line/area chart -->
  </div>
  <div class="widget w-4">
    <div class="widget-header"><span class="widget-title">Top chains</span></div>
    <!-- horizontal bar chart (3-5 rows) -->
  </div>

  <!-- comparison row: 6/6 -->
  <div class="widget w-6">
    <div class="widget-header"><span class="widget-title">User growth</span></div>
    <!-- metric + mini chart -->
  </div>
  <div class="widget w-6">
    <div class="widget-header"><span class="widget-title">Asset breakdown</span></div>
    <!-- donut with legend -->
  </div>
</section>
```

## Widget count guidance

| Canvas | Ideal widget count |
|--------|-------------------|
| portrait-medium | 6–9 widgets |
| portrait-tall | 9–14 widgets |
| landscape | 8–12 widgets |
| square | 4–6 widgets |

## Composition rules

- **Visual rhythm: alternate sizes.** All-equal widgets feel flat. Mix w-3/w-6/w-8.
- **Top row = headline KPIs.** The 4 most important numbers. Always span 3 (or 4 if 3 metrics).
- **Charts in the middle band.** The eye goes: headline → detail → breakdown.
- **Every widget has a tiny title** in `--text-muted` uppercase. The number does the talking.
- **Trend indicators on KPIs** (up/down) when the time dimension matters.
- **12-col grid, not 3-col.** 12 divides cleanly into 2, 3, 4, 6 — gives layout flexibility.

## Dimension guidance

Dashboards shine in landscape (16:9) because the 12-col grid has breathing room. Portrait works but widgets compress.

## Anti-patterns

- Don't mix widget border treatments — all outlined, all filled, or all flat. Consistency.
- Don't leave a widget empty. If a metric isn't available, drop the widget entirely.
- Don't use dashboard layout for 3 widgets. That's just a KPI strip.
- Don't add legends inside every widget. If colors are consistent across charts, one legend in a w-12 caption row is enough.
