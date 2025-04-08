import os
import subprocess
from utils._utils import runSystemFittedProcess, throwError

def getBasePathName():
    cwd = os.getcwd()  # Get the current working directory
    dir_name = os.path.basename(cwd)  # Extract the name of the directory
    return dir_name

def getCurrentGitBranchName():
    return runSystemFittedProcess('git rev-parse --abbrev-ref HEAD')

def getLatestCommitMessage() -> str:
    try:
        full_message = runSystemFittedProcess('git log -1 --pretty=%B').strip()
        return full_message.split('\n')[0]  # Get only the first line
    except subprocess.CalledProcessError:
        throwError("Failed to fetch the latest commit message. Ensure you're in a Git repository.")