# Assignment a2 — Control Flow

Implement the four functions stubbed in `starter/control_flow.py`. The test
suite in `tests/` is the specification — read it first.

| Function                  | Contract                                                     |
|---------------------------|--------------------------------------------------------------|
| `fizzbuzz(n, rules)`      | Generalized FizzBuzz: apply (divisor, word) rules in order   |
| `to_binary(n)`            | Binary string for a non-negative int — no `bin()` allowed    |
| `is_leap_year(year)`      | Gregorian rules: /4 yes, /100 no, /400 yes again             |
| `longest_run(items)`      | Length of the longest streak of equal adjacent items         |

Notes:

- `fizzbuzz` returns a list of `n` strings for 1..n. For each value,
  concatenate the words of every rule whose divisor divides it (in rule
  order); if none divide it, use the number itself as a string.
- `to_binary(0)` is `"0"`. Build it with `//` and `%` — the point is the
  algorithm, not the builtin (the tests reject `bin`, `format`, and
  f-string tricks).
- `longest_run` is a loop-invariant exercise: maintain "longest streak seen
  so far" and "current streak". `longest_run([])` is `0`.

```
uni grade 101/a2 --dry    # score without recording
uni grade 101/a2          # record
```
