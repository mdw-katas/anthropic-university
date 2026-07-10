"""Exploration: assert is a development-time contract check, not validation.

First: what type does a failing assert raise? Second — the important one —
this script re-runs a failing assert under `python -O`. Does the program
crash, or sail straight past the "impossible" condition?

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-01
"""

import subprocess
import sys

PREDICT_ASSERT_TYPE = None       # type NAME raised by a failing assert
PREDICT_SURVIVES_DASH_O = None   # True/False: does `python -O` exit cleanly?


def assert_failure_name():
    """Return the type name raised by a failing assert."""
    try:
        assert 1 == 2, "arithmetic still works, thankfully"
    except Exception as caught:
        return type(caught).__name__
    return "no exception"


def survives_dash_o():
    """Run `python -O -c "assert False; ..."` and report a clean exit."""
    completed = subprocess.run(
        [sys.executable, "-O", "-c", "assert False, 'never checked'; print('fine')"],
        capture_output=True, text=True)
    return completed.returncode == 0


if __name__ == "__main__":
    print(f"failing assert raises: {assert_failure_name()}")
    print(f"under -O, the same program survives: {survives_dash_o()}")
    print("moral: assert documents contracts; it must never guard real input")
