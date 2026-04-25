# Icons — Phosphor + Iconify, Never Emoji

## Hard rule: zero emoji

Not in titles. Not in bullets. Not in buttons. Not in tooltips. If you find yourself reaching for 🎯 📊 🔥 ⚡ 🚀 ✅, use Phosphor instead.

## Primary: Phosphor Icons, Bold weight

Adds via jsDelivr CDN:

```html
<link rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.2/src/bold/style.css">
```

Usage:

```html
<i class="ph-bold ph-chart-pie"></i>
<i class="ph-bold ph-lightning"></i>
<i class="ph-bold ph-users-three"></i>
<i class="ph-bold ph-coins"></i>
```

1,000+ icons, 6 weights (thin/light/regular/bold/fill/duotone). Bold is default for aizfographics-style.

## Secondary: Iconify API

For crypto tokens, chain icons, and anything Phosphor lacks. No library install — SVG served on demand:

```html
<!-- inline image -->
<img src="https://api.iconify.design/cryptocurrency/eth.svg?color=%23F3A950&height=24"
     alt="Ethereum" style="vertical-align: -0.2em;">

<!-- via lucide set through iconify -->
<img src="https://api.iconify.design/lucide/wallet.svg?color=%23E6E6E6&height=20"
     alt="Wallet">
```

Available sets include `cryptocurrency`, `cryptocurrency-color`, `lucide`, `tabler`, `simple-icons` (brand logos).

## Sizing

| Context | Size |
|---------|------|
| Inline with text | 16–20px |
| Card / badge | 24–32px |
| Hero section feature | 40–48px |
| Decorative accent | 64–96px |

`vertical-align: -0.15em` for inline icons to sit on text baseline.

## Color

Always `currentColor` or an explicit CSS variable. Never hard-coded hex in the icon tag unless using Iconify with an encoded color param.

```html
<i class="ph-bold ph-rocket-launch" style="color: var(--accent-1); font-size: 24px;"></i>
```

## Weight selection by style

| Style | Phosphor weight |
|-------|----------------|
| aizfographics-style | bold |
| clean-minimal | regular |
| blueprint (phase 2) | regular |
| hand-drawn (phase 2) | duotone |
| cyberpunk (phase 2) | fill |

## Consistency rules

- All icons in a row or grid must be from the same library and same weight.
- Never mix Phosphor + emoji. Never mix thin + bold in the same infographic.
- For domain-specific icons (token logos, chain icons): Iconify's `cryptocurrency` set first. Fall back to user-provided image URL.

## Common Phosphor picks

| Concept | Icon |
|---------|------|
| Percentage / allocation | `ph-chart-pie`, `ph-chart-donut` |
| Time / vesting | `ph-clock`, `ph-calendar`, `ph-hourglass` |
| Lock / vesting cliff | `ph-lock-simple`, `ph-lock-key` |
| Growth / trend | `ph-trend-up`, `ph-arrow-up-right` |
| Community | `ph-users-three`, `ph-chats-circle` |
| Tech / protocol | `ph-cube`, `ph-tree-structure`, `ph-code` |
| Money / tokens | `ph-coins`, `ph-currency-circle-dollar`, `ph-wallet` |
| Warning / note | `ph-warning`, `ph-info` |
| Check / success | `ph-check-circle`, `ph-seal-check` |
| Fire / hot | `ph-flame` (not 🔥) |
