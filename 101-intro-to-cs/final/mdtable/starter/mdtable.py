"""Final project: mdtable — normalize Markdown tables to fixed-width columns.

The test suite (tests/test_mdtable.py) is the contract. main() is provided
free of charge and is not graded.
"""
import sys


def split_row(line):
    """Strip the line, drop one leading and one trailing '|' if present,
    split on '|', and strip each cell. Returns a list of cell strings.
    """
    raise NotImplementedError


def is_separator(line):
    """True iff the line splits into 1+ cells, each matching :?-+:? ."""
    raise NotImplementedError


def alignment(cell):
    """Map a separator cell to "left", "right", "center", or "default"."""
    raise NotImplementedError


def column_widths(rows):
    """Given content rows (lists of cells; header + body, no separator),
    return each column's width: the longest cell in it, minimum 3.
    Rows may be ragged; missing cells count as "".
    """
    raise NotImplementedError


def format_table(lines):
    """Normalize one table (header line, separator line, body lines).

    Returns the reformatted lines. Content cells are padded to the column
    width (default/left: ljust, right: rjust, center: centered) and framed
    as '| cell |' with single spaces. Separator cells span width + 2
    characters using dashes and their alignment colons. Idempotent.
    """
    raise NotImplementedError


def format_document(text):
    """Reformat every table in the document; leave all other lines —
    including everything inside ``` fenced code blocks — untouched.

    A table is a run of consecutive lines whose stripped form starts with
    '|', in which the second line is a separator row.
    """
    raise NotImplementedError


def main():
    sys.stdout.write(format_document(sys.stdin.read()))


if __name__ == "__main__":
    main()
