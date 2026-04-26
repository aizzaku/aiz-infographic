---
name: create-infographics
description: Create professional infographics as self-contained HTML files with PNG exports. Use when the user asks to create, design, generate, build, or make an infographic, data visualization, visual explainer, chart poster, cheatsheet, or pocket guide. Trigger phrases include "make this visual", "turn this into a graphic", "visualize this data", "infographic for X", "cheatsheet for X", or when the user provides structured data (tokenomics allocations, ecosystem/partner lists, timelines, comparisons, step-by-step processes) AND asks for a visual output. Covers tokenomics, ecosystem overviews, game overviews, cheatsheets, airdrop guides, comparisons, and process flows. Do NOT trigger for plain text answers, markdown tables, bulleted summaries, questions asking for advice or explanations about a topic (even when the topic is tokenomics, ecosystem, vesting, etc.), inline chat diagrams, or data processing with no visual output requested. The signal is "asks for a visual", not "mentions a keyword".
---

# Create Infographics

Produces self-contained HTML infographics following a 5-layer reference system: **canvases × snippets × styles × elements × templates**. Primary output is HTML. PNG is exported reliably via Playwright. For editable vectors, users run the HTML through the html.to.design Figma plugin (see §13).

### Reference hierarchy

| Layer | Lives in | Role |
|---|---|---|
| **Canvas** | `references/canvases/<name>.md` | The page architecture: how the whole infographic is composed. Defines slots that snippets plug into. (bento-box, editorial, dashboard, poster) |
| **Snippet** | `references/snippets/<name>.md` | An embeddable section pattern: timeline spine, fishbone, kpi-strip, comparison table — the content essence with no page chrome. |
| **Style** | `references/styles/<name>.md` | Visual identity: colors, fonts, spacing tokens. (aizfographics-style default) |
| **Element** | `references/elements/<name>.md` | Atomic UI primitives: text, charts, icons, connectors. |
| **Template** | `references/templates/<name>.md` | High-level preset = canvas + style + snippet picks for a content type. (token-economics, cheatsheet, etc.) |

A **canvas** owns the page chrome (header, hero, footer, grid). A **snippet** is a thing on the page (a timeline, a fishbone, a kpi-strip) that plugs into a canvas slot. The user picks the canvas; the data picks the snippets.

The default visual identity is **aizfographics-style** — dark background, Bebas Neue + Montserrat, one accent color pair per infographic, gradient borders, glow effects, no emoji ever.

---

## 1. Mode Detection

Every request is either **one-shot** (generate immediately) or **guided** (ask questions first).

### One-shot triggers — all three must be true:

- Content or data is provided (paste, file, URL, or structured text)
- Type is clear (explicit template name OR obvious content category like "tokenomics")
- Enough data to fill required sections without major guessing

### One-shot override phrases (force one-shot even with incomplete data):

`one-shot`, `just make it`, `don't ask`, `generate directly`, `here's everything`, `quick`, `same as last time`

### Guided triggers — any one is enough:

- Content is vague or incomplete
- No clear type or layout match
- User asks for help choosing

### Guided override phrases:

`help me`, `what canvas`, `what layout`, `walk me through`, `I'm not sure`, `what do you recommend`

When ambiguous, prefer guided — it's easier to skip forward than to regenerate.

---

## 1.5 Canvas Pick (when no template matched)

After §4 Content Intake but before §5 Step 2, fire the canvas picker — but only when no template matched in §2 and the user hasn't named a canvas explicitly.

### Skip this step when:

- A template matched in §2 routing (the template dictates its canvas).
- The user's initial message named a canvas explicitly: `bento`, `bento-box`, `editorial`, `magazine`, `dashboard`, `poster`, `hero-led`, `single subject`.
- Agent context (§11) → default to `bento-box`, do not open the gallery, do not fire `AskUserQuestion`.

### Otherwise:

1. **Open the gallery** — `references/_gallery.html` — using the same auto-open helper as §10:
   - Windows: `start references/_gallery.html`
   - macOS: `open references/_gallery.html`
   - Linux: `xdg-open references/_gallery.html`
2. **Fire `AskUserQuestion`** with each option carrying a short text preview:
   - Question: *"Which canvas architecture? (Gallery just opened — see visual examples)"*
   - Header: `Canvas`
   - Options:
     1. `Bento-box (default)` — preview: *"Mixed-span grid. Hero + cards. Posters, overviews."*
     2. `Editorial / Magazine` — preview: *"Long-form columnar. Headlines + body + sidebar. Storytelling."*
     3. `Dashboard` — preview: *"KPI strip + chart panels. Metrics snapshots."*
     4. `Poster / Hero-led` — preview: *"One big diagram + supports. Single-subject deep-dive."*
