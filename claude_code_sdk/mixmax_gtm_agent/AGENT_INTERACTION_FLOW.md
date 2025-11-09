# Agent Interaction Flow & Handoff Protocols

## Overview

The Mixmax.ai GTM system uses 6 specialized agents working in a coordinated workflow. This document details how agents interact, when handoffs occur, and what information is exchanged.

## The Complete Workflow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         WEEK 0-1: PREPARATION                            │
└─────────────────────────────────────────────────────────────────────────┘

[List Builder Specialist]
    ↓ Sources data from 4 channels
    ↓ Scores intent signals
    ↓ Builds 100K+ raw contact pool
    ↓
HANDOFF #1: Raw Contact Database
    ↓
[Data Quality Engineer]
    ↓ Email verification (60% pass)
    ↓ AI cleanup filtering (60-75% pass)
    ↓ Enrichment & deduplication
    ↓ Quality scoring (Tier A/B/C)
    ↓
HANDOFF #2: 40K-50K Verified Contacts
    │
    │ (Parallel Track)
    │
[Offer Strategist]
    ↓ Mines customer success stories
    ↓ Develops 5-7 offers
    ↓ Creates 3-5 message frameworks
    ↓ Generates 15-20 combinations
    ↓
HANDOFF #3: Email Copy & Hypotheses
    │
    ↓
    ↓ (Streams merge)
    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                        WEEK 2-3: TESTING PHASE                           │
└─────────────────────────────────────────────────────────────────────────┘

[Campaign Orchestrator]
    ↓ Receives: 40K contacts + 15 combinations
    ↓ Allocates: 15K for testing (1K per combo)
    ↓ Reserves: 25K-35K for scaling
    ↓
COORDINATION #1: Domain Requirements
    ↓
[Deliverability Engineer]
    ↓ Provides: 10 warmed domains
    ↓ Monitors: Daily deliverability health
    ↓ Alerts: If reputation drops
    ↑
    ↓ (Continuous feedback loop)
    ↑
[Campaign Orchestrator]
    ↓ Sends: 15K contacts over 2 weeks
    ↓ Tracks: Opens, replies, meetings
    ↓ Analyzes: Performance by combination
    ↓ Identifies: 2-3 winners (>2% reply)
    ↓
HANDOFF #4: Test Results & Winners
    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                       WEEK 4-5: SCALING PHASE                            │
└─────────────────────────────────────────────────────────────────────────┘

[Analytics Optimizer]
    ↓ Receives: Winners + 25K-35K reserve contacts
    ↓ Allocates: 60-80% to GOLD, 20-40% to WINNERS
    ↓
COORDINATION #2: Capacity Check
    ↓
[Deliverability Engineer]
    ↓ Assesses: Current capacity (10 domains)
    ↓ Recommends: Add 8 more domains for scale
    ↓ Provides: 18 warmed domains total
    ↑
    ↓ (Continuous monitoring)
    ↑
[Analytics Optimizer]
    ↓ Deploys: 30K contacts to winners
    ↓ Monitors: Performance trends
    ↓ Detects: Any degradation (>20% drop)
    ↓ Analyzes: Segment performance
    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                   WEEK 6-7: OPTIMIZATION PHASE                           │
└─────────────────────────────────────────────────────────────────────────┘

[Analytics Optimizer]
    ↓ Runs: 70/30 rule (70% proven, 30% tests)
    ↓ Tests: Subject lines, timing, segments
    ↓ Identifies: Top-performing segments
    ↓ Analyzes: Winner characteristics
    ↓
HANDOFF #5: ICP Refinement Recommendations
    ↓
[List Builder Specialist]
    ↓ Receives: High-engagement profile
    ↓ Refines: ICP criteria based on data
    ↓ Sources: 50K+ new contacts (refined ICP)
    ↓
    ↓ (Cycle repeats)
    ↓
HANDOFF #6: Refined Contact Pool
    ↓
[Data Quality Engineer]
    ↓ Processes: New 50K contacts
    ↓ Delivers: 30K-35K verified contacts
    ↓ (Back to testing/scaling cycle)
