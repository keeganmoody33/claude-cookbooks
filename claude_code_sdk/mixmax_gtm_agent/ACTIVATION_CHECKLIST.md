# Mixmax GTM Agent System - Activation Checklist

## ✅ Completed Components

### 1. Agent Definitions (All 6 Specialists)
- ✅ `.claude/agents/list-builder.md` - List building specialist
- ✅ `.claude/agents/data-quality-engineer.md` - Data verification & cleanup
- ✅ `.claude/agents/offer-strategist.md` - Offer & message creation
- ✅ `.claude/agents/campaign-orchestrator.md` - Testing & winner identification
- ✅ `.claude/agents/deliverability-engineer.md` - Infrastructure & deliverability
- ✅ `.claude/agents/analytics-optimizer.md` - Scaling & optimization

### 2. Core Documentation
- ✅ `CLAUDE.md` - System context for all agents
- ✅ `README.md` - Complete system documentation
- ✅ `AGENT_SPECIALIZATION_STRATEGY.md` - Detailed agent strategy
- ✅ `AGENT_INTERACTION_FLOW.md` - Handoff protocols
- ✅ `CASE_STUDY_INTELLIGENCE.md` - 43 customer case studies analyzed
- ✅ `QUICKSTART.md` - Quick start guide (NEW)

### 3. Intelligence Data
- ✅ `data/case_studies.json` - 43 customer case studies
- ✅ `data/icp_intelligence.json` - ICP patterns and sweet spots
- ✅ `data/messaging_intelligence.json` - Value props by segment
- ✅ `data/customers_raw.csv` - Raw customer data

### 4. Processing Scripts
- ✅ `scripts/analyze_customer_icp.py` - Analyze customer CSV
- ✅ `scripts/parse_case_studies.py` - Parse case study text
- ✅ `scripts/process_case_studies.py` - Generate intelligence reports

### 5. Orchestration System (NEW)
- ✅ `orchestrator.py` - Main GTM orchestrator using Claude Code SDK
- ✅ `test_trial.py` - Comprehensive test scenarios
- ✅ `requirements.txt` - All dependencies
- ✅ `.env.example` - Environment configuration template

---

## 🚦 Activation Steps (Before First Run)

### Step 1: Install Dependencies

```bash
cd claude_code_sdk/mixmax_gtm_agent
pip install -r requirements.txt
```

**What this installs:**
- `claude-code-sdk>=0.0.20` - Core SDK for agent orchestration
- `python-dotenv` - Environment management
- `pandas`, `numpy` - Data processing
- Other utilities (requests, httpx, aiohttp, etc.)

### Step 2: Configure Environment

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
nano .env  # or use your preferred editor
```

**Minimum required:**
```
ANTHROPIC_API_KEY=sk-ant-api03-your-actual-key-here
```

**Optional (for full functionality):**
- CLAY_API_KEY - For LinkedIn/data sourcing
- APOLLO_API_KEY - For company/tech stack searches
- ZEROBOUNCE_API_KEY - For email verification
- INSTANTLY_API_KEY - For email sending platform
- (See .env.example for complete list)

### Step 3: Verify Setup

```bash
# Quick verification test
python -c "import claude_code_sdk; print('✅ SDK ready')"

