# Timeline Layout

Events or milestones arranged chronologically. Horizontal by default (88% of DNA). Vertical for dense lists or narrow portrait canvases.

## When to use

- Product roadmap, release history
- Project timeline, milestones
- Vesting schedule (standalone infographic, not tucked inside tokenomics)
- Historical retrospective ("year in review", "Season 3 recap")
- Any sequence of dated events

## Required elements

`connectors.md` (timeline spine, dots), `text.md`, `layout.md`, `decorative.md`, `icons.md`. Optionally `data-widgets.md` for per-milestone metrics.

## Orientation choice

| Events | Portrait canvas | Landscape canvas |
|--------|----------------|------------------|
| 3–5 | Horizontal | Horizontal |
| 6–8 | Vertical | Horizontal (compressed) |
| 9+ | Vertical | Vertical (2-col) |

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│ Timeline span (from → to)    │  small caption
├──────────────────────────────┤
│ ○──────○──────○──────○──────○ │  horizontal OR
│ TGE    Cliff  25%   50%   100% │   vertical stack
├──────────────────────────────┤
│ Event detail cards           │  optional — one card per milestone
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## Horizontal variant HTML

Use the `.timeline` spine pattern from `connectors.md`. For richer event cards below the spine:

```html
<section class="section">
  <div class="timeline">
    <div class="timeline-spine"></div>
    <div class="timeline-nodes">
      <div class="tnode">
        <span class="tdot"></span>
        <span class="tlabel">Launch</span>
        <span class="tdate">Q1 2026</span>
      </div>
      <!-- repeat -->
    </div>
  </div>

  <div class="timeline-details">
    <div class="event-card">
      <span class="badge">Q1 2026</span>
      <h3 class="card-title">Mainnet launch</h3>
      <p class="body">Network activation with initial validator set.</p>
    </div>
    <!-- repeat per event -->
  </div>
</section>

<style>
.timeline-details {
  display: grid;
  grid-template-columns: repeat(var(--event-count, 5), 1fr);
  gap: var(--gap-card);
  margin-top: 8px;
}
.event-card {
  padding: 12px;
  background: var(--panel);
  border-radius: var(--radius-card);
  border: 1px solid color-mix(in srgb, var(--accent-1) 20%, transparent);
  display: flex;
  flex-direction: column;
  gap: 6px;
}
</style>
```

## Vertical variant HTML

```html
<div class="timeline-v">
  <div class="tv-item">
    <div class="tv-marker">
      <span class="tv-dot"></span>
      <span class="tv-line"></span>
    </div>
    <div class="tv-body">
      <div class="tv-date">Q1 2026</div>
      <h3 class="card-title">Mainnet launch</h3>
      <p class="body">Network activation with initial validator set.</p>
    </div>
  </div>
  <!-- repeat; last item drops .tv-line -->
</div>

<style>
.timeline-v { display: flex; flex-direction: column; gap: 0; }
.tv-item {
  display: grid;
  grid-template-columns: 32px 1fr;
  gap: 16px;
  min-height: 80px;
}
.tv-marker {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.tv-dot {
  width: 14px; height: 14px;
  border-radius: 50%;
  background: var(--accent-1);
  box-shadow: 0 0 10px color-mix(in srgb, var(--accent-1) 40%, transparent);
  margin-top: 4px;
  flex-shrink: 0;
}
.tv-line {
  flex: 1;
  width: 1px;
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--accent-1) 40%, transparent),
    transparent);
  margin-top: 4px;
}
.tv-body { padding-bottom: 20px; }
.tv-date {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent-1);
  margin-bottom: 6px;
}
</style>
```

## Composition rules

- Event labels always include BOTH a date and a descriptor. Dates alone ("Q3") mean nothing without context.
- Past vs. future: past events can be dimmed (`filled` dot, `--text-secondary` label). Future events: bright dot, full-opacity label.
- Spans > 18 months: consider chunking into phases (each phase = one timeline segment).
- Avoid more than 8 nodes on a horizontal timeline — labels get cramped. Switch to vertical.

## Anti-patterns

- Never label dates in ambiguous formats ("soon", "upcoming"). Use quarter or month.
- Never show a timeline with only one node. It's a callout, not a timeline.
- Don't use arrows on a timeline — the spine already implies direction.
