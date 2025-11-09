#!/usr/bin/env python3
"""
Process Mixmax case study data directly from the provided format.
Extract company insights, patterns, and ICP intelligence.
"""

import json
import re
from typing import List, Dict, Any
from collections import Counter, defaultdict

# Sample case studies data - in production this would be loaded from file
# For now, we'll manually structure the key companies

CASE_STUDIES_DATA = [
    {
        "company": "Veraset",
        "industry": "Data Infrastructure and Analytics",
        "company_size": "11-50",
        "real_problem": "Coordinating compliant, high-volume outbound across a lean team selling complex data products",
        "success_patterns": [
            "High compliance requirements (data privacy)",
            "Multi-segment audiences (Fortune 500, academia, startups)",
            "Template-driven standardization needed",
            "Small team requiring efficiency gains"
        ],
        "universal_mechanism": "Standardize and track high-volume, multi-segment outreach with compliance guardrails",
        "key_features_valued": ["CRM integration", "Templates", "Tracking", "Compliance workflows"],
        "company_size_bucket": "11-50"
    },
    {
        "company": "Hostfully",
        "industry": "Software Development",
        "company_size": "51-200",
        "real_problem": "Lead follow-up latency causing pipeline leakage across lean revenue team",
        "success_patterns": [
            "Growth-stage SaaS in competitive market",
            "Need to scale without adding headcount",
            "Automated sequences and visibility critical",
            "Fast time-to-first-response needed"
        ],
        "universal_mechanism": "Reduce coordination latency in asynchronous outreach with standardized templates",
        "key_features_valued": ["Sequences", "Templates", "Gmail integration", "CRM tracking"],
        "company_size_bucket": "51-200"
    },
    {
        "company": "Bennie",
        "industry": "Software Development",
        "company_size": "201-500",
        "real_problem": "Inconsistent outreach and lack of visibility across growing team",
        "success_patterns": [
            "Fast implementation requirement (<1 week)",
            "Above-industry reply rates needed",
            "Team-wide visibility required",
            "Gmail/GSuite-native workflow"
        ],
        "universal_mechanism": "Standardize high-volume outreach with shared visibility and rapid onboarding",
        "key_features_valued": ["Sequences", "Templates", "Salesforce integration", "Team sharing"],
        "company_size_bucket": "201-500"
    },
    {
        "company": "Atrium",
        "industry": "Software Development",
        "company_size": "51-200",
        "real_problem": "Manual coordination costs and lack of coaching accountability",
        "success_patterns": [
            "Sales management and coaching focus",
            "Automation to reduce manual tasks",
            "AI-powered coaching desired",
            "Standardized playbooks needed"
        ],
        "universal_mechanism": "Automate coordination while maintaining coaching and accountability visibility",
        "key_features_valued": ["Automation", "Analytics", "Templates", "Coaching insights"],
        "company_size_bucket": "51-200"
    },
    {
        "company": "Brex",
        "industry": "Financial Services",
        "company_size": "1001-5000",
        "real_problem": "Large-scale coordination without delays or blind spots",
        "success_patterns": [
            "High-growth fintech",
            "Multi-rep coordination",
            "Speed and consistency critical",
            "Enterprise-grade tracking needed"
        ],
        "universal_mechanism": "Coordinate large teams with standardized messaging and real-time visibility",
        "key_features_valued": ["Sequences", "CRM integration", "Team analytics", "Automation"],
        "company_size_bucket": "1001-5000"
    },
    {
        "company": "Canva",
        "industry": "Software Development",
        "company_size": "1001-5000",
        "real_problem": "Global outreach coordination without sacrificing responsiveness",
        "success_patterns": [
            "Global, distributed team",
            "High-volume outreach",
            "Brand consistency critical",
            "Fast response times needed"
        ],
        "universal_mechanism": "Scale personalized outreach across global teams with brand consistency",
        "key_features_valued": ["Templates", "CRM integration", "Global collaboration", "Tracking"],
        "company_size_bucket": "1001-5000"
    },
    {
        "company": "Help Scout",
        "industry": "Technology",
        "company_size": "51-200",
        "real_problem": "Manual follow-up and coordination causing latency",
        "success_patterns": [
            "Customer-centric SaaS",
            "Ease-of-use critical",
            "Fast time-to-value needed",
            "Integration with existing stack"
        ],
        "universal_mechanism": "Reduce coordination latency with lightweight, integrated tooling",
        "key_features_valued": ["Easy adoption", "Gmail integration", "Templates", "Tracking"],
        "company_size_bucket": "51-200"
    },
    {
        "company": "Gong",
        "industry": "Software Development",
        "company_size": "1001-5000",
        "real_problem": "Multi-rep coordination without inconsistent follow-ups",
        "success_patterns": [
            "Revenue intelligence platform",
            "High-volume outreach",
            "Process standardization needed",
            "Data-driven optimization"
        ],
        "universal_mechanism": "Standardize outreach with trackable workflows for data-driven iteration",
        "key_features_valued": ["Sequences", "Analytics", "CRM integration", "Templates"],
        "company_size_bucket": "1001-5000"
    }
]

