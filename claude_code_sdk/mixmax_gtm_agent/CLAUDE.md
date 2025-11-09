# CLAUDE.md - Mixmax.ai GTM System Context

## Company Overview
- **Company**: Mixmax.ai
- **Product**: AI-powered outbound sales automation platform
- **Mission**: Help B2B companies build predictable outbound revenue engines
- **Stage**: Go-to-market expansion phase
- **GTM Framework**: Gutenberg Framework (rapid arbitrage testing)

## Gutenberg Framework Overview

The Gutenberg Framework is a systematic, data-driven approach to outbound GTM that uses rapid testing to identify high-performing offer/message combinations before scaling.

### Core Principle
**Volume → Test → Identify Winners → Scale**

Most outbound fails because companies scale too early or test too slowly. The Gutenberg Framework solves this by:
1. Building large contact pools (100K+)
2. Rapidly testing 15-20 offer/message combinations
3. Identifying 2-3 winners (2-4%+ reply rates) in 2 weeks
4. Scaling only what works
5. Continuously optimizing

## The 6-Step Framework

### STEP 1: Intent-Based List Building
**Goal**: 100,000+ raw contacts → 40,000-50,000 verified prospects
**Owner**: List Builder Specialist

**Data Sources:**
- LinkedIn engagement (company + competitor content)
- Tech stack targeting (complementary/competitor tools)
- Hiring signals (job postings, team expansion)
- Customer lookalike modeling

**Output**: Large, high-intent prospect database

### STEP 2: Offer-First Message Creation
**Goal**: 5-7 offers × 3-5 message frameworks = 15-35 test combinations
**Owner**: Offer Strategist

**Offer Types:**
- Free audits
- Free high-intent lists
- Free campaign tests
- Complimentary workshops
- Risk-free pilots

**Message Frameworks:**
- Problem → Solution → Proof → Offer
- Social Proof → Insight → Offer
- Direct Value → Proof → Offer

**Output**: 15-20 testable combinations with hypotheses

### STEP 3: Rapid Arbitrage Testing
**Goal**: Test 15-20 combinations × 1,000 contacts each → Find 2-3 winners in 2 weeks
**Owner**: Campaign Orchestrator

**Testing Math:**
- 15,000 contacts allocated to testing
- 1,000 contacts per combination
- 3-email sequence (Days 1, 4, 7)
- 2-week test window

**Success Thresholds:**
- <1% reply rate = DEAD (kill immediately)
- 2-3% reply rate = WINNER (scale to 10K)
- >4% reply rate = GOLD (scale to 20K+)

**Output**: Identified winners ready for scaling

### STEP 4: Deliverability Infrastructure
**Goal**: Maintain >95% inbox placement at scale
**Owner**: Deliverability Engineer

**Infrastructure:**
- 10-20 domain portfolio
- 30-45 day warmup process
- DNS configuration (SPF, DKIM, DMARC)
- Daily reputation monitoring
- Send rate: 100-150 emails/day/domain

**Output**: Warmed, healthy domain pool for scaling

### STEP 5: Scale Winners
**Goal**: Deploy 30,000+ contacts to winning combinations
**Owner**: Analytics Optimizer

**Scaling Strategy:**
- Week 3-4: 30,000 contacts to winners
- GOLD gets 50-80% of volume
- Monitor for performance degradation
- Adjust based on deliverability

**Output**: Scaled campaigns generating consistent meetings

### STEP 6: Continuous Optimization
**Goal**: Improve performance over time, find next winners
**Owner**: Analytics Optimizer

**Optimization Areas:**
- Subject line tests
- Send timing experiments
- Segment-specific messaging
- Follow-up cadence
- ICP refinement

**70/30 Rule:**
- 70% of volume: Proven winners
- 30% of volume: New tests

**Output**: Continuously improving reply rates + new winner discovery

## Cross-Cutting Responsibility: Data Quality
**Owner**: Data Quality Engineer

**Quality Gates:**
- Email verification (60% pass rate target)
- AI cleanup filtering (60-75% pass rate)
- Data enrichment & standardization
- Duplicate removal
- Compliance checks

**Role**: Acts between List Builder and Campaign Orchestrator to ensure only high-quality contacts enter testing phase.

## Agent Collaboration Model

