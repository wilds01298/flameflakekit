#!/usr/bin/env python3
"""
CLI helpers and formatters
ID: 5c47cc
"""

import sys
import os
from typing import Any, Dict, List


COLORS_5c47cc = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "reset": "\033[0m",
}


def colored_5c47cc(text: str, color: str) -> str:
    if not sys.stdout.isatty():
        return text
    c = COLORS_5c47cc.get(color, "")
    return f"{c}{text}{COLORS_5c47cc['reset']}"


def print_table_5c47cc(headers: List[str], rows: List[List[Any]]) -> None:
    """Print data as ASCII table"""
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    sep = "+-" + "-+-".join("-" * w for w in widths) + "-+"
    header_row = "| " + " | ".join(h.ljust(w) for h, w in zip(headers, widths)) + " |"
    print(sep)
    print(header_row)
    print(sep)
    for row in rows:
        print("| " + " | ".join(str(c).ljust(w) for c, w in zip(row, widths)) + " |")
    print(sep)


def confirm_5c47cc(prompt: str, default: bool = False) -> bool:
    hint = "[Y/n]" if default else "[y/N]"
    answer = input(f"{prompt} {hint}: ").strip().lower()
    if not answer:
        return default
    return answer in ("y", "yes")
