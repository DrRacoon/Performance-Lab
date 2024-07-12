#!/bin/python3.12
"""
Are points in the circle?
"""

from argparse import ArgumentParser, Namespace
from math import hypot
from numbers import Real
from pathlib import Path
from typing import Iterable, NamedTuple


def parse_args() -> Namespace:
    parser = ArgumentParser(description=__doc__)

    parser.add_argument(
        "CIRCLE_FILE",
        type=Path,
        help="path to a file with circle coordinates and radius",
    )
    parser.add_argument(
        "POINTS_FILE", type=Path, help="path to a file with coordinates of points"
    )

    return parser.parse_args()


class Point(NamedTuple):
    x: Real
    y: Real


def read_circle_desc(path: Path) -> tuple[Point, Real]:
    with path.open() as file:
        centre = Point(*map(float, file.readline().strip().split()))
        r = float(file.readline().strip())
    return centre, r


def read_points(path: Path) -> tuple[Point, ...]:
    return tuple(
        Point(*map(float, line.split()))
        for line in path.read_text().strip().splitlines()
    )


def main(circle_centre: Point, r: Real, points: Iterable[Point]) -> None:
    for point in points:
        distance = hypot(circle_centre.x - point.x, circle_centre.y - point.y)
        if distance > r:
            print(2)
        elif distance == r:
            print(0)
        else:
            print(1)


if __name__ == "__main__":
    ns = parse_args()
    circle_centre, r = read_circle_desc(ns.CIRCLE_FILE)
    points = read_points(ns.POINTS_FILE)
    main(circle_centre, r, points)
