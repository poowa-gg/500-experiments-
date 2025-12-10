"""
Flask web application for Climate Experiment Explorer
"""

from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load experiments on startup
with open('climate_experiments.json', 'r') as f:
    EXPERIMENTS = json.load(f)

with open('experiment_summary.json', 'r') as f:
    SUMMARY = json.load(f)

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
    print("Open your browser to: http://localhost:5000")
    print("\nPress CTRL+C to stop the server")
    print("="*60 + "\n")
    app.run(debug=True, port=5000)
