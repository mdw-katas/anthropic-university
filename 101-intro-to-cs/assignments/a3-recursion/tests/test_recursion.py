"""The executable specification for assignment a3."""
import ast
import inspect
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import recursion

FORBIDDEN_NODES = (ast.For, ast.While, ast.AsyncFor,
                   ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)


class TestNoLoops(unittest.TestCase):
    def test_all_functions_are_loop_free(self):
        tree = ast.parse(inspect.getsource(recursion))
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for inner in ast.walk(node):
                    self.assertNotIsInstance(
                        inner, FORBIDDEN_NODES,
                        f"{node.name} contains a loop or comprehension; recursion only")


class TestSumDigits(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(recursion.sum_digits(0), 0)
        self.assertEqual(recursion.sum_digits(7), 7)
        self.assertEqual(recursion.sum_digits(942), 15)
        self.assertEqual(recursion.sum_digits(99999), 45)


class TestPower(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(recursion.power(2, 0), 1)
        self.assertEqual(recursion.power(2, 10), 1024)
        self.assertEqual(recursion.power(3, 5), 243)
        self.assertEqual(recursion.power(10, 3), 1000)

    def test_halves_the_exponent(self):
        # A decrement-style recursion would need ~1000 frames here; halving
        # needs ~10. The temporary ceiling makes the difference observable.
        limit = sys.getrecursionlimit()
        sys.setrecursionlimit(200)
        try:
            self.assertEqual(recursion.power(2, 1000), 2 ** 1000)
        finally:
            sys.setrecursionlimit(limit)


class TestFlatten(unittest.TestCase):
    def test_nested(self):
        self.assertEqual(recursion.flatten([1, [2, [3, [4]]], 5]), [1, 2, 3, 4, 5])

    def test_already_flat(self):
        self.assertEqual(recursion.flatten([1, 2, 3]), [1, 2, 3])

    def test_empty_and_empties(self):
        self.assertEqual(recursion.flatten([]), [])
        self.assertEqual(recursion.flatten([[], [[]], []]), [])

    def test_strings_are_elements_not_lists(self):
        self.assertEqual(recursion.flatten(["ab", ["cd"]]), ["ab", "cd"])


class TestPascalRow(unittest.TestCase):
    def test_first_rows(self):
        self.assertEqual(recursion.pascal_row(0),      [1])
        self.assertEqual(recursion.pascal_row(1),     [1, 1])
        self.assertEqual(recursion.pascal_row(2),    [1, 2, 1])
        self.assertEqual(recursion.pascal_row(3),   [1, 3, 3, 1])
        self.assertEqual(recursion.pascal_row(4),  [1, 4, 6, 4, 1])
        self.assertEqual(recursion.pascal_row(5), [1, 5,10,10, 5, 1])

    def test_row_sums_are_powers_of_two(self):
        self.assertEqual(sum(recursion.pascal_row(10)), 1024)


class TestHanoi(unittest.TestCase):
    def test_zero_and_one(self):
        self.assertEqual(recursion.hanoi(0, "A", "B", "C"), [])
        self.assertEqual(recursion.hanoi(1, "A", "B", "C"), [("A", "C")])

    def test_three_disks_move_count(self):
        moves = recursion.hanoi(3, "A", "B", "C")
        self.assertEqual(len(moves), 7)  # 2^n - 1

    def test_moves_actually_solve_the_puzzle(self):
        n = 4
        pegs = {"A": list(range(n, 0, -1)), "B": [], "C": []}
        for source, target in recursion.hanoi(n, "A", "B", "C"):
            disk = pegs[source].pop()
            self.assertTrue(all(disk < resting for resting in pegs[target][-1:]),
                            "a larger disk landed on a smaller one")
            pegs[target].append(disk)
        self.assertEqual(pegs["C"], list(range(n, 0, -1)))


if __name__ == "__main__":
    unittest.main()
