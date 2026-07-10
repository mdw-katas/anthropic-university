"""Exploration: an iterator is a stream with no rewind.

The same data, summed twice — once as a list, once as an iterator. Then
a membership test that quietly eats part of the stream. Predict all four.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-08
"""

PREDICT_LIST_SECOND_SUM = None  # second sum() of the LIST
PREDICT_ITER_SECOND_SUM = None  # second sum() of the ITERATOR
PREDICT_MEMBERSHIP = None       # 3 in iter([1, 2, 3, 4])
PREDICT_REMAINDER = None        # list(...) of that same iterator afterward


def list_summed_twice():
    data = [1, 2, 3, 4]
    return sum(data), sum(data)


def iterator_summed_twice():
    data = iter([1, 2, 3, 4])
    return sum(data), sum(data)


def membership_then_remainder():
    stream = iter([1, 2, 3, 4])
    found = 3 in stream
    return found, list(stream)


if __name__ == "__main__":
    print(f"list twice:     {list_summed_twice()}")
    print(f"iterator twice: {iterator_summed_twice()}")
    found, rest = membership_then_remainder()
    print(f"3 in stream -> {found}, remainder -> {rest}")
    # The membership test consumed everything up to and including the 3.
