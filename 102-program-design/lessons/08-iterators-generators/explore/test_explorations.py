"""Self-checks for the Lesson 8 explorations: uni grade 102/explore-08"""
import unittest

import ex01_one_shot
import ex02_pull_order
import ex03_deferred_validation


class TestOneShot(unittest.TestCase):
    def test_list_is_reiterable(self):
        _, second = ex01_one_shot.list_summed_twice()
        self.assertEqual(ex01_one_shot.PREDICT_LIST_SECOND_SUM, second)

    def test_iterator_is_one_shot(self):
        _, second = ex01_one_shot.iterator_summed_twice()
        self.assertEqual(ex01_one_shot.PREDICT_ITER_SECOND_SUM, second)

    def test_membership_consumes(self):
        found, remainder = ex01_one_shot.membership_then_remainder()
        self.assertEqual(ex01_one_shot.PREDICT_MEMBERSHIP, found)
        self.assertEqual(ex01_one_shot.PREDICT_REMAINDER, remainder)


class TestPullOrder(unittest.TestCase):
    def test_trail_alternates(self):
        self.assertEqual(ex02_pull_order.PREDICT_TRAIL, ex02_pull_order.scenario())

    def test_unpulled_values_never_produced(self):
        trail = ex02_pull_order.scenario()
        produced = len([c for c in trail if c.startswith("produce")])
        self.assertEqual(ex02_pull_order.PREDICT_PRODUCED_COUNT, produced)


class TestDeferredValidation(unittest.TestCase):
    def test_calling_raises_nothing(self):
        self.assertEqual(ex03_deferred_validation.PREDICT_AT_CALL,
                         ex03_deferred_validation.failure_at_call())

    def test_first_next_detonates(self):
        self.assertEqual(ex03_deferred_validation.PREDICT_AT_NEXT,
                         ex03_deferred_validation.failure_at_next())


if __name__ == "__main__":
    unittest.main()