def analyze_icp_patterns() -> Dict[str, Any]:
    """Analyze ICP patterns from case study data"""

    # Company size distribution
    size_distribution = Counter([cs['company_size_bucket'] for cs in CASE_STUDIES_DATA])

    # Industry distribution
    industry_distribution = Counter([cs['industry'] for cs in CASE_STUDIES_DATA])

    # Common problems
    all_problems = [cs['real_problem'] for cs in CASE_STUDIES_DATA]

    # Success patterns
    all_success_patterns = []
    for cs in CASE_STUDIES_DATA:
        all_success_patterns.extend(cs['success_patterns'])

    success_pattern_themes = Counter(all_success_patterns)

    # Feature value counts
    all_features = []
    for cs in CASE_STUDIES_DATA:
        all_features.extend(cs['key_features_valued'])

    feature_frequency = Counter(all_features)

    # Universal mechanisms
    mechanisms = [cs['universal_mechanism'] for cs in CASE_STUDIES_DATA]

    # ICP Sweet Spots (patterns appearing in multiple companies)
    sweet_spots = []

    # Pattern 1: Growth-stage SaaS 51-200 employees
    growth_saas = [cs for cs in CASE_STUDIES_DATA
                   if 'Software Development' in cs['industry']
                   and cs['company_size_bucket'] in ['51-200', '201-500']]

    if len(growth_saas) >= 2:
        sweet_spots.append({
            'segment': 'Growth-stage SaaS (51-500 employees)',
            'count': len(growth_saas),
            'common_problems': [
                'Lead follow-up latency',
                'Team coordination challenges',
                'Need to scale without adding headcount'
            ],
            'value_props': [
                'Fast implementation',
                'Above-industry reply rates',
                'Team-wide visibility',
                'Reduced manual work'
            ]
        })

    # Pattern 2: Enterprise (1000+ employees)
    enterprise = [cs for cs in CASE_STUDIES_DATA
                  if cs['company_size_bucket'] in ['1001-5000', '5000+']]

    if len(enterprise) >= 2:
        sweet_spots.append({
            'segment': 'Enterprise (1000+ employees)',
            'count': len(enterprise),
            'common_problems': [
                'Multi-team coordination complexity',
                'Maintaining speed at scale',
                'Brand consistency across teams'
            ],
            'value_props': [
                'Enterprise-grade tracking',
                'Global team collaboration',
                'Standardized messaging',
                'Real-time visibility'
            ]
        })

    analysis = {
        'total_case_studies': len(CASE_STUDIES_DATA),
        'company_size_distribution': dict(size_distribution),
        'industry_distribution': dict(industry_distribution),
        'top_success_patterns': dict(success_pattern_themes.most_common(10)),
        'most_valued_features': dict(feature_frequency.most_common()),
        'icp_sweet_spots': sweet_spots,
        'universal_mechanisms': mechanisms,
        'key_insights': {
            'primary_buyer_pain': 'Coordination latency and visibility gaps in high-volume outreach',
            'common_buying_triggers': [
                'Team scaling without proportional headcount',
                'Manual processes causing delays',
                'Lack of visibility into outreach performance',
                'Inconsistent messaging across team'
            ],
            'decision_making_style': 'Pragmatic, speed-oriented, favor ease-of-use and fast time-to-value',
            'critical_success_factors': [
                'Gmail/CRM integration',
                'Fast implementation (<1 week typical)',
                'Template-based standardization',
                'Team-wide visibility and tracking'
            ]
        }
    }

    return analysis

