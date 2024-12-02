import subprocess
import sys
import requests
import os
from getpass import getpass

# Ensure the script is being run with a project name argument
if len(sys.argv) != 2:
    print("Usage: python setup_react_project_vite.py <project-name>")
    sys.exit(1)

PROJECT_NAME = sys.argv[1]

# Step 1: Get GitHub username and Personal Access Token (PAT) securely
GITHUB_USERNAME = input("Enter your GitHub username: ")
GITHUB_TOKEN = getpass("Enter your GitHub Personal Access Token (PAT): ")

# Step 2: Create the React app using Vite
print(f"Creating React app using Vite: {PROJECT_NAME}")
subprocess.run(['npm', 'create', 'vite@latest', PROJECT_NAME, '--template', 'react', '--force'], check=True)

# Change to the project directory
os.chdir(PROJECT_NAME)

# Step 3: Install dependencies
print("Installing dependencies...")
subprocess.run(['npm', 'install'], check=True)


#step-prompting user for the visbility of the repository
visibility = input("Enter the visibility of the repository (public/private): ")

# Step 4: Initialize a git repository
print("Initializing git repository...")
subprocess.run(['git', 'init'], check=True)

# Step 5: Add all files to git
print("Adding files to git...")
subprocess.run(['git', 'add', '.'], check=True)

# Step 6: Commit the initial files
print("Committing initial files to git...")
subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)

# Step 7: Create a new repository on GitHub via the API
print("Creating GitHub repository...")
if(visibility=="public"):
    repo_data = {
        "name": PROJECT_NAME,
        "private":False  # Set to True for a private repository
    }
else:
    repo_data = {
        "name": PROJECT_NAME,
        "private":True  # Set to True for a private repository
        }
# Make the API request to create a new repository on GitHub
response = requests.post(
    'https://api.github.com/user/repos',
    json=repo_data,
    auth=(GITHUB_USERNAME, GITHUB_TOKEN)
)

# Check for successful repository creation
if response.status_code == 201:
    print("GitHub repository created successfully.")
else:
    print(f"Failed to create repository. Error: {response.status_code}")
    print(response.json())
    sys.exit(1)

# Step 8: Add the remote repository to the local git
remote_url = f'https://github.com/{GITHUB_USERNAME}/{PROJECT_NAME}.git'
subprocess.run(['git', 'remote', 'add', 'origin', remote_url], check=True)

# Step 9: Push to GitHub
print("Pushing to GitHub...")

# Ensure you're on the right branch (main vs. master)
subprocess.run(['git', 'branch', '-M', 'main'], check=True)  # Rename branch to 'main'

# Push to GitHub
subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)

# Final message
print(f"Setup complete! Your project is now available at: {remote_url}")