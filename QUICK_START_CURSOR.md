# Quick Start Guide for Cursor

## Where You Are

**Repository**: `/home/user/claude-cookbooks`
**Branch**: `claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV`
**Main Project**: `./claude_code_sdk/mixmax_gtm_agent/`

## Files Created for You

1. **CONVERSATION_EXPORT.md** - Summary of this conversation and repository state
2. **MIXMAX_AGENT_REFERENCE.md** - Complete reference guide for Mixmax GTM agents
3. **QUICK_START_CURSOR.md** - This file (navigation guide)

## Opening in Cursor

```bash
# Navigate to the repository
cd /home/user/claude-cookbooks

# Or open directly in Cursor
cursor /home/user/claude-cookbooks
```

## Important Files to Read First

### 1. Start Here
- `CONVERSATION_EXPORT.md` - Context from Claude conversation
- `MIXMAX_AGENT_REFERENCE.md` - Complete system reference

### 2. Main Documentation
- `claude_code_sdk/mixmax_gtm_agent/README.md` - System overview
- `claude_code_sdk/mixmax_gtm_agent/CLAUDE.md` - Main context for agents
- `claude_code_sdk/mixmax_gtm_agent/AGENT_SPECIALIZATION_STRATEGY.md` - Why specialized agents
- `claude_code_sdk/mixmax_gtm_agent/AGENT_INTERACTION_FLOW.md` - How agents coordinate

### 3. Agent Definitions (The Heart of the System)
All located in `claude_code_sdk/mixmax_gtm_agent/.claude/agents/`:

```
.claude/agents/
├── analytics-optimizer.md          # Agent 6: Scaling & optimization
├── campaign-orchestrator.md        # Agent 4: Testing & winner ID
├── competitive-intelligence.md     # Agent 8: Competitor contact extraction
├── data-quality-engineer.md        # Agent 2: Data verification & cleanup
├── deliverability-engineer.md      # Agent 5: Email infrastructure
├── icp-intelligence.md             # ICP intelligence specialist
├── list-builder.md                 # Agent 1: List building
├── market-intelligence.md          # Agent 7: Buying signal detection
└── offer-strategist.md             # Agent 3: Offer & message creation
```

### 4. Scripts
Located in `claude_code_sdk/mixmax_gtm_agent/scripts/`:

```
scripts/
├── analyze_customer_icp.py         # Analyze customer data for ICP patterns
├── parse_case_studies.py           # Parse case study data
└── process_case_studies.py         # Generate ICP + messaging intelligence
```

### 5. Commands
- `claude_code_sdk/mixmax_gtm_agent/.claude/commands/review-system.md` - Pre-launch review

### 6. Data Files
Check `data/` directory for:
- `case_studies.json` - 43 Mixmax customer case studies
- `icp_intelligence.json` - ICP patterns
- `messaging_intelligence.json` - Value propositions
- `competitors.json` - 60 competitors
- Various CSVs for contacts, test results, etc.

## File Paths Cheat Sheet

### Core Documentation
```
./CONVERSATION_EXPORT.md
./MIXMAX_AGENT_REFERENCE.md
./claude_code_sdk/mixmax_gtm_agent/README.md
./claude_code_sdk/mixmax_gtm_agent/CLAUDE.md
./claude_code_sdk/mixmax_gtm_agent/AGENT_SPECIALIZATION_STRATEGY.md
./claude_code_sdk/mixmax_gtm_agent/AGENT_INTERACTION_FLOW.md
./claude_code_sdk/mixmax_gtm_agent/ACTIVATION_CHECKLIST.md
```

