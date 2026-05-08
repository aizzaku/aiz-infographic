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

## Out of Scope

This skill does NOT:

- Generate animated or video infographics — output is static HTML/PNG.
- Build live-data dashboards — output is a fixed snapshot, not a connected dashboard.
- Produce slide decks or presentations — use the `pptx` skill.
- OCR scanned source documents — provide structured data, not images of data.
- Create technical architecture, UML, or sequence diagrams — use a diagram tool.
- Generate SVG / Figma files directly — vector workflow goes through html.to.design (see §13).
- Fabricate financial numbers, dates, or partner lists when missing (see §4).

If the request is one of the above, route to the appropriate skill or ask for the data shape this skill can render.

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
| Standalone section extraction (§8.5) | `references/_standalone-extraction.md` (loaded only when §8.5 fires) |
| Brand color extraction (§5 Step 4 option 2 or 3) | `references/brand-extraction.md` (loaded only when option 2 or 3 chosen) |
| Pixel-locked sections (cross-cell connectors) | `references/elements/connectors.md` §Pixel-locked sections — already pulled in via the `connectors` element load when any snippet using arrows/leaders is selected |

### Typical load order for a one-shot tokenomics request:

1. `references/templates/token-economics.md`
2. `references/canvases/<canvas named by template>.md` (usually `bento-box`)
3. `references/styles/aizfographics-style.md`
4. Each snippet the template names — load from `references/snippets/<name>.md`. Typical for tokenomics: `statistical`, `comparison`. Donut/vesting-bar are inline `<svg>` patterns under `references/elements/charts.md` + `data-widgets.md`.
5. Each element the template names: `charts.md`, `data-widgets.md`, `text.md`, `layout.md`, `connectors.md`, `decorative.md`
6. **In Claude Code context**, also load `references/creator-tools.md` and `references/viewer-features.md` — these are mandatory inputs to the HTML skeleton (see §6).

Eight to ten files total in Claude Code, six to eight in agent contexts. Do not read other templates, other canvases, or other styles unless the user's request demands them.

**Canvas snippet routing hints:**
- Token flows / allocation flows with value transfer → `sankey-flow` (needs D3 + d3-sankey in `<head>`)
- Ecosystem/partner/relationship maps with 5–20 entities → `network-graph` (needs D3 in `<head>`)
- Multi-axis protocol comparison → radar chart in `charts.md` (needs Chart.js in `<head>`)
- Hierarchical allocation with 6+ segments → treemap chart in `charts.md` (needs D3 in `<head>`)
- 3-variable scatter → bubble chart in `charts.md` (needs Chart.js in `<head>`)
- Holder/allocation distribution as a grid → waffle chart in `charts.md` (raw canvas, no CDN)

### Available references

- **Canvases (4):** `bento-box` (default), `editorial`, `dashboard`, `poster`.
- **Styles (10):** `aizfographics-style` (default), `clean-minimal`, `blueprint`, `editorial`, `corporate`, `cyberpunk`, `chalkboard`, `hand-drawn`, `retro`, `_custom-template` (scaffold).
- **Snippets (24):** `statistical`, `grid-cards`, `process-flow`, `timeline`, `comparison`, `hierarchical`, `list`, `roadmap`, `funnel`, `flowchart`, `dashboard`, `mind-map`, `journey-path`, `pyramid`, `circular-flow`, `iceberg`, `fishbone`, `venn`, `anatomical`, `geographic`, `quadrant`, `swimlane`, `sankey-flow`, `network-graph`. Each declares its slot fit and density cap. Bento-box is canvas-only — no `bento-box` snippet.
- **Templates (10):** `token-economics`, `ecosystem-overview`, `cheatsheet`, `crypto-explainer`, `game-overview`, `airdrop-guide`, `nft-showcase`, `how-it-works`, `report`, `game-mechanics`.
- **Elements (10):** `charts`, `text`, `layout`, `connectors`, `icons`, `data-widgets`, `decorative`, `maps`, `comparison`, `annotation`.

