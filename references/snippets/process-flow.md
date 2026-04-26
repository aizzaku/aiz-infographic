# Process Flow Snippet

Sequential numbered steps with connectors. For mechanism explainers, user journeys, multi-stage protocols.

## When to use

- "How does X work" mechanism breakdowns (3-8 ordered steps)
- Token lifecycles (mint → stake → claim)
- User journeys (onboard → use → reward)

## Slot fit

| Canvas | Slot | Orientation | Notes |
|---|---|---|---|
| bento-box | card-wide (`1/-1`) | horizontal | 3 steps fit |
| bento-box | card-tall | vertical | 4-7 steps stacked |
| editorial | body-column | vertical | 4-6 step inline figure |
| dashboard | panel-large (w-12) | horizontal | Process across the panel |
| poster | centerpiece | horizontal or vertical | The mechanism is the hero |

## Required elements

`connectors.md` (step-connector, arrows), `text.md`, `layout.md`, `decorative.md`, `icons.md`. Optional `data-widgets.md` for per-step metrics.

## Horizontal pattern (3 steps)

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
.step-num {
  font: 400 32px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
}
.arrow-h {
  align-self: center;
  width: 32px; height: 2px;
  background: color-mix(in srgb, var(--accent-1) 60%, transparent);
  position: relative;
}
.arrow-h::after {
  content: '';
  position: absolute; right: -2px; top: -4px;
  border: 5px solid transparent;
  border-left-color: color-mix(in srgb, var(--accent-1) 60%, transparent);
}
</style>
```

## Vertical pattern (4+ steps)

```html
<div class="flow-v">
  <div class="step">
    <div class="step-num">01</div>
    <div class="step-body">
      <h3 class="card-title">Stake</h3>
      <p class="body">Deposit tokens into the contract.</p>
    </div>
  </div>
  <div class="step-connector"></div>
  <div class="step">…</div>
  <!-- repeat -->
</div>

<style>
.flow-v { display: flex; flex-direction: column; gap: 0; }
.step {
  display: grid;
  grid-template-columns: 48px 1fr;
  gap: 14px;
  padding: 12px 0;
}
.step-connector {
  margin-left: 23px;
  width: 2px; height: 32px;
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--accent-1) 60%, transparent),
    color-mix(in srgb, var(--accent-1) 30%, transparent));
}
</style>
```

## Optional per-step metric

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

- Sequential only — never branch into parallel paths in this snippet (use `flowchart` for branches).
- Step numbers always present (`01, 02, 03`). Never just titles without ordering.
- Connectors lead the eye in reading direction.
- Max 8 steps. Past that, split into two phases (each its own flow).
- One sentence of body per step — restructure if more is needed.

## Anti-patterns

- Skipped step numbers.
- Decorative arrows without semantic meaning.
- Multi-paragraph body inside a step.
