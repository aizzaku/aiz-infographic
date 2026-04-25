# Data Widgets — KPIs, Counters, Progress

Compact numeric displays.

## Big number

```html
<div class="big-number">
  <div class="big-number-value" data-counter-to="1000000000">1,000,000,000</div>
  <div class="big-number-label">Total supply</div>
</div>

<style>
.big-number { display: flex; flex-direction: column; gap: 4px; }
.big-number-value {
  font: 400 52px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.04em;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
}
.big-number-label {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
}
</style>
```

## KPI card (boxed)

```html
<div class="kpi-card">
  <div class="kpi-icon"><i class="ph-bold ph-coins"></i></div>
  <div class="kpi-value">1B</div>
  <div class="kpi-label">Total supply</div>
</div>

<style>
.kpi-card {
  padding: 20px;
  background: var(--panel);
  border-radius: var(--radius-card);
  border: 1px solid transparent;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 20%, transparent),
      color-mix(in srgb, var(--accent-1) 40%, transparent)) border-box;
  display: flex; flex-direction: column; gap: 6px;
}
.kpi-icon {
  color: var(--accent-1);
  font-size: 24px;
}
.kpi-value {
  font: 400 36px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.04em;
  color: var(--text-primary);
  font-variant-numeric: tabular-nums;
}
.kpi-label {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-muted);
}
</style>
```

## KPI strip (3–6 cards in a row)

Use `.kpi-strip` from `layout.md` as the wrapper.

## Progress bar (labeled)

```html
<div class="pbar">
  <div class="pbar-header">
    <span class="pbar-label">Vesting unlocked</span>
    <span class="pbar-pct">42%</span>
  </div>
  <div class="pbar-track">
    <div class="pbar-fill" style="--pct: 42;"></div>
  </div>
  <div class="pbar-meta">
    <span>Month 10 of 24</span>
    <span>420M / 1B</span>
  </div>
</div>

<style>
.pbar { display: flex; flex-direction: column; gap: 6px; }
.pbar-header { display: flex; justify-content: space-between; align-items: baseline; }
.pbar-label {
  font: 700 13px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.05em;
}
.pbar-pct {
  font: 400 20px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
}
.pbar-track {
  height: 10px;
  background: color-mix(in srgb, var(--text-primary) 6%, transparent);
  border-radius: 5px;
  overflow: hidden;
}
.pbar-fill {
  width: calc(var(--pct) * 1%);
  height: 100%;
  background: linear-gradient(90deg, var(--accent-1), var(--accent-2));
}
.pbar-meta {
  display: flex; justify-content: space-between;
  font: 400 11px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
}
</style>
```

## Trend arrow (up / down)

```html
<span class="trend trend-up">
  <i class="ph-bold ph-trend-up"></i> +12.4%
</span>

<style>
.trend {
  display: inline-flex; align-items: center; gap: 4px;
  font: 700 14px/1 'Montserrat', sans-serif;
  font-variant-numeric: tabular-nums;
}
.trend-up { color: var(--positive); }
.trend-down { color: var(--negative); }
</style>
```

## Number counter (animated on scroll)

Include once in the HTML (viewer feature, stripped for PNG):

```html
<script>
(function() {
  const fmt = new Intl.NumberFormat('en-US');
  const animate = (el) => {
    const to = Number(el.dataset.counterTo);
    const dur = 1200;
    const t0 = performance.now();
    const step = (t) => {
      const p = Math.min(1, (t - t0) / dur);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt.format(Math.round(to * eased));
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting && !e.target.dataset.counted) {
        e.target.dataset.counted = '1';
        animate(e.target);
      }
    });
  }, { threshold: 0.3 });
  document.querySelectorAll('[data-counter-to]').forEach(el => io.observe(el));
})();
</script>
```

For PNG export, set `data-counter-to` attributes to final values in the DOM — the exporter forces them to final state before screenshotting.

## Role classes (semantic node tokens)

Reusable classes matching the role table in `references/styles/aizfographics-style.md`. Apply as a second class on any card / node / panel to signal its role. Values are expressed in `color-mix` so they follow the active accent pair.

```css
.role-focal {
  background:
    linear-gradient(
      color-mix(in srgb, var(--accent-1) 10%, var(--panel)),
      color-mix(in srgb, var(--accent-1) 10%, var(--panel))
    ) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 30%, transparent),
      color-mix(in srgb, var(--accent-1) 50%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
}
.role-primary {
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 20%, transparent),
      color-mix(in srgb, var(--accent-1) 40%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
}
.role-secondary {
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--text-muted) 40%, transparent);
  border-radius: var(--radius-card);
}
.role-external {
  background: transparent;
  border: 1px dashed color-mix(in srgb, var(--text-muted) 50%, transparent);
  border-radius: var(--radius-card);
}
.role-optional {
  background: color-mix(in srgb, var(--panel) 60%, transparent);
  border: 1px dashed color-mix(in srgb, var(--accent-1) 30%, transparent);
  border-radius: var(--radius-card);
}
.role-positive {
  background: color-mix(in srgb, var(--positive) 8%, var(--panel));
  border: 1px solid color-mix(in srgb, var(--positive) 40%, transparent);
  border-radius: var(--radius-card);
}
.role-negative {
  background: color-mix(in srgb, var(--negative) 8%, var(--panel));
  border: 1px solid color-mix(in srgb, var(--negative) 40%, transparent);
  border-radius: var(--radius-card);
}
```

Usage rules in the style guide (`aizfographics-style.md` → "Node / card roles") — respect caps (`focal` ≤ 1 per section, ≤ 2 per infographic).

## Rules

- Numbers right-aligned in columns, tabular-nums always.
- Big numbers use display font (Bebas Neue in default). Not body font.
- Labels above OR below values consistently per section — pick one, stick with it.
- Include units only when needed (%, $, tokens). Never a bare number without context.
