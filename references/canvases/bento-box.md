# Bento-Box Canvas

Mixed-span grid. One full-width hero strip, then 2-4 rows of cards with varying widths. Cards differ in size, weighted to content density. The default canvas — best for posters, release recaps, product overviews, ecosystem snapshots, anything with 6-12 heterogeneous sections.

## Slots

| Slot | Purpose | Snippets that fit | Density cap |
|---|---|---|---|
| `hero` | Title + meta + 3-4 inline KPIs (full bleed) | hero-strip (built into canvas) | 1 |
| `card-wide` | A column-spanning section, usually `1/3` or `2/4` | Any snippet: kpi-strip, comparison, list, statistical, grid-cards, chart, code-block, feature-roster | up to 5 wide cards |
| `card-medium` | Single-column card (~25% width on 4-col base) | Compact snippets: kpi-card, big-number, single chart, short list | up to 6 medium cards |
| `card-tall` | Vertical sidebar spanning two rows on the right edge | Lookup tables, top-N lists, ranked items, vertical timeline, mini-roadmap | up to 2 tall cards |
| `footer` | Optional full-bleed close | Source / version / CTA strip | 1 |

Total cells cap: **12** (1 hero + 11 secondary). Past 12, split into a second bento infographic — never shrink cards below readable.

## Page skeleton

```html
<div class="infographic-canvas">
  <div class="bento-grid">

    <section class="section bento-card s1" data-section-id="hero">
      <!-- snippet: hero-strip with eyebrow + title + tagline + kpi-strip -->
    </section>

    <!-- 2-4 rows of mixed-span cards. Each .s<N> class declares its grid placement. -->
    <section class="section bento-card s2" data-section-id="<id>"><!-- snippet --></section>
    <section class="section bento-card s3" data-section-id="<id>"><!-- snippet --></section>
    <section class="section bento-card s4" data-section-id="<id>"><!-- snippet --></section>

    <section class="section bento-card s5" data-section-id="<id>"><!-- snippet --></section>
    <section class="section bento-card s6" data-section-id="<id>"><!-- snippet --></section>
    <section class="section bento-card s7" data-section-id="<id>"><!-- snippet --></section>

    <footer class="section bento-card s8" data-section-id="footer"><!-- snippet --></footer>
  </div>
</div>
```

## Grid recipe

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: auto;
  gap: 16px;
  padding: 32px;
}
.bento-card {
  padding: 28px;
  border-radius: var(--radius-card);
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 22%, transparent),
      color-mix(in srgb, var(--accent-1) 44%, transparent)) border-box;
  border: 1px solid transparent;
  box-shadow: 0 0 32px color-mix(in srgb, var(--accent-1) 6%, transparent);
  display: flex; flex-direction: column;
  gap: var(--gap-element);
}
```

For very dense layouts, switch base to `repeat(6, 1fr)` and let cards span 2/3/4/6.

### Span recipes

| Pattern | Placement |
|---|---|
| Hero / footer (full bleed) | `grid-column: 1 / -1` |
| Two-up row (50/50) | `1 / 3` + `3 / 5` |
| Wide + two small (50/25/25) | `1 / 3` + `3` + `4` |
| Small + wide + small (25/50/25) | `1` + `2 / 4` + `4` |
| Four KPIs | `span 1` × 4 |
| Tall sidebar (spans two rows) | `grid-column: 4; grid-row: N / N+2` |
| Wide + tall sidebar | `1 / 4` (wide) + `4 / -1, row N / N+2` (tall) |

Place each card with explicit `grid-column` / `grid-row` declarations on per-section classes (`.s1`, `.s2`, ...). Never rely on auto-flow — content order rarely matches visual order.

## Sizing

Width-only. **1920w default** — bento collapses below that. Custom widths must stay ≥ 1440. Height grows with content; no fixed aspect ratio.

| Use case | Width |
|---|---|
| Wide / presentation / poster | 1920 |
| Custom wide | 1440-2400 |
| **Never** | < 1440 |

If the user asks for a 1080w bento, reroute to a different canvas (poster or dashboard).

## Composition rules

- **One hero, always.** Full-bleed first row carries title, eyebrow, 2-4 inline KPIs.
- **Vary card sizes by content weight.** A card with 8 features deserves more columns than a card with 1 stat. If every card is the same size, the user wants a different canvas (poster or a snippet-only grid).
- **No cross-card connectors.** Bento is fluid grid — arrows/leaders between cells will desync. If the content needs connectors, switch canvas.
- **Group adjacent rows by theme.** KPI row → feature row → ecosystem row. The grid is heterogeneous; the reading flow shouldn't be.
- **Accent emphasis cap: 3.** No more than 3 cards (hero counts) get gradient-text titles or accent-fill. Past that, hierarchy collapses.
- **Pixel-locked sections live elsewhere.** If a single card needs internal pixel-locked geometry (e.g., a flowchart snippet inside one card), that snippet handles its own pixel lock — the card is just its container.

## Style inheritance

Inherits `aizfographics-style` by default. Other styles work but bento was designed for the gradient-border + dark-canvas aesthetic — clean-minimal looks under-decorated, blueprint over-decorated.

## When NOT to use bento

- Long-form storytelling → Editorial canvas
- Single subject deep-dive → Poster canvas
- Metrics-only snapshot → Dashboard canvas
- Sequential read-through (timeline, process) → use a single timeline/process snippet inside a poster canvas, or pick a different canvas entirely
- Side-by-side comparison of two options → Poster canvas with a comparison snippet, or a custom split

## Anti-patterns

- 12 identical cells with no hero → that's a grid, not bento. Pick poster + grid-cards snippet.
- Cards spanning random rows without column-edge alignment → reads as broken.
- Mixed card padding (some 16px, some 32px) → keep `--pad-card` consistent.
- Hero card without inline KPIs → wastes the hero slot. Either add the KPIs or shrink the hero to a regular wide card.
