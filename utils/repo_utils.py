import os

from utils._utils import runSystemFittedProcess


def runTests():
    if os.path.exists('angular.json'):
        print("Running 'ng test'...")
        runSystemFittedProcess('ng test')
    elif os.path.exists('pubspec.yaml'):
        print("Running 'flutter test'...")
        runSystemFittedProcess('flutter test')
    else:
        pass