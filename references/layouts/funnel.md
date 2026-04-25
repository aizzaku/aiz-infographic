# Funnel Layout

Narrowing progression. Each stage has fewer items or lower numbers than the stage above. Classic for conversion funnels, adoption funnels, filtering pipelines.

## When to use

- User conversion (visitors → signups → actives → payers)
- Token holder segmentation (total holders → stakers → voters)
- Application → interview → offer → hire
- Airdrop eligibility funnel
- Any "X% survives each stage" visualization

## Required elements

`text.md`, `layout.md`, `decorative.md`, `data-widgets.md`, `icons.md`, optionally `connectors.md` for drop-off arrows.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│  ████████████████████  Stage 1│  100%
│    ████████████████    Stage 2│   60%  (−40% drop)
│      ████████████      Stage 3│   36%
│        ██████████      Stage 4│   12%
├──────────────────────────────┤
│ Per-stage callouts           │  optional
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## HTML pattern — trapezoid funnel

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
  gap: 16px;
  align-items: center;
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
  gap: 12px;
  align-items: baseline;
}
.funnel-label {
  font: 700 13px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
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
  min-width: 50px;
  text-align: right;
}
</style>
```

## Drop-off callouts

Between stages, optionally show the drop with a small row:

```html
<div class="funnel-drop">
  <i class="ph-bold ph-arrow-down"></i>
  <span>−40% · 40,000 users didn't complete signup</span>
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

## Dimension guidance

- 3–5 stages: portrait-medium (1080 × 1440) — ideal.
- 6+ stages: portrait-tall (1080 × 1920) so trapezoid heights stay readable.
- Landscape works but wastes space — only use if funnel sits alongside context content.

## Composition rules

- **Stages must strictly narrow.** If stage 3 is larger than stage 2, the metaphor breaks. Use `list` layout instead.
- **Both absolute and percentage** on each stage. Percentages alone feel abstract; absolutes alone feel uncalibrated.
- **Reference base is stage 1 = 100%.** Derived percentages of stage 1, not of previous stage.
- **Funnel width is proportional to value.** 60% stage is exactly 60% the width of the top stage.
- **Max 6 stages.** Beyond that, the bottom trapezoids are unreadably narrow.

## Anti-patterns

- Don't use a funnel for non-monotonic data. It implies each stage is a subset of the previous.
- Don't decorate the trapezoids — no icons on the bars themselves, no text inside the bars.
- Don't use funnel when stages aren't causally linked. "Users in region A / region B / region C" is not a funnel — it's a breakdown (use chart).
