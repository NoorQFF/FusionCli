# Fusion CLI Tool 
A cli tool with the following features:

## Features:
- `pr`: CodeCommit PR Tool; used to create pull requests to AWS Codecommit for a given repository

## Table of Contents
- [Setup](#setup)
- [Installation](#installation)
    - [Prerequisites](#prerequisites)

## Setup and Installation
Make sure you have aws configurations set for the correct account and role. You can either download the release for your OS or you can build it yourself.

#### Prerequisites
- install python
- pip install setuptools
- (optional) pip install pyinstaller
  - This can be used to build an executable

To setup fusion cli with setup tools you need to clone the repo, install the prerequsites, and run:
```bash
pip install -e .
```

To create an executable (that you will have to manually add to path) run:
```bash
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --onefile fusion.py 
```

You should now be able to run `fusion`.