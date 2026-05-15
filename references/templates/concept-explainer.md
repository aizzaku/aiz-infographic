# Concept Explainer Template

"How does X work?" content for any concept, protocol, system, or mechanism. Linear narrative with context, core flow, and implications.

## When to use

User mentions: explain X, how does X work, what is X, walk me through X, explainer, concept breakdown, mechanism breakdown, protocol explainer, primer — AND wants a visual output.

## Canvas

`poster` (see `references/canvases/poster.md`) — the mechanism flow is the centerpiece, supports carry the KPIs and definitions.

## Snippets

`process-flow` (centerpiece, the mechanism), `statistical` (header KPIs), `list` (definitions / glossary in supports).

## Default style

`aizfographics-style` (or `blueprint` if the content is highly technical).

## Required elements

- `connectors.md` — step connectors, flow arrows
- `text.md` — all atoms
- `layout.md` — canvas, grid recipes
- `decorative.md` — gradient borders, optional hero overlay
- `icons.md` — Phosphor Bold
- `data-widgets.md` — KPI strip
- Optionally `charts.md` if the mechanism involves proportional breakdowns

## Section order

1. **Header strip** — project/protocol logo + "EXPLAINER" badge
2. **Hero** — "How {X} works" gradient title + one-line pitch
3. **TL;DR strip** — 3–4 single-sentence bullet points summarizing the whole thing
4. **Core flow** — `process-flow` with 3–6 numbered steps
5. **Key numbers** — KPI strip (fees, capacity, throughput, TVL — whatever's relevant)
6. **Why it matters** — 1–2 callout cards explaining implications
7. **Footer** — source, version

## Content expectations

Required:
- Thing being explained (clear scope, not "everything about DeFi")
- 3–6 sequential steps that describe the mechanism
- One-line summary of what the thing does

Strongly recommended:
- Concrete numbers (fees, speeds, capacity) that make it real
- Before/after or with/without comparison
- Specific use case that motivates the explanation

## TL;DR block pattern

```html
<section class="section tldr">
  <h2 class="section-title">TL;DR</h2>
  <ul class="tldr-list">
    <li><i class="ph-bold ph-caret-right"></i>{User deposits asset X into a contract}</li>
    <li><i class="ph-bold ph-caret-right"></i>{Contract routes it to yield source Y}</li>
    <li><i class="ph-bold ph-caret-right"></i>{Rewards flow back proportionally}</li>
    <li><i class="ph-bold ph-caret-right"></i>{No active management needed}</li>
  </ul>
</section>

<style>
.tldr-list {
  list-style: none; padding: 0; margin: 0;
  display: flex; flex-direction: column; gap: 8px;
}
.tldr-list li {
  display: grid;
  grid-template-columns: 20px 1fr;
  gap: 10px;
  align-items: start;
  font: 400 15px/1.4 'Montserrat', sans-serif;
  color: var(--text-primary);
}
.tldr-list i {
  color: var(--accent-1);
  font-size: 14px;
  margin-top: 4px;
}
</style>
```

## Content rules

- **Each step is one sentence.** If a step needs more, split it into two steps.
- **Numbers should be checkable.** "Fast" means nothing; "~2s finality" is a claim the reader can verify.
- **No jargon without introduction.** If you use "L2" or "MEV", define it on first mention in the hero or TL;DR.
- **Linear flow only.** If the mechanism has branches, use the flowchart template instead — concept-explainer is for "step 1 → step 2 → step 3".

## Accent pair selection

Default: pair #6 (green → cyan) — tech/protocol vibe.
Override to pair #1 (amber) for finance-adjacent mechanisms (lending, yield).
Override to pair #3 (lime → gold) for DeFi primitives (AMMs, farming).

## Dimension guidance

Portrait-medium (1080 × 1440) for 3–5 step flows. Portrait-tall (1080 × 1920) when adding charts + callouts.
