# Maps — Structural Pattern Only (Phase 1)

Geographic visualization is NOT fully authored in phase 1. This file documents the structural pattern so a map-containing request can still produce something sensible.

## When you need a real map

If the user explicitly asks for a geographic map (world coverage, regional breakdown), say:

> Geographic map rendering isn't in the phase-1 scope. I can produce a styled placeholder for you to swap in your own SVG map, or I can build the infographic around a different visual (bar chart of regions, grid of flags, etc.). Which do you prefer?

## Placeholder pattern

```html
<div class="map-placeholder">
  <div class="map-placeholder-inner">
    <i class="ph-bold ph-globe" style="font-size: 48px;"></i>
    <p class="caption">Insert world map SVG here</p>
    <p class="caption">Source suggestion: simplemaps.com/resources, naturalearthdata.com</p>
  </div>
</div>

<style>
.map-placeholder {
  aspect-ratio: 2 / 1;
  background: var(--panel);
  border: 1px dashed color-mix(in srgb, var(--text-primary) 20%, transparent);
  border-radius: var(--radius-card);
  display: flex;
  align-items: center;
  justify-content: center;
}
.map-placeholder-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: var(--text-muted);
  text-align: center;
}
</style>
```

## Regional breakdown (non-map alternative)

When map-like data can be communicated without cartography:

```html
<div class="region-grid">
  <div class="region-card">
    <div class="region-flag"><img src="..." alt="USA"></div>
    <div class="region-name">North America</div>
    <div class="region-value">42%</div>
  </div>
  <!-- repeat -->
</div>
```

Style this as a `grid-auto` with icon + metric pairs — essentially a `data-widgets` row with flag images. Often communicates the same thing as a choropleth without the SVG complexity.

## Rules

- Never fabricate a map SVG. Always use a known open-data source or a placeholder.
- If the user has a specific region focus (Asia, EU, etc.), suggest a grid of country cards rather than a map.
- Phase 2 will add real SVG world/region maps with styled data binding.
