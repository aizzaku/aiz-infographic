# `infographics-studio` — Full Spec (v0.1)

> A new, parallel project to the existing `aiz-infographic` HTML skill. Goal: AI-generated, human-polished editable infographics with a real React-based GUI editor. Distributed as an npm package; runs locally via `npx`.

---

## 0. Context & Why

The current `aiz-infographic` skill (`A:\claude\infographics-skill-revamp-v1\aiz-infographic\SKILL.md`) outputs static, self-contained HTML using a 5-layer reference system (canvas × snippet × style × element × template). It's good for one-shot Claude generation but has hard ceilings:

- **No human edit loop.** Polishing requires re-prompting Claude or hand-editing markup.
- **No reusable typed components.** Snippets are markdown patterns Claude reassembles each run → drift.
- **No ecosystem.** Charts, motion, connectors are hand-rolled; we re-invent what Visx/Recharts/etc. already solve.
- **Output ≡ source.** Editing an HTML artifact is a regen.

A reference exists of someone building React-based **slide** editors. Slides are arguably overkill (Google Slides exists). **Infographics is the better fit**: single-page, dense, design-forward, no good editable open-source tool, and Claude can drive it well.

**Decision:** Keep the current HTML skill as-is for one-shot chat use. Build `infographics-studio` as a separate product with a parallel codebase and lifecycle. The two share aesthetic taste but not source.

### Pros / cons of going React (the original question, summarized)

**Pros**
- Reusable, typed snippet components (Zod props) → reliable Claude composition.
- Tractable editor UX (selection, undo/redo, drag, multi-select) — infeasible on raw HTML.
- Visx, Framer Motion, Tldraw-style libs available.
- Source ≠ output: canonical JSON, rendered to HTML/PNG, round-trippable, diffable, git-friendly.
- Real human-polish loop after Claude generation — the killer feature.

**Cons**
- Distribution friction (install vs static HTML opens anywhere). Mitigated by `npx` MVP.
- More machinery: schema versioning, migrations, autosave, theme system, image handling.
- Heavier runtime in the editor (export artifact stays light).
- Two products to maintain. Accepted explicitly.
- AI editing is a separate large project; deferred to v0.2.

**Net:** worth doing, as a new repo, with a deliberately tight v0.1.

---

## 1. Identity & Scope

| | |
|---|---|
| **Name** | `infographics-studio` |
| **Repo** | new public GitHub repo, **MIT**, actively welcoming PRs |
| **Folder** | new top-level project alongside `aiz-infographic`, separate git history |
| **Audience (v0.1)** | Claude Code power users / skill ecosystem (CLI-comfortable; will run `npx`) |
| **Primary deliverable** | npm package with `bin` entry → `npx infographics-studio` |
| **Output artifacts** | self-contained read-only `.html` + high-fidelity `.png` |
| **Source artifact** | `.infographic.json` (canonical, git-friendly) |
| **License** | MIT |

### Non-goals (v0.1)

- ❌ Tauri desktop binary (deferred to v0.3)
- ❌ Hosted web app, auth, accounts, billing
- ❌ Multi-page docs (deferred to v0.4+, may never ship — slides-overkill risk noted)
- ❌ Cmd+K / AI editing inside the editor (deferred to v0.2)
- ❌ Animated / interactive output (export is static)
- ❌ Plugin folder / hot-loaded community snippets (snippets-as-data only)
- ❌ Markdown / WYSIWYG rich text inside nodes
- ❌ AI image generation
- ❌ URL-paste images
- ❌ Multi-user / realtime collab

---

## 2. Architecture Overview

```
┌────────────────────────────────────────────────────────────────────┐
│  Claude Code (existing skill ecosystem)                            │
│  └─ new skill: emits .infographic.json validated against Zod       │
└────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
                    .infographic.json on disk
                               │
                ┌──────────────┴───────────────┐
                ▼                              ▼
   `npx infographics-studio open`     `npx infographics-studio export`
   ┌──────────────────────────┐       ┌─────────────────────────────┐
   │  Vite + React editor     │       │  Headless Node export       │
   │  - Zustand stores        │       │  - SSR React → HTML         │
   │  - Zod validation        │       │  - Playwright PNG sidecar   │
   │  - Visx charts           │       │                             │
   │  - Autosave to disk      │       │                             │
   └──────────────────────────┘       └─────────────────────────────┘
                                                  │
                                                  ▼
                                       artifact.html  artifact.png
```

### Stack

