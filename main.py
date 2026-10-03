"""Wanderstop Desktop — A local helper for Wanderstop tea-shop folders, garden notes, and forest photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='wanderstop_desktop',
        description='A local helper for Wanderstop tea-shop folders, garden notes, and forest photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Wanderstop Desktop')
    print('Keep the tea shop on disk before a story chapter.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
