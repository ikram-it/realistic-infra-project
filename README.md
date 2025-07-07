# Realistic Infrastructure Project: Web App Stack with Docker Compose

This project demonstrates a simple web application stack including:
- Nginx (as a reverse proxy)
- A Python Flask web application
- PostgreSQL database

All services are containerized using Docker and orchestrated with Docker Compose.
CI/CD is implemented using GitHub Actions for linting and Docker image building.

## Project Structure

![alt text](image.png)

 Conversation with Gemini

I am a infrastructure guy, i wish to learn about github, please guide me as newbie to learn Github branch, merge,CICD with a sample project & other relevant things. I am working in a windows PC. Please suggest me the IDE too.I have VScode installed where i work on python.

It's great you're looking to dive into GitHub as an infrastructure professional! Understanding version control, branching, merging, and CI/CD is incredibly valuable, even if your primary role isn't development. Let's break down a learning path for you, keeping your Windows environment and existing VS Code setup in mind.

Learning GitHub for Infrastructure Professionals

1. Fundamental Concepts First (Before Jumping into Code)

    Version Control: What is it and why is it important? Think about tracking changes to configuration files, scripts, or even documentation.

    Git vs. GitHub: Git is the version control system (the engine), and GitHub is a hosting service for Git repositories (the platform where you store and collaborate).

    Repositories (Repos): Your project folder managed by Git.

    Commits: Snapshots of your changes at a specific point in time. Each commit has a unique ID.

    Branches: Independent lines of development. This is crucial for collaborative work and testing changes without affecting the main codebase.

    Merge: Combining changes from different branches.

    Clone, Pull, Push: Basic Git commands for interacting with remote repositories.

Resources for Concepts:

    Git Handbook (GitHub Guides): This is a fantastic, visual introduction: https://guides.github.com/introduction/flow/

    Atlassian Git Tutorial: Very comprehensive and well-explained: https://www.atlassian.com/git/tutorials

2. Setting Up Your Environment

You're already on a Windows PC and have VS Code, which is perfect!

    Install Git for Windows:

        Go to https://git-scm.com/download/win

        Download and run the installer.

        During installation, the default options are usually fine. Ensure "Git Bash" is selected, as it provides a Linux-like terminal experience which is very helpful for Git commands. You can also opt to integrate Git with the Windows Command Prompt or PowerShell.

    Configure Git: Open Git Bash (or your preferred terminal) and run these commands once:
    Bash

    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"

    This identifies your commits.

    VS Code Git Integration: VS Code has excellent built-in Git integration. You'll see a Source Control icon on the left sidebar (it looks like three interconnected circles).

3. Hands-on Sample Project: Infrastructure as Code (IaC) Script

Instead of a Python application, let's create a simple "Infrastructure as Code" project. This will be more relevant to your infrastructure background. We'll simulate managing some configuration files or deployment scripts.

Project Idea: Simple Server Configuration Scripts

Imagine you have scripts to configure a web server (e.g., Nginx or Apache) and a database server.

Steps:

A. Initialize Your Local Repository

    Create a Project Folder:

        Open your terminal (Git Bash, PowerShell, or CMD).

        cd C:\Users\YourUser\Documents (or wherever you want your projects)

        mkdir infrastructure-project

        cd infrastructure-project

    Initialize Git:

        git init (This creates a hidden .git folder, making it a Git repository.)

    Open in VS Code:

        code . (This opens the current directory in VS Code.)

B. Create Initial Files & First Commit

    In VS Code, create the following files and folders:

        README.md (for project description)

        web-server/ (folder)

            web-server/nginx-config.sh (a dummy script)

        db-server/ (folder)

            db-server/mysql-setup.sh (a dummy script)

    Add Content (Example):

        README.md:
        Markdown

# Infrastructure Configuration Project

This repository contains scripts for configuring web and database servers.

web-server/nginx-config.sh:
Bash