3. Load `references/canvases/<picked>.md`. Continue to §5 Step 2 (snippet selection) or to one-shot generation.

---

## 2. Routing Decision Tree

```
Request arrives
│
├─ Matches a known template? (tokenomics, ecosystem overview, cheatsheet…)
│   └─ YES → Load template → load its canvas + style + required snippets + elements
│
├─ User named a canvas explicitly? (bento, editorial, dashboard, poster)
│   └─ YES → Load that canvas → §5 step 2 (snippet pick) → style + elements
│
└─ Generic request ("make an infographic about X")
    └─ §1.5 Canvas Pick (open gallery + AskUserQuestion) → load picked canvas → continue
```

### Template → canvas → snippet → style → elements mapping

Each template file specifies:
- Its `canvas:` (almost always one of the 4)
- Its `snippets:` (which section patterns to host inside the canvas)
- Its default style (almost always `aizfographics-style`)
- The exact element categories it requires

For bento-box / dashboard / poster canvases at 1920w, that's the default. Editorial canvas defaults to 1280w. Templates currently defaulting to `bento-box` canvas: `cheatsheet`, `ecosystem-overview`, `game-overview`, `report`, `token-economics`, `crypto-explainer`, `how-it-works`, `airdrop-guide`, `nft-showcase`, `game-mechanics`.

Never load the full references tree. Read only what the current request maps to.

---

## 3. Reference Loading Rules

**Load the minimum set. Re-read nothing.**

| What you need | Where to find it |
|---|---|
| A known content type preset | `references/templates/<name>.md` |
| The page architecture | `references/canvases/<name>.md` |
| A section / content shape | `references/snippets/<name>.md` |
| Visual tokens (colors, fonts, spacing) | `references/styles/<name>.md` |
| Atomic UI building blocks | `references/elements/<name>.md` |
| Export mechanics | `references/export/<name>.md` |
| Canvas visual gallery | `references/_gallery.html` (auto-opened in §1.5 only) |
| Signal sheet extraction (§8.6) | `references/templates/_signals.md` (loaded only when §8.6 fires) |

### Typical load order for a one-shot tokenomics request:

1. `references/templates/token-economics.md`
2. `references/canvases/<canvas named by template>.md` (usually `bento-box`)
3. `references/styles/aizfographics-style.md`
4. Each snippet the template names — load from `references/snippets/<name>.md`. Typical for tokenomics: `statistical`, `comparison`. Donut/vesting-bar are inline `<svg>` patterns under `references/elements/charts.md` + `data-widgets.md`.
5. Each element the template names: `charts.md`, `data-widgets.md`, `text.md`, `layout.md`, `connectors.md`, `decorative.md`
6. **In Claude Code context**, also load `references/creator-tools.md` and `references/viewer-features.md` — these are mandatory inputs to the HTML skeleton (see §6).

Eight to ten files total in Claude Code, six to eight in agent contexts. Do not read other templates, other canvases, or other styles unless the user's request demands them.

### Available references

**Canvases** (4): `bento-box` (default), `editorial`, `dashboard`, `poster`.

**Styles** (10): `aizfographics-style` (default), `clean-minimal`, `blueprint`, `editorial`, `corporate`, `cyberpunk`, `chalkboard`, `hand-drawn`, `retro`, plus `_custom-template` scaffold for bespoke styles.

**Snippets** (22): `statistical`, `grid-cards`, `process-flow`, `timeline`, `comparison`, `hierarchical`, `list`, `roadmap`, `funnel`, `flowchart`, `dashboard`, `mind-map`, `journey-path`, `pyramid`, `circular-flow`, `iceberg`, `fishbone`, `venn`, `anatomical`, `geographic`, `quadrant`, `swimlane`. Each is an embeddable section pattern that any canvas can host in one of its slots. Each snippet declares its slot fit (which canvas slots accept it, with what dimensions). No `bento-box` snippet — bento-box is canvas-only.

**Templates** (10): `token-economics`, `ecosystem-overview`, `cheatsheet`, `crypto-explainer`, `game-overview`, `airdrop-guide`, `nft-showcase`, `how-it-works`, `report`, `game-mechanics`.

**Elements** (10): `charts`, `text`, `layout`, `connectors`, `icons`, `data-widgets`, `decorative`, `maps`, `comparison`, `annotation`.

**Viewer features** (5 optional, all drop-in): hover tooltips, animated number counters, scroll reveals, expandable sections, dark/light toggle — see `references/viewer-features.md`.

