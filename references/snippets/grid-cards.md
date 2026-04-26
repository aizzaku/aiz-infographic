# Grid Cards Snippet

Equal-weight items in a tiled grid. The workhorse for ecosystems, cheatsheets, feature rosters.

## When to use

- Ecosystem directories (partners, integrations, deployments)
- Cheatsheets (equal-weight tips)
- NFT collections / trait showcases
- Feature catalogues — items that are parallel, not hierarchical

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| bento-box | card-wide / card-medium / card-tall | A bento card hosting a sub-grid (3-9 items) |
| editorial | body-column | Inline figure with 4-9 cards |
| dashboard | panel-large (w-12) | Full-width grid of widget-like cards |
| poster | centerpiece | Grid of 9-16 cards as the hero (when no single diagram fits) |
| poster | support-card | Stack of 2-4 mini cards |

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`. Optional `data-widgets.md` for per-card metrics.

## Column count by item count

| Items | Portrait slot | Landscape slot |
|---|---|---|
| 3 | 3 | 3 |
| 4 | 2 | 4 |
| 5-6 | 2 or 3 | 3 |
| 7-9 | 3 | 3 |
| 10-12 | 3 | 4 |
| 13-16 | 4 (dense) | 4 |
| 17+ | Group into themed sections, never a flat 17+ grid |

Card gap: 12px default. 16px for sparse layouts.

## Logo + name + description card (ecosystem)

```html
<div class="grid grid-3">
  <div class="eco-card">
    <div class="eco-logo"><img src="{logo}" alt="{name}"></div>
    <div class="eco-name">{name}</div>
    <div class="eco-tag">{category}</div>
    <p class="caption">{one-line description}</p>
  </div>
  <!-- repeat -->
</div>

<style>
.grid { display: grid; gap: var(--gap-card); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }
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

## Tip card (cheatsheet dense)

```html
<div class="tip-card">
  <div class="tip-icon"><i class="ph-bold ph-lightning"></i></div>
  <div class="tip-title">Stake early</div>
  <p class="tip-body">Earlier stakers compound higher multiplier bonuses in the first 30 days.</p>
</div>
```

## Categorized variant (ecosystems)

```html
<div class="cat-section">
  <div class="cat-header">
    <span class="badge">DeFi</span>
    <span class="caption">{count} projects</span>
  </div>
  <div class="grid grid-3">
    <!-- eco-cards -->
  </div>
</div>
```

## Composition rules

- Every card has the same fields in the same order. Inconsistency kills a grid.
- Reserve vertical space for optional fields (`&nbsp;` or `visibility:hidden`) so rows align.
- Logos are square (40×40 typical). Pad non-square ones; never stretch.
- Category badges use `--accent-1`; subcategory tags use `--accent-2` or `--text-secondary` — never full accent or the grid drowns.
- ≤ 6 items: no categories. 7-12: optional. 13+: always categorize.

## Anti-patterns

- Mixing card sizes within one grid → that's bento, not grid-cards.
- Stretched logos → pad to square aspect.
- Empty cards as filler → drop the card or fill the field properly.
