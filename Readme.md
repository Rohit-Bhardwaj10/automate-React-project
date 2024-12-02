# Initialize React Project with Vite

This Python script automates the process of creating a new React project using Vite, initializing a local Git repository, creating a remote GitHub repository, and pushing the local repository to GitHub.

## Prerequisites

Before you can run the `initialize_react_project.py` script, make sure you have the following installed on your system:

### 1. Python (3.6+)
Make sure you have Python installed. You can check the Python version by running:

```bash
python3 --version

If Python is not installed, you can install it from here.

### 2. Node.js and npm
This script uses npm to create and manage the React project. Ensure that you have Node.js and npm installed by running:

```bash
node --version
npm --version

You can install Node.js and npm by following the instructions from the Node.js website.

3. Git
Git is used to initialize a repository and push to GitHub. You can verify Git is installed by running:
git --version
If Git is not installed, you can install it from here.

4. GitHub Personal Access Token (PAT)
This script interacts with GitHub's API to create a repository. You will need to generate a Personal Access Token (PAT) on GitHub. To generate a token:

Go to GitHub's token page.
Click "Generate new token".
Give it a name and select repo as the scope.
Click "Generate token" and save it somewhere secure.

5. requests Library for Python
The script uses the requests library to interact with the GitHub API. If you don't have it installed, run:
pip3 install requests

Installation and Setup
Step 1: Download the Script
Download the initialize_react_project.py script to your system.

Step 2: Run the Script
You can run the script by executing the following command from your terminal (make sure you're in the same directory as the script):
python3 initialize_react_project.py <your-project-name>
Replace <your-project-name> with the desired name for your React project. This will create a new React project with that name using Vite.

Step 3: Follow the Prompts
After running the script, you will be prompted for the following:

GitHub Username: Enter your GitHub username.
GitHub Personal Access Token (PAT): Enter your GitHub Personal Access Token securely.
Visibility of Repository: Enter public or private to set the visibility of the GitHub repository.

Step 4: Script Execution Process
The script will perform the following steps:

Create a React app using Vite: It will create a new React app using Vite in the directory you specified.
Install dependencies: It will run npm install to install the required dependencies for the React project.
Initialize a Git repository: It will initialize a new Git repository in the project directory.
Create a GitHub repository: It will use GitHub's API to create a remote repository.
Push to GitHub: It will push your local repository to GitHub.
Once the script finishes, your project will be live on GitHub, and you will be provided with a URL to the repository.