If the user requests a content type that doesn't map to any template, fall through to the canvas pick (§1.5) and pick snippets that match the content shape. If they want a style not listed, copy `_custom-template.md` and fill it in; note the substitution in your response.

---

## 4. Content Intake

Extract, then confirm in one short message:

```
Extracted:
  Topic: <title>
  Type: <template or layout name>
  Data points: <count + shape>
  Content density: <thin | medium | dense>
  Missing: <list anything critical that's absent>
```

If critical data is missing, ask before generating. Never fabricate financial numbers, dates, or partner lists. For cosmetic gaps (accent color preference, exact dimensions), pick a sensible default and proceed.

---

## 5. Guided Mode Step Flow

Only use in guided mode. In one-shot, skip to the Generation step.

**MANDATORY TOOL USAGE.** Every step below that offers options MUST be executed as a single `AskUserQuestion` tool call — not plain text with numbered options. The tool call is what renders the tappable UI in Claude Code. If `AskUserQuestion` is unavailable in the current host (agent contexts like OpenClaw/Hermes), fall back to numbered text options and wait for a reply.

Never bundle more than one question per `AskUserQuestion` call unless the questions are truly independent. One step = one call.

### Step 1 — Intake

Confirm extraction as shown in §4. No tool call; this is a plain-text recap. If critical content is missing, ask for it before proceeding.

### Step 1.5 — Canvas pick

Run §1.5 Canvas Pick (open gallery + AskUserQuestion). Skip when a template matched in §2 or the user named a canvas explicitly.

### Step 2 — Template or snippet selection

Fire `AskUserQuestion`:

- **Template match found:** question = "Use the <name> template, customize, or pick different snippets?" — options = `["Use <name> template", "Customize sections", "Pick different snippets"]`.
- **No template match (canvas already picked in Step 1.5):** question = "Which snippets should the <canvas> host?" — list the 3-5 snippets that best fit the content (each option's preview shows the snippet name + one-line role) plus `"Custom mix (I'll describe)"`. Multi-select is fine here. The picked snippets fill the canvas's slots per its slot rules.

### Step 3 — Style

Fire `AskUserQuestion`. Question = "Keep aizfographics-style or switch?" — options = `["aizfographics-style (default)", "Clean minimal", "Blueprint", "Custom (I'll describe)"]`. For most personal work this is a one-tap confirmation; skip only if the user already named a style in their request.

### Step 4 — Color

Fire `AskUserQuestion`. Question = "How should the accent color be chosen?" — options:

1. **Use style default** — keep the accent pair from the chosen style.
2. **Pick brand color (auto-search)** — Claude runs a web search for "<brand name from content> brand guidelines" / "<brand name> primary color hex", extracts the primary pair, applies it as the accent. Cite the source domain in the Step 6 generation recap. If search yields nothing usable, fall back to option 1 and note the fallback.
3. **Match a brand URL (extract)** — the user gives a site URL; Claude runs the 5-step extraction flow below.
4. **I'll give you the hex values** — follow up with a free-text ask for the hex pair.
5. **Surprise me** — Claude picks a pair that fits the content topic.

#### Brand URL extraction flow (option 3)

1. **Fetch** the URL via `WebFetch`. Keep only the `<head>` + first `<body>` screen worth of content (enough to catch brand CSS vars, logo, hero).
2. **Extract colors.** Scan in priority order:
   - CSS custom properties on `:root` / `html` / `body` starting with `--color-`, `--brand-`, `--primary`, `--accent`.
   - Inline `style="background/color: #…"` on hero-level elements.
   - Computed swatches from `<meta name="theme-color">` and SVG logo `fill=` attrs.
   - As a last resort, run a coarse frequency count of hex colors in the returned CSS and take the two most common non-neutral, non-`#000/#fff`, non-grayscale ones.
3. **Map to accent pair.** Pick the two strongest saturated colors as `--accent-1` (primary/brand) and `--accent-2` (complement/secondary). If only one strong color is found, auto-generate the second by rotating hue +20–40° toward warm or cool based on the first's temperature — stay within the 60-30-10 aesthetic, don't introduce a third color just because the site has one.
4. **Diff-propose.** Before committing, show the user a one-line proposal: *"Extracted `#F3A950` / `#F38150` from acme.xyz — apply as accent pair?"* via `AskUserQuestion` with options `["Apply", "Swap primary/secondary", "Try different colors", "Cancel — use style default"]`.
5. **Cite** the source URL in the Step 6 generation recap under an "Accent source" line.

Fallback behavior: if any step fails (fetch blocked, no colors found, extracted colors fail basic contrast against `--canvas`), fall back to option 1 and note which step failed in the recap. Never silently ship a broken extraction — either the user sees the proposed pair, or they see the fallback.