```

## Detailed Handoff Specifications

### HANDOFF #1: List Builder → Data Quality Engineer

**Trigger**: List Builder completes sourcing 100,000+ raw contacts

**Delivered Assets**:
```
File: data/raw_contacts.csv
Fields:
- contact_id
- email
- first_name
- last_name
- company
- job_title
- industry
- company_size
- source (linkedin_engagement | tech_stack | hiring | lookalike)
- intent_score (0-10)
- sourced_date
```

**Metadata Document**:
```
File: data/sourcing_report.json
{
  "total_contacts": 127450,
  "sources": {
    "linkedin_engagement": 42300,
    "tech_stack": 51200,
    "hiring_signals": 18950,
    "customer_lookalike": 15000
  },
  "intent_distribution": {
    "high (8-10)": 31400,
    "medium (5-7)": 58200,
    "low (1-4)": 37850
  },
  "expected_verification_rate": 0.60,
  "expected_ai_pass_rate": 0.70,
  "projected_final_count": 53500
}
```

**Quality Gates**:
- ✓ Minimum 100,000 raw contacts
- ✓ Source diversity (no single source >60%)
- ✓ Intent distribution (>20% high-intent)
- ✓ All required fields populated >90%

---

### HANDOFF #2: Data Quality Engineer → Campaign Orchestrator

**Trigger**: Data Quality Engineer completes verification & AI cleanup

**Delivered Assets**:
```
File: data/verified_contacts.csv
Fields:
- contact_id
- email
- first_name
- last_name
- company
- job_title
- industry
- company_size
- source
- intent_score
- verification_status (valid | catch-all)
- quality_score (0-100)
- quality_tier (A | B | C)
- ai_icp_fit_score (0-10)
- enrichment_complete (boolean)
```

**Quality Report**:
```
File: data/quality_report.json
{
  "input_contacts": 127450,
  "verified_contacts": 73200,
  "verification_rate": 0.618,
  "ai_filtered_contacts": 46300,
  "ai_pass_rate": 0.632,
  "final_clean_contacts": 43450,
  "quality_distribution": {
    "tier_a (80-100)": 18200,
    "tier_b (60-79)": 20100,
    "tier_c (<60)": 5150
  },
  "cost_summary": {
    "verification_cost": 127.45,
    "ai_cleanup_cost": 92.60,
    "total_cost": 220.05,
    "cost_per_contact": 0.005
  }
}
```

**Quality Gates**:
- ✓ Minimum 40,000 verified contacts
- ✓ Verification rate >50%
- ✓ AI cleanup pass rate >50%
- ✓ Tier A+B >80% of total

---

### HANDOFF #3: Offer Strategist → Campaign Orchestrator

**Trigger**: Offer Strategist completes 15-20 combinations

**Delivered Assets**:
```
Directory: campaign_assets/
├── offers/
│   ├── 01_free_audit.md
│   ├── 02_free_intent_list.md
│   ├── 03_free_campaign_test.md
│   ├── 04_complimentary_workshop.md
│   └── 05_risk_free_pilot.md
├── frameworks/
│   ├── problem_first.md
│   ├── social_proof_first.md
│   └── direct_value_first.md
├── combinations/
│   ├── combo_01_audit_problem.txt
│   ├── combo_02_audit_socialproof.txt
│   ├── ...
│   └── combo_15_pilot_directvalue.txt
└── sequences/
    ├── email1_templates/
    ├── email2_templates/
    └── email3_templates/
