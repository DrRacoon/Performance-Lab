"""
Fills a report out
"""

from argparse import ArgumentParser, Namespace
from pathlib import Path
from statistics import median


def parse_args() -> Namespace:
    parser = ArgumentParser(description=__doc__)

    parser.add_argument("FILE", type=Path, help="path to a file with an array")

    return parser.parse_args()


def main(path: Path) -> None:
    nums = tuple(map(int, path.read_text().strip().split()))
    m = int(median(nums))
    print(sum(abs(n - m) for n in nums))


if __name__ == "__main__":
    ns = parse_args()
    main(ns.FILE)
