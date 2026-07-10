"""Assignment a3: the higher-order classics, from bare closures.

The tests reject imports of functools/itertools and calls to the builtins
map/filter/reduce. Loops and closures only.
"""

_MISSING = object()  # sentinel: "no initial value was supplied"


def my_map(fn, iterable):
    """Return a list of fn(x) for each element, preserving order."""
    raise NotImplementedError


def my_filter(predicate, iterable):
    """Return a list of the elements for which predicate(x) is truthy."""
    raise NotImplementedError


def my_reduce(fn, iterable, initial=_MISSING):
    """Fold left. my_reduce(add, [1, 2, 3], 10) == fn(fn(fn(10, 1), 2), 3).

    Empty + no initial -> TypeError. Empty + initial -> initial.
    One element + no initial -> that element, fn never called.
    """
    raise NotImplementedError


def compose(*functions):
    """compose(f, g, h)(x) == f(g(h(x))). compose()(x) == x."""
    raise NotImplementedError


def memoize(fn):
    """Wrap fn to cache results by positional-argument tuple.

    Each memoized function keeps its own private cache (closure state).
    """
    raise NotImplementedError


def once(fn):
    """Wrap fn to run at most once; later calls replay the first result."""
    raise NotImplementedError
