

"""
Hyperlocal Climate Intelligence - Experiment Scenario Generator
Generates 500 diverse experimental scenarios for testing the platform
"""

import random
import json
from datetime import datetime, timedelta
from itertools import product




class ClimateExperimentGenerator:
    def __init__(self):
        # Define experiment dimensions
        self.user_segments = ['farmers', 'insurers', 'government', 'logistics', 'ngos']
        
        self.regions = ['Lagos', 'Kano', 'Rivers', 'Kaduna', 'Oyo', 'Katsina', 
                       'Benue', 'Niger', 'Ogun', 'Sokoto', 'Plateau', 'Enugu']
        
        self.climate_events = [
            'heavy_rainfall', 'drought', 'flood', 'heatwave', 
            'windstorm', 'early_rain', 'late_rain', 'dry_spell'
        ]
        
        self.alert_channels = ['sms', 'mobile_app', 'web_dashboard', 'ussd', 'whatsapp']
        
        self.forecast_horizons = ['1_hour', '6_hours', '24_hours', '3_days', '7_days', '14_days']
        
        self.actions = {
            'farmers': ['plant', 'irrigate', 'harvest', 'apply_fertilizer', 'pest_control', 'delay_planting'],
            'insurers': ['trigger_payout', 'adjust_premium', 'assess_risk', 'send_alert'],
            'government': ['evacuate', 'deploy_resources', 'issue_warning', 'open_shelter'],
            'logistics': ['reroute', 'delay_shipment', 'expedite_delivery', 'warehouse_prep'],
            'ngos': ['distribute_aid', 'mobilize_volunteers', 'setup_camp', 'health_intervention']
        }
        
        self.accuracy_levels = [0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
        
        self.lead_times = [1, 3, 6, 12, 24, 48, 72]  # hours
        
    def generate_experiments(self, num_experiments=500):
        """Generate diverse experimental scenarios"""
        experiments = []
        
        for i in range(num_experiments):
            experiment = self._create_experiment(i + 1)
            experiments.append(experiment)
        
        return experiments
    
    def _create_experiment(self, exp_id):
        """Create a single experiment scenario"""
        user_segment = random.choice(self.user_segments)
        region = random.choice(self.regions)
        event = random.choice(self.climate_events)
        channel = random.choice(self.alert_channels)
        horizon = random.choice(self.forecast_horizons)
        accuracy = random.choice(self.accuracy_levels)
        lead_time = random.choice(self.lead_times)
        action = random.choice(self.actions[user_segment])
        
        # Generate realistic parameters
        experiment = {
            'experiment_id': f'EXP_{exp_id:04d}',
            'user_segment': user_segment,
            'region': region,
            'climate_event': event,
            'alert_channel': channel,
            'forecast_horizon': horizon,
            'predicted_accuracy': accuracy,
            'lead_time_hours': lead_time,
            'recommended_action': action,
            'hypothesis': self._generate_hypothesis(user_segment, event, channel, accuracy),
            'success_metrics': self._generate_metrics(user_segment),
            'sample_size': random.randint(50, 5000),
            'duration_days': random.randint(7, 90),
            'cost_estimate_ngn': random.randint(50000, 2000000),
            'expected_roi': round(random.uniform(1.5, 5.0), 2),
            'priority': random.choice(['high', 'medium', 'low']),
            'data_sources': self._select_data_sources(),
            'ml_model': random.choice(['random_forest', 'lstm', 'gradient_boosting', 'ensemble']),
            'validation_method': random.choice(['cross_validation', 'holdout', 'time_series_split'])
        }
        
        return experiment
    
    def _generate_hypothesis(self, segment, event, channel, accuracy):
        """Generate experiment hypothesis"""
        templates = [
            f"Delivering {event} alerts via {channel} to {segment} with {accuracy*100}% accuracy will increase preparedness by 30%",
            f"{segment} receiving {event} warnings through {channel} will reduce losses by 40%",
            f"Early {event} detection for {segment} via {channel} improves decision-making response time by 50%",
            f"{channel}-based alerts for {event} will increase {segment} platform adoption by 25%"
        ]
        return random.choice(templates)
    
    def _generate_metrics(self, segment):
        """Define success metrics per segment"""
        metrics_map = {
            'farmers': ['crop_yield_improvement', 'loss_reduction', 'adoption_rate', 'action_compliance'],
            'insurers': ['claim_accuracy', 'payout_speed', 'fraud_reduction', 'customer_satisfaction'],
            'government': ['response_time', 'lives_saved', 'resource_efficiency', 'public_trust'],
            'logistics': ['delivery_success_rate', 'cost_savings', 'route_optimization', 'damage_reduction'],
            'ngos': ['beneficiary_reach', 'aid_efficiency', 'response_time', 'coordination_improvement']
        }
        return random.sample(metrics_map[segment], k=random.randint(2, 4))
    
    def _select_data_sources(self):
        """Select data sources for experiment"""
        sources = ['nimet', 'satellite_imagery', 'iot_sensors', 'crowdsourced', 
                  'global_models', 'radar', 'weather_stations']
        return random.sample(sources, k=random.randint(2, 4))
    
    def save_experiments(self, experiments, filename='experiments.json'):
        """Save experiments to JSON file"""
        with open(filename, 'w') as f:
            json.dump(experiments, f, indent=2)
        print(f"✓ Saved {len(experiments)} experiments to {filename}")
    
    def generate_summary_report(self, experiments):
        """Generate summary statistics"""
        summary = {
            'total_experiments': len(experiments),
            'by_segment': {},
            'by_region': {},
            'by_event': {},
            'by_channel': {},
            'avg_sample_size': sum(e['sample_size'] for e in experiments) / len(experiments),
            'total_estimated_cost': sum(e['cost_estimate_ngn'] for e in experiments),
            'avg_expected_roi': sum(e['expected_roi'] for e in experiments) / len(experiments),
            'high_priority_count': sum(1 for e in experiments if e['priority'] == 'high')
        }
        
        # Count by categories
        for exp in experiments:
            summary['by_segment'][exp['user_segment']] = summary['by_segment'].get(exp['user_segment'], 0) + 1
            summary['by_region'][exp['region']] = summary['by_region'].get(exp['region'], 0) + 1
            summary['by_event'][exp['climate_event']] = summary['by_event'].get(exp['climate_event'], 0) + 1
            summary['by_channel'][exp['alert_channel']] = summary['by_channel'].get(exp['alert_channel'], 0) + 1
        
        return summary


def main():
    print("=" * 60)
    print("Hyperlocal Climate Intelligence Platform")
    print("Experiment Scenario Generator")
    print("=" * 60)
    print()
    
    generator = ClimateExperimentGenerator()
    
    print("Generating 500 experimental scenarios...")
    experiments = generator.generate_experiments(500)
    
    print(f"✓ Generated {len(experiments)} experiments")
    print()
    
    # Save to JSON
    generator.save_experiments(experiments, 'climate_experiments.json')
    
    # Generate summary
    summary = generator.generate_summary_report(experiments)
    
    with open('experiment_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print("✓ Saved summary to experiment_summary.json")
    
    # Display summary
    print("\n" + "=" * 60)
    print("EXPERIMENT SUMMARY")
    print("=" * 60)
    print(f"Total Experiments: {summary['total_experiments']}")
    print(f"Average Sample Size: {summary['avg_sample_size']:.0f} users")
    print(f"Total Estimated Cost: ₦{summary['total_estimated_cost']:,.0f}")
    print(f"Average Expected ROI: {summary['avg_expected_roi']:.2f}x")
    print(f"High Priority Experiments: {summary['high_priority_count']}")
    print()
    
    print("Distribution by User Segment:")
    for segment, count in sorted(summary['by_segment'].items()):
        print(f"  {segment}: {count}")
    print()
    
    print("Distribution by Climate Event:")
    for event, count in sorted(summary['by_event'].items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {event}: {count}")
    print()
    
    print("Distribution by Alert Channel:")
    for channel, count in sorted(summary['by_channel'].items()):
        print(f"  {channel}: {count}")
    print()
    
    # Show sample experiments
    print("=" * 60)
    print("SAMPLE EXPERIMENTS (First 3)")
    print("=" * 60)
    for i, exp in enumerate(experiments[:3], 1):
        print(f"\n{i}. {exp['experiment_id']}")
        print(f"   Segment: {exp['user_segment']} | Region: {exp['region']}")
        print(f"   Event: {exp['climate_event']} | Channel: {exp['alert_channel']}")
        print(f"   Hypothesis: {exp['hypothesis']}")
        print(f"   Sample Size: {exp['sample_size']} | Duration: {exp['duration_days']} days")
        print(f"   Expected ROI: {exp['expected_roi']}x | Priority: {exp['priority']}")


if __name__ == "__main__":
    main()
