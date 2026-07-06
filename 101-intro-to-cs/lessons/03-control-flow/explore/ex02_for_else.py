"""Exploration: the for/else oddball — else means "no break happened".

Predict what classify returns in each case, run, then:
uni grade 101/explore-03
"""

PREDICT_PRESENT = None   # classify([4, 7, 9], 7)
PREDICT_ABSENT = None    # classify([4, 7, 9], 5)
PREDICT_EMPTY = None     # classify([], 5) — does else run on an empty loop?


def classify(items, target):
    for item in items:
        if item == target:
            result = "found"
            break
    else:
        result = "missing"
    return result


if __name__ == "__main__":
    print(f"classify([4, 7, 9], 7) = {classify([4, 7, 9], 7)!r}")
    print(f"classify([4, 7, 9], 5) = {classify([4, 7, 9], 5)!r}")
    print(f"classify([], 5)        = {classify([], 5)!r}")
