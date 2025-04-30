import os
import subprocess
from utils._utils import SEPARATOR, runSystemFittedProcess, throwError

def getCurrentGitBranchName():
    return runSystemFittedProcess('git rev-parse --abbrev-ref HEAD')

def getLastBranchedOffBranchName():
    return runSystemFittedProcess(f'git reflog | grep "checkout:{SEPARATOR}moving{SEPARATOR}from" | grep -m1 "$(git{SEPARATOR}rev-parse{SEPARATOR}--abbrev-ref{SEPARATOR}HEAD)" | sed -E \'s/.*moving from ([^ ]+) to.*/\1/\'')

def getLatestCommitMessage() -> str:
    try:
        full_message = runSystemFittedProcess('git log -1 --pretty=%B').strip()
        return full_message.split('\n')[0]  # Get only the first line
    except subprocess.CalledProcessError:
        throwError("Failed to fetch the latest commit message. Ensure you're in a Git repository.")