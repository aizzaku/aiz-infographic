# Annotation — Margin Callouts with Leaders

A callout that lives **outside** the primary visualization bounds and points at something inside via a dashed leader line + landing dot. Use sparingly — annotations are for adding context the visualization cannot carry on its own, never for duplicating a label that's already there.

Direct adaptation of the "margin annotation" primitive from technical-diagram conventions, translated into the aizfographics dark-mode visual language (Montserrat sans, no serifs, no italic) so it matches the rest of the skill's output.

## When to use

- A data point needs a caveat or citation ("based on Q3 '25 snapshot", "excludes airdrop").
- A node's behaviour deserves a one-line explanation that would bloat the card if inlined.
- A section needs a "why" callout pointing at a specific element, not the whole section.

## When NOT to use

- To add decoration. Every annotation must carry information, not atmosphere.
- As a substitute for a missing label. Label the thing directly instead.
- Inside the canvas. Callouts live in the **margin** — outside card bounds, between sections, or in reserved right/left gutters. Never overlapping primary content.
- More than **2 per infographic.** Past that, the design is doing too little and the annotations are doing too much.

## Pattern (DOM)

Two parts: a `.callout` (the text block) and a `.callout-leader` (the dashed line + landing dot, drawn as SVG so it can bend). The callout is anchored via `position: absolute` to a relatively-positioned section container.

```html
<div class="callout-wrap" style="top: 120px; left: 16px;">
  <p class="callout">
    Vesting restarts at month 6 if the cliff is missed — this is the one edge
    case that breaks the linear unlock curve.
  </p>
  <svg class="callout-leader" viewBox="0 0 120 40" preserveAspectRatio="none">
    <path d="M 0 20 C 40 20, 60 30, 115 35"
          fill="none"
          stroke="color-mix(in srgb, var(--text-muted) 60%, transparent)"
          stroke-width="1"
          stroke-dasharray="3 3"/>
    <circle cx="115" cy="35" r="2.5"
            fill="color-mix(in srgb, var(--accent-1) 70%, transparent)"/>
  </svg>
</div>

<style>
.callout-wrap {
  position: absolute;
  width: 220px;
  pointer-events: none;
}
.callout {
  font: 400 11px/1.4 'Montserrat', sans-serif;
  color: var(--text-secondary);
  letter-spacing: 0;
  text-transform: none;
  margin: 0 0 4px 0;
}
.callout-leader {
  display: block;
  width: 120px;
  height: 40px;
  margin-top: 2px;
}
</style>
```

## Rules

- **Font**: Montserrat 400, 11px. Sentence case, never uppercase. Never italic (conflicts with the style's two-font rule — italic would read as a third typographic treatment).
- **Max 2 per infographic.** One is usually enough.
- **Leader is always dashed.** Solid leaders read as "this is a real connector" (see `connectors.md`). Dashed = "annotation, not structure".
- **Leader color**: `color-mix(in srgb, var(--text-muted) 60%, transparent)`. Never the full accent — the annotation supports the visualization, it doesn't compete with it.
- **Landing dot** uses accent-1 at 70% so the eye can trace the leader back to its target. 2.5px radius.
- **Position the text in the margin.** Never overlap cards, charts, or tables. If you can't find margin room, the infographic is too dense — increase width or cut content, don't cram the annotation inside.
- **One idea per callout.** A callout with two sentences of different points should be two callouts, or more likely a footnote strip.
- **Never annotate an annotation.** Callouts can only point at primary content.

## SVG variant (for annotations inside SVG diagrams)

If the visualization is an inline SVG (e.g. flowchart, circular-flow), render the callout inside the SVG as a `<g>` so it scales with the diagram:

```html
<g class="callout-g" transform="translate(24, 180)">
  <path d="M 0 0 C 40 0, 70 15, 110 20"
        fill="none"
        stroke="color-mix(in srgb, var(--text-muted) 60%, transparent)"
        stroke-width="1"
        stroke-dasharray="3 3"/>
  <circle cx="110" cy="20" r="2.5"
          fill="color-mix(in srgb, var(--accent-1) 70%, transparent)"/>
  <foreignObject x="-200" y="-28" width="200" height="52">
    <p xmlns="http://www.w3.org/1999/xhtml"
       style="font: 400 11px/1.4 'Montserrat', sans-serif;
              color: var(--text-secondary); margin: 0; text-align: right;">
      Claims queue drains lazily — expect 2–5 block latency under load.
    </p>
  </foreignObject>
</g>
```

Same rules apply. `foreignObject` keeps the text as real HTML so typography stays consistent with the rest of the infographic.