### The 8 Agent Files
```
./claude_code_sdk/mixmax_gtm_agent/.claude/agents/list-builder.md
./claude_code_sdk/mixmax_gtm_agent/.claude/agents/data-quality-engineer.md
./claude_code_sdk/mixmax_gtm_agent/.claude/agents/offer-strategist.md
./claude_code_sdk/mixmax_gtm_agent/.claude/agents/campaign-orchestrator.md
./claude_code_sdk/mixmax_gtm_agent/.claude/agents/deliverability-engineer.md
./claude_code_sdk/mixmax_gtm_agent/.claude/agents/analytics-optimizer.md
./claude_code_sdk/mixmax_gtm_agent/.claude/agents/market-intelligence.md
./claude_code_sdk/mixmax_gtm_agent/.claude/agents/competitive-intelligence.md
```

### Scripts
```
./claude_code_sdk/mixmax_gtm_agent/scripts/analyze_customer_icp.py
./claude_code_sdk/mixmax_gtm_agent/scripts/parse_case_studies.py
./claude_code_sdk/mixmax_gtm_agent/scripts/process_case_studies.py
```

## Quick Commands in Cursor

### Git Operations
```bash
# Check current branch and status
git branch
git status

# View recent commits
git log --oneline -10

# View changes
git diff

# When ready to commit
git add .
git commit -m "Your descriptive message"
git push -u origin claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
```

### Navigate the Project
```bash
# Go to main agent directory
cd claude_code_sdk/mixmax_gtm_agent

# List all agent files
ls -la .claude/agents/

# View an agent file
cat .claude/agents/list-builder.md

# List scripts
ls -la scripts/

# Check data directory
ls -la ../../data/  # or wherever data is stored
```

### Run Scripts
```bash
# Generate ICP intelligence
cd claude_code_sdk/mixmax_gtm_agent
python scripts/process_case_studies.py

# Analyze customer data (if CSV exists)
python scripts/analyze_customer_icp.py ../../data/customers_raw.csv
```

### Search the Codebase
```bash
# Find all Python files
find . -name "*.py"

# Find all markdown files
find . -name "*.md"

# Search for specific text
grep -r "Gutenberg Framework" .

# Find files mentioning "competitive intelligence"
grep -r "competitive intelligence" . --include="*.md"
```

## Using Cursor AI

When working in Cursor, you can:

1. **Ask Cursor to explain files**:
   - Open any agent file and ask "Explain what this agent does"
   - Open the workflow diagram and ask "Explain this workflow"

2. **Ask for specific information**:
   - "Show me how the List Builder agent works"
   - "What are the success metrics for each agent?"
   - "How do agents hand off data to each other?"

3. **Make changes**:
   - "Update the List Builder agent to include X data source"
   - "Add a new metric to track Y"
   - "Create a new script to do Z"

4. **Navigate**:
   - Use `Cmd+P` (Mac) or `Ctrl+P` (Windows/Linux) to quickly open files
   - Search for files by name: "list-builder", "README", etc.

## What to Do Next

1. **Understand the System**:
   - Read `MIXMAX_AGENT_REFERENCE.md` for complete overview
   - Review the 8 agent files to understand each specialist's role
   - Check `AGENT_INTERACTION_FLOW.md` to see how they work together

2. **Explore the Code**:
   - Look at the Python scripts in `scripts/`
   - Check if data files exist in `data/` or nearby directories
   - Review any existing test results or outputs

3. **Make Changes** (if needed):
   - Modify agent definitions
   - Add new scripts
   - Update documentation
   - Add new data sources

4. **Commit Your Work**:
   - Stage changes: `git add .`
   - Commit: `git commit -m "Clear message"`
   - Push: `git push -u origin claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV`

## Need Help?

- All context is in `CONVERSATION_EXPORT.md`
- Full reference is in `MIXMAX_AGENT_REFERENCE.md`
- Original README is at `claude_code_sdk/mixmax_gtm_agent/README.md`

## Repository Remote

```
Origin: keeganmoody33/claude-cookbooks
Branch: claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
Remote URL: http://local_proxy@127.0.0.1:25697/git/keeganmoody33/claude-cookbooks
```

---

**You're all set!** Open the repository in Cursor and start exploring. All the context from our conversation is preserved in the export files.
