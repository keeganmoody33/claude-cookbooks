# Mixmax.ai GTM Agent System

A complete multi-agent system for executing the Gutenberg Framework - a data-driven, rapid-testing approach to outbound B2B sales.

## Overview

This agent system automates and optimizes the complete outbound GTM workflow from prospect sourcing to scaled campaigns, using **8 specialized AI agents** working in coordination.

### The Gutenberg Framework

**Core Principle**: Test fast, kill losers, scale winners.

```
100,000+ Contacts → Rapid Testing → Find Winners (2-4% reply) → Scale → Optimize → Repeat
```

**Expected Results** (8-week timeline):
- 300-500 replies
- 100-200 meetings booked
- 15-30 deals closed
- $75K-150K revenue
- 5,000-10,000% ROI

### Strategic Focus

**Sales Focus**: Mixmax is a **sales execution platform**. We focus exclusively on:
- Sales Development (SDR, BDR)
- Account Executives
- Revenue Leadership (CRO, VP Sales, VP Revenue)
- Revenue Operations
- NOT general GTM, NOT marketing automation

**Market Intelligence**: We monitor the **JOB MARKET** for buying signals:
- Target roles: CRO, VP/Director Sales, VP/Director Rev Ops, VP/Director SDR, SDR Manager
- When companies post these roles → they're in a buying cycle for sales tools
- NOT monitoring competitor employees for job changes

