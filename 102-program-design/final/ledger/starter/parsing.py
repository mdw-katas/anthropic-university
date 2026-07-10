"""ledger: text -> model objects. Lazy, and loud about line numbers.

Depends on model only. See README for the full grammar.
"""

import model


class LedgerError(Exception):
    """Base of the parsing failure vocabulary; carries `line_number`."""


class MalformedLineError(LedgerError):
    """A structurally bad line; str() mentions the 1-based line number."""


class AmountError(LedgerError):
    """A bad amount; raised `from` the underlying ValueError."""


def parse_amount(text):
    """Dollars-text to integer cents. "42.50" -> 4250, "-7" -> -700,
    "0.05" -> 5. If '.' appears, exactly two digits follow. Anything
    else -> plain ValueError (this helper knows nothing of files).
    """
    raise NotImplementedError


def parse_ledger(lines):
    """Yield model.Transaction objects from an iterable of text lines.

    A GENERATOR, genuinely lazy: yield each transaction as soon as its
    block completes. Attach 1-based line numbers to every LedgerError;
    chain AmountError `from` the ValueError that parse_amount raised.
    """
    raise NotImplementedError
