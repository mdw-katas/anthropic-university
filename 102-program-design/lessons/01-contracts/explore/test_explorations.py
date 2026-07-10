"""Self-checks for the Lesson 1 explorations: uni grade 102/explore-01"""
import unittest

import ex01_whose_bug
import ex02_weak_postconditions
import ex03_asserts


class TestWhoseBug(unittest.TestCase):
    def test_unchecked_precondition_returns_garbage(self):
        self.assertEqual(ex01_whose_bug.PREDICT_UNCHECKED,
                         ex01_whose_bug.isqrt_unchecked(-4))

    def test_checked_precondition_fails_loudly(self):
        self.assertEqual(ex01_whose_bug.PREDICT_CHECKED_EXCEPTION,
                         ex01_whose_bug.checked_failure_name())


class TestWeakPostconditions(unittest.TestCase):
    def test_sorted_clause(self):
        module = ex02_weak_postconditions
        self.assertEqual(module.PREDICT_SORTED_CLAUSE,
                         module.is_sorted(module.cheating_sort(module.SAMPLE)))

    def test_permutation_clause(self):
        module = ex02_weak_postconditions
        self.assertEqual(module.PREDICT_PERMUTATION_CLAUSE,
                         module.is_permutation(module.SAMPLE,
                                               module.cheating_sort(module.SAMPLE)))


class TestAsserts(unittest.TestCase):
    def test_assert_failure_type(self):
        self.assertEqual(ex03_asserts.PREDICT_ASSERT_TYPE,
                         ex03_asserts.assert_failure_name())

    def test_dash_o_strips_asserts(self):
        self.assertEqual(ex03_asserts.PREDICT_SURVIVES_DASH_O,
                         ex03_asserts.survives_dash_o())


if __name__ == "__main__":
    unittest.main()
