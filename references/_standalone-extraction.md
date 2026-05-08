# Standalone Section Extraction

Loaded only when §8.5 fires. Walks the user through extracting each section of a finished infographic into its own self-contained HTML + PNG.

## Trigger and prompt

Fire `AskUserQuestion`:

- Question: *"Extract each section as its own standalone infographic?"*
- Header: `Extract sections`
- Options:
  1. `Yes — extract all sections`
  2. `Pick specific sections`
  3. `No, I'm done`

On **Pick specific**, follow up with a `multiSelect: true` `AskUserQuestion` listing every section in the final infographic (using the existing `data-section-id` attributes from `references/creator-tools.md`). The user picks which to extract.

## What each standalone file contains

For every selected section, write a new self-contained HTML to:

```
./output/<kebab-name>-<section-id>.html
```

Each standalone is a full, independent infographic. Required properties:

- **Same style + accent pair + width + fonts + viewer features as the parent.** Reuse the exact design tokens from §6 — do not re-ask any §5 questions.
- **All of that section's content, full-detail.** No truncation, no summarization — every data point, sub-element, caption, annotation, and chart label that was in the parent section is preserved. Supporting details that lived alongside the section in the parent (legends, footnotes, axis labels) travel with it.
- **Header → hero.** The section's own header becomes the hero title of the standalone. The parent infographic's title becomes a small uppercase eyebrow label above the hero.
- **Creator-tools per §9 inclusion policy** (Claude Code = yes, agent / clean export = no).
- **Canvas sizing per §6.** Width fixed to the parent's width, height content-driven.

## Export each standalone

For every file written, run:

```bash
python scripts/export.py --png output/<kebab-name>-<section-id>.html
```

Same export chain as §8 — HTML always, PNG via Playwright.

## Consolidated recap

After every selected section has been written and exported, print one single recap listing all the produced paths:

```
Standalone sections:
  output/aiz-tokenomics-allocation.html       +  .png
  output/aiz-tokenomics-vesting.html          +  .png
  output/aiz-tokenomics-utility.html          +  .png
```

## Section IDs

Section IDs are taken from the `data-section-id` attributes already stamped onto section elements by the creator-tools block (see `references/creator-tools.md`). **Do not invent a new tagging scheme.**

## When to skip

- Agent contexts where no follow-up turn is possible (per §11).
- The user's completion signal already included `no extras`, `just the main one`, `skip extraction`, or similar.
