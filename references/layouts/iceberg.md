# Iceberg Layout

"What you see is not all there is" metaphor. Small visible portion above a waterline, large hidden portion below. Classic for revealing complexity, cost, or effort hidden beneath surface appearances.

## When to use

- Visible vs underlying work (the UI you see vs the systems running it)
- Surface costs vs total costs
- Public features vs behind-the-scenes infrastructure
- What users see vs what a protocol actually does
- Perception vs reality

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│           ▲                   │
│          ╱ ╲   ABOVE (visible)│
│         ╱   ╲                 │
│ ~~~~~~~~~~~~~~~~~~~ waterline │
│        ╱     ╲                │
│       ╱       ╲ BELOW (hidden)│
│      ╱         ╲              │
│     ╱___________╲             │
├──────────────────────────────┤
│ Key / legend                 │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## HTML pattern

```html
<div class="iceberg">
  <div class="iceberg-above">
    <h3 class="iceberg-label">What you see</h3>
    <ul class="iceberg-list">
      <li>Landing page</li>
      <li>Wallet connect button</li>
      <li>Trade interface</li>
    </ul>
  </div>

  <div class="iceberg-waterline">
    <span>Surface</span>
  </div>

  <div class="iceberg-below">
    <h3 class="iceberg-label">What runs underneath</h3>
    <ul class="iceberg-list">
      <li>Order routing engine</li>
      <li>AMM contract optimization</li>
      <li>Gas estimation service</li>
      <li>MEV protection</li>
      <li>Liquidity aggregation</li>
      <li>Fallback RPC layer</li>
      <li>State indexing</li>
      <li>Event parsing pipeline</li>
    </ul>
  </div>
</div>

<style>
.iceberg {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  padding: 20px 0;
}

.iceberg-above {
  width: 40%;
  padding: 16px;
  background:
    linear-gradient(180deg,
      color-mix(in srgb, var(--accent-1) 30%, var(--panel)),
      color-mix(in srgb, var(--accent-1) 10%, var(--panel)));
  clip-path: polygon(50% 0, 100% 100%, 0 100%);
  text-align: center;
  color: var(--text-primary);
  padding-bottom: 32px;
  min-height: 140px;
}

.iceberg-waterline {
  width: 100%;
  height: 20px;
  position: relative;
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--accent-2) 25%, transparent),
    color-mix(in srgb, #3366AA 40%, transparent));
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 12px;
  margin: -8px 0;
}
.iceberg-waterline span {
  font: 700 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
}

.iceberg-below {
  width: 85%;
  padding: 20px;
  background:
    linear-gradient(180deg,
      color-mix(in srgb, #0A1628 70%, var(--canvas)),
      color-mix(in srgb, #0A1628 95%, var(--canvas)));
  clip-path: polygon(12% 0, 88% 0, 100% 100%, 0 100%);
  text-align: center;
  color: var(--text-primary);
  padding-top: 24px;
  min-height: 240px;
}

.iceberg-label {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent-1);
  margin: 0 0 10px;
}

.iceberg-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
  font: 400 13px/1.4 'Montserrat', sans-serif;
  color: var(--text-secondary);
}
</style>
```

## Ratio guidance

Typical iceberg ratio is ~10% visible / 90% hidden. Reflect this in the layout:
- Above: 3–5 items
- Below: 8–15 items

If the ratio is inverted (more visible than hidden), this layout is wrong for the content.

## Composition rules

- **Cool palette below, warm or accent above.** Contrast emphasizes the split.
- **Waterline is a distinct element.** Thin gradient band with the word "Surface" or "Waterline".
- **Below section wider than above.** The whole point is scale — width reinforces it.
- **List items, not cards.** Cards fragment the "mass" feeling. Simple text lists read as accumulation.
- **Central vertical axis.** Everything aligned on center.

## Dimension guidance

Portrait-tall (1080 × 1920) works best — vertical metaphor. Landscape misses the point.

## Anti-patterns

- Don't use for equal-weight comparisons. Iceberg specifically means "hidden is larger".
- Don't put more above than below. That inverts the metaphor.
- Don't decorate the waterline with literal ocean imagery — keep it abstract.
