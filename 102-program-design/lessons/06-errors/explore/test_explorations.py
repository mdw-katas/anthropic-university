"""Self-checks for the Lesson 6 explorations: uni grade 102/explore-06"""
import unittest

import ex01_except_order
import ex02_finally_always
import ex03_chaining


class TestExceptOrder(unittest.TestCase):
    def test_base_class_first_swallows(self):
        self.assertEqual(ex01_except_order.PREDICT_BASE_FIRST,
                         ex01_except_order.classify_base_first("oops"))

    def test_precise_clause_first(self):
        self.assertEqual(ex01_except_order.PREDICT_PRECISE_FIRST,
                         ex01_except_order.classify_precise_first("oops"))

    def test_base_clause_catches_subclass(self):
        self.assertEqual(ex01_except_order.PREDICT_BASE_CATCHES_SUB,
                         ex01_except_order.lookup_demo())


class TestFinallyAlways(unittest.TestCase):
    def test_finally_runs_on_return(self):
        self.assertEqual(ex02_finally_always.PREDICT_RETURN_TRAIL,
                         ex02_finally_always.return_scenario())

    def test_finally_runs_on_exception(self):
        self.assertEqual(ex02_finally_always.PREDICT_EXCEPTION_TRAIL,
                         ex02_finally_always.exception_scenario())

    def test_exception_still_propagates(self):
        module = ex02_finally_always
        self.assertEqual(module.PREDICT_EXCEPTION_ESCAPED,
                         "escaped" in module.exception_scenario())


class TestChaining(unittest.TestCase):
    def test_caught_and_cause(self):
        caught, cause = ex03_chaining.caught_and_cause()
        self.assertEqual(ex03_chaining.PREDICT_CAUGHT_TYPE, caught)
        self.assertEqual(ex03_chaining.PREDICT_CAUSE_TYPE, cause)


if __name__ == "__main__":
    unittest.main()
