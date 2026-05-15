# Allocation Breakdown Template

Presents any allocation, distribution, or split: tokenomics, budget breakdowns, ownership splits, resource allocation, or any percentage-based division with supporting detail.

## When to use

User mentions any of: tokenomics, token economics, token distribution, vesting, supply allocation, TGE, FDV, token allocation, token breakdown, emission schedule, token launch, allocation chart.

## Canvas

`bento-box` (see `references/canvases/bento-box.md`) — hero strip with total supply + accent KPIs, then mixed-span cards for allocation, vesting, utility, and emissions.

## Snippets

`statistical` (KPI strip), `donut-chart` or `pie-chart` (allocation), `vesting-bar` (vesting schedule), `comparison` (utility breakdown).

## Default style

`aizfographics-style`

## Required elements

- `charts.md` — donut OR horizontal segmented bar
- `data-widgets.md` — big-number, KPI card, progress bar
- `connectors.md` — horizontal timeline spine (for vesting)
- `text.md` — all atoms
- `layout.md` — canvas, kpi-strip, grid recipes
- `decorative.md` — gradient borders, glow on key KPI, hero overlay
- `icons.md` — Phosphor Bold for KPI icons

## Section order

1. **Header strip** — project logo + "TOKENOMICS" badge
2. **Hero** — `{PROJECT}` gradient title + one-line subtitle
3. **Key metrics strip** — 3–4 KPIs: Total Supply, TGE Price, FDV, (optional) TGE Date
4. **Distribution chart** — donut (≤4 segments) OR horizontal segmented bar (5+ segments, or any segment >75%). Legend with allocation % + token amount per category.
5. **Vesting timeline** — horizontal timeline spine with 3–5 milestones (TGE, cliff ends, partial unlock, full unlock). Below: per-category vesting progress bars showing cliff + linear shape.
6. **Allocation detail cards** — one card per category with: name, percentage, token amount, vesting summary (cliff + schedule).
7. **Footer** — source/whitepaper version + project logo

## Content expectations (user should provide)

Required:
- Token name / ticker (e.g., $AIZ)
- Total supply
- Allocation categories with percentages (at least 3, ideally 4–6)

Strongly recommended:
- Vesting terms per category (cliff length, unlock schedule)

Nice-to-have:
- TGE date, initial price, FDV
- Project logo URL
- Source / document reference

If vesting terms aren't provided and the user says "standard" or "typical", apply sensible defaults and announce them:

> Using standard vesting: 12-month cliff for team/investors, linear 24-month unlock for community/ecosystem, linear 12-month for reserve. Override anything that doesn't match.

## Content rules

- Percentages in the chart must sum to exactly 100. If the user's numbers don't, ask — don't silently "fix" them.
- Token amounts: always formatted with commas (`1,000,000,000`) or short-form with units (`1B`). Pick one and be consistent.
- Dates in MMM YYYY or "Q1 2026" format. Never ambiguous ("soon", "later").

## Example content block (for Claude to fill in)

```
PROJECT: $AIZ
TOTAL SUPPLY: 1,000,000,000
TGE PRICE: $0.05
FDV: $50,000,000
TGE DATE: Q3 2026

ALLOCATIONS:
- Community: 40% (400M). TGE: 10%. Cliff: none. Unlock: linear 24 months.
- Ecosystem: 25% (250M). TGE: 5%. Cliff: none. Unlock: linear 36 months.
- Team: 20% (200M). TGE: 0%. Cliff: 12 months. Unlock: linear 24 months thereafter.
- Investors: 15% (150M). TGE: 0%. Cliff: 6 months. Unlock: linear 12 months thereafter.
```

## HTML skeleton (excerpt)

```html
<div class="infographic-canvas portrait-medium">

  <header class="section header-strip">
    <img src="{logo}" height="28" alt="{project}">
    <span class="badge">Tokenomics</span>
  </header>

  <section class="section hero">
    <div class="hero-bg"></div>
    <h1 class="hero-title gradient-text">{project}</h1>
    <p class="body">Token economics, distribution, and vesting.</p>
  </section>

  <section class="section kpi-strip" style="--kpi-count: 4;">
    <div class="kpi-card"><div class="kpi-icon"><i class="ph-bold ph-coins"></i></div>
      <div class="kpi-value">{total_supply}</div>
      <div class="kpi-label">Total supply</div>
    </div>
    <div class="kpi-card"><div class="kpi-icon"><i class="ph-bold ph-currency-circle-dollar"></i></div>
      <div class="kpi-value">${tge_price}</div>
      <div class="kpi-label">TGE price</div>
    </div>
    <div class="kpi-card"><div class="kpi-icon"><i class="ph-bold ph-chart-line-up"></i></div>
      <div class="kpi-value">${fdv}</div>
      <div class="kpi-label">FDV</div>
    </div>
    <div class="kpi-card"><div class="kpi-icon"><i class="ph-bold ph-calendar"></i></div>
      <div class="kpi-value">{tge_date}</div>
      <div class="kpi-label">TGE</div>
    </div>
  </section>

  <section class="section">
    <h2 class="section-title">Distribution</h2>
    <!-- donut OR segmented bar + legend -->
  </section>

  <section class="section">
    <h2 class="section-title">Vesting</h2>
    <!-- horizontal timeline + per-category progress bars -->
  </section>

  <section class="section">
    <h2 class="section-title">Allocation detail</h2>
    <div class="grid-2">
      <!-- one card per category: name, %, amount, vesting summary -->
    </div>
  </section>

  <footer class="footer">
    <span class="caption">Source: whitepaper v1.0</span>
    <img src="{logo}" height="20" alt="{project}">
  </footer>

</div>
```

## Accent pair selection

Default: pair #1 (`#F3A950` → `#F38150`, warm amber) — suits finance content.

Override to pair #3 (lime → gold) for DeFi / yield content.
Override to pair #6 (green → cyan) for protocol / infrastructure tokens.
Otherwise match the project's brand colors.

## Composition rules

- Chart is the visual anchor. Make sure it's large enough to read segment labels without zooming.
- KPI strip values lead with the most important metric (Total Supply) on the left.
- Timeline goes top-to-bottom in reading order: TGE always leftmost.
- Allocation detail cards sort by percentage, descending.
- If Community isn't the largest allocation, check with the user — it usually is, and reversal is often a data entry mistake.