```
┌─────────────────────────────────────────────────────────┐
│                     GTM ORCHESTRATOR                     │
│            (Coordinates all specialist agents)           │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────────┐
        ▼                   ▼                       ▼
┌───────────────┐   ┌───────────────┐   ┌──────────────────┐
│ List Builder  │──▶│ Data Quality  │──▶│    Campaign      │
│  Specialist   │   │   Engineer    │   │  Orchestrator    │
└───────────────┘   └───────────────┘   └──────────────────┘
        │                   │                       │
        │                   │                       ▼
        │                   │            ┌──────────────────┐
        │                   │            │ Deliverability   │
        │                   │            │    Engineer      │
        │                   │            └──────────────────┘
        │                   │                       │
        ▼                   ▼                       ▼
┌───────────────┐   ┌───────────────┐   ┌──────────────────┐
│     Offer     │──▶│   Campaign    │──▶│   Analytics      │
│  Strategist   │   │ Orchestrator  │   │   Optimizer      │
└───────────────┘   └───────────────┘   └──────────────────┘
                                                   │
                                                   │ Feedback Loop
                                                   ▼
                                          ┌──────────────────┐
                                          │  List Builder    │
                                          │  (ICP Refinement)│
                                          └──────────────────┘
```

## Handoff Protocols

### List Builder → Data Quality Engineer
**Trigger**: 100,000+ raw contacts sourced
**Handoff**:
- Raw contact CSV
- Source attribution
- Intent scores
- Segmentation metadata

### Data Quality Engineer → Campaign Orchestrator
**Trigger**: 40,000+ verified, AI-filtered contacts ready
**Handoff**:
- Verified contact CSV
- Quality scores (Tier A/B/C)
- Compliance status
- Segment breakdown

### Offer Strategist → Campaign Orchestrator
**Trigger**: 15-20 offer/message combinations finalized
**Handoff**:
- Email copy (all variants)
- Hypotheses document
- Expected performance predictions
- Sequence designs

### Campaign Orchestrator → Deliverability Engineer
**Trigger**: Campaign setup complete, ready to send
**Coordination**:
- Domain allocation requests
- Send volume projections
- Warmup status checks
- Deliverability health monitoring

### Campaign Orchestrator → Analytics Optimizer
**Trigger**: 2-week test window complete, winners identified
**Handoff**:
- Test results (all combinations)
- Winner performance data
- Contact pool reserve (for scaling)
- Segment performance breakdowns

### Analytics Optimizer → List Builder (Feedback Loop)
**Trigger**: Week 5+ scaling phase, performance data collected
**Handoff**:
- Winner profile analysis
- High-engagement characteristics
- ICP refinement recommendations
- Underperforming segment data

## Key Metrics (System-Wide)

### Volume Metrics
- **Raw Contacts**: 100,000+ target
- **Verified Contacts**: 60,000 (60% verification rate)
- **Test-Ready Contacts**: 40,000-50,000 (post-AI cleanup)
- **Testing Allocation**: 15,000 contacts
- **Scaling Reserve**: 25,000-35,000 contacts

### Performance Metrics
- **Test Success Rate**: 15-20% of combinations become winners
- **Target Reply Rates**:
  - GOLD: >4%
  - WINNER: 2-3%
  - DEAD: <1%
- **Meeting Booking Rate**: 30-40% of positive replies
- **Deal Close Rate**: 10-20% of meetings

### Efficiency Metrics
- **Cost per Contact**: $0.005-0.01 (verified)
- **Cost per Reply**: $2-5
- **Cost per Meeting**: <$10 (target)
- **Cost per Deal**: $50-100
- **ROI**: 5,000-10,000%

### Infrastructure Metrics
- **Domain Count**: 10-20 domains
- **Inbox Placement**: >90% target
- **Sender Score**: >80 target
- **Send Capacity**: 1,000-3,000 emails/day

## Technology Stack

### Data & List Building
- **Clay**: LinkedIn engagement extraction, AI filtering
- **Apollo**: Tech stack targeting, company search
- **ZeroBounce/NeverBounce**: Email verification

### Email Infrastructure
- **Instantly / Smartlead**: Email sending platform
- **Warmup Inbox / Mailreach**: Domain warmup
- **10-20 domains**: Outbound sending pool

### Analytics & Tracking
- **Campaign tracking spreadsheet**: Performance monitoring
- **Custom Python scripts**: Analysis, optimization, automation
- **Segment analysis tools**: Performance breakdown

## Available Scripts

All specialist agents have access to Python scripts in the `/scripts` directory:

### List Building
- `clay_extractor.py`: LinkedIn engagement extraction
- `apollo_search.py`: Tech stack targeting
- `hiring_signals.py`: Job posting analysis
- `lookalike_builder.py`: Customer reverse engineering
- `intent_scorer.py`: Intent signal scoring

