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

## Hexagonal percentage badge

Self-contained metric tile shaped as a hexagon. Use when a single number needs to feel like a stamp or seal rather than a card.

**Render the hexagon as inline SVG**, not via CSS `clip-path` + `border`. CSS clip-path crops the border on diagonal edges, producing visible slivers / broken outlines. The SVG `<polygon>` renders fill and stroke cleanly.

```html
<div class="hex-badge">
  <svg viewBox="0 0 100 110">
    <!-- Vertices inset by 5 so the 2px stroke sits inside the viewBox -->
    <polygon points="50,5 95,30 95,80 50,105 5,80 5,30"
             fill="color-mix(in srgb, var(--accent-1) 12%, var(--panel))"
             stroke="var(--accent-1)" stroke-width="2"/>
  </svg>
  <span class="hex-badge__value">75%</span>
</div>

<!-- Hollow variant (empty-state, 0%) -->
<div class="hex-badge hex-badge--hollow">
  <svg viewBox="0 0 100 110">
    <polygon points="50,5 95,30 95,80 50,105 5,80 5,30"
             fill="transparent"
             stroke="color-mix(in srgb, var(--accent-1) 45%, transparent)"
             stroke-width="2"/>
  </svg>
  <span class="hex-badge__value">0%</span>
</div>

<style>
.hex-badge {
  position: relative;
  width: 120px; height: 132px;
  display: flex; align-items: center; justify-content: center;
  filter: drop-shadow(0 0 12px color-mix(in srgb, var(--accent-1) 30%, transparent));
}
.hex-badge svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.hex-badge__value {
  position: relative;
  font: 400 36px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  letter-spacing: 0.04em;
  font-variant-numeric: tabular-nums;
}
.hex-badge--hollow { filter: none; }
.hex-badge--hollow .hex-badge__value { color: var(--text-secondary); }
</style>
```

**Use in a row:** `0% (hollow) → 25% → 75% → 100% (filled)` for milestone progress (see Image 2 reference).

**Rules:**
- One value per hex. Don't stack label + value inside.
- 100-160px wide. Smaller is unreadable; larger fights cards for visual weight.
- Glow only on filled variants. Hollow = no glow.

---

## Progress ring variants

The default progress ring lives above. These are four stylistic variants for when one feels too plain.

### V1: Segmented ring

```html
<svg viewBox="0 0 100 100" width="90" height="90">
  <g stroke="var(--accent-1)" stroke-width="10" fill="none">
    <!-- 8 segments, gap=4deg, each arc ~ 41deg of circumference -->
    <circle cx="50" cy="50" r="42" pathLength="100"
            stroke-dasharray="11 1.5" transform="rotate(-90 50 50)"/>
  </g>
</svg>
```

### V2: Dashed-gap ring

```html
<svg viewBox="0 0 100 100" width="90" height="90">
  <circle cx="50" cy="50" r="42" pathLength="100"
          fill="none" stroke="var(--accent-1)" stroke-width="10"
          stroke-dasharray="3 2" transform="rotate(-90 50 50)"/>
</svg>
```

### V3: Petal ring

```html
<svg viewBox="0 0 100 100" width="90" height="90">
  <circle cx="50" cy="50" r="38" pathLength="100"
          fill="none" stroke="var(--accent-1)" stroke-width="14"
          stroke-dasharray="9 3.5" stroke-linecap="round"
          transform="rotate(-90 50 50)"/>
</svg>
```

### V4: Concentric target

```html
<svg viewBox="0 0 100 100" width="90" height="90">
  <circle cx="50" cy="50" r="42" fill="none" stroke="var(--accent-1)" stroke-width="2"/>
  <circle cx="50" cy="50" r="32" fill="none" stroke="var(--accent-1)" stroke-width="2"/>
  <circle cx="50" cy="50" r="22" fill="none" stroke="var(--accent-1)" stroke-width="2"/>
  <circle cx="50" cy="50" r="12" fill="var(--accent-1)"/>
</svg>
```

**When to pick which:**
- **Segmented** — discrete completion steps (8 of N done).
- **Dashed** — incremental / continuous progress.
- **Petal** — decorative / brand-feel KPIs.
- **Concentric** — "bullseye" goal tracking.

