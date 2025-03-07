#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
from pathlib import Path

import pandas as pd

REGEX = r"Time for running the recipe was: (?P<runtime>[0-9]+:[0-9]{2}:[0-9]{2}\.[0-9]+)\n"


def main(path: Path | str):
    path = Path(path).expanduser()

    print()
    for recipe_dir in sorted(path.glob("*")):
        print(recipe_dir.name)

        log_file = recipe_dir / "run" / "main_log.txt"
        if not log_file.is_file():
            print("    -> No log file found")
            print()
            continue

        log_str = log_file.read_text()
        match = re.search(REGEX, log_str)
        if match is None:
            print("    -> Recipe did not finish")
            print()
            continue

        runtime = pd.Timedelta(match.group("runtime")).round("s")
        print(f"    -> Runtime: {runtime} ({runtime.seconds}s)")
        print()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError("No result path given")
    main(sys.argv[1])
