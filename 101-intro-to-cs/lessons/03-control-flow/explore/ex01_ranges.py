"""Exploration: range is half-open — includes start, excludes stop.

Predict, run, then: uni grade 101/explore-03
"""

PREDICT_STEPPED = [2, 5, 8]  # list(range(2, 11, 3))
PREDICT_LAST    = 4          # list(range(5))[-1]
PREDICT_COUNT   = 9          # len(range(10, 100, 10))


if __name__ == "__main__":
    print(f"list(range(2, 11, 3))    = {list(range(2, 11, 3))}")
    print(f"list(range(5))[-1]       = {list(range(5))[-1]}")
    print(f"len(range(10, 100, 10))  = {len(range(10, 100, 10))}")
