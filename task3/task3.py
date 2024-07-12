"""
Fills a report out
"""

import json
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Literal
from warnings import warn


type Test = dict[str, str | list[Test]]


def parse_args() -> Namespace:
    parser = ArgumentParser(description=__doc__)

    parser.add_argument(
        "VALUES_FILE",
        type=Path,
        help="path to a JSON file with test results by id",
    )
    parser.add_argument(
        "TESTS_FILE", type=Path, help="path to a JSON file with a report template"
    )
    parser.add_argument(
        "REPORT_FILE", type=Path, help="path to a JSON file to write a report"
    )

    return parser.parse_args()


def add_values(
    tests: list[Test], results: dict[int, Literal["passed", "failed"]]
) -> None:
    for test in tests:
        id = test["id"]
        if id in results:
            test["value"] = results[id]
        else:
            warn(f"No result of test {id}")
        if "values" in test:
            add_values(test["values"], results)


def main(result_path: Path, template_path: Path, to: Path) -> None:
    report = json.loads(template_path.read_text())
    results = {
        i["id"]: i["value"] for i in json.loads(result_path.read_text())["values"]
    }

    add_values(report["tests"], results)
    to.write_text(json.dumps(report))


if __name__ == "__main__":
    ns = parse_args()
    main(ns.VALUES_FILE, ns.TESTS_FILE, ns.REPORT_FILE)
