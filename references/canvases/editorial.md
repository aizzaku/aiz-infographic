# Editorial / Magazine Canvas

Long-form columnar reading. Big headline, optional drop cap, body text in 1-2 columns, pull quotes, sidebar callouts, inline visuals. Best for storytelling — research deep-dives, opinion pieces, narrative product reveals, "how it really works" explainers, post-mortems.

## Slots

| Slot | Purpose | Snippets that fit | Density cap |
|---|---|---|---|
| `masthead` | Eyebrow / category / date strip above the headline | (built into canvas) | 1 |
| `headline` | Massive display-font title + subdeck | (built into canvas) | 1 |
| `lede` | Opening paragraph with optional drop cap | (built into canvas) | 1 |
| `body-column` | Main reading column. Sequential prose paragraphs interleaved with snippets. | Any narrative-fitting snippet: kpi-strip, big-number, comparison, list, mini-chart, timeline, fishbone, callout-block, image-figure | unlimited (governed by reading time) |
| `sidebar` | Optional right-rail for asides, definitions, related-links, mini-stats | Compact snippets: kpi-card, definition-list, related-links, fact-box | up to 4 sidebar items |
| `pull-quote` | Inset large-text quote pulled from the body | (built into canvas) | up to 3 across the piece |
| `byline-footer` | Author / date / source attribution at the close | (built into canvas) | 1 |

No total cell cap — editorial is governed by **reading time** (target 3-7 minutes / ~600-1500 words). Past that, split into a multi-part series.

## Page skeleton

```html
<div class="infographic-canvas editorial-canvas">

  <header class="editorial-masthead" data-section-id="masthead">
    <span class="ed-eyebrow">{CATEGORY}</span>
    <span class="ed-meta">{DATE} · {AUTHOR}</span>
  </header>

  <h1 class="editorial-headline" data-section-id="headline">
    {Headline} <span class="ed-subdeck">{One-line subdeck}</span>
  </h1>

  <p class="editorial-lede" data-section-id="lede">
    <span class="dropcap">{F}</span>{irst paragraph that hooks the reader and frames the piece.}
  </p>

  <div class="editorial-body" data-section-id="body">
    <p>...prose paragraph...</p>
    <p>...prose paragraph...</p>
    <!-- inline snippet -->
    <figure class="ed-figure" data-section-id="<id>"><!-- snippet --></figure>
    <p>...prose continues...</p>
    <blockquote class="ed-pull-quote">{Pull quote text}</blockquote>
    <p>...more prose...</p>
  </div>

  <aside class="editorial-sidebar" data-section-id="sidebar">
    <!-- 1-4 compact snippets stacked -->
  </aside>

  <footer class="editorial-byline" data-section-id="byline">
    <span>{Author} · {Source} · {Date}</span>
  </footer>
</div>
```

## Grid recipe

Two-column at wide widths, single-column at narrow widths.

```css
.editorial-canvas {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 280px;
  grid-template-areas:
    "masthead masthead"
    "headline headline"
    "lede     lede"
    "body     sidebar"
    "byline   byline";
  gap: 32px 40px;
  padding: 64px 72px;
  max-width: 1280px;
  margin: 0 auto;
}
.editorial-masthead { grid-area: masthead; }
.editorial-headline { grid-area: headline; }
.editorial-lede     { grid-area: lede; }
.editorial-body     { grid-area: body; }
.editorial-sidebar  { grid-area: sidebar; align-self: start; position: sticky; top: 32px; }
.editorial-byline   { grid-area: byline; }

.editorial-headline {
  font: 400 88px/0.95 'Bebas Neue', sans-serif;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  margin: 0;
  background: linear-gradient(30deg, var(--accent-1), var(--accent-2));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.ed-subdeck {
  display: block;
  font: 400 24px/1.3 'Montserrat', sans-serif;
  letter-spacing: normal;
  text-transform: none;
  color: var(--text-secondary);
  margin-top: 12px;
  -webkit-text-fill-color: var(--text-secondary);
}
.editorial-lede {
  font: 400 19px/1.55 'Montserrat', sans-serif;
  color: var(--text-primary);
  max-width: 64ch;
}
.dropcap {
  float: left;
  font: 400 84px/0.85 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  margin: 4px 12px 0 0;
  text-transform: uppercase;
}
.editorial-body { font: 400 16px/1.65 'Montserrat', sans-serif; color: var(--text-primary); }
.editorial-body p { margin: 0 0 18px; max-width: 64ch; }
.ed-pull-quote {
  border-left: 3px solid var(--accent-1);
  padding: 8px 0 8px 24px;
  margin: 28px 0;
  font: 700 22px/1.4 'Montserrat', sans-serif;
  color: var(--text-primary);
  text-transform: uppercase;
  letter-spacing: 0.03em;
  max-width: 56ch;
}
.ed-figure {
  margin: 28px 0;
  padding: 20px;
  background: var(--panel);
  border-radius: var(--radius-card);
  border: 1px solid color-mix(in srgb, var(--accent-1) 18%, transparent);
}
.editorial-sidebar { display: flex; flex-direction: column; gap: 20px; }
```

At narrow widths (< 900px), drop sidebar into single-column flow:

```css
@media (max-width: 900px) {
  .editorial-canvas {
    grid-template-columns: 1fr;
    grid-template-areas: "masthead" "headline" "lede" "body" "sidebar" "byline";
  }
  .editorial-sidebar { position: static; }
}
```

## Sizing

Editorial is portrait-leaning, content-driven height.

| Use case | Width |
|---|---|
| Default / desktop reading | 1280 (max-width) |
| Tablet | 900 |
| Mobile | 720 (sidebar collapses) |
| **Never** | < 720 (text becomes cramped) |

## Composition rules

- **Headline does the work.** Bebas Neue at 88px+, gradient text. The headline carries the visual weight; everything else is supporting.
- **Lede ≤ 60 words.** It's a hook, not a summary.
- **Body in one column at narrow widths, two-column reading is anti-pattern for infographics.** The sidebar is a separate column — that's not "two-column body".
- **Snippets break up prose.** Aim for one inline snippet (chart, comparison, etc.) every 2-3 paragraphs of body. Long unbroken text walls fail the visual brief.
- **Pull quotes punctuate, don't repeat.** A pull quote highlights a different sentence than the surrounding paragraph already says.
- **Sidebar is supplementary.** Critical info goes in the body. Sidebar = related-links, definitions, side-stats.
- **Drop cap once, on the lede only.** Never per-paragraph.
- **Reading flow is top-to-bottom, left-to-right.** Sidebar reads as parallel context, not as a path.

## Style inheritance

Default: `aizfographics-style` (dark canvas, Bebas Neue + Montserrat). The `editorial` style file (`references/styles/editorial.md`) is a cleaner light-mode variant designed specifically for this canvas — recommend it when the user picks Editorial canvas without specifying a style.

## Anti-patterns

- Headline shorter than 4 words → not a headline, it's a tag. Either expand or pick a different canvas.
- More than 3 pull quotes → quotes lose impact when they're everywhere.
- Sidebar with > 4 items → break into two infographics or move some content into the body.
- Putting a flowchart / mind-map / fishbone snippet in the body → those are non-narrative. Use poster canvas instead.
- Dropcap on every paragraph → reads as decoration, not typography.
