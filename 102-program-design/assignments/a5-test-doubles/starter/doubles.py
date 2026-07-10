"""Assignment a5: the doubles taxonomy, hand-built, then used in anger.

retry must wait via the INJECTED clock only — the tests booby-trap
time.sleep.
"""


class FakeClock:
    """A clock that moves only when told to.

    time() -> current fake time (starts at `start`).
    sleep(seconds) -> advance time; append seconds to the public `sleeps`
    list; ValueError if seconds < 0.
    """

    def __init__(self, start=0.0):
        raise NotImplementedError

    def time(self):
        raise NotImplementedError

    def sleep(self, seconds):
        raise NotImplementedError


class Spy:
    """A callable that records the conversation.

    Each call appends (args, kwargs) to the public `calls` list and
    returns the canned `result`. `call_count` is a property.
    """

    def __init__(self, result=None):
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def call_count(self):
        raise NotImplementedError


class StubSequence:
    """A callable with a script: one outcome per call, in order.

    An outcome that is an exception INSTANCE is raised, not returned.
    Calling past the end of the script raises AssertionError.
    """

    def __init__(self, values):
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        raise NotImplementedError


def retry(action, attempts, delay, clock):
    """Call action() up to `attempts` times, backing off between failures.

    Success returns immediately. Failure i (1-based, i < attempts) is
    followed by clock.sleep(delay * 2**(i-1)). The final failure sleeps
    not at all and re-raises. attempts < 1 -> ValueError, action uncalled.
    """
    raise NotImplementedError