| Layer | Choice | Rationale |
|---|---|---|
| Build | Vite | Fast HMR, simple config, ESM-native |
| UI | React 18 + TypeScript | Boring, well-supported, Claude-readable |
| Styling | Tailwind v3 | Token-driven, parity with current skill discipline |
| Editor state | Zustand | Tiny, no provider hell, easy undo/redo middleware |
| Doc state | plain JSON + Zod | Single source of truth, runtime-validated |
| Charts | **Visx** (D3 primitives) | Max flexibility, fits bespoke `aizfographics` aesthetic; outputs SVG |
| Drag/resize | `@dnd-kit/core` + custom resize handles | Active, accessible, works with auto-layout |
| Icons | `lucide-react` | Curated, consistent, MIT |
| Image upload | native file input + drag/drop, base64 in JSON | Simple, no asset pipeline at v0.1 |
| Export HTML | `react-dom/server` + inline CSS extraction | Self-contained artifact |
| Export PNG | Playwright (local Node sidecar) | Highest fidelity; matches current skill |
| Schema | **Zod** as single source | TS types derived; JSON Schema exported for Claude prompts |
| Persistence | autosave-to-file (debounced) | Open path → write through; pairs with git |
| Lint/format | ESLint + Prettier + tsc | Standard |
| Tests | Vitest + Playwright (export e2e) | Standard |
| Package mgr | pnpm | Fast, strict |

---

## 3. Document Format (`.infographic.json`)

### Top-level shape (Zod-defined)

```ts
const Doc = z.object({
  docVersion: z.literal(1),
  meta: z.object({
    title: z.string(),
    createdAt: z.string().datetime(),
    updatedAt: z.string().datetime(),
  }),
  theme: z.enum(["aizfographics", "editorial", "<theme-3>"]),
  themeOverrides: ThemeTokensPartial.optional(),  // accent pair etc.
  canvas: z.object({
    type: z.literal("bento-box"),
    grid: z.object({ cols: z.number(), rows: z.number(), gap: z.number() }),
  }),
  scene: SceneNode,  // tree, recursive
});
```

### `SceneNode` (tagged union)

```ts
const SceneNode = z.discriminatedUnion("type", [
  Slot,         // top-level frame, holds snippets
  // Snippets (typed, props validated):
  KpiStrip, Timeline, ComparisonTable, Fishbone, Callout,
  // Primitives (used inside snippets, also valid top-level):
  Text, Stat, Chart, Image, Icon, Group, Spacer,
]);
```

Every node carries:

```ts
{
  id: string,                  // uuid
  type: "<discriminator>",
  layout: {
    auto: boolean,             // default true
    colSpan?: number, rowSpan?: number, order?: number,  // overrides
  },
  props: {...},                // type-specific
}
```

### Snippet prop shapes (v0.1)

```ts
KpiStrip:        { items: { label: string, value: string, delta?: string }[] }
Timeline:        { orientation: "horizontal"|"vertical",
                   events: { date: string, title: string, body?: TextRich }[] }
ComparisonTable: { columns: string[],
                   rows: { label: string, cells: TextRich[] }[] }
Fishbone:        { spine: string,
                   bones: { label: string, causes: string[] }[] }
Callout:         { variant: "info"|"warn"|"highlight",
                   title: string, body: TextRich }
```

Where `TextRich` is plain text + preset emphasis spans:

```ts
TextRich = (string | { emphasis: "highlight"|"accent"|"subtle", text: string })[]
```

No bold/italic/links. No markdown. Discipline by construction.

### Primitive prop shapes

```ts
Text:    { content: TextRich, role: "h1"|"h2"|"h3"|"body"|"label" }
Stat:    { value: string, label: string, trend?: "up"|"down"|"flat" }
Chart:   { kind: "bar"|"line"|"pie"|"area", data: ChartData, options?: ChartOptions }
Image:   { src: string (base64 data URL or sibling path), alt: string,
           fit: "cover"|"contain" }
Icon:    { name: string (lucide id), size: number }
Group:   { children: SceneNode[] }
Spacer:  { size: number }
```

### Migrations

- `docVersion: 1` shipped at v0.1.
- Every bump comes with a migration function `migrateV1toV2(doc) → doc`.
- Loader runs migrations chained from current → latest before validation.
- Editor refuses to save back as a lower version.

### JSON Schema export

The Zod schema is also exported as JSON Schema (via `zod-to-json-schema`) into the package as `schema/v1.json`. The companion Claude skill embeds this in its prompt so generated JSON is valid by construction.

---

## 4. Themes

Three themes ship at v0.1.

