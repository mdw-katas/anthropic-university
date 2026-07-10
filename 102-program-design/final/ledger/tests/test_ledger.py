"""The executable specification for the CS 102 final."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import model
import parsing
import report
from model import Posting, Transaction, UnbalancedError

SAMPLE = """\
; my-money.ledger
2026-07-01 Opening balance
    assets:checking     1000.00
    equity:opening

2026-07-03 Groceries
    expenses:food         42.50
    assets:checking
"""


def parse_all(text):
    return list(parsing.parse_ledger(text.splitlines()))


class TestPosting(unittest.TestCase):
    def test_value_equality(self):
        self.assertEqual(Posting("assets:checking", 4250),
                         Posting("assets:checking", 4250))
        self.assertNotEqual(Posting("assets:checking", 4250),
                            Posting("assets:checking", 4251))
        self.assertNotEqual(Posting("assets:checking", 4250),
                            Posting("assets:savings", 4250))

    def test_comparison_with_non_posting_is_false_not_fatal(self):
        self.assertFalse(Posting("a", 1) == ("a", 1))


class TestTransactionInvariants(unittest.TestCase):
    def test_balanced_transaction_constructs(self):
        transaction = Transaction("2026-07-01", "ok",
                                  [Posting("a", 500), Posting("b", -500)])
        self.assertEqual(transaction.date, "2026-07-01")
        self.assertEqual(transaction.description, "ok")

    def test_unbalanced_transaction_is_rejected_naming_the_date(self):
        with self.assertRaises(UnbalancedError) as caught:
            Transaction("2026-07-04", "leaky",
                        [Posting("a", 500), Posting("b", -499)])
        self.assertIn("2026-07-04", str(caught.exception))

    def test_unbalanced_error_is_a_value_error(self):
        self.assertTrue(issubclass(UnbalancedError, ValueError))

    def test_fewer_than_two_postings_is_rejected(self):
        with self.assertRaises(ValueError):
            Transaction("2026-07-01", "lonely", [Posting("a", 0)])

    def test_postings_are_snapshotted_as_a_tuple(self):
        source = [Posting("a", 100), Posting("b", -100)]
        transaction = Transaction("2026-07-01", "x", source)
        source.append("intruder")
        self.assertEqual(len(transaction.postings), 2)
        self.assertIsInstance(transaction.postings, tuple)


class TestParseAmount(unittest.TestCase):
    def test_dollars_and_cents(self):
        self.assertEqual(parsing.parse_amount("42.50"), 4250)
        self.assertEqual(parsing.parse_amount("0.05"), 5)
        self.assertEqual(parsing.parse_amount("1000.00"), 100000)

    def test_whole_dollars_and_negatives(self):
        self.assertEqual(parsing.parse_amount("-7"), -700)
        self.assertEqual(parsing.parse_amount("0"), 0)
        self.assertEqual(parsing.parse_amount("-0.05"), -5)

    def test_rejects_malformed_amounts(self):
        for bad in ("12.345", "12.5", "1,000", "$5", "abc", "", "5.", "1 0"):
            with self.assertRaises(ValueError, msg=f"should reject {bad!r}"):
                parsing.parse_amount(bad)


class TestParseLedger(unittest.TestCase):
    def test_parses_the_sample(self):
        transactions = parse_all(SAMPLE)
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0].date, "2026-07-01")
        self.assertEqual(transactions[0].description, "Opening balance")
        self.assertEqual(transactions[1].description, "Groceries")

    def test_explicit_amounts_are_parsed(self):
        first = parse_all(SAMPLE)[0]
        self.assertIn(Posting("assets:checking", 100000), first.postings)

    def test_elided_amount_balances_the_transaction(self):
        first, second = parse_all(SAMPLE)
        self.assertIn(Posting("equity:opening", -100000), first.postings)
        self.assertIn(Posting("assets:checking", -4250), second.postings)

    def test_final_block_needs_no_trailing_blank_line(self):
        transactions = parse_all("2026-01-01 x\n    a:b  1.00\n    c:d")
        self.assertEqual(len(transactions), 1)

    def test_comments_and_blank_lines_are_skipped(self):
        text = "; header\n\n2026-01-01 x\n    a:b  1.00\n    c:d\n# trailer\n"
        self.assertEqual(len(parse_all(text)), 1)

    def test_indented_line_with_no_open_transaction(self):
        with self.assertRaises(parsing.MalformedLineError) as caught:
            parse_all("    orphan:posting  1.00")
        self.assertEqual(caught.exception.line_number, 1)

    def test_second_elided_posting_is_malformed(self):
        text = "2026-01-01 x\n    a:b  1.00\n    c:d\n    e:f\n"
        with self.assertRaises(parsing.MalformedLineError) as caught:
            parse_all(text)
        self.assertEqual(caught.exception.line_number, 4)
        self.assertIn("4", str(caught.exception))

    def test_bad_date_or_missing_description_is_malformed(self):
        with self.assertRaises(parsing.MalformedLineError):
            parse_all("2026/01/01 slashes\n    a:b 1.00\n    c:d\n")
        with self.assertRaises(parsing.MalformedLineError):
            parse_all("2026-01-01\n    a:b 1.00\n    c:d\n")

    def test_bad_amount_carries_line_number_and_cause(self):
        text = "2026-01-01 x\n    a:b  1.00\n    c:d  1O.00\n"
        with self.assertRaises(parsing.AmountError) as caught:
            parse_all(text)
        self.assertEqual(caught.exception.line_number, 3)
        self.assertIsInstance(caught.exception.__cause__, ValueError)

    def test_unbalanced_transaction_propagates_from_the_model(self):
        text = "2026-01-01 leaky\n    a:b  5.00\n    c:d  1.00\n"
        with self.assertRaises(UnbalancedError):
            parse_all(text)

    def test_errors_are_one_catchable_family(self):
        self.assertTrue(issubclass(parsing.MalformedLineError, parsing.LedgerError))
        self.assertTrue(issubclass(parsing.AmountError, parsing.LedgerError))


class CountingLines:
    """A probe: an iterator of lines that counts how far it was consumed."""

    def __init__(self, lines):
        self._lines = iter(lines)
        self.consumed = 0

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self._lines)
        self.consumed += 1
        return line


class TestLaziness(unittest.TestCase):
    def test_first_transaction_costs_only_its_own_lines(self):
        blocks = []
        for day in range(1, 51):
            blocks.append(f"2026-01-{day:02d} block {day}\n"
                          f"    expenses:misc  1.00\n"
                          f"    assets:cash\n\n")
        probe = CountingLines("".join(blocks).splitlines())
        generator = parsing.parse_ledger(probe)
        first = next(generator)
        self.assertEqual(first.description, "block 1")
        self.assertLessEqual(
            probe.consumed, 4,
            "parse_ledger read far past the first block: not actually lazy")


class TestReport(unittest.TestCase):
    def test_format_cents(self):
        self.assertEqual(report.format_cents(4250), "42.50")
        self.assertEqual(report.format_cents(0), "0.00")
        self.assertEqual(report.format_cents(100000), "1000.00")

    def test_format_cents_negative_and_small(self):
        self.assertEqual(report.format_cents(-5), "-0.05")
        self.assertEqual(report.format_cents(-100000), "-1000.00")
        self.assertEqual(report.format_cents(7), "0.07")

    def test_balances_aggregates_across_transactions(self):
        totals = report.balances(parse_all(SAMPLE))
        self.assertEqual(totals["assets:checking"], 95750)
        self.assertEqual(totals["equity:opening"], -100000)
        self.assertEqual(totals["expenses:food"], 4250)

    def test_balance_report_fixed_width(self):
        rendered = report.balance_report(parse_all(SAMPLE))
        self.assertEqual(rendered,
                         "assets:checking    957.50\n"
                         "equity:opening   -1000.00\n"
                         "expenses:food       42.50")

    def test_balance_report_empty(self):
        self.assertEqual(report.balance_report([]), "")


class TestAlgebraicInvariants(unittest.TestCase):
    def test_money_is_conserved(self):
        text = SAMPLE + ("\n2026-07-09 Split dinner\n"
                         "    expenses:food     18.00\n"
                         "    assets:cash      -10.00\n"
                         "    assets:checking\n")
        totals = report.balances(parse_all(text))
        self.assertEqual(sum(totals.values()), 0,
                         "double-entry bookkeeping is a conservation law")

    def test_amounts_round_trip(self):
        for cents in (0, 1, -1, 5, 99, 100, -4250, 123456, -100000):
            self.assertEqual(parsing.parse_amount(report.format_cents(cents)),
                             cents)


if __name__ == "__main__":
    unittest.main()
