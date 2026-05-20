# obsidian-ledger — Antique Accounting Ledger Style

Concept: An antique accounting ledger that has turned black with age. Data is a historical financial record. Gravity and weight are everything.

## When to use

- Financial records, treasury reports, token economics
- Historical data with a ledger-like structure
- Formal financial summaries
- Any content that benefits from the gravity of a physical ledger

## CSS variables

```css
:root {
  /* canvas */
  --canvas:        #0A0A0A;   /* warm black — slightly warmer than Ash */
  --panel:         #0F0F0C;   /* just barely warm */
  --elevated:      #141410;

  /* borders / rules — aged gold */
  --border:        #2E2410;
  --rule-color:    #2E2410;   /* horizontal ruled lines */

  /* text */
  --text-primary:   #D4B86A;  /* primary headings — antique gold */
  --text-secondary: #A08030;  /* active values */
  --text-muted:     #7A6030;  /* body/labels */
  --text-dim:       #4A3A1A;  /* dim/structure */
  --on-accent:      #0A0A0A;

  /* accent — antique gold, headings and active values only */
  --accent-1: #C8A84A;
  --accent-2: #C8A84A;        /* single accent */

  /* semantic */
  --positive: #8B9A4A;        /* desaturated olive for gains */
  --negative: #8A4A2A;        /* desaturated auburn for losses */

  /* spacing */
  --gap-section:   28px;
  --gap-element:   16px;
  --gap-card:      0px;       /* rows are separated by ruled lines, not gap */
  --pad-container: 24px;

  /* radius — none */
  --radius-card:  0px;
  --radius-pill:  0px;
  --radius-btn:   0px;
}
```

## Typography

Serif for all body copy and headings. Monospace for numbers and account codes. Small-caps for column headers.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=JetBrains+Mono:wght@400;700&display=swap">
```

Falls back to: Georgia, 'Times New Roman', serif for the body/heading font.

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero / section heading | IM Fell English / Georgia | 700 | Title Case | 24-40px |
| Column header | IM Fell English / Georgia | 400 | SMALL-CAPS | 11-13px |
| Account code | JetBrains Mono | 400 | UPPERCASE | 10-12px |
| Value / amount | JetBrains Mono | 700 | as-is | 14-18px |
| Body / description | IM Fell English / Georgia | 400 | Sentence | 13-15px |
| Footnote | IM Fell English / Georgia | 400 | Sentence | 11px |

Currency symbols attached to values: `$12,400`, `4,281 ETH`. No space between symbol and number.

## Layout rules

### Horizontal ruled lines as primary structure

Not boxes. The ledger is made of lines, not cards.

```html
<div class="ledger-section">
  <div class="ledger-title">CAPITAL ACCOUNT</div>
  <div class="ledger-rule-heavy"></div>

  <div class="ledger-row">
    <span class="ledger-desc">Protocol revenue — Q1 2026</span>
    <span class="ledger-code">ACC-4412</span>
    <span class="ledger-amount">$2,840,000</span>
  </div>
  <div class="ledger-rule"></div>

  <div class="ledger-row ledger-indent">
    <span class="ledger-desc">Swap fees</span>
    <span class="ledger-code">GL-0091</span>
    <span class="ledger-amount">$1,420,000</span>
  </div>
  <div class="ledger-rule"></div>

  <div class="ledger-row ledger-total">
    <span class="ledger-desc">Total</span>
    <span class="ledger-code"></span>
    <span class="ledger-amount">$2,840,000</span>
  </div>
  <div class="ledger-rule-double"></div>
</div>

<style>
.ledger-section {
  display: flex;
  flex-direction: column;
  font-family: 'IM Fell English', Georgia, serif;
}

.ledger-title {
  font: 700 16px/1.4 'IM Fell English', Georgia, serif;
  color: var(--accent-1, #C8A84A);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-variant-caps: small-caps;
  padding: 8px 0 4px;
}

.ledger-rule-heavy {
  border-top: 2px solid var(--rule-color, #2E2410);
  margin: 4px 0;
}

.ledger-rule {
  border-top: 1px solid var(--rule-color, #2E2410);
  margin: 0;
}

.ledger-rule-double {
  /* Double rule under totals */
  border-top: 3px double var(--accent-1, #C8A84A);
  margin: 2px 0 8px;
}

.ledger-row {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 16px;
  padding: 8px 0;
  align-items: baseline;
}

.ledger-indent .ledger-desc { padding-left: 20px; }

.ledger-desc {
  font: 400 13px/1.4 'IM Fell English', Georgia, serif;
  color: var(--text-muted, #7A6030);
}

.ledger-code {
  font: 400 10px/1 'JetBrains Mono', monospace;
  color: var(--text-dim, #4A3A1A);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  text-align: right;
  min-width: 60px;
}

.ledger-amount {
  font: 700 14px/1 'JetBrains Mono', monospace;
  color: var(--text-secondary, #A08030);
  font-variant-numeric: tabular-nums;
  text-align: right;
  min-width: 100px;
}

.ledger-total .ledger-desc  { font-weight: 700; color: var(--text-primary, #D4B86A); }
.ledger-total .ledger-amount { color: var(--text-primary, #D4B86A); }
</style>
```

### Date stamp

Top corner of section or page:

```html
<div class="ledger-date">FY 1897 — Q3 · Oct-Dec</div>
<style>
.ledger-date {
  font: 400 11px/1 'IM Fell English', Georgia, serif;
  color: var(--text-dim, #4A3A1A);
  text-align: right;
  font-style: italic;
}
</style>
```

### Section stamps

```html
<div class="ledger-stamp">LIABILITIES</div>
<style>
.ledger-stamp {
  font: 400 12px/1 'IM Fell English', Georgia, serif;
  color: var(--accent-1, #C8A84A);
  text-transform: uppercase;
  letter-spacing: 0.15em;
  font-variant-caps: small-caps;
}
</style>
```

## Decorative DNA

Horizontal ruled lines are the only structure. No card boxes. No rounded elements. No icons.

The double-ruled total line `══════` (CSS `border-top: 3px double`) is the signature element.

Gold (`--accent-1`) appears only on headings and active values — never decoratively.

## Gradient text

Disabled. Headings use flat `--text-primary` (#D4B86A).

## Badge override

Use `status-pill` variant from `badges.md` with these color overrides:

```css
.badge-active  { color: #C8A84A; background: rgba(200,168,74,0.10); border-color: rgba(200,168,74,0.25); }
.badge-error   { color: #8A4A2A; background: rgba(138,74,42,0.10);  border-color: rgba(138,74,42,0.25); }
.badge-offline { color: #4A3A1A; background: rgba(74,58,26,0.10);   border-color: rgba(74,58,26,0.25); }
```

## Step-connector override

Square badges, antique gold fill (`#C8A84A`). Connector line: `#2E2410`. Serif step labels.

## Style verification checklist

- [ ] Serif font (IM Fell English or Georgia) used for all headings and body
- [ ] JetBrains Mono for all numbers and account codes
- [ ] `--accent-1: #C8A84A` only on headings and values, never decorative
- [ ] No rounded corners anywhere
- [ ] Horizontal ruled lines as primary structure — not card boxes
- [ ] Double rule `border-top: 3px double` under all total rows
- [ ] Currency symbols attached: `$12,400`, not `$ 12,400`
- [ ] No sans-serif anywhere

## What to avoid

Sans-serif fonts, bright colors, modern layout patterns (flexbox card grids), icons, rounded shapes, card boxes replacing ruled lines, border-radius anywhere.
