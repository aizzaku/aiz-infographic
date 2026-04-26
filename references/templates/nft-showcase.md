# NFT Showcase Template

Collection overview with traits, rarity breakdown, and featured items. For NFT drops, mint announcements, or trait guides.

## When to use

User mentions: NFT collection, mint, traits, rarity chart, floor stats, NFT showcase, collection overview, trait breakdown.

## Canvas

`bento-box` (see `references/canvases/bento-box.md`) — hero strip with collection KPIs, then a wide `grid-cards` snippet for the item gallery, with optional rarity-chart card alongside.

## Snippets

`statistical` (collection KPI strip), `grid-cards` (item gallery), `chart` (trait rarity breakdown, optional).

## Default style

`aizfographics-style`

## Required elements

- `text.md`, `layout.md`, `decorative.md`, `icons.md`
- `data-widgets.md` — KPI strip
- `charts.md` — rarity breakdown (donut or segmented bar)
- Optional `comparison.md` for legendary/rare/common comparison

## Section order

1. **Header strip** — collection name + "COLLECTION OVERVIEW" badge + chain indicator
2. **Hero** — collection title + one-line theme + featured hero image (or placeholder grid)
3. **Collection stats** — supply / owners / floor / volume
4. **Rarity distribution** — breakdown by tier (Legendary / Epic / Rare / Common)
5. **Featured traits** — grid of 4–8 iconic traits with rarity %s
6. **Sample items** — 4–6 item thumbnails with names + tier labels
7. **Mint / where to buy** — CTA block with marketplace links
8. **Footer** — creator, date, collection address (truncated)

## Content expectations

Required:
- Collection name + chain
- Total supply
- At least 3 rarity tiers with counts

Strongly recommended:
- Floor price (with date stamp)
- Owner count
- Sample image URLs
- Featured trait breakdowns

Nice-to-have:
- Mint start / end dates
- Marketplace links
- Creator info

## Item card pattern

```html
<div class="nft-card">
  <div class="nft-image">
    <img src="{image_url}" alt="{item_name}">
  </div>
  <div class="nft-tier tier-legendary">Legendary</div>
  <div class="nft-name">#0042 — Solar</div>
</div>

<style>
.nft-card {
  background: var(--panel);
  border-radius: var(--radius-card);
  overflow: hidden;
  border: 1px solid color-mix(in srgb, var(--accent-1) 25%, transparent);
  display: flex;
  flex-direction: column;
}
.nft-image {
  aspect-ratio: 1 / 1;
  background: var(--elevated);
  overflow: hidden;
}
.nft-image img { width: 100%; height: 100%; object-fit: cover; }
.nft-tier {
  font: 700 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 4px 10px;
  background: var(--elevated);
}
.tier-legendary { background: color-mix(in srgb, #FFD166 30%, var(--elevated)); color: #FFD166; }
.tier-epic      { background: color-mix(in srgb, #C57AFF 30%, var(--elevated)); color: #C57AFF; }
.tier-rare      { background: color-mix(in srgb, #42D4F4 30%, var(--elevated)); color: #42D4F4; }
.tier-common    { background: var(--elevated); color: var(--text-secondary); }
.nft-name {
  padding: 8px 12px;
  font: 700 12px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
</style>
```

## Trait breakdown table

```html
<table class="trait-table">
  <thead><tr><th>Trait</th><th>Count</th><th>% of supply</th></tr></thead>
  <tbody>
    <tr><td>Golden Crown</td><td>42</td><td class="val-accent">0.42%</td></tr>
    <tr><td>Laser Eyes</td><td>128</td><td class="val-accent">1.28%</td></tr>
    <!-- … -->
  </tbody>
</table>
```

Use `.feature-table` styling from the comparison element.

## Content rules

- **Always include chain.** NFT content without chain context is confusing — Ethereum and Solana are very different markets.
- **Rarity tiers are collection-defined.** Don't impose Legendary/Epic/Rare/Common if the creator uses Mythic/Ultra/Standard.
- **Floor price is volatile.** Stamp with date+time or mark "as of {date}".
- **Sample items chosen for diversity**, not just for rarity — show the range.

## Accent pair selection

Default: pair #4 (red → pink) — NFT culture energy.
Override to match collection's brand palette.

## Dimension guidance

Portrait-tall (1080 × 1920) for rich showcases. Portrait-medium for compact summaries. Square for social teasers.
