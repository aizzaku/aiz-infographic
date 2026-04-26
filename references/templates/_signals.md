# Signals Template

Sibling infographic that surfaces **derived insight** from the same source data as a main infographic. A signal is a fact the viewer would miss by reading the presented data alone — hidden math, comparative weight, or second-order consequences. Loaded only when §8.6 Signal Sheet fires.

## When to use

Loaded by §8.6 of `SKILL.md` after the main infographic has shipped and the user opted in. Never used as a primary template — always a sibling to a main piece.

## Canvas

`bento-box` (see `references/canvases/bento-box.md`) — using the `cheatsheet` template in **signals-variant mode** (see `references/templates/cheatsheet.md` §Signals variant). Grouped 3×3 grid, fixed card schema — no bento mixed-span here, signals demand uniformity for honest comparison.

## Default style

Inherit from the main infographic. Reuse the exact `--accent-1`, `--accent-2`, fonts, width, viewer-feature flags, creator-tools inclusion. **Never re-ask** §5 questions.

## Required elements

- `text.md` — atoms
- `layout.md` — canvas, grouped grid recipe
- `decorative.md` — gradient borders for cards, hairline group dividers
- `data-widgets.md` — for inline math display
- `annotation.md` — source citation labels (small uppercase chip beneath each card)

## Signal lenses

Exactly three lenses. Only emit groups with ≥1 surviving signal.

| Lens | What it surfaces | Card body shape |
|---|---|---|
| **Derived** | Hidden ratios, %s, dilution, runway, implied valuations not stated in source | Math expression, e.g. `40M / 200M = 20%` |
| **Comparative** | How a value sits vs. peers / benchmarks (only when peer data is supplied or web-searched) | `<this value> vs <peer median> (source: <domain>)` |
| **Causal** | Downstream consequence a non-expert wouldn't trace | Short chain: `A → B → C` |

## Two-pass extraction

### Pass 1 — Draft

Read source data + main infographic. Draft up to ~15 candidate signals. For each candidate produce:

```
{
  lens: derived | comparative | causal
  headline: plain-English claim, ≤10 words, verb-first
  evidence: math expression | comparison statement | causal chain
  source: data point reference (e.g., "ALLOCATION TABLE → TEAM ROW") or external domain
  confidence: high | medium | low
}
```

### Pass 2 — Cold critique

Re-read each candidate cold against source data only. Reject if any of:

- Cited source data doesn't actually support the claim
- Math doesn't reconcile when re-computed from scratch
- Causal chain requires assumptions not present in source data
- Confidence drops below `high` on re-evaluation

Surviving candidates are sorted by impact (causal weight, magnitude of derived value, divergence from comparative norm) and capped at **9 total**, **max 3 per lens**.

### Thin-data fallback

If <3 high-confidence signals survive Pass 2, do not write the file. Print:

```
Signal sheet: skipped — not enough derivable signals from the provided data.
```

§13 Closing Tip still prints last.

## Card schema (fixed)

Every card has exactly three slots. No icons, no chips, no decoration beyond the gradient border.

```html
<div class="signal-card">
  <h3 class="signal-headline gradient-text">{HEADLINE, UPPERCASE}</h3>
  <div class="signal-evidence">{math | comparison | causal chain}</div>
  <div class="signal-source">SRC: {source reference}</div>
</div>
```

```css
.signal-card {
  padding: 16px 20px;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 24%, transparent),
      color-mix(in srgb, var(--accent-2) 32%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
  display: flex; flex-direction: column; gap: 8px;
  min-height: 144px;
}
.signal-headline {
  font: 700 16px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin: 0;
}
.signal-evidence {
  font: 600 14px/1.3 'Montserrat', sans-serif;
  color: var(--text-primary);
  font-variant-numeric: tabular-nums;
}
.signal-source {
  font: 600 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  margin-top: auto;
}
```

## Page structure

