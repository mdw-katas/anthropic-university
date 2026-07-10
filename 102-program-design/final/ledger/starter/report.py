"""ledger: model objects -> text for humans. Pure functions only.

Depends on model only (and in truth, only on duck-typed attributes).
"""


def format_cents(cents):
    """4250 -> "42.50"; -5 -> "-0.05"; 0 -> "0.00". Two decimals, always."""
    raise NotImplementedError


def balances(transactions):
    """Dict of account -> summed cents, for every account that appears
    in any posting (even if its total is zero)."""
    raise NotImplementedError


def balance_report(transactions):
    """One line per account, sorted by account name.

    Account left-justified to the longest account name, two spaces,
    formatted amount right-justified to the widest amount. Lines joined
    with "\\n", no trailing newline. Empty input -> "".
    """
    raise NotImplementedError
