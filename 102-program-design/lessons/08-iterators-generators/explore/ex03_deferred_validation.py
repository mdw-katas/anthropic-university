"""Exploration: a generator's body does not run at call time — including
its validation.

read_evens rejects a negative limit... eventually. Predict WHERE the
ValueError surfaces: at the call, or at the first next()?

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-08
"""

PREDICT_AT_CALL = None   # type NAME raised BY THE CALL read_evens(-1), or "no exception"
PREDICT_AT_NEXT = None   # type NAME raised by next() on it, or "no exception"


def read_evens(limit):
    """Yield even numbers up to limit. Requires limit >= 0 (checked... late)."""
    if limit < 0:
        raise ValueError("limit must be non-negative")
    for n in range(0, limit + 1, 2):
        yield n


def failure_at_call():
    try:
        read_evens(-1)
        return "no exception"
    except Exception as caught:
        return type(caught).__name__


def failure_at_next():
    generator = read_evens(-1)
    try:
        next(generator)
        return "no exception"
    except Exception as caught:
        return type(caught).__name__


if __name__ == "__main__":
    print(f"read_evens(-1) itself:  {failure_at_call()}")
    print(f"first next() on it:     {failure_at_next()}")
    # To fail fast, validate in a plain function that RETURNS a generator.
