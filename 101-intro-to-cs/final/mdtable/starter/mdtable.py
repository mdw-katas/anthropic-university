"""Final project: mdtable — normalize Markdown tables to fixed-width columns.

The test suite (tests/test_mdtable.py) is the contract. main() is provided
free of charge and is not graded.
"""
import re
import sys


def split_row(line):
    """Strip the line, drop one leading and one trailing '|' if present,
    split on '|', and strip each cell. Returns a list of cell strings.
    """
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [x.strip() for x in line.split('|')]


def is_separator(line):
    """True if the line splits into 1+ cells, each matching :?-+:? ."""
    line = line.strip()
    if not line.startswith('|'):
        return False
    if not line.endswith('|'):
        return False

    fields = line[1:-1].split('|')
    for field in fields:
        field = field.strip()
        start = 0
        end = len(field)
        if start == end:
            return False
        if field.startswith(':'):
            start += 1
        if field.endswith(':'):
            end -= 1
        for c in field[start:end]:
            if c != '-':
                return False
    return True


def alignment(cell):
    """Map a separator cell to "left", "right", "center", or "default"."""
    if cell.startswith(':-') and cell.endswith('-:'):
        return "center"
    if cell.startswith(':-'):
        return "left"
    if cell.endswith('-:'):
        return "right"
    return "default"


def column_widths(rows):
    """Given content rows (lists of cells; header + body, no separator),
    return each column's width: the longest cell in it, minimum 3.
    Rows may be ragged; missing cells count as "".
    """
    max_row_count = max([len(row) for row in rows])
    max_lengths = [3 for _ in range(max_row_count)]
    for row in rows:
        for n, field in enumerate(row):
            if n >= len(max_lengths):
                continue
            max_lengths[n] = max(max_lengths[n], len(field))
    return max_lengths


def format_row(fields, widths, aligns):
    result = "|"
    while len(fields) < len(widths):
        fields.append('')
    for n, field in enumerate(fields):
        if aligns[n] == "center":
            field = field.center(widths[n])
        elif aligns[n] == "right":
            field = field.rjust(widths[n])
        else:
            field = field.ljust(widths[n])
        result += " " + field + " |"
    return result


def format_separator_row(fields, widths):
    result = "|"
    for n, original in enumerate(fields):
        field = '-' * (widths[n] + 2)
        if original.startswith(":"):
            field = ":" + field[1:]
        if original.endswith(":"):
            field = field[:-1] + ":"
        result += field+"|"
    return result


def format_table(lines):
    """Normalize one table (header line, separator line, body lines).

    Returns the reformatted lines. Content cells are padded to the column
    width (default/left: ljust, right: rjust, center: centered) and framed
    as '| cell |' with single spaces. Separator cells span width + 2
    characters using dashes and their alignment colons. Idempotent.
    """
    if len(lines) < 2:
        return lines
    if not is_separator(lines[1]):
        return lines
    header, separator, *records = [split_row(line) for line in lines]
    widths = column_widths([header] + records)
    aligns = [alignment(sep) for sep in separator]
    return [
        format_row(header, widths, aligns),
        format_separator_row(separator, widths)
    ] + [format_row(record, widths, aligns) for record in records]

def format_document(text):
    """Reformat every table in the document; leave all other lines —
    including everything inside ``` fenced code blocks — untouched.

    A table is a run of consecutive lines whose stripped form starts with
    '|', in which the second line is a separator row.
    """
    table = []
    results = []
    in_fenced_code = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fenced_code = not in_fenced_code
            results.append(line)
            continue
        if in_fenced_code:
            results.append(line)
            continue
        if not line.strip().startswith('|'):
            results += format_table(table)
            table = []
            results.append(line)
            continue
        table.append(line)

    results += format_table(table)
    result = '\n'.join(results)
    if text.endswith('\n'):
        result += '\n'
    return result


def main():
    sys.stdout.write(format_document(sys.stdin.read()))


if __name__ == "__main__":
    main()
