"""Exploration: parameters alias their arguments.

Predict the state of BOTH module-level lists after main() runs.
Run this file to check, then: uni grade 101/explore-06
"""

PREDICT_SHARED_AFTER = None  # e.g. [1, 2, 3] — the list passed directly
PREDICT_COPIED_AFTER = None  # the list passed as a copy


def sneaky(items):
    items.append(99)
    return len(items)


def main():
    shared = [1, 2, 3]
    copied = [1, 2, 3]
    sneaky(shared)
    sneaky(copied.copy())
    return shared, copied


if __name__ == "__main__":
    shared, copied = main()
    print(f"passed directly:  {shared}")
    print(f"passed as copy:   {copied}")
