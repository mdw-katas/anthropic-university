# Assignment a4 — Word Stats

A small text-analysis toolkit built on Lesson 6's collections. Implement the
five functions stubbed in `starter/word_stats.py`; the tests are the spec.

| Function                    | Contract                                                  |
|-----------------------------|-----------------------------------------------------------|
| `normalize_words(text)`     | Lowercased words, punctuation stripped, in order          |
| `word_frequencies(text)`    | Dict of word → count over the normalized words            |
| `top_n(frequencies, n)`     | The `n` (word, count) pairs, highest first; ties A→Z      |
| `bigrams(words)`            | Adjacent pairs: `["a","b","c"]` → `[("a","b"),("b","c")]` |
| `vocabulary_richness(text)` | Distinct words ÷ total words, as a float; `0.0` if empty  |

Notes:

- "Punctuation stripped" means stripped from the *edges* of each
  whitespace-separated token (`"end."` → `"end"`, `"don't"` stays
  `"don't"`). Tokens that were pure punctuation vanish.
  `string.punctuation` and `str.strip` make friends here.
- `top_n` must be deterministic: sort by count descending, then
  alphabetically. Asking for more than exists returns what exists.
- The counting idiom (`counts.get(word, 0) + 1`) or `collections.Counter`
  are both fair game — stdlib is allowed; the *shape* is what's graded.

```
uni grade 101/a4 --dry
uni grade 101/a4
```
