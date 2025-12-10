"""
Export experiments to CSV for spreadsheet analysis
"""

import json
import csv

def export_to_csv():
    # Load experiments
    with open('climate_experiments.json', 'r') as f:
        experiments = json.load(f)
    
    # Define CSV columns
    fieldnames = [
        'experiment_id', 'user_segment', 'region', 'climate_event',
        'alert_channel', 'forecast_horizon', 'predicted_accuracy',
        'lead_time_hours', 'recommended_action', 'sample_size',
        'duration_days', 'cost_estimate_ngn', 'expected_roi',
        'priority', 'ml_model', 'validation_method', 'hypothesis'
    ]
    
    # Write to CSV
    with open('climate_experiments.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for exp in experiments:
            row = {k: exp.get(k, '') for k in fieldnames}
            # Convert lists to strings
            if isinstance(row.get('success_metrics'), list):
                row['success_metrics'] = ', '.join(exp.get('success_metrics', []))
            if isinstance(row.get('data_sources'), list):
                row['data_sources'] = ', '.join(exp.get('data_sources', []))
            writer.writerow(row)
    
    print(f"✓ Exported {len(experiments)} experiments to climate_experiments.csv")
    print("  Open in Excel, Google Sheets, or any spreadsheet software")

if __name__ == "__main__":
    export_to_csv()
