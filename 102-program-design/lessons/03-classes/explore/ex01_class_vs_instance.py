"""Exploration: class attributes are shared; instance attributes are not.

SharedTeam puts its list on the class. SeparateTeam creates one per
instance in __init__. Each scenario builds two teams and adds one member
to each. Predict what each team reports.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-03
"""

PREDICT_SHARED_COUNT = None    # len(team_a.members) in shared_scenario()
PREDICT_SEPARATE_COUNT = None  # len(team_a.members) in separate_scenario()


class SharedTeam:
    members = []  # lives on the CLASS

    def add(self, name):
        self.members.append(name)


class SeparateTeam:
    def __init__(self):
        self.members = []  # lives on the INSTANCE

    def add(self, name):
        self.members.append(name)


def shared_scenario():
    team_a, team_b = SharedTeam(), SharedTeam()
    team_a.add("ada")
    team_b.add("grace")
    return len(team_a.members)


def separate_scenario():
    team_a, team_b = SeparateTeam(), SeparateTeam()
    team_a.add("ada")
    team_b.add("grace")
    return len(team_a.members)


if __name__ == "__main__":
    print(f"shared:   team_a sees {shared_scenario()} member(s)")
    print(f"separate: team_a sees {separate_scenario()} member(s)")
    # SharedTeam.members is polluted for every future instance, too.