def extract_messaging_intelligence() -> Dict[str, Any]:
    """Extract messaging and positioning intelligence from case studies"""

    messaging = {
        'value_prop_themes': {
            'efficiency': [
                'Reduce manual work',
                'Automate repetitive tasks',
                'Feel like extra headcount',
                'Do more with same team'
            ],
            'speed': [
                'Fast time-to-first-response',
                'Quick implementation',
                'Rapid testing and iteration',
                'Eliminate delays'
            ],
            'visibility': [
                'Team-wide transparency',
                'Track every touchpoint',
                'Data-driven optimization',
                'Never miss a follow-up'
            ],
            'quality': [
                'Consistent messaging',
                'Brand-compliant communication',
                'Professional templates',
                'Higher reply rates'
            ]
        },
        'pain_points_by_segment': {
            'growth_stage_saas': [
                'Lead leakage from slow follow-up',
                'Inconsistent messaging hurting conversion',
                'Cannot scale without hiring',
                'No visibility into what works'
            ],
            'enterprise': [
                'Coordination chaos across teams',
                'Brand inconsistency',
                'Delayed responses',
                'Tracking gaps'
            ],
            'fintech_regulated': [
                'Compliance requirements',
                'Audit trails needed',
                'Sensitive data handling',
                'Approved messaging control'
            ]
        },
        'proof_points': {
            'implementation_speed': 'Most customers live in <1 week',
            'reply_rate_lift': 'Above-industry reply rates consistently',
            'efficiency_gain': 'Feels like adding headcount without hiring',
            'adoption': 'Native Gmail/CRM experience = high adoption'
        }
    }

    return messaging

def main():
    """Generate ICP and messaging intelligence report"""

    print("=" * 80)
    print("MIXMAX CUSTOMER ICP & MESSAGING INTELLIGENCE")
    print("=" * 80)
    print()

    # Analyze ICP patterns
    icp_analysis = analyze_icp_patterns()

    print("## ICP ANALYSIS")
    print()
    print(f"Total Case Studies Analyzed: {icp_analysis['total_case_studies']}")
    print()

    print("### Company Size Distribution:")
    for size, count in sorted(icp_analysis['company_size_distribution'].items()):
        print(f"  {size}: {count} companies")
    print()

    print("### Industry Distribution:")
    for industry, count in icp_analysis['industry_distribution'].items():
        print(f"  {industry}: {count} companies")
    print()

    print("### ICP Sweet Spots:")
    for sweet_spot in icp_analysis['icp_sweet_spots']:
        print(f"\n  Segment: {sweet_spot['segment']}")
        print(f"  Count: {sweet_spot['count']} customers")
        print(f"  Common Problems:")
        for problem in sweet_spot['common_problems']:
            print(f"    - {problem}")
        print(f"  Value Props:")
        for vp in sweet_spot['value_props']:
            print(f"    - {vp}")
    print()

    print("### Most Valued Features:")
    for feature, count in icp_analysis['most_valued_features'].items():
        print(f"  {feature}: {count} mentions")
    print()

    print("### Key Buying Insights:")
    for insight_type, value in icp_analysis['key_insights'].items():
        if isinstance(value, list):
            print(f"\n  {insight_type.replace('_', ' ').title()}:")
            for item in value:
                print(f"    - {item}")
        else:
            print(f"\n  {insight_type.replace('_', ' ').title()}: {value}")
    print()

    print("\n" + "=" * 80)
    print("## MESSAGING INTELLIGENCE")
    print("=" * 80)
    print()

    messaging = extract_messaging_intelligence()

    print("### Value Prop Themes:")
    for theme, messages in messaging['value_prop_themes'].items():
        print(f"\n  {theme.upper()}:")
        for msg in messages:
            print(f"    - {msg}")
    print()

    print("### Pain Points by Segment:")
    for segment, pains in messaging['pain_points_by_segment'].items():
        print(f"\n  {segment.replace('_', ' ').upper()}:")
        for pain in pains:
            print(f"    - {pain}")
    print()

    print("### Proof Points:")
    for key, value in messaging['proof_points'].items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    print()

    # Save to JSON files
    with open('data/icp_intelligence.json', 'w') as f:
        json.dump(icp_analysis, f, indent=2)

    with open('data/messaging_intelligence.json', 'w') as f:
        json.dump(messaging, f, indent=2)

    print("\n" + "=" * 80)
    print("Data saved to:")
    print("  - data/icp_intelligence.json")
    print("  - data/messaging_intelligence.json")
    print("=" * 80)

if __name__ == '__main__':
    main()
