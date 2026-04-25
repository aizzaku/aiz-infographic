# Viewer Features

Optional interactive features for generated HTML. These remain in the final export (unlike creator tools, which are deferred to phase 3). Each feature is drop-in: add the HTML/CSS/JS once, works everywhere in the canvas.

The export script (`scripts/export.py`) already handles all of these for PNG output — counters freeze at final value, reveals force visible, expandables open. You do NOT need separate handling code per feature.

## 1. Hover tooltips on data elements

Show exact value on hover — for chart segments, timeline nodes, KPI cards. Pure CSS, zero JS.

### Chart segment tooltip

```html
<g class="chart-segment" data-tip="Community · 40% · 400M tokens">
  <circle cx="100" cy="100" r="80" … />
  <title>Community · 40% · 400M tokens</title>
</g>
```

SVG `<title>` is the simplest path — browsers render it as a native tooltip on hover. No CSS needed.

### Richer HTML tooltip (for KPI cards, timeline nodes)

```html
<div class="kpi-card" data-tip>
  …
  <span class="tooltip">Detailed context — source, method, exact value.</span>
</div>

<style>
[data-tip] { position: relative; }
[data-tip] .tooltip {
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(-4px);
  padding: 6px 10px;
  background: var(--elevated);
  border: 1px solid color-mix(in srgb, var(--accent-1) 40%, transparent);
  border-radius: 4px;
  color: var(--text-primary);
  font: 400 11px/1.3 'Montserrat', sans-serif;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.15s, transform 0.15s;
  z-index: 100;
}
[data-tip]:hover .tooltip {
  opacity: 1;
  transform: translateX(-50%) translateY(-8px);
}
</style>
```

### PNG export behavior

Tooltips are hover-triggered, so they're never visible at export time. No special handling.

## 2. Animated number counters

Numbers count up from 0 to the target value when scrolled into view. Makes KPI strips feel premium.

### HTML

```html
<div class="big-number-value" data-counter-to="1000000000">1,000,000,000</div>
```

The text content is the final value (what users without JS will see). The `data-counter-to` attribute drives the animation.

### JS (include once in the HTML)

```html
<script>
(function() {
  const fmt = new Intl.NumberFormat('en-US');
  const animate = (el) => {
    const to = Number(el.dataset.counterTo);
    if (Number.isNaN(to)) return;
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

### Decimal / currency values

For `$12.4M` style values, use a different counter (skip this library for those) or include unit suffixing in the formatter. Default implementation is integer-only.

### PNG export behavior

`export.py` forces all `[data-counter-to]` elements to their final value before screenshot. No mid-animation capture.

## 3. Scroll-triggered section reveals

Sections fade/slide in as they enter viewport. Effective for tall portrait canvases.

### CSS

```css
.section {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.section.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### JS

```html
<script>
(function() {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.15 });
  document.querySelectorAll('.section').forEach(s => io.observe(s));
})();
</script>
```

### When NOT to use

- Short canvases (square, landscape) — there's no scroll to trigger the reveal.
- Time-sensitive content (live dashboards) — reveals feel gimmicky.

### PNG export behavior

`export.py` forces `.visible` on every `.section` before screenshot. All sections fully rendered.

## 4. Expandable detail sections

For dense infographics (cheatsheets, comprehensive overviews), let sections collapse to save initial scroll length.

### HTML

```html
<section class="section expandable" data-expanded="true">
  <div class="section-header" onclick="this.closest('.expandable').dataset.expanded =
    this.closest('.expandable').dataset.expanded === 'true' ? 'false' : 'true'">
    <h2 class="section-title">Allocation detail</h2>
    <span class="expand-indicator">
      <i class="ph-bold ph-caret-down"></i>
    </span>
  </div>
  <div class="section-body">
    <!-- content -->
  </div>
</section>

<style>
.expandable .section-header {
  cursor: pointer;
  user-select: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.expandable .expand-indicator i {
  color: var(--accent-1);
  transition: transform 0.2s ease;
}
.expandable[data-expanded="false"] .expand-indicator i {
  transform: rotate(-90deg);
}
.expandable .section-body {
  max-height: 2000px;
  overflow: hidden;
  transition: max-height 0.3s ease, opacity 0.2s ease;
  opacity: 1;
}
.expandable[data-expanded="false"] .section-body {
  max-height: 0;
  opacity: 0;
}
</style>
```

### When to use

- Cheatsheets with multiple domains
- Very long reports where the user may want to skim the headlines first
- Any case where the "top-of-fold" summary is valuable without expanding details

### PNG export behavior

`export.py` forces all expandables to `data-expanded="true"` before screenshot. Full content captured.

## 5. Dark / light mode toggle

Some viewers need to embed in a light-context page. Offer a toggle.

### CSS

```css
:root {
  /* dark mode defaults */
  --canvas: #0F1115;
  /* ... */
}
:root[data-theme="light"] {
  --canvas: #F5F5F5;
  --panel: #EBEBEB;
  --elevated: #E0E0E0;
  --text-primary: #1A1A1A;
  --text-secondary: #4A4A4A;
  --text-muted: #808080;
  --on-accent: #F5F5F5;
  /* accents might darken — per style spec */
}
```

### HTML toggle

```html
<button class="theme-toggle" onclick="
  const r = document.documentElement;
  r.dataset.theme = r.dataset.theme === 'light' ? 'dark' : 'light';
">
  <i class="ph-bold ph-sun"></i>
  <i class="ph-bold ph-moon"></i>
</button>

<style>
.theme-toggle {
  position: fixed;
  top: 16px; right: 16px;
  padding: 8px;
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--accent-1) 30%, transparent);
  border-radius: 50%;
  color: var(--accent-1);
  cursor: pointer;
  z-index: 100;
}
.theme-toggle .ph-moon { display: none; }
:root[data-theme="light"] .theme-toggle .ph-sun { display: none; }
:root[data-theme="light"] .theme-toggle .ph-moon { display: inline-block; }
</style>
```

### When to use

- Content published to both dark and light contexts
- Accessibility-conscious output (user preference)

### When NOT to use

- Style is explicitly theme-locked (cyberpunk, chalkboard, retro don't have credible light-mode counterparts — don't offer the toggle)
- Content is presentation-only (generated PNG always uses dark)

### PNG export behavior

Default state (`data-theme` unset) is captured. PNGs always dark unless the HTML explicitly sets `data-theme="light"` at load time.

## Feature enablement policy

Generated HTML should include features based on content type:

| Template | Counters | Reveals | Tooltips | Expandables | Toggle |
|----------|----------|---------|----------|-------------|--------|
| token-economics | ✓ KPIs | ✓ | ✓ chart | — | — |
| ecosystem-overview | ✓ stats | ✓ | — | optional by category | — |
| cheatsheet | — | ✓ | — | ✓ sections | — |
| report | ✓ KPIs | ✓ | ✓ charts | — | ✓ optional |
| airdrop-guide | — | ✓ | — | — | — |
| game-overview | ✓ stats | ✓ | — | — | — |
| All others | ✓ | ✓ | — | — | — |

Reveals are always safe to include. Counters on every KPI. Tooltips only for charts (overhead per element). Expandables only for dense content. Toggle only when specifically asked for.

## File size / performance

All five features combined add ~1.5 KB of JS and ~2 KB of CSS to the HTML. Zero external deps. No frameworks.
