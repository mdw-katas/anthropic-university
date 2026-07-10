"""Exploration: a closure is private, persistent state — per creation.

make_counter returns a function that increments and returns its own
count. Predict the printed sequence: two counters, interleaved calls.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-05
"""

PREDICT_SEQUENCE = None  # list from interleaved(), e.g. [1, 2, 3, 4, 5]


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


def interleaved():
    """first, first, second, first, second -> what sequence?"""
    first = make_counter()
    second = make_counter()
    return [first(), first(), second(), first(), second()]


if __name__ == "__main__":
    print(f"interleaved counters: {interleaved()}")
    # Each make_counter() call mints an independent count variable.
