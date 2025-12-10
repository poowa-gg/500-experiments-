"""
Flask web application for Climate Experiment Explorer
"""

from flask import Flask, render_template, jsonify, request
import json
import os
import sys

app = Flask(__name__)

# Auto-generate experiments if they don't exist
def ensure_experiments_exist():
    """Generate experiments if JSON files don't exist"""
    if not os.path.exists('climate_experiments.json'):
        print("Generating experiments (first run)...")
        # Import and run the generator
        sys.path.insert(0, os.path.dirname(__file__))
        from climate_experiment_generator import ClimateExperimentGenerator
        
        generator = ClimateExperimentGenerator()
        experiments = generator.generate_experiments(500)
        generator.save_experiments(experiments, 'climate_experiments.json')
        
        summary = generator.generate_summary_report(experiments)
        with open('experiment_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        
        print("✓ Experiments generated successfully!")
        return experiments, summary
    else:
        # Load existing experiments
        with open('climate_experiments.json', 'r') as f:
            experiments = json.load(f)
        with open('experiment_summary.json', 'r') as f:
            summary = json.load(f)
        return experiments, summary

# Load or generate experiments on startup
EXPERIMENTS, SUMMARY = ensure_experiments_exist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/experiments')
def get_experiments():
    """Get all experiments with optional filters"""
    filters = {
        'user_segment': request.args.get('segment'),
        'region': request.args.get('region'),
        'climate_event': request.args.get('event'),
        'alert_channel': request.args.get('channel'),
        'priority': request.args.get('priority')
    }
    
    # Filter experiments
    results = EXPERIMENTS
    for key, value in filters.items():
        if value:
            results = [e for e in results if e.get(key) == value]
    
    # Sort by ROI if requested
    sort_by = request.args.get('sort', 'experiment_id')
    reverse = request.args.get('order', 'desc') == 'desc'
    
    if sort_by in ['expected_roi', 'cost_estimate_ngn', 'sample_size']:
        results = sorted(results, key=lambda x: x.get(sort_by, 0), reverse=reverse)
    
    return jsonify(results)

@app.route('/api/summary')
def get_summary():
    """Get summary statistics"""
    return jsonify(SUMMARY)

@app.route('/api/experiment/<exp_id>')
def get_experiment(exp_id):
    """Get single experiment details"""
    exp = next((e for e in EXPERIMENTS if e['experiment_id'] == exp_id), None)
    if exp:
        return jsonify(exp)
    return jsonify({'error': 'Experiment not found'}), 404

@app.route('/api/filters')
def get_filters():
    """Get available filter options"""
    return jsonify({
        'segments': list(set(e['user_segment'] for e in EXPERIMENTS)),
        'regions': list(set(e['region'] for e in EXPERIMENTS)),
        'events': list(set(e['climate_event'] for e in EXPERIMENTS)),
        'channels': list(set(e['alert_channel'] for e in EXPERIMENTS)),
        'priorities': ['high', 'medium', 'low']
    })

if __name__ == '__main__':
    print("\n" + "="*60)
    print("Climate Experiment Explorer")
    print("="*60)
    print("\nStarting web server...")
    
    # Get port from environment variable (for deployment) or use 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Check if running in production
    is_production = os.environ.get('RENDER') or os.environ.get('HEROKU')
    
    if is_production:
        print(f"Running in production mode on port {port}")
        app.run(debug=False, host='0.0.0.0', port=port)
    else:
        print("Open your browser to: http://localhost:5000")
        print("\nPress CTRL+C to stop the server")
        print("="*60 + "\n")
        app.run(debug=True, host='0.0.0.0', port=port)
