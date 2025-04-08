import os
import subprocess


SEPARATOR = "|||_|||"

def getBasePathName():
    cwd = os.getcwd()  # Get the current working directory
    dir_name = os.path.basename(cwd)  # Extract the name of the directory
    return dir_name

def isOperatingSystemWindows() -> bool:
    return os.name == 'nt'

def getSystemFittedPath(path: str) -> str:
    if isOperatingSystemWindows():
        return path.replace('/', '\\')
    else:
        return path

def runSystemFittedProcess(cmd: str):
    isWin = isOperatingSystemWindows()
    cmd_parts = [" ".join(x.split(SEPARATOR)) for x in cmd.split(' ')]
    print(f"executing: \033[90m{cmd_parts}\033[0m")
    try:
        result = subprocess.run(
            cmd_parts,
            shell=isWin,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        throwError(f"Command: `\033[90m{" ".join(e.cmd)}\033[31m`\nfailed with exit code {e.returncode}\n{e.stderr}")
    except FileNotFoundError:
        throwError("Command not found. Please ensure the command or executable exists.")
    except OSError as e:
        throwError(f"OS error occurred: {e}")

def throwError(error: str):
    print(f"\033[31m\n!ERROR\n{error}\n\033[0m")
    exit(-1)