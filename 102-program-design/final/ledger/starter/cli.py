"""ledger: the imperative shell. Provided free and ungraded — wire-up is
free, logic is not. Usage: python3 cli.py < some.ledger"""

import sys

import model
import parsing
import report


def main():
    try:
        transactions = list(parsing.parse_ledger(sys.stdin))
        rendered = report.balance_report(transactions)
        if rendered:
            print(rendered)
        return 0
    except (parsing.LedgerError, model.UnbalancedError, ValueError) as err:
        print(f"error: {err}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
