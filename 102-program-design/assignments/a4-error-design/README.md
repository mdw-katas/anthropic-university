# Assignment a4 — Designed Failure

Implement the exception hierarchy, parser, and Result type stubbed in
`starter/outcome.py`. The theme is Lesson 6 made concrete: every failure
below is a **designed outcome** — typed, informative, and raised at the
right abstraction level. The test suite parses your source and **rejects
any bare `except:` and any `except Exception` / `except BaseException`** —
you will catch precisely, or you will catch an F.

## The exception hierarchy

```
ConfigError(Exception)
├── MalformedLineError    # line has no "=", or an empty key
├── DuplicateKeyError     # same key assigned twice
└── BadValueError         # value has the wrong form (parse_port)
```

`MalformedLineError` and `DuplicateKeyError` carry a `line_number`
attribute (1-based), and their `str()` must mention that number — an error
message that names its line is worth a debugger session.

## The functions

| Function                        | Contract                                                       |
|---------------------------------|----------------------------------------------------------------|
| `parse_config(text)`            | Parse `key = value` lines into a dict; see rules below         |
| `parse_port(text)`              | `int` in 1..65535, else `BadValueError`; see chaining note     |
| `try_call(exceptions, fn, *args)` | `Ok(fn(*args))`, or `Err(caught)` if it raises one of `exceptions` |
| `partition(results)`            | Split an iterable of Results into `(values, errors)` lists     |

`parse_config` rules, in order, per line (numbered from 1):

1. Strip the line. Skip it if empty or starting with `#`.
2. No `=` anywhere, or nothing but whitespace left of the first `=`:
   raise `MalformedLineError` with that line number.
3. Split on the FIRST `=`; strip both sides. The value may legally be
   empty, and keeps its internal spaces (`greeting = hello world`).
4. Key already seen: raise `DuplicateKeyError` with the line number of the
   second occurrence.

`parse_port` must translate at the boundary (Lesson 6, section 3): callers
see `BadValueError`, never `ValueError` — but chain it with
`raise ... from`, so the test finds `isinstance(err.__cause__, ValueError)`
when the text is not numeric. A numeric value outside 1..65535 is also a
`BadValueError` (no cause required).

## The Result type

| Expression            | `Ok(v)`               | `Err(e)`                  |
|-----------------------|-----------------------|---------------------------|
| `.is_ok()`            | `True`                | `False`                   |
| `.value` / `.error`   | `v` / (absent)        | (absent) / `e`            |
| `.map(fn)`            | `Ok(fn(v))`           | the same `Err`, fn UNCALLED |
| `.and_then(fn)`       | `fn(v)` (a Result)    | the same `Err`, fn UNCALLED |
| `.unwrap_or(default)` | `v`                   | `default`                 |

The "fn UNCALLED" cells are tested with exploding functions. `try_call`'s
`exceptions` parameter is whatever `except` accepts — one type or a tuple —
and exceptions NOT listed must propagate untouched (that is the whole
point: the caller names the failures it can handle).

```
uni grade 102/a4 --dry
uni grade 102/a4
```
