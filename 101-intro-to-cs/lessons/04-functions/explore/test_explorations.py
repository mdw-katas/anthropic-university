"""Self-checks for the Lesson 4 explorations: uni grade 101/explore-04"""
import unittest

import ex01_shadowing
import ex02_returns


class TestShadowing(unittest.TestCase):
    def test_shadow_return(self):
        self.assertEqual(ex01_shadowing.PREDICT_SHADOW_RETURN, ex01_shadowing.shadow())

    def test_module_x_untouched(self):
        ex01_shadowing.shadow()
        self.assertEqual(ex01_shadowing.PREDICT_MODULE_X_AFTER, ex01_shadowing.x)


class TestReturns(unittest.TestCase):
    def test_silent_none(self):
        self.assertNotEqual(ex02_returns.PREDICT_ADD_RESULT, "FILL_ME",
                            "replace FILL_ME with your prediction")
        self.assertEqual(ex02_returns.PREDICT_ADD_RESULT, ex02_returns.add(2, 3))

    def test_keyword_binding(self):
        self.assertNotEqual(ex02_returns.PREDICT_KWARGS, "FILL_ME",
                            "replace FILL_ME with your prediction")
        self.assertEqual(ex02_returns.PREDICT_KWARGS,
                         ex02_returns.power(exponent=3, base=2))


if __name__ == "__main__":
    unittest.main()
