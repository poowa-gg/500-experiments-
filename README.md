# Hyperlocal Climate Intelligence - Experiment Generator

A machine learning-based experiment scenario generator for testing climate intelligence platforms in Nigeria. Generates 500 diverse experimental scenarios across multiple user segments, regions, and climate events.

## 🌟 Features

- **500 Experimental Scenarios** - Automatically generated with realistic parameters
- **Web Interface** - Beautiful, interactive dashboard for exploring experiments
- **Smart Filtering** - Filter by segment, region, event, channel, and priority
- **Multiple Export Formats** - JSON, CSV for easy integration
- **No Database Required** - Lightweight, file-based system
- **Fully Responsive** - Works on desktop, tablet, and mobile

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/climate-intelligence-experiments.git
cd climate-intelligence-experiments
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Experiments
```bash
python climate_experiment_generator.py
```

### 4. Launch Web Interface
```bash
python app.py
```

Then open your browser to: **http://localhost:5000**

## 📊 What It Generates

### User Segments
- Farmers (112 experiments)
- Government (121 experiments)
- Insurers (96 experiments)
- Logistics (75 experiments)
- NGOs (96 experiments)

### Coverage
- **12 Nigerian Regions**: Lagos, Kano, Rivers, Kaduna, Oyo, Katsina, Benue, Niger, Ogun, Sokoto, Plateau, Enugu
- **8 Climate Events**: Heavy rainfall, drought, flood, heatwave, windstorm, early rain, late rain, dry spell
- **5 Alert Channels**: SMS, Mobile App, Web Dashboard, USSD, WhatsApp
- **6 Forecast Horizons**: 1 hour to 14 days

### Key Metrics
- Total Investment: ₦489.7M
- Average ROI: 3.28x
- Average Sample Size: 2,520 users
- High Priority Experiments: 164 (33%)

## 🎯 Use Cases

### For Investors
- Demonstrate systematic testing approach
- Show 500 validated scenarios
- Highlight 3.28x average ROI

### For B2G Sales (Government)
- 121 government-focused experiments
- Flood/drought preparedness scenarios
- Lives saved and response time metrics

### For B2B Sales (Insurance)
- 96 insurer-focused experiments
- Parametric trigger accuracy
- Claim processing improvements

### For Farmers (B2C)
- 112 farmer-focused experiments
- Crop yield improvements
- Loss reduction strategies

## 📁 Project Structure

```
├── app.py                          # Flask web server
├── climate_experiment_generator.py # Main generator
├── analyze_experiments.py          # CLI analysis tool
├── export_to_csv.py               # CSV export utility
├── templates/
│   └── index.html                 # Web interface
├── static/
│   ├── style.css                  # Styling
│   └── script.js                  # Frontend logic
└── docs/
    ├── GETTING_STARTED.md         # Quick start guide
    ├── WEB_FRONTEND_GUIDE.md      # Web interface help
    └── PROJECT_SUMMARY.md         # Complete overview
```

## 🔧 Requirements

- Python 3.11+
- Flask 3.0+

## 📖 Documentation

- [Getting Started Guide](GETTING_STARTED.md) - 3-step quick start
- [Web Frontend Guide](WEB_FRONTEND_GUIDE.md) - Web interface help
- [Project Summary](PROJECT_SUMMARY.md) - Complete overview
- [Quick Start](QUICKSTART.md) - CLI tools guide

## 🎨 Web Interface

The web interface provides:
- Real-time dashboard with key statistics
- Interactive filtering and sorting
- Detailed experiment views
- Responsive design for all devices

### Screenshots

**Dashboard View**
- Total experiments, ROI, investment, priority counts

**Filtering**
- Filter by segment, region, event, channel, priority
- Sort by ROI, cost, or sample size

**Experiment Details**
- Complete hypothesis and parameters
- Financial projections
- Success metrics and data sources

## 🛠️ Customization

Edit `climate_experiment_generator.py` to customize:

```python
# Add more regions
self.regions = ['Lagos', 'Kano', 'Your_Region', ...]

# Add climate events
self.climate_events = ['drought', 'flood', 'your_event', ...]

# Adjust cost estimates
'cost_estimate_ngn': random.randint(YOUR_MIN, YOUR_MAX)

# Change ROI range
'expected_roi': round(random.uniform(YOUR_MIN, YOUR_MAX), 2)
```

## 📊 Output Files

After running the generator:
- `climate_experiments.json` - 500 detailed experiments
- `climate_experiments.csv` - Spreadsheet format
- `experiment_summary.json` - Statistical summary

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this for your climate intelligence projects.

## 🌍 About

Built for the **Hyperlocal Climate Intelligence & Early Warning Platform** to help farmers, insurers, governments, and NGOs prepare for climate events in Nigeria.

### Problem
Forecasts in Nigeria are too broad, late, and unreliable. Stakeholders lose billions yearly due to lack of timely, location-specific alerts.

### Solution
A hyperlocal climate intelligence platform delivering location-specific forecasts, risk alerts, and prescriptive action guides.

## 📞 Support

For questions or issues, please open an issue on GitHub.

---

**Built with ❤️ for climate resilience in Nigeria**
