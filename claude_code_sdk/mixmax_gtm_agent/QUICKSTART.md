# Mixmax GTM Agent System - Quick Start Guide

Get up and running with the Mixmax GTM agent system in 5 minutes.

## Prerequisites

- Python 3.11+
- Anthropic API key

## Setup (5 minutes)

### 1. Install Dependencies

```bash
cd claude_code_sdk/mixmax_gtm_agent
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Anthropic API key
# Minimum required: ANTHROPIC_API_KEY=your_key_here
```

### 3. Run Test Trial

```bash
# Run a simple test to verify everything works
python test_trial.py icp
```

This will:
- Load the GTM Orchestrator agent
- Analyze ICP intelligence data
- Demonstrate agent coordination

## Usage Examples

### Example 1: Run All Test Scenarios

```bash
python test_trial.py all
```

This runs 4 test scenarios:
1. ICP Intelligence Analysis
2. Offer Strategy Development
3. Phase 1 Execution Planning
4. Agent Coordination Simulation

### Example 2: Run Individual Scenarios

```bash
# ICP analysis
python test_trial.py icp

# Offer strategy
python test_trial.py offer

# Planning mode
python test_trial.py plan

# Coordination demo
python test_trial.py coordination
```

### Example 3: Use Orchestrator Directly

```python
import asyncio
from orchestrator import send_query

async def my_query():
    result, messages = await send_query("""
    Help me analyze our ICP data and suggest
    the top 3 industries to target for list building.
    """)
    print(result)

asyncio.run(my_query())
```

### Example 4: Interactive Python Session

```python
from orchestrator import send_query
import asyncio

# Run a query
result = asyncio.run(send_query("What are our ICP sweet spots?"))
print(result[0])

# Continue conversation
result = asyncio.run(send_query(
    "Based on that, suggest 5 offer ideas",
    continue_conversation=True
))
```

## Available Specialist Agents

The orchestrator can activate these specialists via the Task tool:

1. **list-builder** - Build 100K+ contact databases
2. **data-quality-engineer** - Verify and clean data
3. **offer-strategist** - Create offers and messaging
4. **campaign-orchestrator** - Run A/B tests
5. **deliverability-engineer** - Manage email infrastructure
6. **analytics-optimizer** - Scale and optimize

## Data & Intelligence

The system includes pre-analyzed intelligence:

- **data/case_studies.json** - 43 customer case studies
- **data/icp_intelligence.json** - ICP patterns and sweet spots
- **data/messaging_intelligence.json** - Value props and pain points

## Scripts

Automation scripts in `scripts/`:

```bash
# Analyze customer data for ICP patterns
python scripts/analyze_customer_icp.py data/customers_raw.csv

# Process case studies to generate intelligence
python scripts/process_case_studies.py
```

## Execution Phases

### Phase 1: Preparation (Week 0-1)
```python
result = await send_query("""
Execute Phase 1: List Building & Offer Creation

1. Activate List Builder to plan 100K contact sourcing strategy
2. Activate Offer Strategist to develop 15-20 test combinations
3. Prepare Data Quality Engineer verification pipeline
""")
```

### Phase 2: Testing (Week 2-3)
```python
result = await send_query("""
Execute Phase 2: Rapid Testing

1. Activate Campaign Orchestrator to configure 15 test campaigns
2. Coordinate with Deliverability Engineer for domain setup
3. Deploy 15K contacts across combinations
4. Identify winners (>2% reply rate)
""")
```

### Phase 3: Scaling (Week 4-5)
```python
result = await send_query("""
Execute Phase 3: Scale Winners

1. Activate Analytics Optimizer with winner data
2. Allocate 30K reserve contacts to winning campaigns
3. Monitor performance and detect degradation
""")
```

### Phase 4: Optimization (Week 6-8)
```python
result = await send_query("""
Execute Phase 4: Continuous Optimization

1. Run 70/30 rule (70% proven, 30% new tests)
2. Analyze winner characteristics
3. Refine ICP based on performance data
4. Feed insights back to List Builder
""")
```

## Permission Modes

Control agent behavior with permission modes:

```python
# Default: Execute actions
result = await send_query("Build a list", permission_mode="default")

# Plan: Think only, don't execute
result = await send_query("Plan Phase 1", permission_mode="plan")

# Accept edits: Interactive editing mode
result = await send_query("Edit this doc", permission_mode="acceptEdits")
```

## Troubleshooting

### ImportError: No module named 'claude_code_sdk'

```bash
pip install claude-code-sdk>=0.0.20
```

### Missing API Key Error

Make sure `.env` exists and contains:
```
ANTHROPIC_API_KEY=your_actual_key_here
```

### Can't find data files

Ensure you're running from the mixmax_gtm_agent directory:
```bash
cd claude_code_sdk/mixmax_gtm_agent
python test_trial.py
```

## Next Steps

1. ✅ Run `python test_trial.py all` to verify setup
2. 📖 Read [AGENT_SPECIALIZATION_STRATEGY.md](AGENT_SPECIALIZATION_STRATEGY.md) for detailed strategy
3. 🔄 Review [AGENT_INTERACTION_FLOW.md](AGENT_INTERACTION_FLOW.md) for handoff protocols
4. 📊 Explore intelligence data in `data/` directory
5. 🚀 Start executing Phase 1 with real data

## Support

- Full documentation: [README.md](README.md)
- Agent strategy: [AGENT_SPECIALIZATION_STRATEGY.md](AGENT_SPECIALIZATION_STRATEGY.md)
- Case studies: [CASE_STUDY_INTELLIGENCE.md](CASE_STUDY_INTELLIGENCE.md)
- Claude Code SDK: https://github.com/anthropics/claude-code-sdk-python

## Expected Results (8-Week Timeline)

Following the complete framework:
- 300-500 replies
- 100-200 meetings booked
- 15-30 deals closed
- $75K-150K revenue
- 5,000-10,000% ROI
- <$10 cost per meeting
