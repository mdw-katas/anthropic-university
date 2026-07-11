# Assignment a3 — Recursion (no loops allowed)

Implement the five functions stubbed in `starter/recursion.py` — recursively.
The test suite parses your source with `ast` and **fails if any function
contains a `for`, `while`, or comprehension**. Base case + progress, nothing
else.

| Function              | Contract                                                    |
|-----------------------|-------------------------------------------------------------|
| `sum_digits(n)`       | Sum of the decimal digits of non-negative `n`               |
| `power(base, exp)`    | `base ** exp` for `exp >= 0` — by fast (halving) recursion  |
| `flatten(nested)`     | Flatten arbitrarily nested lists into one flat list         |
| `pascal_row(n)`       | Row `n` of Pascal's triangle; row 0 is `[1]`                |
| `hanoi(n, a, b, c)`   | Move list solving Towers of Hanoi from peg `a` to peg `c`   |

Notes:

- `power` must halve the exponent (`exp // 2`) rather than decrement it —
  the test rejects a solution that recurses 1000 deep on `power(2, 1000)`
  by watching the recursion depth. Think: `power(b, 10) == power(b*b, 5)`.
- `flatten([1, [2, [3, [4]]], 5])` is `[1, 2, 3, 4, 5]`. An element is a
  sub-list if `isinstance(element, list)`.
- `hanoi` returns moves as `(from_peg, to_peg)` tuples. Trust the contract:
  move n-1 out of the way, move the big one, move n-1 back on top.

```
uni grade 101/a3 --dry
uni grade 101/a3
```
