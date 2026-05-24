# Dashboard Canvas

KPI strip on top, panel grid below. Static snapshot shaped like an interactive dashboard. Best for weekly/monthly stats summaries, protocol health reports, season recaps, executive analytics summaries — anything where multiple simultaneous metrics each tell a small slice of the story.

## Slots

| Slot | Purpose | Snippets that fit | Density cap |
|---|---|---|---|
| `header-strip` | Period + title + last-updated meta | (built into canvas) | 1 |
| `kpi-row` | Top headline KPIs (3-6 big numbers across) | `stat-spotlight` snippets or `statistical` KPI strip | 3-6 |
| `panel-large` | A wide chart panel (8/12 width) | `kpi-panel-grid`, `comparison`, `list` (top-N variant). Plus chart variants from `charts.md`. | up to 4 across the body |
| `panel-medium` | Half-width panel (6/12) | `kpi-panel-grid`, `comparison`, `list`. Plus chart variants (donut + legend, ranked list) from `charts.md`. | up to 6 |
| `panel-small` | Quarter-width panel (3/12) | `stat-spotlight` (with sparkline). Plus single chart or mini-bar from `charts.md`. | up to 8 |
| `footer` | Source / period note / data freshness | (built into canvas) | 1 |

Total widget cap by canvas size:

| Canvas width | Ideal widget count |
|---|---|
| 1080 (square / portrait) | 4-6 widgets |
| 1440 (landscape medium) | 8-10 widgets |
| 1920 (landscape wide) | 10-14 widgets |

Past the cap → split by category into multiple dashboards (e.g., "Protocol Health" + "User Growth").

## Page skeleton

```html
<div class="infographic-canvas dashboard-canvas">

  <header class="dash-header" data-section-id="header">
    <div>
      <span class="dash-period">{Q1 2026 · Week 14}</span>
      <h1 class="dash-title">{Project} Health Snapshot</h1>
    </div>
    <span class="dash-updated">Last updated {date}</span>
  </header>

  <div class="dashboard-grid">

    <!-- KPI row: 3-6 cells, each w-3 or w-4 -->
    <div class="widget kpi-widget w-3" data-section-id="kpi-tvl">
      <span class="widget-title">TVL</span>
      <div class="big-number-value">$42M</div>
      <div class="trend trend-up"><i class="ph-bold ph-trend-up"></i>+12%</div>
    </div>
    <!-- ...repeat for other KPIs... -->

    <!-- Body panels: mix of large/medium/small -->
    <div class="widget w-8" data-section-id="volume">
      <div class="widget-header"><span class="widget-title">Volume · 30d</span></div>
      <!-- snippet: line/area chart -->
    </div>
    <div class="widget w-4" data-section-id="top-chains">
      <div class="widget-header"><span class="widget-title">Top chains</span></div>
      <!-- snippet: horizontal bar chart -->
    </div>

    <div class="widget w-6" data-section-id="users"><!-- snippet --></div>
    <div class="widget w-6" data-section-id="assets"><!-- snippet --></div>

  </div>

  <footer class="dash-footer" data-section-id="footer">
    <span class="caption">Source: {data origin} · Refreshed {cadence}</span>
  </footer>
</div>
```

## Grid recipe

12-column base. Widget widths use `w-3 / w-4 / w-6 / w-8 / w-12` span classes.

```css
.dashboard-canvas {
  display: flex; flex-direction: column;
  gap: var(--gap-section);
  padding: 32px;
}
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
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
}
.kpi-widget .big-number-value {
  font: 400 48px/1 'Bebas Neue', sans-serif;
  color: var(--text-primary);
  margin: 4px 0 6px;
}
.trend {
  font: 700 11px/1 'Montserrat', sans-serif;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  display: inline-flex; align-items: center; gap: 4px;
}
.trend-up   { color: var(--positive); }
.trend-down { color: var(--negative); }

.dash-header {
  display: flex; justify-content: space-between; align-items: flex-end;
  padding-bottom: 16px;
  border-bottom: 1px solid color-mix(in srgb, var(--text-muted) 25%, transparent);
}
.dash-period {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--accent-1);
}
.dash-title {
  font: 400 36px/1 'Bebas Neue', sans-serif;
  text-transform: uppercase; letter-spacing: 0.04em;
  color: var(--text-primary);
  margin: 4px 0 0;
}
.dash-updated {
  font: 400 11px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
}
```

## Sizing

Dashboards shine in landscape — 12-col grid has breathing room.

| Use case | Width |
|---|---|
| Wide / TV display | 1920 |
| Standard | 1440 |
| Compact | 1080 (drop to 4-6 widgets) |
| **Never** | < 900 (12-col grid collapses to unreadable) |

## Composition rules

- **Visual rhythm: alternate sizes.** All-equal widgets feel flat. Mix `w-3 / w-6 / w-8`.
- **Top row = headline KPIs.** The 3-6 most important numbers. Always the first row, always span 3 (or 4 if 3 metrics).
- **Charts in the middle band.** Reading flow: headline → detail → breakdown.
- **Every widget has a tiny title** in `--text-muted` uppercase. The number does the talking.
- **Trend indicators on KPIs** (up/down with %) when a time dimension matters.
- **12-col grid only, never 3-col.** 12 divides cleanly into 2, 3, 4, 6 — gives layout flexibility.
- **One legend at the bottom, not per-widget.** If chart colors are consistent across widgets, render one legend strip in a `w-12` row near the footer.
- **Empty widgets are forbidden.** If a metric isn't available, drop the widget. Don't ship "TVL: --".

## Style inheritance

Default: `aizfographics-style`. Works well with `corporate` style (more restrained, less gradient) when the audience is exec/finance. Avoid `cyberpunk` / `chalkboard` / `hand-drawn` here — dashboards demand precision aesthetic.

## Anti-patterns

- Dashboard layout for 3 widgets → that's just a KPI strip. Use poster canvas.
- Mixing widget border treatments (some outlined, some filled) → consistency matters.
- Adding decorative dividers between widgets → the gap and gradient borders are the divider.
- Widget titles in primary text color (not muted) → competes with the number.
- Charts with no axis labels or units → numbers without context aren't snapshots.
