# Report Template

Periodic snapshot / recap. Weekly, monthly, quarterly, or seasonal summary of numbers + highlights. Visual "State of X" piece.

## When to use

User mentions: weekly report, monthly report, recap, season recap, state of X, quarterly summary, update, digest, year in review.

## Canvas

`bento-box` (see `references/canvases/bento-box.md`) — hero strip with the period + headline KPIs, then bento cards for metric details, highlights, and "up next" callouts. Heavier metrics get wider cards; the highlights list becomes a tall sidebar.

## Snippets

`statistical` (hero KPIs), `chart` (metric details, mini line/bar/area), `list` (highlights), `timeline` (period trend, optional), `callout-block` ("up next").

**Canvas fallback:** for pure metrics-focused reports without narrative, use `dashboard` canvas instead with the same snippets.

## Default style

`aizfographics-style` or `corporate` for investor-facing reports.

## Required elements

- `text.md`, `layout.md`, `decorative.md`, `icons.md`
- `data-widgets.md` — KPI cards everywhere
- `charts.md` — mini line/bar charts for trends
- Optionally `connectors.md` for timeline

## Section order

Arranged as a hero card plus 2–3 rows of metric and highlight cards.

1. **Hero card (full-bleed)** — project logo + report title + period stamp + 4 top KPIs inline with WoW/MoM/QoQ deltas
2. **Metric detail row** — 2–3 medium cards each containing a mini chart (line/bar) + title + 1-line takeaway. Hot metric gets a wide card (`1 / 3`); supporting metrics tile alongside.
3. **Highlights card (tall sidebar)** — `grid-row: N / N+2` listing 3–5 highlights (icon + title + 1-sentence body)
4. **Secondary metric cards** — small cards under the metric detail row for any remaining KPIs
5. **Up next card (medium)** — 2–3 forward-looking bullets
6. **Footer card (full-bleed)** — attribution, methodology link, next report date

## Content expectations

Required:
- Reporting period (e.g., "Week 47, 2026" or "Oct 2026")
- Key metrics with current value and change vs previous period
- At least 3 highlights

Strongly recommended:
- Mini charts showing trend within the period
- "Up next" forward-looking items
- Methodology / data source note

## Period stamp pattern

```html
<div class="period-stamp">
  <span class="period-label">Week 47</span>
  <span class="period-dates">Nov 17 – Nov 23, 2026</span>
</div>

<style>
.period-stamp {
  display: flex; flex-direction: column; gap: 2px;
  text-align: right;
}
.period-label {
  font: 700 16px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent-1);
}
.period-dates {
  font: 400 11px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
}
</style>
```

## KPI with period-over-period delta

```html
<div class="kpi-card">
  <div class="widget-header">
    <span class="widget-title">Daily active users</span>
  </div>
  <div class="big-number-value">12,840</div>
  <div class="trend trend-up">
    <i class="ph-bold ph-trend-up"></i> +18% WoW
  </div>
</div>
```

"WoW" (week-over-week), "MoM" (month-over-month), "QoQ" (quarter-over-quarter) — pick the correct abbreviation for the period.

## Highlights block pattern

```html
<section class="section">
  <h2 class="section-title">Highlights</h2>
  <ul class="highlight-list">
    <li class="highlight">
      <span class="highlight-icon"><i class="ph-bold ph-rocket-launch"></i></span>
      <div>
        <h4 class="card-title">Mainnet launch completed</h4>
        <p class="body">First 24h: {stat}. {one-sentence context}.</p>
      </div>
    </li>
    <!-- repeat -->
  </ul>
</section>
```

## Content rules

- **Deltas require comparable baselines.** "+18% WoW" means comparing to week 46. State the base period when it's ambiguous.
- **Don't bury bad numbers.** Report reliability depends on showing declines honestly. Use `trend-down` with the negative semantic color.
- **Period-over-period ONLY when applicable.** Launch-week reports have no baseline — drop the delta, just show absolutes.
- **Highlights are 1-sentence bodies.** If a highlight needs a paragraph, it's its own blog post.

## Accent pair selection

Default: match project's brand palette.
Fallback to pair #1 (amber) for financial-heavy reports, pair #6 (green → cyan) for protocol/tech reports.

## Dimension guidance

Bento reports are landscape-first.

- Default: **1920w wide**, content-driven height — works for weekly, monthly, and quarterly recaps.
- Highlights-rich reports (10+ items): keep 1920w; add a second highlights card or extract highlights as a standalone via §8.5.
- Compact weekly digest only on explicit request: 1080w (collapses bento to 2 columns).
