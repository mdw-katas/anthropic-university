"""Exploration: a clock that arrives as a parameter is a clock you control.

elapsed_seconds times a task using WHATEVER clock it is given — the seam.
make_ticking_clock (a closure, from Lesson 5) returns a fake that
advances a fixed step per reading. Predict the measurements.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-07
"""

PREDICT_TICKING_ELAPSED = None  # elapsed_seconds(idle, make_ticking_clock(5))
PREDICT_BUSY_ELAPSED = None     # elapsed via a step-3 clock when work reads it once


def elapsed_seconds(work, clock):
    """Time work() using the injected clock. Reads the clock exactly twice."""
    start = clock()
    work(clock)
    return clock() - start


def make_ticking_clock(step):
    """A fake clock: every reading is `step` later than the last."""
    now = 0

    def clock():
        nonlocal now
        now += step
        return now

    return clock


def idle(clock):
    """Never reads the clock."""


def reads_clock_once(clock):
    """Sneaks one extra reading in the middle of being timed."""
    clock()


if __name__ == "__main__":
    print(f"idle, step-5 clock:       {elapsed_seconds(idle, make_ticking_clock(5))}")
    print(f"one extra read, step-3:   {elapsed_seconds(reads_clock_once, make_ticking_clock(3))}")
    # Every reading advances the fake - count the readings, know the answer.
