# New Template Design Briefs

11 templates to design. Each section includes: what it is, canvas, snippets, style hint, and ready-to-use mock data you can drop straight into the infographic generator to test your layout.

---

## 1. `tutorial`

**What it is:** Numbered, hands-on step-by-step guide. More prescriptive than `how-it-works` — includes warnings, tips, and expected outcomes per step.

**Canvas:** `bento-box`
**Snippets:** `process-flow`, `list`, `annotation`
**Accent:** pair #5 (blue → purple) — instructional tone

**Mock data:**

```
TOPIC: How to set up a Solana wallet from scratch
STEPS:
1. Download Phantom wallet from phantom.app (Chrome/Firefox extension or iOS/Android app)
   TIP: Only download from the official site. Beware of fake extensions.
2. Click "Create a new wallet" and set a strong password
   WARNING: This password only protects local access. It does not recover your wallet.
3. Write down your 12-word Secret Recovery Phrase on paper
   WARNING: Never screenshot or store digitally. Anyone with this phrase owns your funds.
4. Confirm the phrase by selecting words in the correct order
5. Your wallet is ready. Copy your public address from the top of the app.
   TIP: Your public address is safe to share — it's like an email address.

EXPECTED OUTCOME: A funded, secure Solana wallet ready for transactions
TIME TO COMPLETE: ~5 minutes
DIFFICULTY: Beginner
```

---

## 2. `concept-map`

**What it is:** Topic broken into branches, subtopics, and relationships. Good for "everything about X" overviews, knowledge maps, and subject breakdowns.

**Canvas:** `poster`
**Snippets:** `mind-map`, `hierarchical`, `network-graph`
**Accent:** pair #3 (lime → gold) — knowledge/education

**Mock data:**

```
CENTRAL TOPIC: DeFi (Decentralized Finance)

BRANCHES:
- Lending & Borrowing
  - Protocols: Aave, Compound, Morpho
  - Mechanism: Collateralized loans, interest rate models
  - Risk: Liquidation if collateral drops below threshold

- Trading
  - Protocols: Uniswap, Curve, dYdX
  - Mechanism: AMM (Automated Market Maker), order book hybrids
  - Risk: Impermanent loss, slippage

- Yield
  - Protocols: Yearn, Convex, EigenLayer
  - Mechanism: Strategy vaults, restaking, points
  - Risk: Smart contract risk, protocol dependency

- Stablecoins
  - Types: Fiat-backed (USDC), Crypto-backed (DAI), Algorithmic (FRAX)
  - Risk: De-peg, regulatory, collateral failure

- Infrastructure
  - Oracles: Chainlink, Pyth
  - Cross-chain: Layerzero, Wormhole
  - Wallets: Metamask, Safe

CONNECTIONS:
- Lending requires Oracles for price feeds
- Yield strategies depend on Lending + Trading protocols
- Stablecoins underpin all DeFi activity
```

---

## 3. `swot-analysis`

**What it is:** Classic 4-quadrant SWOT (Strengths, Weaknesses, Opportunities, Threats). Works for any product, company, protocol, game, or project.

**Canvas:** `bento-box`
**Snippets:** `quadrant`, `comparison`, `grid-cards`
**Accent:** pair #6 (green → cyan) for strategy; pair #4 (red → pink) for competitive/defensive framing

**Mock data:**

```
SUBJECT: Solana blockchain (as of 2026)

STRENGTHS:
- Fastest L1: ~65,000 TPS theoretical; ~2,000 TPS sustained
- Sub-cent transaction fees ($0.00025 avg)
- Strong DeFi + NFT ecosystem (Phantom, Jupiter, Magic Eden)
- Firedancer client adds client diversity and throughput
- Developer growth: 2nd largest by GitHub commits

WEAKNESSES:
- History of network outages (2021-2022 incidents)
- High validator hardware requirements (~$10k+ setup)
- Single client until Firedancer launches fully
- VC-heavy initial token distribution perception

OPPORTUNITIES:
- Consumer apps (payments, gaming, social) gaining traction
- Institutional products: Solana ETF filings in progress
- Mobile-first with Saga/Seeker phones
- AI agent wallets trending toward Solana for speed/cost

THREATS:
- Ethereum L2s (Base, Arbitrum) closing speed/cost gap
- Regulatory uncertainty on PoS tokens as securities
- Firedancer launch risk (new code = new bugs)
- ETH brand recognition remains dominant with institutions
```

---

## 4. `stat-story`

**What it is:** Data-first narrative with big statistics as the hero. Heavier on numbers and charts than `report`. Reads like a "by the numbers" feature piece.

**Canvas:** `editorial`
**Snippets:** `statistical`, `dashboard`, `timeline`
**Accent:** pair #1 (amber → orange) — data/finance energy

**Mock data:**