```ts
const ThemeTokens = z.object({
  bg: z.object({ canvas: hex, panel: hex, inset: hex }),
  fg: z.object({ primary: hex, secondary: hex, muted: hex }),
  accent: z.object({ primary: hex, secondary: hex }),
  font: z.object({ display: string, body: string, mono: string }),
  radius: z.object({ sm: px, md: px, lg: px }),
  spacing: z.object({ xs: px, sm: px, md: px, lg: px, xl: px }),
  border: z.object({ width: px, style: "solid"|"gradient", colors: hex[] }),
  shadow: z.object({ sm: shadowDef, md: shadowDef, glow: shadowDef }),
});
```

### Shipped themes

1. **`aizfographics`** (default): dark canvas, Bebas Neue display + Montserrat body, single accent pair, gradient borders, glow shadows. Carries the current skill's identity.
2. **`editorial`**: light, serif display (e.g. Fraunces), clean borders, no glow. Print-friendly.
3. **Theme 3 — TBD at design time.** Likely a "tech-doc" / Stripe-press-style flat theme. Decide during impl.

`themeOverrides` lets users tweak the accent pair without forking a theme.

---

## 5. Editor UX

### Window layout

```
┌────────────────────────────────────────────────────────────────────┐
│ Toolbar: [theme switcher] [export ▾] [undo/redo] [autosave indic]  │
├──────────┬─────────────────────────────────────┬───────────────────┤
│ Outline  │                                     │ Inspector         │
│ tree of  │           Canvas (bento-box)        │ props for         │
│ scene    │           live render               │ selected node     │
│ nodes    │                                     │                   │
│          │                                     │                   │
│          │                                     │                   │
└──────────┴─────────────────────────────────────┴───────────────────┘
```

### Interactions

- **Selection.** Click a node → highlights in canvas + outline + inspector.
- **Drag-to-reorder.** Snippets in slots reflow auto-layout; drag handle on each card.
- **Resize.** Edge handles snap to canvas grid (`colSpan`/`rowSpan` overrides).
- **Inline text edit.** Double-click a `Text` node → contenteditable; Tab applies emphasis from a small popover (`highlight` / `accent` / `subtle` / clear).
- **Image upload.** Drag-drop a PNG/JPG/SVG onto an `Image` slot or use file picker; encoded as base64, stored in JSON.
- **Icon picker.** `Icon` inspector field opens a Lucide search.
- **Theme switcher.** Cycles 3 themes; `themeOverrides` panel lets user tweak accent pair.
- **Undo/redo.** Cmd+Z / Cmd+Shift+Z; ring buffer of last 100 doc states.
- **Autosave.** Debounced 500ms; toolbar shows "saved" / "saving…".
- **Keyboard.** Delete, duplicate (Cmd+D), nudge with arrow keys (only when manual override is on).

### Auto-layout with manual overrides

Default: snippets fill the bento grid by `order` and intrinsic `colSpan`/`rowSpan` declared in the snippet schema. User can flip a snippet's `layout.auto = false` and override `colSpan` / `rowSpan` / `order`. Resize and drag handles set these overrides explicitly.

### Inspector panels

One panel component per node `type`; each reads/writes the matching `props` block. Field types map directly (string → text input, enum → select, array → list editor with add/remove). Built mechanically from the Zod schema where possible.

---

## 6. Export

### HTML export