### Step 5 — Dimensions (width-only)

Fire `AskUserQuestion`. Question = "What width do you need?" — options = `["Wide (1920w, default)", "Social (1080w)", "Blog (1080w)", "Square (1080w)", "Custom width"]`. Height is never asked — the canvas grows to fit content, no bottom padding. Default one-shot width depends on the chosen canvas: bento-box / dashboard / poster default to **1920**; editorial defaults to **1280**. Bento-box never goes below 1440. Editorial never goes below 720.

### Step 6 — Generate

Write HTML, report paths and key decisions in 4–6 bullets (template, style, accent colors + source if brand-searched, width, section list).

### Step 7 — Iteration loop

Accept natural-language edits; regenerate; ask "What else?"

### Step 8 — Export

On completion signal (`done`, `export`, `looks good`, `ship it`, `give me the PNG`), run the export chain in §8.

### AskUserQuestion pattern

Keep options short and concrete — each label under ~40 chars. Never chain multiple questions into one call unless truly independent.

---

## 6. Generation Rules

### HTML skeleton

Every output is a single self-contained `.html` file with:

- `<!DOCTYPE html>` + `<html lang="...">`
- `<meta charset>`, `<meta viewport>`
- Google Fonts `<link>` for the exact pair the style specifies
- Phosphor Icons CDN `<link>` whenever icons are used **OR creator tools are included** (required so the toolbar buttons render)
- All CSS inlined in a single `<style>` block
- All JS (if any) inlined in a single `<script>` block
- No external image hosts except Iconify API and user-provided image URLs
- A root `.infographic-canvas` element with a fixed `max-width` per the chosen width preset and **no fixed aspect-ratio or height** — height grows with content
- **In Claude Code context (required, no exceptions):** a `<div class="creator-tools" data-creator-tools>` block injected before `</body>` containing the accent color editor, inline text editing (`e` toggle), Save / Revert, undo/redo persistence, and floating export toolbar, exactly as specified in `references/creator-tools.md`. Omit only when the user explicitly asks for a clean / embed-ready HTML.
- **In Claude Code context (required):** the viewer-features script block from `references/viewer-features.md` (hover tooltips, animated number counters, scroll-triggered reveals, expandable sections, optional dark/light toggle), gated by the feature flags noted in the generation recap. See §9 for the full inclusion policy. Generation MUST load `references/creator-tools.md` and `references/viewer-features.md` before emitting HTML in Claude Code context.

### Canvas sizing

Width-only. Height is content-driven — the canvas grows to fit its sections, then stops. No fixed aspect ratio, no trailing blank space at the bottom.

| Use case | Width |
|----------|-------|
| Wide (default) | 1920 |
| Presentation | 1920 |
| Social | 1080 |
| Blog | 1080 |
| Square | 1080 |
| Custom | user-specified |

Default: **1920 width, content-driven height.** Bento-box layouts require 1920+ — they collapse poorly under that.

Implementation: the `.infographic-canvas` root gets `width: 100%; max-width: <chosen>px` and no `aspect-ratio` / no fixed `height`. Set `min-height: 100vh` only if you want the canvas to at least fill the viewport on short content.

### Hard rules

