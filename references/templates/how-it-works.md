# How It Works Template

Mechanism walkthrough — closer cousin of `crypto-explainer` but more general. Works for non-crypto too (game systems, product features, service flows).

## When to use

User mentions: how does X work, walkthrough, breakdown of X, explain the mechanism, step-by-step guide, behind the scenes — AND wants a visual.

## Canvas

`poster` (see `references/canvases/poster.md`) — process-flow as the centerpiece, supports carry context KPIs and "what's next" callouts.

## Snippets

`process-flow` (centerpiece, the mechanism), `statistical` (header KPIs), `callout-block` (footer "what's next" CTA).

## Default style

`aizfographics-style`

## Required elements

- `connectors.md` — step connectors
- `text.md`, `layout.md`, `decorative.md`, `icons.md`
- Optional `data-widgets.md`, `charts.md`

## Section order

1. **Header strip** — subject logo + "HOW IT WORKS" badge
2. **Hero** — "How {X} works" gradient title + short pitch
3. **At a glance** — optional 3-bullet TL;DR
4. **Step-by-step flow** — 4–7 numbered steps, vertical layout preferred for readability
5. **Under the hood** — optional callout explaining one hidden/technical detail
6. **Footer** — source, date

## Content expectations

Required:
- The thing being explained
- 4–7 sequential steps that describe it
- Action verb per step ("Deposit", "Route", "Settle")

Recommended:
- One specific example that runs through the flow
- Numbers attached to specific steps (time, amount, probability)

## Step card pattern

```html
<div class="step">
  <div class="step-num">01</div>
  <div class="step-body">
    <h3 class="card-title">Deposit</h3>
    <p class="body">User locks {asset} in the vault contract. The deposit triggers an event picked up by off-chain indexers.</p>
  </div>
  <div class="step-meta">
    <span class="step-time">~5 sec</span>
  </div>
</div>
```

Use `.step` from `references/elements/connectors.md`, extending with an optional `.step-meta` right column:

```css
.step {
  grid-template-columns: 48px 1fr auto;
}
.step-meta {
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  align-self: start;
  padding-top: 4px;
}
.step-time { color: var(--accent-1); }
```

## "Under the hood" callout

```html
<section class="section under-hood">
  <h2 class="section-title">Under the hood</h2>
  <div class="hood-card">
    <i class="ph-bold ph-gear"></i>
    <div>
      <h3 class="card-title">Why the two-phase commit?</h3>
      <p class="body">Separating the intent from the execution lets us batch orders and reduce gas per transaction by ~40%.</p>
    </div>
  </div>
</section>

<style>
.hood-card {
  padding: 16px;
  background: var(--elevated);
  border-radius: var(--radius-card);
  border: 1px solid color-mix(in srgb, var(--accent-2) 35%, transparent);
  display: grid;
  grid-template-columns: 40px 1fr;
  gap: 16px;
  align-items: start;
}
.hood-card i {
  color: var(--accent-2);
  font-size: 28px;
  margin-top: 2px;
}
</style>
```

## Content rules

- **Verbs, not nouns, for step titles.** "Deposit" beats "Deposit phase".
- **One idea per step.** If a step needs 3 sentences of body, it's actually 2–3 steps.
- **Technical terms explained on first mention** — "MEV (maximal extractable value)", "RPC (remote procedure call)".
- **Max 7 steps.** 8+ feels like instructions, not explanation; switch to a `list` layout.

## Accent pair selection

Default: pair #1 (amber) for finance mechanisms.
Override to pair #6 (green → cyan) for technical/protocol flows.
Override to pair #3 (lime → gold) for yield/farming flows.

## Dimension guidance

Portrait-medium (1080 × 1440) for 4–5 step flows. Portrait-tall (1080 × 1920) when adding "under the hood" and examples.
