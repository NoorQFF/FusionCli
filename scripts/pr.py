from utils._utils import SEPARATOR, getBasePathName, runSystemFittedProcess, throwError
from utils.aws_utils import createPullRequestCommand
from utils.cli_utils import CustomShell
from utils.git_utils import getCurrentGitBranchName, getLatestCommitMessage
from utils.repo_utils import runTests

def start_aws_pr(args):
    print("PR Tool running...")
    # runTests()

    # Get the current branch name and latest commit message
    current_branch = getCurrentGitBranchName()
    latest_commit_message = getLatestCommitMessage().split("\n")[0]
    base_path = getBasePathName()
    default_title = f"{current_branch.upper()}: {latest_commit_message}"

    if args.default:
        target = "development"
        repository = base_path
        title = default_title
        desc = ""

    else:
        with CustomShell() as cs:
            target = cs.customInput("Where is your destination?", "development")
            repository = cs.customInput("What is the name of the repository?", base_path)
            title = cs.customInput("What is your PR named?", default_title)
            desc = cs.customInput("What is the description of your PR (optional)?", "")

    repository = repository.replace(" ", SEPARATOR)
    target = target.replace(" ", SEPARATOR)
    title = title.replace(" ", SEPARATOR)
    desc = desc.replace(" ", SEPARATOR)

    runSystemFittedProcess(createPullRequestCommand(current_branch, target, repository, title, desc), silent=False)