- **No emoji. Ever.** Not in headers, labels, bullets, icons, tooltips. Use Phosphor Bold or Iconify.
- **No em dashes or en dashes in rendered text.** Em dash (`—`, U+2014) and en dash (`–`, U+2013) are AI-output tells and must never appear in the generated infographic copy — headlines, body, captions, tooltips, source citations, signal evidence, anything. Use a regular hyphen (`-`), comma, period, parentheses, or restructure the sentence. This applies to **content Claude generates**, not to this skill file's prose. Inline editing strips dashes silently the same way emoji are stripped.
- **Exactly two fonts per infographic.** Display font for hero title only. Body font for everything else (bold/caps for headers, regular for body).
- **One accent color pair per infographic**, unless the content genuinely needs two (e.g., comparing two brands). Use 60-30-10: 60% canvas, 30% structural neutrals, 10% accent.
- **Never single-sided thick borders.** No `border-top: 3px solid accent`, no accent bar on one edge. Always full-perimeter or none. Use gradient borders for emphasis.
- **Uppercase all headers and labels.** Body text stays sentence case.
- **Gradient text is for titles and headers only.** Never for body copy.
- **Responsive scaling**: the canvas scales to the viewport width; height always follows content.
- **Dark mode is default.** Light mode on explicit request only.
- **4px grid.** All spacing tokens, font sizes, node dimensions, and SVG coords must be multiples of 4. Existing `--gap-*` / `--pad-*` / `--radius-*` variables already comply — don't override them to odd values. This applies at generation time; the viewer's responsive scaling can still produce sub-pixel values at render.
- **Density budgets.** Enforce the cap below at generation time — past the cap, either split into a second infographic or promote detail into a secondary cheatsheet card. Infographics are allowed to be dense (unlike technical diagrams), but every canvas/snippet still has a ceiling:

  | Canvas or snippet | Primary node / card cap | Accent emphases | Notes |
  |---|---|---|---|
  | `bento-box` | ≤ 1 hero + 11 secondary cards (12 cells total) | ≤ 3 (hero counts) | past 12 cells → split into a second bento infographic |
  | `statistical`, `dashboard` | ≤ 12 KPI cards / panels | ≤ 2 "hero" cards with accent fill | split grid by category if over |
  | `grid-cards`, `cheatsheet` | ≤ 16 cards per grid | ≤ 3 accented | break into sub-sections past 16 |
  | `process-flow`, `journey-path`, `funnel` | ≤ 9 steps | 1 "primary path" accent | 10+ steps → split into phases |
  | `flowchart`, `mind-map`, `fishbone` | ≤ 18 nodes | ≤ 2 | deeper trees → collapse leaves into groups |
  | `timeline`, `roadmap` | ≤ 12 milestones per spine | ≤ 2 | more → split by year / phase |
  | `ecosystem-overview`, `geographic` | ≤ 24 logos / regions | n/a | groups/categories above that |
  | `comparison` | ≤ 4 options | 1 "recommended" | 5+ → `feature-table` variant only |
  | `quadrant`, `venn`, `iceberg`, `pyramid`, `circular-flow`, `anatomical` | ≤ 9 labeled zones | ≤ 2 | any more → switch layouts |
  | `list` | ≤ 14 items | ≤ 3 | or break into a 2-column list |

- **Legend placement.** When a visualization needs a legend (color mapping, node-role table, chart series), render it as a horizontal strip at the bottom of the section it belongs to — never floating inside the canvas, never at the top. Pattern in `references/elements/layout.md` under "Legend strip". Separate from the content above with a hairline `color-mix(in srgb, var(--text-muted) 30%, transparent)` 1px divider. Expand the section's height to accommodate it; don't steal space from the visualization.
- **Callout / annotation limits.** If using the `annotation` element (see `references/elements/annotation.md`), cap it at 2 callouts per infographic and keep leaders outside the primary content bounds. Callouts annotate; they never duplicate what a label already says.
- **Bento-box uses fluid grid, not pixel lock.** Bento has no cross-cell connectors by design — the pixel-locked rule below does NOT apply. Use `display: grid` with `repeat(4, 1fr)` (or 6) and let cards reflow within their span. If a layout needs arrows between cards, it's not bento — pick a pixel-locked layout instead.
- **Pixel-locked sections for cross-cell connectors.** Any section that draws arrows, leaders, or overlays that must align to specific cell edges (swimlane handoffs, flowchart edges, anatomical pointers, quadrant axis callouts, annotation leaders into the grid) MUST be laid out pixel-locked, not responsively. **Infographics are posters, not web pages — we do not care about fluid reflow.** The enclosing section gets a fixed `width` and `height` in px, children inside it use absolute `top/left/width/height` in px on a 4px grid, and any overlay SVG uses `viewBox="0 0 <W> <H>"` with `preserveAspectRatio="none"` and explicit `width="<W>" height="<H>"` matching the container 1:1 — so SVG user units map to container pixels directly. Arrow endpoints are hand-authored px coordinates that land on cell edges (not cell centers, not interiors), and SVG `<marker refX="<markerWidth>">` so the arrowhead tip sits exactly at the path endpoint. To fit the infographic inside smaller viewports, wrap the whole canvas (or just the pixel-locked section) in a scaler:

  ```css
  .poster-scale-wrap {
    transform-origin: top left;
    /* JS sets transform: scale(min(vw/W, vh/H, 1)) on load + resize */
  }
  ```

  Do NOT try to make the grid itself responsive with `1fr` / `minmax` / `aspect-ratio` when connectors are involved — arrow geometry and cell geometry will desync. Fluid reflow is reserved for sections that are purely flow-of-text or unordered card grids with no overlays.

### Image assets

When the user provides logo URLs or image URLs, use them directly in `<img>` tags with appropriate `alt` text. When not provided, leave a styled placeholder (dashed border, centered label) — do not invent image URLs.

---

## 7. Iteration Grammar

Accept these command types without asking:

