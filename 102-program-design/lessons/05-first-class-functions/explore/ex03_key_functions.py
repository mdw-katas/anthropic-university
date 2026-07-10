"""Exploration: key functions inject policy into a sorting mechanism.

WORDS is sorted three ways. Predict each result — the default sort is
the one most likely to surprise (capital letters sort before ALL
lowercase letters, because ordinals).

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-05
"""

WORDS = ["banana", "Cherry", "apple"]

PREDICT_DEFAULT = None      # sorted(WORDS)
PREDICT_CASEFOLDED = None   # sorted(WORDS, key=str.lower)
PREDICT_BY_LENGTH = None    # sorted(WORDS, key=len)  (ties keep input order)


if __name__ == "__main__":
    print(f"sorted(WORDS)                 = {sorted(WORDS)}")
    print(f"sorted(WORDS, key=str.lower)  = {sorted(WORDS, key=str.lower)}")
    print(f"sorted(WORDS, key=len)        = {sorted(WORDS, key=len)}")
    # Python's sort is stable: equal keys preserve their original order.
