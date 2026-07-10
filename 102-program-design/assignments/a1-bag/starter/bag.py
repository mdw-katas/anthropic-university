"""Assignment a1: a Bag (multiset) ADT.

Rep invariant: no element is stored with a count <= 0.
The tests reject any import of the collections module — build on dict.
"""


class Bag:
    """An unordered collection whose elements may repeat.

    Bag(["a", "b", "a"]) holds two "a" and one "b".
    """

    def __init__(self, iterable=()):
        """Snapshot the iterable's elements (defensive: later mutation of
        the argument must not affect this bag)."""
        raise NotImplementedError

    def add(self, item, count=1):
        """Add count copies of item. ValueError if count < 1."""
        raise NotImplementedError

    def remove(self, item, count=1):
        """Remove count copies of item.

        ValueError if count < 1, or if the bag holds fewer than count
        copies of item — in which case the bag must be left unchanged.
        Removing the last copy removes the element entirely (rep invariant).
        """
        raise NotImplementedError

    def count(self, item):
        """How many copies of item this bag holds (0 if absent)."""
        raise NotImplementedError

    def distinct(self):
        """Sorted list of distinct elements — a fresh list every call."""
        raise NotImplementedError

    def most_common(self, k):
        """First k (item, count) pairs: count descending, ties by item
        ascending. k == 0 gives []; oversized k gives all pairs."""
        raise NotImplementedError

    def __len__(self):
        """Total number of elements, counting multiplicity."""
        raise NotImplementedError

    def __contains__(self, item):
        """True iff at least one copy of item is present."""
        raise NotImplementedError

    def __eq__(self, other):
        """Value equality against another Bag; NotImplemented otherwise.

        Do NOT define __hash__ — bags are mutable.
        """
        raise NotImplementedError
