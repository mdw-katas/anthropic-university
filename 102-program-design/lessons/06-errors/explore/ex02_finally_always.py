"""Exploration: finally runs no matter HOW control leaves the try.

Each scenario appends breadcrumbs to a list. Predict the full breadcrumb
trail — pay attention to whether "cleanup" appears, and where.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-06
"""

PREDICT_RETURN_TRAIL = None     # trail from return_scenario(), e.g. ["a", "b"]
PREDICT_EXCEPTION_TRAIL = None  # trail from exception_scenario()
PREDICT_EXCEPTION_ESCAPED = None  # True/False: did the ValueError still propagate?


def return_scenario():
    """The try block RETURNS. Does finally run before the caller gets it?"""
    trail = []

    def work():
        try:
            trail.append("working")
            return "result"
        finally:
            trail.append("cleanup")

    work()
    return trail


def exception_scenario():
    """The try block RAISES, and nothing here catches it."""
    trail = []
    escaped = False

    def work():
        try:
            trail.append("working")
            raise ValueError("boom")
        finally:
            trail.append("cleanup")

    try:
        work()
    except ValueError:
        escaped = True
    trail.append("escaped" if escaped else "swallowed")
    return trail


if __name__ == "__main__":
    print(f"return scenario:    {return_scenario()}")
    print(f"exception scenario: {exception_scenario()}")
    # finally ran in both - after the return was staged, before delivery.
