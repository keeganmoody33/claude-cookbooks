# Claude Conversation Export
**Date**: 2025-11-12
**Repository**: keeganmoody33/claude-cookbooks
**Branch**: `claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV`

## Current Repository State

### Git Status
- **Current Branch**: `claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV`
- **Status**: Clean (no uncommitted changes)
- **Working Directory**: `/home/user/claude-cookbooks`

### Recent Commits
```
1444adf Integrate 280-customer ICP dataset into Mixmax GTM agent system
783ee36 Add comprehensive pre-launch review system for Mixmax GTM agents
6c5dcdd Refactor intelligence agents: Add market intelligence and refocus competitive intelligence
2ba3752 Add Competitive Intelligence agent and 60-competitor dataset
ce95294 Add orchestrator and test infrastructure for Mixmax GTM agents
```

## Repository Structure

### Key Directories
```
claude-cookbooks/
├── claude_code_sdk/
│   ├── mixmax_gtm_agent/          # Main Mixmax GTM Agent System
│   │   ├── .claude/
│   │   │   ├── agents/            # Specialized agent definitions
│   │   │   └── commands/
│   │   ├── scripts/
│   │   ├── README.md
│   │   ├── CLAUDE.md
│   │   ├── AGENT_INTERACTION_FLOW.md
│   │   ├── AGENT_SPECIALIZATION_STRATEGY.md
│   │   └── ACTIVATION_CHECKLIST.md
│   ├── chief_of_staff_agent/
│   ├── observability_agent/
│   └── research_agent/
├── data/                           # Data files
├── skills/
├── tool_use/
├── multimodal/
└── third_party/
```

## Mixmax GTM Agent System

### Specialized Agents Found
Located in `./claude_code_sdk/mixmax_gtm_agent/.claude/agents/`:

1. **data-quality-engineer.md** - Data quality management
2. **campaign-orchestrator.md** - Campaign orchestration
3. **offer-strategist.md** - Offer strategy
4. **analytics-optimizer.md** - Analytics optimization
5. **deliverability-engineer.md** - Email deliverability
6. **list-builder.md** - List building
7. **icp-intelligence.md** - ICP (Ideal Customer Profile) intelligence
8. **market-intelligence.md** - Market intelligence
9. **competitive-intelligence.md** - Competitive intelligence

### Key Scripts
Located in `./claude_code_sdk/mixmax_gtm_agent/scripts/`:
- `analyze_customer_icp.py` - Customer ICP analysis
- `process_case_studies.py` - Case study processing
- `parse_case_studies.py` - Case study parsing

### Documentation Files
- `README.md` - Main documentation
- `CLAUDE.md` - Claude-specific documentation
- `AGENT_INTERACTION_FLOW.md` - How agents interact
- `AGENT_SPECIALIZATION_STRATEGY.md` - Agent specialization approach
- `ACTIVATION_CHECKLIST.md` - Pre-launch checklist

## Conversation Summary

### Initial Questions Asked
1. What is the exact GitHub repository URL?
   - **Answer**: Already in `keeganmoody33/claude-cookbooks`

2. What agent information from Claude web should be included?
   - **Status**: User clarified they need to export conversation to Cursor

3. What should be done with the repository?
   - **Status**: Repository already cloned and on correct branch

### User's Current Need
- Export this conversation thread to use in Cursor IDE
- Thread is too long to easily copy-paste
- Wants to preserve the work and context

## What to Do in Cursor

1. **Open the repository**: Open `/home/user/claude-cookbooks` in Cursor
2. **Check out the branch**:
   ```bash
   git checkout claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
   ```
3. **Main working directory**: `./claude_code_sdk/mixmax_gtm_agent/`
4. **Review recent changes**: Check the commit history to see what's been done

## Next Steps - Define Your Task

To continue working on this project, please specify what you need:

### Option 1: Agent Development
- Add new agent capabilities
- Modify existing agents
- Create new specialized agents

### Option 2: Data Integration
- Add new datasets (ICP, competitors, case studies)
- Process existing data
- Create data pipelines

### Option 3: System Enhancement
- Improve agent orchestration
- Add new tools or integrations
- Enhance testing infrastructure

### Option 4: Documentation
- Document existing systems
- Create user guides
- Add API documentation

### Option 5: Testing & QA
- Add test coverage
- Run pre-launch reviews
- Validate agent behavior

### Option 6: Export/Import from Claude Web
- Export specific Claude project data
- Import agent configurations
- Sync with Claude web workspace

## Important Git Commands

### Push changes when ready:
```bash
git add .
git commit -m "Your descriptive message"
git push -u origin claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
```

### Check status:
```bash
git status
git log --oneline -5
```

### Fetch latest:
```bash
git fetch origin claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
git pull origin claude/mixmax-agent-specialization-011CUxTM7tEJHnJT6hRqy3AV
```

## Repository Access
- **Remote URL**: `http://local_proxy@127.0.0.1:25697/git/keeganmoody33/claude-cookbooks`
- **Branch must start with**: `claude/` and end with session ID
- **Current session ID**: `011CUxTM7tEJHnJT6hRqy3AV`

## Environment Setup

### Python Requirements
The repository uses:
- `requirements.txt` - Main dependencies
- `requirements-dev.txt` - Development dependencies
- `uv.toml` / `uv.lock` - UV package manager configuration

### To install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Or with UV:
```bash
uv sync
```

---

## Notes
- All development should happen on the feature branch specified above
- Never push to a different branch without explicit permission
- Commit messages should be clear and descriptive
- Use git push with retry logic if network issues occur
