# Mind Map Snippet

Central concept with radial branches. Branches are peers (not parent/child — that's `hierarchical`). Non-hierarchical relational map.

## When to use

- Brainstorm of related ideas
- Protocol feature map (central token → related features)
- Community / ecosystem circles
- "Everything connected to X" overviews

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| poster | centerpiece | Best — radial demands square space |
| bento-box | card-tall (square cell) | Compact mind map (4-6 branches) |
| editorial | body-column | Inline radial figure |

## Required elements

`connectors.md` (curved arrows), `text.md`, `layout.md`, `decorative.md`, `icons.md`.

## HTML pattern (CSS grid + SVG overlay)

```html
<div class="mindmap">
  <svg class="mindmap-wires" viewBox="0 0 800 600" preserveAspectRatio="xMidYMid meet">
    <path d="M 400 300 Q 300 200, 200 150"
          stroke="color-mix(in srgb, var(--accent-1) 50%, transparent)"
          stroke-width="2" fill="none"/>
    <!-- one curved path per branch, center to branch position -->
  </svg>

  <div class="mindmap-nodes">
    <div class="mm-center"><div class="mm-center-title">Governance</div></div>
    <div class="mm-branch" style="--x: 10%; --y: 25%;">
      <i class="ph-bold ph-users-three"></i><div>Voting</div>
    </div>
    <div class="mm-branch" style="--x: 85%; --y: 25%;">…</div>
    <div class="mm-branch" style="--x: 85%; --y: 75%;">…</div>
    <div class="mm-branch" style="--x: 10%; --y: 75%;">…</div>
  </div>
</div>

<style>
.mindmap { position: relative; aspect-ratio: 4 / 3; }
.mindmap-wires { position: absolute; inset: 0; z-index: 0; pointer-events: none; }
.mindmap-nodes { position: relative; z-index: 1; width: 100%; height: 100%; }

.mm-center {
  position: absolute; left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  width: 160px; height: 160px;
  border-radius: 50%;
  background:
    linear-gradient(var(--elevated), var(--elevated)) padding-box,
    linear-gradient(135deg, var(--accent-1), var(--accent-2)) border-box;
  border: 2px solid transparent;
  display: flex; align-items: center; justify-content: center;
  text-align: center;
  box-shadow: 0 0 32px color-mix(in srgb, var(--accent-1) 24%, transparent);
}
.mm-center-title {
  font: 700 18px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--accent-1);
}
.mm-branch {
  position: absolute;
  left: var(--x); top: var(--y);
  transform: translate(-50%, -50%);
  padding: 10px 16px;
  border-radius: 999px;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 30%, transparent),
      color-mix(in srgb, var(--accent-1) 50%, transparent)) border-box;
  border: 1px solid transparent;
  display: flex; align-items: center; gap: 8px;
  font: 700 13px/1 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.04em;
  white-space: nowrap;
}
.mm-branch i { color: var(--accent-1); }
</style>
```

## Branch count

- 4-8 branches ideal. 8+ → branches collide.
- Distribute evenly around the circle (12, 2, 4, 6, 8, 10 o'clock for 6).
- Each branch can have 0-3 sub-branches.

## Composition rules

- Center node visually dominant: strong border, glow, larger size, pair-gradient bg.
- Branches equal to each other. No weighted siblings in a mind map.
- Short labels: 1-3 words for branches, 1-4 for sub-branches.
- Curved connectors feel organic.
- Square aspect ideal.

## Anti-patterns

- Use for hierarchies → use `hierarchical`.
- Use for sequences → use `process-flow` or `circular-flow`.
- Fewer than 4 branches → it's a hub-and-spoke, not a mind map.
- Center and branches same size → center must dominate.
