# Deploy Your App Online (Free Options)

If you want to make your Climate Experiment Explorer accessible from anywhere (not just localhost), here are free deployment options:

## 🎯 Best Free Options

### 1. Render (Recommended - Easiest)

**Pros:** Free tier, auto-deploys from GitHub, easy setup
**URL:** `your-app.onrender.com`

#### Steps:
1. Push your code to GitHub (use `push_to_github.bat`)
2. Go to https://render.com
3. Sign up with GitHub
4. Click "New +" → "Web Service"
5. Connect your repository
6. Settings:
   - **Name:** climate-experiments
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
7. Click "Create Web Service"
8. Wait 5-10 minutes for deployment
9. Access at: `https://climate-experiments.onrender.com`

**Note:** Free tier sleeps after 15 min of inactivity (takes 30s to wake up)

---

### 2. PythonAnywhere

**Pros:** Python-focused, reliable, good free tier
**URL:** `yourusername.pythonanywhere.com`

#### Steps:
1. Go to https://www.pythonanywhere.com
2. Sign up (free account)
3. Go to "Files" → Upload your project files
4. Go to "Web" → "Add a new web app"
5. Choose "Flask"
6. Set path to your `app.py`
7. Click "Reload" 
8. Access at: `https://yourusername.pythonanywhere.com`

---

### 3. Railway

**Pros:** Modern, fast, GitHub integration
**URL:** `your-app.railway.app`

#### Steps:
1. Push to GitHub first
2. Go to https://railway.app
3. Sign up with GitHub
4. Click "New Project" → "Deploy from GitHub repo"
5. Select your repository
6. Railway auto-detects Python
7. Add environment variables if needed
8. Deploy!
9. Access at: `https://your-app.railway.app`

---

### 4. Heroku (Classic Option)

**Pros:** Well-established, lots of documentation
**URL:** `your-app.herokuapp.com`

#### Steps:

1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli

2. Create `Procfile` in your project:
```bash
echo web: python app.py > Procfile
```

3. Update `app.py` (last line):
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```

4. Deploy:
```bash
heroku login
heroku create climate-experiments
git push heroku main
heroku open
```

---

## 📝 Files Needed for Deployment

### For Render/Railway/Heroku:

1. **requirements.txt** (already have it ✓)
```
Flask==3.0.0
```

2. **Procfile** (create this):
```
web: python app.py
```

3. **Update app.py** (change last line):
```python
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```

---

## 🚀 Quick Deploy Script

I'll create files to help you deploy:

### For Render/Railway/Heroku:

Create `Procfile`:
```bash
echo web: python app.py > Procfile
```

Update `app.py` for production:
```python
# Replace the last section with:
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    # Use debug=False in production
    app.run(debug=False, host='0.0.0.0', port=port)
```

Commit changes:
```bash
git add Procfile app.py
git commit -m "Add deployment configuration"
git push
```

---

## ⚡ Fastest Option: Render

1. Push to GitHub: Run `push_to_github.bat`
2. Go to https://render.com
3. Connect GitHub repo
4. Click deploy
5. Done! Get your URL

**Time:** ~10 minutes total

---

## 💰 Cost Comparison

| Platform | Free Tier | Limitations |
|----------|-----------|-------------|
| Render | ✅ Yes | Sleeps after 15 min inactivity |
| PythonAnywhere | ✅ Yes | Limited CPU time |
| Railway | ✅ Yes | $5 credit/month |
| Heroku | ⚠️ Limited | Requires credit card |

---

## 🎯 Recommendation

**For this project, use Render:**
1. Easiest setup
2. Auto-deploys from GitHub
3. Free tier is generous
4. Good for demos and portfolios

---

## 📊 After Deployment

Once deployed, you can:
- Share the URL with anyone
- Access from any device
- Show to investors/clients
- Add to your portfolio

Example URLs:
- `https://climate-experiments.onrender.com`
- `https://yourusername.pythonanywhere.com`
- `https://climate-experiments.railway.app`

---

## 🔄 Updates

After deployment, to update:
```bash
# Make changes to your code
git add .
git commit -m "Update feature X"
git push
```

Render/Railway auto-deploy from GitHub!

---

## ⚠️ Important Notes

1. **Generate data on first run**: After deployment, visit the site to trigger experiment generation
2. **Free tier limitations**: May sleep after inactivity
3. **Environment**: Set `debug=False` in production
4. **Port**: Use `PORT` environment variable

---

## 🆘 Need Help?

- Render docs: https://render.com/docs
- PythonAnywhere help: https://help.pythonanywhere.com
- Railway docs: https://docs.railway.app

---

**For now, use http://localhost:5000 - it's already working!**
**Deploy online when you're ready to share publicly.**
