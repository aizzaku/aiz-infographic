# Geographic Layout

Map-anchored data. Regions, countries, or city-level breakdowns with data overlaid. Phase 2 supports both real maps (SVG world/region) and map-alternative grid views.

## When to use

- Regional user distribution
- Multi-chain geographic presence (deployments by region)
- Regulatory-landscape infographics
- Event locations
- Infrastructure footprint (data centers, nodes)

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`, `data-widgets.md`, `maps.md`.

## Variant 1 — Real SVG map

Requires a source SVG (Natural Earth or SimpleMaps) dropped in as inline SVG or `<img src>`. The skill does NOT bundle map SVGs — user provides or you fetch from a known open-data source.

```html
<section class="section">
  <div class="geomap">
    <!-- inline SVG world map (paths for each country/region) -->
    <!-- Apply data-driven fills via CSS or inline attributes -->
    <svg class="geomap-svg" viewBox="0 0 1000 500">
      <g class="regions">
        <!-- each region is a <path> with data-region attribute and
             fill derived from a value -->
        <path d="M ..." data-region="NA"
              fill="color-mix(in srgb, var(--accent-1) 60%, var(--panel))"/>
        <path d="M ..." data-region="EU"
              fill="color-mix(in srgb, var(--accent-1) 85%, var(--panel))"/>
        <path d="M ..." data-region="AS"
              fill="color-mix(in srgb, var(--accent-1) 40%, var(--panel))"/>
      </g>
    </svg>

    <!-- overlay pins / markers -->
    <div class="geopin" style="--x: 22%; --y: 34%;">
      <span class="geopin-dot"></span>
      <span class="geopin-label">NYC</span>
    </div>
  </div>

  <!-- legend with value scale -->
  <div class="geomap-legend">
    <div class="scale">
      <span class="scale-bar"></span>
      <div class="scale-labels">
        <span>0</span>
        <span>10k</span>
        <span>100k+</span>
      </div>
    </div>
  </div>
</section>

<style>
.geomap { position: relative; }
.geomap-svg { width: 100%; height: auto; }
.regions path {
  stroke: color-mix(in srgb, var(--text-primary) 12%, transparent);
  stroke-width: 0.5;
  transition: fill 0.2s;
}
.geopin {
  position: absolute;
  left: var(--x); top: var(--y);
  transform: translate(-50%, -50%);
  display: flex;
  align-items: center;
  gap: 6px;
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
  display: flex;
  justify-content: space-between;
  font: 400 10px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
}
</style>
```

## Variant 2 — Map-alternative grid (no SVG map)

When an SVG map isn't practical (licensing, time, unfamiliar regions), pivot to a grid of flag cards:

```html
<div class="grid-auto">
  <div class="region-card">
    <div class="region-flag"><img src="{flag_url}" alt="{country}"></div>
    <div class="region-name">United States</div>
    <div class="region-value">42%</div>
  </div>
  <!-- repeat -->
</div>
```

Use Iconify's `twemoji` or `flag` icon set for flags, or user-supplied flag SVGs.

## Choropleth fill strategy

Map fills convey quantity:
- 0% — `var(--panel)` (no data or null)
- Low — `color-mix(in srgb, var(--accent-1) 20%, var(--panel))`
- Mid — `color-mix(in srgb, var(--accent-1) 50%, var(--panel))`
- High — `color-mix(in srgb, var(--accent-1) 85%, var(--panel))`
- Peak — solid `var(--accent-1)`

## Composition rules

- **Map below, legend beside or below.** Map without a scale is decorative, not informational.
- **Pins for specific places, fills for regions.** Don't mix heavily — pick a primary encoding.
- **Neutral region outlines.** The data is in the fills, not the borders.
- **Projection matters.** If you use a map, the projection (Mercator, Equal Earth) affects political perception. Note it in a caption when using non-trivial projections.

## Dimension guidance

Landscape (16:9) for world maps. Portrait for country-level (vertical continents). Square for single-region (a country).

## Anti-patterns

- Don't fabricate a map SVG. Use an open-data source or pivot to grid-alternative.
- Don't overload the map with text. Use pins sparingly; put detail in a side panel.
- Don't rainbow-scale choropleths. Single-hue lightness scales read cleanest.
- Don't forget Antarctica exists but isn't the focus — crop or omit when irrelevant.
