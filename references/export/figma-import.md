# Figma Import (html.to.design)

The canonical path for getting an infographic into Figma as editable layers.

## Tool

`html.to.design` — a Figma plugin that imports HTML/CSS directly into Figma as editable layer trees.

- Install: https://www.figma.com/community/plugin/1159123024924461424/html-to-design
- Free tier covers single-file HTML imports

## Workflow

1. Open Figma, create or open a file.
2. Run the `html.to.design` plugin.
3. Paste the URL of the HTML if hosted, or upload the local `.html` file.
4. The plugin renders the HTML in a headless browser and maps the DOM to Figma layers.
5. You get an editable frame tree: rectangles, text nodes, images, strokes — all native Figma.

## What imports cleanly

- All text (uppercase, weights, colors, letter-spacing)
- Backgrounds, panels, rounded corners
- Inline SVG charts (pass through as SVG frames in Figma, editable)
- Phosphor icons (as text — switch to SVG vectors inside Figma if editing is needed)
- Gradient borders (mapped to stroke gradients or border frames)
- Layout grids (preserved as auto-layout frames when possible)

## What needs manual cleanup

- `backdrop-filter` effects (become flat layers)
- CSS `mix-blend-mode` overlays
- Complex SVG masks
- Very deeply nested flex layouts (may flatten)

## Typical uses

| Need | Path |
|------|------|
| Quick PNG for social | `scripts/export.py` PNG |
| Final tweaks before client delivery | html.to.design → edit in Figma → export Figma's PNG |
| Design system capture (reuse components) | html.to.design → save as Figma components |

## Tips

- Use the creator-tools **Clean Download** button (or `ctCleanDownload()`) to get a stripped HTML without the creator-tools UI before importing.
- Turn off scroll-reveal animations before import (set `.section.visible` on every section in the saved HTML, or let `scripts/export.py` do it when you re-save from the screenshot run).
- If imports consistently break for a specific layout, file the issue — this is signal the HTML is using CSS features the plugin doesn't support.