Unmapped content type → §1.5 canvas pick + snippets that match the content shape. Unlisted style → copy `_custom-template.md`, fill, note the substitution.

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
2. **Pick brand color (auto-search)** — Claude web-searches for the brand and extracts a primary pair.
3. **Match a brand URL (extract)** — the user gives a site URL; Claude scrapes a primary pair.
4. **I'll give you the hex values** — follow up with a free-text ask for the hex pair.
5. **Surprise me** — Claude picks a pair that fits the content topic.

For options 2 and 3, load `references/brand-extraction.md` and follow the flow there. Cite the source in Step 6's recap. Never silently ship a broken extraction — either the user sees the proposed pair, or they see a fallback.

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
- **Canvas library `<script>` tags (conditional — add only when the output uses that element):**
  - Chart.js v4 (`https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js`) when using `radar` or `bubble` charts
  - D3 v7 (`https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js`) when using `treemap` chart, `sankey-flow` snippet, or `network-graph` snippet
  - d3-sankey (`https://cdn.jsdelivr.net/npm/d3-sankey@0.12/dist/d3-sankey.min.js`) after D3, only for `sankey-flow`
  - Never add these globally — only when the specific element type is present in the output
- All CSS inlined in a single `<style>` block
- All JS (if any) inlined in a single `<script>` block (canvas chart scripts may be multiple `<script>` blocks, one per chart element, each IIFE-wrapped)
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

### Universal output rules

These apply to every infographic regardless of style or canvas. They are NOT duplicated in style or canvas reference files — this is the only home.

- **No emoji. Ever.** Not in headers, labels, bullets, icons, tooltips. Use Phosphor Bold or Iconify.
- **Never wrap icons in bg or borders.** No icon badge, no bordered tile around an icon, no circular bg behind an icon — anywhere. Icons render as glyphs directly on the surface. Increase size or change color for emphasis, never give an icon its own container. Full rule + examples in `references/elements/icons.md`.
- **No em dashes or en dashes in rendered text.** Em dash (`—`, U+2014) and en dash (`–`, U+2013) are AI-output tells and must never appear in the generated infographic copy — headlines, body, captions, tooltips, source citations, signal evidence, anything. Use a regular hyphen (`-`), comma, period, parentheses, or restructure the sentence. This applies to **content Claude generates**, not to this skill file's prose. Inline editing strips dashes silently the same way emoji are stripped.
- **4px grid.** All spacing tokens, font sizes, node dimensions, and SVG coords must be multiples of 4. Existing `--gap-*` / `--pad-*` / `--radius-*` variables already comply — don't override them to odd values. Applies at generation time; the viewer's responsive scaling can still produce sub-pixel values at render.
- **Never single-sided thick borders.** No `border-top: 3px solid accent`, no accent bar on one edge. Always full-perimeter or none. Use gradient borders for emphasis.
- **Responsive scaling.** The canvas scales to the viewport width; height always follows content. No fixed aspect ratio, no trailing blank.
- **Image assets.** When the user provides logo URLs or image URLs, embed them via `<img>` with appropriate `alt` text. When not provided, leave a styled placeholder (dashed border, centered label) — never invent image URLs.

### Rules that live in reference files (loaded per §3)

- **Style rules** — uppercase headers, exactly two fonts, gradient text titles only, one accent pair, dark mode default → `references/styles/<picked>.md`.
- **Density caps** (cards/steps/nodes/items per snippet, accent emphasis caps per canvas) → each `references/snippets/<name>.md` and `references/canvases/<name>.md` declares its own ceiling. Past the cap, split into a second infographic.
- **Bento fluid-grid rule + no cross-card connectors** → `references/canvases/bento-box.md`.
- **Pixel-locked sections (cross-cell connectors)** → `references/elements/connectors.md` §Pixel-locked sections (covers `flowchart`, `fishbone`, `swimlane`, `anatomical`, `quadrant`, plus annotation leaders into grids).
- **Legend strip placement** → `references/elements/layout.md` §Legend strip.
- **Callout / annotation limits** (max 2 per infographic, leader rules) → `references/elements/annotation.md`.

When a relevant reference file is loaded per §3, treat its rules as binding — they are not optional.

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

Run the export script using the **full absolute path** to the script in this skill's directory (the base dir is always shown at the top of your context as `Base directory for this skill:`):

