# Grid Cards Layout

N items (optionally grouped into categories) in an equal-weight grid. The workhorse layout for ecosystem overviews, cheatsheets, feature rosters, and dense reference material.

## When to use

- Ecosystem directories (partners, integrations, deployments)
- Cheatsheets (equal-weight tips or items)
- NFT collections / trait showcases
- Feature catalogues
- Any content where items are parallel, not hierarchical

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`, optionally `data-widgets.md` for per-card metrics.

## Structural variants

### Flat grid (no categories)

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│ ┌──┐ ┌──┐ ┌──┐ ┌──┐          │
│ └──┘ └──┘ └──┘ └──┘          │
│ ┌──┐ ┌──┐ ┌──┐ ┌──┐          │  repeating cards
│ └──┘ └──┘ └──┘ └──┘          │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

### Categorized grid (preferred for ecosystems)

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│ [CATEGORY BADGE]             │
│ ┌──┐ ┌──┐ ┌──┐               │
│ └──┘ └──┘ └──┘               │
├──────────────────────────────┤
│ [CATEGORY BADGE]             │
│ ┌──┐ ┌──┐ ┌──┐               │
│ └──┘ └──┘ └──┘               │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## Grid specifications

Column count by item count:

| Items | Columns (portrait) | Columns (landscape) |
|-------|-------------------|---------------------|
| 3 | 3 | 3 |
| 4 | 2 | 4 |
| 5–6 | 2 or 3 | 3 |
| 7–9 | 3 | 3 |
| 10–12 | 3 | 4 |
| 13–16 | 4 (dense) | 4 |
| 17+ | 4 dense OR split into themed sections |

Card gap: 12px default (compact). 16px for sparse layouts.

## Card variants

### Logo + name + one-line description (ecosystem default)

```html
<div class="eco-card">
  <div class="eco-logo"><img src="{logo}" alt="{name}"></div>
  <div class="eco-name">{name}</div>
  <div class="eco-tag">{category}</div>
  <p class="caption">{one-line description}</p>
</div>

<style>
.eco-card {
  padding: 14px;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 18%, transparent),
      color-mix(in srgb, var(--accent-1) 36%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
  display: flex; flex-direction: column; gap: 6px;
}
.eco-logo {
  width: 40px; height: 40px;
  border-radius: 8px;
  overflow: hidden;
  background: var(--elevated);
  display: flex; align-items: center; justify-content: center;
}
.eco-logo img { width: 100%; height: 100%; object-fit: cover; }
.eco-name {
  font: 700 14px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.04em;
  color: var(--text-primary);
}
.eco-tag {
  font: 700 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--accent-1);
}
</style>
```

### Tip card (cheatsheet dense)

```html
<div class="tip-card">
  <div class="tip-icon"><i class="ph-bold ph-lightning"></i></div>
  <div class="tip-title">Stake early</div>
  <p class="tip-body">Earlier stakers compound higher multiplier bonuses in the first 30 days.</p>
</div>
```

## Category section

```html
<section class="section">
  <div class="cat-header">
    <span class="badge">DeFi</span>
    <span class="caption">{count} projects</span>
  </div>
  <div class="grid-3">
    <!-- eco-cards -->
  </div>
</section>
```

## Adaptation rules

- ≤6 items: single grid, no categories, 2–3 columns.
- 7–12 items, 2–3 categories: one small category badge per group.
- 13+ items: always categorize. Never show a flat grid of 16 unrelated items.
- Dense variant (cheatsheets): reduce card padding to 10px and gap to 8px.
- If item names vary wildly in length, set `grid-auto-rows: 1fr` to keep cards equal-height.

## Rules

- Every card has the same fields in the same order. Inconsistency is the fastest way to kill a grid.
- If any field is optional per item, still reserve the vertical space (use `&nbsp;` or visibility:hidden) so rows align.
- Logos are square (40×40 typical). Pad the non-square ones; don't stretch them.
- Category badges use `--accent-1`. Subcategory tags inside cards use `--accent-2` or `text-secondary` — never full accent or the grid drowns.
