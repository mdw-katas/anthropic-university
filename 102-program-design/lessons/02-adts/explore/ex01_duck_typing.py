"""Exploration: duck typing auditions every method call at runtime.

drain(container) pops until empty. Predict what it returns for a list,
and what happens when the container is a dict — which HAS a pop method
and a length, but with a different contract.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-02
"""

PREDICT_LIST_DRAIN = None    # drain([1, 2, 3])
PREDICT_DICT_FAILURE = None  # type NAME raised by drain({"a": 1}), e.g. "KeyError"


def drain(container):
    """Pop everything, returning items in the order popped."""
    items = []
    while len(container) > 0:
        items.append(container.pop())
    return items


def dict_failure_name():
    """Return the type name of whatever drain({'a': 1}) raises."""
    try:
        drain({"a": 1})
    except Exception as caught:
        return type(caught).__name__
    return "no exception"


if __name__ == "__main__":
    print(f"drain([1, 2, 3])   = {drain([1, 2, 3])}")
    print(f"drain({{'a': 1}}) raises {dict_failure_name()}")
    print("dict.pop demands a key; the duck had the right shape, wrong contract")
