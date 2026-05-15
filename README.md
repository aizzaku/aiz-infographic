# aiz-infographic

A Claude Code skill that turns structured data into self-contained HTML infographics with reliable PNG export. Built on a 5-layer reference system: **canvases × snippets × styles × elements × templates**.

## Key Features

- **4 canvases × 10 styles × 24 snippets**, plus **10 ready-made templates** for common content types (allocation breakdown, ecosystem overview, cheatsheet, concept explainer, game overview, distribution guide, collection showcase, how-it-works, report, game mechanics).
- **One-shot and guided modes.** Tappable `AskUserQuestion` selection in Claude Code; auto-defaults in agent contexts (OpenClaw, Hermes).
- **Brand-color extraction** from a URL or web search. Or hand it the hex pair directly.
- **In-browser creator tools** (inline text edit, accent color editor, undo/redo, save/revert) injected into every Claude Code output and stripped automatically at PNG export.
- **Viewer features** (hover tooltips, animated counters, scroll-triggered reveals, expandable sections) preserved in the PNG snapshot.
- **Optional signal sheet** that surfaces derived insights (math, comparisons, second-order consequences) from the same source data, plus standalone-section extraction for any single panel.
- **html.to.design Figma round-trip** for fully editable vector files.
- **Width-only sizing.** The canvas grows to fit content. No trailing blank space.

## Installation

### Full install — skill + PNG export dependencies

```bash
curl -fsSL https://raw.githubusercontent.com/aizzaku/aiz-infographic/main/install.sh | bash
```

Installs the skill via `npx skills`, then installs the Python Playwright package and downloads the Chromium browser used for PNG export. Requires Node.js and Python 3.9+ on your PATH.

### Skill only

```bash
npx skills add https://github.com/aizzaku/aiz-infographic
```

### PNG export (separate, if you skipped the full install)

```bash
pip install "playwright>=1.40.0"
playwright install chromium
```

## Quick Usage

Once installed, trigger the skill in Claude Code with any of:

```
make an infographic for this tokenomics: <paste data>
cheatsheet for the Solana validator economy
visualize this ecosystem: <paste partner list>
turn this roadmap into a visual
```

The skill auto-detects one-shot vs guided mode based on whether you provided enough data and named a clear type. Force one-shot with phrases like `just make it`, `here's everything`, or `quick`. Force guided with `help me`, `walk me through`, or `what canvas`.

When done iterating, say `done`, `export`, `looks good`, or `ship it` to trigger the export chain.

## Output Structure

```
output/
├── <kebab-name>.html           # canonical, self-contained
├── <kebab-name>.png            # 2x DPR via Playwright
├── <kebab-name>-signals.html   # optional signal sheet
├── <kebab-name>-signals.png
└── <kebab-name>-merged.html    # optional: signals appended to main
```

The HTML is the canonical source of truth. PNG is a render of it. SVG is produced by running the HTML through the html.to.design Figma plugin.

## Reference Layers

| Layer | Lives in | Role |
|---|---|---|
| **Canvas** | `references/canvases/<name>.md` | Page architecture: header, hero, footer, slot grid. (`bento-box`, `editorial`, `dashboard`, `poster`) |
| **Snippet** | `references/snippets/<name>.md` | Embeddable section pattern: timeline spine, fishbone, kpi-strip, sankey-flow, network-graph, etc. |
| **Style** | `references/styles/<name>.md` | Visual identity: colors, fonts, spacing tokens. (`aizfographics-style` default) |
| **Element** | `references/elements/<name>.md` | Atomic UI primitives: text, charts, icons, connectors. |
| **Template** | `references/templates/<name>.md` | High-level preset = canvas + style + snippet picks for a content type. |

Defaults: canvas `bento-box`, style `aizfographics-style`, width `1920`. Editorial canvas defaults to `1280`.

## Configuration

Defaults and routing rules live in [aiz-infographic/SKILL.md](aiz-infographic/SKILL.md). To add a new visual style, copy `references/styles/_custom-template.md`, fill in the tokens, and reference it by name in your request.

## Credits

- Install pattern modeled after [baoyu-skills](https://github.com/jimliu/baoyu-skills) by Jim Liu.
- Distributed via [skills.sh](https://skills.sh).

TIP: Use the html.to.design Figma plugin to get a fully editable infographic in Figma.

NOTE: If you liked this skill and it helped, I would appreciate a star on aiz-infographic Github. Thank you.
