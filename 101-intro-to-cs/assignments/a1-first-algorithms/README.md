# Assignment a1 — First Algorithms

Implement the five functions stubbed in `starter/algorithms.py`. The test
suite in `tests/` is the complete specification — read it. This is
red-green-refactor: everything starts red.

## The functions

| Function                        | Contract                                                    |
|---------------------------------|-------------------------------------------------------------|
| `gcd(a, b)`                     | Greatest common divisor via Euclid; `gcd(n, 0) == n`        |
| `is_prime(n)`                   | True iff `n` is prime; anything below 2 is not prime        |
| `collatz_length(n)`             | Steps for `n` to reach 1 under the Collatz rules            |
| `linear_search(items, target)`  | Index of `target` in `items`, or `-1` if absent             |
| `binary_search(items, target)`  | Same contract, but `items` is sorted — exploit that         |

## Rules of engagement

- Python standard library only; no imports needed at all, in fact.
- `binary_search` must actually be binary: one test hands you a large list
  that counts how many elements you touch, and a linear scan will fail it.
- Iterate: edit `starter/algorithms.py`, then re-run the grader.

## Grading

```
uni grade 101/a1          # run, score, and record
uni grade 101/a1 --dry    # run and score without recording
```

Score is the fraction of tests passing; the pass bar is 80%, and only your
best score counts. Aim for 100% anyway — you know you want to.
