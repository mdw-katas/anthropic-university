# Assignment a3 — Functional Tools (build them once, import them forever)

Implement the six functions stubbed in `starter/functional_tools.py` — the
higher-order classics, from bare closures. The test suite parses your source
with `ast` and **rejects any import of `functools` or `itertools`, and any
call to the builtins `map`, `filter`, or `reduce`**. Loops and closures only.

| Function                          | Contract                                                    |
|-----------------------------------|-------------------------------------------------------------|
| `my_map(fn, iterable)`            | List of `fn(x)` for each element, in order                  |
| `my_filter(predicate, iterable)`  | List of elements where `predicate(x)` is truthy, in order   |
| `my_reduce(fn, iterable, initial)` | Fold left: `fn(fn(acc, x1), x2)...`; see notes              |
| `compose(*functions)`             | `compose(f, g, h)(x) == f(g(h(x)))`; `compose()` is identity |
| `memoize(fn)`                     | Wrapper that caches results by positional arguments         |
| `once(fn)`                        | Wrapper that calls `fn` at most once, replaying the result  |

Notes that resolve every ambiguity the tests exercise:

- `my_reduce`'s third parameter defaults to the module-level sentinel
  `_MISSING` (already defined in the starter — Lesson 6 foreshadowed why
  `None` cannot play this role: `None` is a legitimate initial value).
  - Empty iterable, no initial: raise `TypeError`.
  - Empty iterable, initial given: return the initial.
  - Single element, no initial: return it **without calling `fn` at all**
    (a test hands you an exploding `fn` to check).
- `compose` applies right to left (mathematical order). `compose()` with no
  arguments returns an identity function. Single-argument functions only.
- `memoize(fn)`: cache keyed by the positional argument tuple. A probe
  counts calls to the wrapped function: equal arguments must hit the
  underlying function exactly once; different arguments miss separately.
  Two independently memoized functions must never share a cache (your cache
  lives in the closure, not in module or global state).
- `once(fn)`: the first call runs `fn` (forwarding args) and stores the
  result; every later call returns that stored result without calling `fn`,
  regardless of arguments. (Think `sync.Once`, but it also keeps the value.)
- Return values of `memoize`/`once` are ordinary callables. No classes
  required — closures are the point (though a class would also pass; the
  only bans here are the imports and builtin calls listed above).

```
uni grade 102/a3 --dry
uni grade 102/a3
```
