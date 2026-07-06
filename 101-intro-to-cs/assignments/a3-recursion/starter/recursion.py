"""Assignment a3: recursion only — the tests reject loops and comprehensions."""


def sum_digits(n):
    """Return the sum of the decimal digits of non-negative n.

    sum_digits(942) == 15. Hint: n % 10 is the last digit.
    """
    raise NotImplementedError


def power(base, exp):
    """Return base ** exp for exp >= 0, recursing on exp // 2.

    Fast exponentiation: even exp -> square the base, halve the exponent.
    The tests check power(2, 1000) without letting you recurse 1000 deep.
    """
    raise NotImplementedError


def flatten(nested):
    """Return a flat list of all non-list elements, depth-first.

    flatten([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]
    """
    raise NotImplementedError


def pascal_row(n):
    """Return row n of Pascal's triangle (row 0 == [1]).

    Each row is built from the previous: neighbors summed, 1s at the ends.
    """
    raise NotImplementedError


def hanoi(n, source, spare, target):
    """Return the list of (from_peg, to_peg) moves carrying n disks
    from source to target using spare. hanoi(0, ...) == [].
    """
    raise NotImplementedError
