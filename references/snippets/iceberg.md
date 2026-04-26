# Iceberg Snippet

"What you see is not all there is." Small visible portion above a waterline, large hidden portion below. Reveals complexity, cost, or effort beneath surface appearances.

## When to use

- Visible vs underlying work (UI vs systems running it)
- Surface costs vs total costs
- Public features vs behind-the-scenes infrastructure
- Perception vs reality

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| poster | centerpiece | Best — vertical metaphor needs full height |
| editorial | body-column | Inline tall figure |
| bento-box | card-tall | Compact iceberg in a sidebar slot |

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`.

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

  <div class="iceberg-waterline"><span>Surface</span></div>

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
.iceberg { display: flex; flex-direction: column; align-items: center; gap: 0; padding: 20px 0; }

.iceberg-above {
  width: 40%;
  padding: 16px 16px 32px;
  background:
    linear-gradient(180deg,
      color-mix(in srgb, var(--accent-1) 30%, var(--panel)),
      color-mix(in srgb, var(--accent-1) 10%, var(--panel)));
  clip-path: polygon(50% 0, 100% 100%, 0 100%);
  text-align: center;
  color: var(--text-primary);
  min-height: 140px;
}

.iceberg-waterline {
  width: 100%; height: 20px;
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--accent-2) 25%, transparent),
    color-mix(in srgb, #3366AA 40%, transparent));
  display: flex; align-items: center; justify-content: flex-end;
  padding-right: 12px;
  margin: -8px 0;
}
.iceberg-waterline span {
  font: 700 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.1em;
  color: var(--text-muted);
}

.iceberg-below {
  width: 85%;
  padding: 24px 20px 20px;
  background:
    linear-gradient(180deg,
      color-mix(in srgb, #0A1628 70%, var(--canvas)),
      color-mix(in srgb, #0A1628 95%, var(--canvas)));
  clip-path: polygon(12% 0, 88% 0, 100% 100%, 0 100%);
  text-align: center;
  color: var(--text-primary);
  min-height: 240px;
}

.iceberg-label {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--accent-1);
  margin: 0 0 10px;
}
.iceberg-list {
  list-style: none; padding: 0; margin: 0;
  display: flex; flex-direction: column; gap: 4px;
  font: 400 13px/1.4 'Montserrat', sans-serif;
  color: var(--text-secondary);
}
</style>
```

## Ratio guidance

Typical: ~10% visible, ~90% hidden.
- Above: 3-5 items
- Below: 8-15 items

If inverted (more above), this snippet is wrong for the content.

## Composition rules

- Cool palette below, warm/accent above — contrast emphasizes the split.
- Waterline is a distinct band with the word "Surface" or "Waterline".
- Below section wider than above — width reinforces scale.
- List items, not cards. Cards fragment the "mass" feeling.
- Central vertical axis.

## Anti-patterns

- Equal-weight comparisons (iceberg specifically means hidden > visible).
- More above than below (inverts metaphor).
- Literal ocean imagery on the waterline — keep abstract.
