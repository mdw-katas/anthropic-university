"""Self-checks for the Lesson 8 explorations: uni grade 101/explore-08"""
import unittest

import ex01_pairs
import ex02_membership
import ex03_halving


class TestPairs(unittest.TestCase):
    def test_steps_for_100(self):
        self.assertEqual(ex01_pairs.PREDICT_STEPS_FOR_100, ex01_pairs.count_pairs(100))


class TestMembership(unittest.TestCase):
    def test_comparisons(self):
        _, comparisons = ex02_membership.counted_membership(list(range(1000)), 999)
        self.assertEqual(ex02_membership.PREDICT_COMPARISONS, comparisons)


class TestHalving(unittest.TestCase):
    def test_probes(self):
        self.assertEqual(ex03_halving.PREDICT_PROBES,
                         ex03_halving.worst_case_probes(1_000_000))


if __name__ == "__main__":
    unittest.main()
