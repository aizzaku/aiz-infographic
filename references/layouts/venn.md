# Venn Diagram Layout

Overlapping sets with intersections. 2 or 3 circles, with labels for each set and the shared regions.

## When to use

- Feature overlap (what 3 products have in common)
- Audience segmentation intersections
- Skill / domain intersections ("AI × Design = ...")
- Positioning diagrams ("we sit at the intersection of X and Y")

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│         ╭───╮  ╭───╮          │
│        ╱     ╲╱     ╲         │
│       (   A   )(   B   )      │  intersections
│        ╲     ╱╲     ╱         │
│         ╰───╯  ╰───╯          │
│              ╰───╯            │
│               C               │
├──────────────────────────────┤
│ Legend (set definitions)     │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## HTML pattern (SVG for precise circle math)

```html
<div class="venn">
  <svg viewBox="0 0 400 400" class="venn-svg">
    <defs>
      <filter id="vglow" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="6"/>
      </filter>
    </defs>

    <!-- 3-circle arrangement (triangular) -->
    <circle cx="160" cy="160" r="110"
            fill="color-mix(in srgb, var(--accent-1) 25%, transparent)"
            stroke="var(--accent-1)" stroke-width="1.5"/>
    <circle cx="240" cy="160" r="110"
            fill="color-mix(in srgb, var(--accent-2) 25%, transparent)"
            stroke="var(--accent-2)" stroke-width="1.5"
            style="mix-blend-mode: screen;"/>
    <circle cx="200" cy="240" r="110"
            fill="color-mix(in srgb, #7C3AED 25%, transparent)"
            stroke="#7C3AED" stroke-width="1.5"
            style="mix-blend-mode: screen;"/>

    <!-- set labels on outer edges -->
    <text x="70" y="110" font-family="Montserrat" font-weight="700"
          font-size="14" fill="var(--accent-1)" text-transform="uppercase">
      Speed
    </text>
    <text x="300" y="110" font-family="Montserrat" font-weight="700"
          font-size="14" fill="var(--accent-2)" text-transform="uppercase"
          text-anchor="end">
      Cost
    </text>
    <text x="200" y="370" font-family="Montserrat" font-weight="700"
          font-size="14" fill="#7C3AED" text-anchor="middle">
      Quality
    </text>

    <!-- intersection label at center -->
    <text x="200" y="205" font-family="Bebas Neue"
          font-size="18" fill="var(--text-primary)" text-anchor="middle"
          letter-spacing="0.04em">
      Our sweet spot
    </text>
  </svg>

  <ul class="venn-legend">
    <li><span class="swatch" style="background: var(--accent-1);"></span>
      <strong>Speed</strong> — sub-second finality</li>
    <li><span class="swatch" style="background: var(--accent-2);"></span>
      <strong>Cost</strong> — under $0.001 per tx</li>
    <li><span class="swatch" style="background: #7C3AED;"></span>
      <strong>Quality</strong> — enterprise reliability</li>
  </ul>
</div>

<style>
.venn {
  display: grid;
  grid-template-columns: 1fr 220px;
  gap: 32px;
  align-items: center;
}
.venn-svg { width: 100%; max-width: 400px; }
.venn-legend {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font: 400 13px/1.3 'Montserrat', sans-serif;
  color: var(--text-secondary);
}
.venn-legend strong {
  color: var(--text-primary);
  text-transform: uppercase;
  font-size: 12px;
  letter-spacing: 0.05em;
}
.venn-legend .swatch {
  display: inline-block;
  width: 12px; height: 12px;
  border-radius: 3px;
  margin-right: 8px;
  vertical-align: -0.1em;
}
</style>
```

## 2-circle variant

For binary overlap, simplify to two horizontally-positioned circles with three labels: A alone, A∩B (intersection), B alone.

## Composition rules

- **2 or 3 circles only.** 4+ Venns need Euler diagrams; out of phase-2 scope.
- **Colors contrast** but additive overlap reads cleanly. Use `mix-blend-mode: screen` on circles 2 and 3 for natural intersection blending.
- **Label placement** is the art: set names on the outer edges of circles, intersection labels in the middle regions.
- **Legend mandatory** — intersection labels alone are cryptic without set definitions.

## Dimension guidance

Square (1080 × 1080) ideal. Landscape works with legend beside. Portrait is cramped.

## Anti-patterns

- Don't use Venn when sets don't actually overlap. A simple VS block is clearer.
- Don't stack 4+ circles. Becomes illegible fast.
- Don't use Venn for things that aren't truly set-overlap (no magic math).
