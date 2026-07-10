"""The executable specification for assignment a1."""
import ast
import inspect
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import bag as bag_module
from bag import Bag


class TestNoCollectionsImport(unittest.TestCase):
    def test_collections_module_is_banned(self):
        tree = ast.parse(inspect.getsource(bag_module))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.assertNotEqual(alias.name.split(".")[0], "collections",
                                        "no Counter/defaultdict — build on dict")
            if isinstance(node, ast.ImportFrom):
                self.assertNotEqual((node.module or "").split(".")[0], "collections",
                                    "no Counter/defaultdict — build on dict")


class TestConstruction(unittest.TestCase):
    def test_empty_bag(self):
        bag = Bag()
        self.assertEqual(len(bag), 0)
        self.assertEqual(bag.distinct(), [])

    def test_counts_multiplicity(self):
        bag = Bag(["a", "b", "a"])
        self.assertEqual(bag.count("a"), 2)
        self.assertEqual(bag.count("b"), 1)
        self.assertEqual(bag.count("z"), 0)
        self.assertEqual(len(bag), 3)

    def test_constructor_snapshots_its_argument(self):
        source = ["a", "b"]
        bag = Bag(source)
        source.append("c")
        self.assertEqual(bag.count("c"), 0, "the bag must copy, not alias")


class TestAddAndRemove(unittest.TestCase):
    def test_add_accumulates(self):
        bag = Bag(["a"])
        bag.add("a")
        bag.add("b", 3)
        self.assertEqual(bag.count("a"), 2)
        self.assertEqual(bag.count("b"), 3)

    def test_add_rejects_nonpositive_count(self):
        bag = Bag()
        with self.assertRaises(ValueError):
            bag.add("a", 0)
        with self.assertRaises(ValueError):
            bag.add("a", -2)

    def test_remove_decrements(self):
        bag = Bag(["a", "a", "a"])
        bag.remove("a", 2)
        self.assertEqual(bag.count("a"), 1)

    def test_removing_last_copy_removes_the_element(self):
        bag = Bag(["a", "a", "b"])
        bag.remove("a", 2)
        self.assertNotIn("a", bag)
        self.assertEqual(bag.distinct(), ["b"])

    def test_remove_more_than_held_raises_and_changes_nothing(self):
        bag = Bag(["a", "a"])
        with self.assertRaises(ValueError):
            bag.remove("a", 3)
        self.assertEqual(bag.count("a"), 2, "a failed remove must not half-happen")
        with self.assertRaises(ValueError):
            bag.remove("missing")

    def test_remove_rejects_nonpositive_count(self):
        bag = Bag(["a"])
        with self.assertRaises(ValueError):
            bag.remove("a", 0)


class TestQueries(unittest.TestCase):
    def test_contains(self):
        bag = Bag(["x"])
        self.assertIn("x", bag)
        self.assertNotIn("y", bag)

    def test_distinct_is_sorted(self):
        bag = Bag(["pear", "apple", "pear", "fig"])
        self.assertEqual(bag.distinct(), ["apple", "fig", "pear"])

    def test_distinct_returns_a_fresh_list(self):
        bag = Bag(["a", "b"])
        stolen = bag.distinct()
        stolen.append("intruder")
        self.assertEqual(bag.distinct(), ["a", "b"],
                         "mutating the returned list must not corrupt the bag")

    def test_most_common_orders_and_breaks_ties(self):
        bag = Bag(["b", "a", "b", "c", "a", "b"])
        self.assertEqual(bag.most_common(2), [("b", 3), ("a", 2)])
        self.assertEqual(bag.most_common(0), [])

    def test_most_common_tie_breaks_alphabetically(self):
        bag = Bag(["dog", "cat", "dog", "cat", "emu"])
        self.assertEqual(bag.most_common(3), [("cat", 2), ("dog", 2), ("emu", 1)])

    def test_most_common_oversized_k_returns_everything(self):
        bag = Bag(["a", "b"])
        self.assertEqual(bag.most_common(99), [("a", 1), ("b", 1)])


class TestValueSemantics(unittest.TestCase):
    def test_equality_ignores_insertion_order(self):
        self.assertEqual(Bag(["a", "b", "a"]), Bag(["b", "a", "a"]))

    def test_inequality_by_count(self):
        self.assertNotEqual(Bag(["a"]), Bag(["a", "a"]))

    def test_comparison_with_non_bag_is_false_not_fatal(self):
        self.assertFalse(Bag(["a"]) == ["a"])
        self.assertFalse(Bag(["a"]) == "a")

    def test_mutable_bags_are_unhashable(self):
        with self.assertRaises(TypeError):
            hash(Bag(["a"]))


if __name__ == "__main__":
    unittest.main()
