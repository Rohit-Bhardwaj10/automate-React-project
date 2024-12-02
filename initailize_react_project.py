import subprocess
import sys
import requests
import os
from getpass import getpass


if len(sys.argv) != 2:
    print("Usage: python setup_react_project_vite.py <project-name>")
    sys.exit(1)

PROJECT_NAME = sys.argv[1]


GITHUB_USERNAME = input("Enter your GitHub username: ")
GITHUB_TOKEN = getpass("Enter your GitHub Personal Access Token (PAT): ")


print(f"Creating React app using Vite: {PROJECT_NAME}")
subprocess.run(['npm', 'create', 'vite@latest', PROJECT_NAME, '--template', 'react', '--force'], check=True)


os.chdir(PROJECT_NAME)


print("Installing dependencies...")
subprocess.run(['npm', 'install'], check=True)


visibility = input("Enter the visibility of the repository (public/private): ")


print("Initializing git repository...")
subprocess.run(['git', 'init'], check=True)


print("Adding files to git...")
subprocess.run(['git', 'add', '.'], check=True)


print("Committing initial files to git...")
subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)

#Create a new repository on GitHub via the API
print("Creating GitHub repository...")
if(visibility=="public"):
    repo_data = {
        "name": PROJECT_NAME,
        "private":False  
    }
else:
    repo_data = {
        "name": PROJECT_NAME,
        "private":True  
        }
# Make the API request to create a new repository on GitHub
response = requests.post(
    'https://api.github.com/user/repos',
    json=repo_data,
    auth=(GITHUB_USERNAME, GITHUB_TOKEN)
)


if response.status_code == 201:
    print("GitHub repository created successfully.")
else:
    print(f"Failed to create repository. Error: {response.status_code}")
    print(response.json())
    sys.exit(1)


remote_url = f'https://github.com/{GITHUB_USERNAME}/{PROJECT_NAME}.git'
subprocess.run(['git', 'remote', 'add', 'origin', remote_url], check=True)


print("Pushing to GitHub...")


subprocess.run(['git', 'branch', '-M', 'main'], check=True)  


subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)


print(f"Setup complete! Your project is now available at: {remote_url}")