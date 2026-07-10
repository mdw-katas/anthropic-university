"""The executable specification for assignment a2."""
import ast
import inspect
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import expressions
from expressions import Add, Literal, Mul, Neg, Var


class TestNoTypeSwitching(unittest.TestCase):
    def test_module_never_inspects_types(self):
        tree = ast.parse(inspect.getsource(expressions))
        for node in ast.walk(tree):
            self.assertNotIsInstance(node, ast.Match,
                                     "no match statements — dispatch instead")
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, ("isinstance", "type"),
                                 "no type-switching — dispatch instead")


class TestLiteral(unittest.TestCase):
    def test_evaluate(self):
        self.assertEqual(Literal(2).evaluate({}), 2)
        self.assertEqual(Literal(-7).evaluate({"x": 1}), -7)

    def test_render(self):
        self.assertEqual(Literal(42).render(), "42")

    def test_variables(self):
        self.assertEqual(Literal(1).variables(), set())


class TestVar(unittest.TestCase):
    def test_evaluate_looks_up_env(self):
        self.assertEqual(Var("x").evaluate({"x": 5}), 5)

    def test_missing_variable_raises_nameerror_naming_it(self):
        with self.assertRaises(NameError) as caught:
            Var("velocity").evaluate({"x": 1})
        self.assertIn("velocity", str(caught.exception))

    def test_render_and_variables(self):
        self.assertEqual(Var("x").render(), "x")
        self.assertEqual(Var("x").variables(), {"x"})


class TestComposites(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Add(Literal(2), Literal(3)).evaluate({}), 5)

    def test_mul(self):
        self.assertEqual(Mul(Literal(4), Literal(5)).evaluate({}), 20)

    def test_neg(self):
        self.assertEqual(Neg(Literal(9)).evaluate({}), -9)

    def test_nested_evaluation(self):
        tree = Mul(Literal(2), Add(Var("x"), Neg(Literal(3))))
        self.assertEqual(tree.evaluate({"x": 10}), 14)

    def test_nested_render(self):
        tree = Mul(Literal(2), Add(Var("x"), Neg(Literal(3))))
        self.assertEqual(tree.render(), "(2 * (x + (-3)))")

    def test_variables_union(self):
        tree = Add(Mul(Var("a"), Var("b")), Add(Var("a"), Literal(1)))
        self.assertEqual(tree.variables(), {"a", "b"})


class Clamp:
    """A node type your module has never heard of. If your composites
    dispatch through the protocol, they will host it without noticing."""

    def __init__(self, inner, low, high):
        self.inner, self.low, self.high = inner, low, high

    def evaluate(self, env):
        return max(self.low, min(self.high, self.inner.evaluate(env)))

    def render(self):
        return f"clamp({self.inner.render()}, {self.low}, {self.high})"

    def variables(self):
        return self.inner.variables()


class TestOpenToExtension(unittest.TestCase):
    def test_foreign_node_evaluates_inside_yours(self):
        tree = Add(Literal(1), Clamp(Var("x"), 0, 10))
        self.assertEqual(tree.evaluate({"x": 99}), 11)

    def test_foreign_node_renders_inside_yours(self):
        tree = Add(Literal(1), Clamp(Var("x"), 0, 10))
        self.assertEqual(tree.render(), "(1 + clamp(x, 0, 10))")

    def test_foreign_node_reports_variables_inside_yours(self):
        tree = Mul(Clamp(Var("t"), 0, 1), Var("u"))
        self.assertEqual(tree.variables(), {"t", "u"})


if __name__ == "__main__":
    unittest.main()
