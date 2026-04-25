# Pyramid Layout

Stacked tiers with implied hierarchy or volume. Wider at the base, narrower at the top (or inverted). Classic Maslow-style visualization — strong metaphor for "foundation → peak" narratives.

## When to use

- Maturity levels (foundation → intermediate → advanced)
- Market segmentation (TAM → SAM → SOM, inverted)
- Needs hierarchy (basics → growth → self-actualization)
- Token holder tiers (holders → stakers → governors → delegates)
- Reward tiers, rank ladders

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`, optionally `data-widgets.md` for per-tier metrics.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│         ▲                    │
│        ▲ ▲    TOP            │
│       ▲   ▲                  │
│      ▲─────▲  MIDDLE         │
│     ▲       ▲                │
│    ▲─────────▲ BASE          │
├──────────────────────────────┤
│ Per-tier detail              │  optional side cards
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## HTML pattern (CSS trapezoids stacked)

```html
<div class="pyramid">
  <div class="ptier" style="--width: 40;">
    <div class="ptier-bar"></div>
    <div class="ptier-meta">
      <div class="ptier-title">Governors</div>
      <div class="ptier-count">~250</div>
    </div>
  </div>
  <div class="ptier" style="--width: 65;">
    <div class="ptier-bar"></div>
    <div class="ptier-meta">
      <div class="ptier-title">Stakers</div>
      <div class="ptier-count">~4,200</div>
    </div>
  </div>
  <div class="ptier" style="--width: 100;">
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
  gap: 16px;
  align-items: center;
}
.ptier-bar {
  height: 64px;
  width: calc(var(--width) * 1%);
  margin: 0 auto;
  background: linear-gradient(90deg, var(--accent-1), var(--accent-2));
  clip-path: polygon(10% 0, 90% 0, 100% 100%, 0 100%);
  box-shadow: 0 0 24px color-mix(in srgb, var(--accent-1) 12%, transparent);
}
.ptier:first-child .ptier-bar {
  clip-path: polygon(25% 0, 75% 0, 100% 100%, 0 100%);
}
.ptier-title {
  font: 700 16px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-primary);
}
.ptier-count {
  font: 400 22px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
}
</style>
```

## Inverted pyramid (funnel-like)

For narrowing-at-bottom (e.g., TAM/SAM/SOM), flip by setting `flex-direction: column-reverse;` and adjusting clip-paths. Note: this overlaps visually with `funnel.md` — prefer funnel when there's an explicit conversion narrative.

## Composition rules

- **3–5 tiers standard.** 6+ tiers stack too thin.
- **Widths monotonic.** Each tier wider (or narrower) than the previous.
- **Counts or %s on every tier.** A pyramid without scale is meaningless.
- **Per-tier body** on the side, not inside the trapezoid. Text inside gets clipped.
- **Top tier is special.** Stronger color, slight glow.

## Anti-patterns

- Don't use pyramid when widths are roughly equal. The shape exists to show hierarchy of scale.
- Don't stack more than 5 tiers.
- Don't put long labels inside trapezoids — they get clipped. Side-label always.
