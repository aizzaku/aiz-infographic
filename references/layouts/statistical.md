# Statistical Layout

Hero chart + KPI strip + callout cards. Data-heavy infographics where one or two key metrics anchor the composition.

## When to use

- Tokenomics distribution
- Protocol stats / ecosystem metrics
- Data stories with one primary chart
- Any content where 3–6 KPIs and one hero chart are the core payload

## Required elements

`charts.md`, `data-widgets.md`, `text.md`, `layout.md`, `decorative.md`, `connectors.md` (timeline only if vesting), `icons.md`

## Section order (portrait 3:4, default)

```
┌──────────────────────────────────┐
│ Header strip                     │  logo + title + type badge
├──────────────────────────────────┤
│ Hero section                     │  big title (gradient) + subtitle
├──────────────────────────────────┤
│ KPI strip (3–6 cells)            │  Total / Price / FDV / etc.
├──────────────────────────────────┤
│ Hero chart + legend/callouts     │  donut OR horizontal segmented bar
├──────────────────────────────────┤
│ Supporting section(s)            │  timeline / detail cards / progress
├──────────────────────────────────┤
│ Footer                           │  source + attribution + logo
└──────────────────────────────────┘
```

## Grid specifications

Portrait medium (1080 × 1440):
- Outer padding: 20px
- Section gap: 32px
- Hero section: `flex` column, min-height ~160px
- KPI strip: 3–4 cells → `.kpi-strip { --kpi-count: <n> }`
- Hero chart area: 2-col asymmetric (chart 60% / legend 40%) OR full-width segmented bar
- Footer: fixed at bottom with `margin-top: auto`

Landscape 16:9 variant:
- Header, hero, KPI strip stay on top
- Chart + supporting content side-by-side (60/40)
- Footer full-width at bottom

## Adaptation rules

| Data size | Response |
|-----------|----------|
| 3 KPIs | `.kpi-strip { --kpi-count: 3 }`, chart becomes larger |
| 4–5 KPIs | `.kpi-strip { --kpi-count: 4 }`, drop 5th into supporting section |
| 6+ KPIs | Split across 2 rows OR drop lowest-priority metrics |
| 3–4 chart segments | Donut with center metric, legend to the right |
| 5–8 chart segments | Horizontal segmented bar full-width, legend below |
| >8 segments | Group into "Other" bucket OR switch to horizontal bar chart |
| Any segment >75% | Switch from donut to horizontal segmented bar |

## HTML skeleton

```html
<div class="infographic-canvas portrait-medium">
  <header class="section hgroup header-strip">
    <div class="brand"><img src="{logo}" alt="{project}" height="28"></div>
    <span class="badge">Tokenomics</span>
  </header>

  <section class="section hero">
    <div class="hero-bg"></div>
    <h1 class="hero-title gradient-text">{project} Economics</h1>
    <p class="body">Supply, distribution, and vesting at a glance.</p>
  </section>

  <section class="section kpi-strip" style="--kpi-count: 4;">
    <!-- 3-6 .kpi-card elements -->
  </section>

  <section class="section">
    <h2 class="section-title">Distribution</h2>
    <div class="grid-2-asym">
      <!-- chart: donut OR segmented bar -->
      <!-- legend OR stacked info cards -->
    </div>
  </section>

  <section class="section">
    <h2 class="section-title">Vesting</h2>
    <!-- timeline OR progress bars -->
  </section>

  <footer class="footer">
    <span class="caption">Source: whitepaper v1.0</span>
    <img src="{logo}" alt="{project}" height="20">
  </footer>
</div>
```

## Composition rules

- Hero title is the single biggest text. Nothing competes.
- KPI strip values use the display font; labels use body font uppercase.
- Chart lives above the fold — visible without scrolling in viewport.
- At most 2 supporting sections after the chart. If more data, split into a second infographic.
- Footer always present, always subtle (`text-muted`).

## Visual weight distribution

- Hero: ~15% of canvas height
- KPI strip: ~12%
- Hero chart area: ~35% (dominant)
- Supporting section(s): ~30%
- Footer: ~5%
- Gaps + padding: ~3%
