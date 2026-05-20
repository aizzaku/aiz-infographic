# Callout Grid Snippet

Icon + headline + body cards arranged in a 2-3 column responsive grid. The most common dark-theme layout primitive for feature highlights, benefit lists, and category breakdowns.

## When to use

- Feature highlights (3-9 items with distinct icons)
- Benefit cards / value propositions
- Category breakdowns where each item warrants a short description
- Ecosystem category panels (when items are equal-weight, no hierarchy)

Do NOT use when items need hierarchy (use `hierarchical`), comparison (use `comparison`), or when there are more than 9 items (split into two grids or use `grid-cards`).

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| bento-box | card-wide (`1/-1`) | Full-bleed callout grid as a section |
| bento-box | card-span-2 | Half-width grid, 2-col layout |
| editorial | body-column | Full-width body column grid |
| poster | support-card | 2-3 card row in support area |
| dashboard | panel | Fills a panel slot |

## Density cap

3-9 cards. Grid reflows:
- 9 cards → 3-col grid
- 6 cards → 3-col grid
- 4-5 cards → 2-col grid (or 3+2 with last row justified left)
- 3 cards → 3-col grid

## Required elements

`icons.md`, `text.md`, `layout.md`

## HTML pattern

```html
<section class="callout-grid">
  <div class="callout-card">
    <i class="ph-bold ph-lightning" aria-hidden="true"></i>
    <h3 class="callout-title">Fast Finality</h3>
    <p class="callout-body">Transactions confirm in under 400ms using optimistic rollup sequencing.</p>
  </div>
  <div class="callout-card">
    <i class="ph-bold ph-lock-key" aria-hidden="true"></i>
    <h3 class="callout-title">Native Security</h3>
    <p class="callout-body">ZK proofs verify state transitions without trusting the sequencer.</p>
  </div>
  <div class="callout-card">
    <i class="ph-bold ph-tree-structure" aria-hidden="true"></i>
    <h3 class="callout-title">Modular Stack</h3>
    <p class="callout-body">Swap DA layers, execution environments, and settlement chains independently.</p>
  </div>
  <!-- repeat .callout-card up to 9 total -->
</section>

<style>
.callout-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--gap-card, 12px);
}

.callout-card {
  padding: 20px;
  background: var(--panel);
  border-radius: var(--radius-card, 10px);
  border: 1px solid transparent;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 15%, transparent),
      color-mix(in srgb, var(--accent-1) 30%, transparent)) border-box;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.callout-card i,
.callout-card .ph {
  font-size: 28px;
  color: var(--accent-1);
  line-height: 1;
}

.callout-title {
  margin: 0;
  font: 700 15px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-primary);
}

.callout-body {
  margin: 0;
  font: 400 13px/1.5 'Montserrat', sans-serif;
  color: var(--text-secondary);
}
</style>
```

## Forcing column count

When `auto-fit` reflow doesn't match content (e.g., 6 cards but want exactly 2 cols):

```css
/* 2-column forced */
.callout-grid.cols-2 {
  grid-template-columns: repeat(2, 1fr);
}
/* 3-column forced */
.callout-grid.cols-3 {
  grid-template-columns: repeat(3, 1fr);
}
```

## Theme adaptations

### Terminal theme

Remove card border and background radius. Use box-drawing instead of icons.

```css
/* terminal override */
.callout-grid { gap: 0; border: 1px solid #30363D; }
.callout-card {
  background: #161B22;
  border: none;
  border-bottom: 1px solid #30363D;
  border-radius: 0;
  padding: 16px;
}
.callout-card:last-child { border-bottom: none; }
.callout-card i { display: none; } /* no icons in terminal */
.callout-title { font-family: monospace; color: #3FB950; }
.callout-body  { font-family: monospace; color: #8B949E; }
```

### Forge theme

Hard rectangles, compressed padding, no icon.

```css
.callout-card {
  border-radius: 0;
  padding: 12px;
  border: 1px solid #2A1800;
  background: #150D05;
}
.callout-title { color: #F0A050; font-family: monospace; }
.callout-body  { color: #6B4A20; font-family: monospace; font-size: 11px; }
```

### Glasspaper theme

Semi-transparent card fill, no hard border.

```css
.callout-card {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 7px;
  background: rgba(255,255,255,0.06);
}
.callout-title { color: #C9B8F0; }
.callout-body  { color: #8AB4D4; }
```

## Composition rules

- One icon per card. The icon must be Phosphor Bold — no emoji, no custom SVG icons.
- Never give the icon a background circle, border, or container tile (see `icons.md` icon rule).
- Headline is 2-5 words, uppercase. Body is 1-2 sentences, sentence case.
- All cards in the grid are equal-weight — no focal card in a callout grid. For hierarchy, use a different snippet.

## Anti-patterns

- More than 9 cards in one grid — split into two sections or switch to `grid-cards`
- Icon badge or circular icon container — icons render directly on the card surface
- Emoji as icons
- Long body copy (>3 sentences per card) — truncate or use a different layout
- Mixed card heights due to unequal copy — use `align-items: start` on grid, not `stretch`, if heights vary dramatically
