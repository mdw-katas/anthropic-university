# Assignment a5 — Stack Calculator

Build a stack, then put it to work twice. Implement everything stubbed in
`starter/stack_calc.py`. This assignment foreshadows CS 201 (the data
structure) and CS 410 (evaluation) — and echoes Lesson 5: an explicit stack
is what iteration uses where recursion would have used the call stack.

| Piece                       | Contract                                                   |
|-----------------------------|------------------------------------------------------------|
| `class Stack`               | `push`, `pop`, `peek`, `is_empty`, `size` — LIFO           |
| `tokenize(expression)`      | `"3 4 +"` → `["3", "4", "+"]` (whitespace splitting)       |
| `evaluate_rpn(tokens)`      | Evaluate Reverse Polish Notation with `+ - * /`            |
| `balanced(text)`            | Are `()[]{}` properly nested? Uses your Stack              |

Notes:

- `pop`/`peek` on an empty stack raise `IndexError` — an empty stack has
  nothing to say, and saying so loudly beats returning None quietly.
- RPN: operands push; an operator pops the top TWO values (the first pop is
  the RIGHT operand — order matters for `-` and `/`), applies, pushes the
  result. `["3", "4", "-"]` is 3 − 4 = −1. Division is `/` (true division).
  Numbers may be negative ("-3") or have decimal points.
- A malformed RPN expression (operator without two operands, or leftover
  values at the end) raises `ValueError`.
- `balanced` ignores every character except the six brackets:
  `"f(x[i]) { }"` → True; `"([)]"` → False.

```
uni grade 101/a5 --dry
uni grade 101/a5
```
