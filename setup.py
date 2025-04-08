from setuptools import setup, find_packages

setup(
    name="pr",  # this is the command you'll run globally
    version="0.1",
    packages=find_packages(),  # includes your `utils` package
    py_modules=["pr_tool"],  # your main script (cli.py)
    install_requires=[],
    entry_points={
        "console_scripts": [
            "prtool=pr_tool:main",  # 'command-name=filename:function'
        ],
    },
)
