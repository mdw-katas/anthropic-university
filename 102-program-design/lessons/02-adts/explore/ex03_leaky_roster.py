"""Exploration: rep exposure — returning internal state hands out a crowbar.

LeakyRoster.members() returns its internal list. SealedRoster returns a
copy. The same rude client mutates whatever it is given. Predict what
each roster reports afterward.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-02
"""

PREDICT_LEAKY_AFTER = None   # leaky.members() after the rude client runs
PREDICT_SEALED_AFTER = None  # sealed.members() after the rude client runs


class LeakyRoster:
    def __init__(self, names):
        self._names = list(names)

    def add(self, name):
        self._names.append(name)

    def members(self):
        return self._names  # rep exposure: this IS the internal list


class SealedRoster:
    def __init__(self, names):
        self._names = list(names)

    def add(self, name):
        self._names.append(name)

    def members(self):
        return list(self._names)  # defensive copy


def rude_client(roster):
    """Mutates whatever members() hands back. Never calls add()."""
    listing = roster.members()
    listing.append("intruder")


def roster_after(roster_class):
    roster = roster_class(["ada", "grace"])
    rude_client(roster)
    return roster.members()


if __name__ == "__main__":
    print(f"LeakyRoster after rude client:  {roster_after(LeakyRoster)}")
    print(f"SealedRoster after rude client: {roster_after(SealedRoster)}")
