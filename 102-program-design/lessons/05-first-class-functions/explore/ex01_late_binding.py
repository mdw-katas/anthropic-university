"""Exploration: closures capture variables, not values.

Both factories build three zero-argument functions in a loop. Predict
the list each produces when all three are called afterward.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-05
"""

PREDICT_LATE_BOUND = None  # results from make_late_bound(), e.g. [0, 1, 2]
PREDICT_FROZEN = None      # results from make_frozen()


def make_late_bound():
    """The classic: every lambda closes over the SAME variable i."""
    callbacks = []
    for i in range(3):
        callbacks.append(lambda: i)
    return [call() for call in callbacks]


def make_frozen():
    """The standard fix: default arguments evaluate at definition time."""
    callbacks = []
    for i in range(3):
        callbacks.append(lambda i=i: i)
    return [call() for call in callbacks]


if __name__ == "__main__":
    print(f"late-bound: {make_late_bound()}")
    print(f"frozen:     {make_frozen()}")
