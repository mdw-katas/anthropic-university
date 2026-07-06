"""Exploration: recursion depth — how many frames are live at the peak?

factorial(5) calls factorial(4) calls ... calls factorial(0). Count the
factorial frames alive at the deepest moment. Predict, run, then:
uni grade 101/explore-05
"""

PREDICT_MAX_DEPTH = None  # deepest simultaneous factorial frames, n=5


def factorial_max_depth(n):
    deepest = 0

    def factorial(k, depth):
        nonlocal deepest
        deepest = max(deepest, depth)
        if k == 0:
            return 1
        return k * factorial(k - 1, depth + 1)

    factorial(n, 1)
    return deepest


if __name__ == "__main__":
    print(f"factorial(5) reaches depth {factorial_max_depth(5)}")
