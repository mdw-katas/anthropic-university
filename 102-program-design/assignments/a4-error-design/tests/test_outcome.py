"""The executable specification for assignment a4."""
import ast
import inspect
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import outcome
from outcome import (BadValueError, ConfigError, DuplicateKeyError, Err,
                     MalformedLineError, Ok, parse_config, parse_port,
                     partition, try_call)


class TestCatchPrecisely(unittest.TestCase):
    def test_no_bare_or_catch_all_except(self):
        tree = ast.parse(inspect.getsource(outcome))
        for node in ast.walk(tree):
            if not isinstance(node, ast.ExceptHandler):
                continue
            self.assertIsNotNone(node.type, "bare except: is banned")
            named = []
            if isinstance(node.type, ast.Name):
                named = [node.type.id]
            elif isinstance(node.type, ast.Tuple):
                named = [e.id for e in node.type.elts if isinstance(e, ast.Name)]
            for name in named:
                self.assertNotIn(name, ("Exception", "BaseException"),
                                 "catch precisely, not Exception")


class TestHierarchy(unittest.TestCase):
    def test_all_config_errors_share_a_base(self):
        for subclass in (MalformedLineError, DuplicateKeyError, BadValueError):
            self.assertTrue(issubclass(subclass, ConfigError))
        self.assertTrue(issubclass(ConfigError, Exception))

    def test_one_except_clause_catches_the_family(self):
        try:
            parse_config("no equals sign here")
        except ConfigError:
            return
        self.fail("a ConfigError subclass should have been raised")


class TestParseConfig(unittest.TestCase):
    def test_happy_path(self):
        text = "host = example.com\nport = 8080\n"
        self.assertEqual(parse_config(text),
                         {"host": "example.com", "port": "8080"})

    def test_blank_lines_and_comments_are_skipped(self):
        text = "\n# the port\nport = 9\n\n   # done\n"
        self.assertEqual(parse_config(text), {"port": "9"})

    def test_value_keeps_internal_spaces(self):
        self.assertEqual(parse_config("greeting = hello world"),
                         {"greeting": "hello world"})

    def test_value_may_be_empty(self):
        self.assertEqual(parse_config("retries ="), {"retries": ""})

    def test_only_the_first_equals_splits(self):
        self.assertEqual(parse_config("formula = a = b"),
                         {"formula": "a = b"})

    def test_malformed_line_carries_its_line_number(self):
        with self.assertRaises(MalformedLineError) as caught:
            parse_config("host = ok\nport 8080\n")
        self.assertEqual(caught.exception.line_number, 2)
        self.assertIn("2", str(caught.exception))

    def test_empty_key_is_malformed(self):
        with self.assertRaises(MalformedLineError) as caught:
            parse_config("= value")
        self.assertEqual(caught.exception.line_number, 1)

    def test_duplicate_key_names_the_second_line(self):
        with self.assertRaises(DuplicateKeyError) as caught:
            parse_config("a = 1\nb = 2\na = 3\n")
        self.assertEqual(caught.exception.line_number, 3)
        self.assertIn("3", str(caught.exception))


class TestParsePort(unittest.TestCase):
    def test_valid_port(self):
        self.assertEqual(parse_port("8080"), 8080)

    def test_non_numeric_raises_translated_and_chained(self):
        with self.assertRaises(BadValueError) as caught:
            parse_port("http")
        self.assertIsInstance(caught.exception.__cause__, ValueError,
                              "translate at the boundary with raise...from")

    def test_out_of_range_is_a_bad_value(self):
        for text in ("0", "65536", "-1"):
            with self.assertRaises(BadValueError):
                parse_port(text)


class TestResult(unittest.TestCase):
    def test_ok_basics(self):
        result = Ok(21)
        self.assertTrue(result.is_ok())
        self.assertEqual(result.value, 21)
        self.assertEqual(result.unwrap_or(0), 21)

    def test_err_basics(self):
        failure = ValueError("nope")
        result = Err(failure)
        self.assertFalse(result.is_ok())
        self.assertIs(result.error, failure)
        self.assertEqual(result.unwrap_or(0), 0)

    def test_ok_map(self):
        mapped = Ok(21).map(lambda v: v * 2)
        self.assertTrue(mapped.is_ok())
        self.assertEqual(mapped.value, 42)

    def test_err_map_never_calls_fn(self):
        def exploding(_):
            raise AssertionError("map on Err must not call fn")
        result = Err(ValueError("nope")).map(exploding)
        self.assertFalse(result.is_ok())

    def test_and_then_chains_and_short_circuits(self):
        def half(n):
            if n % 2:
                return Err("odd")
            return Ok(n // 2)
        self.assertEqual(Ok(8).and_then(half).and_then(half).value, 2)
        chained = Ok(6).and_then(half).and_then(half)
        self.assertFalse(chained.is_ok())
        self.assertEqual(chained.error, "odd")

    def test_err_and_then_never_calls_fn(self):
        def exploding(_):
            raise AssertionError("and_then on Err must not call fn")
        result = Err("already failed").and_then(exploding)
        self.assertFalse(result.is_ok())


class TestTryCall(unittest.TestCase):
    def test_success_is_ok(self):
        result = try_call(ValueError, int, "42")
        self.assertTrue(result.is_ok())
        self.assertEqual(result.value, 42)

    def test_listed_exception_is_captured(self):
        result = try_call(ValueError, int, "not a number")
        self.assertFalse(result.is_ok())
        self.assertIsInstance(result.error, ValueError)

    def test_unlisted_exception_propagates(self):
        with self.assertRaises(TypeError):
            try_call(ValueError, len, 42)

    def test_tuple_of_exception_types(self):
        result = try_call((KeyError, ValueError), int, "x")
        self.assertIsInstance(result.error, ValueError)


class TestPartition(unittest.TestCase):
    def test_splits_values_and_errors(self):
        results = [Ok(1), Err("a"), Ok(2), Err("b")]
        values, errors = partition(results)
        self.assertEqual(values, [1, 2])
        self.assertEqual(errors, ["a", "b"])

    def test_bulk_validation_scenario(self):
        raw = ["80", "http", "443", "0"]
        values, errors = partition([try_call(BadValueError, parse_port, r)
                                    for r in raw])
        self.assertEqual(values, [80, 443])
        self.assertEqual(len(errors), 2,
                         "failure is data: nothing detonates, all are reported")


if __name__ == "__main__":
    unittest.main()
