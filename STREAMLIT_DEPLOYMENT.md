# 🚀 Streamlit Deployment Guide

## Quick Deploy to Render

### Option 1: Update Existing Service

1. **Update your repository:**
```bash
git add streamlit_app.py requirements_streamlit.txt
git commit -m "Add Streamlit interactive playground"
git push
```

2. **Update Render service:**
   - Go to https://dashboard.render.com
   - Select your service
   - Go to "Settings"
   - Change **Start Command** to: `streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`
   - Change **Build Command** to: `pip install -r requirements_streamlit.txt`
   - Click "Save Changes"
   - Click "Manual Deploy" → "Deploy latest commit"

### Option 2: Create New Streamlit Service

1. Push code to GitHub
2. Go to https://dashboard.render.com
3. Click "New +" → "Web Service"
4. Connect your repository
5. Settings:
   - **Name:** climate-ml-playground
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements_streamlit.txt`
   - **Start Command:** `streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`
6. Click "Create Web Service"

## One-Line Deploy Command

```bash
git add streamlit_app.py requirements_streamlit.txt && git commit -m "Add Streamlit app" && git push
```

Then update Render start command to:
```
streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
```

## Embed in Existing HTML

Add this iframe to your current `index.html`:

```html
<iframe 
    src="https://climate-experiments.onrender.com" 
    width="100%" 
    height="800px" 
    frameborder="0"
    style="border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"
></iframe>
```

Or create a dedicated page:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Climate × ML Playground</title>
    <style>
        body { margin: 0; padding: 0; overflow: hidden; }
        iframe { width: 100vw; height: 100vh; border: none; }
    </style>
</head>
<body>
    <iframe src="https://climate-experiments.onrender.com"></iframe>
</body>
</html>
```

## Features Included

✅ Hero section with gradient design
✅ 3 interactive datasets (Global Temp, Arctic Ice, CO2)
✅ Real-time ML forecasting with scikit-learn
✅ Sortable data tables with Plotly charts
✅ Download buttons for all datasets
✅ Leaderboard with placeholders
✅ WhatsApp CTA in sidebar + all tabs
✅ Integration with your experiment generator
✅ Dark theme, mobile-friendly
✅ Sticky sidebar with metrics

## Testing Locally

```bash
pip install -r requirements_streamlit.txt
streamlit run streamlit_app.py
```

Opens at: http://localhost:8501

## URL After Deployment

Your app will be live at:
- https://climate-experiments.onrender.com (if updating existing)
- https://climate-ml-playground.onrender.com (if new service)

## Performance Notes

- First load: ~30 seconds (free tier)
- Subsequent loads: Instant
- Data caching enabled for fast reloads
- Auto-generates experiments on demand

## Customization

Edit `streamlit_app.py` to:
- Change WhatsApp link
- Update metrics
- Add more datasets
- Modify color scheme
- Adjust model parameters

---

**Deploy now and watch ML engineers join your WhatsApp channel!** 🚀
