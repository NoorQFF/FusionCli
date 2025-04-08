import json
import subprocess

from utils.git_utils import getCurrentGitBranchName
from utils._utils import getBasePathName, throwError

def getCurrentAwsUser():
    try:
        result = subprocess.run(['aws', 'sts', 'get-caller-identity'], capture_output=True, text=True, check=True)
        response = json.loads(result.stdout)
        return response['Arn'].split(":")[-1]

    except:
        return None

def createPullRequestCommand(destinationBranch: str, repositoryName: str, title: str, desc: str = '') -> str:
    if destinationBranch == None or destinationBranch == '':
        throwError('No Destination branch chosen')    
    if title == None or title == '':
        throwError('No title given to PR')

    prCmd = f"aws codecommit create-pull-request --title {title} --description {desc} "
    prCmd += f'--targets repositoryName={repositoryName},sourceReference={getCurrentGitBranchName()},destinationReference={destinationBranch} --debug'
    return prCmd