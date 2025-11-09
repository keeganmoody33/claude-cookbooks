# Mixmax.ai GTM Agent System

A complete multi-agent system for executing the Gutenberg Framework - a data-driven, rapid-testing approach to outbound B2B sales.

## Overview

This agent system automates and optimizes the complete outbound GTM workflow from prospect sourcing to scaled campaigns, using 6 specialized AI agents working in coordination.

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

## The 6 Specialized Agents

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

## How the System Works

### Phase 1: Preparation (Week 0-1)

```
[List Builder] → Sources 100K+ contacts → [Data Quality] → Verifies/Cleans
                                                ↓
                                        40K-50K verified contacts
                                                ↓
[Offer Strategist] → Creates 15-20 combinations
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
├── README.md                      # This file
│
├── .claude/
│   ├── agents/
│   │   ├── list-builder.md        # Agent 1: List building specialist
│   │   ├── data-quality-engineer.md # Agent 2: Verification & cleanup
│   │   ├── offer-strategist.md    # Agent 3: Offer & message creation
│   │   ├── campaign-orchestrator.md # Agent 4: Testing & winner ID
│   │   ├── deliverability-engineer.md # Agent 5: Infrastructure & reputation
│   │   └── analytics-optimizer.md # Agent 6: Scaling & optimization
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
│   └── winner_profile.py          # Winner characteristic analysis
│
└── data/                          # Data storage (gitignored)
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
- **All agents ↔ GTM Orchestrator**: Emergency protocol coordination

## Decision-Making Authority

Each agent has **full autonomy** within their domain:
- List Builder decides data sources & intent scoring
- Offer Strategist creates all copy & offer variations
- Data Quality Engineer sets verification thresholds
- Campaign Orchestrator allocates contacts & identifies winners
- Deliverability Engineer manages domains & reputation
- Analytics Optimizer determines scaling allocation & tests

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
