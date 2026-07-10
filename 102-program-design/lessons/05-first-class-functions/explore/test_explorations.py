"""Self-checks for the Lesson 5 explorations: uni grade 102/explore-05"""
import unittest

import ex01_late_binding
import ex02_counter_state
import ex03_key_functions


class TestLateBinding(unittest.TestCase):
    def test_late_bound_lambdas(self):
        self.assertEqual(ex01_late_binding.PREDICT_LATE_BOUND,
                         ex01_late_binding.make_late_bound())

    def test_frozen_lambdas(self):
        self.assertEqual(ex01_late_binding.PREDICT_FROZEN,
                         ex01_late_binding.make_frozen())


class TestCounterState(unittest.TestCase):
    def test_interleaved_counters(self):
        self.assertEqual(ex02_counter_state.PREDICT_SEQUENCE,
                         ex02_counter_state.interleaved())


class TestKeyFunctions(unittest.TestCase):
    def test_default_sort(self):
        module = ex03_key_functions
        self.assertEqual(module.PREDICT_DEFAULT, sorted(module.WORDS))

    def test_casefolded_sort(self):
        module = ex03_key_functions
        self.assertEqual(module.PREDICT_CASEFOLDED,
                         sorted(module.WORDS, key=str.lower))

    def test_length_sort(self):
        module = ex03_key_functions
        self.assertEqual(module.PREDICT_BY_LENGTH,
                         sorted(module.WORDS, key=len))


if __name__ == "__main__":
    unittest.main()
