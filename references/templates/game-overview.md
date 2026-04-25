# Game Overview Template

Comprehensive single-page introduction to a game. Hero visual, core loop, key mechanics, progression, and where to start.

## When to use

User mentions: game overview, whitepaper visual, game infographic, introduce game, game pitch visual, game summary. Often paired with gaming content (Gigaverse, Parallel, etc.).

## Base layout

`bento-box` (see `references/layouts/bento-box.md`) — hero strip + mixed-span cards for stats, features, core loop, progression, and start-steps. Each section is its own bento card sized to weight: a feature gets a wide card, a stat gets a small one, the core loop card can be tall to accommodate a circular-flow diagram.

**Layout fallback:** if the user wants a more traditional one-column flow, use a hybrid of `statistical` + `grid-cards` + (optionally) `circular-flow` for the loop.

## Default style

`aizfographics-style` or `retro` if the game is pixel-art.

## Required elements

- `text.md`, `layout.md`, `decorative.md`, `icons.md`
- `data-widgets.md` — big numbers for game stats
- `connectors.md` — for core loop arrows
- Optionally `charts.md`, `comparison.md`

## Section order

Arranged as a hero card plus 2–3 rows of mixed cards.

1. **Hero card (full-bleed)** — game logo + game title + tagline + 4 key-stat KPIs inline (genre / chain / players / season). Key art can sit inside the hero or become its own tall sidebar card.
2. **Core loop card (wide or tall)** — circular-flow OR 3–5 step process. If the loop is the centerpiece, give it `1 / 3` plus `grid-row` span 2.
3. **Feature cards** — 3–6 small/medium bento cards alongside the loop. Each feature card is a mini grid-cards-style cell (icon + title + 1-line body + optional badge).
4. **Progression / economy card (medium)** — short description with 1–2 supporting stats.
5. **How to start card (wide)** — 3–4 steps as a numbered list in one wide card. Sits in the bottom row.
6. **Footer card (full-bleed, optional)** — links, socials, key dates.

## Content expectations

Required:
- Game name + genre
- Platform/chain(s)
- 3–5 core features
- Brief gameplay loop description

Strongly recommended:
- Key stats (active players, total matches, season duration)
- How to start steps
- Key art / screenshot URLs

## Core loop pattern

Use `circular-flow` for cyclical games (stake → play → earn → upgrade → stake). Use `process-flow` for linear games with distinct phases (tutorial → ranked → prestige).

## Feature card variant

```html
<div class="feature-card">
  <div class="feature-icon"><i class="ph-bold ph-sword"></i></div>
  <h3 class="card-title">Real-time combat</h3>
  <p class="body">Live 4v4 matches with active ability management.</p>
  <div class="feature-meta">
    <span class="badge">PvP</span>
  </div>
</div>
```

Use the standard `grid-cards` layout spec (batch-1 grid-cards.md) for the grid wrapper.

## Content rules

- **Show, don't describe.** Include at least one key-art image if available. A game overview without art is weaker than one with a placeholder.
- **One loop metaphor.** If you show a cycle, everything else should feed into that framing. Don't mix "cycle" and "funnel" language for the same mechanic.
- **Concrete numbers.** "Fast matches" vs "3-min matches" — always the second.
- **Start steps last.** CTA at the bottom matches reading flow.

## Accent pair selection

Default: match game's brand palette.
Fallback: pair #4 (red → pink) for action/competitive games, pair #3 (lime → gold) for economy-heavy games, pair #6 (green → cyan) for sci-fi.

## Dimension guidance

Bento game overviews are landscape-first.

- Default: **1920w wide**, content-driven height — fits hero + loop + features + start steps comfortably.
- Pitch-deck variant: 1920w with tighter row count (skip progression card if the user wants 3 rows max).
- Social teaser variant only on explicit request: 1080w (collapses bento to 2 columns; drop loop card or make it row-1).
