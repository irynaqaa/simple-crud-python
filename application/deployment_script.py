import os
import sys
import subprocess

# Define the deployment strategy
def deploy():
    # Deploy the system on Windows
    if sys.platform == "win32":
        # Use the subprocess module to run the deployment command
        subprocess.run(["powershell", "deploy_windows.ps1"])
    # Deploy the system on Linux
    elif sys.platform == "linux":
        # Use the subprocess module to run the deployment command
        subprocess.run(["bash", "deploy_linux.sh"])
    # Deploy the system on macOS
    elif sys.platform == "darwin":
        # Use the subprocess module to run the deployment command
        subprocess.run(["bash", "deploy_macos.sh"])
    else:
        print("Unsupported platform")
        sys.exit(1)

# Call the deploy function
if __name__ == "__main__":
    deploy()