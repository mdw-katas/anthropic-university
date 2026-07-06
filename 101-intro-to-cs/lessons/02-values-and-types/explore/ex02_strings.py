"""Exploration: slicing is half-open, strings are immutable.

Index the word first:  a-b-s-t-r-a-c-t-i-o-n
                       0 1 2 3 4 5 6 7 8 9 10
Predict, run, then: uni grade 101/explore-02
"""

WORD = "abstraction"

PREDICT_SLICE = None    # WORD[2:6]
PREDICT_PREFIX = None   # WORD[:3]
PREDICT_SUFFIX = None   # WORD[-4:]
PREDICT_AFTER_UPPER = None  # WORD itself, after WORD.upper() is called


if __name__ == "__main__":
    print(f"WORD[2:6]  = {WORD[2:6]!r}")
    print(f"WORD[:3]   = {WORD[:3]!r}")
    print(f"WORD[-4:]  = {WORD[-4:]!r}")
    WORD.upper()
    print(f"after WORD.upper(), WORD = {WORD!r}")
