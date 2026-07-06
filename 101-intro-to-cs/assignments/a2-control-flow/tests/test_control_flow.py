"""The executable specification for assignment a2."""
import ast
import inspect
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import control_flow


class TestFizzbuzz(unittest.TestCase):
    def test_classic(self):
        result = control_flow.fizzbuzz(15, [(3, "Fizz"), (5, "Buzz")])
        self.assertEqual(result[0], "1")
        self.assertEqual(result[2], "Fizz")
        self.assertEqual(result[4], "Buzz")
        self.assertEqual(result[14], "FizzBuzz")
        self.assertEqual(len(result), 15)

    def test_rule_order_matters(self):
        result = control_flow.fizzbuzz(6, [(2, "B"), (3, "A")])
        self.assertEqual(result[5], "BA")  # 6 matches both, in rule order

    def test_no_rules(self):
        self.assertEqual(control_flow.fizzbuzz(3, []), ["1", "2", "3"])

    def test_custom_rules(self):
        result = control_flow.fizzbuzz(7, [(7, "Boom")])
        self.assertEqual(result, ["1", "2", "3", "4", "5", "6", "Boom"])


class TestToBinary(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(control_flow.to_binary(0), "0")

    def test_known_values(self):
        self.assertEqual(control_flow.to_binary(1), "1")
        self.assertEqual(control_flow.to_binary(2), "10")
        self.assertEqual(control_flow.to_binary(5), "101")
        self.assertEqual(control_flow.to_binary(255), "11111111")
        self.assertEqual(control_flow.to_binary(1024), "10000000000")

    def test_no_builtin_shortcuts(self):
        source = inspect.getsource(control_flow.to_binary)
        for forbidden in ("bin(", "format(", ":b", "!b"):
            self.assertNotIn(forbidden, source,
                             f"build the binary string yourself (found {forbidden!r})")


class TestIsLeapYear(unittest.TestCase):
    def test_ordinary_years(self):
        self.assertFalse(control_flow.is_leap_year(2023))
        self.assertTrue(control_flow.is_leap_year(2024))

    def test_century_rules(self):
        self.assertFalse(control_flow.is_leap_year(1900))
        self.assertTrue(control_flow.is_leap_year(2000))
        self.assertFalse(control_flow.is_leap_year(2100))


class TestLongestRun(unittest.TestCase):
    def test_basic_runs(self):
        self.assertEqual(control_flow.longest_run([1, 1, 2, 2, 2, 3]), 3)
        self.assertEqual(control_flow.longest_run([7, 7, 7, 7]), 4)

    def test_no_repeats(self):
        self.assertEqual(control_flow.longest_run([1, 2, 3]), 1)

    def test_edges(self):
        self.assertEqual(control_flow.longest_run([]), 0)
        self.assertEqual(control_flow.longest_run([5]), 1)

    def test_run_at_end(self):
        self.assertEqual(control_flow.longest_run([1, 2, 2, 3, 3, 3]), 3)

    def test_works_on_strings_too(self):
        self.assertEqual(control_flow.longest_run(list("aabbbcc")), 3)


class TestHonestControlFlow(unittest.TestCase):
    def test_uses_a_loop_somewhere(self):
        tree = ast.parse(inspect.getsource(control_flow))
        loops = [node for node in ast.walk(tree)
                 if isinstance(node, (ast.For, ast.While))]
        self.assertTrue(loops, "this assignment is about loops; use some")


if __name__ == "__main__":
    unittest.main()
