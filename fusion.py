#!/usr/bin/env python3
import argparse

from scripts.pr import start_aws_pr

def main():
    parser = argparse.ArgumentParser(description="A Fusion Family cli tool")
    subparsers = parser.add_subparsers(dest='command', required=True)

    pr_tool_parser = subparsers.add_parser("pr", help="Make an AWS Codecommit Pull Request in the current git repo")
    pr_tool_parser.add_argument("-d", "--default", action="store_true", help="Make a pr for the current git repo with default values")

    args = parser.parse_args()
    print(f"Parsed arguments: {args}")

    if args.command == "pr":
        start_aws_pr(args)

if __name__ == "__main__":
    main()
