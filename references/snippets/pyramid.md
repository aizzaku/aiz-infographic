# Pyramid Snippet

Stacked tiers with implied scale hierarchy. Wider at base, narrower at top (or inverted). "Foundation → peak" metaphor.

## When to use

- Maturity levels (foundation → intermediate → advanced)
- Market segmentation (TAM → SAM → SOM, inverted)
- Needs hierarchy (basics → growth → self-actualization)
- Token holder tiers (holders → stakers → governors)
- Reward tiers, rank ladders

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| poster | centerpiece | Best — pyramid is portrait-leaning hero |
| bento-box | card-tall | Vertical pyramid as a tall sidebar |
| editorial | sidebar | Mini pyramid as supporting visual |

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`. Optional `data-widgets.md` for per-tier counts.

## HTML pattern (CSS clip-path trapezoids stacked)

```html
<div class="pyramid">
  <div class="ptier" style="--width: 40; --shade: 100%;">
    <div class="ptier-bar"></div>
    <div class="ptier-meta">
      <div class="ptier-title">Governors</div>
      <div class="ptier-count">~250</div>
    </div>
  </div>
  <div class="ptier" style="--width: 65; --shade: 65%;">
    <div class="ptier-bar"></div>
    <div class="ptier-meta">
      <div class="ptier-title">Stakers</div>
      <div class="ptier-count">~4,200</div>
    </div>
  </div>
  <div class="ptier" style="--width: 100; --shade: 35%;">
    <div class="ptier-bar"></div>
    <div class="ptier-meta">
      <div class="ptier-title">Holders</div>
      <div class="ptier-count">~48,000</div>
    </div>
  </div>
</div>

<style>
.pyramid { display: flex; flex-direction: column; gap: 4px; }
.ptier {
  display: grid;
  grid-template-columns: 1fr 220px;
  gap: 16px; align-items: center;
}
.ptier-bar {
  height: 64px;
  width: calc(var(--width) * 1%);
  margin: 0 auto;
  /* mono-accent shade ladder per parts-of-a-whole rule (see charts.md) */
  background: color-mix(in srgb, var(--accent-1) var(--shade), var(--canvas));
  clip-path: polygon(10% 0, 90% 0, 100% 100%, 0 100%);
}
.ptier:first-child .ptier-bar {
  clip-path: polygon(25% 0, 75% 0, 100% 100%, 0 100%);
  box-shadow: 0 0 24px color-mix(in srgb, var(--accent-1) 25%, transparent);
}
.ptier-title {
  font: 700 16px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.05em;
  color: var(--text-primary);
}
.ptier-count {
  font: 400 22px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
}
</style>
```

## Inverted variant

For TAM/SAM/SOM (narrowing-at-bottom), set `flex-direction: column-reverse;` and adjust clip-paths. Note: this overlaps with `funnel` — prefer funnel when there's an explicit conversion narrative.

## Composition rules

- 3-5 tiers standard. 6+ tiers stack too thin.
- Widths monotonic — each tier wider (or narrower) than the previous.
- Counts or %s on every tier. Pyramid without scale is meaningless.
- Per-tier body on the side, not inside the trapezoid (text inside gets clipped).
- Top tier is special: stronger color, slight glow.

## Anti-patterns

- Roughly equal widths → pyramid metaphor breaks. Use list.
- 6+ tiers.
- Long labels inside trapezoids (clipping). Side-label always.
