# Final Project — `mdtable`, a Markdown Table Formatter

Build a tool that rewrites Markdown so every table has fixed-width columns:

```
| Course | Title |                      | Course | Title                  |
|---|---|                        →     |--------|------------------------|
| 101 | Intro to CS |                  | 101    | Intro to CS            |
| 440 | Deep Learning and LLMs |       | 440    | Deep Learning and LLMs |
```

This is the whole course in one program: real parsing (state), functions
with contracts, collections, invariants (idempotency!), and edge cases that
punish sloppy thinking. It is also a tool this university's registrar
genuinely wants to exist.

## The specification

Implement the six functions stubbed in `starter/mdtable.py`. The test suite
is the contract; the rules in prose:

1. **`split_row(line)`** — strip the line, remove one leading and one
   trailing `|` if present, split on `|`, strip each cell.
2. **`is_separator(line)`** — True iff the line splits into one or more
   cells, each matching `:?-+:?` (dashes, optional alignment colons).
3. **`alignment(cell)`** — a separator cell maps to `"left"` (`:--`),
   `"right"` (`--:`), `"center"` (`:-:`), or `"default"` (`---`).
4. **`column_widths(rows)`** — given cell-lists (header + body, NOT the
   separator), the width of each column is its longest cell, minimum 3.
   Ragged rows are treated as padded with `""`.
5. **`format_table(lines)`** — lines[0] is the header, lines[1] the
   separator, the rest body. Pad every row to the widest column count.
   Content cells render `| cell |` with one space each side, padded to the
   column width: default/left ljust, right rjust, center centered. Separator
   cells span the full inner width (width + 2): `-----`, `:----`, `----:`,
   or `:---:`. The output must be **idempotent**: formatting twice changes
   nothing.
6. **`format_document(text)`** — walk the document; a table is a run of
   consecutive lines that (stripped) start with `|`, where the second line
   is a separator. Format each table; leave everything else byte-for-byte —
   especially the interiors of ``` fenced code blocks, which are never
   touched no matter what they contain.

`main()` (stdin → stdout) is provided; it is not graded. When your tests are
green, try it on this university's own README:

```
python3 starter/mdtable.py < ../../../README.md
```

## Grading

```
uni grade 101/final --dry
uni grade 101/final
```

19 tests; pass bar 80%, best score kept, like everything else — but this is
the final. Go get 100%.
