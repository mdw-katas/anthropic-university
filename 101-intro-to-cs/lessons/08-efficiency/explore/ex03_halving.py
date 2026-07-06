"""Exploration: the power of halving.

Binary search on a MILLION sorted items, hunting a target that is not
there (the worst case): how many probes before the window is empty?
Hint: how many times can you halve 1,000,000 before reaching 0?
Predict, run, then: uni grade 101/explore-08
"""

PREDICT_PROBES = None  # worst-case probes for n = 1,000,000


def worst_case_probes(n):
    probes = 0
    low, high = 0, n - 1
    while low <= high:
        probes += 1
        middle = (low + high) // 2
        low = middle + 1  # simulate always searching the upper half
    return probes


if __name__ == "__main__":
    print(f"worst_case_probes(1_000_000) = {worst_case_probes(1_000_000)}")
