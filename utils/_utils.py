import os
import subprocess
import threading
import time
import sys

SEPARATOR = "|||_|||"

def getBasePathName():
    cwd = os.getcwd()
    dir_name = os.path.basename(cwd)
    return dir_name

def isOperatingSystemWindows() -> bool:
    return os.name == 'nt'

def getSystemFittedPath(path: str) -> str:
    if isOperatingSystemWindows():
        return path.replace('/', '\\')
    else:
        return path

def throwError(error: str):
    print(f"\033[31m\n!ERROR\n{error}\n\033[0m")
    exit(-1)

def runSystemFittedProcess(cmd: str, silent: bool = True):
    isWin = isOperatingSystemWindows()
    cmd_parts = [" ".join(x.split(SEPARATOR)) for x in cmd.split(' ')]
    stop_spinner = False
    spinner_thread = None
    if not silent: 
        print(f"executing: \033[90m{' '.join(cmd_parts)}\033[0m")

        # Spinner logic
        def spinner():
            symbols = ['|', '/', '-', '\\']
            i = 0
            while not stop_spinner:
                sys.stdout.write(f"\r\033[90m⏳ Running... {symbols[i % len(symbols)]}\033[0m")
                sys.stdout.flush()
                time.sleep(0.1)
                i += 1

        spinner_thread = threading.Thread(target=spinner)
        spinner_thread.start()
    
    try:
        result = subprocess.run(
            cmd_parts,
            shell=isWin,
            check=True,
            capture_output=True,
            text=True
        )
        if spinner_thread is not None: 
            stop_spinner = True
            spinner_thread.join()
            sys.stdout.write("\r\033[32m✓ Done.                       \033[0m\n\n")
            sys.stdout.flush()
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        if spinner_thread is not None: 
            stop_spinner = True
            spinner_thread.join()
            sys.stdout.flush()
        throwError(f"Command: `\033[90m{' '.join(e.cmd)}\033[31m`\nfailed with exit code {e.returncode}\n{e.stderr}")
    except FileNotFoundError:
        if spinner_thread is not None: 
            stop_spinner = True
            spinner_thread.join()
            sys.stdout.flush()
        throwError("Command not found. Please ensure the command or executable exists.")
    except OSError as e:
        if spinner_thread is not None: 
            stop_spinner = True
            spinner_thread.join()
            sys.stdout.flush()
        throwError(f"OS error occurred: {e}")