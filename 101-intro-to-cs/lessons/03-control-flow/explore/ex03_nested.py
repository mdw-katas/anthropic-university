"""Exploration: how many times does a nested loop body run?

count_pairs visits each UNORDERED pair (i < j) once; count_grid visits
every ordered combination. Predict both for n = 5, run, then:
uni grade 101/explore-03

(Hint for pairs: 4 + 3 + 2 + 1 + 0. This is Lesson 8 foreshadowed.)
"""

PREDICT_PAIRS_FOR_5 = None
PREDICT_GRID_FOR_5 = None


def count_pairs(n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count


def count_grid(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


if __name__ == "__main__":
    print(f"count_pairs(5) = {count_pairs(5)}")
    print(f"count_grid(5)  = {count_grid(5)}")