```
HEADLINE: The Solana DeFi Surge: By The Numbers (Q1 2026)

HERO STAT: $18.4B Total Value Locked — up 340% YoY

KEY STATISTICS:
- $18.4B TVL (Jan 2026), up from $4.2B (Jan 2025)
- 4.2M daily active wallets — highest ever on any chain
- $2.1B daily DEX volume — Jupiter accounts for 68%
- 1.1B transactions in Q1 2026 alone
- Average fee: $0.00021 per transaction
- Stablecoin supply on Solana: $9.8B (USDC: 71%, USDT: 22%)

TIMELINE:
- Jan 2025: TVL $4.2B, 900K daily wallets
- Apr 2025: Firedancer testnet launch — confidence spike
- Jul 2025: Solana ETF filing by Grayscale
- Oct 2025: TVL hits $10B for first time
- Jan 2026: $18.4B TVL, 4.2M daily wallets

BREAKDOWN BY CATEGORY:
- Liquid Staking: 38% of TVL ($7.0B) — Marinade, Jito
- DEX Liquidity: 29% ($5.3B) — Jupiter, Raydium, Orca
- Lending: 21% ($3.9B) — Kamino, Marginfi
- Other (Perps, RWA, etc.): 12% ($2.2B)

INSIGHT: Solana processed more transactions in Q1 2026 than Ethereum + all its L2s combined.
```

---

## 5. `research-findings`

**What it is:** Visual summary of a survey, study, or research report. Shows methodology, key findings, and takeaways. Good for industry reports and original research.

**Canvas:** `bento-box`
**Snippets:** `statistical`, `comparison`, `funnel`
**Accent:** pair #6 (green → cyan) — analytical/academic tone

**Mock data:**

```
STUDY: Developer Experience in Web3 — Annual Survey 2026
CONDUCTED BY: Electric Capital + Alchemy
SAMPLE: 3,847 active blockchain developers (GitHub commit activity in last 90 days)
DATE: February 2026

METHODOLOGY:
- Online survey, Jan 3–31 2026
- Respondents recruited via GitHub, Discord, X developer communities
- Verified by at least 1 on-chain transaction in past 6 months

KEY FINDINGS:
1. 68% of new devs in 2025 chose Solana as primary chain (up from 31% in 2023)
2. Ethereum still leads total active developers: 4,200 vs Solana's 2,800
3. Rust adoption: 52% of Solana devs previously had zero Rust experience
4. Average time to first deployed program: 3.2 weeks on Solana vs 5.8 weeks on Ethereum
5. Top barriers: tooling documentation (41%), wallet UX (33%), gas cost unpredictability (28%)

FUNNEL — DEVELOPER JOURNEY:
- Heard about web3 development: 100%
- Attempted a tutorial: 74%
- Deployed a test contract/program: 51%
- Shipped to mainnet: 29%
- Still active 6 months later: 18%

TOP TOOLS BY SATISFACTION (1-5 scale):
- Anchor Framework: 4.3
- Hardhat: 3.9
- Foundry: 4.1
- Remix IDE: 3.2
- Seahorse (Python-to-Rust): 3.7

CONCLUSION: Solana's developer growth is driven by new entrants (not migration). Retention is the next challenge.
```

---

## 6. `market-map`

**What it is:** Industry landscape showing categories, players, and competitive positioning. Good for ecosystem overviews, competitive maps, and category definitions.

**Canvas:** `poster`
**Snippets:** `geographic`, `quadrant`, `grid-cards`
**Accent:** pair #2 (gold → orange) — market/business energy

**Mock data:**

```
MARKET: AI Infrastructure (2026)

CATEGORIES & PLAYERS:

Training Infrastructure
  - NVIDIA (H100/B200 GPUs) — market leader
  - AMD (MI300X) — challenger
  - Google (TPU v5) — captive
  - Cerebras, Groq — specialized ASICs

Model Providers
  - OpenAI (GPT-5) — consumer + API leader
  - Anthropic (Claude 4) — enterprise/safety focus
  - Google DeepMind (Gemini Ultra) — multimodal
  - Meta (Llama 4) — open source
  - Mistral — European, open weight

Inference & Serving
  - Together AI, Fireworks AI, Groq — fast inference
  - Replicate — developer-friendly
  - Modal — serverless GPU

Application Layer
  - Cursor, GitHub Copilot — coding
  - Perplexity, You.com — search
  - Harvey, Clio — legal
  - Nabla, Suki — medical

Orchestration & Agents
  - LangChain, LlamaIndex — frameworks
  - Crew AI, AutoGen — multi-agent
  - Zapier, Make — no-code automation

POSITIONING NOTE:
- X-axis: Open vs Closed (model access)
- Y-axis: Consumer vs Enterprise focus
```

---

