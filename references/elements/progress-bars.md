# Progress Bars

Flat fill bars for data-dense and industrial themes. No Chart.js dependency — pure HTML/CSS.

## Variant 1: flat-bar (forge / terminal default)

Zero border-radius. Hard rectangle fill. No gradients on the fill track.

```html
<div class="pbar-flat">
  <div class="pbar-flat-header">
    <span class="pbar-flat-label">YIELD</span>
    <span class="pbar-flat-pct">68%</span>
  </div>
  <div class="pbar-flat-track">
    <div class="pbar-flat-fill" style="--pct: 68;"></div>
  </div>
</div>

<style>
.pbar-flat { display: flex; flex-direction: column; gap: 4px; }
.pbar-flat-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}
.pbar-flat-label {
  font: 700 10px/1 monospace;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-secondary);
}
.pbar-flat-pct {
  font: 700 12px/1 monospace;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
}
.pbar-flat-track {
  height: 8px;                                 /* compact: 8px | standard: 12px | hero: 20px */
  background: color-mix(in srgb, var(--text-primary) 8%, transparent);
  border-radius: 0;                            /* hard edge — no radius */
  overflow: hidden;
}
.pbar-flat-fill {
  width: calc(var(--pct) * 1%);
  height: 100%;
  background: var(--accent-1);                 /* flat color, no gradient */
  border-radius: 0;
}
</style>
```

## Variant 2: rounded-bar (default / glasspaper)

4px radius. Accent gradient fill. Used when the theme allows soft edges.

```html
<div class="pbar-rounded">
  <div class="pbar-header">
    <span class="pbar-label">Vesting unlocked</span>
    <span class="pbar-pct">42%</span>
  </div>
  <div class="pbar-track-r">
    <div class="pbar-fill-r" style="--pct: 42;"></div>
  </div>
  <div class="pbar-meta">
    <span>Month 10 of 24</span>
    <span>420M / 1B</span>
  </div>
</div>

<style>
.pbar-rounded { display: flex; flex-direction: column; gap: 6px; }
.pbar-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}
.pbar-label {
  font: 700 12px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-secondary);
}
.pbar-pct {
  font: 400 20px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
}
.pbar-track-r {
  height: 10px;
  background: color-mix(in srgb, var(--text-primary) 6%, transparent);
  border-radius: 5px;
  overflow: hidden;
}
.pbar-fill-r {
  width: calc(var(--pct) * 1%);
  height: 100%;
  background: linear-gradient(90deg, var(--accent-1), var(--accent-2));
  border-radius: 5px;
}
.pbar-meta {
  display: flex;
  justify-content: space-between;
  font: 400 11px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
}
</style>
```

## Variant 3: segmented-bar

Divided into N equal cells. Filled cells determined by value. Used for discrete progress (steps, stages, token unlock schedule).

```html
<div class="pbar-seg" style="--segs: 10; --filled: 7;">
  <!-- JS fills the cells, but HTML-only fallback uses CSS counters -->
</div>

<script>
(function() {
  document.querySelectorAll('.pbar-seg').forEach(function(el) {
    var segs = parseInt(el.style.getPropertyValue('--segs')) || 10;
    var filled = parseInt(el.style.getPropertyValue('--filled')) || 0;
    el.innerHTML = Array.from({length: segs}, function(_, i) {
      return '<div class="pbar-seg-cell' + (i < filled ? ' filled' : '') + '"></div>';
    }).join('');
    el.setAttribute('data-canvas-ready', 'true');
  });
})();
</script>

<style>
.pbar-seg {
  display: flex;
  gap: 2px;
  height: 12px;
}
.pbar-seg-cell {
  flex: 1;
  border-radius: 0;
  background: color-mix(in srgb, var(--text-primary) 8%, transparent);
}
.pbar-seg-cell.filled {
  background: var(--accent-1);
}
</style>
```

## Variant 4: ascii-bar (terminal theme only)

Pure text. No DOM elements for the fill. Renders correctly in monospace contexts.

```html
<div class="pbar-ascii">
  <span class="pbar-ascii-label">YIELD</span>
  <span class="pbar-ascii-bar" data-pct="68"><!-- filled by JS --></span>
  <span class="pbar-ascii-pct">68%</span>
</div>

<script>
(function() {
  document.querySelectorAll('.pbar-ascii-bar[data-pct]').forEach(function(el) {
    var pct = parseInt(el.dataset.pct) || 0;
    var total = 20;
    var filled = Math.round(pct / 100 * total);
    el.textContent = '[' + '█'.repeat(filled) + '░'.repeat(total - filled) + ']';
    el.closest('.pbar-ascii').setAttribute('data-canvas-ready', 'true');
  });
})();
</script>

<style>
.pbar-ascii {
  display: flex;
  align-items: center;
  gap: 8px;
  font: 400 12px/1 monospace;
  color: var(--text-primary);
}
.pbar-ascii-label {
  color: var(--text-secondary);
  letter-spacing: 0.06em;
  min-width: 60px;
}
.pbar-ascii-bar {
  color: var(--accent-1);
  letter-spacing: -0.02em;
}
.pbar-ascii-pct {
  color: var(--text-muted);
  min-width: 36px;
  text-align: right;
}
</style>
```

## Sizing reference

| Size | Height | Use |
|---|---|---|
| Compact | 8px | Dense data grids, forge batch rows |
| Standard | 12px | Default stat rows |
| Hero | 20px | Single prominent metric |

When bar height is 20px or taller, the percentage label may be overlaid inside the fill:

```css
.pbar-flat-track.hero {
  height: 20px;
  position: relative;
}
.pbar-flat-track.hero .pbar-inline-label {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  font: 700 11px/1 monospace;
  color: var(--on-accent, #0F1115);
}
```

## Rules

- No gradient fills in terminal or forge themes — solid `var(--accent-1)` only.
- No rounded bar ends in terminal or forge themes — `border-radius: 0` everywhere.
- Always set `data-canvas-ready="true"` after JS rendering (Playwright export requirement).
- Width is always `100%` of the container — never fixed pixel widths.
- Segmented and ascii variants require the inline JS block; include it once per page.
