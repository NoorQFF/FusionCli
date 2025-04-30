import os
import subprocess
from utils._utils import runSystemFittedProcess, throwError

def getCurrentGitBranchName():
    return runSystemFittedProcess('git rev-parse --abbrev-ref HEAD')

def getLastBranchedOffBranchName():
    return runSystemFittedProcess('git reflog | grep "checkout: moving from" | grep -m1 "$(git rev-parse --abbrev-ref HEAD)" | sed -E \'s/.*moving from ([^ ]+) to.*/\1/\'')

def getLatestCommitMessage() -> str:
    try:
        full_message = runSystemFittedProcess('git log -1 --pretty=%B').strip()
        return full_message.split('\n')[0]  # Get only the first line
    except subprocess.CalledProcessError:
        throwError("Failed to fetch the latest commit message. Ensure you're in a Git repository.")