# Flowchart Layout

Branching decision paths or state machines. Unlike `process-flow.md` (strictly sequential), flowchart supports branches, loops, and conditional paths.

## When to use

- Decision tree ("should I stake? → if X then Y else Z")
- State machine (idle → active → locked → claimable)
- Conditional logic in a protocol ("if balance > threshold, then rebate")
- Routing logic (request → router → A or B or C)

## Required elements

`connectors.md` (straight + curved arrows), `text.md`, `layout.md`, `decorative.md`, `icons.md`.

## Node types

| Shape | Meaning | CSS class |
|-------|---------|-----------|
| Rounded rect | Process step | `.fc-step` |
| Diamond | Decision | `.fc-decision` |
| Rounded pill | Start / end | `.fc-terminal` |
| Rectangle with side bars | Input / output data | `.fc-io` |

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│         [ START ]             │
│            │                  │
│      [ Step A ]               │
│            │                  │
│     ◇ Decision? ◇             │
│       │       │               │
│     YES      NO               │
│     │         │               │
│  [ Step B ] [ Step C ]        │
│     │         │               │
│      └───┬───┘                │
│          │                    │
│      [  END  ]                │
├──────────────────────────────┤
│ Key / legend (optional)       │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## HTML pattern (SVG-based)

Flowcharts are best built as SVG because arbitrary branching/merging requires absolute positioning of paths. Use CSS Grid for node placement, then SVG overlay for connectors.

```html
<div class="flowchart">
  <svg class="flowchart-wires" viewBox="0 0 800 600" preserveAspectRatio="xMidYMid meet">
    <defs>
      <marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
        <path d="M0,0 L8,4 L0,8 z" fill="color-mix(in srgb, var(--accent-1) 60%, transparent)"/>
      </marker>
    </defs>
    <!-- draw paths connecting node centers; coordinates match CSS grid cell centers -->
    <path d="M 400 60 V 110" stroke="color-mix(in srgb, var(--accent-1) 60%, transparent)"
          stroke-width="2" fill="none" marker-end="url(#arrow)"/>
    <!-- more paths -->
  </svg>

  <div class="flowchart-nodes">
    <div class="fc-terminal" style="grid-area: start;">Start</div>
    <div class="fc-step" style="grid-area: a;">Step A</div>
    <div class="fc-decision" style="grid-area: dec;">
      <span>Decision?</span>
    </div>
    <div class="fc-step" style="grid-area: b;">Step B</div>
    <div class="fc-step" style="grid-area: c;">Step C</div>
    <div class="fc-terminal" style="grid-area: end;">End</div>
  </div>
</div>

<style>
.flowchart { position: relative; }
.flowchart-wires { position: absolute; inset: 0; z-index: 0; pointer-events: none; }
.flowchart-nodes {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-areas:
    ". start ."
    ". a ."
    ". dec ."
    "b . c"
    ". end .";
  grid-template-columns: 1fr 1fr 1fr;
  gap: 32px 24px;
  justify-items: center;
  align-items: center;
}
.fc-step, .fc-terminal, .fc-decision, .fc-io {
  padding: 12px 18px;
  font: 700 13px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.04em;
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

- **Top-to-bottom or left-to-right.** Pick one direction, stick with it.
- **Label every branch.** On a decision, both paths need labels ("Yes"/"No", "Pass"/"Fail", "High"/"Low").
- **Merge points matter.** Show where parallel paths rejoin with explicit converging arrows.
- **5–12 nodes ideal.** Beyond that, a flowchart becomes unreadable; break into sub-flows.
- **Loops use a distinct arrow style.** Dashed or curved — so viewers distinguish "loop back" from "continue forward".

## Anti-patterns

- Don't squeeze 15+ nodes into one flowchart. Split.
- Don't make every node the same shape — shape carries semantic meaning.
- Don't use flowchart when the real shape is a tree (use `hierarchical.md`) or a sequence (use `process-flow.md`).
- Don't rely on text "IF"/"THEN" labels to explain logic — the diamond + branch labels should do that work.