| Command type | Example | Response |
|--------------|---------|----------|
| Content edit | "change team from 20% to 15%" | Edit HTML, regenerate, refresh |
| Layout edit | "swap chart and timeline" | Restructure sections |
| Style edit | "more orange, less teal" | Shift accent pair |
| Dimension edit | "make it landscape" | Reset canvas + reflow |
| Section-specific | "vesting section is cramped" | Adjust just that section |
| Font override | "use Orbitron for the title" | Swap display font |
| Density | "make it more compact" | Tighten spacing tokens |

After each iteration, confirm in one line what changed. Don't narrate every step.

---

## 8. Export Chain

When the user signals completion (`done`, `export`, `looks good`, `ship it`, `give me the PNG`):

```
Output/
├── <name>.html   (always produced)
└── <name>.png    (via Playwright, 2x DPR)
```

Run the export script:

```bash
python scripts/export.py --png output/<name>.html
```

### Output messaging

```
Exported:
  HTML: output/<name>.html
  PNG:  output/<name>.png  (1080w × auto @ 2x)
```

The HTML is always the canonical source of truth.

See `references/export/png-export.md`, `references/export/figma-import.md` for mechanics.

---

## 8.5 Standalone Section Extraction

After the §8 export recap prints, fire an `AskUserQuestion` to offer standalone section extraction:

- Question: *"Extract each section as its own standalone infographic?"*
- Header: `Extract sections`
- Options:
  1. `Yes — extract all sections`
  2. `Pick specific sections`
  3. `No, I'm done`

On **Pick specific**, follow up with a `multiSelect: true` `AskUserQuestion` listing every section in the final infographic (using the existing section IDs from §9 creator-tools). The user picks which to extract.

### What each standalone file contains

For every selected section, write a new self-contained HTML to:

```
./output/<kebab-name>-<section-id>.html
```

Each standalone file is a full, independent infographic:

- Same style + accent pair + width + fonts + viewer features as the parent — reuse the exact design tokens from §6, do not re-ask any §5 questions.
- **All of that section's content, full-detail.** No truncation, no summarization — every data point, sub-element, caption, annotation, and chart label that was in the parent section is preserved. Supporting details that lived alongside the section in the parent (legends, footnotes, axis labels) travel with it.
- The section's own header becomes the hero title of the standalone. The parent infographic's title becomes a small uppercase eyebrow label above the hero.
- Creator-tools included per §9 inclusion policy (Claude Code = yes, agent / clean export = no).
- Canvas sizing rules from §6 apply — width fixed to the parent's width, height content-driven.

### Export each standalone

For every file written, run:

```bash
python scripts/export.py --png output/<kebab-name>-<section-id>.html
```

Same export chain as §8 — HTML always, PNG via Playwright.

### Consolidated recap

After every selected section has been written and exported, print one single recap listing all the produced paths, e.g.:

```
Standalone sections:
  output/aiz-tokenomics-allocation.html       +  .png
  output/aiz-tokenomics-vesting.html          +  .png
  output/aiz-tokenomics-utility.html          +  .png
```

Section IDs are taken from the `data-section-id` attributes already stamped onto section elements by the creator-tools block (see `references/creator-tools.md`). Do not invent a new tagging scheme.

### When to skip §8.5

- Agent contexts where no follow-up turn is possible (§11).
- The user's completion signal already included `no extras`, `just the main one`, `skip extraction`, or similar.

---

## 8.6 Signal Sheet

A *signal* is the hidden derived insight a viewer would miss by reading the presented data alone — derived math, comparative weight, or second-order consequence. The signal sheet is a sibling infographic that surfaces these insights with citations and shown calculations.

Fire **after** §8.5 standalone extraction completes (or is skipped), **before** §13 Closing Tip. Full reference: `references/templates/_signals.md`.

### Sub-flow

1. **Opt-in question.** Fire `AskUserQuestion`:
   - Question: *"Generate a signal sheet — derived insights from the same data?"*
   - Header: `Signal sheet`
   - Options: `["Yes — generate signal sheet", "No, I'm done"]`
   - On **No** → skip to §13.

2. **Comparative sourcing decision** — only fire if the data has ≥1 point where peer benchmarks would add value (e.g., vesting cliffs, allocation %s, supply caps, growth rates). If no comparative-eligible points exist, skip this question and go straight to step 3.
   - Question: *"Comparative signals need peer/benchmark data. How should I source it?"*
   - Header: `Benchmarks`
   - Options:
     1. `I'll provide` — follow up with a free-text ask for peer data
     2. `Web search (slower, more tokens)` — Claude runs targeted searches, cites source domains
     3. `Skip comparative — derived + causal only`

3. **Two-pass extraction** per `references/templates/_signals.md` — Pass 1 drafts up to ~15 candidates with source citations and confidence; Pass 2 re-reads cold against source data and rejects anything that doesn't reconcile or drops below `high` confidence. Surviving signals capped at **9 total, max 3 per lens (Derived / Comparative / Causal)**.

