# Roadmap Snippet

Forward-looking phased plan with status semantics. Unlike `timeline` (neutral past/future), roadmap is anticipatory — *what's shipping next*.

## When to use

- Project roadmap (Q1/Q2/Q3 shipping schedule)
- Product release plan
- Season or epoch plan
- Post-launch rollout

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| bento-box | card-wide (`1/-1`) | Horizontal phases, full-bleed |
| editorial | body-column | Inline figure between paragraphs |
| dashboard | panel-large (w-12) | Phase grid across the panel |
| poster | centerpiece | Roadmap as the hero (3-5 phases) |

## Required elements

`connectors.md`, `text.md`, `layout.md`, `decorative.md`, `icons.md`. Optional `data-widgets.md`.

## Horizontal phase pattern

```html
<div class="roadmap-h">
  <div class="phase shipped">
    <div class="phase-header">
      <span class="phase-label">Q1 2026</span>
      <span class="phase-status">Shipped</span>
    </div>
    <h3 class="card-title">Foundation</h3>
    <ul class="phase-features">
      <li><i class="ph-bold ph-check-circle"></i>Testnet launch</li>
      <li><i class="ph-bold ph-check-circle"></i>Core SDK v1</li>
      <li><i class="ph-bold ph-check-circle"></i>Block explorer</li>
    </ul>
  </div>

  <div class="phase active">
    <div class="phase-header">
      <span class="phase-label">Q2 2026</span>
      <span class="phase-status">In progress</span>
    </div>
    <h3 class="card-title">Mainnet</h3>
    <ul class="phase-features">
      <li><i class="ph-bold ph-arrow-right"></i>Validator onboarding</li>
      <li><i class="ph-bold ph-arrow-right"></i>Bridge v1</li>
      <li><i class="ph-bold ph-circle"></i>Governance portal</li>
    </ul>
  </div>

  <div class="phase">
    <div class="phase-header">
      <span class="phase-label">Q3 2026</span>
      <span class="phase-status">Planned</span>
    </div>
    <h3 class="card-title">Ecosystem</h3>
    <ul class="phase-features">
      <li><i class="ph-bold ph-circle"></i>Grants program</li>
      <li><i class="ph-bold ph-circle"></i>Mobile SDK</li>
    </ul>
  </div>
</div>

<style>
.roadmap-h {
  display: grid;
  grid-template-columns: repeat(var(--phase-count, 3), 1fr);
  gap: var(--gap-card);
}
.phase {
  padding: 16px;
  border-radius: var(--radius-card);
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 15%, transparent),
      color-mix(in srgb, var(--accent-1) 30%, transparent)) border-box;
  border: 1px solid transparent;
  display: flex; flex-direction: column; gap: 8px;
}
.phase.shipped { opacity: 0.7; }
.phase.active {
  background:
    linear-gradient(var(--elevated), var(--elevated)) padding-box,
    linear-gradient(135deg, var(--accent-1), var(--accent-2)) border-box;
  box-shadow: 0 0 24px color-mix(in srgb, var(--accent-1) 15%, transparent);
}
.phase-header { display: flex; justify-content: space-between; align-items: baseline; }
.phase-label {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--accent-1);
}
.phase-status {
  font: 400 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--text-muted);
}
.phase-features { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 6px; }
.phase-features li {
  display: flex; align-items: center; gap: 8px;
  font: 400 13px/1.3 'Montserrat', sans-serif;
  color: var(--text-secondary);
}
.phase-features .ph-check-circle { color: var(--positive); }
.phase-features .ph-arrow-right { color: var(--accent-1); }
.phase-features .ph-circle { color: var(--text-muted); }
</style>
```

## Vertical variant

Stack phases vertically using the timeline-v spine pattern, with each `.tv-body` containing a phase card.

## Status semantics

| Status | Icon | Visual |
|---|---|---|
| Shipped | `ph-check-circle` (positive green) | Card at 70% opacity |
| Active | `ph-arrow-right` (accent-1) | Card with glow + strong border |
| Planned | `ph-circle` (text-muted) | Card full opacity, no glow |
| Blocked | `ph-warning` (negative) | Card with negative-tint border |

## Composition rules

- Shipped phases dimmed — past work is context. Active gets the glow.
- Phase labels always have a date, even approximate ("Q3 2026").
- 3-5 features per phase max.
- Status must be honest. Slipped feature → move to later phase or mark blocked.
- 3-5 phases ideal. 6+ feels speculative; chunk into epochs.

## Anti-patterns

- Painting every future phase green (calibration loss).
- Specific dates on far-future work (anything past Q2+3 of current year).
- Using roadmap for retrospective content — that's `timeline`.