## 7. `org-profile`

**What it is:** Company, team, or project profile card. Mission, key people, stats, and timeline of milestones. Good for investor decks, team introductions, and project overviews.

**Canvas:** `bento-box`
**Snippets:** `grid-cards`, `timeline`, `statistical`
**Accent:** match brand — default pair #1 (amber) for startups

**Mock data:**

```
ORG: Aizaku Labs
TAGLINE: Infrastructure for AI-native applications
FOUNDED: 2024
HEADQUARTERS: San Francisco, CA
STAGE: Seed ($3.2M raised)
WEBSITE: aizaku.xyz

MISSION: Make it trivially easy for AI agents to read, write, and reason over structured data at scale.

KEY STATS:
- $3.2M raised (seed round, Dec 2024)
- 8 full-time team members
- 1,200+ GitHub stars across open-source repos
- 14 enterprise pilots in Q1 2026
- 99.97% API uptime since launch

TEAM:
- Aiz (CEO/Founder) — prev. Senior Staff Eng @ Stripe
- Kris Chen (CTO) — prev. ML Infra @ Anthropic
- Lena Park (Head of Product) — prev. PM @ Linear
- 5 engineers (Rust, Python, TypeScript)

TIMELINE:
- Jan 2024: Company founded, stealth mode
- Jun 2024: First enterprise pilot (Fortune 500 logistics co.)
- Dec 2024: $3.2M seed led by Benchmark
- Feb 2025: Public launch, 400 signups in 48h
- Q1 2026: 14 enterprise clients, first revenue positive month

INVESTORS: Benchmark (lead), Y Combinator (W24), angels from Stripe, Figma, Anthropic
```

---

## 8. `persona`

**What it is:** User persona or audience segment profile. Demographics, goals, frustrations, behaviors, and a representative quote. Good for product design, marketing, and UX research.

**Canvas:** `bento-box`
**Snippets:** `grid-cards`, `list`, `comparison`
**Accent:** pair #5 (blue → purple) — human/empathy tone

**Mock data:**

```
PERSONA NAME: "The Builder Dev"
ARCHETYPE: Solo indie developer shipping AI-powered tools

DEMOGRAPHICS:
- Age: 27-35
- Location: Remote (USA/EU/SEA)
- Role: Full-stack developer / solo founder
- Experience: 5-8 years coding, 1-2 years AI tooling

GOALS:
1. Ship fast — MVP in days, not weeks
2. Keep infrastructure costs under $500/mo
3. Build something users actually pay for
4. Learn new tech (AI, agents) on the job

FRUSTRATIONS:
1. AI SDKs break every 3 weeks with new model versions
2. Documentation that assumes you already know everything
3. Vendor lock-in disguised as "convenience"
4. Rate limits that kill demos at the worst moment

TOOLS THEY USE:
- Cursor / Claude Code (daily)
- Vercel / Railway for hosting
- Supabase or PlanetScale for DB
- Stripe for payments
- Linear for solo issue tracking

BEHAVIORS:
- Ships 6 days/week
- Reads Hacker News at 7am
- Follows 200+ developers on X
- Shares progress updates publicly (build in public)
- Joins 2-3 Discord servers per project

QUOTE: "I don't need enterprise features. I need it to just work at 2am when I'm trying to ship."

REPRESENTED BY: 34% of our current active users
```

---

## 9. `tech-stack`

**What it is:** Technology architecture overview showing layers, categories, and how systems connect. Good for engineering blogs, onboarding docs, and architecture showcases.

**Canvas:** `poster`
**Snippets:** `hierarchical`, `network-graph`, `grid-cards`
**Accent:** pair #6 (green → cyan) — technical/infrastructure

**Mock data:**

```
PRODUCT: Aizaku Data Platform
DESCRIPTION: End-to-end data pipeline for AI agent memory and retrieval

STACK LAYERS (top to bottom):

Client Layer
  - Claude Code (primary AI interface)
  - REST API (external integrations)
  - Dashboard (React + Vite, Tailwind CSS)

API Gateway
  - Language: TypeScript (Bun runtime)
  - Framework: Hono
  - Auth: JWT + API keys (Clerk)
  - Rate limiting: Upstash Redis

Core Services
  - Ingestion Service (Python, FastAPI) — parses and chunks incoming data
  - Embedding Service (Python) — text-embedding-3-large via OpenAI
  - Query Service (TypeScript) — semantic search + BM25 hybrid
  - Agent Memory Service (TypeScript) — session state, episodic memory

Data Layer
  - Primary DB: PostgreSQL (Supabase) — metadata, user accounts
  - Vector DB: Qdrant — embeddings at scale
  - Cache: Redis (Upstash) — query cache, sessions
  - Object Storage: R2 (Cloudflare) — raw files, exports

Infrastructure
  - Hosting: Railway (API), Cloudflare Workers (edge)
  - CI/CD: GitHub Actions
  - Observability: Axiom (logs), Sentry (errors)
  - IaC: Pulumi (TypeScript)

KEY CONNECTIONS:
- Claude Code → REST API → Query Service → Qdrant (main read path)
- Ingestion → Embedding → Qdrant (main write path)
- All services → PostgreSQL for audit trail
```