```html
<div class="infographic-canvas">

  <header class="signals-hero">
    <span class="eyebrow">{MAIN TITLE}</span>
    <h1 class="hero-title gradient-text">{Main Title} — Signals</h1>
    <p class="hero-sub">Derived insights from the underlying data.</p>
  </header>

  <section class="signal-group" data-lens="derived">
    <h2 class="group-label">DERIVED</h2>
    <div class="signal-row"><!-- 1–3 .signal-card --></div>
  </section>

  <section class="signal-group" data-lens="comparative">
    <h2 class="group-label">COMPARATIVE</h2>
    <div class="signal-row"><!-- 1–3 .signal-card --></div>
  </section>

  <section class="signal-group" data-lens="causal">
    <h2 class="group-label">CAUSAL</h2>
    <div class="signal-row"><!-- 1–3 .signal-card --></div>
  </section>

</div>
```

```css
.signal-group { margin-top: 32px; }
.group-label {
  font: 700 12px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--text-muted);
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid color-mix(in srgb, var(--text-muted) 30%, transparent);
}
.signal-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
```

Empty groups are not rendered. A sheet with only Derived + Causal renders two rows. The grid stays 3-column to keep card width consistent across groups; a row with 1 signal places that card in column 1 and leaves the rest empty (do not stretch).

## Composition rules

- Confidence is **never displayed**. It only filters at extraction.
- Every card must show its evidence inline. Numbers without their math are forbidden.
- Every card must cite a source. `SRC: <reference>` for in-data; `SRC: <domain>` for web-searched comparative.
- Headlines are verb-first or noun-first declarative — never questions, never speculation ("might", "could", "perhaps").
- No emoji. No icons on cards. The cards are about the claim, not the chrome.
- All §6 Generation Rules apply unchanged (4px grid, two-font, gradient text only on headers, etc.).

## Comparative sourcing

Three modes, picked by §8.6 step 2:

1. **User-provided** — user pastes peer data after the question. Cite as `SRC: USER-PROVIDED PEERS`.
2. **Web search** — Claude runs targeted searches for benchmark medians/norms relevant to the data points. Each comparative card cites the source domain. Skip cards where search yielded nothing reliable.
3. **Skip** — emit only Derived + Causal groups. Comparative group is not rendered.

## Output paths

| Step | Path |
|---|---|
| Standalone signal sheet | `./output/<kebab-name>-signals.html` + `.png` |
| Merged variant (when user merges) | `./output/<kebab-name>-merged.html` + `.png` |

Original `<kebab-name>.html` is never overwritten unless the user explicitly chooses "Replace main" after the merge variant is shown.

## Merge behavior

When the user signals merge (`merge signals`, `merge them`, `merge if accurate`):

1. Read the live `<kebab-name>.html` and the signals from `<kebab-name>-signals.html`.
2. Append a new `<section class="signals-section">` to the canvas as the final section. Inside, render the same grouped 3-column structure as the standalone sheet.
3. Write to `<kebab-name>-merged.html`. Do not modify `<kebab-name>.html`.
4. Export `<kebab-name>-merged.png`.
5. Print recap, then fire `AskUserQuestion` for `Replace main` / `Keep both`. On `Replace main`, copy merged HTML+PNG over the originals.

## Agent context behavior

Per §11:
- Auto-generate signal sheet (no opt-in possible).
- Skip comparative sourcing entirely (no user prompt, no web search latency).
- Never offer merge — ship `<name>-signals.html`+`.png` alongside `<name>.html`+`.png`.
- Thin-data fallback: skip silently.

## Anti-patterns

- Don't fabricate peer benchmarks. If no source, drop the comparative card.
- Don't restate facts already on the main infographic verbatim — that's not a signal.
- Don't show confidence tiers in the rendered output.
- Don't mix lenses inside a single card. One lens per card.
- Don't pad to fill a 3-card row. A row of 1 card is honest; a row padded with filler is not.
- Don't summarize the main infographic in the hero. The eyebrow + title is enough — readers already saw the parent.
