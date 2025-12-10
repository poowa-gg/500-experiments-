
# Hyperlocal Climate Intelligence - Experiment Generator

A lightweight machine learning model that generates 500 diverse experimental scenarios for testing your Hyperlocal Climate Intelligence & Early Warning Platform.

## What It Does

Generates realistic experimental scenarios across:
- **5 User Segments**: Farmers, Insurers, Government, Logistics, NGOs
- **12 Nigerian Regions**: Lagos, Kano, Rivers, Kaduna, Oyo, etc.
- **8 Climate Events**: Heavy rainfall, drought, flood, heatwave, windstorm, etc.
- **5 Alert Channels**: SMS, Mobile App, Web Dashboard, USSD, WhatsApp
- **6 Forecast Horizons**: 1 hour to 14 days

## Quick Start

### Option 1: Web Interface (Recommended)
```bash
python app.py
```
Then open your browser to: **http://localhost:5000**

### Option 2: Command Line
```bash
python climate_experiment_generator.py
```

## Output Files

1. **climate_experiments.json** - 500 detailed experiment scenarios
2. **experiment_summary.json** - Statistical summary and distributions

## Experiment Structure

Each experiment includes:
- Unique ID and user segment
- Geographic region and climate event
- Alert channel and forecast horizon
- Hypothesis and success metrics
- Sample size and duration
- Cost estimate and expected ROI
- ML model and validation method
- Data sources

## Example Use Cases

### For Farmers
- Test when SMS alerts about drought improve irrigation timing
- Measure crop yield improvement from 7-day rainfall forecasts

### For Insurers
- Validate parametric trigger accuracy for flood events
- Test claim processing speed with real-time weather data

### For Government
- Evaluate evacuation response times with 24-hour flood warnings
- Measure lives saved through early heatwave alerts

### For Logistics
- Test route optimization during windstorm predictions
- Measure delivery success rates with weather-aware planning

### For NGOs
- Assess aid distribution efficiency with climate forecasts
- Test volunteer mobilization speed for disaster response

## Key Metrics Generated

- Average Sample Size: ~2,500 users per experiment
- Total Investment: ~₦490M across all experiments
- Average Expected ROI: 3.28x
- High Priority Experiments: ~33% of total

## Customization

Edit the `ClimateExperimentGenerator` class to:
- Add more regions or climate events
- Adjust accuracy levels or lead times
- Modify success metrics per segment
- Change cost estimates or ROI ranges

## Next Steps

1. **Prioritize**: Start with high-priority, high-ROI experiments
2. **Pilot**: Run small-scale tests in 1-2 regions
3. **Measure**: Track actual vs. predicted metrics
4. **Scale**: Expand successful experiments nationwide
5. **Iterate**: Refine models based on real-world results

## Business Impact

This generator helps you:
- Plan systematic platform testing
- Allocate resources efficiently
- Demonstrate value to investors
- Build evidence for B2G/B2B sales
- Meet SDG and ESG targets with data
