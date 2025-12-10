# GitHub Push Guide - Step by Step

## 📋 Pre-Push Checklist

### Files to Keep (Will be pushed to GitHub)
✅ Python scripts (.py files)
✅ Web application (app.py, templates/, static/)
✅ Documentation (.md files)
✅ Configuration (requirements.txt, .gitignore)
✅ Utilities (start_web.bat)

### Files to Exclude (Already in .gitignore)
❌ climate_experiments.json (423 KB - too large, regenerate instead)
❌ climate_experiments.csv (107 KB - too large, regenerate instead)
❌ experiment_summary.json (generated file)
❌ .vscode/ (IDE settings)
❌ __pycache__/ (Python cache)

## 🚀 Step-by-Step Push Instructions

### Step 1: Initialize Git (if not already done)

```bash
git init
```

### Step 2: Configure Git (First time only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Check What Will Be Committed

```bash
git status
```

You should see:
- Green: Files ready to commit
- Red: Untracked files
- Files in .gitignore won't show up

### Step 4: Add Files to Git

```bash
# Add all files (respects .gitignore)
git add .

# Or add specific files
git add *.py *.md requirements.txt
git add templates/ static/
git add .gitignore start_web.bat
```

### Step 5: Verify What's Staged

```bash
git status
```

Make sure large data files (JSON, CSV) are NOT listed.

### Step 6: Create First Commit

```bash
git commit -m "Initial commit: Climate Intelligence Experiment Generator"
```

### Step 7: Create GitHub Repository

1. Go to https://github.com
2. Click "+" → "New repository"
3. Name it: `climate-intelligence-experiments`
4. Description: "ML-based experiment generator for climate intelligence platform"
5. Choose: Public or Private
6. **DO NOT** initialize with README (we already have one)
7. Click "Create repository"

### Step 8: Connect to GitHub

GitHub will show you commands. Use these:

```bash
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/climate-intelligence-experiments.git

# Verify remote
git remote -v
```

### Step 9: Push to GitHub

```bash
# Push to main branch
git push -u origin main
```

If you get an error about "master" vs "main":

```bash
# Rename branch to main
git branch -M main

# Then push
git push -u origin main
```

### Step 10: Verify on GitHub

1. Go to your repository URL
2. Check that files are uploaded
3. Verify README.md displays correctly

## 🔧 Common Issues & Solutions

### Issue 1: Large Files Error

**Error:** "file is too large"

**Solution:**
```bash
# Remove large files from staging
git rm --cached climate_experiments.json
git rm --cached climate_experiments.csv

# Commit the removal
git commit -m "Remove large data files"

# Push again
git push
```

### Issue 2: Authentication Failed

**Solution:**
Use Personal Access Token instead of password:

1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo`
4. Copy the token
5. Use token as password when pushing

Or use SSH:
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add to GitHub: Settings → SSH and GPG keys
# Change remote to SSH
git remote set-url origin git@github.com:YOUR_USERNAME/climate-intelligence-experiments.git
```

### Issue 3: Branch Name Mismatch

**Error:** "src refspec main does not match any"

**Solution:**
```bash
# Check current branch
git branch

# Rename to main if needed
git branch -M main

# Push
git push -u origin main
```

### Issue 4: Merge Conflicts

**Error:** "Updates were rejected"

**Solution:**
```bash
# Pull first
git pull origin main --allow-unrelated-histories

# Resolve conflicts if any
# Then push
git push origin main
```

## 📝 After First Push

### Update README on GitHub

Replace README.md with README_GITHUB.md:

```bash
# Backup current README
mv README.md README_LOCAL.md

# Use GitHub version
mv README_GITHUB.md README.md

# Commit and push
git add README.md
git commit -m "Update README for GitHub"
git push
```

### Add Repository Description

On GitHub:
1. Go to repository
2. Click "About" (gear icon)
3. Add description: "ML-based experiment generator for climate intelligence platform in Nigeria"
4. Add topics: `climate`, `machine-learning`, `nigeria`, `flask`, `experiments`

### Create Releases

1. Go to "Releases" → "Create a new release"
2. Tag: `v1.0.0`
3. Title: "Initial Release - 500 Experiment Generator"
4. Description: Key features and usage
5. Publish release

## 🔄 Future Updates

### Making Changes

```bash
# Make your changes to files

# Check what changed
git status
git diff

# Stage changes
git add .

# Commit with descriptive message
git commit -m "Add new feature: X"

# Push to GitHub
git push
```

### Good Commit Messages

✅ Good:
- "Add filtering by forecast horizon"
- "Fix ROI calculation bug"
- "Update documentation for web interface"

❌ Bad:
- "Update"
- "Fix stuff"
- "Changes"

## 📊 Repository Structure on GitHub

```
climate-intelligence-experiments/
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── climate_experiment_generator.py
├── analyze_experiments.py
├── export_to_csv.py
├── start_web.bat
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── docs/ (optional)
    ├── GETTING_STARTED.md
    ├── WEB_FRONTEND_GUIDE.md
    ├── PROJECT_SUMMARY.md
    └── QUICKSTART.md
```

## ✅ Final Checklist

Before pushing:
- [ ] .gitignore file created
- [ ] Large data files excluded
- [ ] All Python scripts included
- [ ] Documentation files included
- [ ] Web application files included
- [ ] requirements.txt updated
- [ ] README.md is clear and helpful
- [ ] Commit message is descriptive

After pushing:
- [ ] Repository is accessible on GitHub
- [ ] README displays correctly
- [ ] Files are organized properly
- [ ] No sensitive data exposed
- [ ] Repository description added
- [ ] Topics/tags added

## 🎉 You're Done!

Your project is now on GitHub and ready to share!

Share your repository:
```
https://github.com/YOUR_USERNAME/climate-intelligence-experiments
```

## 📞 Need Help?

- GitHub Docs: https://docs.github.com
- Git Basics: https://git-scm.com/book/en/v2
- GitHub Desktop: https://desktop.github.com (GUI alternative)
