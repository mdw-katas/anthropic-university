# Final Project — `ledger`, a Plain-Text Double-Entry Ledger

Build the engine of a plain-text accounting tool, in the format that tools
like `ledger` and `hledger` made famous (simplified). Money moves between
named accounts; every transaction must balance to zero; the tool reports
account balances:

```
; my-money.ledger                        $ python3 starter/cli.py < my-money.ledger
2026-07-01 Opening balance               assets:checking    957.50
    assets:checking     1000.00          equity:opening   -1000.00
    equity:opening                       expenses:food       42.50

2026-07-03 Groceries
    expenses:food         42.50
    assets:checking
```

This is the whole course in one program, in exactly the shape Lesson 9
drew: `model.py` (invariants — Lessons 1-3), `parsing.py` (a designed
exception hierarchy and a lazy generator — Lessons 6, 8), `report.py`
(pure functions — Lessons 5, 7), and a free, ungraded `cli.py` on top.
`model` imports nothing. Keep it that way.

## The format

- Amounts are written in dollars (`1000.00`, `-7`, `0.05`) and stored as
  **integer cents** (CS 101 Lesson 2 explained why floats don't get to
  touch money). Optional leading `-`; if a `.` appears, exactly two digits
  follow it. Nothing else — no `,`, no `$`, no whitespace inside.
- A **transaction** is a date line followed by indented posting lines:
  - Date line (not indented): `YYYY-MM-DD description` — a 10-character
    date token (digits and dashes in the right places), then a non-empty
    description.
  - Posting line (indented with spaces/tabs): `account` and optionally an
    amount, whitespace-separated. Accounts contain no spaces
    (`expenses:food`). More than two tokens is malformed.
- At most ONE posting per transaction may omit its amount: it receives
  whatever balances the transaction. A second elided posting is malformed.
- Blank lines and comment lines (first non-blank char `;` or `#`) end the
  current transaction, if one is open.
- An indented line with no transaction open is malformed.

## `model.py`

| Name                                   | Contract                                              |
|----------------------------------------|-------------------------------------------------------|
| `Posting(account, cents)`              | Value object: `.account`, `.cents`, value `__eq__`    |
| `UnbalancedError(ValueError)`          | Raised by Transaction's constructor                   |
| `Transaction(date, description, postings)` | Validates and stores; see invariants               |

Transaction's rep invariants, enforced in the constructor (Lesson 3):
postings sum to exactly 0 cents (else `UnbalancedError` mentioning the
date) and there are at least 2 of them (else plain `ValueError`).
`postings` is stored as a **tuple** — snapshot the iterable you were
given, and clients can't mutate what they can't reach. `Posting.__eq__`
returns `NotImplemented` for non-Postings.

## `parsing.py`

| Name                          | Contract                                                    |
|-------------------------------|-------------------------------------------------------------|
| `LedgerError(Exception)`      | Base; carries a 1-based `line_number` attribute             |
| `MalformedLineError(LedgerError)` | Structural problems; `str()` mentions the line number   |
| `AmountError(LedgerError)`    | A bad amount; chained `from` the underlying `ValueError`    |
| `parse_amount(text)`          | Dollars-text to int cents; raises plain `ValueError`        |
| `parse_ledger(lines)`         | **Generator** of Transactions from an iterable of lines    |

`parse_amount` is a pure helper with no knowledge of files or line
numbers — that is why it raises plain `ValueError`. `parse_ledger`
translates at the boundary (Lesson 6): a bad amount on line 7 becomes
`AmountError` with `line_number == 7`, chained with `raise ... from`.

`parse_ledger` must be **genuinely lazy** (Lesson 8): each transaction is
yielded as soon as its block is complete, and a probing test counts how
many lines you consumed to produce the first one. (You may read at most
one line past the end of a block — the line that told you it ended.)
Model-level failures (`UnbalancedError`, too-few-postings) propagate
as they are; they already speak for themselves.

## `report.py`

| Name                        | Contract                                                        |
|-----------------------------|-----------------------------------------------------------------|
| `format_cents(cents)`       | `4250 -> "42.50"`, `-5 -> "-0.05"`; always two decimals         |
| `balances(transactions)`    | Dict: account -> summed cents, every account that appears       |
| `balance_report(transactions)` | One line per account, sorted; fixed-width columns            |

`balance_report` formatting: account name left-justified to the longest
account name, two spaces, amount right-justified to the widest formatted
amount. No trailing whitespace would survive that spec — the amount column
is exactly as wide as its widest member. Lines joined with `"\n"`, no
trailing newline. (Yes: fixed-width columns. The registrar has a type.)

## Invariants the suite checks algebraically

- **Conservation**: for any parsed ledger, `sum(balances(...).values())`
  is exactly 0. Double-entry bookkeeping is a conservation law; if this
  fails, money leaked somewhere in YOUR code, and nowhere else.
- **Round-trip**: `parse_amount(format_cents(n)) == n` across a spread of
  values, positive and negative.

## Grading

`cli.py` is provided and ungraded — wire-up is free, logic is not. 29
tests. Pass bar 80%, best score kept — but this is the final, and the
final of a course about *doing design on purpose*. Go get 100%.

```
uni grade 102/final --dry
uni grade 102/final
```