4. **Thin-data fallback.** If <3 high-confidence signals survive Pass 2:
   ```
   Signal sheet: skipped — not enough derivable signals from the provided data.
   ```
   No file written. Continue to §13.

5. **Write `./output/<kebab-name>-signals.html`** using the cheatsheet `signals-variant` (see `references/templates/cheatsheet.md` §Signals variant). Reuse style, accent pair, fonts, width, viewer features, creator-tools inclusion from the main infographic — **never re-ask any §5 questions**.

6. **Export PNG**: `python scripts/export.py --png output/<kebab-name>-signals.html`.

7. **Recap + merge tip:**
   ```
   Signal sheet:
     HTML: output/<kebab-name>-signals.html
     PNG:  output/<kebab-name>-signals.png

   TIP: If all signals look accurate, ask "merge signals" to append them
        to the main infographic as a new section.
   ```

8. §13 Closing Tip prints last, regardless.

### Merge behavior

Triggered when the user says `merge signals`, `merge them`, `merge if accurate`, or similar:

1. Read the live `<kebab-name>.html` and the signals from `<kebab-name>-signals.html`.
2. Append a new `Signals` section as the final section of the canvas, using the same grouped-3-column structure as the standalone sheet.
3. Write to a **new variant file**: `./output/<kebab-name>-merged.html`. The original `<kebab-name>.html` is preserved untouched.
4. Export PNG: `python scripts/export.py --png output/<kebab-name>-merged.html`.
5. Recap:
   ```
   Merged variant:
     HTML: output/<kebab-name>-merged.html
     PNG:  output/<kebab-name>-merged.png
   ```
6. Fire `AskUserQuestion`:
   - Question: *"Replace the main infographic with the merged variant?"*
   - Header: `Replace main`
   - Options: `["Replace main", "Keep both"]`
   - On **Replace main**: copy `<kebab-name>-merged.html` over `<kebab-name>.html` and `<kebab-name>-merged.png` over `<kebab-name>.png`. Confirm in one line.
7. §13 Closing Tip prints last.

### Confidence tiers

Confidence is used **only for filtering** during Pass 2 — never displayed in the rendered sheet. Low/medium-confidence candidates are dropped, not annotated.

### When to skip §8.6

- The user's completion signal included `no signals`, `skip signals`, or similar.
- Thin-data fallback fires inside the flow (handled at step 4).

---

## 9. Interactive HTML Features

Two categories of features can be included in generated HTML: **viewer features** (stay in the final export, enhance the viewing experience) and **creator tools** (authoring aids that get stripped automatically at export time). Both are drop-in and work with the export pipeline.

### Viewer features — see `references/viewer-features.md`

- **Responsive scaling** — canvas scales to viewport, aspect preserved
- **Hover tooltips** — on chart segments, timeline nodes, KPI cards
- **Animated number counters** — KPIs count up on scroll into view
- **Scroll-triggered section reveals** — fade/slide in per section
- **Expandable detail sections** — for dense infographics
- **Dark/light mode toggle** — on explicit request only

All viewer features freeze to final state during PNG export — the exporter forces counters to target value, reveals to visible, expandables to open.

### Creator tools — see `references/creator-tools.md`

- **Inline text editing** — `e` toggles `contenteditable`, emoji stripped silently, headers stay uppercase via CSS.
- **Accent color editor** — two pickers for `--accent-1` / `--accent-2` plus a preset palette strip; recolors the whole infographic via CSS variables.
- **Forgiving persistence** — localStorage autosave (survives refresh), `Ctrl+Z` / `Ctrl+Shift+Z` undo/redo, `Ctrl+S` saves via File System Access API (Chromium) or Clean Download fallback, Revert button discards all edits.
- **Floating toolbar** — Edit / Color / Save / Revert / Copy / Clean HTML. Every button shows its action name next to the icon. **No in-browser PNG button** — after Save, the user asks Claude to re-export the PNG via `scripts/export.py` (Playwright). A small hint chip above the toolbar reminds the user of this flow.
- **Keyboard shortcuts** — `e` edit, `Ctrl+Z/Shift+Z` undo/redo, `Ctrl+S` save.

All creator-tool elements carry `data-creator-tools`. The exporter hides them before screenshotting, so they never appear in PNG output. A "Clean Download" button produces a stripped-HTML copy for embedding. In-browser edits only land in PNG after the user hits Save (or Clean Download) — the exporter reads from disk, not from the live DOM.

