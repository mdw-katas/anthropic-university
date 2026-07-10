"""Exploration: except clauses are tried top to bottom; first match wins.

Both classifiers handle int("oops"), which raises ValueError. One lists
the base class Exception FIRST. Predict which handler reports the catch
in each, and whether `except LookupError` catches a KeyError.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-06
"""

PREDICT_BASE_FIRST = None      # classify_base_first("oops")
PREDICT_PRECISE_FIRST = None   # classify_precise_first("oops")
PREDICT_BASE_CATCHES_SUB = None  # True/False: LookupError clause catches KeyError?


def classify_base_first(text):
    try:
        return int(text)
    except Exception:
        return "generic handler"
    except ValueError:
        return "value handler"  # unreachable: the base class got there first


def classify_precise_first(text):
    try:
        return int(text)
    except ValueError:
        return "value handler"
    except Exception:
        return "generic handler"


def lookup_demo():
    """KeyError is a subclass of LookupError. Does the base clause catch it?"""
    try:
        return {"a": 1}["missing"]
    except LookupError:
        return True
    except KeyError:
        return False  # unreachable for the same reason as above


if __name__ == "__main__":
    print(f"base first:    {classify_base_first('oops')!r}")
    print(f"precise first: {classify_precise_first('oops')!r}")
    print(f"LookupError catches KeyError: {lookup_demo()}")
    # Order most-derived first, or the base class swallows everything.
