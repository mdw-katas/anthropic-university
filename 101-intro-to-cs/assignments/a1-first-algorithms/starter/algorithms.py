"""Assignment a1: implement these five classic algorithms.

The test suite (tests/test_algorithms.py) is the specification.
Run it with: uni grade 101/a1
"""

import math


def gcd(a, b):
    """Return the greatest common divisor of non-negative a and b.

    Use Euclid's algorithm. By convention gcd(n, 0) == n and gcd(0, 0) == 0.
    """
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    """Return True if n is prime, False otherwise (including all n < 2)."""
    if n < 2:
        return False
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True


def collatz_length(n):
    """Return how many Collatz steps positive integer n takes to reach 1.

    One step: even n becomes n // 2, odd n becomes 3n + 1.
    collatz_length(1) == 0.
    """
    steps = 0
    while n != 1:
        steps += 1
        if n % 2:
            n = (3 * n) + 1
        else:
            n = n // 2
    return steps


def linear_search(items, target):
    """Return the index of the first occurrence of target, or -1 if absent."""
    for n, v in enumerate(items):
        if v == target:
            return n
    return -1


def binary_search(items, target):
    """Return an index of target in the SORTED list items, or -1 if absent.

    Must run in O(log n): repeatedly halve the search interval. A linear
    scan will fail the probe test.
    """
    lo, hi = 0, len(items)-1
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        item = items[mid]
        if item == target:
            return mid
        if target < item:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