#!/bin/bash
echo "Configuring Nginx web server..."
# Add Nginx configuration commands here
echo "Nginx configured successfully."

db-server/mysql-setup.sh:
Bash

    #!/bin/bash
    echo "Setting up MySQL database..."
    # Add MySQL setup commands here
    echo "MySQL setup complete."

Stage and Commit:

    VS Code (Recommended for Newbies): Go to the Source Control tab (Ctrl+Shift+G). You'll see your new files listed under "Changes." Hover over "Changes" and click the + sign (Stage All Changes). Then, type a commit message (e.g., "Initial project setup with basic server scripts") in the message box and click the checkmark icon to commit.

    Terminal (Alternative):
    Bash

        git add . # Stages all new and modified files
        git commit -m "Initial project setup with basic server scripts"

C. GitHub Repository Creation

    Create a New Repository on GitHub:

        Go to https://github.com/new

        Repository Name: infrastructure-project (or anything you like)

        Description: "Scripts for server configuration (web and DB)"

        Visibility: Choose "Public" or "Private" (Private is fine for personal learning).

        DO NOT check "Add a README file," "Add .gitignore," or "Choose a license" – you already have these locally.

        Click "Create repository."

    Link Local to Remote: GitHub will show you commands. Copy and paste the following into your terminal (from your infrastructure-project directory):
    Bash

    git remote add origin https://github.com/YOUR_GITHUB_USERNAME/infrastructure-project.git
    git branch -M main # Renames your default branch to 'main'
    git push -u origin main # Pushes your local 'main' branch to GitHub

    (Replace YOUR_GITHUB_USERNAME with your actual GitHub username.)

        git remote add origin: Tells Git that "origin" is a shorthand for your GitHub repository URL.

        git branch -M main: Renames your default branch from master (old default) to main (new standard).

        git push -u origin main: Pushes your main branch to the origin remote, and -u sets it up so future git push commands without arguments will push to origin main.

    Refresh your GitHub repository page; you should now see your files!

4. GitHub Branching and Merging Workflow

This is where the power of Git shines.

Scenario: You need to add a new script for firewall configuration, but you don't want to mess with the existing working scripts on main.

    Create a New Branch:

        Terminal: git branch feature/add-firewall

        VS Code: Click on the branch name in the bottom-left status bar (probably "main"). Type feature/add-firewall and press Enter.

        Switch to the New Branch:

            Terminal: git checkout feature/add-firewall

            (If you used VS Code, it automatically switched.)

            You can verify by running git branch (the current branch will have an asterisk) or looking at the bottom-left of VS Code.

    Make Changes on the New Branch:

        In VS Code, create a new file: firewall/iptables-rules.sh

        Add some content:
        Bash

        #!/bin/bash
        echo "Configuring iptables firewall rules..."
        # Add iptables commands here
        echo "Firewall rules applied."

    Commit Changes on the New Branch:

        Stage the firewall/ folder and iptables-rules.sh file.

        Commit message: "Add firewall configuration script"

    Push the New Branch to GitHub:

        Terminal: git push -u origin feature/add-firewall

        VS Code: Go to the Source Control tab, click the "..." (more actions) menu, then "Push." It might ask you to confirm pushing the new branch.

    Go to your GitHub repository. You'll see a notification about the new branch and a button to "Compare & pull request."

    Create a Pull Request (PR):

        A Pull Request is a request to merge your changes from one branch into another (usually main). This is where code reviews happen.

        On GitHub, click the "Compare & pull request" button.

        Title: "Feature: Add firewall configuration"

        Description: "This PR introduces a new script for managing iptables firewall rules."

        Click "Create pull request."

    Review and Merge:

        As the repository owner, you can now review the changes. In a real team, others would review.

        Click the "Files changed" tab to see the differences.

        If everything looks good, click the "Merge pull request" button, then "Confirm merge."

        Click "Delete branch" (optional, but good practice after merging) – this only deletes the branch on GitHub, not locally yet.

    Update Your Local main Branch:

        Switch back to main:

            Terminal: git checkout main

            VS Code: Click the branch name in the status bar, then select main.

        Pull changes from GitHub:

            Terminal: git pull origin main

            VS Code: Click the "Synchronize Changes" button in the bottom-left status bar (looks like two arrows). This pulls down the merged changes from main on GitHub.

    Now your local main branch is up-to-date with the firewall script.

