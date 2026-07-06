"""Exploration 1: trace state by hand.

Read trace() below. WITHOUT running it, follow the state (x, y) through
each loop iteration on paper, then fill in the three PREDICT_ values.

Then run this file (python3 ex01_tracing.py) to see the truth, and
finally record your calibration with: uni grade 101/explore-01
"""

PREDICT_FINAL_X = 32
PREDICT_FINAL_Y = 25
PREDICT_ITERATIONS = 5


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

"""
x: 1
y: 10
i: 0

x: 2
y: 13
i: 1

x: 4
y: 16
i: 2

x: 8
y: 19
i: 3

x: 16
y: 22
i: 4

x: 32
y: 25
i: 5
"""