# Check data files
ls -la data/*.json
```

### Step 4: Run Test Trial

```bash
# Run a simple ICP analysis test
python test_trial.py icp

# Or run all test scenarios
python test_trial.py all
```

**Test scenarios included:**
1. ICP Intelligence Analysis
2. Offer Strategy Development
3. Phase 1 Execution Planning
4. Agent Coordination Simulation

---

## 🎯 First Real Execution

Once tests pass, you can execute the actual Gutenberg Framework:

### Phase 1: Preparation (Week 0-1)

```python
from orchestrator import send_query
import asyncio

async def execute_phase_1():
    result = await send_query("""
    Execute Phase 1: List Building & Offer Creation

    I need you to coordinate the following:

    1. ACTIVATE List Builder Specialist to:
       - Plan data sourcing strategy (100K contact goal)
       - Identify 4 data sources (LinkedIn, Apollo, hiring signals, lookalikes)
       - Define intent scoring criteria

    2. ACTIVATE Offer Strategist to:
       - Mine our case studies for customer success patterns
       - Develop 5-7 offer variations
       - Create 3-5 message frameworks
       - Generate 15-20 testable combinations

    3. PREPARE Data Quality Engineer:
       - Define verification strategy (ZeroBounce/NeverBounce)
       - Set AI cleanup criteria based on ICP intelligence
       - Plan enrichment pipeline

    Use our ICP intelligence and case study data to inform all decisions.
    """)

    print(result[0])

asyncio.run(execute_phase_1())
```

### Phase 2: Testing (Week 2-3)

```python
async def execute_phase_2():
    result = await send_query("""
    Execute Phase 2: Rapid Arbitrage Testing

    Prerequisites check:
    - [ ] 40K+ verified contacts from Data Quality
    - [ ] 15-20 combinations from Offer Strategist
    - [ ] 10 warmed domains from Deliverability Engineer

    ACTIVATE Campaign Orchestrator to:
    1. Allocate 15K contacts for testing (1K per combination)
    2. Configure 15-20 test campaigns in Instantly/Smartlead
    3. Deploy 3-email sequences over 2 weeks
    4. Track: opens, replies, meetings
    5. Identify winners: <1% DEAD, 2-3% WINNER, >4% GOLD

    COORDINATE with Deliverability Engineer for:
    - Daily reputation monitoring
    - Domain health checks
    - Crisis response if needed
    """, continue_conversation=True)

    print(result[0])
```

---

## 📊 Success Indicators

After running test_trial.py, you should see:

✅ **ICP Analysis (Scenario 1)**
- Agent successfully reads `data/icp_intelligence.json`
- Identifies top 3 ICP sweet spots (e.g., Growth SaaS 51-500 employees)
- Lists primary buyer pain points
- Recommends target industries

✅ **Offer Strategy (Scenario 2)**
- Agent reads case study and messaging data
- Extracts top value proposition themes
- Identifies strongest pain points
- Suggests 3-5 testable offer ideas

✅ **Planning Mode (Scenario 3)**
- Agent creates detailed Phase 1 plan
- Lists specific tasks for each specialist
- Defines timeline and dependencies
- Sets success criteria

✅ **Coordination (Scenario 4)**
- Agent references handoff protocols
- Defines deliverables format
- Lists validation checks
- Specifies acceptance criteria

---

## 🚨 Troubleshooting

### Issue: ModuleNotFoundError: No module named 'claude_code_sdk'

**Solution:**
```bash
pip install claude-code-sdk>=0.0.20
```

### Issue: Missing API Key

**Error:** `anthropic.APIStatusError: Error code: 401`

**Solution:**
1. Check `.env` file exists in mixmax_gtm_agent directory
2. Verify `ANTHROPIC_API_KEY=sk-ant-api03-...` is set correctly
3. No quotes needed around the key in .env

### Issue: Can't find data files

**Error:** `FileNotFoundError: data/icp_intelligence.json`

**Solution:**
```bash
# Make sure you're in the right directory
cd /path/to/claude-cookbooks/claude_code_sdk/mixmax_gtm_agent

# Verify files exist
ls -la data/*.json
```

### Issue: Agent not activating specialists

**Problem:** Orchestrator isn't delegating to specialist agents

**Solution:**
- Check `.claude/agents/` directory exists with all 6 agent .md files
- Verify `CLAUDE.md` exists in root directory
- Ensure orchestrator.py has `"Task"` in allowed_tools list
- Use explicit activation language: "ACTIVATE [agent-name] to do X"

---

## 🎓 Learning Resources

### Example Queries to Try

**Query 1: Explore ICP Data**
```
Show me the top 5 customer case studies from our
highest-value segments and extract common patterns.
```

**Query 2: Generate Offer Ideas**
```
Based on our messaging intelligence, create 5 offer
ideas specifically for SaaS companies with 100-500
employees who are scaling their sales teams.
```

**Query 3: Plan List Building**
```
ACTIVATE the List Builder specialist to create a
detailed sourcing plan for 100K contacts targeting
our ICP sweet spots.
```

**Query 4: Multi-Agent Workflow**
```
Walk me through the complete handoff process from
List Builder → Data Quality → Campaign Orchestrator.
What data format is used at each stage?
```

### Understanding Agent Behavior

**Direct Execution:**
```python
result = await send_query("Analyze ICP data", permission_mode="default")
# Agent will read files, process data, return analysis
```

**Planning Mode:**
```python
result = await send_query("Plan Phase 1", permission_mode="plan")
# Agent will think through strategy without executing
```

**Conversation Continuation:**
```python
result1 = await send_query("What are our ICP sweet spots?")
result2 = await send_query(
    "Based on that, which industries should we target?",
    continue_conversation=True
)
# Second query has context from first
```

---

## ✨ What's Next?

After activation, you can:

1. **Execute Phase 1** - Start list building and offer creation
2. **Integrate Real Tools** - Connect Clay, Apollo, verification APIs
3. **Run Live Tests** - Deploy actual email campaigns
4. **Scale Winners** - Use Analytics Optimizer to scale successful campaigns
5. **Optimize Continuously** - Implement 70/30 rule and ICP refinement

---

## 📈 Expected Outcomes (8-Week Timeline)

Following the complete Gutenberg Framework:

| Metric | Target | Economic Value |
|--------|--------|----------------|
| Contacts tested | 15,000 | $75-150 cost |
| Reply rate | 2-4% | 300-500 replies |
| Meeting rate | 30-40% of replies | 100-200 meetings |
| Deal close rate | 10-20% of meetings | 15-30 deals |
| Revenue @ $5K ACV | 15-30 deals | $75K-150K |
| ROI | >5,000% | 8,200% typical |
| Cost per meeting | <$10 | vs. $200+ traditional |

---

## 🎉 Ready to Activate!

All components are built and ready. Just need to:

1. ✅ Install dependencies (`pip install -r requirements.txt`)
2. ✅ Configure API key (`.env` file)
3. ✅ Run test trial (`python test_trial.py all`)
4. 🚀 Execute Phase 1 of Gutenberg Framework

**Total time to activation: ~10 minutes**

---

*Built with Claude Code SDK v0.0.20+*
*Last updated: 2025-11-09*
