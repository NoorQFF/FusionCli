import os

from utils._utils import runSystemFittedProcess


def runTests():
    if os.path.exists('angular.json'):
        runSystemFittedProcess('ng test', silent=False)
    elif os.path.exists('pubspec.yaml'):
        runSystemFittedProcess('flutter test', silent=False)
    else:
        pass