```

**Hypothesis Document**:
```
File: campaign_assets/hypotheses.json
[
  {
    "combo_id": 1,
    "offer": "Free Audit",
    "framework": "Problem-First",
    "hypothesis": "Problem-first messaging will resonate with ops leaders experiencing pain",
    "expected_reply_rate": 2.8,
    "success_threshold": 2.5,
    "kill_threshold": 1.0,
    "learning_goal": "Validate pain point awareness"
  },
  ...
]
```

**Quality Gates**:
- ✓ 15-20 combinations documented
- ✓ All sequences complete (Email 1, 2, 3)
- ✓ Hypotheses with expected performance
- ✓ Customer social proof included

---

### HANDOFF #4: Campaign Orchestrator → Analytics Optimizer

**Trigger**: 2-week test window complete

**Delivered Assets**:
```
File: data/test_results.csv
Fields:
- combo_id
- offer
- message_framework
- contacts_sent
- opens
- open_rate
- replies
- reply_rate
- positive_replies
- positive_rate
- meetings_booked
- meeting_rate
- negative_replies
- unsubscribes
- classification (GOLD | WINNER | WEAK | DEAD)
```

**Winner Profiles**:
```
File: data/winners.json
[
  {
    "combo_id": 3,
    "classification": "GOLD",
    "offer": "Free Intent List",
    "framework": "Direct Value",
    "contacts_sent": 1000,
    "reply_rate": 4.2,
    "positive_rate": 2.6,
    "meeting_rate": 0.9,
    "recommendation": "Scale to 20,000 contacts immediately",
    "best_segments": ["SaaS", "100-500 employees", "Director-level"],
    "email_copy": "campaign_assets/combinations/combo_03_list_directvalue.txt"
  },
  {
    "combo_id": 7,
    "classification": "WINNER",
    "offer": "Free Audit",
    "framework": "Problem-First",
    "contacts_sent": 1000,
    "reply_rate": 2.6,
    "positive_rate": 1.8,
    "meeting_rate": 0.7,
    "recommendation": "Scale to 10,000 contacts"
  }
]
```

**Reserve Pool**:
```
File: data/reserve_contacts.csv
(25,000-35,000 contacts not used in testing, ready for scaling)
```

**Quality Gates**:
- ✓ All 15 combinations tested (1K each)
- ✓ 2-week test window completed
- ✓ 2+ winners identified (>2% reply)
- ✓ Reserve pool available for scaling

---

### HANDOFF #5: Analytics Optimizer → List Builder (Feedback Loop)

**Trigger**: Week 5+, sufficient scaling data collected

**Delivered Assets**:
```
File: data/icp_refinement.json
{
  "analysis_period": "Week 1-5",
  "total_positive_replies": 1580,
  "high_engagement_profile": {
    "industries": {
      "SaaS": 0.64,
      "FinTech": 0.22,
      "MarTech": 0.14
    },
    "company_size": {
      "100-500": 0.78,
      "50-100": 0.15,
      "500-1000": 0.07
    },
    "job_titles": {
      "VP Revenue": 0.32,
      "Director Sales Ops": 0.28,
      "Head of Growth": 0.18,
      "Manager": 0.12,
      "C-Level": 0.10
    },
    "tech_stack": {
      "Salesforce": 0.89,
      "Outreach": 0.67,
      "HubSpot": 0.54
    },
    "intent_signals": {
      "linkedin_engagement_30d": 0.91,
      "hiring_signal_60d": 0.43
    }
  },
  "recommendations": {
    "increase_targeting": [
      "SaaS companies 100-500 employees",
      "VP/Director titles (reduce Manager)",
      "Salesforce OR Outreach users",
      "LinkedIn engagers last 30 days"
    ],
    "decrease_targeting": [
      "Healthcare industry",
      "Companies <100 employees",
      "C-Level (lower reply rate than VP/Director)"
    ]
  },
  "expected_lift": 0.30
}
```

**Underperforming Segments**:
```
File: data/underperforming_segments.csv
industry,company_size,avg_reply_rate,recommendation
Healthcare,<100,1.8%,Exclude from future lists
Manufacturing,All,1.5%,Exclude from future lists
```

**Quality Gates**:
- ✓ Minimum 1,000 replies analyzed
- ✓ Statistical significance achieved
- ✓ Clear high-performing segments identified
- ✓ Actionable recommendations for List Builder

---

### HANDOFF #6: List Builder → Data Quality Engineer (Cycle 2)

**Trigger**: Refined ICP complete, new sourcing executed

**Delivered Assets**:
(Same format as Handoff #1, but with refined targeting)

```
File: data/raw_contacts_refined.csv
(50,000+ new contacts matching refined ICP)
```

**Refinement Report**:
```
File: data/refinement_report.json
{
  "refinement_changes": {
    "industries": "Focused on SaaS (60%), FinTech (30%), MarTech (10%)",
    "company_size": "Narrowed to 100-500 employees (primary)",
    "job_titles": "Prioritized VP/Director, reduced Manager-level",
    "tech_stack_filters": "Added: Using Salesforce OR Outreach",
    "intent_boost": "2x score for LinkedIn engagement last 30d"
  },
  "expected_improvements": {
    "icp_fit_score_avg": "+25%",
    "predicted_reply_rate": "+30-40%",
    "higher_tier_a_percentage": "+15%"
  }
}
```

---

## Continuous Coordination Protocols

### Deliverability Engineer ↔ Campaign Orchestrator

**Daily Sync** (automated via scripts):
```
Deliverability Engineer provides:
- Domain health status (all 10-18 domains)
- Available send capacity (emails/day)
- Reputation scores
- Inbox placement rates
- Alert: Any domain <80 reputation

Campaign Orchestrator responds:
- Pause sending on flagged domains
- Redistribute volume to healthy domains
- Adjust daily send rates if capacity constrained
```

### Analytics Optimizer ↔ Deliverability Engineer

**Weekly Sync**:
```
Analytics Optimizer requests:
- Capacity expansion plan (if scaling >2K/day)
- Inbox placement trends by campaign

