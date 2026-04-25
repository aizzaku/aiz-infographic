# Mind Map Layout

Central concept with radial branches. Each branch is a related idea; each idea can have its own sub-branches. Non-hierarchical (unlike `hierarchical.md`) — branches are peers, not parent/child.

## When to use

- Brainstorm of related ideas
- Protocol feature map (central token → related features)
- Community / ecosystem circles
- Research topic breakdown
- "Everything connected to X" overviews

## Required elements

`connectors.md` (curved arrows), `text.md`, `layout.md`, `decorative.md`, `icons.md`.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│           [ B1 ]              │
│              \                │
│      [ B6 ] — [CENTER] — [B2] │
│              /     \           │
│           [ B5 ]   [ B3 ]      │
│                  [ B4 ]        │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## HTML pattern (CSS grid + SVG overlay)

```html
<div class="mindmap">
  <svg class="mindmap-wires" viewBox="0 0 800 600" preserveAspectRatio="xMidYMid meet">
    <!-- curved paths from center to each branch -->
    <path d="M 400 300 Q 300 200, 200 150"
          stroke="color-mix(in srgb, var(--accent-1) 50%, transparent)"
          stroke-width="2" fill="none"/>
    <!-- more paths -->
  </svg>

  <div class="mindmap-nodes">
    <div class="mm-center">
      <div class="mm-center-title">Governance</div>
    </div>

    <div class="mm-branch" style="--x: 10%; --y: 25%;">
      <i class="ph-bold ph-users-three"></i>
      <div>Voting</div>
    </div>
    <div class="mm-branch" style="--x: 85%; --y: 25%;">…</div>
    <div class="mm-branch" style="--x: 85%; --y: 75%;">…</div>
    <div class="mm-branch" style="--x: 10%; --y: 75%;">…</div>
    <!-- etc -->
  </div>
</div>

<style>
.mindmap { position: relative; aspect-ratio: 4 / 3; }
.mindmap-wires { position: absolute; inset: 0; z-index: 0; pointer-events: none; }
.mindmap-nodes { position: relative; z-index: 1; width: 100%; height: 100%; }

.mm-center {
  position: absolute;
  left: 50%; top: 50%;
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
  text-transform: uppercase;
  letter-spacing: 0.06em;
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
  text-transform: uppercase;
  letter-spacing: 0.04em;
  white-space: nowrap;
}
.mm-branch i { color: var(--accent-1); }
</style>
```

## Branch count and placement

- 4–8 branches ideal. Beyond 8, branches collide.
- Distribute evenly around the circle. Think of a clock: 12, 2, 4, 6, 8, 10 o'clock for 6 branches.
- Each branch can have 0–3 sub-branches; more becomes a mini-hierarchy and belongs in a different layout.

## Composition rules

- **Center node is visually dominant.** Strong border, glow, larger size, pair-gradient background.
- **Branches are equal to each other.** No weighted siblings in a mind map.
- **Short labels only.** Branches are 1–3 words. Sub-branches are 1–4 words.
- **Curved connectors** feel more organic than straight lines — mind maps have a "handmade" vibe.
- **Category tint optional.** You can color-code branch groups ("core features" vs "future features") but it's optional.

## Dimension guidance

- Square canvas (1080 × 1080) is ideal — radial shapes work best in square formats.
- Landscape works but center shifts.
- Portrait is awkward for radial layouts — use `hierarchical` or `grid-cards` instead.

## Anti-patterns

- Don't use a mind map when the relationship is truly hierarchical (parent → child). Use `hierarchical.md`.
- Don't use for processes. Mind maps show connections, not sequences.
- Avoid mind maps with fewer than 4 branches — it's just a hub with spokes.
- Don't label center and branches the same size. The center dominates.
