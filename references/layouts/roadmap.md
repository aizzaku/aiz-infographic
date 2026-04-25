# Roadmap Layout

Forward-looking timeline emphasizing future milestones, phases, and deliverables. Unlike `timeline.md` (neutral past-or-future), roadmap is explicitly anticipatory — "here's what we're shipping next".

## When to use

- Project roadmap (Q1/Q2/Q3/Q4 shipping schedule)
- Product release plan
- Season or epoch plan
- Post-launch rollout timeline
- Feature delivery schedule

## Required elements

`connectors.md`, `text.md`, `layout.md`, `decorative.md`, `icons.md`, optionally `data-widgets.md`.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│ Phase 1 ──► Phase 2 ──► Phase 3 │  horizontal OR
│    │         │          │    │
│ features   features  features  │
├──────────────────────────────┤
│ Legend (status key)          │  optional
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## Horizontal phase pattern

```html
<section class="section roadmap-h">
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
  <!-- active phase -->
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
  <!-- future phase -->
  <div class="phase">
    <div class="phase-header">
      <span class="phase-label">Q3 2026</span>
      <span class="phase-status">Planned</span>
    </div>
    <h3 class="card-title">Ecosystem</h3>
    <ul class="phase-features">
      <li><i class="ph-bold ph-circle"></i>Grants program</li>
      <li><i class="ph-bold ph-circle"></i>Mobile SDK</li>
      <li><i class="ph-bold ph-circle"></i>Subnets</li>
    </ul>
  </div>
</section>

<style>
.roadmap-h {
  display: grid;
  grid-template-columns: repeat(var(--phase-count, 3), 1fr);
  gap: var(--gap-card);
  flex-direction: row !important;
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
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.phase.shipped {
  opacity: 0.7;
}
.phase.active {
  background:
    linear-gradient(var(--elevated), var(--elevated)) padding-box,
    linear-gradient(135deg, var(--accent-1), var(--accent-2)) border-box;
  box-shadow: 0 0 24px color-mix(in srgb, var(--accent-1) 15%, transparent);
}
.phase-header { display: flex; justify-content: space-between; align-items: baseline; }
.phase-label {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent-1);
}
.phase-status {
  font: 400 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-muted);
}
.phase-features {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
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

## Vertical phase pattern

Stack phases vertically; use a vertical spine like `timeline.md`'s vertical variant but with phase cards as tv-body content.

## Status semantics

| Status | Icon | Visual |
|--------|------|--------|
| Shipped | `ph-check-circle` (positive green) | Card dimmed at 70% opacity |
| Active / in progress | `ph-arrow-right` (accent-1) | Card with glow, strong border gradient |
| Planned | `ph-circle` (text-muted) | Card at full opacity but no glow |
| Blocked / paused | `ph-warning` (accent-2 or negative) | Card with negative-semantic border tint |

## Composition rules

- **Shipped phases dimmed** — past work is context, not focus. Active gets the glow.
- **Phase labels always have a date**, even if approximate ("Q3 2026", "H2 2026").
- **Feature lists per phase: 3–5 items max.** More becomes unreadable in card-sized space.
- **Status should be honest.** If a feature slipped, either move it to a later phase or mark it blocked. Don't hide it.
- **3–5 phases ideal.** 6+ phases look speculative; chunk into epochs.

## Anti-patterns

- Don't paint every future milestone green. The eye calibrates to meaning.
- Don't put specific dates on unplanned work. "Q4 2027" for anything past Q2+3 of current year is fiction.
- Don't use a roadmap for retrospective content — that's `timeline.md`.
