#!/usr/bin/env python3
"""
Analyze Mixmax customer data to identify ICP patterns
"""

import csv
import json
from collections import Counter, defaultdict
from statistics import median, mean

def parse_float(value):
    """Parse float from string, return 0 if empty or invalid"""
    if not value or value == "":
        return 0.0
    try:
        return float(value)
    except ValueError:
        return 0.0

def parse_int(value):
    """Parse int from string, return 0 if empty or invalid"""
    if not value or value == "":
        return 0
    try:
        return int(value)
    except ValueError:
        return 0

def analyze_customers(csv_path):
    """Analyze customer CSV and extract ICP patterns"""

    customers = []

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Calculate total ARR
            ds_arr = parse_float(row.get('DWH DS Customer ARR', '0'))
            ss_arr = parse_float(row.get('DWH SS Customer ARR', '0'))
            total_arr = ds_arr + ss_arr

            # Parse seat counts
            all_seats = parse_int(row.get('All Used Seats', '0'))
            enterprise_seats = parse_int(row.get('Enterprise Purchased Seats', '0'))
            smb_seats = parse_int(row.get('SMB Purchased Seats', '0'))

            customer = {
                'name': row.get('Account Name', ''),
                'domain': row.get('Company Domain Text', ''),
                'total_arr': total_arr,
                'ds_arr': ds_arr,
                'ss_arr': ss_arr,
                'all_seats': all_seats,
                'enterprise_seats': enterprise_seats,
                'smb_seats': smb_seats,
                'crm': row.get('CRM', ''),
                'email_provider': row.get('Email Provider', ''),
                'naics_code': row.get('NAICS Code', ''),
                'team': row.get('Team', ''),
                'notes': row.get('Prospecting Notes', '')
            }
            customers.append(customer)

    # Filter paying customers (ARR > 0)
    paying_customers = [c for c in customers if c['total_arr'] > 0]

    # Top customers by ARR
    top_customers = sorted(paying_customers, key=lambda x: x['total_arr'], reverse=True)[:30]

    # ARR distribution
    arrs = [c['total_arr'] for c in paying_customers]
    arr_stats = {
        'total_customers': len(paying_customers),
        'total_arr': sum(arrs),
        'avg_arr': mean(arrs) if arrs else 0,
        'median_arr': median(arrs) if arrs else 0,
        'min_arr': min(arrs) if arrs else 0,
        'max_arr': max(arrs) if arrs else 0
    }

    # ARR buckets
    arr_buckets = {
        '<$5K': len([a for a in arrs if 0 < a < 5000]),
        '$5K-$10K': len([a for a in arrs if 5000 <= a < 10000]),
        '$10K-$25K': len([a for a in arrs if 10000 <= a < 25000]),
        '$25K-$50K': len([a for a in arrs if 25000 <= a < 50000]),
        '$50K-$100K': len([a for a in arrs if 50000 <= a < 100000]),
        '$100K+': len([a for a in arrs if a >= 100000])
    }

    # Seat size distribution (company size proxy)
    seat_buckets = defaultdict(int)
    for c in paying_customers:
        seats = c['all_seats']
        if seats == 0:
            continue
        elif seats < 10:
            seat_buckets['1-9 seats'] += 1
        elif seats < 25:
            seat_buckets['10-24 seats'] += 1
        elif seats < 50:
            seat_buckets['25-49 seats'] += 1
        elif seats < 100:
            seat_buckets['50-99 seats'] += 1
        else:
            seat_buckets['100+ seats'] += 1

    # NAICS code analysis (industry)
    naics_counter = Counter([c['naics_code'] for c in paying_customers if c['naics_code']])

    # NAICS code mapping (simplified)
    naics_mapping = {
        '51': 'Information/Publishing/Media',
        '52': 'Finance & Insurance',
        '53': 'Real Estate',
        '54': 'Professional/Scientific/Technical Services',
        '56': 'Administrative/Support Services',
        '61': 'Educational Services',
        '62': 'Healthcare',
        '71': 'Arts/Entertainment/Recreation',
        '72': 'Accommodation & Food Services',
        '81': 'Other Services',
        '99': 'Other',
        '11': 'Agriculture',
        '22': 'Utilities',
        '31': 'Manufacturing - Food',
        '32': 'Manufacturing - Textiles',
        '33': 'Manufacturing - Other',
        '42': 'Wholesale Trade',
        '44': 'Retail Trade',
        '45': 'Retail - Clothing',
        '48': 'Transportation'
    }

    industry_distribution = {}
    for code, count in naics_counter.most_common():
        industry = naics_mapping.get(code, f'NAICS {code}')
        industry_distribution[industry] = count

    # CRM usage
    crm_counter = Counter([c['crm'] for c in paying_customers if c['crm']])

    # Email provider
    email_counter = Counter([c['email_provider'] for c in paying_customers if c['email_provider']])

    # Identify high-value segment (top 20% by ARR)
    arr_threshold = sorted(arrs, reverse=True)[int(len(arrs) * 0.2)] if arrs else 0
    high_value_customers = [c for c in paying_customers if c['total_arr'] >= arr_threshold]

    # Analyze high-value segment
    hv_naics = Counter([c['naics_code'] for c in high_value_customers if c['naics_code']])
    hv_crm = Counter([c['crm'] for c in high_value_customers if c['crm']])
    hv_seats = [c['all_seats'] for c in high_value_customers if c['all_seats'] > 0]

    hv_industry_dist = {}
    for code, count in hv_naics.most_common():
        industry = naics_mapping.get(code, f'NAICS {code}')
        hv_industry_dist[industry] = count

    # Compile analysis
    analysis = {
        'arr_statistics': arr_stats,
        'arr_distribution': arr_buckets,
        'seat_distribution': dict(seat_buckets),
        'industry_distribution': industry_distribution,
        'crm_distribution': dict(crm_counter),
        'email_provider_distribution': dict(email_counter),
        'top_30_customers': [
            {
                'name': c['name'],
                'domain': c['domain'],
                'arr': c['total_arr'],
                'seats': c['all_seats'],
                'crm': c['crm'],
                'naics': c['naics_code']
            }
            for c in top_customers
        ],
        'high_value_segment': {
            'threshold_arr': arr_threshold,
            'count': len(high_value_customers),
            'avg_seats': mean(hv_seats) if hv_seats else 0,
            'industry_concentration': hv_industry_dist,
            'crm_usage': dict(hv_crm),
            'avg_arr': mean([c['total_arr'] for c in high_value_customers])
        }
    }

    return analysis

if __name__ == '__main__':
    import sys

    csv_path = sys.argv[1] if len(sys.argv) > 1 else 'data/customers_raw.csv'

    analysis = analyze_customers(csv_path)

    # Pretty print JSON
    print(json.dumps(analysis, indent=2))
