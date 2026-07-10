# Assignment a5 — Build Your Own Test Doubles

Implement the three doubles and one production function stubbed in
`starter/doubles.py`. The finale is self-referential in the best way: the
tests use **your** fake clock and **your** stub to test **your** retry loop
— and a booby-trapped `time.sleep` makes sure nothing in the building
actually sleeps. The suite finishes in milliseconds while testing seconds
of "waiting"; that is the entire sales pitch for injected clocks.

| Piece                  | Contract                                                        |
|------------------------|-----------------------------------------------------------------|
| `FakeClock(start=0.0)` | `time()` reports now; `sleep(s)` advances now and records `s`   |
| `Spy(result=None)`     | Callable; records every call; returns `result` each time        |
| `StubSequence(values)` | Callable; returns/raises the next scripted value per call       |
| `retry(action, attempts, delay, clock)` | Call `action()` up to `attempts` times with backoff; see below |

Notes that resolve every ambiguity the tests exercise:

- **`FakeClock`**: `time()` returns the current fake time (starts at
  `start`). `sleep(seconds)` advances it by `seconds` and appends `seconds`
  to a public `sleeps` list. `sleep` raises `ValueError` for negative
  seconds, leaving the time (and the list) unchanged. No real time is
  ever consulted.
- **`Spy`**: each call appends `(args, kwargs)` — a tuple and a dict — to a
  public `calls` list, then returns the canned `result`. Expose
  `call_count` as a property equal to `len(calls)`.
- **`StubSequence`**: constructed with a list of scripted outcomes,
  returned one per call, in order. If the next outcome `isinstance` of
  `BaseException`, it is **raised** instead of returned. Calling an
  exhausted stub raises `AssertionError` (a test double that runs off its
  script should fail the test, loudly).
- **`retry`**: calls `action()` (no arguments). On success, returns the
  value immediately. On an `Exception`, sleeps via `clock.sleep(...)` and
  tries again — the waits form exponential backoff: `delay`, `delay * 2`,
  `delay * 4`, ... After the final attempt fails there is **no sleep**;
  the last exception is re-raised (`attempts == 3` means at most 3 calls
  and at most 2 sleeps). `attempts < 1` raises `ValueError` without
  calling `action`. `retry` must use ONLY the injected clock — the test
  suite replaces `time.sleep` with a tripwire for the duration.
- This is the one module where catching broad (`except Exception`) is
  legitimate: retry's contract is "try again on any failure," and it
  re-raises when it gives up. Know why it is right here and wrong in a4.

```
uni grade 102/a5 --dry
uni grade 102/a5
```
