"""Exploration: an unchecked precondition does not fail loudly — it lies.

isqrt_unchecked documents "requires n >= 0" but never checks it. Predict
what it returns for -4 (not what it SHOULD return — what it DOES return).
Then predict which exception type the checked version raises.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-01
"""

PREDICT_UNCHECKED = None           # isqrt_unchecked(-4)
PREDICT_CHECKED_EXCEPTION = None   # exception type NAME, e.g. "TypeError"


def isqrt_unchecked(n):
    """Integer square root. Precondition (unchecked!): n >= 0."""
    root = 0
    while (root + 1) * (root + 1) <= n:
        root += 1
    return root


def isqrt_checked(n):
    """Integer square root, with the precondition enforced at the door."""
    if n < 0:
        raise ValueError(f"isqrt requires n >= 0, got {n}")
    return isqrt_unchecked(n)


def checked_failure_name():
    """Return the type name of whatever isqrt_checked(-4) raises."""
    try:
        isqrt_checked(-4)
    except Exception as caught:
        return type(caught).__name__
    return "no exception"


if __name__ == "__main__":
    print(f"isqrt_unchecked(16) = {isqrt_unchecked(16)}")
    print(f"isqrt_unchecked(-4) = {isqrt_unchecked(-4)}   <- garbage, delivered politely")
    print(f"isqrt_checked(-4) raises {checked_failure_name()}")