5. Continuous Integration/Continuous Deployment (CI/CD) with GitHub Actions

CI/CD automates testing and deployment. For infrastructure, this could mean:

    Linting your shell scripts (checking for syntax errors, best practices).

    Running integration tests (e.g., using a tool like Terratest for Terraform configurations).

    Deploying configurations to a test environment.

Let's create a very simple GitHub Actions workflow to "lint" our shell scripts.

    Create Workflow Folder:

        In your infrastructure-project directory, create: .github/workflows/

    Create Workflow File:

        Inside .github/workflows/, create shell-lint.yml

    Add Workflow Content (shell-lint.yml):
    YAML

    name: Shell Script Linting

    on:
      push:
        branches:
          - main # Run when changes are pushed to the main branch
      pull_request:
        branches:
          - main # Run when a pull request targets the main branch

    jobs:
      lint:
        runs-on: ubuntu-latest # Run this job on an Ubuntu virtual machine

        steps:
        - name: Checkout repository
          uses: actions/checkout@v4 # Action to check out your code

        - name: Set up ShellCheck
          run: |
            sudo apt-get update
            sudo apt-get install -y shellcheck # Install ShellCheck linter

        - name: Lint shell scripts
          run: |
            find . -name "*.sh" -print0 | xargs -0 -n1 shellcheck # Find and lint all .sh files
          # You might want to exclude certain folders if they contain binaries or sensitive files
          # For example: find . -name "*.sh" ! -path "./node_modules/*" -print0 | xargs -0 -n1 shellcheck

    Commit and Push the Workflow:

        Stage .github/ folder.

        Commit message: "Add ShellCheck linting workflow"

        Push to main: git push origin main

    Observe GitHub Actions:

        Go to your GitHub repository.

        Click on the "Actions" tab. You should see your "Shell Script Linting" workflow running (or already completed).

        Click on the workflow run to see the details and logs. If there are no errors in your scripts, it should pass.

    To see a failure: Introduce a syntax error in one of your .sh files (e.g., echo "Hello without closing quotes), commit, and push. Observe the failed GitHub Action. Then fix it, commit, and push again to see it pass.

6. Other Relevant Things for Infrastructure Guys

    .gitignore: This file tells Git which files or directories to ignore (e.g., temporary files, sensitive data, build artifacts, .DS_Store on macOS). Create one at the root of your project:

    # Ignore compiled Python files
    *.pyc
    __pycache__/

    # Ignore editor specific files
    .vscode/
    .idea/

    # Ignore environment variables
    .env

    # Ignore log files
    *.log

    Then git add .gitignore and commit.

    SSH Keys for Authentication: Instead of typing your username/password every time you push/pull, you can set up SSH keys for secure authentication with GitHub. This is common in professional environments.

        GitHub Docs: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

    Git Tags: Use tags to mark specific points in your repository's history, like release versions (e.g., v1.0.0).

        git tag -a v1.0.0 -m "Initial stable release"

        git push origin v1.0.0

    GitHub Issues: Use Issues to track bugs, features, and tasks for your project. Great for project management.

    GitHub Projects: Kanban boards and other tools to organize your work.

    GitHub Pages: Host static websites directly from your GitHub repository (useful for documentation).

    GitHub CLI: Command-line interface for GitHub, allowing you to interact with GitHub without leaving your terminal.

        https://cli.github.com/

    Using Git with PowerShell: While Git Bash is popular, you can also use Git commands directly in PowerShell if you prefer. Just make sure Git is in your system's PATH.

    Visual Git Clients: While VS Code's integration is good, dedicated GUI clients like GitKraken or Sourcetree can provide a more visual way to manage your repositories, especially when dealing with complex histories. However, I recommend learning the command line first for a deeper understanding.

IDE Suggestion

You already have VS Code, and it is by far the best choice for your needs.

    Built-in Git Integration: As you've seen, it provides a very intuitive interface for staging, committing, branching, and syncing.

    Extensions: A vast marketplace of extensions for Python development, shell scripting, YAML linting (for GitHub Actions), and more.

    Integrated Terminal: You can open Git Bash, PowerShell, or CMD directly within VS Code, so you don't need to switch windows.

    Lightweight and Fast: Doesn't consume too many resources.

Key VS Code Features to Explore for Git:

    Source Control View (Ctrl+Shift+G): Your primary hub for Git operations.

    Diff Editor: VS Code clearly shows you line-by-line differences when you click on a changed file.

    Timeline View: Right-click a file in the Explorer and choose "Open Timeline" to see a history of commits affecting that file.

    Git Graph Extension: (Highly Recommended!) Search for and install the "Git Graph" extension. It provides a beautiful visual representation of your repository's commit history, branches, and merges, which is incredibly helpful for understanding what's going on.

Next Steps & Continuous Learning

    Practice, Practice, Practice: The best way to learn is by doing. Create more small projects, experiment with branches, and try to break things (and fix them!).

    Collaborate: If you have colleagues also interested, try working on a shared repository to experience real-world branching and merging conflicts.

    Explore Advanced Git Concepts:

        Rebase: For cleaning up commit history.

        Cherry-pick: Applying specific commits from one branch to another.

        Stash: Temporarily saving changes without committing.

        Reflog: Your safety net to recover lost commits.

    Deep Dive into GitHub Actions: As an infrastructure person, understanding how to automate deployments, tests, and compliance checks with GitHub Actions will be incredibly powerful. Look into using more complex actions, secrets management, and environment targeting.

    Learn a Configuration Management Tool: If you're not already, consider learning tools like Ansible, Puppet, Chef, or Terraform. These tools, combined with Git and GitHub, form the core of modern infrastructure automation (DevOps/GitOps).

You're on a great path to enhancing your infrastructure skills with version control and automation! Good luck!

stg@STG-LAPTOP-01 MINGW64 /d/MyRepo/infrastructure-project (main)

$ git remote add origin https://github.com/ikram-it/infrastructure-project.git

git branch -M main

git push -u origin main

error: remote origin already exists.

info: please complete authentication in your browser...

remote: Repository not found.

fatal: repository 'https://github.com/YOUR_GITHUB_USERNAME/infrastructure-projec

t.git/' not found

It looks like you encountered a couple of common issues, which is great because it gives us a chance to debug and learn! Let's break down the errors and how to fix them.

Error 1: error: remote origin already exists.

Reason: This means you've already run git remote add origin ... at some point for this local repository. Git remembers that origin points to a specific remote URL.

Solution:
You have two main options:

    Remove the existing remote and add it again (most common fix if the URL was wrong):
    Bash

git remote remove origin
git remote add origin https://github.com/ikram-it/infrastructure-project.git

Change the URL of the existing remote (if origin was already there but pointing to the wrong place):
Bash

    git remote set-url origin https://github.com/ikram-it/infrastructure-project.git

In your case, since you're setting it up for the first time for ikram-it, using git remote remove origin first, then git remote add origin ... is usually the cleanest approach.

Error 2: remote: Repository not found. and fatal: repository 'https://github.com/YOUR_GITHUB_USERNAME/infrastructure-project.git/' not found

Reason: This is the critical error. It means that the URL you provided to GitHub (https://github.com/ikram-it/infrastructure-project.git) either:

    Does not exist on GitHub. You might have made a typo in the username (ikram-it) or the repository name (infrastructure-project).

    Exists, but you don't have permission to push to it. This is less likely if you just created it under your own account and are logged in.

    You used a placeholder: Your error message explicitly says fatal: repository 'https://github.com/YOUR_GITHUB_USERNAME/infrastructure-project.git/' not found. This suggests you copied the command directly from a guide (like mine!) without replacing YOUR_GITHUB_USERNAME with your actual GitHub username.

Crucial Check:

    Did you actually create the repository infrastructure-project on GitHub under your account ikram-it?

        Go to https://github.com/ikram-it/infrastructure-project in your browser.

        If it gives a 404 "Not Found" error, then the repository does not exist, and you need to create it first.

        If it exists, verify the exact URL in the browser's address bar.

Step-by-Step Fix for Your Situation

Let's assume your GitHub username is ikram-it and you want your repository name to be infrastructure-project.

1. Verify GitHub Repository Existence:

    Go to https://github.com/new in your web browser.

    Log in with your GitHub account (ikram-it).

    Repository name: Type infrastructure-project (exactly).

    Description: (Optional) "My infrastructure scripts"

    Visibility: Choose "Public" or "Private".

    IMPORTANT: Make sure "Initialize this repository with a README" is NOT checked, as you already have a README.md locally.

    Click "Create repository".

    Once created, you should see a page with instructions on how to push an existing repository. The URL provided there should be exactly https://github.com/ikram-it/infrastructure-project.git.

2. Correct Your Git Commands in Git Bash:

Open your Git Bash terminal in your infrastructure-project directory.
Bash

# 1. Remove the old 'origin' remote (since it already exists and might be wrong)
git remote remove origin

# 2. Add the correct 'origin' remote with your actual GitHub username and repo name
#    Make sure 'ikram-it' is your exact GitHub username
git remote add origin https://github.com/ikram-it/infrastructure-project.git

# 3. Rename your local default branch to 'main' (standard practice)
git branch -M main

# 4. Push your local 'main' branch to the 'origin' remote on GitHub
#    The '-u' sets 'origin/main' as the upstream branch, so future 'git push' (without args) will work.
git push -u origin main

3. Authentication:

When you run git push, if you haven't set up SSH keys or a credential helper, Git will prompt you for authentication.

    Windows Credential Manager (Recommended for HTTPS on Windows): Git for Windows usually sets up a credential manager. When prompted with info: please complete authentication in your browser..., a browser window should pop up asking you to log into GitHub. Complete the login, and it will store your credentials securely so you don't have to enter them every time.

    Personal Access Token (PAT): For more robust security or if the browser method fails, you can create a Personal Access Token on GitHub and use that as your password when prompted.

        Go to GitHub -> Settings -> Developer settings -> Personal access tokens -> Tokens (classic) -> Generate new token.

        Give it a descriptive name (e.g., "Git for infrastructure-project").

        Grant it repo scope (full control of private repositories).

        Generate the token and copy it immediately (you won't see it again).

        When git push prompts for your password, paste the PAT instead of your GitHub password.

After following these steps, your push should succeed, and you should see your local files appear on your GitHub repository page. Let me know if you run into any more issues!

C:\Users\stg>ssh-add C:\Users\stg\.ssh\ikramsshkey

Bad permissions. Try removing permissions for user: STG-LAPTOP-01\\mis (S-1-5-21-318855882-392476681-3897922682-1010) on file C:/Users/stg/.ssh/ikramsshkey.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Permissions for 'C:\\Users\\stg\\.ssh\\ikramsshkey' are too open.

It is required that your private key files are NOT accessible by others.

This private key will be ignored.

You've hit a very common and important security feature when dealing with SSH keys on Windows (and Linux/macOS too)! The error messages Bad permissions. and WARNING: UNPROTECTED PRIVATE KEY FILE! are telling you that your private key file (ikramsshkey) has permissions that are too broad, meaning other users (or even certain system accounts) on your computer could potentially read it.

SSH clients are designed to be extremely strict about private key permissions to prevent unauthorized access to your remote systems. If anyone else can read your private key, they could potentially impersonate you.

The key phrase here is: "It is required that your private key files are NOT accessible by others."

The Fix: Restricting Permissions on Your Private Key File

You need to use Windows' file permissions (NTFS permissions) to restrict access to only your user account.

Here's how to do it step-by-step:

    Navigate to the .ssh directory:

        Open File Explorer.

        Go to C:\Users\stg\.ssh\

    Right-click on your private key file:

        Right-click on ikramsshkey (the file itself, not the folder).

        Select "Properties."

    Go to the Security Tab:

        In the ikramsshkey Properties window, click on the "Security" tab.

    Edit Permissions:

        Click the "Edit..." button to change permissions.

    Remove Unwanted Users/Groups:

        In the "Permissions for ikramsshkey" window, you'll see a list of "Group or user names."

        Crucially, you need to ensure that only your specific user account (STG-LAPTOP-01\stg or just stg) and potentially "SYSTEM" have "Read" and "Full control" permissions.

        Select any entries that are NOT your user account (e.g., "Users", "Authenticated Users", "Everyone", or the problematic STG-LAPTOP-01\mis that was specifically mentioned) and click the "Remove" button.

        Do NOT remove "SYSTEM" or your own user account.

        If you see STG-LAPTOP-01\mis (S-1-5-21-318855882-392476681-3897922682-1010) specifically, remove that one.

    Ensure Your User has Full Control:

        Select your user account (stg or STG-LAPTOP-01\stg).

        In the "Permissions for stg" box below, ensure "Full control" is checked under "Allow." (Read is sufficient for the key, but Full Control won't hurt if it's just you).

    Disable Inheritance (Important!):

        Click the "Advanced" button (on the "Security" tab).

        In the "Advanced Security Settings for ikramsshkey" window, click "Disable inheritance."

        When prompted, choose "Convert inherited permissions into explicit permissions on this object." This will make the permissions on this file independent of the parent folder.

    Clean Up Explicit Permissions (After Disabling Inheritance):

        Now, with inheritance disabled, you might see a cleaner list.

        Remove any users/groups again that are NOT SYSTEM and your specific user account (stg or STG-LAPTOP-01\stg).

        Click "Apply" and then "OK" on all open windows.

Example of Correct Permissions:

After you're done, if you check the "Security" tab again, you should typically see only two entries under "Group or user names":

    SYSTEM

    STG-LAPTOP-01\stg (or just stg)

Both of these should have "Full control" or at least "Read" permissions. No other users or groups should be listed.

Try ssh-add again:

Once you've set the permissions correctly, go back to your Git Bash or command prompt and try the ssh-add command again:
Bash

ssh-add C:\Users\stg\.ssh\ikramsshkey

This time, it should add the key without the permission warnings. If it asks for a passphrase, enter the passphrase you set when you generated the key.

This step is critical for SSH security, and it's good that you encountered it early!

Now wish to go forward with this project which is realistic. like db server ,webserver should work realistic.

Excellent! Moving towards a more realistic project is a fantastic idea. As an infrastructure person, this is where you start to bridge the gap between "code" and "operations." We'll focus on Infrastructure as Code (IaC).

For a realistic web server and database server project on a Windows PC, the most practical and industry-relevant approach would be to use Docker and Docker Compose. This allows you to define and run these services in isolated containers, mimicking real-world deployments without needing to set up full virtual machines.

Here's a breakdown of the new project, incorporating Docker, Docker Compose, and a more robust CI/CD pipeline.

Realistic Infrastructure Project: Web Application Stack with Docker Compose

Goal:

    Define a web server (Nginx) and a database server (PostgreSQL) using Docker Compose.

    Include a simple web application (e.g., a Python Flask app) that connects to the database.

    Use Git and GitHub for version control.

    Implement CI/CD with GitHub Actions to:

        Lint code (Python, YAML).

        Build Docker images.

        (Optional, but advanced) Run basic tests.

Prerequisites:

    Git for Windows: Already installed.

    VS Code: Already installed.

    Docker Desktop for Windows: This is essential. Download and install it from https://www.docker.com/products/docker-desktop/. Ensure WSL 2 (Windows Subsystem for Linux 2) integration is enabled in Docker Desktop settings for best performance.

Project Structure (New realistic-infra-project)

realistic-infra-project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml             # GitHub Actions workflow
├── app/
│   ├── app.py                    # Simple Flask application
│   └── requirements.txt          # Python dependencies
├── nginx/
│   └── nginx.conf                # Nginx configuration
├── docker-compose.yml            # Defines the services (web, db, app)
├── .gitignore                    # Files/folders to ignore from Git
└── README.md                     # Project description

Step 1: Project Setup and Initial Files

    Create a New Project Directory:

        Open Git Bash (or PowerShell/CMD with Git installed).

        cd D:\MyRepo (or your preferred location)

        mkdir realistic-infra-project

        cd realistic-infra-project

        git init

        code . (to open in VS Code)

    Create .gitignore:

        Create a file named .gitignore at the root of your project.

        Add the following content:

        # Python
        *.pyc
        __pycache__/
        .venv/
        venv/

        # Docker
        .dockerignore
        *.log
        tmp/

        # IDE
        .vscode/
        .idea/

        # Secrets (if you ever add any)
        .env

        Commit: Stage .gitignore and commit: git commit -m "Add .gitignore file"

    Create docker-compose.yml:

        Create a file named docker-compose.yml at the root.

        This file will define our services:
        YAML

    version: '3.8' # Use a recent Docker Compose file format

    services:
      # Our simple Flask web application
      web_app:
        build: ./app # Build Docker image from the 'app' directory
        container_name: flask_app
        restart: always
        environment:
          # Environment variables for the Flask app to connect to the DB
          DATABASE_URL: postgresql://user:password@db:5432/mydatabase
        depends_on:
          - db # Ensure database starts before the app
        networks:
          - app_network

      # Nginx reverse proxy / web server
      nginx:
        image: nginx:latest # Use the official Nginx image
        container_name: nginx_proxy
        ports:
          - "80:80" # Map host port 80 to container port 80
        volumes:
          - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro # Mount Nginx config
        depends_on:
          - web_app # Nginx depends on the web_app being available
        networks:
          - app_network

      # PostgreSQL database server
      db:
        image: postgres:13 # Use a specific version of PostgreSQL
        container_name: postgres_db
        restart: always
        environment:
          POSTGRES_DB: mydatabase
          POSTGRES_USER: user
          POSTGRES_PASSWORD: password
        volumes:
          - db_data:/var/lib/postgresql/data # Persistent data volume
        networks:
          - app_network

    volumes:
      db_data: # Define the named volume for database persistence

    networks:
      app_network: # Define a custom network for inter-service communication
        driver: bridge

Create app/ directory and files:

    Create a folder named app at the root.

    Inside app, create Dockerfile:
    Dockerfile

# Use a slim Python image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]

Inside app, create requirements.txt:

Flask
psycopg2-binary # For PostgreSQL connection

Inside app, create app.py:
Python

    from flask import Flask
    import os
    import psycopg2

    app = Flask(__name__)

    # Get database connection string from environment variable
    DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost:5432/mydatabase')

    def get_db_connection():
        conn = psycopg2.connect(DATABASE_URL)
        return conn

    @app.route('/')
    def hello():
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('SELECT 1;') # Simple query to test DB connection
            db_status = "Database connection successful!"
            cur.close()
            conn.close()
        except Exception as e:
            db_status = f"Database connection failed: {e}"

        return f"<h1>Hello from Flask App!</h1><p>{db_status}</p>"

    @app.route('/health')
    def health_check():
        return "OK", 200

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)

Create nginx/ directory and nginx.conf:

    Create a folder named nginx at the root.

    Inside nginx, create nginx.conf:
    Nginx

    events {
        worker_connections 1024;
    }

    http {
        include       mime.types;
        default_type  application/octet-stream;

        sendfile        on;
        keepalive_timeout  65;

        server {
            listen 80; # Nginx listens on port 80

            location / {
                # Proxy requests to the Flask web_app service (defined in docker-compose.yml)
                proxy_pass http://web_app:5000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }

            location /health {
                # Direct access to the health check endpoint
                proxy_pass http://web_app:5000/health;
            }
        }
    }

Update README.md:

    Provide instructions for setting up and running the project.

Markdown

# Realistic Infrastructure Project: Web App Stack with Docker Compose

This project demonstrates a simple web application stack including:
- Nginx (as a reverse proxy)
- A Python Flask web application
- PostgreSQL database

All services are containerized using Docker and orchestrated with Docker Compose.
CI/CD is implemented using GitHub Actions for linting and Docker image building.

## Project Structure

.
├── .github/              # GitHub Actions workflows
│   └── workflows/
│       └── ci-cd.yml     # CI/CD pipeline for linting and Docker builds
├── app/                  # Python Flask application source code
│   ├── Dockerfile        # Dockerfile for the Flask app
│   ├── app.py            # Main Flask application file
│   └── requirements.txt  # Python dependencies for the Flask app
├── nginx/                # Nginx configuration
│   └── nginx.conf        # Nginx configuration file
├── docker-compose.yml    # Docker Compose definition for the entire stack
├── .gitignore            # Git ignore file
└── README.md             # This README file


## Prerequisites

- [Git](https://git-scm.com/downloads)
- [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/) (ensure WSL 2 integration is enabled)
- [VS Code](https://code.visualstudio.com/) (recommended IDE)

## How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/realistic-infra-project.git](https://github.com/YOUR_GITHUB_USERNAME/realistic-infra-project.git)
    cd realistic-infra-project
    ```
2.  **Start Docker Desktop:** Ensure Docker Desktop is running on your Windows machine.
3.  **Build and Run the Stack:**
    Open Git Bash or your preferred terminal in the `realistic-infra-project` directory and run:
    ```bash
    docker compose up --build -d
    ```
    * `docker compose up`: Starts the services defined in `docker-compose.yml`.
    * `--build`: Forces Docker to rebuild images (especially for `web_app`) before starting.
    * `-d`: Runs the containers in "detached" mode (in the background).
4.  **Verify Services:**
    * Open your web browser and go to `http://localhost/`. You should see "Hello from Flask App! Database connection successful!"
    * You can also check the health endpoint at `http://localhost/health`.
5.  **View Logs (Optional):**
    To see logs from all services:
    ```bash
    docker compose logs -f
    ```
    To see logs from a specific service (e.g., `web_app`):
    ```bash
    docker compose logs -f web_app
    ```
6.  **Stop and Clean Up:**
    When you're done, stop and remove the containers, networks, and volumes:
    ```bash
    docker compose down -v
    ```
    * `-v`: Removes named volumes (`db_data` in our case), which is useful for starting fresh.

## CI/CD with GitHub Actions

The `.github/workflows/ci-cd.yml` file defines a GitHub Actions workflow that automatically runs checks and builds Docker images:

-   **On `push` to `main` branch or `pull_request` to `main`:**
    -   **Lint Python code:** Uses `flake8`.
    -   **Lint YAML files:** Uses `yamllint`.
    -   **Build Docker images:** Builds the `web_app` image defined in `app/Dockerfile`.

This ensures that your infrastructure code and application code are continuously validated and that Docker images can be built successfully upon changes.

---