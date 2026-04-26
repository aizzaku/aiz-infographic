# Geographic Snippet

Map-anchored data. Regions/countries/cities with data overlaid. Real SVG map OR map-alternative grid.

## When to use

- Regional user distribution
- Multi-chain geographic presence (deployments by region)
- Regulatory landscape
- Event locations
- Infrastructure footprint

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| poster | centerpiece | Best — maps need horizontal space |
| dashboard | panel-large (w-12) | World map across the panel |
| bento-box | card-wide (`1/-1`) | Compact regional map |

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`, `data-widgets.md`, `maps.md`.

## Variant 1 — Real SVG map (choropleth + pins)

User provides the SVG (Natural Earth or SimpleMaps). The skill does NOT bundle map SVGs.

```html
<div class="geomap">
  <svg class="geomap-svg" viewBox="0 0 1000 500">
    <g class="regions">
      <path d="M ..." data-region="NA"
            fill="color-mix(in srgb, var(--accent-1) 60%, var(--panel))"/>
      <path d="M ..." data-region="EU"
            fill="color-mix(in srgb, var(--accent-1) 85%, var(--panel))"/>
      <path d="M ..." data-region="AS"
            fill="color-mix(in srgb, var(--accent-1) 40%, var(--panel))"/>
    </g>
  </svg>

  <div class="geopin" style="--x: 22%; --y: 34%;">
    <span class="geopin-dot"></span>
    <span class="geopin-label">NYC</span>
  </div>
</div>

<div class="geomap-legend">
  <div class="scale">
    <span class="scale-bar"></span>
    <div class="scale-labels">
      <span>0</span><span>10k</span><span>100k+</span>
    </div>
  </div>
</div>

<style>
.geomap { position: relative; }
.geomap-svg { width: 100%; height: auto; }
.regions path {
  stroke: color-mix(in srgb, var(--text-primary) 12%, transparent);
  stroke-width: 0.5;
}
.geopin {
  position: absolute;
  left: var(--x); top: var(--y);
  transform: translate(-50%, -50%);
  display: flex; align-items: center; gap: 6px;
}
.geopin-dot {
  width: 10px; height: 10px;
  border-radius: 50%;
  background: var(--accent-1);
  box-shadow: 0 0 10px color-mix(in srgb, var(--accent-1) 80%, transparent);
}
.geopin-label {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  color: var(--text-primary);
  background: color-mix(in srgb, var(--canvas) 80%, transparent);
  padding: 2px 6px;
  border-radius: 3px;
}
.scale { display: flex; flex-direction: column; gap: 4px; max-width: 280px; }
.scale-bar {
  height: 8px;
  background: linear-gradient(90deg,
    var(--panel),
    color-mix(in srgb, var(--accent-1) 50%, var(--panel)),
    var(--accent-1));
  border-radius: 4px;
}
.scale-labels {
  display: flex; justify-content: space-between;
  font: 400 10px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
}
</style>
```

## Variant 2 — Flag-grid alternative (no SVG map)

```html
<div class="grid grid-4">
  <div class="region-card">
    <div class="region-flag"><img src="{flag_url}" alt="{country}"></div>
    <div class="region-name">United States</div>
    <div class="region-value">42%</div>
  </div>
  <!-- repeat -->
</div>
```

Flag sources: Iconify `twemoji` / `flag` icon set, or user-supplied SVGs.

## Choropleth fill scale

Single-hue lightness scale:
- 0% — `var(--panel)` (no data)
- Low — `color-mix(in srgb, var(--accent-1) 20%, var(--panel))`
- Mid — `color-mix(in srgb, var(--accent-1) 50%, var(--panel))`
- High — `color-mix(in srgb, var(--accent-1) 85%, var(--panel))`
- Peak — solid `var(--accent-1)`

## Composition rules

- Map below, legend beside or below. Map without scale is decorative.
- Pins for specific places, fills for regions. Don't mix heavily — pick a primary encoding.
- Neutral region outlines. Data is in the fills, not borders.
- Note projection (Mercator, Equal Earth) in caption when non-trivial.

## Anti-patterns

- Fabricating map SVGs (use open-data source or pivot to grid).
- Overloading with text — pins sparingly, detail in side panel.
- Rainbow choropleth — single-hue lightness reads cleanest.
- Antarctica when irrelevant — crop or omit.
