"""
Test Trial for Mixmax GTM Agent System

This script demonstrates the agent system capabilities with simulated scenarios.
Run different test scenarios to see how agents coordinate.
"""

import asyncio
import sys
from orchestrator import send_query


async def test_scenario_1_icp_analysis():
    """Test Scenario 1: ICP Intelligence Analysis"""
    print("\n" + "=" * 80)
    print("📊 TEST SCENARIO 1: ICP Intelligence Analysis")
    print("=" * 80)
    print()

    query = """
    Activate the appropriate specialist agent to analyze our ICP intelligence data.

    I need you to:
    1. Read the ICP intelligence data from data/icp_intelligence.json
    2. Summarize the top 3 ICP sweet spots
    3. Identify the primary buyer pain points
    4. Recommend which industries and company sizes to prioritize for list building

    This is for planning our Phase 1 list building strategy.
    """

    print(f"🎯 Query:\n{query}\n")
    print("-" * 80)

    result, messages = await send_query(query, permission_mode="default")

    print("\n" + "=" * 80)
    print("✅ Scenario 1 Complete!")
    print("=" * 80)

    return result


async def test_scenario_2_offer_strategy():
    """Test Scenario 2: Offer Strategy Development"""
    print("\n" + "=" * 80)
    print("✉️  TEST SCENARIO 2: Offer Strategy Development")
    print("=" * 80)
    print()

    query = """
    I need to develop our initial offer strategy for testing.

    Based on our case study intelligence and messaging data:
    1. What are the top 3 value proposition themes that resonate most?
    2. What are the strongest pain points we solve?
    3. Suggest 3-5 offer ideas we could test (e.g., audits, free tools, pilots)

    Read from data/messaging_intelligence.json and data/case_studies.json
    """

    print(f"🎯 Query:\n{query}\n")
    print("-" * 80)

    result, messages = await send_query(query, permission_mode="default", continue_conversation=True)

    print("\n" + "=" * 80)
    print("✅ Scenario 2 Complete!")
    print("=" * 80)

    return result


async def test_scenario_3_planning_mode():
    """Test Scenario 3: Phase 1 Execution Planning"""
    print("\n" + "=" * 80)
    print("📋 TEST SCENARIO 3: Phase 1 Execution Planning")
    print("=" * 80)
    print()

    query = """
    Help me plan the execution of Phase 1 (Week 0-1: Preparation).

    I need a detailed action plan that includes:
    1. List Builder tasks: What data sources to use, how to score intent
    2. Data Quality tasks: Verification strategy, AI cleanup criteria
    3. Offer Strategist tasks: Offer development, message framework creation
    4. Timeline and dependencies
    5. Success criteria for each task

    Use plan mode to think through this systematically.
    """

    print(f"🎯 Query:\n{query}\n")
    print("-" * 80)

    result, messages = await send_query(query, permission_mode="plan", continue_conversation=False)

    print("\n" + "=" * 80)
    print("✅ Scenario 3 Complete!")
    print("=" * 80)

    return result


async def test_scenario_4_agent_coordination():
    """Test Scenario 4: Multi-Agent Coordination Simulation"""
    print("\n" + "=" * 80)
    print("🤝 TEST SCENARIO 4: Multi-Agent Coordination Simulation")
    print("=" * 80)
    print()

    query = """
    Simulate a handoff scenario between agents.

    Scenario: The List Builder has finished sourcing 100K contacts.

    1. What deliverables should the List Builder provide to Data Quality Engineer?
    2. What's the expected handoff format?
    3. What validation checks should happen at this handoff point?
    4. What are the acceptance criteria for Data Quality Engineer to proceed?

    Reference the AGENT_INTERACTION_FLOW.md for handoff protocols.
    """

    print(f"🎯 Query:\n{query}\n")
    print("-" * 80)

    result, messages = await send_query(query, permission_mode="default", continue_conversation=False)

    print("\n" + "=" * 80)
    print("✅ Scenario 4 Complete!")
    print("=" * 80)

    return result


async def run_all_scenarios():
    """Run all test scenarios sequentially"""
    print("\n" + "🚀" * 40)
    print("MIXMAX GTM AGENT SYSTEM - TEST TRIAL")
    print("🚀" * 40)

    scenarios = [
        ("ICP Analysis", test_scenario_1_icp_analysis),
        ("Offer Strategy", test_scenario_2_offer_strategy),
        ("Phase 1 Planning", test_scenario_3_planning_mode),
        ("Agent Coordination", test_scenario_4_agent_coordination),
    ]

    results = {}

    for name, scenario_func in scenarios:
        try:
            result = await scenario_func()
            results[name] = "✅ PASSED"
        except Exception as e:
            results[name] = f"❌ FAILED: {str(e)}"
            print(f"\n❌ Error in {name}: {e}")

    # Summary
    print("\n" + "=" * 80)
    print("📊 TEST TRIAL SUMMARY")
    print("=" * 80)
    for name, status in results.items():
        print(f"{status} - {name}")

    print("\n" + "=" * 80)
    print("🎉 Test Trial Complete!")
    print("=" * 80)


async def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        scenario = sys.argv[1]

        scenarios = {
            "1": test_scenario_1_icp_analysis,
            "icp": test_scenario_1_icp_analysis,
            "2": test_scenario_2_offer_strategy,
            "offer": test_scenario_2_offer_strategy,
            "3": test_scenario_3_planning_mode,
            "plan": test_scenario_3_planning_mode,
            "4": test_scenario_4_agent_coordination,
            "coordination": test_scenario_4_agent_coordination,
            "all": run_all_scenarios,
        }

        if scenario in scenarios:
            await scenarios[scenario]()
        else:
            print(f"Unknown scenario: {scenario}")
            print("\nAvailable scenarios:")
            print("  1, icp         - ICP Intelligence Analysis")
            print("  2, offer       - Offer Strategy Development")
            print("  3, plan        - Phase 1 Execution Planning")
            print("  4, coordination - Agent Coordination Simulation")
            print("  all            - Run all scenarios")
    else:
        # Run all by default
        await run_all_scenarios()


if __name__ == "__main__":
    asyncio.run(main())