Deliverability Engineer provides:
- Domain expansion timeline (new domains need 30d warmup)
- Placement optimization recommendations
```

### Campaign Orchestrator ↔ Offer Strategist

**Ad-hoc (when needed)**:
```
Campaign Orchestrator triggers when:
- All tests <1% reply rate (no winners)
- Need new angles for saturated market
- Persona-specific variants needed

Offer Strategist delivers:
- New offer variations
- Message refresh
- Segment-specific copy
```

---

## Emergency Protocols

### Protocol #1: Deliverability Crisis

**Trigger**: Domain reputation <60 OR blacklisted

**Response**:
1. **Deliverability Engineer**:
   - IMMEDIATELY stop all sends from affected domain(s)
   - Diagnose root cause
   - Initiate recovery protocol

2. **Campaign Orchestrator**:
   - Pause affected campaigns
   - Redistribute to healthy domains (if capacity available)
   - OR delay sends until resolution

3. **GTM Orchestrator**:
   - Alert all agents
   - Coordinate recovery timeline
   - Approve/reject aggressive recovery attempts

---

### Protocol #2: No Winners Found

**Trigger**: 15,000+ contacts tested, all <1% reply rate

**Response**:
1. **Campaign Orchestrator**:
   - Compile detailed failure analysis
   - Identify: Deliverability issue? Content issue? ICP issue?

2. **Offer Strategist**:
   - Develop 5 new offer/message combinations
   - Test on small sample (500 contacts each)

3. **List Builder + Data Quality**:
   - Audit ICP targeting
   - Validate contact quality
   - Source fresh data if stale

4. **GTM Orchestrator**:
   - Decide: Pivot strategy OR refine and retest
   - Approve 5,000-10,000 contact allocation for new tests

---

### Protocol #3: Contact Pool Depletion

**Trigger**: Reserve pool <10,000 contacts

**Response**:
1. **Analytics Optimizer**:
   - Alert GTM Orchestrator
   - Provide timeline until exhaustion

2. **List Builder**:
   - Accelerate new sourcing (target 50K+ in 1 week)
   - Explore new data sources if existing depleted

3. **Data Quality Engineer**:
   - Expedite verification pipeline
   - Prioritize high-quality Tier A contacts

4. **Campaign Orchestrator**:
   - Slow scaling pace (if needed)
   - Reserve 5K contacts as safety buffer

---

## Agent Autonomy Boundaries

### Full Autonomy (No approval needed):
- **List Builder**: Data source selection, intent scoring methodology
- **Offer Strategist**: Email copy, offer design within proven frameworks
- **Data Quality Engineer**: Verification thresholds, AI cleanup criteria
- **Campaign Orchestrator**: Contact allocation math, campaign setup
- **Deliverability Engineer**: Domain management, warmup schedules
- **Analytics Optimizer**: Scaling allocation, A/B test design

### Coordination Required:
- **Campaign Orchestrator + Deliverability**: Send volume planning
- **Analytics Optimizer + List Builder**: ICP refinement
- **All agents**: Emergency protocol activation

### GTM Orchestrator Approval Needed:
- Major strategy pivots (e.g., changing entire offer approach)
- Budget increases (>$5K additional spend)
- Timeline extensions (>2 weeks past original plan)
- Emergency protocol decisions (e.g., pause entire GTM for 1 week)

---

## Success Metrics by Agent

### List Builder
- Source diversity: No single channel >50%
- Intent quality: >20% high-intent contacts
- Volume: 100K+ raw contacts delivered

### Data Quality Engineer
- Verification rate: 60-70%
- AI pass rate: 60-75%
- Final output: 40K+ verified contacts

### Offer Strategist
- Combination count: 15-20 testable combos
- Winner prediction accuracy: 2+ actual winners match predictions

### Campaign Orchestrator
- Test completion: 100% of combos tested
- Winner identification: 2-3 winners >2% reply rate
- Time to decision: <14 days

### Deliverability Engineer
- Inbox placement: >90%
- Sender score: >80
- Zero blacklists

### Analytics Optimizer
- Scaling efficiency: Maintain reply rate ±20%
- Optimization lift: 10-30% improvement from tests
- ROI: >5,000%

---

This interaction flow ensures each specialist agent operates autonomously within their domain while coordinating seamlessly for end-to-end GTM execution.
