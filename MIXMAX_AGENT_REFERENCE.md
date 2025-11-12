# Mixmax GTM Agent System - Complete Reference Guide

**Date**: 2025-11-12
**For**: Cursor IDE Import
**Location**: `./claude_code_sdk/mixmax_gtm_agent/`

---

## Table of Contents
1. [System Overview](#system-overview)
2. [The 8 Specialized Agents](#the-8-specialized-agents)
3. [Agent Workflow & Coordination](#agent-workflow--coordination)
4. [Key Files & Data](#key-files--data)
5. [Getting Started](#getting-started)
6. [Quick Commands](#quick-commands)

---

## System Overview

### What is This?
A complete multi-agent system for executing the **Gutenberg Framework** - a data-driven, rapid-testing approach to outbound B2B sales for Mixmax.ai.

### Core Principle
**Test fast, kill losers, scale winners.**

```
100,000+ Contacts → Rapid Testing → Find Winners (2-4% reply) → Scale → Optimize → Repeat
```

### Expected Results (8-week timeline)
- 300-500 replies
- 100-200 meetings booked
- 15-30 deals closed
- $75K-150K revenue
- 5,000-10,000% ROI

### Strategic Focus
Mixmax is a **sales execution platform** focusing on:
- Sales Development (SDR, BDR)
- Account Executives
- Revenue Leadership (CRO, VP Sales, VP Revenue)
- Revenue Operations
- **NOT** general GTM, **NOT** marketing automation

---

## The 8 Specialized Agents

### 1. List Builder Specialist
**File**: `.claude/agents/list-builder.md`
**Domain**: STEP 1 - Intent-Based List Building

**Responsibilities**:
- Multi-channel data sourcing (LinkedIn, Apollo, hiring signals, lookalikes)
- Intent signal scoring
- Build 100K+ raw contact pools

**Key Metrics**:
- Source diversity (no single channel >50%)
- Intent distribution (>20% high-intent)
- Volume target: 100K+ raw contacts

**Tools**: Clay, Apollo, Python scripts

---

### 2. Data Quality Engineer
**File**: `.claude/agents/data-quality-engineer.md`
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

### 3. Offer Strategist
**File**: `.claude/agents/offer-strategist.md`
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

### 4. Campaign Orchestrator
**File**: `.claude/agents/campaign-orchestrator.md`
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

### 5. Deliverability Engineer
**File**: `.claude/agents/deliverability-engineer.md`
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

### 6. Analytics Optimizer
**File**: `.claude/agents/analytics-optimizer.md`
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

### 7. Market Intelligence Specialist
**File**: `.claude/agents/market-intelligence.md`
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

### 8. Competitive Intelligence Specialist
**File**: `.claude/agents/competitive-intelligence.md`
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

## Agent Workflow & Coordination

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

---

## Key Files & Data

### File Structure
```
mixmax_gtm_agent/
├── CLAUDE.md                      # Main context file (company, framework, metrics)
├── AGENT_INTERACTION_FLOW.md      # Detailed handoff protocols
├── AGENT_SPECIALIZATION_STRATEGY.md # Why specialized agents
├── CASE_STUDY_INTELLIGENCE.md     # 43 customer case studies + ICP intelligence
├── ACTIVATION_CHECKLIST.md        # Pre-launch checklist
├── README.md                      # System overview
│
├── .claude/
│   ├── agents/
│   │   ├── list-builder.md
│   │   ├── data-quality-engineer.md
│   │   ├── offer-strategist.md
│   │   ├── campaign-orchestrator.md
│   │   ├── deliverability-engineer.md
│   │   ├── analytics-optimizer.md
│   │   ├── market-intelligence.md
│   │   └── competitive-intelligence.md
│   │
│   └── commands/
│       └── review-system.md       # Pre-launch system review
│
├── scripts/
│   ├── analyze_customer_icp.py    # Analyze customer CSV for ICP patterns
│   ├── process_case_studies.py    # Generate ICP + messaging intelligence
│   └── parse_case_studies.py      # Parse case study data
│
└── data/                          # Data storage (gitignored)
    ├── customers_raw.csv
    ├── case_studies.json          # 43 Mixmax customer case studies
    ├── icp_intelligence.json      # ICP patterns and sweet spots
    ├── messaging_intelligence.json # Value props by segment
    ├── competitors.json           # 60 competitors with monitoring priorities
    ├── raw_contacts.csv
    ├── verified_contacts.csv
    ├── test_results.csv
    ├── winners.json
    └── icp_refinement.json
```

### Important Documentation

1. **CLAUDE.md** - Main context for all agents (company info, framework details, metrics)
2. **AGENT_INTERACTION_FLOW.md** - How agents pass data and coordinate
3. **AGENT_SPECIALIZATION_STRATEGY.md** - Why we use specialized agents
4. **README.md** - System overview and getting started guide
5. **ACTIVATION_CHECKLIST.md** - Pre-launch checklist

### Case Study Intelligence

**Available Data**:
- `data/case_studies.json`: 43 customer profiles with problems, patterns, success factors
- `data/icp_intelligence.json`: Company size/industry sweet spots, buyer triggers
- `data/messaging_intelligence.json`: Value props, pain points by segment

**Key ICP Findings**:
- **Sweet Spots**:
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

---

## Getting Started

### Pre-Launch Review (IMPORTANT!)

Before deploying agents, run a comprehensive architecture review:

```bash
cd claude_code_sdk/mixmax_gtm_agent
/review-system
```

This command will:
1. ✅ Analyze all 8 agents and coordination logic
2. 🔍 Identify gaps, risks, and weaknesses
3. 💬 Ask iterative questions to strengthen the system
4. ✔️ Validate production readiness
5. 🚀 Launch agents with your approval

**Expected time**: 40-65 minutes for thorough review + Q&A

### Environment Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Add: API keys for Clay, Apollo, verification services, email platform
```

### Initialize Agents

The GTM Orchestrator will activate specialist agents as needed. Each agent reads from:
- `CLAUDE.md` (system context)
- `.claude/agents/{agent-name}.md` (specialist instructions)

### Execute Gutenberg Framework

**Week 1-2: List building & testing**
```
GTM Orchestrator: "Execute Gutenberg Framework Phase 1: Build 100K contact list"
  → Activates List Builder Specialist
  → Hands off to Data Quality Engineer
  → Coordinates with Offer Strategist
```

**Week 2-3: Campaign testing**
```
GTM Orchestrator: "Execute Phase 2: Test 15 combinations"
  → Activates Campaign Orchestrator
  → Coordinates with Deliverability Engineer
```

**Week 3-8: Scaling & optimization**
```
GTM Orchestrator: "Execute Phase 3: Scale winners"
  → Activates Analytics Optimizer
  → Feedback loop to List Builder
```

---

## Quick Commands

### Generate Intelligence Reports
```bash
# Generate ICP and messaging intelligence
python scripts/process_case_studies.py

# Analyze customer ARR/industry/tech stack
python scripts/analyze_customer_icp.py data/customers_raw.csv
```

### Git Operations
```bash
# Check status
git status
git log --oneline -5

# Commit changes
git add .
git commit -m "Your message"

# Push to feature branch
git push -u origin claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
```

### View Agent Files
```bash
# List all agents
ls -la .claude/agents/

# Read specific agent
cat .claude/agents/list-builder.md
cat .claude/agents/competitive-intelligence.md
```

---

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

---

## Success Metrics Dashboard

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

---

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

---

## Next Steps in Cursor

1. **Open repository**: `/home/user/claude-cookbooks`
2. **Navigate to**: `./claude_code_sdk/mixmax_gtm_agent/`
3. **Review documentation**:
   - Start with `README.md`
   - Read `AGENT_SPECIALIZATION_STRATEGY.md`
   - Understand `AGENT_INTERACTION_FLOW.md`
4. **Explore agent files**: `.claude/agents/*.md`
5. **Check data files**: `./data/` (if not gitignored)
6. **Review scripts**: `./scripts/*.py`
7. **Run pre-launch review**: `/review-system` (if available in Cursor)

---

**Built with the Claude Code SDK** - Leveraging Claude's agentic capabilities for go-to-market automation.

For questions or issues, refer to the main documentation files or the CONVERSATION_EXPORT.md file.
