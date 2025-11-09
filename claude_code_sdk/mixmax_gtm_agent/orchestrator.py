"""
Mixmax GTM Orchestrator Agent

Coordinates 6 specialized agents to execute the Gutenberg Framework:
- List Builder Specialist
- Data Quality Engineer
- Offer Strategist
- Campaign Orchestrator
- Deliverability Engineer
- Analytics Optimizer
"""

import asyncio
import json
import os
from collections.abc import Callable
from typing import Any, Literal

from dotenv import load_dotenv

from claude_code_sdk import ClaudeCodeOptions, ClaudeSDKClient

load_dotenv()


def get_activity_text(msg) -> str | None:
    """Extract activity text from a message"""
    try:
        if "Assistant" in msg.__class__.__name__:
            if hasattr(msg, "content") and msg.content:
                first_content = msg.content[0] if isinstance(msg.content, list) else msg.content
                if hasattr(first_content, "name"):
                    return f"🤖 Using: {first_content.name}()"
            return "🤖 Thinking..."
        elif "User" in msg.__class__.__name__:
            return "✓ Tool completed"
    except (AttributeError, IndexError):
        pass
    return None


def print_activity(msg) -> None:
    """Print activity to console"""
    activity = get_activity_text(msg)
    if activity:
        print(activity)


async def send_query(
    prompt: str,
    continue_conversation: bool = False,
    permission_mode: Literal["default", "plan", "acceptEdits"] = "default",
    activity_handler: Callable[[Any], None | Any] = print_activity,
) -> tuple[str | None, list]:
    """
    Send a query to the GTM Orchestrator agent.

    Args:
        prompt: The query to send
        continue_conversation: Continue the previous conversation if True
        permission_mode: "default" (execute), "plan" (think only), or "acceptEdits"
        activity_handler: Callback for activity updates (default: print_activity)

    Returns:
        Tuple of (result, messages) - result is the final text, messages is the full conversation

    Features:
        - Memory: CLAUDE.md context loaded from mixmax_gtm_agent/CLAUDE.md
        - Subagents: 6 specialists via Task tool (defined in .claude/agents)
        - Intelligence: Case studies, ICP data, messaging data in data/
        - Scripts: Python automation scripts in scripts/ via Bash
    """

    system_prompt = """You are the GTM Orchestrator for Mixmax.ai's outbound sales execution.

You coordinate 8 specialized agents to execute the Gutenberg Framework - a rapid-testing,
data-driven approach to outbound that achieves 8,200% ROI.

Your specialists (activate via Task tool):
- list-builder: Build 100K+ contact databases with intent scoring
- data-quality-engineer: Verify emails, AI cleanup, enrich data
- offer-strategist: Create offers & messaging (15-20 combinations)
- campaign-orchestrator: Run A/B tests, identify winners (<2 weeks)
- deliverability-engineer: Manage domains, warmup, maintain >90% inbox placement
- analytics-optimizer: Scale winners, optimize, refine ICP
- market-intelligence: Monitor job market for buying signals (VP Sales, CRO, Rev Ops hires)
- competitive-intelligence: Extract contacts from competitor engagement (Outreach, SalesLoft, Groove)

Market Intelligence Focus:
We monitor the JOB MARKET for decision-maker hiring signals (NOT competitor employee changes).
Target roles: CRO, VP/Director Sales, VP/Director Rev Ops, VP/Director SDR, SDR Manager.
When companies post these roles, they're likely in a buying cycle for sales tools.

Competitive Intelligence Focus:
We extract CONTACTS who engage with competitors (NOT monitor what competitors do).
Primary targets: Outreach, SalesLoft, Groove (these are our main threats - we're taking them out).
Awareness only: HubSpot, Lemlist (track but don't prioritize).
Sources: LinkedIn/Twitter engagements (last 90 days), G2/Capterra/TrustRadius reviews.

Sales Focus:
Mixmax is a SALES execution platform. Focus on sales roles (SDR, AE, CRO, Rev Ops).
NOT general GTM, NOT marketing automation.

You have automation scripts in scripts/:
- python scripts/analyze_customer_icp.py: Analyze customer data for ICP patterns
- python scripts/process_case_studies.py: Generate ICP + messaging intelligence

Intelligence data in data/:
- case_studies.json: 43 analyzed customer case studies
- icp_intelligence.json: ICP sweet spots, buyer triggers, target decision-maker roles
- messaging_intelligence.json: Value props and pain points by segment

Framework phases:
1. Week 0-1: List building (100K→40K verified) + offer creation (15 combos)
2. Week 2-3: Testing (15K contacts, identify 2-3 winners >2% reply)
3. Week 4-5: Scaling (30K to winners, 300-500 replies expected)
4. Week 6-8: Optimization (70/30 rule, ICP refinement, continuous improvement)

Your role: Coordinate handoffs, monitor progress, activate specialists at the right time.
Let specialists make domain decisions. Intervene only for cross-domain coordination.
"""

    # Build options
    options_dict = {
        "model": "claude-sonnet-4-20250514",
        "allowed_tools": [
            "Task",  # enables subagent delegation
            "Read",
            "Write",
            "Edit",
            "Bash",
            "Glob",
            "Grep",
            "WebSearch",
        ],
        "continue_conversation": continue_conversation,
        "system_prompt": system_prompt,
        "permission_mode": permission_mode,
        "cwd": os.path.dirname(os.path.abspath(__file__)),
    }

    options = ClaudeCodeOptions(**options_dict)

    # Send query
    result = None
    messages = []

    async with ClaudeSDKClient() as client:
        async for msg in client.create_message_stream(prompt, options):
            if activity_handler:
                activity_handler(msg)

            messages.append(msg)

            # Capture final text result
            if "Assistant" in msg.__class__.__name__:
                if hasattr(msg, "content"):
                    for content in msg.content if isinstance(msg.content, list) else [msg.content]:
                        if hasattr(content, "text"):
                            result = content.text

    return result, messages


async def main():
    """
    Example usage of the GTM Orchestrator
    """
    print("🚀 Mixmax GTM Orchestrator Agent")
    print("=" * 60)
    print()

    # Example query
    query = """
    Help me understand the current state of our GTM system.

    Check what intelligence data we have available and give me:
    1. A summary of our ICP intelligence
    2. Key messaging themes from case studies
    3. Recommended next steps to execute Phase 1
    """

    print(f"Query: {query}\n")
    print("-" * 60)
    print()

    result, _ = await send_query(query)

    print()
    print("=" * 60)
    print("✅ Complete!")
    print()
    if result:
        print("Final Result:")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
