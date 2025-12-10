# 🚀 Getting Started - 3 Simple Steps

## Step 1: Start the Web Server

### Option A: Double-click the launcher
```
Double-click: start_web.bat
```

### Option B: Use command line
```bash
python app.py
```

You'll see:
```
============================================================
Climate Experiment Explorer
============================================================

Starting web server...
Open your browser to: http://localhost:5000

Press CTRL+C to stop the server
============================================================
```

## Step 2: Open Your Browser

Navigate to:
```
http://localhost:5000
```

You'll see a beautiful interface with:
- 📊 Dashboard showing 500 experiments
- 🔍 Filter controls
- 📋 Experiment cards

## Step 3: Explore Your Data

### Quick Wins - Find Best Experiments
1. Click "Sort by ROI" dropdown
2. See highest return experiments first
3. Click any card for full details

### Find Farmer Experiments
1. Select "Farmers" from Segment filter
2. Select "High" from Priority filter
3. Review results

### Budget Planning
1. Select "Sort by Cost"
2. Filter by your target region
3. Find affordable experiments

### Regional Focus
1. Select "Lagos" or "Kano" from Region
2. See all experiments for that area
3. Plan your pilot program

## 🎯 What You Can Do

### Dashboard Overview
- See total experiments (500)
- View average ROI (3.28x)
- Check total investment (₦489.7M)
- Count high priority items (164)

### Filter & Sort
- **By Segment**: Farmers, Insurers, Government, Logistics, NGOs
- **By Region**: 12 Nigerian regions
- **By Event**: Drought, flood, rainfall, heatwave, etc.
- **By Channel**: SMS, Mobile App, Web, USSD, WhatsApp
- **By Priority**: High, Medium, Low
- **Sort**: By ROI, Cost, or Sample Size

### View Details
Click any experiment card to see:
- Complete hypothesis
- Recommended action
- All parameters (sample size, duration, accuracy)
- Financial details (cost, ROI)
- Success metrics
- Data sources
- ML model used

## 💡 Example Workflows

### For Investor Pitch
1. Sort by "ROI" (highest first)
2. Click top 5 experiments
3. Screenshot the details
4. Show systematic approach

### For Government Sales
1. Filter: Segment = "Government"
2. Filter: Priority = "High"
3. Review flood/drought scenarios
4. Export relevant experiments

### For Pilot Planning
1. Filter: Region = "Lagos"
2. Filter: Priority = "High"
3. Sort by "Cost" (lowest first)
4. Select 3-5 experiments to start

### For Budget Allocation
1. Sort by "Cost"
2. Filter by your target segment
3. Calculate total for top 10
4. Plan phased rollout

## 🛑 Stop the Server

When done, press:
```
CTRL + C
```

## 🔄 Restart Anytime

Just run again:
```bash
python app.py
```
or double-click `start_web.bat`

## 📱 Access from Phone/Tablet

1. Find your computer's IP address:
   ```bash
   ipconfig
   ```
2. Edit `app.py`, change last line to:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5000)
   ```
3. Access from any device on same network:
   ```
   http://YOUR_IP:5000
   ```

## 🎨 What Makes This Special

- **No Database**: All data in JSON files
- **Fast**: Instant filtering of 500 experiments
- **Beautiful**: Modern gradient design
- **Responsive**: Works on any screen size
- **Interactive**: Click cards for details
- **Smart**: Combines multiple filters
- **Exportable**: Use CSV for spreadsheets

## 📚 More Help

- **Web Interface**: See `WEB_FRONTEND_GUIDE.md`
- **Quick Start**: See `QUICKSTART.md`
- **Full Docs**: See `README.md`
- **Project Overview**: See `PROJECT_SUMMARY.md`

## ✅ You're All Set!

Your Climate Intelligence Experiment Explorer is ready to use. Start exploring and find the best experiments for your platform!

---

**Need help?** Check the documentation files or review the code comments.