- `react-dom/server.renderToStaticMarkup` against the read-only renderer (no editor code).
- Inline all CSS (Tailwind classes resolved + theme tokens injected as CSS vars).
- Inline all images (already base64 in JSON).
- Optionally embed source as `<script type="application/json" id="infographic-source">` for round-trip re-import. **Default: yes** (cheap, useful, doesn't bloat materially).
- Output: single `.html` file. Opens in any browser, no network calls.

### PNG export

- Playwright local-Node sidecar.
- First run downloads Chromium (~150MB) with progress UI; cached `~/.cache/ms-playwright`.
- Renders the HTML export at `2x` device-pixel-ratio (configurable: `--scale 1|2|3`).
- Output: single `.png`.

### CLI surface

```
npx infographics-studio open <file.json>          # spawn editor
npx infographics-studio export <file.json> --html [--out dir]
npx infographics-studio export <file.json> --png  [--out dir] [--scale 2]
npx infographics-studio export <file.json> --html --png   # both
npx infographics-studio init [--theme aizfographics]      # scaffold a blank doc
npx infographics-studio validate <file.json>              # Zod check, exit code
```

---

## 7. Persistence

- Editor opens a path. **All mutations write through** to that file (debounced 500ms).
- No "unsaved" buffer state; no save button.
- File ops use `fs/promises` from a tiny Node helper exposed to the renderer via Vite's dev-server middleware (or, in the production-built case, a thin Express layer the CLI bin spins up).
- Autosave indicator in toolbar: idle / saving / saved / error.
- Pairs naturally with `git` — user gets free history.

---

## 8. Claude's Role

### v0.1
- **Generate-time only.** A new companion skill (`infographics-studio-doc`) emits `.infographic.json` from a content prompt. Skill prompt embeds the `schema/v1.json` JSON Schema and seed examples from `examples/`.
- User then runs `npx infographics-studio open <file>` and polishes manually.

### v0.2 (planned, not v0.1)
- Selection-driven AI: cmd+K on a node opens a prompt; Claude returns a JSON patch. Capabilities:
  1. Rewrite copy in selected node
  2. Replace a snippet with a different snippet type
  3. Generate a new snippet from a content prompt (insert)
  4. Restyle / retheme selected scope (mutates `themeOverrides` or node-level overrides)
- BYOK: user pastes Anthropic API key; stored in OS keychain (Tauri) or `~/.infographics-studio/key` (npx, encrypted at rest with a passphrase). No relay server.

---

## 9. Repo Skeleton

```
infographics-studio/
├── package.json                  # { "bin": { "infographics-studio": "./bin/cli.js" } }
├── pnpm-lock.yaml
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.ts
├── README.md
├── LICENSE                       # MIT
├── CONTRIBUTING.md
├── bin/
│   └── cli.js                    # entrypoint: open / export / init / validate
├── schema/
│   └── v1.json                   # generated JSON Schema (committed)
├── examples/
│   ├── tokenomics.infographic.json
│   ├── ecosystem.infographic.json
│   └── cheatsheet.infographic.json
├── src/
│   ├── editor/                   # Vite+React app
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   ├── store/
│   │   │   ├── doc.ts            # Zustand: doc state, undo/redo
│   │   │   ├── selection.ts
│   │   │   └── ui.ts
│   │   ├── canvas/
│   │   │   ├── BentoCanvas.tsx
│   │   │   ├── DragLayer.tsx
│   │   │   └── ResizeHandle.tsx
│   │   ├── outline/Outline.tsx
│   │   ├── inspector/
│   │   │   ├── Inspector.tsx
│   │   │   └── fields/           # generic Zod-driven field editors
│   │   ├── snippets/
│   │   │   ├── KpiStrip.tsx
│   │   │   ├── Timeline.tsx
│   │   │   ├── ComparisonTable.tsx
│   │   │   ├── Fishbone.tsx
│   │   │   └── Callout.tsx
│   │   ├── primitives/
│   │   │   ├── Text.tsx
│   │   │   ├── Stat.tsx
│   │   │   ├── Chart.tsx         # Visx wrappers
│   │   │   ├── Image.tsx
│   │   │   ├── Icon.tsx
│   │   │   ├── Group.tsx
│   │   │   └── Spacer.tsx
│   │   ├── themes/
│   │   │   ├── aizfographics.ts
│   │   │   ├── editorial.ts
│   │   │   └── <theme-3>.ts
│   │   └── io/
│   │       ├── autosave.ts
│   │       ├── load.ts
│   │       └── upload.ts
│   ├── schema/
│   │   ├── doc.ts                # Zod root
│   │   ├── snippets/             # one Zod per snippet
│   │   ├── primitives/
│   │   ├── theme.ts
│   │   └── migrations.ts
│   ├── export/
│   │   ├── html.ts               # SSR renderer
│   │   ├── png.ts                # Playwright sidecar
│   │   └── inline-css.ts
│   ├── server/
│   │   └── dev-server.ts         # Express layer for autosave fs ops
│   └── shared/
│       ├── types.ts
│       └── utils.ts
├── tests/
│   ├── schema.test.ts
│   ├── migrations.test.ts
│   ├── export.html.test.ts
│   └── e2e/
│       ├── editor.spec.ts        # Playwright
│       └── export.png.spec.ts
└── .github/
    ├── workflows/
    │   ├── ci.yml                # typecheck + test on PR
    │   └── release.yml           # changesets → npm publish
    └── ISSUE_TEMPLATE/
```

---

## 10. Implementation Plan (rough phasing)

**Week 1 — Foundations**
- Repo init, license, README, CI skeleton.
- Zod schema for doc + 5 snippets + 7 primitives + 1 theme.
- JSON Schema export, committed to `schema/v1.json`.
- Read-only renderer for `aizfographics` theme + 5 snippets.
- HTML export pipeline + e2e test.

**Week 2 — Editor shell**
- Vite app, Zustand stores, autosave fs layer.
- Outline + Inspector + Bento canvas (read-only first).
- Theme switcher; remaining 2 themes designed and shipped.
- 3 seed examples.

**Week 3 — Editing**
- Drag-to-reorder (dnd-kit).
- Edge-resize handles → manual layout overrides.
- Inline text edit + emphasis spans popover.
- Image upload, icon picker.
- Undo/redo middleware.

**Week 4 — Export & polish**
- PNG export (Playwright sidecar) + first-run UX.
- CLI: open / export / init / validate.
- Round-trip re-import from HTML's embedded source script.
- Docs site (README + simple GitHub Pages).
- v0.1.0 release on npm with `next` dist-tag, then promote to `latest`.

---

## 11. Companion Claude Skill (separate, follow-up)

Create a new skill `create-infographic-studio-doc` (separate from existing `aiz-infographic`):

- Trigger phrases: "make an editable infographic", "infographic I can polish", "studio infographic for X".
- Prompt embeds `schema/v1.json` + 3 seed examples.
- Output: a path on disk to the generated `.infographic.json` + a tip to run `npx infographics-studio open <file>`.
- Lives in this repo's `claude-skill/` directory, distributed via the skill ecosystem.

The existing HTML skill **stays untouched** for chat one-shots.

---

## 12. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Editor scope creeps toward Figma-clone | Snippets-as-data only; no plugin folder; no free-canvas; auto-layout default |
| Visx requires more chart code than Recharts | Limit v0.1 chart kinds to bar/line/pie/area; expand later |
| Playwright Chromium download confuses users | First-run UX with progress + clear messaging; HTML export works without it |
| Two products diverge over time | Accepted; both serve different lanes; no shared code at v0.1 |
| Autosave clobbers on git merge | Standard git conflict UX; doc is JSON, diffable |
| Zod schema churn breaks old docs | Migrations committed with every version bump; tests cover round-trip |
| `npx` filters non-dev users | Tauri binary planned for v0.3 once core is proven |
| Aesthetic mismatch with `aizfographics` brand | Default theme ships with current tokens 1:1; designer review before v0.1 |

---

## 13. Verification (v0.1 ship gate)

All seven must pass:

1. **Schema:** `pnpm test` — Zod round-trip for all 5 snippets, 7 primitives, 3 themes; migration tests pass.
2. **Generate:** companion Claude skill produces a valid `.infographic.json` for a sample tokenomics prompt; file validates against Zod.
3. **Edit:** `npx infographics-studio open sample.infographic.json` opens editor; user can:
   - Drag a snippet to a new slot position
   - Resize via edge handle (snaps to grid)
   - Edit text content + apply `accent` emphasis to a span
   - Switch all 3 themes; layout doesn't break
   - Upload a PNG and place it in an `Image` primitive
   - Disk file updates within ~1s of any change (autosave)
4. **Export HTML:** `--html` produces self-contained `.html`; opens in any browser; pixel-matches editor render; embedded source round-trips.
5. **Export PNG:** `--png` produces high-fidelity PNG via Playwright; first run installs Chromium with progress; subsequent runs <5s.
6. **Round-trip:** edit → autosave → close → reopen → state preserved exactly.
7. **CI:** clean `pnpm typecheck`, `pnpm lint`, `pnpm test`, Playwright e2e green.

---

## 14. Roadmap Beyond v0.1

- **v0.2** — In-editor selection-driven AI (cmd+K) with BYOK Anthropic key. Capabilities listed in §8. Add 5 more snippets (process-flow, allocation-pie, ecosystem-grid, stat-card, quote-block). Add `editorial` canvas variant.
- **v0.3** — Tauri desktop binary (Mac/Win/Linux), file associations, OS keychain for API key. Same codebase wraps.
- **v0.4** — History/snapshots without git. Optional plugin folder for community snippets (sandboxed).
- **v0.5+** — Multi-page (only on real demand). Live interactivity in exports. Hosted gallery.

---

## 15. Open Questions (deferred, not blocking)

- Final identity of the 3rd shipped theme.
- Whether Visx wrappers should be vendored as a tiny in-repo lib or kept inline in `primitives/Chart.tsx`.
- Drag/resize: dnd-kit only vs custom. Decide first impl week.
- Whether to ship a `--watch` mode for export (regenerate HTML/PNG on JSON change) or leave it editor-only.
- npm publishing cadence (proposed: `next` dist-tag from day one, weekly `latest` promotions until v1.0).
- Final repo name confirmation (`infographics-studio` proposed; alternative `aizfographics-studio` ties to brand).

---

*Spec date: 2026-05-06. v0.1 target scope locked; details inside scope adjustable during impl.*