---

## 10. `event-recap`

**What it is:** Post-event summary with highlights, stats, and notable moments. Good for conferences, hackathons, product launches, game seasons, and community milestones.

**Canvas:** `bento-box`
**Snippets:** `timeline`, `statistical`, `grid-cards`
**Accent:** pair #2 (gold → orange) — celebratory/announcement

**Mock data:**

```
EVENT: Breakpoint 2025 — Solana's Annual Developer Conference
DATE: October 14-16, 2025
LOCATION: Amsterdam, Netherlands

BY THE NUMBERS:
- 8,400 attendees (largest Breakpoint ever, up 2.3x from 2024)
- 124 speakers across 6 stages
- 47 countries represented
- 82 sponsor companies
- 600+ hackathon submissions ($2.1M in prizes)
- 140,000+ livestream viewers (peak)

HACKATHON WINNERS:
- Grand Prize ($500K): SolanaOS — AI agent OS built on-chain
- DeFi Track ($200K): FluxFi — intent-based cross-chain DEX
- Consumer Track ($200K): PocketPay — NFC Solana payments for merchants
- Gaming Track ($150K): RealmForge — fully on-chain game engine

KEY ANNOUNCEMENTS:
- Firedancer 1.0 mainnet launch date confirmed: Q1 2026
- Solana Mobile Chapter 2 (Seeker) ships globally
- Solana Foundation $100M ecosystem fund for AI agents
- Visa announces Solana USDC settlement expansion to 12 new markets

NOTABLE TALKS:
- Anatoly Yakovenko: "The path to 1M TPS" (keynote)
- Lily Liu: "Solana as the internet's payment rail"
- Armani Ferrante: "Anchor v2 and the next 10K Solana devs"

VIBE: Amsterdam turned orange. The energy was different this year — less speculation, more builders.
```

---

## 11. `roadmap-visual`

**What it is:** Product or project roadmap with phases, milestones, owners, and status. Visual alternative to text-heavy roadmap docs.

**Canvas:** `bento-box`
**Snippets:** `roadmap`, `timeline`, `swimlane`
**Accent:** pair #3 (lime → gold) — progress/forward motion

**Mock data:**

```
PRODUCT: Aizaku Data Platform
PERIOD: Q1 2026 — Q4 2026

PHASES:

Phase 1 — Foundation (Q1 2026) [COMPLETE]
  Owner: Core Infra team
  - [x] Qdrant vector DB integration (shipped Jan 15)
  - [x] Hybrid search (BM25 + semantic, shipped Feb 2)
  - [x] Multi-tenant architecture (shipped Feb 28)
  - [x] Claude Code MCP connector v1 (shipped Mar 10)

Phase 2 — Intelligence (Q2 2026) [IN PROGRESS]
  Owner: ML + Product teams
  - [x] Re-ranking pipeline (shipped Apr 3)
  - [ ] Episodic memory (agent session persistence) — ETA May 30
  - [ ] Multi-modal ingestion (images, PDFs) — ETA Jun 15
  - [ ] Streaming search responses — ETA Jun 30

Phase 3 — Scale (Q3 2026) [PLANNED]
  Owner: Infra + Growth teams
  - [ ] Enterprise SSO (SAML, OIDC)
  - [ ] Dedicated cluster option (10x throughput)
  - [ ] Usage-based billing (pay-per-query)
  - [ ] EU data residency (GDPR)

Phase 4 — Ecosystem (Q4 2026) [PLANNED]
  Owner: DevRel + Partnerships
  - [ ] Public connector marketplace
  - [ ] Partner SDK (Python, TypeScript, Rust)
  - [ ] Aizaku Agents — pre-built AI agents powered by the platform
  - [ ] GA launch + pricing announcement

KEY MILESTONES:
- Mar 10: MCP connector live → developer onboarding begins
- May 30: Episodic memory → enables long-running agent workflows
- Sep 1: Scale release → enterprise sales kickoff
- Dec 1: GA launch → public pricing, growth motion
```

---

## Design Notes (applies to all 11)

- All use existing snippets — no new infrastructure needed
- Default canvas per template listed above — override in request if needed
- All should work with `aizfographics-style` as default; `clean-minimal` or `corporate` for professional/B2B content
- Width: 1920 default; 1080 for social-first layouts (persona, event-recap)
- Test each design by pasting the mock data block into the generator with the template name
