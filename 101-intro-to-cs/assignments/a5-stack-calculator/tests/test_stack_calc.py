"""The executable specification for assignment a5."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import stack_calc


class TestStack(unittest.TestCase):
    def test_lifo_order(self):
        stack = stack_calc.Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_peek_does_not_remove(self):
        stack = stack_calc.Stack()
        stack.push("top")
        self.assertEqual(stack.peek(), "top")
        self.assertEqual(stack.size(), 1)

    def test_is_empty_and_size(self):
        stack = stack_calc.Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
        stack.push(7)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 1)

    def test_empty_pop_and_peek_raise(self):
        stack = stack_calc.Stack()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()


class TestTokenize(unittest.TestCase):
    def test_splits_on_whitespace(self):
        self.assertEqual(stack_calc.tokenize("3 4 +"), ["3", "4", "+"])
        self.assertEqual(stack_calc.tokenize("  1   2  "), ["1", "2"])

    def test_empty(self):
        self.assertEqual(stack_calc.tokenize(""), [])


class TestEvaluateRPN(unittest.TestCase):
    def evaluate(self, expression):
        return stack_calc.evaluate_rpn(stack_calc.tokenize(expression))

    def test_single_operations(self):
        self.assertAlmostEqual(self.evaluate("3 4 +"), 7)
        self.assertAlmostEqual(self.evaluate("3 4 -"), -1)
        self.assertAlmostEqual(self.evaluate("3 4 *"), 12)
        self.assertAlmostEqual(self.evaluate("8 4 /"), 2)

    def test_operand_order_for_subtraction_and_division(self):
        self.assertAlmostEqual(self.evaluate("10 2 -"), 8)
        self.assertAlmostEqual(self.evaluate("10 2 /"), 5)

    def test_composite_expressions(self):
        # (3 + 4) * 2
        self.assertAlmostEqual(self.evaluate("3 4 + 2 *"), 14)
        # 5 - (6 / 3)
        self.assertAlmostEqual(self.evaluate("5 6 3 / -"), 3)

    def test_single_operand(self):
        self.assertAlmostEqual(self.evaluate("42"), 42)

    def test_negative_and_fractional(self):
        self.assertAlmostEqual(self.evaluate("-3 1.5 *"), -4.5)

    def test_malformed_raises(self):
        with self.assertRaises(ValueError):
            self.evaluate("+")
        with self.assertRaises(ValueError):
            self.evaluate("1 +")
        with self.assertRaises(ValueError):
            self.evaluate("1 2 3 +")  # leftover operand
        with self.assertRaises(ValueError):
            self.evaluate("")


class TestBalanced(unittest.TestCase):
    def test_balanced_examples(self):
        self.assertTrue(stack_calc.balanced(""))
        self.assertTrue(stack_calc.balanced("()"))
        self.assertTrue(stack_calc.balanced("f(x[i]) { return }"))
        self.assertTrue(stack_calc.balanced("([{}])"))

    def test_unbalanced_examples(self):
        self.assertFalse(stack_calc.balanced("("))
        self.assertFalse(stack_calc.balanced(")("))
        self.assertFalse(stack_calc.balanced("([)]"))
        self.assertFalse(stack_calc.balanced("{[}"))


if __name__ == "__main__":
    unittest.main()