**Competitive Intelligence**: We extract **CONTACTS** from competitor engagement:
- Primary targets: **Outreach, SalesLoft, Groove** (main threats - we're taking them out)
- Awareness only: HubSpot, Lemlist (track but don't prioritize)
- Sources: LinkedIn/Twitter engagements (90 days), G2/Capterra/TrustRadius reviews
- Goal: Find dissatisfied users, extract contacts for displacement campaigns

## The 8 Specialized Agents

### 1. **List Builder Specialist** (.claude/agents/list-builder.md)
**Domain**: STEP 1 - Intent-Based List Building

**Responsibilities**:
- Multi-channel data sourcing (LinkedIn, Apollo, hiring signals, lookalikes)
- Intent signal scoring
- Build 100K+ raw contact pools

**Key Metrics**:
- Source diversity (no single channel >50%)
- Intent distribution (>20% high-intent)
- Volume target: 100K+ raw contacts

**Tools**: Clay, Apollo, Python scripts for extraction & scoring

---

### 2. **Data Quality Engineer** (.claude/agents/data-quality-engineer.md)
**Domain**: Cross-cutting - Data Verification & Cleanup

**Responsibilities**:
- Email verification (ZeroBounce/NeverBounce)
- AI-powered ICP cleanup filtering
- Data enrichment & standardization
- Duplicate detection & removal
- Compliance checks

**Key Metrics**:
- Verification rate: 60-70%
- AI cleanup pass rate: 60-75%
- Final output: 40K-50K verified contacts

**Tools**: ZeroBounce, Claude/GPT for AI filtering, enrichment APIs

---

### 3. **Offer Strategist** (.claude/agents/offer-strategist.md)
**Domain**: STEP 2 - Offer-First Message Creation

**Responsibilities**:
- Customer success story mining
- Offer development (5-7 variations: audits, free lists, pilots, etc.)
- Message framework creation (3-5 frameworks)
- A/B test hypothesis generation
- 3-email sequence design

**Key Metrics**:
- Combination count: 15-20 testable combos
- Winner prediction accuracy
- Message clarity & value perception

**Tools**: Customer interviews, copywriting frameworks, variant generators

---

### 4. **Campaign Orchestrator** (.claude/agents/campaign-orchestrator.md)
**Domain**: STEP 3 - Rapid Arbitrage Testing

**Responsibilities**:
- Combination matrix mathematics
- Contact allocation (15K for testing, 25K-35K reserved)
- Campaign configuration (15-20 campaigns × 1,000 contacts each)
- Performance tracking & winner identification
- Decision logic: <1% = DEAD, 2-3% = WINNER, >4% = GOLD

**Key Metrics**:
- Test completion rate: 100%
- Winner identification: 2-3 campaigns >2% reply
- Time to decision: <14 days

**Tools**: Instantly/Smartlead, tracking spreadsheets, statistical analysis scripts

---

### 5. **Deliverability Engineer** (.claude/agents/deliverability-engineer.md)
**Domain**: STEP 4 - Deliverability Infrastructure

**Responsibilities**:
- Domain portfolio management (10-20 domains)
- DNS configuration (SPF, DKIM, DMARC)
- 30-45 day warmup strategy
- Sender reputation monitoring (daily)
- Crisis management & recovery

**Key Metrics**:
- Inbox placement: >90%
- Sender score: >80
- Bounce rate: <3%
- Spam complaint rate: <0.1%

**Tools**: Warmup services, DNS validators, blacklist monitors, seed testing

---

### 6. **Analytics Optimizer** (.claude/agents/analytics-optimizer.md)
**Domain**: STEPS 5-6 - Scale Winners & Continuous Optimization

**Responsibilities**:
- Winner scaling strategy (30K+ contacts)
- Performance degradation monitoring
- Continuous optimization testing (70/30 rule)
- Segment performance analysis
- ROI tracking & economics
- Feedback loop to List Builder (ICP refinement)

**Key Metrics**:
- Scaling efficiency: ±20% reply rate maintained
- Optimization lift: 10-30% improvement
- Cost per meeting: <$10
- ROI: >5,000%

**Tools**: Analytics dashboards, A/B testing frameworks, segment analysis, winner profilers

---

### 7. **Market Intelligence Specialist** (.claude/agents/market-intelligence.md)
**Domain**: Cross-cutting - Buying Signal Detection & Market Monitoring

**Responsibilities**:
- Monitor job market for decision-maker hiring signals (VP Sales, CRO, Director Sales, Rev Ops, SDR Manager)
- Identify companies entering buying cycles based on hiring patterns
- Track thought leaders in revenue roles (NOT general GTM)
- Enrich hiring signals with company intelligence
- Deliver high-intent buying signal leads to List Builder

**Key Metrics**:
- Daily buying signals captured: 10-30 high-intent companies
- Signal-to-pipeline conversion rate: >15%
- Average signal score: >7/10
- Time from signal detection to handoff: <24 hours for score ≥8

**Tools**: LinkedIn Jobs, company career pages, job board APIs, enrichment services

**Why This Matters**:
- Job postings = buying signals (new VP Sales = likely evaluating sales tools)
- 2-3X higher reply rates vs. generic prospecting
- Timing advantage (reach them during evaluation window)

---

### 8. **Competitive Intelligence Specialist** (.claude/agents/competitive-intelligence.md)
**Domain**: Cross-cutting - Competitive Contact Extraction

**Responsibilities**:
- Scrape LinkedIn/Twitter engagements from Outreach, SalesLoft, Groove (last 90 days)
- Extract contacts from G2/Capterra/TrustRadius reviews (especially 1-3 star reviews)
- Enrich and verify competitive contacts for displacement campaigns
- Analyze pain points from reviews for messaging insights
- Deliver tiered contact lists to List Builder and pain point intelligence to Offer Strategist

**Primary Targets**:
- **Outreach** (CRITICAL - direct platform competitor, complexity/cost complaints)
- **SalesLoft** (CRITICAL - enterprise competitor, cost complaints)
- **Groove** (CRITICAL - in-inbox competitor, feature limitation complaints)

**Awareness Only** (Low priority):
- HubSpot Sales Hub (CRM suite, not overly concerned)
- Lemlist (different positioning)

**Key Metrics**:
- Weekly contact extraction: 500-1,000 contacts
- Email verification rate: >80%
- Tier 1 (high-intent dissatisfied users): >15% of total
- Reply rate differential: 2-3X vs. generic prospecting

**Tools**: LinkedIn/Twitter scraping, G2 API, review scrapers, enrichment APIs, email verification

**Why This Matters**:
- People engaging with competitors = high-intent, category-aware prospects
- Dissatisfied users (low reviews) = displacement opportunities
- Pain point extraction = messaging goldmine for Offer Strategist
- Competitive context = higher relevance in outreach

---

## How the System Works

### Intelligence Layer (Continuous)

```
[Market Intelligence]                    [Competitive Intelligence]
  ↓ Monitors job postings                  ↓ Scrapes LinkedIn/Twitter/G2
  ↓ Detects buying signals                 ↓ Extracts competitor engagers
  ↓ CRO/VP Sales/Rev Ops hires             ↓ Reviews (1-3 stars)
  ↓                                         ↓
  ↓ High-intent leads ──────────────────→ [List Builder] ←─── Competitive contacts
  ↓                                                           ↓ Pain points
  ↓ Thought leader insights ──────────────────────────→ [Offer Strategist]
```

### Phase 1: Preparation (Week 0-1)

```
[List Builder] → Sources 100K+ contacts (includes buying signals + competitive contacts)
                                                ↓
                                    [Data Quality] → Verifies/Cleans
                                                ↓
                                        40K-50K verified contacts
                                                ↓
[Offer Strategist] → Creates 15-20 combinations (informed by pain point intelligence)
                                                ↓
                        [Campaign Orchestrator receives all assets]
```

### Phase 2: Testing (Week 2-3)

```
[Campaign Orchestrator]
  ↓ Allocates 15K contacts (1K per combo)
  ↓ Configures 15-20 test campaigns
  ↓ Coordinates with [Deliverability Engineer]
  ↓ Sends over 2 weeks (3-email sequences)
  ↓ Tracks: Opens, replies, meetings
  ↓ Identifies 2-3 winners (>2% reply rate)
  ↓
Handoff to [Analytics Optimizer]
```

### Phase 3: Scaling (Week 3-4)

```
[Analytics Optimizer]
  ↓ Receives winners + 25K-35K reserve contacts
  ↓ Allocates: 60-80% to GOLD, 20-40% to WINNERS
  ↓ Deploys 30K contacts
  ↓ Monitors performance trends
  ↓ Coordinates capacity with [Deliverability Engineer]
  ↓ Expected: 300-500 replies, 100-200 meetings
```

### Phase 4: Optimization (Week 5-8)

```
[Analytics Optimizer]
  ↓ 70/30 Rule: 70% proven winners, 30% new tests
  ↓ Runs optimization experiments (subject lines, timing, segments)
  ↓ Analyzes winner characteristics
  ↓ Identifies top segments (e.g., SaaS + 100-500 employees)
  ↓
Feedback to [List Builder]
  ↓ Refines ICP based on winner data
  ↓ Sources 50K+ new contacts (refined targeting)
  ↓ Expected lift: +25-35% reply rate
  ↓
(Cycle repeats)
```

## Key Files & Structure

```
mixmax_gtm_agent/
├── CLAUDE.md                      # Main context file (company, framework, metrics)
├── AGENT_INTERACTION_FLOW.md      # Detailed handoff protocols
├── CASE_STUDY_INTELLIGENCE.md     # 43 customer case studies + ICP intelligence
├── README.md                      # This file
│
├── .claude/
│   ├── agents/
│   │   ├── list-builder.md        # Agent 1: List building specialist
│   │   ├── data-quality-engineer.md # Agent 2: Verification & cleanup
│   │   ├── offer-strategist.md    # Agent 3: Offer & message creation
│   │   ├── campaign-orchestrator.md # Agent 4: Testing & winner ID
│   │   ├── deliverability-engineer.md # Agent 5: Infrastructure & reputation
│   │   ├── analytics-optimizer.md # Agent 6: Scaling & optimization
│   │   ├── market-intelligence.md # Agent 7: Buying signal detection (job postings)
│   │   └── competitive-intelligence.md # Agent 8: Contact extraction (competitor engagers)
│   │
│   └── commands/                  # (Optional) Slash commands for common tasks
│
├── scripts/                       # Python automation scripts
│   ├── clay_extractor.py          # LinkedIn engagement extraction
│   ├── apollo_search.py           # Tech stack targeting
│   ├── verify_emails.py           # Email verification
│   ├── ai_filter.py               # AI ICP cleanup
│   ├── campaign_builder.py        # Campaign configuration
│   ├── track_performance.py       # Metrics tracking
│   ├── warmup_scheduler.py        # Domain warmup automation
│   ├── segment_performance.py     # Segment analysis
│   ├── winner_profile.py          # Winner characteristic analysis
│   ├── analyze_customer_icp.py    # Analyze customer CSV for ICP patterns
│   └── process_case_studies.py    # Generate ICP + messaging intelligence
│
└── data/                          # Data storage (gitignored)
    ├── customers_raw.csv          # Raw customer data
    ├── case_studies.json          # 43 Mixmax customer case studies
    ├── icp_intelligence.json      # ICP patterns and sweet spots
    ├── messaging_intelligence.json # Value props and pain points by segment
    ├── competitors.json           # 60 direct/indirect competitors with monitoring priorities
    ├── raw_contacts.csv
    ├── verified_contacts.csv
    ├── test_results.csv
    ├── winners.json
    └── icp_refinement.json
```

## Agent Coordination Model

### Handoff Sequence

```
List Builder → Data Quality Engineer → Campaign Orchestrator
      ↓                                         ↓
Offer Strategist ────────────────────────→ Campaign Orchestrator
                                                ↓
                                    Analytics Optimizer
                                                ↓
                                        (Feedback Loop)
                                                ↓
                                          List Builder
```

### Continuous Coordination

- **Campaign Orchestrator ↔ Deliverability Engineer**: Daily domain health sync
- **Analytics Optimizer ↔ List Builder**: Weekly ICP refinement
- **Competitive Intelligence ↔ Offer Strategist**: Real-time battlecard updates and positioning insights
- **Competitive Intelligence ↔ All Agents**: Weekly market signals and strategic intelligence
- **All agents ↔ GTM Orchestrator**: Emergency protocol coordination

## Decision-Making Authority

Each agent has **full autonomy** within their domain:
- List Builder decides data sources & intent scoring
- Offer Strategist creates all copy & offer variations
- Data Quality Engineer sets verification thresholds
- Campaign Orchestrator allocates contacts & identifies winners
- Deliverability Engineer manages domains & reputation
- Analytics Optimizer determines scaling allocation & tests
- Competitive Intelligence identifies threats, maintains battlecards & provides market insights

**GTM Orchestrator** (main agent) coordinates handoffs but does NOT override specialist decisions unless emergency protocol activated.

## Success Criteria (8-Week Timeline)

| Week | Phase | Key Deliverables | Success Metrics |
|------|-------|------------------|-----------------|
| 1-2 | Testing | 15K contacts tested, winners identified | 2-3 combos >2% reply rate |
| 3-4 | Scaling | 30K contacts to winners | 300-500 replies, 100-200 meetings |
| 5-6 | Optimization | 3-5 tests run, ICP refined | 10-30% performance lift |
| 7-8 | Sustainable | Consistent 1,000+ sends/day | 150+ meetings/month, 15-30 deals |

**Economic Targets**:
- Cost per meeting: <$10
- Cost per deal: <$100
- ROI: >5,000%

## Technology Stack

### Data & Sourcing
- **Clay**: LinkedIn extraction, AI filtering
- **Apollo**: Tech stack targeting, company search
- **ZeroBounce/NeverBounce**: Email verification

### Email Infrastructure
- **Instantly or Smartlead**: Email sending platform
- **10-20 domains**: Outbound sending pool
- **Warmup Inbox/Mailreach**: Domain warmup service

### Analytics
- **Tracking spreadsheets**: Performance monitoring
- **Python scripts**: Automation, analysis, optimization

## Getting Started

### 1. Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Add: API keys for Clay, Apollo, verification services, email platform
```

### 2. Initialize Agents
```bash
# The GTM Orchestrator will activate specialist agents as needed
# Each agent reads from:
# - CLAUDE.md (system context)
# - .claude/agents/{agent-name}.md (specialist instructions)
```

### 3. Execute Gutenberg Framework
```bash
# Week 1-2: List building & testing
GTM Orchestrator: "Execute Gutenberg Framework Phase 1: Build 100K contact list"
  → Activates List Builder Specialist
  → Hands off to Data Quality Engineer
  → Coordinates with Offer Strategist

# Week 2-3: Campaign testing
GTM Orchestrator: "Execute Phase 2: Test 15 combinations"
  → Activates Campaign Orchestrator
  → Coordinates with Deliverability Engineer

# Week 3-8: Scaling & optimization
GTM Orchestrator: "Execute Phase 3: Scale winners"
  → Activates Analytics Optimizer
  → Feedback loop to List Builder
```

## Emergency Protocols

### Deliverability Crisis (Reputation <60)
1. Deliverability Engineer: Stop all sends
2. Campaign Orchestrator: Redistribute to healthy domains
3. GTM Orchestrator: Coordinate recovery

### No Winners Found (All <1% reply)
1. Campaign Orchestrator: Failure analysis
2. Offer Strategist: Develop new combinations
3. List Builder + Data Quality: Audit ICP & quality

### Contact Depletion (<10K reserve)
1. Analytics Optimizer: Alert & slow scaling
2. List Builder: Accelerate new sourcing
3. Data Quality Engineer: Expedite verification

## Key Metrics Dashboard

### Volume Metrics
- Raw contacts: 100K+ target
- Verified contacts: 60K (60% rate)
- Test-ready: 40K-50K
- Testing allocation: 15K
- Scaling reserve: 25K-35K

### Performance Metrics
- GOLD reply rate: >4%
- WINNER reply rate: 2-3%
- Meeting booking: 30-40% of positive replies
- Deal close: 10-20% of meetings

### Efficiency Metrics
- Cost per contact: $0.005-0.01
- Cost per reply: $2-5
- Cost per meeting: <$10
- Cost per deal: $50-100
- ROI: 5,000-10,000%

### Infrastructure Metrics
- Domain count: 10-20
- Inbox placement: >90%
- Sender score: >80
- Send capacity: 1,000-3,000/day

## Case Study Intelligence & ICP Data

The system includes **43 analyzed Mixmax customer case studies** providing data-driven ICP intelligence and messaging insights.

### Available Data
- **`data/case_studies.json`**: 43 customer profiles with real problems, patterns, and success factors
- **`data/icp_intelligence.json`**: Company size/industry sweet spots, buyer triggers, success factors
- **`data/messaging_intelligence.json`**: Value prop themes, pain points by segment, proof points

### Key Findings
- **ICP Sweet Spots**:
  - Growth SaaS (51-500 employees): 19 customers - highest concentration
  - Enterprise (1000+): 10 customers - highest ARR potential
  - Software/SaaS: 16 customers - primary vertical

- **Primary Buyer Pain**: Coordination latency and visibility gaps in high-volume outreach

- **Buying Triggers**:
  - Team scaling without proportional headcount
  - Manual processes causing delays
  - Lack of visibility into outreach performance
  - Inconsistent messaging across team

- **Most Valued Features**:
  - Templates (40+ mentions)
  - Sequences (35+ mentions)
  - CRM integration (30+ mentions)
  - Tracking (30+ mentions)

### How Agents Use This Data
- **List Builder**: Lookalike targeting, intent signals, industry prioritization
- **Offer Strategist**: Pain-based offers, customer story mining, value prop development
- **Campaign Orchestrator**: Segment campaigns by ICP patterns, test hypotheses
- **Analytics Optimizer**: Winner profiling, segment performance analysis, ICP refinement

**Full documentation**: See `CASE_STUDY_INTELLIGENCE.md`

### Generate Intelligence Reports
```bash
# Generate ICP and messaging intelligence
python scripts/process_case_studies.py

# Analyze customer ARR/industry/tech stack
python scripts/analyze_customer_icp.py data/customers_raw.csv
```

## Contributing

This agent system is designed for Mixmax.ai's GTM execution. To extend or customize:

1. **Add new agents**: Create `.claude/agents/{new-agent}.md` following the pattern
2. **Add scripts**: Place in `/scripts` directory with clear documentation
3. **Update CLAUDE.md**: Add new context, metrics, or protocols
4. **Document handoffs**: Update AGENT_INTERACTION_FLOW.md

## References

- **Gutenberg Framework**: This documentation
- **Claude Code SDK**: https://github.com/anthropics/claude-code-sdk-python
- **Agent Pattern Examples**: See `claude_code_sdk/chief_of_staff_agent/` in parent directory

---

**Built with the Claude Code SDK** - Leveraging Claude's agentic capabilities for go-to-market automation.
