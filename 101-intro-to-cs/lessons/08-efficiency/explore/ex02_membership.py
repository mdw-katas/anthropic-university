"""Exploration: `in` on a list is a loop in disguise.

Searching a 1000-item list for its LAST element compares against every
element on the way. Predict the comparison count, run, then:
uni grade 101/explore-08
"""

PREDICT_COMPARISONS = None  # comparisons to find 999 in list(range(1000))


def counted_membership(items, target):
    comparisons = 0
    for item in items:
        comparisons += 1
        if item == target:
            return True, comparisons
    return False, comparisons


if __name__ == "__main__":
    found, comparisons = counted_membership(list(range(1000)), 999)
    print(f"found={found} after {comparisons} comparisons")
    print("(a set would have answered in ~1 — same `in` syntax, different machine)")
