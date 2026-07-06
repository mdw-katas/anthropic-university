"""Self-checks for the Lesson 3 explorations: uni grade 101/explore-03"""
import unittest

import ex01_ranges
import ex02_for_else
import ex03_nested


class TestRanges(unittest.TestCase):
    def test_stepped(self):
        self.assertEqual(ex01_ranges.PREDICT_STEPPED, list(range(2, 11, 3)))

    def test_last(self):
        self.assertEqual(ex01_ranges.PREDICT_LAST, list(range(5))[-1])

    def test_count(self):
        self.assertEqual(ex01_ranges.PREDICT_COUNT, len(range(10, 100, 10)))


class TestForElse(unittest.TestCase):
    def test_present(self):
        self.assertEqual(ex02_for_else.PREDICT_PRESENT, ex02_for_else.classify([4, 7, 9], 7))

    def test_absent(self):
        self.assertEqual(ex02_for_else.PREDICT_ABSENT, ex02_for_else.classify([4, 7, 9], 5))

    def test_empty(self):
        self.assertEqual(ex02_for_else.PREDICT_EMPTY, ex02_for_else.classify([], 5))


class TestNested(unittest.TestCase):
    def test_pairs(self):
        self.assertEqual(ex03_nested.PREDICT_PAIRS_FOR_5, ex03_nested.count_pairs(5))

    def test_grid(self):
        self.assertEqual(ex03_nested.PREDICT_GRID_FOR_5, ex03_nested.count_grid(5))


if __name__ == "__main__":
    unittest.main()
