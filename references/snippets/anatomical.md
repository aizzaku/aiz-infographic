# Anatomical Snippet

"Exploded diagram" style. Central image or schematic with numbered hotspots and a side legend describing each part.

## When to use

- Product feature callouts (dashboard screenshot → labels per panel)
- Mechanism / component breakdown (engine parts, protocol components)
- Character / gear breakdown in gaming content
- Visual specs — "what each part does"

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| poster | centerpiece | Best — needs space for image + legend side panel |
| bento-box | card-wide (`1/-1`) | Compact 3-5 hotspot anatomical |
| editorial | body-column | Inline figure with legend below |

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`, `connectors.md` (callout leader lines).

## HTML pattern (image + numbered hotspots + legend)

```html
<div class="anatomy">
  <div class="anatomy-subject">
    <img src="{product_shot}" alt="{product}" class="anatomy-img">
    <div class="hotspot" style="--x: 28%; --y: 22%;">
      <span class="hotspot-num">01</span>
    </div>
    <div class="hotspot" style="--x: 65%; --y: 35%;">
      <span class="hotspot-num">02</span>
    </div>
    <!-- etc -->
  </div>

  <ol class="anatomy-legend">
    <li>
      <span class="num">01</span>
      <div>
        <h4 class="card-title">Primary display</h4>
        <p class="body">Main information panel with real-time updates.</p>
      </div>
    </li>
    <li>
      <span class="num">02</span>
      <div>
        <h4 class="card-title">Control cluster</h4>
        <p class="body">Input controls and primary actions.</p>
      </div>
    </li>
    <!-- repeat -->
  </ol>
</div>

<style>
.anatomy {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 32px; align-items: center;
}
.anatomy-subject {
  position: relative;
  aspect-ratio: 4 / 3;
  background: var(--panel);
  border-radius: var(--radius-card);
  border: 1px solid color-mix(in srgb, var(--accent-1) 20%, transparent);
  overflow: hidden;
}
.anatomy-img { width: 100%; height: 100%; object-fit: contain; }
.hotspot {
  position: absolute;
  left: var(--x); top: var(--y);
  transform: translate(-50%, -50%);
  z-index: 2;
}
.hotspot-num {
  display: flex; align-items: center; justify-content: center;
  width: 28px; height: 28px;
  border-radius: 50%;
  background: var(--accent-1);
  color: var(--on-accent);
  font: 700 12px/1 'Montserrat', sans-serif;
  box-shadow: 0 0 12px color-mix(in srgb, var(--accent-1) 60%, transparent);
}
.anatomy-legend {
  list-style: none; padding: 0; margin: 0;
  display: flex; flex-direction: column; gap: 12px;
}
.anatomy-legend li {
  display: grid;
  grid-template-columns: 36px 1fr;
  gap: 12px; align-items: start;
}
.anatomy-legend .num {
  font: 400 24px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
  text-align: center;
}
</style>
```

## Leader-line variant (textbook style)

For a more textbook look, add SVG leader lines from hotspots to labels in the margin (rather than separate side legend). Requires hand-tuning per image — best for static compositions.

## Composition rules

- 3-8 callouts. Fewer feels sparse; more becomes a labeled cloud.
- Numbered hotspots paired with numbered legend. Cleaner than labels next to hotspots.
- Subject image dominates — ~60% of composition width in 2-col layout.
- Hotspots non-overlapping. Reserve visual space.
- Legend: title + one-sentence body per item.

## Anti-patterns

- No strong central visual → without an image, it's just a numbered list.
- Cramming numbered labels onto the image (use margin legend).
- Color-only hotspot semantics — numbers carry the meaning.
