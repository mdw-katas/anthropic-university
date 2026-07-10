"""Exploration: translate exceptions at abstraction boundaries with
`raise ... from`, and the original survives as __cause__.

load_port hides its parsing strategy behind ConfigError. Predict what a
caller catches, and what type hangs off the caught exception's __cause__.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-06
"""

PREDICT_CAUGHT_TYPE = None  # type NAME a caller of load_port("http") catches
PREDICT_CAUSE_TYPE = None   # type NAME of caught.__cause__


class ConfigError(Exception):
    """The failure vocabulary of the config layer."""


def load_port(text):
    try:
        return int(text)
    except ValueError as err:
        raise ConfigError(f"port must be an integer, got {text!r}") from err


def caught_and_cause():
    """Return (caught type name, cause type name) for load_port('http')."""
    try:
        load_port("http")
    except Exception as caught:
        return type(caught).__name__, type(caught.__cause__).__name__
    return "no exception", "no cause"


if __name__ == "__main__":
    caught, cause = caught_and_cause()
    print(f"caller catches:      {caught}")
    print(f"caught.__cause__ is: {cause}")
    # The traceback prints both stories, joined by
    # "The above exception was the direct cause of the following exception".
