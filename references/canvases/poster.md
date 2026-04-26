# Poster / Hero-Led Canvas

One big visual centerpiece + a ring of smaller support panels around it. The centerpiece is the *thing*: a flowchart, a fishbone, a quadrant matrix, a single timeline, an anatomical diagram, a mind-map, a venn — anything that wants the whole canvas's attention. Support panels add context (the legend, the takeaway, the source, related stats).

Best for single-subject deep-dives, "anatomy of X" pieces, framework explainers, mechanism breakdowns.

## Slots

| Slot | Purpose | Snippets that fit | Density cap |
|---|---|---|---|
| `header-strip` | Eyebrow + title + tagline (full bleed top) | (built into canvas) | 1 |
| `centerpiece` | The hero diagram. Owns 60-70% of vertical space. | Any complex snippet: flowchart, fishbone, swimlane, mind-map, anatomical, quadrant, venn, iceberg, journey-path, circular-flow, geographic, hierarchical-tree, pyramid, funnel | 1 |
| `support-card` | Small contextual panel around the centerpiece. | Compact snippets: kpi-strip, legend-strip, big-number, definition-list, comparison-mini, list, callout-block | up to 4 |
| `legend-strip` | Horizontal legend explaining centerpiece colors / roles | (built into canvas) | 1 |
| `footer` | Source + takeaway + attribution | (built into canvas) | 1 |

The centerpiece always owns the visual hierarchy. Support panels are visually quieter.

## Page skeleton

```html
<div class="infographic-canvas poster-canvas">

  <header class="poster-header" data-section-id="header">
    <span class="poster-eyebrow">{CATEGORY · TYPE}</span>
    <h1 class="poster-title gradient-text">{TITLE}</h1>
    <p class="poster-tagline">{One-line tagline that primes the centerpiece}</p>
  </header>

  <div class="poster-stage">

    <main class="poster-centerpiece" data-section-id="centerpiece">
      <!-- snippet: fishbone | flowchart | mind-map | anatomical | quadrant | etc. -->
    </main>

    <aside class="poster-supports">
      <div class="support-card" data-section-id="<id>"><!-- snippet --></div>
      <div class="support-card" data-section-id="<id>"><!-- snippet --></div>
      <div class="support-card" data-section-id="<id>"><!-- snippet --></div>
      <div class="support-card" data-section-id="<id>"><!-- snippet --></div>
    </aside>

  </div>

  <div class="poster-legend" data-section-id="legend">
    <!-- legend-strip snippet, horizontal -->
  </div>

  <footer class="poster-footer" data-section-id="footer">
    <span class="caption">{takeaway}</span>
    <span class="caption">{source} · {date}</span>
  </footer>
</div>
```

## Grid recipe

Centerpiece + right-side support column. At square/portrait widths, supports drop below.

```css
.poster-canvas {
  display: flex; flex-direction: column;
  gap: var(--gap-section);
  padding: 48px;
  min-height: 100vh;
}
.poster-header {
  text-align: left;
  border-bottom: 1px solid color-mix(in srgb, var(--text-muted) 25%, transparent);
  padding-bottom: 20px;
}
.poster-eyebrow {
  font: 700 12px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.12em;
  color: var(--accent-1);
}
.poster-title {
  font: 400 80px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  margin: 8px 0;
}
.poster-tagline {
  font: 400 18px/1.5 'Montserrat', sans-serif;
  color: var(--text-secondary);
  max-width: 72ch;
  margin: 0;
}

.poster-stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 320px;
  gap: 32px;
  flex: 1;
}
.poster-centerpiece {
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 22%, transparent),
      color-mix(in srgb, var(--accent-1) 44%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
  padding: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 600px;
}
.poster-supports {
  display: flex; flex-direction: column;
  gap: var(--gap-card);
}
.support-card {
  padding: 16px 18px;
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--text-muted) 30%, transparent);
  border-radius: var(--radius-card);
}

.poster-legend {
  border-top: 1px solid color-mix(in srgb, var(--text-muted) 25%, transparent);
  padding-top: 12px;
}
.poster-footer {
  display: flex; justify-content: space-between;
  font: 400 11px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
}

@media (max-width: 1100px) {
  .poster-stage {
    grid-template-columns: 1fr;
  }
  .poster-supports {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
  }
}
```

## Sizing

Poster is canvas-shape-flexible — it adapts to its centerpiece's natural aspect.

| Use case | Width |
|---|---|
| Landscape (default) | 1600 |
| Square (anatomical diagrams, quadrants) | 1080 (supports below) |
| Portrait (vertical centerpiece like iceberg, pyramid) | 1080 |
| Wide (geographic, swimlane) | 1920 |
| **Never** | < 900 |

The centerpiece dictates aspect. A pyramid wants portrait, a swimlane wants wide.

## Composition rules

- **One centerpiece. One.** This canvas is built around exactly one hero diagram. If the content needs two, it's not a poster — switch to bento.
- **Centerpiece needs ≥ 60% of vertical space.** Anything less and it stops being the hero.
- **Supports are quieter.** No gradient borders on support cards (use plain 1px borders), no gradient text in support card titles. Hierarchy demands the centerpiece dominate.
- **Legend goes below the stage, full width.** Inside the centerpiece is anti-pattern (it competes with the diagram).
- **Pixel-locked centerpiece is fine.** If the centerpiece snippet uses pixel-locked geometry (flowchart, fishbone, swimlane), the canvas doesn't fight it — it just hosts it. The poster canvas itself is fluid; the centerpiece can be pixel-locked inside its container.
- **Tagline primes the centerpiece.** ≤ 18 words. It tells the reader what they're about to see.
- **Footer carries the takeaway.** One line. The "so what" of the diagram.

## Style inheritance

Default: `aizfographics-style`. The centerpiece's snippet may impose its own role-based palette (e.g., focal/primary/secondary nodes) — those are pulled from the style's role tokens, not invented.

## Anti-patterns

- Two centerpieces side-by-side → that's a comparison or split layout, not a poster. Use bento with two large cards.
- Centerpiece smaller than the supports combined → kills the hierarchy. Make it bigger or pick bento.
- Support cards with gradient borders → they shouldn't compete with the centerpiece visually.
- Title shorter than the tagline → headline should always be the largest text on the page.
- Forgetting the legend → if the centerpiece uses color/role coding, the legend is mandatory. Without it, the poster fails its job.
