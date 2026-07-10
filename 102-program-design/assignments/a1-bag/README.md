# Assignment a1 — A Bag ADT (graded on your invariant, not just your answers)

Implement the `Bag` (multiset) class stubbed in `starter/bag.py`: an
unordered collection where elements may appear more than once. This is your
first class graded as an ADT: several tests never look at your answers —
they look at your **copies**, your **equality**, and whether your
representation invariant holds up under abuse.

| Operation             | Contract                                                     |
|-----------------------|--------------------------------------------------------------|
| `Bag(iterable=())`    | New bag containing the iterable's elements                   |
| `add(item, count=1)`  | Add `count` copies; `ValueError` if `count < 1`              |
| `remove(item, count=1)` | Remove `count` copies; `ValueError` if `count < 1` or the bag holds fewer than `count` of `item` |
| `count(item)`         | How many of `item` the bag holds (0 if absent)               |
| `len(bag)`            | Total elements, counting multiplicity                        |
| `item in bag`         | True iff `count(item) > 0`                                   |
| `distinct()`          | Sorted list of the distinct elements, freshly built per call |
| `most_common(k)`      | First `k` `(item, count)` pairs: count descending, ties by item ascending |
| `bag_a == bag_b`      | Value equality: same elements with same counts               |

Notes that resolve every ambiguity the tests exercise:

- **Rep invariant**: no element is stored with a count of zero or less.
  Behaviorally: after removing the last copy of `"x"`, `"x" in bag` is
  False and `distinct()` omits it. Establish the invariant in the
  constructor, preserve it in every method.
- **Defensive copies** (Lesson 2): the constructor must snapshot its
  argument — mutating the original iterable afterward must not affect the
  bag — and mutating a list returned by `distinct()` or `most_common(k)`
  must not affect the bag either.
- **Equality**: field-by-field over the counts, order of insertion
  irrelevant. Comparing a `Bag` to a non-Bag returns `NotImplemented` from
  `__eq__` (so `==` yields False rather than crashing). Because bags are
  mutable, do NOT define `__hash__` — the tests confirm your bags are
  unhashable, exactly as Lesson 3's eq/hash contract demands.
- **`most_common(k)`**: `k` larger than the number of distinct elements
  returns all of them; `k == 0` returns `[]`. Test elements are strings, so
  "ties by item ascending" is plain string order.
- A failed `remove` must leave the bag completely unchanged (it is not
  allowed to remove 2 of 3 requested copies and then complain).
- **The ban**: the test suite parses your source and rejects any import of
  `collections` — no `Counter`, no `defaultdict`. A plain dict and your own
  hands. You will import `Counter` with a clear conscience for the rest of
  your life; today you earn it.

```
uni grade 102/a1 --dry
uni grade 102/a1
```
