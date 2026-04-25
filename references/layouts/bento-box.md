# Bento-Box Layout

Heterogeneous content arranged as a hero strip plus mixed-span cards. Cards differ in size, weighted to content density. Designed to fit a wide release recap, product overview, or dense feature tour onto a single landscape canvas without forcing every section to full width.

## When to use

- Release recaps and changelogs (one hero + many feature cards of varying weight)
- Product / agent / app overviews (mix of stats, feature lists, code blocks, callouts)
- Comprehensive cheatsheets where some tips are heavier than others
- Ecosystem snapshots with a hero category and supporting micro-cards
- Anything with 6–12 heterogeneous sections that would otherwise stack into a tall, repetitive scroll

## When NOT to use

- Single-flow content — use `timeline`, `process-flow`, `funnel`, `journey-path`
- Side-by-side comparisons — use `comparison`
- Anything with cross-cell connectors / arrows / leaders — bento uses fluid grid; use a pixel-locked layout (`flowchart`, `swimlane`, `fishbone`, `quadrant`) instead
- Equal-weight item catalogs — use `grid-cards` (12 identical tiles is not bento, it's a grid)

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`, `data-widgets.md`. Optionally `charts.md` for embedded mini-charts in cards.

## Structure

```
┌──────────────────────────────────────────────────────────┐
│ HERO (full-width: 1 / -1)                                │
│   title · meta · 3–4 inline KPIs                         │
├──────────────────┬─────────────────┬─────────────────────┤
│ wide card (1/3)  │ med (3)         │ med (4)             │
├──────────────────┴────────┬────────┴────────┬────────────┤
│ wide (1/3)                │ tall (3,r3/r5)  │ tall (4,r3/r5) │
├──────────┬────────┬───────┘                 │            │
│ sm (1)   │ sm (2) │ sm (3)                  │            │
├──────────┴────────┴─────────────────────────┴────────────┤
│ FOOTER (full-width: 1 / -1, optional)                    │
└──────────────────────────────────────────────────────────┘
```

## Grid structure

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: auto;
  gap: 16px;
  padding: 32px;
}
```

Use a 4-column base. For very dense layouts, switch to 6 columns and let cards span 2/3/4/6.

### Span recipes

| Pattern | Placement |
|---------|-----------|
| Hero / footer (full bleed) | `grid-column: 1 / -1` |
| Two-up row (50/50) | `1 / 3` + `3 / 5` |
| Wide + two small (50/25/25) | `1 / 3` + `3` + `4` |
| Small + wide + small (25/50/25) | `1` + `2 / 4` + `4` |
| Four KPIs | `span 1` × 4 |
| Tall sidebar (spans two rows) | `grid-column: 4; grid-row: N / N+2` |
| Wide + tall sidebar | `1 / 4` (wide) + `4 / -1, row N / N+2` (tall) |

Place each card with explicit `grid-column` / `grid-row` declarations on per-section classes (`.s1`, `.s2`, …). Don't rely on auto-flow — content order rarely matches visual order.

## Card base

Reuse the gradient-border card pattern from `aizfographics-style`. Every bento card starts from this skeleton:

```css
.bento-card {
  padding: 28px;
  border-radius: var(--radius-card);
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 22%, transparent),
      color-mix(in srgb, var(--accent-1) 44%, transparent)) border-box;
  border: 1px solid transparent;
  box-shadow: 0 0 32px color-mix(in srgb, var(--accent-1) 6%, transparent);
  display: flex;
  flex-direction: column;
  gap: var(--gap-element);
}
```

Hero card variants can swap the inner background for `var(--elevated)` and add a radial vignette for emphasis. Tall sidebar cards stay on `--panel` to read as quieter.

## Card content patterns

Each card is self-contained — title + body + optional list/widget — and never references another card via connectors. Common interior shapes:

- **Title + paragraph** — feature explainer
- **Title + bulleted feature list** — sub-feature roster (icon + label + sub-line per row)
- **Title + KPI big-number + caption** — single-stat callout
- **Title + mini chart + legend strip** — embedded chart card
- **Title + code block / shell-hook list** — technical reference
- **Hero card** — display-font title + subtitle + inline KPI strip (3–4 metrics on the right)

## Composition rules

- **One hero, always.** First row is full-bleed and carries the title, eyebrow/version meta, and 2–4 inline KPIs. No exceptions.
- **Vary card sizes by content weight.** A card with 8 features deserves more columns than a card with 1 stat. If every card is the same size, switch to `grid-cards`.
- **Cap at ~12 cells total** (1 hero + up to 11 secondary). Past that, split into a second infographic or promote dense cards to standalone via §8.5.
- **No cross-card connectors.** Bento is intentionally non-connected. If sections need arrows between them, use a pixel-locked layout instead.
- **Group adjacent rows by theme** when possible — KPI row, then feature row, then ecosystem row. The grid is heterogeneous; the reading flow shouldn't be.
- **Footer is optional.** A full-bleed footer card is fine; an unceremonious bottom edge is also fine.
- **No fixed aspect ratio on the canvas.** Height grows with rows. The `min-height: 100vh` rule from §6 still applies.
- **Fluid grid only — not pixel-locked.** Bento has no overlay arrows that need pixel alignment, so the SKILL.md §6 pixel-lock rule does not apply here. Cards reflow within their span; that's the whole point.

## Density budget

| Slot | Cap |
|------|-----|
| Hero | 1 |
| Secondary cards | ≤ 11 |
| Total cells | ≤ 12 |
| Accent-emphasis cards | ≤ 3 (hero counts as 1) |

Past 12 cells, split into a second bento infographic (e.g., "Hermes v0.11 — Core" + "Hermes v0.11 — Plugins") rather than shrinking cards.

## Example skeleton

```html
<div class="infographic-canvas">
  <div class="bento-grid">

    <section class="section bento-card s1">
      <div class="hero-inner">
        <div class="hero-text-block">
          <span class="hero-eyebrow">v0.11.0</span>
          <h1 class="hero-title">Project Title</h1>
          <p class="hero-tagline">One-line release description.</p>
        </div>
        <div class="kpi-strip">
          <div class="kpi-card"><span class="kpi-value">748</span><span class="kpi-label">Pull Requests</span></div>
          <div class="kpi-card"><span class="kpi-value">1,530</span><span class="kpi-label">Commits</span></div>
          <div class="kpi-card"><span class="kpi-value">29</span><span class="kpi-label">Contributors</span></div>
        </div>
      </div>
    </section>

    <section class="section bento-card s2"><!-- wide feature: 1 / 3 --></section>
    <section class="section bento-card s3"><!-- med:        3     --></section>
    <section class="section bento-card s4"><!-- med:        4     --></section>

    <section class="section bento-card s5"><!-- small:      1     --></section>
    <section class="section bento-card s6"><!-- wide:       2 / 4 --></section>
    <section class="section bento-card s7"><!-- tall:       4, r3/r5 --></section>

    <section class="section bento-card s8"><!-- small:      1     --></section>
    <section class="section bento-card s9"><!-- small:      2     --></section>
    <section class="section bento-card s10"><!-- small:     3     --></section>

  </div>
</div>

<style>
  .s1  { grid-column: 1 / -1; grid-row: 1; }
  .s2  { grid-column: 1 / 3;  grid-row: 2; }
  .s3  { grid-column: 3;      grid-row: 2; }
  .s4  { grid-column: 4;      grid-row: 2; }
  .s5  { grid-column: 1;      grid-row: 3; }
  .s6  { grid-column: 2 / 4;  grid-row: 3; }
  .s7  { grid-column: 4;      grid-row: 3 / 5; }
  .s8  { grid-column: 1;      grid-row: 4; }
  .s9  { grid-column: 2;      grid-row: 4; }
  .s10 { grid-column: 3;      grid-row: 4; }
</style>
```

## Adaptation rules

- **6–8 cells:** 4-column base, hero + 2 rows of mixed spans. No tall sidebars needed.
- **9–12 cells:** 4-column base, hero + 3–4 rows. Introduce one tall sidebar to break monotony.
- **Wide canvas (1920+):** 4-column base reads well. Consider 6-column base only when cells are very small (KPI-only).
- **Narrow canvas (1080):** drop to 2-column base — bento with too few columns at 1080 looks like a list.
- **Footer:** full-bleed final row (`1 / -1`) with attribution, source URL, and "full changelog" link is the canonical close.

## Accent emphasis

Apply gradient-text to the hero title and any one or two "headline" card titles. Keep the rest on `--text-primary`. Never gradient every title — bento depends on visual hierarchy between cards, and uniform gradients flatten it.

## Anti-patterns

- 12 identical cells with no hero → that's `grid-cards`, not bento.
- Cards spanning random rows without alignment to a column edge → reads as broken, not bento.
- Cross-card arrows, leaders, or "see also" connectors → pick a pixel-locked layout instead.
- Mixed card padding (some 16px, some 32px) within one infographic → keep `--pad-card` consistent.
- More than 3 accented cards → drowns the hero.
