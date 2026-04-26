# Flowchart Snippet

Branching decision paths or state machines. Unlike `process-flow` (strict sequence), flowchart supports branches, loops, conditionals.

## When to use

- Decision tree ("should I stake? → if X then Y else Z")
- State machine (idle → active → locked → claimable)
- Conditional protocol logic
- Routing logic (request → router → A or B or C)

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| poster | centerpiece | Best fit — flowcharts demand space for branches |
| bento-box | card-wide (`1/-1`) | Compact 5-8 node flowchart |
| editorial | body-column | Inline 3-5 node decision figure |

## Required elements

`connectors.md` (straight + curved arrows), `text.md`, `layout.md`, `decorative.md`, `icons.md`.

## Node types

| Shape | Meaning | Class |
|---|---|---|
| Rounded rect | Process step | `.fc-step` |
| Diamond | Decision | `.fc-decision` |
| Rounded pill | Start / end | `.fc-terminal` |
| Rectangle with side bars | Input / output data | `.fc-io` |

## HTML pattern (SVG-overlay on grid)

Flowcharts use CSS Grid for node placement + SVG overlay for connectors. Pixel-locked when arrow geometry must align to cell edges (see SKILL.md §6 pixel-lock rule).

```html
<div class="flowchart">
  <svg class="flowchart-wires" viewBox="0 0 800 600" preserveAspectRatio="none" width="800" height="600">
    <defs>
      <marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
        <path d="M0,0 L8,4 L0,8 z" fill="color-mix(in srgb, var(--accent-1) 60%, transparent)"/>
      </marker>
    </defs>
    <path d="M 400 60 V 110" stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)"
          stroke-width="2" fill="none" marker-end="url(#arrow)"/>
    <!-- more paths matching cell-edge coordinates -->
  </svg>

  <div class="flowchart-nodes">
    <div class="fc-terminal" style="grid-area: start;">Start</div>
    <div class="fc-step" style="grid-area: a;">Step A</div>
    <div class="fc-decision" style="grid-area: dec;"><span>Decision?</span></div>
    <div class="fc-step" style="grid-area: b;">Step B</div>
    <div class="fc-step" style="grid-area: c;">Step C</div>
    <div class="fc-terminal" style="grid-area: end;">End</div>
  </div>
</div>

<style>
.flowchart { position: relative; width: 800px; height: 600px; }
.flowchart-wires { position: absolute; inset: 0; z-index: 0; pointer-events: none; }
.flowchart-nodes {
  position: relative; z-index: 1;
  display: grid;
  grid-template-areas:
    ". start ."
    ". a ."
    ". dec ."
    "b . c"
    ". end .";
  grid-template-columns: 1fr 1fr 1fr;
  gap: 32px 24px;
  justify-items: center; align-items: center;
}
.fc-step, .fc-terminal, .fc-decision, .fc-io {
  padding: 12px 18px;
  font: 700 13px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase; letter-spacing: 0.04em;
  color: var(--text-primary);
  text-align: center;
  min-width: 140px;
}
.fc-step {
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--accent-1) 40%, transparent);
  border-radius: var(--radius-card);
}
.fc-terminal {
  background: var(--elevated);
  border: 1px solid color-mix(in srgb, var(--accent-1) 60%, transparent);
  border-radius: 999px;
  color: var(--accent-1);
}
.fc-decision {
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--accent-2) 50%, transparent);
  transform: rotate(45deg);
  padding: 24px;
  width: 120px; height: 120px;
  display: flex; align-items: center; justify-content: center;
}
.fc-decision > span { transform: rotate(-45deg); }
</style>
```

## Composition rules

- Top-to-bottom or left-to-right. Pick one direction.
- Label every branch — both paths off a decision need labels (Yes/No, Pass/Fail).
- Show merge points with explicit converging arrows.
- 5-12 nodes ideal. Beyond → split into sub-flows.
- Loops use a distinct arrow style (dashed or curved).
- Pixel-lock geometry per SKILL.md §6 — arrow endpoints land on cell edges.

## Anti-patterns

- 15+ nodes in one flowchart — split.
- All nodes the same shape — shape carries semantic meaning.
- Flowchart when the real shape is a tree (use `hierarchical`) or sequence (use `process-flow`).
- "IF"/"THEN" text labels to explain logic — the diamond + branch labels do that work.
