# Funnel Snippet

Narrowing progression. Each stage smaller than the one above. Conversion funnels, adoption funnels, eligibility filters.

## When to use

- User conversion (visitors → signups → actives → payers)
- Token holder segmentation (total → stakers → voters)
- Application → interview → offer → hire
- Airdrop eligibility funnel
- Any "X% survives each stage" visualization

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| bento-box | card-tall | Vertical funnel as a tall sidebar |
| bento-box | card-wide | Horizontal funnel option (rotate the trapezoid) |
| editorial | body-column | Inline funnel figure |
| poster | centerpiece | Funnel as the hero diagram |

## Required elements

`text.md`, `layout.md`, `decorative.md`, `data-widgets.md`, `icons.md`. Optional `connectors.md` for drop-off arrows.

## HTML pattern

```html
<div class="funnel">
  <div class="funnel-stage" style="--width: 100;">
    <div class="funnel-bar"></div>
    <div class="funnel-meta">
      <div class="funnel-label">Awareness</div>
      <div class="funnel-value">100,000</div>
      <div class="funnel-pct">100%</div>
    </div>
  </div>
  <div class="funnel-stage" style="--width: 60;">
    <div class="funnel-bar"></div>
    <div class="funnel-meta">
      <div class="funnel-label">Signups</div>
      <div class="funnel-value">60,000</div>
      <div class="funnel-pct">60%</div>
    </div>
  </div>
  <!-- repeat -->
</div>

<style>
.funnel { display: flex; flex-direction: column; gap: 4px; align-items: stretch; }
.funnel-stage {
  display: grid;
  grid-template-columns: 1fr 220px;
  gap: 16px; align-items: center;
}
.funnel-bar {
  height: 48px;
  width: calc(var(--width) * 1%);
  margin: 0 auto;
  background: linear-gradient(90deg, var(--accent-1), var(--accent-2));
  clip-path: polygon(4% 0, 96% 0, 100% 100%, 0 100%);
  border-radius: 4px;
  box-shadow: 0 0 20px color-mix(in srgb, var(--accent-1) 12%, transparent);
}
.funnel-meta {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 12px; align-items: baseline;
}
.funnel-label {
  font: 700 13px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.05em;
  color: var(--text-primary);
}
.funnel-value {
  font: 400 20px/1 'Bebas Neue', sans-serif;
  color: var(--text-primary);
  font-variant-numeric: tabular-nums;
}
.funnel-pct {
  font: 400 20px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
  min-width: 50px; text-align: right;
}
</style>
```

## Drop-off callout (optional)

```html
<div class="funnel-drop">
  <i class="ph-bold ph-arrow-down"></i>
  <span>-40% · 40,000 users didn't complete signup</span>
</div>

<style>
.funnel-drop {
  display: flex; align-items: center; gap: 8px;
  padding: 4px 16px;
  font: 400 11px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
}
.funnel-drop i { color: var(--negative); }
</style>
```

## Composition rules

- Stages must strictly narrow. If a later stage is larger, the metaphor breaks — use `list` instead.
- Both absolute and percentage on each stage. Percentages alone feel abstract; absolutes alone feel uncalibrated.
- Reference base = stage 1 = 100%. Derived percentages of stage 1, not previous stage.
- Funnel width is proportional to value (60% stage = 60% width of top).
- Max 6 stages. Beyond that, bottom trapezoids unreadable.

## Anti-patterns

- Funnel for non-monotonic data (implies subset relationship).
- Decorative trapezoids — no icons or text inside the bars.
- Funnel for non-causally-linked stages (e.g., "users in region A / B / C") — use chart instead.
