# Step Connector Snippet

Numbered linear sequence with visual emphasis on the connections between steps. Used for onboarding flows, protocol phases, and process sequences where the path between steps matters as much as the steps themselves.

Different from `process-flow`: process-flow uses icons and may branch. Step-connector uses number badges and emphasizes the spine connecting steps. No decision nodes.

## When to use

- Onboarding sequences (Step 1, Step 2, Step 3)
- Protocol phases or epochs (strictly ordered, no branching)
- Setup or installation sequences
- Claim / unlock / milestone flows

Do NOT use when:
- Steps can be skipped or reordered (not a sequence)
- There are decision branches (use `flowchart`)
- Steps have complex internal structure (use `swimlane`)

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| bento-box | card-wide (`1/-1`) | Horizontal strip, all steps in one row |
| bento-box | card-span-3 | Horizontal 3-5 steps |
| editorial | body-column | Vertical layout preferred |
| poster | centerpiece | Horizontal or vertical, max 5 steps |
| dashboard | panel | Vertical compact, 3-4 steps |

## Density cap

3-7 steps. Beyond 7, split into two sequences (Phase 1 / Phase 2).

## Required elements

`connectors.md`, `badges.md`, `text.md`

## HTML pattern — horizontal (default)

```html
<div class="step-connector step-connector-h">
  <div class="step-item">
    <div class="step-badge">1</div>
    <div class="step-content">
      <div class="step-title">Connect Wallet</div>
      <div class="step-body">Link your wallet to the protocol dashboard.</div>
    </div>
  </div>
  <div class="step-line" aria-hidden="true"></div>
  <div class="step-item">
    <div class="step-badge">2</div>
    <div class="step-content">
      <div class="step-title">Stake Tokens</div>
      <div class="step-body">Deposit a minimum of 100 tokens to enter the pool.</div>
    </div>
  </div>
  <div class="step-line" aria-hidden="true"></div>
  <div class="step-item">
    <div class="step-badge">3</div>
    <div class="step-content">
      <div class="step-title">Earn Rewards</div>
      <div class="step-body">Rewards accrue daily and can be claimed at any time.</div>
    </div>
  </div>
</div>

<style>
.step-connector-h {
  display: flex;
  align-items: flex-start;
  gap: 0;
}

.step-connector-h .step-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  flex: 1;
  text-align: center;
}

.step-badge {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--accent-1);
  color: var(--on-accent, #0F1115);
  display: flex;
  align-items: center;
  justify-content: center;
  font: 700 15px/1 'Montserrat', sans-serif;
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}

.step-connector-h .step-line {
  flex: 0 0 auto;
  width: 60px;
  height: 2px;
  background: color-mix(in srgb, var(--accent-1) 40%, transparent);
  margin-top: 17px; /* vertically center on badge */
  position: relative;
}

/* Arrow tip on connector line */
.step-connector-h .step-line::after {
  content: '';
  position: absolute;
  right: -1px;
  top: 50%;
  transform: translateY(-50%);
  border: 5px solid transparent;
  border-left-color: color-mix(in srgb, var(--accent-1) 50%, transparent);
  border-right: none;
}

.step-title {
  font: 700 13px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-primary);
}

.step-body {
  font: 400 12px/1.5 'Montserrat', sans-serif;
  color: var(--text-secondary);
  max-width: 160px;
}
</style>
```

## HTML pattern — vertical

```html
<div class="step-connector step-connector-v">
  <div class="step-v-item">
    <div class="step-v-left">
      <div class="step-badge">1</div>
      <div class="step-v-spine" aria-hidden="true"></div>
    </div>
    <div class="step-content">
      <div class="step-title">Connect Wallet</div>
      <div class="step-body">Link your wallet to the protocol dashboard.</div>
    </div>
  </div>
  <div class="step-v-item">
    <div class="step-v-left">
      <div class="step-badge">2</div>
      <div class="step-v-spine" aria-hidden="true"></div>
    </div>
    <div class="step-content">
      <div class="step-title">Stake Tokens</div>
      <div class="step-body">Deposit a minimum of 100 tokens to enter the pool.</div>
    </div>
  </div>
  <div class="step-v-item step-v-last">
    <div class="step-v-left">
      <div class="step-badge">3</div>
      <!-- no spine on last item -->
    </div>
    <div class="step-content">
      <div class="step-title">Earn Rewards</div>
      <div class="step-body">Rewards accrue daily and can be claimed at any time.</div>
    </div>
  </div>
</div>

<style>
.step-connector-v { display: flex; flex-direction: column; }

.step-v-item {
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.step-v-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-shrink: 0;
}

.step-v-spine {
  width: 2px;
  flex: 1;
  min-height: 28px;
  background: color-mix(in srgb, var(--accent-1) 40%, transparent);
  margin-top: 4px;
}

.step-connector-v .step-content {
  padding-bottom: 24px;
}

.step-v-last .step-content { padding-bottom: 0; }
</style>
```

## Theme: terminal / forge / ash (square badges)

Replace circle badge with hard square. Monospace text throughout.

```css
/* Terminal/Forge/Ash square badge override */
.step-badge {
  border-radius: 0;        /* hard square */
  background: var(--accent-1);
  font-family: monospace;
  font-size: 14px;
}

/* Terminal: green badge */
.terminal-theme .step-badge { background: #3FB950; color: #0D1117; }
/* Forge: ember badge */
.forge-theme .step-badge { background: #E07B20; color: #0F0A04; }
/* Ash: gray badge */
.ash-theme .step-badge { background: #D0D0D0; color: #0E0E0E; }

/* Terminal connector line */
.terminal-theme .step-v-spine,
.terminal-theme .step-connector-h .step-line {
  background: #30363D;
}

/* Remove arrow tip in terminal (no rounded decoration) */
.terminal-theme .step-connector-h .step-line::after { display: none; }
```

## Active / completed step states

When the sequence shows progress (some steps done, one current):

```html
<div class="step-badge step-done">1</div>   <!-- completed -->
<div class="step-badge step-active">2</div> <!-- current step -->
<div class="step-badge step-pending">3</div> <!-- not yet -->

<style>
.step-done {
  background: color-mix(in srgb, var(--accent-1) 20%, transparent);
  border: 1px solid color-mix(in srgb, var(--accent-1) 40%, transparent);
  color: var(--accent-1);
}
.step-active {
  background: var(--accent-1);
  color: var(--on-accent, #0F1115);
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent-1) 20%, transparent);
}
.step-pending {
  background: color-mix(in srgb, var(--text-muted) 15%, transparent);
  border: 1px solid color-mix(in srgb, var(--text-muted) 30%, transparent);
  color: var(--text-muted);
}
</style>
```

## Composition rules

- Number badges always show ordinal numbers (1, 2, 3) — never icons, letters, or bullets.
- One connector line between each consecutive pair of steps. Connector thickness: 2px.
- In horizontal layout, badge centers vertically align with the connector line.
- In vertical layout, the spine starts at the badge bottom and ends at the next badge top.
- No decision diamond, no branch — if the sequence branches, switch to `flowchart`.

## Anti-patterns

- Icons replacing numbers — defeats the sequential numbered purpose
- More than 7 steps in one connector sequence
- Decision branches or conditional paths — use `flowchart`
- Connector lines thicker than 2px — dominates over badge hierarchy
- Horizontal layout with more than 5 steps — labels become too narrow; switch to vertical
