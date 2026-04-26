# Game Mechanics Template

Deep-dive on a specific game system — not the whole game (that's `game-overview`), but one mechanic explained in detail. Stats, formulas, and interaction rules.

## When to use

User mentions: game mechanic, mechanic breakdown, damage formula, staking mechanic, combat system, level-up system, how {specific feature} works in the game.

## Canvas

`bento-box` (see `references/canvases/bento-box.md`) — hero with key stats, then mixed-span cards for the interaction flow, formula breakdown, and values lookup.

## Snippets

`statistical` (hero KPI strip), `process-flow` (interaction sequence), `comparison` (values lookup table), `formula-block` (when a damage/yield formula is involved).

## Default style

`aizfographics-style` or `retro` for pixel-art games.

## Required elements

- `text.md`, `layout.md`, `decorative.md`, `icons.md`
- `data-widgets.md` — KPI strip for key numbers
- `charts.md` — optional scaling curves
- `connectors.md` — interaction sequence arrows
- `comparison.md` — value lookup tables

## Section order

1. **Header strip** — game logo + "GAME MECHANICS" badge + mechanic name
2. **Hero** — mechanic name + one-line role in the game
3. **Core numbers** — KPI strip (base values, caps, cooldowns)
4. **Formula / calculation** — if the mechanic has a formula, show it with variables labeled
5. **Interaction flow** — 3–5 step process showing how the mechanic plays out in a turn/match
6. **Value lookup table** — scaling values by level/tier/rank
7. **Edge cases** — 2–3 callouts for counter-intuitive interactions
8. **Footer** — patch version, balance notes date

## Content expectations

Required:
- Mechanic name
- Core numeric parameters (values, caps)
- Basic interaction description

Strongly recommended:
- Formula if one exists
- Scaling table by tier/level
- Game version / patch number

## Formula block pattern

```html
<section class="section formula">
  <h2 class="section-title">Damage formula</h2>
  <div class="formula-box">
    <div class="formula-expression">
      <span class="var">ATK</span>
      <span class="op">×</span>
      <span class="paren">(</span>
      <span class="literal">1</span>
      <span class="op">+</span>
      <span class="var">CRIT%</span>
      <span class="op">×</span>
      <span class="var">CRIT_MULT</span>
      <span class="paren">)</span>
      <span class="op">÷</span>
      <span class="var">DEF</span>
    </div>
    <ul class="formula-legend">
      <li><span class="var">ATK</span> attack stat of the attacker</li>
      <li><span class="var">CRIT%</span> chance of a critical hit (0–1)</li>
      <li><span class="var">CRIT_MULT</span> critical hit multiplier (default 2×)</li>
      <li><span class="var">DEF</span> defense stat of the target</li>
    </ul>
  </div>
</section>

<style>
.formula-box {
  padding: 24px;
  background: var(--elevated);
  border: 1px solid color-mix(in srgb, var(--accent-1) 35%, transparent);
  border-radius: var(--radius-card);
}
.formula-expression {
  font: 400 28px/1.2 'JetBrains Mono', monospace;
  text-align: center;
  color: var(--text-primary);
  margin-bottom: 16px;
  font-variant-numeric: tabular-nums;
  display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;
}
.formula-expression .var {
  color: var(--accent-1);
  font-weight: 700;
}
.formula-expression .literal {
  color: var(--accent-2);
}
.formula-expression .op,
.formula-expression .paren {
  color: var(--text-secondary);
}
.formula-legend {
  list-style: none; padding: 0; margin: 0;
  display: flex; flex-direction: column; gap: 4px;
  font: 400 12px/1.4 'Montserrat', sans-serif;
  color: var(--text-secondary);
}
.formula-legend .var {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  color: var(--accent-1);
  margin-right: 8px;
}
</style>
```

## Scaling table pattern

Use `.feature-table` from comparison element with a level column and stat columns.

## Content rules

- **Number the steps of interactions.** Each step is a discrete tick/turn.
- **Formula variables consistent case** across formula, legend, table.
- **Edge cases labeled warning-yellow**, not red. They're surprises, not errors.
- **Patch version required.** Mechanics change. A mechanics infographic without version is stale by next patch.

## Accent pair selection

Default: pair #3 (lime → gold) — energetic gaming feel.
Override to pair #4 (red → pink) for combat-focused mechanics.
Override to pair #2 (gold → orange) for economy-focused mechanics (farming, trading).

## Dimension guidance

Portrait-tall (1080 × 1920) usually — formulas + tables + flow all stack vertically. Landscape works for simple mechanics without a formula.

## Anti-patterns

- Don't show a formula without variable legend.
- Don't publish without patch version / date.
- Don't mix multiple mechanics — one infographic, one mechanic.
