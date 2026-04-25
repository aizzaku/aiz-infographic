# Process Flow Layout

Sequential steps with connectors. For how-it-works explainers, crypto mechanisms, user journeys, multi-stage processes.

## When to use

- "How does X work" explainers
- Token lifecycles (mint → stake → claim)
- User journeys (onboard → use → reward)
- Multi-step protocols (3–8 ordered steps)

## Required elements

`connectors.md` (step connector, timeline spine, arrows), `text.md`, `layout.md`, `decorative.md`, `icons.md`, optionally `data-widgets.md` for per-step stats.

## Orientation

| Steps | Portrait | Landscape |
|-------|----------|-----------|
| 3 | Horizontal row | Horizontal row |
| 4–5 | Vertical stack | Horizontal row |
| 6–8 | Vertical stack | Vertical stack (2 columns) |

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │  title + short summary
├──────────────────────────────┤
│ Optional context             │  key terms / definitions
├──────────────────────────────┤
│ Step 1 ──► Step 2 ──► Step 3 │  or vertical stack
├──────────────────────────────┤
│ Outcome / summary            │  optional
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## Horizontal variant (3 steps)

```html
<div class="flow-h">
  <div class="step-h">
    <div class="step-num">01</div>
    <h3 class="card-title">Stake</h3>
    <p class="body">Deposit tokens into the contract.</p>
  </div>
  <div class="arrow-h" aria-hidden="true"></div>
  <div class="step-h">
    <div class="step-num">02</div>
    <h3 class="card-title">Earn</h3>
    <p class="body">Accrue rewards over the vesting window.</p>
  </div>
  <div class="arrow-h" aria-hidden="true"></div>
  <div class="step-h">
    <div class="step-num">03</div>
    <h3 class="card-title">Claim</h3>
    <p class="body">Withdraw accrued rewards any time.</p>
  </div>
</div>

<style>
.flow-h {
  display: grid;
  grid-template-columns: 1fr auto 1fr auto 1fr;
  align-items: start;
  gap: 16px;
}
.step-h {
  padding: 16px;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 20%, transparent),
      color-mix(in srgb, var(--accent-1) 40%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
  display: flex; flex-direction: column; gap: 8px;
}
</style>
```

## Vertical variant (4+ steps)

Use `.step` + `.step-connector` pattern from `connectors.md`. Nested as:

```html
<div class="flow-v">
  <div class="step">
    <div class="step-num">01</div>
    <div class="step-body">
      <h3 class="card-title">Stake</h3>
      <p class="body">…</p>
    </div>
  </div>
  <div class="step-connector"></div>
  <div class="step">…</div>
  <!-- repeat -->
</div>
```

## Adaptation rules

| Steps | Layout |
|-------|--------|
| 3 | Horizontal (portrait or landscape) |
| 4 | Vertical portrait, horizontal landscape |
| 5 | Vertical |
| 6–7 | Vertical, possibly 2 groups |
| 8+ | Split into two phases, each a separate flow |

## Optional: per-step metric

For processes where each step has a quantifiable outcome, add a metric beside the step body:

```html
<div class="step">
  <div class="step-num">01</div>
  <div class="step-body">
    <h3 class="card-title">Stake</h3>
    <p class="body">Deposit tokens into the contract.</p>
  </div>
  <div class="step-stat">
    <span class="metric-value">15%</span>
    <span class="metric-label">APR</span>
  </div>
</div>
```

Adjust grid: `grid-template-columns: 48px 1fr auto;`

## Composition rules

- Steps are sequential. Never branch into parallel paths in this layout — use `flowchart` (phase 2) for branches.
- Step numbers use the display font in the numbered circle.
- Connectors lead the eye in reading direction (left→right or top→bottom).
- No more than 8 steps in a single flow. Past that, readers lose the sequence.
- If the outcome matters, add an "Outcome" callout card after the last step. Otherwise, end with the footer.

## Anti-patterns

- Don't skip step numbers. Always 01, 02, 03 — never just card titles with no ordering cue.
- Don't make connectors decorative. An arrow with no actual relationship between boxes is noise.
- Don't put more than one sentence of body copy per step. If more is needed, restructure into fewer richer steps OR move detail to a reference card below.
