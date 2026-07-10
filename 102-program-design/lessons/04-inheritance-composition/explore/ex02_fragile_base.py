"""Exploration: the fragile base class, live and in person.

LoggingDict subclasses dict and overrides __setitem__ to log every write.
scenario() performs three writes by three different routes. Predict how
many actually get logged — then predict the same for the composed version.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-04
"""

PREDICT_SUBCLASS_LOGGED = None  # len(log) for the dict SUBCLASS
PREDICT_COMPOSED_LOGGED = None  # len(log) for the COMPOSED wrapper


class LoggingDict(dict):
    def __init__(self, *args, **kwargs):
        self.log = []
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        self.log.append(key)
        super().__setitem__(key, value)


class ComposedLoggingDict:
    """HAS a dict. Every write must come through the front door."""

    def __init__(self, **kwargs):
        self.log = []
        self._store = {}
        self.update(**kwargs)

    def __setitem__(self, key, value):
        self.log.append(key)
        self._store[key] = value

    def update(self, **kwargs):
        for key, value in kwargs.items():
            self[key] = value


def subclass_scenario():
    d = LoggingDict(a=1)   # write 1: the constructor
    d["b"] = 2             # write 2: plain assignment
    d.update(c=3)          # write 3: update()
    return len(d.log)


def composed_scenario():
    d = ComposedLoggingDict(a=1)
    d["b"] = 2
    d.update(c=3)
    return len(d.log)


if __name__ == "__main__":
    print(f"subclass logged {subclass_scenario()} of 3 writes")
    print(f"composed logged {composed_scenario()} of 3 writes")
    # dict's C internals write past your override; the wrapper cannot be bypassed.
