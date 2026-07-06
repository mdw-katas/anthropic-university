"""Exploration: read the crash before you run it.

outer() calls middle() calls inner(). Something below will raise.
Predict the exception's type name and WHICH function's body raises it
(the innermost frame — the bottom of the traceback). Run, then:
uni grade 101/explore-07
"""

PREDICT_EXCEPTION_TYPE = None   # e.g. "ValueError" (a string)
PREDICT_RAISING_FUNCTION = None  # "outer", "middle", or "inner"


def outer():
    return middle([])


def middle(rows):
    return inner(sum(rows), len(rows))


def inner(total, count):
    return total / count


def observe_crash():
    try:
        outer()
    except Exception as caught:
        trace = caught.__traceback__
        while trace.tb_next is not None:
            trace = trace.tb_next
        return type(caught).__name__, trace.tb_frame.f_code.co_name
    return None, None


if __name__ == "__main__":
    exception_type, function = observe_crash()
    print(f"exception: {exception_type} raised in {function}()")
