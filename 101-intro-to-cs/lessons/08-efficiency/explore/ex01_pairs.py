"""Exploration: count the hidden work in a nested loop.

The all-pairs loop from Lesson 3, now at n = 100. The body runs
99 + 98 + ... + 1 + 0 times. (Gauss found the shortcut as a schoolboy:
n(n-1)/2.) Predict, run, then: uni grade 101/explore-08
"""

PREDICT_STEPS_FOR_100 = None


def count_pairs(n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count


if __name__ == "__main__":
    print(f"count_pairs(100) = {count_pairs(100)}")
