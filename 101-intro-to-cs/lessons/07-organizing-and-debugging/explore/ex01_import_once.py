"""Exploration: importing runs a module's top-level code — how many times?

This file imports tally twice; the test file imports it yet again.
All in one process. Predict how many entries tally.RUNS holds by the
time anyone looks. Run this file, then: uni grade 101/explore-07
"""

import tally
import tally  # noqa: F811 — deliberately imported again

PREDICT_RUN_COUNT = None  # len(tally.RUNS)


if __name__ == "__main__":
    print(f"len(tally.RUNS) = {len(tally.RUNS)}")
