"""Exploration: what is __name__, and when?

NAME below is captured at import time. The grader IMPORTS this module;
running the file executes it as a script. Predict both. Run, then:
uni grade 101/explore-07
"""

NAME = __name__

PREDICT_NAME_WHEN_IMPORTED = None  # NAME as the test suite sees it (a string)
PREDICT_NAME_WHEN_RUN = None       # __name__ when you run this file directly


if __name__ == "__main__":
    print(f"__name__ right now = {__name__!r}")
    print("(when the grader imports this module, NAME will differ — that is the point)")
