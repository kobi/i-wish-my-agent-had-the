#!/usr/bin/env python3
"""Pad one string to a requested width."""

import argparse
import sys


def pad(value: str, width: int, fill: str) -> str:
    """Return value padded to width without truncating it."""
    if len(fill) != 1:
        raise ValueError("fill must be exactly one character")
    if width <= len(value):
        return value

    amount = width - len(value)
    return fill * amount + value


def main() -> int:
    parser = argparse.ArgumentParser(description="Pad a string to a fixed width")
    parser.add_argument("value", help="string to pad")
    parser.add_argument("width", type=int, help="target string width")
    parser.add_argument("--fill", default=" ", help="one-character fill (default: space)")
    args = parser.parse_args()

    try:
        result = pad(args.value, args.width, args.fill)
    except ValueError as error:
        parser.error(str(error))
    sys.stdout.write(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
