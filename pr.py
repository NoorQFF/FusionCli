#!/usr/bin/env python3
import sys

import os
import subprocess

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

def runTests():
    if os.path.exists('angular.json'):
        print("Running 'ng test'...")
        runSystemFittedProcess('ng test')
    elif os.path.exists('pubspec.yaml'):
        print("Running 'flutter test'...")
        runSystemFittedProcess('flutter test')
    else:
        pass

def isOperatingSystemWindows() -> bool:
    return os.name == 'nt'

def getSystemFittedPath(path: str) -> str:
    if isOperatingSystemWindows():
        return path.replace('/', '\\')
    else:
        return path

def runSystemFittedProcess(cmd: str):
    isWin = isOperatingSystemWindows()
    result = subprocess.run([" ".join(x.split(separator)) for x in cmd.split(' ')], shell=isWin, check=True, capture_output=True, text=True)
    return result.stdout.strip()

def throwError(error: str):
    print(f"\033[31m\n!ERROR\n{error}\n\033[0m")
    exit(-1)

def createPullRequestCommand(destinationBranch: str, title: str, desc: str = '') -> str:
    if destinationBranch == None or destinationBranch == '':
        throwError('No Destination branch chosen')    
    if title == None or title == '':
        throwError('No title given to PR')

    prCmd = f'aws codecommit create-pull-request --title "{title}" --description "{desc}" '
    prCmd += f'--targets repositoryName={getBasePathName()},sourceReference={getCurrentGitBranchName()},destinationReference={destinationBranch}'
    return prCmd


if __name__ == "__main__":
    separator = "|||_|||"
    if len(sys.argv) != 2:
        throwError('Incorrect Usage.\nTry: python3 pr.py target')

    target = sys.argv[1]

    runTests()

    # Get the current branch name and latest commit message
    current_branch = getCurrentGitBranchName()
    latest_commit_message = getLatestCommitMessage().split("\n")[0]

    title = input(f"Enter the title of the PR [{current_branch}: {latest_commit_message}]: ").strip()
    if not title:  # Use the default if no input is provided
        title = f"{current_branch}: {latest_commit_message}"
    title = title.replace(" ", separator)

    # Prompt for the description
    desc = input("Enter the description of the PR (optional): ").strip()
    desc = desc.replace(" ", separator)


    runSystemFittedProcess(createPullRequestCommand(target, title, desc))
