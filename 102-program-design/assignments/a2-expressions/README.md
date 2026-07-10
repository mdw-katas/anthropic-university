# Assignment a2 — Expressions (dispatch or die)

Implement the five node classes stubbed in `starter/expressions.py`. Together
they form arithmetic expression trees:

```python
# 2 * (x + -3)
tree = Mul(Literal(2), Add(Var("x"), Neg(Literal(3))))
tree.evaluate({"x": 10})   # 14
tree.render()              # "(2 * (x + (-3)))"
tree.variables()           # {"x"}
```

| Class            | `evaluate(env)`                       | `render()`                  | `variables()`        |
|------------------|---------------------------------------|-----------------------------|----------------------|
| `Literal(value)` | `value`                               | `str(value)`                | `set()`              |
| `Var(name)`      | `env[name]`; `NameError` if missing   | `name`                      | `{name}`             |
| `Add(left, right)` | sum of children                     | `"(L + R)"`                 | union of children    |
| `Mul(left, right)` | product of children                 | `"(L * R)"`                 | union of children    |
| `Neg(inner)`     | negation of child                     | `"(-X)"`                    | child's              |

Notes that resolve every ambiguity the tests exercise:

- `render()` is fully parenthesized, exactly as shown: every `Add`, `Mul`,
  and `Neg` contributes one pair of parentheses; `Literal` and `Var`
  contribute none. `L`, `R`, `X` above stand for the child's own `render()`.
  One space around `+` and `*`; none after the unary minus.
- `Var.evaluate` raises `NameError` whose message contains the variable's
  name, when the name is absent from `env`.
- `variables()` returns a `set` of variable name strings.
- **The twist (Lesson 4, section 5)**: this is an exercise in dynamic
  dispatch, and the tests enforce it two ways.
  1. AST inspection rejects your module if it calls `isinstance` or
     `type`, or uses a `match` statement. No type-switching.
  2. The suite defines its own node class — one you have never seen — and
     plants it as a child inside YOUR `Add`. If your composite nodes talk
     to their children only through `evaluate` / `render` / `variables`,
     you will pass without knowing it exists. That is the whole point:
     polymorphic code is open to types written after it.
- Design consequence you can rely on: composite nodes never inspect their
  children — they ask. `Add.evaluate(env)` is one line.

```
uni grade 102/a2 --dry
uni grade 102/a2
```
