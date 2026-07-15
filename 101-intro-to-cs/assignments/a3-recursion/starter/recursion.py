"""Assignment a3: recursion only — the tests reject loops and comprehensions."""


def sum_digits(n):
    """Return the sum of the decimal digits of non-negative n.

    sum_digits(942) == 15. Hint: n % 10 is the last digit.
    """

    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)

def power(base, exp):
    """Return base ** exp for exp >= 0, recursing on exp // 2.

    Fast exponentiation: even exp -> square the base, halve the exponent.
    The tests check power(2, 1000) without letting you recurse 1000 deep.
    """

    if exp == 0:
        return 1
    if exp == 1:
        return base

    squared = power(base * base, exp // 2) # squaring divides the exp in half
    leftover = power(base, exp % 2) # multiply by base for odd exp
    return squared * leftover


def flatten(nested):
    """Return a flat list of all non-list elements, depth-first.

    flatten([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]
    """
    if len(nested) == 0:
        return []
    if not isinstance(nested[0], list):
        return [nested[0]]+flatten(nested[1:])
    return flatten(nested[0])+flatten(nested[1:])


def pascal_row(n):
    """Return row n of Pascal's triangle (row 0 == [1]).

    Each row is built from the previous: neighbors summed, 1s at the ends.
    """

    def sum_pairs(row):
        if len(row) < 2:
            return []
        return [row[0] + row[1]] + sum_pairs(row[1:])

    if n == 0:
        return [1]
    previous = pascal_row(n - 1)
    return [1] + sum_pairs(previous) + [1]


def hanoi(n, source, spare, target):
    """Return the list of (from_peg, to_peg) moves carrying n disks
    from source to target using spare. hanoi(0, ...) == [].
    """
    raise NotImplementedError
