@echo off
REM Windows batch script to deploy Personal Finance Chatbot to Streamlit Cloud

echo ========================================
echo Deploying Personal Finance Chatbot
echo ========================================

REM Check if git is installed
git --version
if errorlevel 1 (
    echo Git is not installed. Please install Git from https://git-scm.com/
    pause
    exit /b 1
)

REM Initialize git repository if not already done
if not exist .git (
    git init
    echo Git repository initialized.
) else (
    echo Git repository already exists.
)

REM Add all files
git add .
echo Files added to git.

REM Commit changes
git commit -m "Initial commit for Personal Finance Chatbot"
echo Changes committed.

echo ========================================
echo NEXT STEPS:
echo ========================================
echo 1. Create a new repository on GitHub.com
echo 2. Copy the repository URL
echo 3. Run: git remote add origin YOUR_REPO_URL
echo 4. Run: git push -u origin main
echo 5. Go to https://streamlit.io/cloud
echo 6. Connect your GitHub repository
echo 7. Deploy your app!
echo ========================================
echo.
echo Your app will be available at: https://yourusername-yourrepo.streamlit.app
echo ========================================

pause
