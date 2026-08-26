#!/usr/bin/env python3
"""
CLI tool entry point
Project ID: 5c47cc
"""

import argparse
import sys
import os
from pathlib import Path


def cmd_run_5c47cc(args):
    """Execute run subcommand"""
    print(f"Running task: {args.task}")
    print(f"Output dir: {args.output}")
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)
    result_file = output_path / f"result_5c47cc.txt"
    result_file.write_text(f"Task: {args.task}\nID: 5c47cc\n")
    print(f"Result written to {result_file}")


def cmd_status_5c47cc(args):
    """Execute status subcommand"""
    print(f"Status check for: {args.name}")
    print(f"Instance ID: 5c47cc")
    print("Status: OK")


def build_parser_5c47cc() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tool-5c47cc",
        description="A command-line utility tool",
    )
    subparsers = parser.add_subparsers(dest="command")

    run_p = subparsers.add_parser("run", help="Execute a task")
    run_p.add_argument("task", help="Task name to execute")
    run_p.add_argument("-o", "--output", default="./output", help="Output directory")
    run_p.set_defaults(func=cmd_run_5c47cc)

    status_p = subparsers.add_parser("status", help="Check status")
    status_p.add_argument("name", nargs="?", default="default", help="Instance name")
    status_p.set_defaults(func=cmd_status_5c47cc)

    return parser


def main():
    parser = build_parser_5c47cc()
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)
    args.func(args)


if __name__ == "__main__":
    main()
