# Ecosystem Overview Template

Catalogs partners, integrations, deployments, or projects within a platform's ecosystem. Dense, information-heavy, category-grouped.

## When to use

User mentions any of: ecosystem, integrations, partners, partnerships, deployments, built on, chain overview, protocol catalogue, projects on X, who's building on.

## Base layout

`bento-box` (see `references/layouts/bento-box.md`) — hero strip + category cards of varied span. Each category becomes a bento card whose width reflects how many projects it holds; the most prominent category gets a wide card, smaller categories tile alongside.

**Layout fallback:** for very flat ecosystems with no category weighting, swap to `grid-cards` (categorized variant).

## Default style

`aizfographics-style`

## Required elements

- `text.md` — all atoms
- `layout.md` — canvas, grid recipes, section containers
- `decorative.md` — gradient borders on cards, accent dividers between categories
- `icons.md` — Phosphor Bold for category icons, Iconify for chain logos if needed
- Optionally `data-widgets.md` — if each project has a headline metric (TVL, users)

## Section order

Arranged as a hero card plus 2–3 rows of category cards.

1. **Hero card (full-bleed)** — platform logo + `{PLATFORM} ECOSYSTEM` title + subtitle (`{n} projects across {m} categories`) + 3–4 ecosystem KPIs inline (total projects, TVL, active users, categories)
2. **Category cards** — one bento card per category, sized to project count:
   - Largest category (10+ projects): wide card (`1 / 3` or `1 / -1`) with internal 3- or 4-column eco-card grid
   - Medium category (5–9 projects): half-width (`1 / 3` or `3 / 5`) with 2- or 3-column grid
   - Small category (≤ 4 projects): quarter-width single column
3. **Featured / spotlight card** (optional) — a tall sidebar (`grid-row: N / N+2`) highlighting one project with logo + 1-paragraph description
4. **Footer card (full-bleed)** — source/URL + attribution + last-updated date

## Content expectations

Required:
- Platform name (e.g., "Abstract")
- At least one category with 2+ projects
- For each project: name (logos strongly recommended, else styled placeholder)

Strongly recommended:
- Categories for grouping (DeFi, Gaming, NFTs, Infra, Wallets, etc.)
- One-line description per project

Nice-to-have:
- Logo URLs
- Category icons
- Per-project metrics

## Category guidance

Common categories for crypto ecosystems:

- DeFi (DEX, lending, yield, derivatives)
- Gaming (games, platforms, publishers)
- NFT (marketplaces, collections, tools)
- Infra (RPC, indexing, data, developer tools)
- Wallets
- Bridges
- Launchpads
- Social / community
- Oracles / data
- L2 / scaling

If the user gives a flat list without categories, ask whether to group — many lists have obvious groupings.

## Card content pattern

```
┌──────────────────────┐
│ [LOGO]  Relay        │
│         DEX / BRIDGE │
│                      │
│ Instant cross-chain  │
│ swaps on Abstract.   │
└──────────────────────┘
```

Logo top-left. Name uppercase. Category tag in accent-1 below name. Optional description in 1–2 body lines.

## Column counts by total projects

Per `grid-cards.md` adaptation rules. Within a category:

| Projects in category | Columns |
|---------------------|---------|
| 1–3 | 3 |
| 4–6 | 3 |
| 7–9 | 3 |
| 10+ | 4 (dense card variant) |

Keep column count consistent across categories within a single infographic.

## HTML skeleton (excerpt)

```html
<div class="infographic-canvas">
  <div class="bento-grid">

    <section class="section bento-card s1"><!-- hero: 1 / -1 -->
      <img src="{platform_logo}" height="28" alt="{platform}">
      <h1 class="hero-title gradient-text">{platform} Ecosystem</h1>
      <p class="body">{n} projects across {m} categories.</p>
      <div class="kpi-strip"><!-- 3-4 ecosystem KPIs --></div>
    </section>

    <!-- biggest category: wide card 1 / 3 -->
    <section class="section bento-card s2">
      <div class="cat-header">
        <span class="badge"><i class="ph-bold ph-currency-circle-dollar"></i> DeFi</span>
        <span class="caption">{count} projects</span>
      </div>
      <div class="grid-3"><!-- .eco-card per project --></div>
    </section>

    <!-- medium category: 3 / 5 -->
    <section class="section bento-card s3">
      <div class="cat-header"><span class="badge">Gaming</span></div>
      <div class="grid-2"><!-- .eco-card per project --></div>
    </section>

    <!-- small categories alongside -->
    <section class="section bento-card s4"><!-- NFTs --></section>
    <section class="section bento-card s5"><!-- Infra --></section>
    <section class="section bento-card s6"><!-- Wallets --></section>

    <footer class="section bento-card s7"><!-- footer: 1 / -1 -->
      <span class="caption">Updated {date}</span>
      <img src="{platform_logo}" height="20" alt="{platform}">
    </footer>

  </div>
</div>
```

## Accent pair selection

Default: pair #6 (green → cyan) — matches protocol / ecosystem energy.
Override to pair #1 (amber) for DeFi-heavy ecosystems.
Override to pair #4 (red → pink) for NFT-focused ecosystems.
Override to match the platform's brand.

## Dimension guidance

Bento ecosystem overviews are landscape-first.

- Default: **1920w wide**, content-driven height.
- Very dense (40+ projects across 6+ categories): keep 1920w; let height grow, or split into per-category standalones via §8.5.
- Compact / social variant only on explicit request: 1080w (collapses to a 2-column bento — works only for ≤ 12 projects).

## Composition rules

- Every card in a category has the same fields in the same order.
- Logos should all be square or padded to square. Don't stretch.
- Category ordering: most prominent first, or alphabetical. Pick one and be consistent across infographics in a series.
- One accent color pair for the whole infographic. Don't color-code categories unless that's the whole point of the visual.
- If the ecosystem has 40+ projects, consider splitting into multiple infographics (e.g., "DeFi" standalone, "Gaming" standalone).
