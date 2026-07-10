"""Exploration: a spy records the conversation so the test can assert on it.

notify_overdue sends one reminder per overdue member, skipping anyone
who opted out. The spy stands in for the real send function. Predict
exactly what it records.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-07
"""

PREDICT_CALL_COUNT = None  # len(spy.calls) after the scenario
PREDICT_FIRST_CALL = None  # spy.calls[0], e.g. ("bob", "pay up")

MEMBERS = [
    {"name": "ada", "overdue": True, "opted_out": False},
    {"name": "bob", "overdue": True, "opted_out": True},
    {"name": "cyd", "overdue": False, "opted_out": False},
    {"name": "dee", "overdue": True, "opted_out": False},
]


class SendSpy:
    """Pretends to send; actually just takes notes."""

    def __init__(self):
        self.calls = []

    def __call__(self, name, message):
        self.calls.append((name, message))


def notify_overdue(members, send):
    for member in members:
        if member["overdue"] and not member["opted_out"]:
            send(member["name"], "your library book is overdue")


def scenario():
    spy = SendSpy()
    notify_overdue(MEMBERS, spy)
    return spy


if __name__ == "__main__":
    spy = scenario()
    print(f"calls recorded: {len(spy.calls)}")
    for call in spy.calls:
        print(f"  send{call}")
