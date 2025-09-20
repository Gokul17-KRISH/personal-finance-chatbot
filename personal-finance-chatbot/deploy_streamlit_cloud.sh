#!/bin/bash
# Script to deploy the Personal Finance Chatbot to Streamlit Cloud

# Step 1: Initialize git repository if not already done
git init

# Step 2: Add all files
git add .

# Step 3: Commit changes
git commit -m "Initial commit for Personal Finance Chatbot"

# Step 4: Create a new GitHub repository manually or via CLI (not included here)
# Step 5: Add remote origin (replace with your GitHub repo URL)
# git remote add origin https://github.com/yourusername/your-repo-name.git

# Step 6: Push to GitHub
git push -u origin main

# After pushing, go to https://streamlit.io/cloud and connect your GitHub repo to deploy the app.
