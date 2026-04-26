# Journey Path Snippet

User journey with stages along a winding path. Narrative experience — not a process, not a timeline. The "experience" of moving through X.

## When to use

- User onboarding journey (landing → signup → first-use → habit)
- Customer lifecycle (discovery → consideration → adoption → advocacy)
- Quest progression
- Narrative walkthrough with emotional/metric arc

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| poster | centerpiece | Best — winding path needs space |
| bento-box | card-wide (`1/-1`) | Horizontal journey across the bottom |
| editorial | body-column | Inline figure |

## Required elements

`connectors.md` (curved arrows or winding path), `text.md`, `layout.md`, `decorative.md`, `icons.md`, `data-widgets.md`.

## HTML pattern

```html
<div class="journey">
  <div class="journey-path">
    <svg viewBox="0 0 1000 200" preserveAspectRatio="none">
      <path d="M 50 100 Q 200 40, 350 100 T 650 100 T 950 100"
            stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)"
            stroke-width="2" fill="none"
            stroke-dasharray="6 4"/>
    </svg>
    <div class="journey-stages">
      <div class="jstage"><div class="jstage-dot"></div><div class="jstage-label">Discover</div></div>
      <div class="jstage"><div class="jstage-dot"></div><div class="jstage-label">Sign up</div></div>
      <div class="jstage"><div class="jstage-dot"></div><div class="jstage-label">First use</div></div>
      <div class="jstage"><div class="jstage-dot"></div><div class="jstage-label">Habit</div></div>
    </div>
  </div>

  <div class="journey-details">
    <div class="jdetail">
      <i class="ph-bold ph-magnifying-glass"></i>
      <div class="jdetail-title">Discover</div>
      <p class="body">Sees a tweet, visits the landing page, reads the pitch.</p>
    </div>
    <!-- repeat per stage -->
  </div>
</div>

<style>
.journey { display: flex; flex-direction: column; gap: 24px; }
.journey-path { position: relative; height: 140px; }
.journey-path svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.journey-stages {
  position: relative;
  display: grid;
  grid-template-columns: repeat(var(--stage-count, 4), 1fr);
  align-items: center; height: 100%;
}
.jstage { display: flex; flex-direction: column; align-items: center; gap: 6px; }
.jstage-dot {
  width: 16px; height: 16px;
  border-radius: 50%;
  background: var(--accent-1);
  box-shadow: 0 0 16px color-mix(in srgb, var(--accent-1) 50%, transparent);
}
.jstage-label {
  font: 700 13px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--text-primary);
}
.journey-details {
  display: grid;
  grid-template-columns: repeat(var(--stage-count, 4), 1fr);
  gap: var(--gap-card);
}
.jdetail {
  padding: 14px;
  background: var(--panel);
  border-radius: var(--radius-card);
  border: 1px solid color-mix(in srgb, var(--accent-1) 20%, transparent);
  display: flex; flex-direction: column; gap: 6px;
}
.jdetail i { color: var(--accent-1); font-size: 24px; }
.jdetail-title {
  font: 700 14px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.05em;
}
</style>
```

## Stage count and direction

- 3-5 stages standard.
- Horizontal winding path for landscape slots.
- Vertical snake path for portrait (s-curve between stages).
- 6+ stages → split into phases with sub-journeys.

## Composition rules

- Each stage has the same fields (title, icon, one-line description, optional metric).
- Path is visual connective tissue — shows flow direction.
- Icons match the action (discover = magnifying glass, sign up = key, first use = lightning, habit = repeat).
- Path can dip and rise to show emotional arc.
- Curves imply experience; straight lines imply machinery.

## Anti-patterns

- Branches → use `flowchart`.
- Pure chronology → use `timeline` or `roadmap`.
- Disproportionate detail at one stage — journey is about the whole flow.
- Straight lines for the path.
