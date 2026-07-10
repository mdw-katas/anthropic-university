"""ledger: the domain model. Imports nothing; knows nothing but money.

Rep invariants live here, enforced at construction (Lesson 3).
"""


class UnbalancedError(ValueError):
    """A transaction whose postings do not sum to zero cents."""


class Posting:
    """One movement of money: `cents` into (or out of, if negative)
    `account`. A value object: equality is field-by-field.
    """

    def __init__(self, account, cents):
        raise NotImplementedError

    def __eq__(self, other):
        """Value equality against another Posting; NotImplemented otherwise."""
        raise NotImplementedError


class Transaction:
    """A dated, described group of postings that MUST balance.

    Rep invariants (constructor-enforced):
      - at least 2 postings          -> else ValueError
      - postings sum to exactly 0    -> else UnbalancedError naming the date
    `postings` is stored as a tuple snapshot of whatever iterable arrives.
    """

    def __init__(self, date, description, postings):
        raise NotImplementedError