All creator-tool CSS uses hardcoded hex fallbacks inside `var()` calls so the toolbar and color editor render visibly on any style, even ones that don't define `--elevated`, `--accent-1`, or `--text-secondary`.

### Inclusion policy

| Context | Viewer features | Creator tools |
|---------|-----------------|---------------|
| Claude Code iteration | ✓ | ✓ |
| Claude Code one-shot | ✓ | ✓ |
| Agent output (OpenClaw, Hermes) | ✓ | ✗ |
| "Final" / "clean" / embed-ready export | ✓ | ✗ |

---

## 10. Output Path Conventions

- Write HTML to `./output/<kebab-name>.html` relative to the current working directory.
- If `./output/` doesn't exist, create it first.
- Name files after the primary subject (e.g., `aiz-tokenomics.html`, `abstract-ecosystem.html`), not generic names like `infographic.html`.
- After writing, attempt to auto-open in the default browser:
  - Windows: `start <file>` via shell
  - macOS: `open <file>`
  - Linux: `xdg-open <file>`

---

## 11. Platform-Specific Behavior

### Claude Code (primary target)

- Use `AskUserQuestion` for guided mode selections (tappable in terminal)
- Write to working directory
- Auto-open browser after write
- Iterate via chat; re-write file; user refreshes browser

### Agent context (OpenClaw, Hermes)

- Default to one-shot mode
- **Skip §1.5 Canvas Pick** — default to `bento-box` canvas, do not open the gallery, do not fire the canvas `AskUserQuestion`. If the agent caller named a different canvas in the prompt, honor it.
- **§8.5 Standalone Section Extraction** — offer only if the agent host supports follow-up turns; otherwise skip silently
- **§8.6 Signal Sheet** — auto-generate by default (no opt-in possible). Skip the comparative-sourcing question entirely (no user prompt, no web-search latency in agent contexts). Never offer merge — always ship the twin (`<name>.html` + `<name>-signals.html` + PNGs). Thin-data fallback: skip silently.
- The §13 Closing Tip still prints at the end of the final message
- If content is incomplete, ask via the agent's chat channel
- Export scripts run automatically after generation
- Output file to the configured workspace directory

---

## 12. Development & Testing Notes

The skill can be tested without installing:

```
Read ./create-infographics/SKILL.md and follow its instructions
to create a <type> infographic for <project>. <data>
```

Evals for trigger accuracy live at `evals/evals.json`. Run `run_loop.py` from the skill-creator plugin to iterate the description copy against them.

Install via `package_skill.py` when ready for auto-triggering.

---

## Quick Reference Card

| Situation | What to do |
|-----------|------------|
| User pastes structured tokenomics data | Load `templates/token-economics.md`, one-shot, bento-box canvas |
| User says "help me make an infographic" | Guided mode, start at intake → §1.5 canvas pick |
| User says "cheatsheet for X" | Load `templates/cheatsheet.md` (bento-box canvas) |
| User asks about ecosystem/partners/integrations | Load `templates/ecosystem-overview.md` (bento-box canvas) |
| User asks for a long-form deep-dive / "how it really works" | Pick `editorial` canvas |
| User asks for a stats/metrics snapshot | Pick `dashboard` canvas |
| User asks for "anatomy of X" / framework / mechanism | Pick `poster` canvas, hero centerpiece is one big snippet |
| User wants a release recap, product overview, or dense multi-section snapshot | `bento-box` canvas (1920w) |
| User wants a positioning / 2×2 matrix | `poster` canvas + `quadrant` snippet as centerpiece |
| User wants a multi-actor process / handoff flow | `poster` canvas + `swimlane` snippet as centerpiece |
| User wants a caveat or citation on a data point | Use `references/elements/annotation.md` (max 2 callouts) |
| User wants a style that isn't MVP | Substitute `aizfographics-style` and note |
| User asks for vector/Figma | Point to `references/export/figma-import.md` (html.to.design plugin) |
| User hasn't given data | Ask for it — do not fabricate |
| After export, want hidden insights surfaced | §8.6 Signal Sheet — load `references/templates/_signals.md` |
| User says "merge signals" | Run §8.6 merge flow → write `<name>-merged.html`, ask Replace/Keep |

---

## 13. Closing Tip (always printed last)

The final message of every completed skill run MUST end with this single line, verbatim:

```
TIP: Use the html.to.design Figma plugin to get a fully editable infographic in Figma.
```

Rules:

- Print it after §8 export recap AND (if run) after §8.5 standalone extraction recap — it is the last line of the skill's output.
- Print it regardless of whether standalone extraction or signal sheet was run.
- Print it even in agent contexts.
- Single line. No bullet, no heading, no emoji, no extra prose around it.
