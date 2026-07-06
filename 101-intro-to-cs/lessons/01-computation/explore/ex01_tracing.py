"""Exploration 1: trace state by hand.

Read trace() below. WITHOUT running it, follow the state (x, y) through
each loop iteration on paper, then fill in the three PREDICT_ values.

Then run this file (python3 ex01_tracing.py) to see the truth, and
finally record your calibration with: uni grade 101/explore-01
"""

PREDICT_FINAL_X = None
PREDICT_FINAL_Y = None
PREDICT_ITERATIONS = None


def trace():
    x, y = 1, 10
    iterations = 0
    while x < y:
        x = x * 2
        y = y + 3
        iterations += 1
    return x, y, iterations


if __name__ == "__main__":
    x, y, iterations = trace()
    print(f"final x = {x}")
    print(f"final y = {y}")
    print(f"iterations = {iterations}")
