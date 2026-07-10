"""The executable specification for assignment a3."""
import ast
import inspect
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import functional_tools as ft


class TestTheBans(unittest.TestCase):
    def test_no_functools_or_itertools(self):
        tree = ast.parse(inspect.getsource(ft))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.assertNotIn(alias.name.split(".")[0],
                                     ("functools", "itertools"),
                                     "build it yourself this once")
            if isinstance(node, ast.ImportFrom):
                self.assertNotIn((node.module or "").split(".")[0],
                                 ("functools", "itertools"),
                                 "build it yourself this once")

    def test_no_calls_to_builtin_map_filter_reduce(self):
        tree = ast.parse(inspect.getsource(ft))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, ("map", "filter", "reduce"),
                                 "the builtins are exactly what you are building")


class TestMyMap(unittest.TestCase):
    def test_transforms_in_order(self):
        self.assertEqual(ft.my_map(lambda x: x * x, [1, 2, 3]), [1, 4, 9])

    def test_empty(self):
        self.assertEqual(ft.my_map(len, []), [])

    def test_consumes_any_iterable(self):
        self.assertEqual(ft.my_map(str.upper, iter(["a", "b"])), ["A", "B"])


class TestMyFilter(unittest.TestCase):
    def test_keeps_truthy_in_order(self):
        self.assertEqual(ft.my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]), [2, 4])

    def test_truthiness_not_just_true(self):
        self.assertEqual(ft.my_filter(len, ["", "a", "", "b"]), ["a", "b"])


class TestMyReduce(unittest.TestCase):
    def test_folds_left(self):
        self.assertEqual(ft.my_reduce(lambda acc, x: acc - x, [1, 2, 3], 10), 4)

    def test_no_initial_uses_first_element(self):
        self.assertEqual(ft.my_reduce(lambda acc, x: acc + x, [1, 2, 3, 4]), 10)

    def test_empty_with_initial_returns_initial(self):
        self.assertEqual(ft.my_reduce(lambda acc, x: acc + x, [], 99), 99)

    def test_none_is_a_legitimate_initial(self):
        result = ft.my_reduce(lambda acc, x: (acc, x), [1], None)
        self.assertEqual(result, (None, 1))

    def test_empty_without_initial_raises_typeerror(self):
        with self.assertRaises(TypeError):
            ft.my_reduce(lambda acc, x: acc + x, [])

    def test_single_element_never_calls_fn(self):
        def exploding(acc, x):
            raise AssertionError("fn must not be called for a single element")
        self.assertEqual(ft.my_reduce(exploding, [7]), 7)


class TestCompose(unittest.TestCase):
    def test_right_to_left(self):
        double = lambda x: x * 2
        increment = lambda x: x + 1
        self.assertEqual(ft.compose(double, increment)(5), 12)
        self.assertEqual(ft.compose(increment, double)(5), 11)

    def test_empty_compose_is_identity(self):
        self.assertEqual(ft.compose()("anything"), "anything")

    def test_three_deep(self):
        self.assertEqual(ft.compose(str, abs, int)("-42"), "42")


class CountingFunction:
    """A probe: counts how many times it is actually invoked."""

    def __init__(self, fn):
        self.fn = fn
        self.calls = 0

    def __call__(self, *args):
        self.calls += 1
        return self.fn(*args)


class TestMemoize(unittest.TestCase):
    def test_returns_correct_results(self):
        memoized = ft.memoize(lambda a, b: a + b)
        self.assertEqual(memoized(2, 3), 5)
        self.assertEqual(memoized(2, 4), 6)

    def test_equal_arguments_hit_the_function_once(self):
        probe = CountingFunction(lambda a, b: a * b)
        memoized = ft.memoize(probe)
        for _ in range(5):
            self.assertEqual(memoized(6, 7), 42)
        self.assertEqual(probe.calls, 1)

    def test_different_arguments_miss_separately(self):
        probe = CountingFunction(lambda n: n * 10)
        memoized = ft.memoize(probe)
        memoized(1), memoized(2), memoized(1), memoized(2)
        self.assertEqual(probe.calls, 2)

    def test_two_memoized_functions_do_not_share_a_cache(self):
        plus_one = ft.memoize(lambda n: n + 1)
        times_two = ft.memoize(lambda n: n * 2)
        self.assertEqual(plus_one(10), 11)
        self.assertEqual(times_two(10), 20,
                         "a shared/global cache collides on equal arguments")


class TestOnce(unittest.TestCase):
    def test_first_result_is_replayed(self):
        probe = CountingFunction(lambda: "expensive")
        guarded = ft.once(probe)
        self.assertEqual(guarded(), "expensive")
        self.assertEqual(guarded(), "expensive")
        self.assertEqual(probe.calls, 1)

    def test_later_arguments_are_ignored(self):
        probe = CountingFunction(lambda n: n * 2)
        guarded = ft.once(probe)
        self.assertEqual(guarded(5), 10)
        self.assertEqual(guarded(999), 10)
        self.assertEqual(probe.calls, 1)


if __name__ == "__main__":
    unittest.main()