Pick one variant per infographic. Don't mix.

---

## Slider / equalizer KPI

Vertical tracks with a circular numbered token at a height encoding the value. Equalizer-style.

```html
<div class="slider-kpi-row">
  <div class="slider-kpi" style="--val: 30%;">
    <div class="slider-kpi__track"></div>
    <div class="slider-kpi__fill"></div>
    <div class="slider-kpi__handle">01</div>
  </div>
  <div class="slider-kpi" style="--val: 60%;">
    <div class="slider-kpi__track"></div>
    <div class="slider-kpi__fill"></div>
    <div class="slider-kpi__handle">02</div>
  </div>
  <div class="slider-kpi" style="--val: 45%;">
    <div class="slider-kpi__track"></div>
    <div class="slider-kpi__fill"></div>
    <div class="slider-kpi__handle">03</div>
  </div>
  <div class="slider-kpi" style="--val: 80%;">
    <div class="slider-kpi__track"></div>
    <div class="slider-kpi__fill"></div>
    <div class="slider-kpi__handle">04</div>
  </div>
</div>

<style>
.slider-kpi-row { display: flex; gap: 24px; height: 220px; align-items: flex-end; }
.slider-kpi {
  position: relative;
  width: 8px;
  height: 100%;
}
.slider-kpi__track {
  position: absolute; inset: 0;
  background: var(--elevated);
  border-radius: 4px;
}
.slider-kpi__fill {
  position: absolute; left: 0; right: 0; bottom: 0;
  height: var(--val);
  background: var(--accent-1);
  border-radius: 4px;
}
.slider-kpi__handle {
  position: absolute;
  left: 50%;
  bottom: var(--val);
  transform: translate(-50%, 50%);
  width: 32px; height: 32px;
  border-radius: 50%;
  background: var(--accent-1);
  color: var(--on-accent);
  display: flex; align-items: center; justify-content: center;
  font: 700 12px/1 'Montserrat', sans-serif;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.05em;
  box-shadow: 0 0 10px color-mix(in srgb, var(--accent-1) 40%, transparent);
}
</style>
```

**Rules:**
- 3-6 sliders per row. More than 6 visual noise.
- Handle is always filled accent with token number. Use `01-09` zero-padded.
- Height: 180-240px. Below 180 the spread becomes illegible.

---

## Donut-row KPI list

Vertical list pattern: small donut left, value inside, label + body stacked right. Repeats vertically as a sidebar.

```html
<div class="kpi-list">
  <div class="kpi-list__row">
    <svg class="kpi-list__donut" viewBox="0 0 100 100" width="64" height="64">
      <circle cx="50" cy="50" r="42" fill="none"
              stroke="var(--elevated)" stroke-width="10"/>
      <circle cx="50" cy="50" r="42" fill="none"
              stroke="var(--accent-1)" stroke-width="10"
              stroke-dasharray="158.34 263.89" stroke-linecap="round"
              transform="rotate(-90 50 50)"/>
      <text x="50" y="56" text-anchor="middle"
            font-family="Bebas Neue" font-size="22" fill="var(--text-primary)">60%</text>
    </svg>
    <div class="kpi-list__copy">
      <div class="item-label">Adoption</div>
      <p class="caption">60% of seed users active monthly.</p>
    </div>
  </div>
  <!-- … repeat … -->
</div>

<style>
.kpi-list { display: flex; flex-direction: column; gap: 16px; }
.kpi-list__row { display: flex; gap: 16px; align-items: center; }
.kpi-list__donut { flex-shrink: 0; }
.kpi-list__copy { display: flex; flex-direction: column; gap: 4px; }
</style>
```

**Rules:**
- 3-6 rows. Use this when 4+ percentage-style KPIs share a sidebar.
- Donut size: 56-72px. Fixed across the list — never vary row to row.
- Body copy: ≤ 12 words per row (§6.5 caps).

## Rules

- Numbers right-aligned in columns, tabular-nums always.
- Big numbers use display font (Bebas Neue in default). Not body font.
- Labels above OR below values consistently per section — pick one, stick with it.
- Include units only when needed (%, $, tokens). Never a bare number without context.
