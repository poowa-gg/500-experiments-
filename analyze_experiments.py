"""
Analysis tool for exploring generated experiments
"""

import json

def load_experiments():
    with open('climate_experiments.json', 'r') as f:
        return json.load(f)

def filter_experiments(experiments, **filters):
    """Filter experiments by criteria"""
    results = experiments
    
    for key, value in filters.items():
        if value:
            results = [e for e in results if e.get(key) == value]
    
    return results

def top_roi_experiments(experiments, n=10):
    """Get top N experiments by ROI"""
    sorted_exp = sorted(experiments, key=lambda x: x['expected_roi'], reverse=True)
    return sorted_exp[:n]

def high_priority_experiments(experiments):
    """Get all high priority experiments"""
    return [e for e in experiments if e['priority'] == 'high']

def experiments_by_budget(experiments, max_budget):
    """Get experiments within budget"""
    return [e for e in experiments if e['cost_estimate_ngn'] <= max_budget]

def print_experiment(exp):
    """Pretty print an experiment"""
    print(f"\n{'='*60}")
    print(f"ID: {exp['experiment_id']} | Priority: {exp['priority'].upper()}")
    print(f"{'='*60}")
    print(f"Segment: {exp['user_segment'].title()}")
    print(f"Region: {exp['region']}")
    print(f"Event: {exp['climate_event'].replace('_', ' ').title()}")
    print(f"Channel: {exp['alert_channel'].replace('_', ' ').title()}")
    print(f"\nHypothesis:")
    print(f"  {exp['hypothesis']}")
    print(f"\nMetrics: {', '.join(exp['success_metrics'])}")
    print(f"\nDetails:")
    print(f"  Sample Size: {exp['sample_size']:,} users")
    print(f"  Duration: {exp['duration_days']} days")
    print(f"  Cost: ₦{exp['cost_estimate_ngn']:,}")
    print(f"  Expected ROI: {exp['expected_roi']}x")
    print(f"  Accuracy: {exp['predicted_accuracy']*100}%")
    print(f"  Lead Time: {exp['lead_time_hours']} hours")
    print(f"  ML Model: {exp['ml_model']}")
    print(f"  Data Sources: {', '.join(exp['data_sources'])}")

def main():
    print("Loading experiments...")
    experiments = load_experiments()
    print(f"✓ Loaded {len(experiments)} experiments\n")
    
    # Analysis examples
    print("="*60)
    print("TOP 5 HIGHEST ROI EXPERIMENTS")
    print("="*60)
    top_roi = top_roi_experiments(experiments, 5)
    for exp in top_roi:
        print_experiment(exp)
    
    print("\n\n" + "="*60)
    print("FARMER-FOCUSED EXPERIMENTS (Sample)")
    print("="*60)
    farmer_exp = filter_experiments(experiments, user_segment='farmers')
    print(f"\nTotal farmer experiments: {len(farmer_exp)}")
    for exp in farmer_exp[:3]:
        print_experiment(exp)
    
    print("\n\n" + "="*60)
    print("LOW-COST, HIGH-PRIORITY EXPERIMENTS")
    print("="*60)
    budget_exp = experiments_by_budget(experiments, 200000)
    high_pri = [e for e in budget_exp if e['priority'] == 'high']
    print(f"\nFound {len(high_pri)} experiments under ₦200,000 with high priority")
    for exp in high_pri[:3]:
        print_experiment(exp)
    
    # Regional analysis
    print("\n\n" + "="*60)
    print("LAGOS REGION EXPERIMENTS")
    print("="*60)
    lagos_exp = filter_experiments(experiments, region='Lagos')
    print(f"\nTotal Lagos experiments: {len(lagos_exp)}")
    for exp in lagos_exp[:2]:
        print_experiment(exp)

if __name__ == "__main__":
    main()
