# Stat Spotlight Snippet

Single hero metric with sparkline and delta indicator. Used when one number deserves full visual weight with trend context. The single-metric counterpart to the multi-KPI `statistical` snippet.

## When to use

- One metric dominates the section's message (DAU, TVL, revenue, supply)
- The trend matters as much as the value (sparkline required)
- A delta vs a reference period adds meaning (+34% WoW)

Do NOT use for 3+ metrics side-by-side — use `statistical` instead.

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| bento-box | hero | Full-bleed hero spotlight |
| bento-box | card-span-2 | Wide card, center-aligned |
| bento-box | card-1 | Single cell — value only, compact sparkline |
| dashboard | kpi-hero | Top-left feature metric |
| poster | header-strip | Dominant metric above the centerpiece |

## Required elements

`data-widgets.md`, `sparklines.md`, `text.md`. Optional `callout-card.md` (folded-corner emphasis frame for the spotlighted metric).

## HTML pattern

```html
<div class="stat-spotlight">
  <div class="stat-spotlight-label">DAILY ACTIVE USERS</div>
  <div class="stat-spotlight-value">1.2M</div>
  <div class="stat-spotlight-row">
    <!-- sparkline from sparklines.md -->
    <svg class="sparkline sparkline-area"
         data-values="820000,890000,940000,870000,1010000,1080000,1150000,1200000"
         data-color="positive"
         width="140" height="40"
         viewBox="0 0 140 40"
         preserveAspectRatio="none">
    </svg>
    <!-- delta badge -->
    <span class="stat-delta stat-delta-up">
      <i class="ph-bold ph-trend-up" aria-hidden="true"></i>
      +34% vs last month
    </span>
  </div>
  <!-- optional: subtitle context -->
  <div class="stat-spotlight-sub">Peak: 1.4M on May 12</div>
</div>

<style>
.stat-spotlight {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 28px;
  background: var(--panel);
  border-radius: var(--radius-card, 10px);
  border: 1px solid transparent;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 20%, transparent),
      color-mix(in srgb, var(--accent-1) 40%, transparent)) border-box;
}

.stat-spotlight-label {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.10em;
  color: var(--text-muted);
}

.stat-spotlight-value {
  font: 400 64px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.02em;
  color: var(--text-primary);
  font-variant-numeric: tabular-nums;
  line-height: 1;
}

.stat-spotlight-row {
  display: flex;
  align-items: center;
  gap: 16px;
}

.stat-delta {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font: 700 14px/1 'Montserrat', sans-serif;
  font-variant-numeric: tabular-nums;
}
.stat-delta-up   { color: var(--positive, #00D018); }
.stat-delta-down { color: var(--negative, #D0002D); }
.stat-delta-flat { color: var(--text-secondary); }

.stat-spotlight-sub {
  font: 400 12px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
}
</style>
```

## Compact variant (single bento cell)

When placed in a 1-cell bento slot, reduce font sizes and use a compact sparkline:

```html
<div class="stat-spotlight stat-spotlight-compact">
  <div class="stat-spotlight-label">TVL</div>
  <div class="stat-spotlight-value" style="font-size: 48px;">$42M</div>
  <div class="stat-spotlight-row">
    <svg class="sparkline sparkline-line"
         data-values="28,32,36,30,38,40,42"
         data-color="positive"
         width="100" height="32"
         viewBox="0 0 100 32"
         preserveAspectRatio="none">
    </svg>
    <span class="stat-delta stat-delta-up">+18%</span>
  </div>
</div>

<style>
.stat-spotlight-compact { padding: 20px; gap: 8px; }
.stat-spotlight-compact .stat-spotlight-value { font-size: 48px; }
</style>
```

## Monospace / terminal variant

For terminal and forge themes, replace display font and adjust sizes:

```css
.stat-spotlight-value {
  font: 700 52px/1 monospace;
  letter-spacing: -0.02em;
  color: #79C0FF; /* terminal: blue for values */
}
.stat-spotlight-label {
  font-family: monospace;
  color: #8B949E; /* terminal: gray for comments */
}
.stat-spotlight {
  background: #161B22;
  border: 1px solid #30363D;
  border-radius: 0;
}
```

## Sparkline wiring

The `<svg>` elements are rendered by the sparklines.md JS block — include that script on the same page. `data-canvas-ready="true"` is set automatically by the sparkline renderer.

## Delta sign conventions

| Value | Class | Icon |
|---|---|---|
| Positive change | `stat-delta-up` | `ph-trend-up` |
| Negative change | `stat-delta-down` | `ph-trend-down` |
| No change / flat | `stat-delta-flat` | `ph-minus` |

Always show the sign explicitly: `+18%`, `-3.2%`. Never a bare number for a delta.

## Composition rules

- One metric per spotlight. If two metrics need equal hero treatment, use two spotlight cards side by side in a 2-col bento layout, not a single spotlight with two values.
- The sparkline carries the trend story — it must be present if the delta is shown. A delta without a sparkline is just a number with a percent sign.
- Label is above the value. Delta row is below the value. Subtitle (if any) is at the bottom.
- No animated number counter on the value — the sparkline provides motion context; stacking both is visual noise.

## Anti-patterns

- Chart.js for the sparkline — too heavy; use the inline SVG from `sparklines.md`
- More than one metric per spotlight — use `statistical` snippet
- Delta label without explicit sign (+/-) — always include the sign
- Sparkline with axes or labels — it ceases to be a sparkline
