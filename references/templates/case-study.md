# Case Study Infographic Template

Visual storytelling of a named growth case with methodology + replicable framework.

## When to use

User presents a documented case study with named company/person + specific metrics. Trigger phrases: "case study", "growth hack results", "how [company] grew", "success story", "[tactic] worked for [X]".

Use when you have:
- Named subject (company/person)
- Specific outcome metrics (revenue, conversion, growth rate)
- At least one documented mechanism or tactic in the source material

## Canvas

`bento-box` (see `references/canvases/bento-box.md`) — hero outcome + KPI cards + mechanism + application steps.

## Snippets

- `statistical` — headline outcome card(s)
- `comparison` — before vs after (if available)
- `grid-cards` — mechanism breakdown (2–3 key tactics)
- `process-flow` OR `numbered-list` — How to Apply (4–5 step action framework)
- `comparison` — Search Keywords (compact reference table)

## Default style

`aizfographics-style` or `glassmorphism` for social growth content (glassmorphism for growth hacking per compact mode).

## Required elements

- `text.md` — all copy
- `layout.md` — grid recipes, spacing
- `icons.md` — one icon per mechanism card
- `comparison.md` — keyword table

## Section order (standard pattern)

```
┌──────────────────────────────────────────────┐
│ HERO: Outcome + named subject + timeframe    │
│ ── headline stat: "50% MRR Increase"         │
│ ── KPI row: [3 cards] results                │
├──────────────────────────────────────────────┤
│ MECHANISM CARD (wide: 1/2 or 1/3?)           │
│ ── "How They Did It"                         │
│ ── 2–3 key tactics with icons                │
├──────────────────────────────────────────────┤
│ CORE CARDS (3 columns):                       │
│ ── Card 1: First tactical insight            │
│ ── Card 2: Second tactical insight           │
│ ── Card 3: Third tactical insight            │
│ ⚠︎ if not enough space → reduce to 2 cards  │
│   but always show the mechanism               │
├──────────────────────────────────────────────┤
│ HOW TO APPLY (full-width, 1/-1)              │
│ ── 4–5 numbered steps                          │
│ ── concrete, executable                        │
│ ── NOT generic advice — reproduceable         │
├──────────────────────────────────────────────┤
│ SEARCH KEYWORDS (comparison table, narrow)   │
│ ── compact 2-col table                          │
│ ── use when searching to learn more           │
│ ── example format: "presell lifetime deals"   │
├──────────────────────────────────────────────┤
│ FOOTER: Source attribution                    │
└──────────────────────────────────────────────┘
```

## Content requirements (non-negotiable)

Every case study infographic must include **all four** layers:

1. **OUTCOME** — what happened, with numbers + timeframe
2. **MECHANISM** — the specific tactics they used (2–3 items)
3. **APPLICATION** — how YOU can do this, step-by-step (4–5 numbered actions)
4. **DISCOVERY** — search keywords or resource names so the reader can dig deeper

If the source material does not include application steps, infer them from the Mechanism by asking: "Given what they did, what's the closest reproducible sequence for a founder with similar resources?" — still output a concrete numbered list. Derive from context, don't punt.

## Copy constraints

- Hero headline = outcome-oriented but verb-driven: "Doubled ARPU", "Ship Nothing, Collect $20K"
- Mechanism cards = tactic names + 1-sentence explanation each
- Application steps = imperative mood, 8–15 words per step max
- Search table = exact phrases, not questions

## Common pitfall

If you only have "outcome + context" and skip mechanism/application sections, you are producing a 50% signal artifact. Aiz will correct this and ask for regeneration. Default to including all four layers even if details are thin — extrapolate conservatively.

## Width & density

- Default: **1920px** (social/landscape optimized)
- Card count: ≤ 6 total (hero + 4 content + keywords) to preserve readability
- Font size floor: 14px body, 36px hero

## Related templates

- `cheatsheet` — for tip collections, not story-driven case studies
- `report` — for multi-case, data-heavy briefings
