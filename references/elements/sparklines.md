# Sparklines

Inline SVG sparklines for KPI strips and stat-spotlight. No Chart.js or D3 dependency.

## Variant 1: line-sparkline (default)

`<polyline>` path on SVG canvas. No axes, no labels, no grid.

```html
<svg class="sparkline sparkline-line"
     data-values="12,18,14,22,19,28,24,32,27,36"
     data-color="accent"
     width="100" height="32"
     viewBox="0 0 100 32"
     preserveAspectRatio="none">
  <!-- filled by JS -->
</svg>

<script>
(function() {
  function renderSparklines() {
    document.querySelectorAll('.sparkline[data-values]').forEach(function(svg) {
      var raw = svg.dataset.values.split(',').map(Number);
      var w = parseFloat(svg.getAttribute('width')) || 100;
      var h = parseFloat(svg.getAttribute('height')) || 32;
      var pad = 3;
      var min = Math.min.apply(null, raw);
      var max = Math.max.apply(null, raw);
      var range = max - min || 1;
      var xs = raw.map(function(_, i) {
        return pad + (i / (raw.length - 1)) * (w - pad * 2);
      });
      var ys = raw.map(function(v) {
        return pad + (1 - (v - min) / range) * (h - pad * 2);
      });
      var pts = xs.map(function(x, i) { return x + ',' + ys[i]; }).join(' ');

      /* color source */
      var color = svg.dataset.color === 'positive' ? 'var(--positive, #00D018)'
                : svg.dataset.color === 'negative' ? 'var(--negative, #D0002D)'
                : 'var(--accent-1, #F3A950)';

      if (svg.classList.contains('sparkline-line')) {
        var line = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
        line.setAttribute('points', pts);
        line.setAttribute('fill', 'none');
        line.setAttribute('stroke', color);
        line.setAttribute('stroke-width', '1.5');
        line.setAttribute('stroke-linejoin', 'round');
        line.setAttribute('stroke-linecap', 'round');
        svg.appendChild(line);
      }

      if (svg.classList.contains('sparkline-area')) {
        /* close path to bottom edge for fill */
        var areapts = pts
          + ' ' + xs[xs.length - 1] + ',' + (h - pad)
          + ' ' + xs[0] + ',' + (h - pad);
        var area = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        area.setAttribute('points', areapts);
        area.setAttribute('fill', color);
        area.setAttribute('fill-opacity', '0.12');
        area.setAttribute('stroke', 'none');
        svg.appendChild(area);
        /* line on top */
        var topLine = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
        topLine.setAttribute('points', pts);
        topLine.setAttribute('fill', 'none');
        topLine.setAttribute('stroke', color);
        topLine.setAttribute('stroke-width', '1.5');
        topLine.setAttribute('stroke-linejoin', 'round');
        svg.appendChild(topLine);
      }

      if (svg.classList.contains('sparkline-bar')) {
        var barW = Math.max(2, Math.floor((w - pad * 2) / raw.length) - 1);
        raw.forEach(function(v, i) {
          var barH = Math.max(2, Math.round(((v - min) / range) * (h - pad * 2)));
          var rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
          rect.setAttribute('x', String(pad + i * ((w - pad * 2) / raw.length)));
          rect.setAttribute('y', String(h - pad - barH));
          rect.setAttribute('width', String(barW));
          rect.setAttribute('height', String(barH));
          rect.setAttribute('fill', color);
          svg.appendChild(rect);
        });
      }

      svg.setAttribute('data-canvas-ready', 'true');
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderSparklines);
  } else {
    renderSparklines();
  }
})();
</script>
```

## Variant 2: area-sparkline

Same as line-sparkline with a semi-transparent fill under the line. Add `.sparkline-area` class.

```html
<svg class="sparkline sparkline-area"
     data-values="12,18,14,22,19,28,24,32"
     data-color="positive"
     width="140" height="40"
     viewBox="0 0 140 40"
     preserveAspectRatio="none">
</svg>
```

## Variant 3: bar-sparkline

Vertical bar columns. Add `.sparkline-bar` class.

```html
<svg class="sparkline sparkline-bar"
     data-values="5,8,6,12,9,14,11,16,13,18"
     data-color="accent"
     width="100" height="32"
     viewBox="0 0 100 32"
     preserveAspectRatio="none">
</svg>
```

## Standard dimensions

| Size | Width | Height | Use |
|---|---|---|---|
| Compact | 100px | 32px | KPI strip inline, stat-spotlight row |
| Standard | 140px | 40px | Standalone KPI card |
| Wide | 200px | 48px | Hero sparkline in stat-spotlight |

## Data binding

Pass comma-separated numbers via `data-values`. The JS normalizes them to the SVG coordinate space. Negative trends use `data-color="negative"`, positive use `data-color="positive"`, neutral use `data-color="accent"` (default).

## Color rules

| Condition | `data-color` | Rendered as |
|---|---|---|
| Positive trend / good metric | `positive` | `--positive` (#00D018) |
| Negative trend / bad metric | `negative` | `--negative` (#D0002D) |
| Neutral / general | `accent` (default) | `--accent-1` |

## Rules

- Never use Chart.js or D3 for sparklines — the inline SVG approach is sufficient and keeps the file self-contained.
- Never add axes, tick marks, or value labels to a sparkline — it ceases to be a sparkline.
- `data-canvas-ready="true"` is set synchronously by the JS render function — required for Playwright export.
- The same `<script>` block handles all three variants. Include it once per page, not once per sparkline.
- `preserveAspectRatio="none"` ensures the sparkline stretches to exactly its declared dimensions regardless of data range.