### Data Quality
- `verify_emails.py`: Email verification
- `ai_filter.py`: AI-powered ICP validation
- `enrich_contacts.py`: Data enrichment
- `deduplicate.py`: Duplicate detection
- `score_quality.py`: Contact quality scoring

### Campaign Management
- `random_allocator.py`: Random contact assignment
- `segment_allocator.py`: Strategic segmentation
- `campaign_builder.py`: Campaign configuration
- `track_performance.py`: Metrics sync
- `identify_winners.py`: Winner analysis

### Deliverability
- `setup_domain.py`: Domain configuration
- `check_dns.py`: DNS validation
- `warmup_scheduler.py`: Automated warmup
- `check_reputation.py`: Sender score monitoring
- `check_blacklists.py`: Blacklist detection
- `seed_test.py`: Inbox placement testing

### Analytics & Optimization
- `allocate_scale.py`: Scaling allocation
- `performance_trend.py`: Trend analysis
- `segment_performance.py`: Segment breakdown
- `run_ab_test.py`: A/B testing framework
- `winner_profile.py`: Winner characteristic analysis
- `calculate_roi.py`: ROI calculator

## Decision-Making Authority

Each specialist agent has FULL AUTHORITY over their domain:

1. **List Builder**: Which sources to use, how to score intent
2. **Offer Strategist**: Which offers to create, message frameworks to test
3. **Data Quality Engineer**: Which contacts pass verification/AI cleanup
4. **Campaign Orchestrator**: Contact allocation, test setup, winner classification
5. **Deliverability Engineer**: Domain warmup, send limits, reputation management
6. **Analytics Optimizer**: Scaling allocation, optimization tests, ICP refinement

**GTM Orchestrator** (main agent) coordinates handoffs but does NOT override specialist decisions.

## Risk Management

### Critical Risks
1. **Deliverability Failure**: Can destroy entire GTM engine
   - Mitigation: Deliverability Engineer monitors daily
   - Alert threshold: Sender score <70, bounce rate >3%

2. **No Winners Found**: All tests <1% reply rate
   - Mitigation: Offer Strategist develops new angles
   - Pivot threshold: 20K contacts tested, 0 winners

3. **Contact Pool Depletion**: Running out of prospects
   - Mitigation: List Builder continuously sources
   - Alert threshold: Reserve pool <10K contacts

4. **Performance Degradation**: Winners decline when scaled
   - Mitigation: Analytics Optimizer monitors trends
   - Alert threshold: >20% reply rate drop week-over-week

5. **Market Saturation**: Same prospects receiving multiple campaigns
   - Mitigation: Deduplication, send frequency caps
   - Limit: Max 1 campaign per prospect per month

## Success Criteria (8-Week Timeline)

**Week 1-2: Testing Phase**
- 100K+ raw contacts sourced ✓
- 40K+ verified, ready for testing ✓
- 15-20 combinations tested (15K contacts) ✓
- 2-3 winners identified (>2% reply rate) ✓

**Week 3-4: Scaling Phase**
- 30K contacts deployed to winners ✓
- 300-500 replies generated ✓
- 100-200 meetings booked ✓
- Deliverability maintained (>90%) ✓

**Week 5-6: Optimization Phase**
- 3-5 optimization tests run ✓
- 10-30% performance lift achieved ✓
- ICP refined based on winner data ✓
- New contact pool built (50K+) ✓

**Week 7-8: Sustainable Growth**
- Consistent 1,000+ sends/day ✓
- 2-4% reply rate maintained ✓
- 150+ meetings/month ✓
- 15-30 deals closed ✓
- Positive ROI (>5,000%) ✓

## Specialist Agent Activation

When a user requests work related to a specific domain, the GTM Orchestrator should delegate to the appropriate specialist:

- "Build me a list of..." → **List Builder Specialist**
- "Create an offer for..." → **Offer Strategist**
- "Set up a test campaign..." → **Campaign Orchestrator**
- "Verify these contacts..." → **Data Quality Engineer**
- "Check domain health..." → **Deliverability Engineer**
- "Analyze campaign performance..." → **Analytics Optimizer**

Each specialist has deep expertise in their domain and should be trusted to make decisions autonomously within their scope.

---

**Remember**: The Gutenberg Framework is a SYSTEM, not a tactic. All 6 agents must work in harmony for the GTM engine to function. Speed, precision, and continuous optimization are the keys to success.
