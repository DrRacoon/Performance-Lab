#!/bin/python3.12
"""
Finds the path of a circle array.
"""

from argparse import ArgumentParser, Namespace
from itertools import batched, cycle, islice


def parse_args() -> Namespace:
    parser = ArgumentParser(description=__doc__)

    parser.add_argument("n", type=int, help="array length")
    parser.add_argument("m", type=int, help="interval length")

    return parser.parse_args()


def main(n: int, m: int) -> None:
    it = cycle(range(1, n + 1))
    first_batch = tuple(islice(it, m))
    first, last = first_batch[0], first_batch[-1]
    print(first, end="")

    for interval in batched(it, m-1):
        interval = (last, *interval)
        print(interval[0], end="")
        last = interval[-1]
        if last == first:
            break


if __name__ == "__main__":
    ns = parse_args()
    main(ns.n, ns.m)
