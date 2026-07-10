"""Exploration: a weak postcondition lets the implementation cheat.

cheating_sort returns something genuinely sorted — and quietly drops
duplicates. Which clauses of the honest sorting contract does it satisfy
for SAMPLE?

Fill the PREDICT_* constants (True/False), run this file, then:
uni grade 102/explore-01
"""

PREDICT_SORTED_CLAUSE = None       # is_sorted(cheating_sort(SAMPLE))
PREDICT_PERMUTATION_CLAUSE = None  # is_permutation(SAMPLE, cheating_sort(SAMPLE))

SAMPLE = [3, 1, 3, 2]


def cheating_sort(items):
    """Passes 'output is sorted'. Fails the clause everyone forgets."""
    return sorted(set(items))


def is_sorted(items):
    return all(a <= b for a, b in zip(items, items[1:]))


def is_permutation(original, candidate):
    return sorted(original) == sorted(candidate)


if __name__ == "__main__":
    result = cheating_sort(SAMPLE)
    print(f"cheating_sort({SAMPLE}) = {result}")
    print(f"is_sorted      -> {is_sorted(result)}")
    print(f"is_permutation -> {is_permutation(SAMPLE, result)}")
