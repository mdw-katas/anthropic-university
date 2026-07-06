"""The executable contract for the final project, mdtable."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "starter"))

import mdtable


class TestSplitRow(unittest.TestCase):
    def test_standard_row(self):
        self.assertEqual(mdtable.split_row("| a | b |"), ["a", "b"])

    def test_without_outer_pipes(self):
        self.assertEqual(mdtable.split_row("a | b"), ["a", "b"])

    def test_empty_cells_survive(self):
        self.assertEqual(mdtable.split_row("| a |  | c |"), ["a", "", "c"])

    def test_surrounding_whitespace(self):
        self.assertEqual(mdtable.split_row("   | x |   "), ["x"])


class TestIsSeparator(unittest.TestCase):
    def test_separators(self):
        self.assertTrue(mdtable.is_separator("|---|---|"))
        self.assertTrue(mdtable.is_separator("|:--|--:|:-:|"))
        self.assertTrue(mdtable.is_separator("| --- | --- |"))

    def test_non_separators(self):
        self.assertFalse(mdtable.is_separator("| a | b |"))
        self.assertFalse(mdtable.is_separator("just text"))
        self.assertFalse(mdtable.is_separator(""))
        self.assertFalse(mdtable.is_separator("|--x--|"))


class TestAlignment(unittest.TestCase):
    def test_all_four(self):
        self.assertEqual(mdtable.alignment("---"), "default")
        self.assertEqual(mdtable.alignment(":--"), "left")
        self.assertEqual(mdtable.alignment("--:"), "right")
        self.assertEqual(mdtable.alignment(":-:"), "center")


class TestColumnWidths(unittest.TestCase):
    def test_longest_cell_wins(self):
        rows = [["Course", "Title"], ["101", "Intro to CS"]]
        self.assertEqual(mdtable.column_widths(rows), [6, 11])

    def test_minimum_width_is_three(self):
        self.assertEqual(mdtable.column_widths([["a", "b"], ["1", "2"]]), [3, 3])

    def test_ragged_rows(self):
        rows = [["alpha", "b"], ["1"]]
        self.assertEqual(mdtable.column_widths(rows), [5, 3])


class TestFormatTable(unittest.TestCase):
    def test_normalizes_ragged_widths(self):
        lines = [
            "| Course | Title |",
            "|---|---|",
            "| 101 | Intro to CS |",
            "| 440 | Deep Learning and LLMs |",
        ]
        self.assertEqual(mdtable.format_table(lines), [
            "| Course | Title                  |",
            "|--------|------------------------|",
            "| 101    | Intro to CS            |",
            "| 440    | Deep Learning and LLMs |",
        ])

    def test_alignment_is_preserved_and_applied(self):
        lines = [
            "| name | qty | price |",
            "|:-----|:---:|------:|",
            "| tea | 2 | 4.50 |",
        ]
        self.assertEqual(mdtable.format_table(lines), [
            "| name | qty | price |",
            "|:-----|:---:|------:|",
            "| tea  |  2  |  4.50 |",
        ])

    def test_ragged_row_padded_with_empty_cells(self):
        lines = ["| a | b |", "|---|---|", "| 1 |"]
        self.assertEqual(mdtable.format_table(lines), [
            "| a   | b   |",
            "|-----|-----|",
            "| 1   |     |",
        ])

    def test_idempotent(self):
        lines = [
            "| x | y |",
            "|--:|:--|",
            "| 10 | left |",
        ]
        once = mdtable.format_table(lines)
        self.assertEqual(mdtable.format_table(once), once)


class TestFormatDocument(unittest.TestCase):
    def test_formats_table_leaves_prose(self):
        text = "Intro prose.\n\n| a | b |\n|---|---|\n| 1 | 22 |\n\nOutro."
        self.assertEqual(mdtable.format_document(text),
                         "Intro prose.\n\n"
                         "| a   | b   |\n"
                         "|-----|-----|\n"
                         "| 1   | 22  |\n"
                         "\nOutro.")

    def test_fenced_code_blocks_untouched(self):
        text = "```\n| not | a | table |\n|---|---|---|\n```\n"
        self.assertEqual(mdtable.format_document(text), text)

    def test_pipe_lines_without_separator_untouched(self):
        text = "| just | one | line |\nno separator follows\n"
        self.assertEqual(mdtable.format_document(text), text)

    def test_two_tables_in_one_document(self):
        text = ("| a | b |\n|---|---|\n| 1 | 2 |\n"
                "\nbetween\n\n"
                "| ccc | d |\n|---|---|\n| 3 | 4 |")
        expected = ("| a   | b   |\n|-----|-----|\n| 1   | 2   |\n"
                    "\nbetween\n\n"
                    "| ccc | d   |\n|-----|-----|\n| 3   | 4   |")
        self.assertEqual(mdtable.format_document(text), expected)

    def test_document_is_idempotent(self):
        text = "title\n\n| aa | b |\n|:-:|--:|\n| 1 | 2 |\n"
        once = mdtable.format_document(text)
        self.assertEqual(mdtable.format_document(once), once)


if __name__ == "__main__":
    unittest.main()
