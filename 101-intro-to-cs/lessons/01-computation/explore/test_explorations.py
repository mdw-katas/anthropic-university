"""Self-checks for the Lesson 1 explorations.

Run via: uni grade 101/explore-01
Each test fails until you fill in the PREDICT_ values in the ex*.py
files — and fails honestly if your prediction disagrees with reality.
"""
import unittest

import ex01_tracing
import ex02_euclid
import ex03_collatz


class TestTracingPredictions(unittest.TestCase):
    def test_predictions_are_filled_in(self):
        self.assertIsNotNone(ex01_tracing.PREDICT_FINAL_X, "fill in PREDICT_FINAL_X before grading")
        self.assertIsNotNone(ex01_tracing.PREDICT_FINAL_Y, "fill in PREDICT_FINAL_Y before grading")
        self.assertIsNotNone(ex01_tracing.PREDICT_ITERATIONS, "fill in PREDICT_ITERATIONS before grading")

    def test_final_x(self):
        x, _, _ = ex01_tracing.trace()
        self.assertEqual(ex01_tracing.PREDICT_FINAL_X, x)

    def test_final_y(self):
        _, y, _ = ex01_tracing.trace()
        self.assertEqual(ex01_tracing.PREDICT_FINAL_Y, y)

    def test_iterations(self):
        _, _, iterations = ex01_tracing.trace()
        self.assertEqual(ex01_tracing.PREDICT_ITERATIONS, iterations)


class TestEuclidPredictions(unittest.TestCase):
    def test_gcd_value(self):
        value, _ = ex02_euclid.gcd_with_steps(1071, 462)
        self.assertEqual(ex02_euclid.PREDICT_GCD, value)

    def test_step_count(self):
        _, steps = ex02_euclid.gcd_with_steps(1071, 462)
        self.assertEqual(ex02_euclid.PREDICT_STEPS, steps)


class TestCollatzPredictions(unittest.TestCase):
    def test_steps_for_6(self):
        self.assertEqual(ex03_collatz.PREDICT_STEPS_FOR_6, ex03_collatz.collatz_steps(6))

    def test_champion_under_10(self):
        self.assertEqual(ex03_collatz.PREDICT_CHAMPION_UNDER_10, ex03_collatz.champion(10))


if __name__ == "__main__":
    unittest.main()
