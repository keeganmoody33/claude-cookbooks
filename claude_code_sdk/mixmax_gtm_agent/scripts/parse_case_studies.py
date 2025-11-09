#!/usr/bin/env python3
"""
Parse flattened Mixmax case study data into structured JSON format
"""

import json
import re
from typing import List, Dict, Any

def parse_tacit_knowledge_fields(tacit_text: str) -> Dict[str, Any]:
    """Parse the semicolon-separated tacit knowledge fields"""
    fields = {}

    # Parse unsaidInsights
    unsaid_pattern = r'unsaidInsights: (\d+) - ([^;]+)'
    unsaid_matches = re.findall(unsaid_pattern, tacit_text)
    if unsaid_matches:
        fields['unsaid_insights_raw'] = [match[1].strip() for match in unsaid_matches]

    # Parse structuralPattern
    structural_pattern = r'structuralPattern: ([^;]+)'
    structural_match = re.search(structural_pattern, tacit_text)
    if structural_match:
        fields['structural_pattern_raw'] = structural_match.group(1).strip()

    # Parse fundamentalMechanism
    mechanism_pattern = r'fundamentalMechanism: ([^;]+)'
    mechanism_match = re.search(mechanism_pattern, tacit_text)
    if mechanism_match:
        fields['fundamental_mechanism_raw'] = mechanism_match.group(1).strip()

    # Parse successPrerequisites
    prereq_pattern = r'successPrerequisites: (\d+) - ([^;]+)'
    prereq_matches = re.findall(prereq_pattern, tacit_text)
    if prereq_matches:
        fields['success_prerequisites_raw'] = [match[1].strip() for match in prereq_matches]

    # Parse crossVerticalApplications (these are [object Object], we'll get them from JSON)

    return fields

def parse_case_study_entry(entry_text: str) -> Dict[str, Any]:
    """Parse a single case study entry (tacit + JSON)"""

    # Split on tab to separate tacit knowledge from JSON
    parts = entry_text.split('\t')

    if len(parts) < 2:
        return None

    tacit_text = parts[1] if len(parts) > 1 else ''
    json_text = parts[2] if len(parts) > 2 else ''

    # Parse tacit knowledge fields
    tacit_fields = parse_tacit_knowledge_fields(tacit_text)

    # Parse JSON
    try:
        case_data = json.loads(json_text)
        # Merge tacit fields with JSON data
        case_data['_tacit_fields'] = tacit_fields
        return case_data
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        print(f"JSON text: {json_text[:200]}...")
        return None

def parse_all_case_studies(raw_text: str) -> List[Dict[str, Any]]:
    """Parse all case studies from the raw data"""

    case_studies = []

    # Split by the "Case Study (Flattened)" header pattern
    # Each entry starts with: Case Study (Flattened)\t[tacit]\t{json}
    entries = raw_text.split('Case Study (Flattened)\t')

    for entry in entries[1:]:  # Skip first empty split
        if not entry.strip():
            continue

        # Each entry is: Tacit Knowledge Extraction\n[tacit fields]\t{json}
        # Remove the "Tacit Knowledge Extraction" prefix
        entry = entry.replace('Tacit Knowledge Extraction\n', '')
        entry = 'x\t' + entry  # Add dummy first column

        case_study = parse_case_study_entry(entry)
        if case_study:
            case_studies.append(case_study)

    return case_studies

def main():
    """Main entry point"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python parse_case_studies.py <input_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'data/case_studies.json'

    with open(input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    case_studies = parse_all_case_studies(raw_text)

    print(f"Parsed {len(case_studies)} case studies")

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(case_studies, f, indent=2)

    print(f"Wrote case studies to {output_file}")

    # Print summary
    companies = [cs.get('case_summary', {}).get('company', 'Unknown') for cs in case_studies]
    print("\nCompanies included:")
    for i, company in enumerate(companies, 1):
        print(f"{i}. {company}")

if __name__ == '__main__':
    main()
