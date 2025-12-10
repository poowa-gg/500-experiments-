# Web Frontend Guide

## 🎉 Your Web Application is Running!

The Climate Experiment Explorer web interface is now live and accessible.

## Access the Application

**Open your browser and go to:**
```
http://localhost:5000
```

## Features

### 📊 Dashboard Overview
- **Total Experiments**: See all 500 generated scenarios
- **Average ROI**: Quick view of expected returns (3.28x)
- **Total Investment**: Estimated cost across all experiments (₦489.7M)
- **High Priority Count**: Number of urgent experiments (164)

### 🔍 Smart Filtering
Filter experiments by:
- **User Segment**: Farmers, Insurers, Government, Logistics, NGOs
- **Region**: Lagos, Kano, Rivers, Kaduna, and 8 more
- **Climate Event**: Drought, flood, heavy rainfall, heatwave, etc.
- **Alert Channel**: SMS, Mobile App, Web Dashboard, USSD, WhatsApp
- **Priority**: High, Medium, Low
- **Sort By**: ROI, Cost, or Sample Size

### 📋 Experiment Cards
Each card shows:
- Experiment ID and priority badge
- User segment and region
- Climate event and alert channel
- Hypothesis statement
- Key metrics: ROI, Cost, Sample Size, Duration

### 🔎 Detailed View
Click any experiment card to see:
- Complete hypothesis and recommended action
- Full experiment parameters
- Financial projections
- Success metrics
- Data sources
- ML model and validation method

## Example Use Cases

### Find High-ROI Farmer Experiments
1. Select "Farmers" from Segment filter
2. Select "High" from Priority filter
3. Sort by "ROI"
4. Click any card for full details

### Budget-Conscious Planning
1. Sort by "Cost" (ascending)
2. Filter by your target region
3. Review low-cost, high-impact experiments

### Regional Focus
1. Select "Lagos" or "Kano" from Region filter
2. Review all experiments for that area
3. Identify quick wins for pilot programs

### Channel-Specific Analysis
1. Select "SMS" from Channel filter
2. See all SMS-based experiments
3. Useful for planning communication infrastructure

## Tips

- **Reset Filters**: Click "Reset Filters" button to clear all selections
- **Multiple Filters**: Combine filters for precise results
- **Click Cards**: Always click experiment cards for complete details
- **Responsive Design**: Works on desktop, tablet, and mobile

## Stop the Server

When you're done, press `CTRL+C` in the terminal where the server is running.

## Restart the Server

```bash
python app.py
```

## Technical Details

- **Framework**: Flask (Python web framework)
- **Frontend**: Vanilla JavaScript (no dependencies)
- **Styling**: Custom CSS with gradient design
- **Data**: Loads from `climate_experiments.json`
- **API Endpoints**: RESTful JSON API for filtering

## Next Steps

1. **Explore the data** using filters
2. **Identify top experiments** for your pilot
3. **Export specific sets** using the Python analysis tools
4. **Share with stakeholders** by opening the URL on your network

## Troubleshooting

**Port already in use?**
```bash
# Change port in app.py, line: app.run(debug=True, port=5000)
# Change 5000 to another port like 5001
```

**Can't access from another device?**
```bash
# Change app.run to:
app.run(debug=True, host='0.0.0.0', port=5000)
# Then access via: http://YOUR_IP:5000
```

---

**Enjoy exploring your 500 climate intelligence experiments!** 🌍
