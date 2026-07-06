"""Self-checks for the Lesson 5 explorations: uni grade 101/explore-05"""
import unittest

import ex01_call_count
import ex02_depth
import ex03_reverse


class TestCallCount(unittest.TestCase):
    def test_value(self):
        value, _ = ex01_call_count.fib_counting(5)
        self.assertEqual(ex01_call_count.PREDICT_VALUE_FOR_5, value)

    def test_calls(self):
        _, calls = ex01_call_count.fib_counting(5)
        self.assertEqual(ex01_call_count.PREDICT_CALLS_FOR_5, calls)


class TestDepth(unittest.TestCase):
    def test_max_depth(self):
        self.assertEqual(ex02_depth.PREDICT_MAX_DEPTH,
                         ex02_depth.factorial_max_depth(5))


class TestReverse(unittest.TestCase):
    def test_reversed(self):
        self.assertEqual(ex03_reverse.PREDICT_REVERSED,
                         ex03_reverse.reverse("stack"))


if __name__ == "__main__":
    unittest.main()
