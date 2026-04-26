# Timeline Snippet

Events or milestones arranged chronologically. Horizontal by default, vertical for dense lists or narrow slots.

## When to use

- Roadmap, release history, vesting schedule
- Historical retrospective ("year in review", "season recap")
- Any sequence of dated events (≥ 2 nodes, ≤ 8 horizontal / ≤ 12 vertical)

## Slot fit

| Canvas | Slot | Orientation | Notes |
|---|---|---|---|
| bento-box | card-wide (`1/3` or `1/-1`) | horizontal | 3-5 nodes fit in `1/3`; full-bleed for 6-8 |
| bento-box | card-tall | vertical | Best place for 8-12 events |
| editorial | body-column | horizontal | Inline figure between paragraphs, ≤ 5 nodes |
| editorial | sidebar | vertical | Mini timeline (3-4 dates) as supporting context |
| dashboard | panel-large (w-12) | horizontal | Period markers across the panel |
| poster | centerpiece | horizontal or vertical | Full timeline as the hero diagram |
| poster | support-card | vertical | Mini timeline supporting another centerpiece |

## Required elements

`connectors.md` (timeline spine, dots), `text.md`, `layout.md`. Optionally `data-widgets.md` for per-milestone metrics.

## Horizontal pattern

```html
<div class="timeline">
  <div class="timeline-spine"></div>
  <div class="timeline-nodes">
    <div class="tnode">
      <span class="tdot"></span>
      <span class="tlabel">Launch</span>
      <span class="tdate">Q1 2026</span>
    </div>
    <!-- repeat per event -->
  </div>
</div>

<!-- Optional event-detail cards row beneath the spine -->
<div class="timeline-details">
  <div class="event-card">
    <span class="badge">Q1 2026</span>
    <h3 class="card-title">Mainnet launch</h3>
    <p class="body">Network activation with initial validator set.</p>
  </div>
  <!-- repeat -->
</div>

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
  display: flex; flex-direction: column; gap: 6px;
}
</style>
```

## Vertical pattern

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
.tv-marker { position: relative; display: flex; flex-direction: column; align-items: center; }
.tv-dot {
  width: 14px; height: 14px;
  border-radius: 50%;
  background: var(--accent-1);
  box-shadow: 0 0 10px color-mix(in srgb, var(--accent-1) 40%, transparent);
  margin-top: 4px; flex-shrink: 0;
}
.tv-line {
  flex: 1; width: 1px;
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--accent-1) 40%, transparent),
    transparent);
  margin-top: 4px;
}
.tv-body { padding-bottom: 20px; }
.tv-date {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--accent-1);
  margin-bottom: 6px;
}
</style>
```

## Composition rules

- Every node has BOTH a date and a descriptor. Dates alone ("Q3") mean nothing.
- Past events: dimmed dot + `--text-secondary` label. Future: bright dot + full opacity.
- Spans > 18 months → chunk into phases (each phase = its own timeline segment).
- > 8 nodes horizontal → switch to vertical.

## Anti-patterns

- Ambiguous dates ("soon", "upcoming") → use quarter or month.
- Single-node timeline → that's a callout, not a timeline.
- Decorative arrows on the spine → the spine already implies direction.
