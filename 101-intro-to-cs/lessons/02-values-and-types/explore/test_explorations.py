"""Self-checks for the Lesson 2 explorations: uni grade 101/explore-02"""
import unittest

import ex01_numbers
import ex02_strings
import ex03_rebinding


class TestNumbers(unittest.TestCase):
    def test_floor_division(self):
        self.assertEqual(ex01_numbers.PREDICT_FLOOR_DIV, -7 // 2)

    def test_modulo(self):
        self.assertEqual(ex01_numbers.PREDICT_MOD, -7 % 2)

    def test_float_equality(self):
        self.assertEqual(ex01_numbers.PREDICT_FLOAT_EQUAL, 0.1 + 0.2 == 0.3)


class TestStrings(unittest.TestCase):
    def test_slice(self):
        self.assertEqual(ex02_strings.PREDICT_SLICE, ex02_strings.WORD[2:6])

    def test_prefix(self):
        self.assertEqual(ex02_strings.PREDICT_PREFIX, ex02_strings.WORD[:3])

    def test_suffix(self):
        self.assertEqual(ex02_strings.PREDICT_SUFFIX, ex02_strings.WORD[-4:])

    def test_immutability(self):
        word = ex02_strings.WORD
        word.upper()
        self.assertEqual(ex02_strings.PREDICT_AFTER_UPPER, word)


class TestRebinding(unittest.TestCase):
    def test_string_rebinding(self):
        _, y = ex03_rebinding.rebind()
        self.assertEqual(ex03_rebinding.PREDICT_Y, y)

    def test_int_rebinding(self):
        _, b = ex03_rebinding.arithmetic()
        self.assertEqual(ex03_rebinding.PREDICT_B, b)


if __name__ == "__main__":
    unittest.main()