```bash
python "<skill-base-dir>/scripts/export.py" --png output/<name>.html
```

Concrete example: `python "C:\Users\Aiz\.claude\skills\create-infographics\scripts\export.py" --png output/my-infographic.html`

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

After the §8 export recap prints (and before §8.6), offer standalone extraction. Load `references/_standalone-extraction.md` and follow it.

The non-negotiable rule from that file, repeated here so it isn't lost: **each standalone preserves all of that section's content, full-detail. No truncation, no summarization.** Every data point, sub-element, caption, annotation, and chart label that was in the parent section is preserved. Reuse the parent's style, accent pair, width, fonts, viewer features, and creator-tools inclusion — never re-ask §5 questions.

### When to skip

- Agent contexts where no follow-up turn is possible (§11).
- The user's completion signal already included `no extras`, `just the main one`, `skip extraction`, or similar.

---

## 8.6 Signal Sheet

A *signal* is a hidden derived insight a viewer would miss by reading the presented data alone — derived math, comparative weight, or second-order consequence. The signal sheet is a sibling infographic that surfaces these insights with citations and shown calculations.

Fire **after** §8.5 (or its skip), **before** §13. Full extraction logic (two-pass draft/verify, confidence tiering, lens caps) lives in `references/templates/_signals.md` — load it when this section fires.

### Sub-flow

1. **Opt-in.** `AskUserQuestion`: *"Generate a signal sheet — derived insights from the same data?"* — options `["Yes — generate signal sheet", "No, I'm done"]`. On No → §13.

2. **Comparative sourcing** (only if the data has ≥1 peer-benchmarkable point). `AskUserQuestion`: *"Comparative signals need peer/benchmark data. How should I source it?"* — options `["I'll provide", "Web search (slower)", "Skip comparative — derived + causal only"]`.

3. **Generate** per `_signals.md` (two-pass, max 9 signals / 3 per lens). If <3 high-confidence signals survive Pass 2, print `Signal sheet: skipped — not enough derivable signals from the provided data.` and continue to §13.

4. **Write** `./output/<kebab-name>-signals.html` using the cheatsheet `signals-variant`. Reuse the parent's style, accent pair, fonts, width, viewer features, creator-tools inclusion — **never re-ask §5 questions**.

5. **Export**: `python "<skill-base-dir>/scripts/export.py" --png output/<kebab-name>-signals.html` (use the full absolute path to the skill's script).

6. **Recap + merge tip:**
   ```
   Signal sheet:
     HTML: output/<kebab-name>-signals.html
     PNG:  output/<kebab-name>-signals.png

   TIP: If all signals look accurate, ask "merge signals" to append them
        to the main infographic as a new section.
   ```

### Merge (`merge signals` / `merge them` / `merge if accurate`)

Append the signals as a final section of a **new variant file** `./output/<kebab-name>-merged.html` (the original is preserved). Export PNG. Then `AskUserQuestion`: *"Replace the main infographic with the merged variant?"* — options `["Replace main", "Keep both"]`. On Replace main, copy the merged HTML/PNG over the originals and confirm in one line.

### When to skip

- Completion signal included `no signals`, `skip signals`, or similar.
- Thin-data fallback fires (handled at step 3).

---

## 9. Interactive HTML Features

Two categories — **viewer features** (stay in PNG export, frozen to final state by the exporter) and **creator tools** (authoring aids stripped at export via `data-creator-tools`). Both are drop-in.

- Viewer features (hover tooltips, animated counters, scroll reveals, expandables, dark/light toggle, responsive scaling) → `references/viewer-features.md`
- Creator tools (inline text editing, accent color editor, persistence, floating toolbar, shortcuts) → `references/creator-tools.md`

Both reference files are loaded per §3 in Claude Code context. The full implementation, CSS, JS, and behavioral rules live there — emit the HTML according to those files.

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

Test without installing: `Read ./create-infographics/SKILL.md and follow its instructions to create a <type> infographic for <project>. <data>`. Evals at `evals/evals.json` (run via `run_loop.py` from skill-creator plugin). Install via `package_skill.py` when ready for auto-triggering.

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
