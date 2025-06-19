import os
import sys
import subprocess

# Define the deployment script
def deploy():
    # Install dependencies
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    # Run the application
    subprocess.run(["python", "main.py"])

if __name__ == "__main__":
    deploy()
