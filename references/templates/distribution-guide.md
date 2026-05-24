# Distribution Guide Template

Eligibility, allocation, claim steps, and deadlines for any distribution event: airdrops, giveaways, reward campaigns, grants, or public launches. High-stakes informational content — clarity beats style.

## When to use

User mentions: airdrop, claim guide, eligibility infographic, airdrop eligibility, claim instructions, airdrop breakdown, retro rewards, giveaway guide, reward campaign, distribution event, grant guide.

## Canvas

`bento-box` (see `references/canvases/bento-box.md`) — hero strip with allocation + KPIs, then mixed-span cards for eligibility, claim steps, and deadlines.

## Snippets

**Snippets:** `statistical` (allocation KPI strip), `list` (eligibility criteria), `process-flow` (claim steps), `timeline` (deadlines).

## Default style

`aizfographics-style`

## Required elements

- `text.md`, `layout.md`, `decorative.md`, `icons.md`
- `data-widgets.md` — big-number for total allocation
- `connectors.md` — timeline for deadlines, step connectors for claim flow
- Optionally `charts.md` for allocation breakdown

## Section order

1. **Header strip** — project logo + "DISTRIBUTION GUIDE" badge + status tag (Live / Ending Soon / Closed)
2. **Hero** — "$TOKEN Airdrop" title + one-line summary
3. **Allocation stats** — Total tokens + % of supply + recipient count
4. **Eligibility criteria** — numbered list of requirements (must hold X / staked Y / used Z)
5. **Claim steps** — process-flow with 3–5 steps (visit → connect → verify → claim)
6. **Timeline / deadlines** — horizontal timeline with key dates (snapshot, claim window, expiry)
7. **Warnings** — callout with security reminders (no DMs, official URL only)
8. **Footer** — official URL, support channel

## Content expectations

Required:
- Token name and ticker
- Total airdrop allocation
- Eligibility criteria (concrete rules)
- Claim URL
- Deadlines (snapshot date, claim opens, claim closes)

Strongly recommended:
- Expected distribution shape (per-user, tiered)
- Required wallet or credential (EVM, solana, Discord, etc.)
- Known issues or FAQ

## Warnings block pattern

```html
<section class="section warnings">
  <h2 class="section-title">Stay safe</h2>
  <ul class="warning-list">
    <li><i class="ph-bold ph-warning"></i>
      Only claim from the official URL: <strong>{official_url}</strong>
    </li>
    <li><i class="ph-bold ph-warning"></i>
      No team member will DM you first. Ignore unsolicited messages.
    </li>
    <li><i class="ph-bold ph-warning"></i>
      Never share your seed phrase. The claim flow only needs a signature, not your keys.
    </li>
  </ul>
</section>

<style>
.warnings {
  padding: 16px;
  border: 1px solid color-mix(in srgb, var(--negative) 40%, transparent);
  background: color-mix(in srgb, var(--negative) 5%, transparent);
  border-radius: var(--radius-card);
}
.warning-list {
  list-style: none; padding: 0; margin: 0;
  display: flex; flex-direction: column; gap: 8px;
}
.warning-list li {
  display: grid;
  grid-template-columns: 22px 1fr;
  gap: 10px;
  font: 400 13px/1.4 'Montserrat', sans-serif;
  color: var(--text-primary);
}
.warning-list i { color: var(--negative); font-size: 16px; margin-top: 2px; }
.warning-list strong { color: var(--accent-1); }
</style>
```

The warnings section is **mandatory** in every distribution infographic involving a claim flow. Distribution events are high-phishing-risk; the infographic shares partial responsibility for user safety.

## Content rules

- **Claim URL appears exactly twice** — in the warnings block and in the footer. Never in the body.
- **Deadlines explicit.** Always include timezone (UTC preferred). "7-day window" without a start date is useless.
- **Eligibility is binary where possible.** "Held X on date Y" = yes/no. Avoid "active participant" (too subjective).
- **Numbers round carefully.** "2.5M tokens" not "2,500,000" in hero; full number in the stats strip.

## Accent pair selection

Default: pair #2 (gold → orange) — launch / announcement energy.
Override to pair #4 (red → pink) if the drop is time-critical / competitive.

## Dimension guidance

Portrait-medium (1080 × 1440) or portrait-tall (1080 × 1920). The warnings block adds ~150px — account for it.

## Anti-patterns

- Never exaggerate eligibility ("everyone qualifies" — no)
- Never omit deadlines ("soon" — no)
- Never substitute claim URL with an abbreviated one ("bit.ly/..." invites phishing copies). Full domain only.
