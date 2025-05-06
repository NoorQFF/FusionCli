import os
import subprocess
from utils._utils import SEPARATOR, runSystemFittedProcess, throwError

def getCurrentGitBranchName():
    return runSystemFittedProcess('git rev-parse --abbrev-ref HEAD')
    
def getLastBranchedOffBranchName():
    """
    Get the last branch the current branch was branched off from.
    Defaults to 'development' if no branch is found.
    """
    current_branch = getCurrentGitBranchName()
    # Step 1: Get the reflog
    reflog_output = runSystemFittedProcess('git reflog')
    
    # Step 2: Filter for 'checkout: moving from'
    filtered_reflog = [
        line for line in reflog_output.splitlines() 
        if 'checkout: moving from' in line and current_branch in line
    ]
    
    # Step 3: Extract the branch name
    if filtered_reflog:
        last_entry = filtered_reflog[0]
        from_branch = last_entry.split('moving from ')[1].split(' to')[0]
        return from_branch
    else:
        return 'development'

def getLatestCommitMessage() -> str:
    try:
        full_message = runSystemFittedProcess('git log -1 --pretty=%B').strip()
        return full_message.split('\n')[0]  # Get only the first line
    except subprocess.CalledProcessError:
        throwError("Failed to fetch the latest commit message. Ensure you're in a Git repository.")