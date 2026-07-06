"""Assignment a1: implement these five classic algorithms.

The test suite (tests/test_algorithms.py) is the specification.
Run it with: uni grade 101/a1
"""


def gcd(a, b):
    """Return the greatest common divisor of non-negative a and b.

    Use Euclid's algorithm. By convention gcd(n, 0) == n and gcd(0, 0) == 0.
    """
    raise NotImplementedError


def is_prime(n):
    """Return True if n is prime, False otherwise (including all n < 2)."""
    raise NotImplementedError


def collatz_length(n):
    """Return how many Collatz steps positive integer n takes to reach 1.

    One step: even n becomes n // 2, odd n becomes 3n + 1.
    collatz_length(1) == 0.
    """
    raise NotImplementedError


def linear_search(items, target):
    """Return the index of the first occurrence of target, or -1 if absent."""
    raise NotImplementedError


def binary_search(items, target):
    """Return an index of target in the SORTED list items, or -1 if absent.

    Must run in O(log n): repeatedly halve the search interval. A linear
    scan will fail the probe test.
    """
    raise NotImplementedError
