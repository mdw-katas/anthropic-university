"""Exploration: no return statement means the function returns None.

Because None is this exploration set's "not filled in yet" sentinel,
use the string "FILL_ME" as the placeholder here and replace it with
your actual prediction (which may legitimately be None!).

Predict, run, then: uni grade 101/explore-04
"""

PREDICT_ADD_RESULT = None  # add(2, 3)
PREDICT_KWARGS = 8         # power(exponent=3, base=2)


def add(a, b):
    total = a + b   # oops: the author forgot something


def power(base, exponent):
    return base ** exponent


if __name__ == "__main__":
    print(f"add(2, 3) = {add(2, 3)!r}")
    print(f"power(exponent=3, base=2) = {power(exponent=3, base=2)}")
