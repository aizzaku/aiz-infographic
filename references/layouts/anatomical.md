# Anatomical Layout

"Exploded diagram" style. A central image or schematic with callout lines radiating to labels that describe each part. Like a textbook anatomy figure.

## When to use

- Product feature callouts (dashboard screenshot → labels explaining each panel)
- Mechanism / component breakdown (engine parts, protocol components)
- Character / gear breakdown in gaming content
- Visual specs — "what each part does"

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`, `connectors.md` (callout leader lines).

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│   Label 1                     │
│   ╲                           │
│    ╲     [  image  ]          │
│     ╲       /                 │
│      ╲     /──Label 2         │
│       ╲                       │
│        ───Label 3             │
│                               │
│   Label 4 ───                 │
├──────────────────────────────┤
│ Spec table / summary         │  optional
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## HTML pattern

```html
<div class="anatomy">
  <div class="anatomy-subject">
    <!-- central image or SVG -->
    <img src="{product_shot}" alt="{product}" class="anatomy-img">

    <!-- callout hotspots positioned relative to image -->
    <div class="hotspot" style="--x: 28%; --y: 22%; --ref-x: 0%; --ref-y: 10%;">
      <span class="hotspot-num">01</span>
    </div>
    <div class="hotspot" style="--x: 65%; --y: 35%; --ref-x: 100%; --ref-y: 20%;">
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
  gap: 32px;
  align-items: center;
}
.anatomy-subject {
  position: relative;
  aspect-ratio: 4 / 3;
  background: var(--panel);
  border-radius: var(--radius-card);
  border: 1px solid color-mix(in srgb, var(--accent-1) 20%, transparent);
  overflow: hidden;
}
.anatomy-img {
  width: 100%; height: 100%; object-fit: contain;
}
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
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.anatomy-legend li {
  display: grid;
  grid-template-columns: 36px 1fr;
  gap: 12px;
  align-items: start;
}
.anatomy-legend .num {
  font: 400 24px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
  text-align: center;
}
</style>
```

## Leader-line variant

For a more textbook look, add SVG leader lines from hotspots to labels in margin. Requires hand-tuning coordinates per image — best for static compositions.

## Composition rules

- **3–8 callouts.** Fewer feels sparse; more becomes a labeled cloud.
- **Numbered hotspots, matched numbered legend.** Clean pairing beats trying to squeeze labels next to hotspots.
- **Subject image dominates** — ~60% of composition width in 2-col layout.
- **Hotspots non-overlapping.** Reserve visual space for each.
- **Legend wording matters.** One line per item. Title + one-sentence body.

## Dimension guidance

Landscape (16:9) for wide product shots. Portrait for tall subjects (characters, gear). Square if the subject fits.

## Anti-patterns

- Don't use anatomical when you don't have a strong central visual. Without an image, it's just a numbered list.
- Don't cram numbered labels directly onto the image. Use the margin legend pattern.
- Don't rely on color alone to distinguish hotspots — numbers carry the semantics.
