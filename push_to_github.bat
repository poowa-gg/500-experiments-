@echo off
echo ============================================================
echo GitHub Push Helper
echo ============================================================
echo.
echo This will help you push to GitHub.
echo.
echo IMPORTANT: Create your GitHub repository first!
echo Go to: https://github.com/new
echo.
pause
echo.
echo Enter your GitHub username:
set /p username=Username: 
echo.
echo Enter your repository name (default: climate-intelligence-experiments):
set /p reponame=Repository name: 
if "%reponame%"=="" set reponame=climate-intelligence-experiments
echo.
echo ============================================================
echo Connecting to: https://github.com/%username%/%reponame%.git
echo ============================================================
echo.

git remote add origin https://github.com/%username%/%reponame%.git
git branch -M main
echo.
echo Ready to push! Press any key to continue...
pause
echo.
echo Pushing to GitHub...
git push -u origin main
echo.
echo ============================================================
echo Done! Check your repository at:
echo https://github.com/%username%/%reponame%
echo ============================================================
pause
