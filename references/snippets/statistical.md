# Statistical Snippet

Hero KPI strip plus a single primary chart. Use when 3-6 headline numbers anchor the section, with a chart for distribution or trend.

## When to use

- Tokenomics distribution (KPIs + donut/bar)
- Protocol stats / ecosystem metrics
- Any section where 3-6 KPIs and one hero chart are the core payload

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| bento-box | hero (KPIs only, no chart) | KPI strip inline with hero title |
| bento-box | card-wide (`1/-1`) | KPI strip + chart in one full-bleed card |
| editorial | body-column | Inline figure with KPIs + small chart |
| dashboard | full kpi-row | KPI strip is the row; chart goes in panel below |
| poster | header-strip | KPIs only, before centerpiece |
| poster | support-card | Single KPI breakdown card |

## Required elements

`charts.md`, `data-widgets.md`, `text.md`, `layout.md`, `decorative.md`

## KPI strip pattern

```html
<section class="kpi-strip" style="--kpi-count: 4;">
  <div class="kpi-card">
    <span class="kpi-value">$42M</span>
    <span class="kpi-label">TVL</span>
  </div>
  <!-- 3-6 .kpi-card cells -->
</section>

<style>
.kpi-strip {
  display: grid;
  grid-template-columns: repeat(var(--kpi-count, 4), 1fr);
  gap: var(--gap-card);
}
.kpi-card {
  padding: 16px;
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--accent-1) 18%, transparent);
  border-radius: var(--radius-card);
  display: flex; flex-direction: column; gap: 4px;
}
.kpi-value {
  font: 400 36px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.02em;
  color: var(--text-primary);
}
.kpi-label {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--text-muted);
}
</style>
```

## Chart-with-legend pattern (donut variant)

```html
<div class="grid-2-asym">
  <!-- chart: donut from charts.md (60% width) -->
  <div class="chart-donut">…</div>
  <!-- legend: stacked rows (40% width) -->
  <div class="legend-stack">
    <div class="legend-row">
      <span class="legend-swatch" style="background: var(--accent-1);"></span>
      <span class="legend-label">Community</span>
      <span class="legend-value">30%</span>
    </div>
    <!-- repeat -->
  </div>
</div>

<style>
.grid-2-asym { display: grid; grid-template-columns: 60% 40%; gap: 24px; align-items: center; }
.legend-stack { display: flex; flex-direction: column; gap: 8px; }
.legend-row {
  display: grid;
  grid-template-columns: 16px 1fr auto;
  gap: 10px; align-items: center;
}
.legend-swatch { width: 12px; height: 12px; border-radius: 3px; }
.legend-label { font: 600 12px/1 'Montserrat', sans-serif; color: var(--text-primary); }
.legend-value { font: 700 12px/1 'Montserrat', sans-serif; color: var(--accent-1); }
</style>
```

## Adaptation rules

| Data | Response |
|---|---|
| 3 KPIs | `--kpi-count: 3`, larger chart |
| 4-5 KPIs | `--kpi-count: 4`, drop 5th into supporting card |
| 6+ KPIs | Two rows OR drop lowest-priority |
| 3-4 chart segments | Donut + legend |
| 5-8 chart segments | Horizontal segmented bar full-width, legend below |
| Any segment > 75% | Switch from donut to segmented bar |

## Composition rules

- KPI values use display font; labels use body font uppercase.
- One chart per section, max. If two are needed, split into two snippets.
- Legend always paired with chart, never floating.
- Numbers must be either real or clearly placeholder (`{value}`) — never invented.

## Anti-patterns

- All-equal-weight KPIs with no hierarchy → bold the most important value 1.2× larger.
- Donut for > 8 segments → unreadable; switch to bar.
- Pie chart with one segment > 75% → use a bar with a delta call-out instead.
