"""Assignment a4: failure as a designed outcome.

The tests reject bare `except:` and `except Exception`/`BaseException`
anywhere in this module. Catch precisely.
"""


class ConfigError(Exception):
    """Base of this module's failure vocabulary."""


class MalformedLineError(ConfigError):
    """A config line with no '=' or an empty key.

    Carries a 1-based `line_number` attribute; str() mentions it.
    """

    def __init__(self, line_number):
        raise NotImplementedError


class DuplicateKeyError(ConfigError):
    """The same key assigned twice.

    Carries a 1-based `line_number` attribute (of the SECOND occurrence);
    str() mentions it.
    """

    def __init__(self, key, line_number):
        raise NotImplementedError


class BadValueError(ConfigError):
    """A value with the wrong form (e.g. a non-numeric port)."""


def parse_config(text):
    """Parse `key = value` lines into a dict. See README for the rules."""
    raise NotImplementedError


def parse_port(text):
    """Return the port as an int in 1..65535.

    Non-numeric text -> BadValueError chained (`raise ... from`) to the
    underlying ValueError. Out-of-range numbers -> BadValueError.
    """
    raise NotImplementedError


class Ok:
    """A successful Result carrying .value."""

    def __init__(self, value):
        raise NotImplementedError

    def is_ok(self):
        raise NotImplementedError

    def map(self, fn):
        raise NotImplementedError

    def and_then(self, fn):
        raise NotImplementedError

    def unwrap_or(self, default):
        raise NotImplementedError


class Err:
    """A failed Result carrying .error."""

    def __init__(self, error):
        raise NotImplementedError

    def is_ok(self):
        raise NotImplementedError

    def map(self, fn):
        raise NotImplementedError

    def and_then(self, fn):
        raise NotImplementedError

    def unwrap_or(self, default):
        raise NotImplementedError


def try_call(exceptions, fn, *args):
    """Ok(fn(*args)), or Err(the exception) if it raises one of
    `exceptions` (a type or tuple of types). Anything else propagates."""
    raise NotImplementedError


def partition(results):
    """Split an iterable of Results into ([ok values...], [errors...])."""
    raise NotImplementedError
