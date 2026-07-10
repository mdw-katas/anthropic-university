"""Exploration: double-underscore "privacy" is name mangling, not a wall.

Vault stores its combination in __combination. Predict what a direct
attribute read raises — and then predict whether the documented mangled
name gets straight through the fence.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-03
"""

PREDICT_DIRECT_FAILURE = None  # type NAME raised by vault.__combination
PREDICT_MANGLED_VALUE = None   # value of vault._Vault__combination


class Vault:
    def __init__(self):
        self.__combination = "13-31-42"

    def open_with(self, attempt):
        return attempt == self.__combination


def direct_failure_name():
    """Return the type name raised by reading vault.__combination."""
    vault = Vault()
    try:
        return vault.__combination
    except Exception as caught:
        return type(caught).__name__


def mangled_read():
    """Read the combination through the documented mangled name."""
    vault = Vault()
    return vault._Vault__combination


if __name__ == "__main__":
    print(f"vault.__combination raises:   {direct_failure_name()}")
    print(f"vault._Vault__combination is: {mangled_read()!r}")
    print("mangling prevents subclass collisions; it does not keep secrets")
