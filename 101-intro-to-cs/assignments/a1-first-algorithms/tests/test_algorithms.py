"""The executable specification for assignment a1."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import algorithms


class TestGCD(unittest.TestCase):
    def test_known_pairs(self):
        self.assertEqual(algorithms.gcd(1071, 462), 21)
        self.assertEqual(algorithms.gcd(48, 18), 6)
        self.assertEqual(algorithms.gcd(17, 5), 1)

    def test_zero_conventions(self):
        self.assertEqual(algorithms.gcd(7, 0), 7)
        self.assertEqual(algorithms.gcd(0, 7), 7)
        self.assertEqual(algorithms.gcd(0, 0), 0)

    def test_equal_arguments(self):
        self.assertEqual(algorithms.gcd(12, 12), 12)


class TestIsPrime(unittest.TestCase):
    def test_small_primes(self):
        for n in (2, 3, 5, 7, 11, 13, 97):
            self.assertTrue(algorithms.is_prime(n), f"{n} is prime")

    def test_small_composites(self):
        for n in (4, 6, 9, 15, 91, 100):
            self.assertFalse(algorithms.is_prime(n), f"{n} is composite")

    def test_below_two(self):
        for n in (1, 0, -1, -7):
            self.assertFalse(algorithms.is_prime(n), f"{n} is not prime")

    def test_larger_prime(self):
        self.assertTrue(algorithms.is_prime(7919))


class TestCollatzLength(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(algorithms.collatz_length(1), 0)

    def test_known_lengths(self):
        self.assertEqual(algorithms.collatz_length(2), 1)
        self.assertEqual(algorithms.collatz_length(6), 8)
        self.assertEqual(algorithms.collatz_length(27), 111)


class TestLinearSearch(unittest.TestCase):
    def test_finds_first_occurrence(self):
        self.assertEqual(algorithms.linear_search([5, 3, 5, 1], 5), 0)
        self.assertEqual(algorithms.linear_search([5, 3, 5, 1], 1), 3)

    def test_absent_and_empty(self):
        self.assertEqual(algorithms.linear_search([1, 2, 3], 9), -1)
        self.assertEqual(algorithms.linear_search([], 9), -1)


class ProbeList(list):
    """A list that counts element accesses, to catch linear scans."""

    def __init__(self, iterable):
        super().__init__(iterable)
        self.accesses = 0

    def __getitem__(self, index):
        self.accesses += 1
        return super().__getitem__(index)

    def __iter__(self):
        for index in range(len(self)):
            yield self[index]

    def __contains__(self, value):
        self.accesses += len(self)
        return super().__contains__(value)

    def index(self, *args):
        self.accesses += len(self)
        return super().index(*args)


class TestBinarySearch(unittest.TestCase):
    def test_finds_present_targets(self):
        items = [1, 3, 5, 7, 9, 11]
        for index, value in enumerate(items):
            self.assertEqual(algorithms.binary_search(items, value), index)

    def test_absent_and_empty(self):
        self.assertEqual(algorithms.binary_search([1, 3, 5], 4), -1)
        self.assertEqual(algorithms.binary_search([1, 3, 5], 0), -1)
        self.assertEqual(algorithms.binary_search([1, 3, 5], 6), -1)
        self.assertEqual(algorithms.binary_search([], 1), -1)

    def test_single_element(self):
        self.assertEqual(algorithms.binary_search([5], 5), 0)
        self.assertEqual(algorithms.binary_search([5], 4), -1)

    def test_actually_binary(self):
        items = ProbeList(range(0, 20000, 2))  # 10,000 sorted even numbers
        self.assertEqual(algorithms.binary_search(items, 19998), 9999)
        self.assertLessEqual(
            items.accesses, 60,
            "too many element accesses: that looks like a linear scan, "
            "not binary search",
        )


if __name__ == "__main__":
    unittest.main()
