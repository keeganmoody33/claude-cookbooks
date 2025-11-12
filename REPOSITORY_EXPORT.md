# Repository Export - keeganmoody33/claude-cookbooks

**Generated**: 2025-11-12
**Repository**: keeganmoody33/claude-cookbooks
**Branch**: claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
**Working Directory**: /home/user/claude-cookbooks

---

## Table of Contents

1. [Repository Overview](#repository-overview)
2. [Quick Start](#quick-start)
3. [Directory Structure](#directory-structure)
4. [Primary Project: Mixmax GTM Agent System](#primary-project-mixmax-gtm-agent-system)
5. [Additional Projects](#additional-projects)
6. [Data Files](#data-files)
7. [Git Information](#git-information)
8. [Export Instructions](#export-instructions)
9. [Complete File Listing](#complete-file-listing)

---

## Repository Overview

This repository contains the **Claude Cookbooks** collection with a focus on the **Mixmax GTM Agent System** - an advanced multi-agent system for go-to-market operations.

### What's in This Repository

- **Primary Focus**: Mixmax GTM Agent System (8 specialized agents)
- **Additional Agent Systems**: Chief of Staff, Observability, Research agents
- **Claude Cookbooks**: Skills, patterns, examples, and third-party integrations
- **Documentation**: Comprehensive guides, strategies, and workflows
- **Data**: Customer case studies, competitor intelligence, ICP data
- **Scripts**: Python utilities for data processing and analysis

### Key Statistics

- **Total Agent Definitions**: 12+ specialized agents
- **Documentation Files**: 30+ markdown files
- **Python Scripts**: 15+ utility and agent scripts
- **Data Files**: 15+ JSON/CSV files with real intelligence
- **Case Studies**: 43 Mixmax customer success stories
- **Competitor Data**: 60 tracked competitors

---

## Quick Start

### For Cursor Users

```bash
# Open in Cursor
cursor /home/user/claude-cookbooks

# Read these files first:
1. CONVERSATION_EXPORT.md - Conversation context
2. MIXMAX_AGENT_REFERENCE.md - Complete system reference
3. QUICK_START_CURSOR.md - Navigation guide
4. COMPLETE_FILE_INVENTORY.md - File inventory
```

### For Claude Code Users

```bash
# Navigate to repository
cd /home/user/claude-cookbooks

# Start with main documentation
cat claude_code_sdk/mixmax_gtm_agent/README.md

# View agent definitions
ls -la claude_code_sdk/mixmax_gtm_agent/.claude/agents/

# Check data files
ls -la claude_code_sdk/mixmax_gtm_agent/data/
```

### For General Use

```bash
# Clone the repository
git clone https://github.com/keeganmoody33/claude-cookbooks.git
cd claude-cookbooks

# Switch to the feature branch
git checkout claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV

# Explore the Mixmax GTM Agent System
cd claude_code_sdk/mixmax_gtm_agent
```

---

## Directory Structure

```
claude-cookbooks/
│
├── 📄 Export Files (Created for easy navigation)
│   ├── REPOSITORY_EXPORT.md          ⭐ This file - Complete export
│   ├── CONVERSATION_EXPORT.md         ⭐ Conversation context
│   ├── MIXMAX_AGENT_REFERENCE.md      ⭐ System reference
│   ├── QUICK_START_CURSOR.md          ⭐ Cursor quick start
│   └── COMPLETE_FILE_INVENTORY.md     ⭐ File inventory
│
├── 📁 claude_code_sdk/                🎯 MAIN PROJECTS
│   ├── mixmax_gtm_agent/              🚀 PRIMARY PROJECT
│   │   ├── .claude/
│   │   │   ├── agents/                🤖 8 Specialized Agents
│   │   │   │   ├── list-builder.md
│   │   │   │   ├── data-quality-engineer.md
│   │   │   │   ├── offer-strategist.md
│   │   │   │   ├── campaign-orchestrator.md
│   │   │   │   ├── deliverability-engineer.md
│   │   │   │   ├── analytics-optimizer.md
│   │   │   │   ├── market-intelligence.md
│   │   │   │   ├── competitive-intelligence.md
│   │   │   │   └── icp-intelligence.md
│   │   │   └── commands/
│   │   │       └── review-system.md
│   │   ├── scripts/                   🐍 Python Scripts
│   │   │   ├── analyze_customer_icp.py
│   │   │   ├── parse_case_studies.py
│   │   │   └── process_case_studies.py
│   │   ├── data/                      📊 Intelligence Data
│   │   │   ├── case_studies.json      (43 customer stories)
│   │   │   ├── competitors.json       (60 competitors)
│   │   │   ├── customers_raw.csv
│   │   │   ├── icp_intelligence.json
│   │   │   └── messaging_intelligence.json
│   │   ├── orchestrator.py            🎯 Main orchestrator
│   │   ├── test_trial.py
│   │   └── 📘 Documentation (9 files)
│   │       ├── README.md
│   │       ├── CLAUDE.md
│   │       ├── AGENT_SPECIALIZATION_STRATEGY.md
│   │       ├── AGENT_INTERACTION_FLOW.md
│   │       ├── CASE_STUDY_INTELLIGENCE.md
│   │       ├── ACTIVATION_CHECKLIST.md
│   │       ├── LAUNCH_INSTRUCTIONS.md
│   │       ├── QUICKSTART.md
│   │       └── REVIEW_GUIDE.md
│   │
│   ├── chief_of_staff_agent/          💼 Chief of Staff Agent
│   │   ├── .claude/
│   │   │   ├── agents/
│   │   │   │   ├── financial-analyst.md
│   │   │   │   └── recruiter.md
│   │   │   ├── commands/
│   │   │   └── hooks/
│   │   ├── scripts/
│   │   ├── financial_data/
│   │   └── audit/
│   │
│   ├── observability_agent/           📊 Observability Agent
│   └── research_agent/                🔬 Research Agent
│
├── 📁 data/
│   └── mixmax-icp/                    📊 Additional ICP Data
│       ├── MIXMAX_ICP_MASTER.csv
│       ├── MIXMAX_ICP_SUMMARY.json
│       └── PROSPECTING_PARAMETERS.md
│
├── 📁 skills/                         🎓 Claude Skills Examples
│   ├── classification/
│   ├── retrieval_augmented_generation/
│   ├── summarization/
│   ├── text_to_sql/
│   └── contextual-embeddings/
│
├── 📁 patterns/                       📐 Design Patterns
│   └── agents/
│
├── 📁 third_party/                    🔌 Third-Party Integrations
│   ├── VoyageAI/
│   ├── LlamaIndex/
│   └── Deepgram/
│
├── 📁 tool_use/                       🛠️ Tool Use Examples
├── 📁 multimodal/                     🖼️ Multimodal Examples
├── 📁 extended_thinking/              🧠 Extended Thinking
├── 📁 finetuning/                     ⚙️ Fine-tuning
├── 📁 anthropic_cookbook/             📚 Anthropic Cookbook
│
├── .claude/                           ⚙️ Claude Configuration
│   └── commands/
│       ├── link-review.md
│       ├── model-check.md
│       └── notebook-review.md
│
├── .github/                           🔧 GitHub Workflows
│   └── workflows/
│
├── README.md                          📘 Main README
├── CONTRIBUTING.md                    📝 Contributing Guide
├── LICENSE                            ⚖️ License
├── requirements.txt                   📦 Dependencies
└── pyproject.toml                     🔧 Project Config
```

---

## Primary Project: Mixmax GTM Agent System

**Location**: `./claude_code_sdk/mixmax_gtm_agent/`

### Overview

The Mixmax GTM Agent System is an advanced multi-agent system designed for go-to-market operations. It consists of 8 specialized agents working together to execute demand generation campaigns from list building through optimization.

### The 8 Specialized Agents

1. **List Builder** (`list-builder.md`) - 5.6 KB
   - Multi-channel data sourcing
   - Intent signal scoring
   - Builds 100K+ contact pools

2. **Data Quality Engineer** (`data-quality-engineer.md`) - 9.3 KB
   - Email verification
   - AI-powered ICP filtering
   - Data enrichment & cleanup

3. **Offer Strategist** (`offer-strategist.md`) - 10.3 KB
   - Customer success story mining
   - Offer development (5-7 variations)
   - 3-email sequence design

4. **Campaign Orchestrator** (`campaign-orchestrator.md`) - 10.7 KB
   - Combination matrix mathematics
   - Contact allocation (15K testing, 25K-35K reserve)
   - Winner identification

5. **Deliverability Engineer** (`deliverability-engineer.md`) - 13.1 KB
   - Domain portfolio management (10-20 domains)
   - DNS configuration (SPF, DKIM, DMARC)
   - Warmup strategy

6. **Analytics Optimizer** (`analytics-optimizer.md`) - 14.2 KB
   - Winner scaling strategy
   - Performance monitoring
   - Continuous optimization (70/30 rule)

7. **Market Intelligence** (`market-intelligence.md`) - 22.2 KB
   - Job market monitoring
   - Buying signal detection
   - High-intent lead generation

8. **Competitive Intelligence** (`competitive-intelligence.md`) - 30.7 KB
   - Competitor engagement scraping
   - Contact extraction from reviews
   - Displacement campaign support

9. **ICP Intelligence** (`icp-intelligence.md`) - 10.7 KB
   - ICP analysis and refinement
   - Pattern identification

### Core Documentation Files

| File | Size | Purpose |
|------|------|---------|
| `README.md` | 577 lines | System overview, workflow, getting started |
| `CLAUDE.md` | - | Main context for all agents |
| `AGENT_SPECIALIZATION_STRATEGY.md` | 543 lines | Why specialized agents, ROI calculations |
| `AGENT_INTERACTION_FLOW.md` | 633 lines | Coordination protocols, handoff specs |
| `CASE_STUDY_INTELLIGENCE.md` | - | 43 customer case studies, ICP patterns |
| `ACTIVATION_CHECKLIST.md` | - | Pre-launch checklist |
| `LAUNCH_INSTRUCTIONS.md` | - | Launch guide |
| `QUICKSTART.md` | - | Quick start guide |
| `REVIEW_GUIDE.md` | - | System review guide |

### Python Scripts

Located in `./claude_code_sdk/mixmax_gtm_agent/scripts/`:

1. **analyze_customer_icp.py**
   - Analyzes customer CSV data
   - Extracts ICP patterns
   - Identifies sweet spots

2. **parse_case_studies.py**
   - Parses case study data
   - Extracts key information

3. **process_case_studies.py**
   - Generates ICP intelligence
   - Creates messaging intelligence
   - Produces structured outputs

### Data Files

Located in `./claude_code_sdk/mixmax_gtm_agent/data/`:

| File | Content | Purpose |
|------|---------|---------|
| `case_studies.json` | 43 case studies | Real customer problems, solutions, patterns |
| `competitors.json` | 60 competitors | Competitive landscape, monitoring priorities |
| `customers_raw.csv` | Customer data | Raw data for ICP analysis |
| `icp_intelligence.json` | ICP patterns | Sweet spots, triggers, success factors |
| `messaging_intelligence.json` | Messaging guide | Value props, pain points by segment |

### Commands

- **review-system.md** - Pre-launch comprehensive system review
  - Architecture validation
  - Gap analysis
  - Risk identification
  - Production readiness check

### Workflow Summary

```
1. List Builder → 100K+ raw contacts
2. Data Quality Engineer → 40K-50K verified contacts
3. Offer Strategist → 5-7 offer variations + messaging
4. Campaign Orchestrator → Test combinations, identify winners
5. Deliverability Engineer → Infrastructure & reputation
6. Analytics Optimizer → Scale winners, optimize continuously
7. Market Intelligence → High-intent leads from buying signals
8. Competitive Intelligence → Competitor contact extraction
```

---

## Additional Projects

### Chief of Staff Agent

**Location**: `./claude_code_sdk/chief_of_staff_agent/`

Executive assistant agent with financial analysis and recruiting capabilities.

**Agents**:
- `financial-analyst.md` - Financial forecasting and analysis
- `recruiter.md` - Talent acquisition and screening

**Commands**:
- `budget-impact.md` - Budget impact analysis
- `strategic-brief.md` - Strategic briefing generation
- `talent-scan.md` - Talent market scanning

**Features**:
- Custom hooks for tracking (Python)
- Output style customization
- Audit logging (JSON)
- Financial data analysis

### Observability Agent

**Location**: `./claude_code_sdk/observability_agent/`

System monitoring and observability agent.

### Research Agent

**Location**: `./claude_code_sdk/research_agent/`

Research and information gathering agent.

---

## Data Files

### Mixmax GTM Agent Data

**Location**: `./claude_code_sdk/mixmax_gtm_agent/data/`

- ✅ **case_studies.json** - 43 Mixmax customer case studies
- ✅ **competitors.json** - 60 direct/indirect competitors
- ✅ **customers_raw.csv** - Raw customer data
- ✅ **icp_intelligence.json** - ICP patterns and sweet spots
- ✅ **messaging_intelligence.json** - Value propositions by segment

### Additional ICP Data

**Location**: `./data/mixmax-icp/`

- ✅ **MIXMAX_ICP_MASTER.csv** - Master ICP dataset
- ✅ **MIXMAX_ICP_SUMMARY.json** - ICP summary and insights
- ✅ **PROSPECTING_PARAMETERS.md** - Prospecting parameter guide
- ✅ **ENRICHMENT_SUMMARY.md** - Data enrichment summary
- ✅ **README.md** - ICP data documentation

### Chief of Staff Agent Data

**Location**: `./claude_code_sdk/chief_of_staff_agent/`

- `financial_data/burn_rate.csv`
- `financial_data/hiring_costs.csv`
- `financial_data/revenue_forecast.json`
- `audit/report_history.json`
- `audit/script_usage_log.json`

---

## Git Information

### Repository Details

```bash
Repository: keeganmoody33/claude-cookbooks
Current Branch: claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
Remote URL: http://local_proxy@127.0.0.1:20295/git/keeganmoody33/claude-cookbooks
```

### Recent Commits

```
7969aa0 Add Cursor export files with complete system documentation
1444adf Integrate 280-customer ICP dataset into Mixmax GTM agent system
783ee36 Add comprehensive pre-launch review system for Mixmax GTM agents
6c5dcdd Refactor intelligence agents: Add market intelligence and refocus competitive intelligence
2ba3752 Add Competitive Intelligence agent and 60-competitor dataset
```

### Working Tree Status

Clean - No uncommitted changes

### Git Operations

```bash
# Check status
git status

# View history
git log --oneline -10

# Push changes
git push -u origin claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV

# Create new branch
git checkout -b your-branch-name

# View all branches
git branch -a
```

---

## Export Instructions

### Export to Cursor

1. **Open in Cursor**:
   ```bash
   cursor /home/user/claude-cookbooks
   ```

2. **Read These First**:
   - `CONVERSATION_EXPORT.md` - Get conversation context
   - `MIXMAX_AGENT_REFERENCE.md` - Understand the system
   - `QUICK_START_CURSOR.md` - Navigate efficiently
   - `COMPLETE_FILE_INVENTORY.md` - See all files

3. **Navigate to Main Project**:
   ```bash
   cd claude_code_sdk/mixmax_gtm_agent
   ```

### Export to Another System

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/keeganmoody33/claude-cookbooks.git
   cd claude-cookbooks
   ```

2. **Switch to Feature Branch**:
   ```bash
   git checkout claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   # or
   uv pip install -r requirements.txt
   ```

4. **Explore the System**:
   ```bash
   cd claude_code_sdk/mixmax_gtm_agent
   cat README.md
   ls -la .claude/agents/
   ```

### Export to Documentation

To export this system as documentation:

1. **Core Documentation Bundle**:
   - `REPOSITORY_EXPORT.md` (this file)
   - `MIXMAX_AGENT_REFERENCE.md`
   - `claude_code_sdk/mixmax_gtm_agent/README.md`
   - `claude_code_sdk/mixmax_gtm_agent/AGENT_SPECIALIZATION_STRATEGY.md`
   - `claude_code_sdk/mixmax_gtm_agent/AGENT_INTERACTION_FLOW.md`

2. **Agent Definitions Bundle**:
   - All 9 files from `.claude/agents/`

3. **Data Bundle**:
   - All 5 files from `data/`

### Export for Backup

```bash
# Create a complete archive
cd /home/user
tar -czf claude-cookbooks-backup-$(date +%Y%m%d).tar.gz claude-cookbooks/

# Or zip
zip -r claude-cookbooks-backup-$(date +%Y%m%d).zip claude-cookbooks/
```

---

## Complete File Listing

### Export Files (Root)

```
REPOSITORY_EXPORT.md          ⭐ This file - Complete export
CONVERSATION_EXPORT.md         ⭐ Conversation context
MIXMAX_AGENT_REFERENCE.md      ⭐ System reference
QUICK_START_CURSOR.md          ⭐ Cursor quick start
COMPLETE_FILE_INVENTORY.md     ⭐ File inventory
```

### Mixmax GTM Agent System Files

**Documentation** (9 files):
```
claude_code_sdk/mixmax_gtm_agent/README.md
claude_code_sdk/mixmax_gtm_agent/CLAUDE.md
claude_code_sdk/mixmax_gtm_agent/AGENT_SPECIALIZATION_STRATEGY.md
claude_code_sdk/mixmax_gtm_agent/AGENT_INTERACTION_FLOW.md
claude_code_sdk/mixmax_gtm_agent/CASE_STUDY_INTELLIGENCE.md
claude_code_sdk/mixmax_gtm_agent/ACTIVATION_CHECKLIST.md
claude_code_sdk/mixmax_gtm_agent/LAUNCH_INSTRUCTIONS.md
claude_code_sdk/mixmax_gtm_agent/QUICKSTART.md
claude_code_sdk/mixmax_gtm_agent/REVIEW_GUIDE.md
```

**Agent Definitions** (9 files):
```
claude_code_sdk/mixmax_gtm_agent/.claude/agents/list-builder.md
claude_code_sdk/mixmax_gtm_agent/.claude/agents/data-quality-engineer.md
claude_code_sdk/mixmax_gtm_agent/.claude/agents/offer-strategist.md
claude_code_sdk/mixmax_gtm_agent/.claude/agents/campaign-orchestrator.md
claude_code_sdk/mixmax_gtm_agent/.claude/agents/deliverability-engineer.md
claude_code_sdk/mixmax_gtm_agent/.claude/agents/analytics-optimizer.md
claude_code_sdk/mixmax_gtm_agent/.claude/agents/market-intelligence.md
claude_code_sdk/mixmax_gtm_agent/.claude/agents/competitive-intelligence.md
claude_code_sdk/mixmax_gtm_agent/.claude/agents/icp-intelligence.md
```

**Commands** (1 file):
```
claude_code_sdk/mixmax_gtm_agent/.claude/commands/review-system.md
```

**Python Scripts** (3 files):
```
claude_code_sdk/mixmax_gtm_agent/scripts/analyze_customer_icp.py
claude_code_sdk/mixmax_gtm_agent/scripts/parse_case_studies.py
claude_code_sdk/mixmax_gtm_agent/scripts/process_case_studies.py
```

**Python Code** (2 files):
```
claude_code_sdk/mixmax_gtm_agent/orchestrator.py
claude_code_sdk/mixmax_gtm_agent/test_trial.py
```

**Data Files** (5 files):
```
claude_code_sdk/mixmax_gtm_agent/data/case_studies.json
claude_code_sdk/mixmax_gtm_agent/data/competitors.json
claude_code_sdk/mixmax_gtm_agent/data/customers_raw.csv
claude_code_sdk/mixmax_gtm_agent/data/icp_intelligence.json
claude_code_sdk/mixmax_gtm_agent/data/messaging_intelligence.json
```

### Chief of Staff Agent Files

**Agent Definitions** (2 files):
```
claude_code_sdk/chief_of_staff_agent/.claude/agents/financial-analyst.md
claude_code_sdk/chief_of_staff_agent/.claude/agents/recruiter.md
```

**Commands** (4 files):
```
claude_code_sdk/chief_of_staff_agent/.claude/commands/budget-impact.md
claude_code_sdk/chief_of_staff_agent/.claude/commands/slash-command-test.md
claude_code_sdk/chief_of_staff_agent/.claude/commands/strategic-brief.md
claude_code_sdk/chief_of_staff_agent/.claude/commands/talent-scan.md
```

**Scripts** (5 files):
```
claude_code_sdk/chief_of_staff_agent/scripts/decision_matrix.py
claude_code_sdk/chief_of_staff_agent/scripts/financial_forecast.py
claude_code_sdk/chief_of_staff_agent/scripts/hiring_impact.py
claude_code_sdk/chief_of_staff_agent/scripts/simple_calculation.py
claude_code_sdk/chief_of_staff_agent/scripts/talent_scorer.py
```

### Repository Root Files

```
README.md                     Main repository README
CONTRIBUTING.md               Contribution guidelines
LICENSE                       License file
requirements.txt              Python dependencies
requirements-dev.txt          Development dependencies
pyproject.toml                Python project config
uv.toml                       UV package manager config
uv.lock                       UV lock file
.env.example                  Environment variable template
.gitignore                    Git ignore rules
lychee.toml                   Link checker config
.pre-commit-config.yaml       Pre-commit hooks
```

---

## Quick Reference Commands

### Navigate to Key Locations

```bash
# Main project
cd claude_code_sdk/mixmax_gtm_agent

# View agents
cd claude_code_sdk/mixmax_gtm_agent/.claude/agents

# View scripts
cd claude_code_sdk/mixmax_gtm_agent/scripts

# View data
cd claude_code_sdk/mixmax_gtm_agent/data

# ICP data
cd data/mixmax-icp
```

### Search the Repository

```bash
# Find all agent files
find . -path "*/.claude/agents/*.md"

# Find all Python scripts
find . -name "*.py" -path "*/scripts/*"

# Find all data files
find . -name "*.json" -o -name "*.csv" | grep -v ".git"

# Search for specific content
grep -r "Gutenberg Framework" . --include="*.md"
```

### View Files

```bash
# View main README
cat claude_code_sdk/mixmax_gtm_agent/README.md

# View an agent
cat claude_code_sdk/mixmax_gtm_agent/.claude/agents/list-builder.md

# List all agents with sizes
ls -lh claude_code_sdk/mixmax_gtm_agent/.claude/agents/

# View data file
cat claude_code_sdk/mixmax_gtm_agent/data/icp_intelligence.json | jq
```

---

## File Statistics

### Mixmax GTM Agent System
- Documentation: 9 markdown files
- Agent Definitions: 9 agent files
- Commands: 1 command file
- Python Scripts: 3 files
- Python Code: 2 files
- Data Files: 5 files
- **Total**: 29 files

### Chief of Staff Agent
- Documentation: 3 markdown files
- Agent Definitions: 2 files
- Commands: 4 files
- Scripts: 5 Python files
- Hooks: 2 Python files
- Data Files: 5 files
- **Total**: 21 files

### Total Repository
- Markdown Files: 80+ files
- Python Files: 40+ files
- JSON Files: 20+ files
- CSV Files: 10+ files
- **Total**: 150+ tracked files

---

## Next Steps

### If You're New to This Repository

1. **Read the Context**:
   - Start with `CONVERSATION_EXPORT.md`
   - Then read `MIXMAX_AGENT_REFERENCE.md`

2. **Understand the Main Project**:
   - Read `claude_code_sdk/mixmax_gtm_agent/README.md`
   - Review `AGENT_SPECIALIZATION_STRATEGY.md`
   - Check `AGENT_INTERACTION_FLOW.md`

3. **Explore the Agents**:
   - Browse the 9 agent files in `.claude/agents/`
   - Understand their roles and coordination

4. **Check the Data**:
   - Review the 5 data files
   - Understand what intelligence is available

### If You're Ready to Work

1. **Set Up Your Environment**:
   ```bash
   cd /home/user/claude-cookbooks
   pip install -r requirements.txt
   ```

2. **Run the Scripts**:
   ```bash
   cd claude_code_sdk/mixmax_gtm_agent
   python scripts/process_case_studies.py
   ```

3. **Make Changes**:
   - Modify agent definitions as needed
   - Update documentation
   - Add new scripts or data

4. **Commit Your Work**:
   ```bash
   git add .
   git commit -m "Your descriptive message"
   git push -u origin claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
   ```

---

## Support & Documentation

### Internal Documentation
- `MIXMAX_AGENT_REFERENCE.md` - Complete system reference
- `QUICK_START_CURSOR.md` - Quick start for Cursor
- `COMPLETE_FILE_INVENTORY.md` - Complete file inventory

### Project Documentation
- `claude_code_sdk/mixmax_gtm_agent/README.md` - Main README
- `claude_code_sdk/mixmax_gtm_agent/REVIEW_GUIDE.md` - Review guide
- `claude_code_sdk/mixmax_gtm_agent/LAUNCH_INSTRUCTIONS.md` - Launch guide

---

## Export Metadata

**Created**: 2025-11-12
**Export Type**: Complete Repository Export
**Format**: Markdown Documentation
**Source**: keeganmoody33/claude-cookbooks
**Branch**: claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
**Working Directory**: /home/user/claude-cookbooks

---

**You now have a complete export of the repository!**

This file serves as your comprehensive guide to understanding, navigating, and working with the claude-cookbooks repository, with a special focus on the Mixmax GTM Agent System.
