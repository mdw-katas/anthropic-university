"""Exploration: the __eq__ / __hash__ contract has teeth.

PlainPoint defines neither. ValuePoint defines __eq__ only — and Python
responds by setting its __hash__ to None. Predict the equality results,
and what happens when a ValuePoint is used as a dict key.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-03
"""

PREDICT_PLAIN_EQUAL = None   # PlainPoint(1, 2) == PlainPoint(1, 2)
PREDICT_VALUE_EQUAL = None   # ValuePoint(1, 2) == ValuePoint(1, 2)
PREDICT_KEY_FAILURE = None   # type NAME raised using ValuePoint as a dict key


class PlainPoint:
    def __init__(self, x, y):
        self.x, self.y = x, y


class ValuePoint:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        if not isinstance(other, ValuePoint):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)
    # no __hash__: Python sets it to None because __eq__ is defined


def key_failure_name():
    """Return the type name raised by {ValuePoint(1, 2): 'home'}."""
    try:
        return str({ValuePoint(1, 2): "home"})
    except Exception as caught:
        return type(caught).__name__


if __name__ == "__main__":
    print(f"PlainPoint(1,2) == PlainPoint(1,2): {PlainPoint(1, 2) == PlainPoint(1, 2)}")
    print(f"ValuePoint(1,2) == ValuePoint(1,2): {ValuePoint(1, 2) == ValuePoint(1, 2)}")
    print(f"ValuePoint as dict key raises: {key_failure_name()}")
